# Computational Geometry

# 21.0 Introduction

It is a safe bet that more computer cycles are expended on the formulas of computational geometry than on all other uses of computers put together. We include not just the computer’s nominal CPU, of course, but also those other other, often vastly more powerful, CPUs hidden in the computer’s graphics chipset, and in all the video entertainment and high-definition television boxes in the world.

Indeed, computational geometry, and the broader fields of computer graphics and computer vision in which it is embedded, have become central areas of computer science, supporting a huge industrial base of applied work and employment for computer scientists and program developers at all professional levels. It is impossible for us to do justice to this colossus in a single chapter. Yet, there are a number of elementary techniques from the field that ought to be in the repertory of any practicing computational scientist.

In this chapter we will build a body of methods sufficient to construct efficient Delaunay triangulations in two dimensions, and to use such triangulations for interpolating functions of two variables on an irregular grid, and other applications. In getting to this goal (and a bit beyond it) we will allow ourselves to be diverted into various other interesting, and often useful, topics, including:

- tree data structures for sets of points   
nearest-neighbor problems much about lines, triangles, and polygons spheres in $n$ dimensions, and rotation matrices Voronoi and all that convex hulls minimum spanning trees   
- finding intersecting objects

and more.

In the spirit of full disclosure, we must mention that our treatment of some of the most interesting topics in the above list will be restricted to the two-dimensional case, even when the three-dimensional case may be equally relevant to computational science. The reason is simply one of space on the page. Three-dimensional algorithms are often more complex, have more special cases that must be treated, and generally result in codes that are too long for us to include. We have struggled to condense working, reasonably efficient, two-dimensional codes to an appropriate size for this chapter. You will be able to use these for two-dimensional problems, or you can mine them for understanding before seeking out three-dimensional solutions in the references.

An additional disclosure relates to our use of floating-point arithmetic, and our treatment of special cases of “exact” equality. Since floating-point numbers and their arithmetic are not exact, it usually does not make computational sense to test for cases of exact equality. However, historically, geometers have always distinguished, e.g., between a point being “inside” a triangle versus “on an edge” or “at a vertex.” This has introduced a certain schizophrenia into the field. On the one hand (and especially before about 1990), practitioners have labored to create algorithms that use exact (integer) arithmetic, so that the traditional distinctions can be elegantly preserved. On the other hand (and especially after about 1990, when fast floating operations in special-purpose graphics processors started to be available), many of these niceties are no longer needed, and sloppiness at the level of “machine epsilon” can be tolerated in the interest of speed. In this chapter we are unapologetically in the sloppy camp. In boundary cases, our code is supposed to produce reasonable results, but not necessarily choose that specific reasonable result that you might think you want. Caveat emptor.

A less specific goal in this chapter is to give some of the “flavor” of the field of computational geometry. It is a flavor that deliciously combines elements of Euclid (pardon!) with elements of modern computer science and mathematics.

Some good general references are listed here.

# CITED REFERENCES AND FURTHER READING:

de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry: Algorithms and Applications, 2nd revised ed.(Berlin: Springer). [Best-selling text, especially strong on references to the published literature.]   
O’Rourke, J. 1998, Computational Geometry in C, 2nd ed. (Cambridge, UK: Cambridge University Press). [Well written, with clear explanations and C code.]   
Preparata, F.P. and Shamos, M.I. 1991, Computational Geometry: An Introduction (Berlin: Springer).   
Schneider, P.J. and Eberly, D.H. 2003, Geometric Tools for Computer Graphics (San Francisco: Morgan Kaufmann). [Huge compendium of formulas and code.]   
Bowyer, A. and Woodwark, J. 1983, A Programmer’s Geometry (London: Butterworths). [Delightful classic, especially for those who get nostalgic at seeing Fortran printed in all uppercase.]   
Glassner, A.S., ed. 1990, Graphics Gems (San Diego: Academic Press). [Series of books full of algorithmic tricks-of-the-trade.]   
Arvo, J., ed. 1991, Graphics Gems II (San Diego: Academic Press).   
Kirk, D., ed. 1992, Graphics Gems III (Cambridge, MA: Academic Press).   
Heckbert, P.S., ed. 1994, Graphics Gems IV (Cambridge, MA: Academic Press).   
Euclid, ca. 300BC, Euclid’s Elements; reprinted 2002 (Santa Fe, NM: Green Lion Press).

# 21.1 Points and Boxes

A point $\mathbf { p }$ in a $D$ -dimensional space is specified by its $D$ Cartesian coordinates, $( x _ { 0 } , x _ { 1 } , \ldots , x _ { D - 1 } )$ . Generally we will concern ourselves only with the cases $D = 2$ (points in a plane) and $D = 3$ (points in 3-space), but the concept is more general.

The representation in code follows just this paradigm. By eschewing special names for individual coordinates — like $x$ , y, z — we keep the ability to loop easily over coordinates in $D$ dimensions.

template<Int DIM> struct Point {   
Simple structure to represent a point in DIM dimensions. Doub x[DIM]; The coordinates. Point(const Point &p) { Copy constructor. for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ; i<DIM; $\mathrm { i + + ) } \ \mathrm { \ x [ i ] ~ \eta = \ p \cdot \mathrm { \ x [ i ] : } }$ Point& operator $=$ (const Point &p) { Assignment operator. for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ; i<DIM; $\dot { \bf 1 } + +$ ) x[i] $=$ p.x[i]; return \*this; 1 bool operator $\mathrel { = } =$ (const Point &p) const { for (Int $\scriptstyle \dot { 1 } = 0$ ; i<DIM; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \beta } } } .$ ) if (x[i] $\ ! = \ p . \mathbf { x }$ [i]) return false; return true; } Point(Doub $\mathbf { x } 0 ~ = ~ 0 . 0$ , Doub $\mathrm { ~ x 1 ~ } = ~ 0 . 0$ , Doub ${ \bf x } 2 ~ = ~ 0 . 0$ ) { $\mathbf { x } \left[ 0 \right] \ = \ \mathbf { x } 0$ ; Constructor by coordinate values. Arguments if (DIM $> 1 \dot { }$ ) $\mathbf { x } \left[ 1 \right] \ = \ \mathbf { x } 1$ ; beyond the required number are not used if (DIM $> 2$ ) $\mathbf { x } \left[ 2 \right] \ = \ \mathbf { x } 2$ ; and can be omitted. if (DIM $> 3$ ) throw("Point not implemented for DIM > 3"); }   
};

# pointbox.h

#

In the interest of concise code, the constructor above may pass some unnecessary default arguments of zero. You can easily clean this up if you care.

If we have two points $\mathbf { p }$ and $\mathbf { q }$ , we can compute their distance $d$ ,

$$
d = | \mathbf { p } - \mathbf { q } | = \left[ \sum _ { i = 0 } ^ { D - 1 } ( p _ { i } - q _ { i } ) ^ { 2 } \right] ^ { 1 / 2 }
$$

where $p _ { i }$ and $q _ { i }$ are now the respective Cartesian coordinates for each point.

In code, we have

template<Int DIM> Doub dist(const Point<DIM> &p, const Point<DIM> &q) { Returns the distance between two points in DIM dimensions.

Doub dd $= ~ 0 . 0$ ;  
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<DIM; ${ \mathrm { j } } + + { \mathrm { . } }$ ) dd $+ =$ SQR(q.x[j]-p.x[j]);  
return sqrt(dd);

Note that dist is not a member of the class Point, but rather a freestanding function whose arguments are Points. We will overload dist with other types of arguments, signifying other kinds of distances between objects.

# 21.1.1 Boxes

By a box, we mean a rectangle (for $D = 2$ ) or rectangular parallelepiped (for $D = 3$ , a “brick” in other words) that is aligned with the coordinate axes. Boxes are interesting because they can tessellate (that is, partition) $D$ -dimensional space, and they can contain other objects. Indeed, every finite, extended object has a bounding box, which is the unique smallest box that contains it. One way to represent a box is by the points at two special, diagonally opposite, corners. The first point (“low”) has coordinate values that are the minima on the surface of the box; the second point (“high”) has coordinate values that are the maxima. All other corners of a box, it should be obvious, have coordinate values that are, dimension by dimension, either the value of “low” or the value of “high”; and all such permutations are corners, $2 ^ { D }$ in all.

The code follows this description:

template<Int DIM> struct Box {   
Structure to represent a Cartesian box in DIM dimensions. Point<DIM> lo, hi; Diagonally opposite corners (min of all coordinates and Box() {} max of all coordinates) are stored as two points. Box(const Point<DIM> &mylo, const Point<DIM> &myhi) : lo(mylo), hi(myhi) {}   
};

Note that a copy constructor and assignment operator are not needed, since by default the two Points will be appropriately copied or assigned (one convenience of this representation).

A point can be either outside a box, inside it, or — in principle — on its surface. As mentioned in $\ S 2 1 . 0$ , we represent all coordinates as (approximate) floating-point numbers, not (exact) integers, so it would not be prudent to depend on any exact equalities of coordinate values or distances. We will be careful, therefore, not to put too much credence in the idea of the exact surface of a box; usually we’ll consider the surface (should some exact equality happen to hold) as a part of the box’s interior.

If a point is outside a box, then we define its distance from the box to be the distance to the nearest point on the surface of (or inside) the box. A glance at Figure 21.1.1 shows that this distance is the Pythagorean sum (that is, square root of sum of squares) of the distances from the point to some — but not all — of the hyperplanes that bound the box. The rule is that when a point has a coordinate that is greater than the corresponding max of the box, or less than the corresponding min, then that coordinate contributes to the sum. When the point has a coordinate between the max and min, then it does not contribute to the sum, since (along that coordinate) the shortest line can be perpendicular to the hyperplane. When a point is inside, or on the surface of, a box, we define its distance to the box to be zero.

These definitions of distance are embodied in the following code.

template<Int DIM> Doub dist(const Box<DIM> &b, const Point<DIM> &p) { If point p lies outside box b, the distance to the nearest point on b is returned. If p is inside b or on its surface, zero is returned.

Doub dd $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
for (Int $\scriptstyle { \dot { 1 } } = 0$ ; i<DIM; i++) { if (p.x[i]<b.lo.x[i]) dd $+ =$ SQR(p.x[i]-b.lo.x[i]); if (p.x[i]>b.hi.x[i]) dd $+ =$ SQR(p.x[i]-b.hi.x[i]);   
}   
return sqrt(dd);

Frequently we want to know if a point is inside or outside a box. The above dist routine can be used for this. A positive return means outside, zero means inside. If inside-versus-outside, and not distance, is all you want to know, then some streamlining is possible: Replace dd by a Boolean variable, substitute logical-or’s for the additions, and of course omit the square root. The logic remains otherwise the same.

![](images/f851fd2782bf32c8a5b8131b8b67e821578328dd87fb3ddfb0496498b62705c5.jpg)  
Figure 21.1.1. Distance from a point to a $D$ -dimensional box. The general formula (as for lines $A A ^ { \prime }$ and $C C ^ { \prime } )$ ) is a Pythagorean sum of $D$ distances to the plane that includes the nearer side of the box. But when the point is between two such parallel planes (as for $B B ^ { \prime }$ and $D D ^ { \prime }$ ) then the corresponding coordinate is omitted from the sum.

# 21.1.2 Nodes for Binary Trees of Boxes

In the next section we will construct a binary tree of nested boxes, wherein each box is subdivided into, and linked to, two daughter boxes. Each box in the tree will also contain a list of points that lie inside the box. For use in such a task, we here give a structure, derived from the Box structure, but with additional variables that can point to a mother box, two daughter boxes, and the low and high indices on a list of points (designating the range of points inside the box). The constructor just sets all the values explicitly.

template<Int DIM> struct Boxnode : Box<DIM>   
Node in a binary tree of boxes containing points. See text for details. Int mom, dau1, dau2, ptlo, pthi; Boxnode() {} Boxnode(Point<DIM> mylo, Point<DIM> myhi, Int mymom, Int myd1, Int myd2, Int myptlo, Int mypthi) : Box<DIM>(mylo, myhi), mom(mymom), dau1(myd1), dau2(myd2), ptlo(myptlo), pthi(mypthi) {}

# 21.2 KD Trees and Nearest-Neighbor Finding

Once, long ago, the term “kd tree” (or “k-D tree”) was an abbreviation for “ $k$ -dimensional tree.” However, the term has come to mean a very specific, and useful, kind of tree structure for partitioning points, especially in small numbers of dimensions, like 2 or 3. A KD tree that contains $N$ points can be constructed in ${ \cal O } ( N \log N )$ time and $O ( N )$ space. Once constructed, the KD tree facilitates such operations as finding a point’s nearest neighbor in ${ \cal O } ( \log N )$ time, or all nearest neighbors in ${ \cal O } ( N \log N )$ time. KD trees were first described by Bentley [8] in 1975. Let’s see how this works.

Start with a very large box, one that easily contains all possible points that are of interest. There is no penalty for making this root box humongous, so coordinates of $\pm 1 0 ^ { 9 9 }$ are fine. Now generate a list of $N$ points (of interest to your application) that lie inside the root box. The defining principles of a KD tree are

- Boxes are successively partitioned into two daughter boxes.   
Each partition is along the axis of one coordinate.   
The coordinates are used cyclically in successive partitions. In making the partition, the position of the “cut” is chosen to leave equal numbers of points on the two sides (or differing by one in the case of an odd number of points).

Within these principles, there are some arbitrary design choices to be made. In the implementation below, the partition “cut” goes exactly through one of the points (i.e., shares one of its coordinate values). This avoids a bit of extra bookkeeping incurred by other possible choices. Also, we terminate the tree when a box node contains either one or two points, avoiding the additional partitioning of two-point boxes into two one-point boxes. This choice is natural because the Boxnode structure already has pointers to two points (ptlo and pthi), and it reduces the total number of stored boxes by as much as $50 \%$ .

With these principles and design rules in mind, you can decode Figure 21.2.1, which shows a two-dimensional KD tree containing 1000 points. (As a bit of artistic license, the root box in the figure has been shrunk to just contain the points, instead of being off near infinity.)

Interestingly, given $N$ , the number of points, it is possible to give an exact formula for the number of boxes generated by our KD tree partition rules. (This makes memory allocation for the tree very straightforward.) If $N _ { B } ( N )$ is the number of boxes needed for $N$ points, then two obvious recurrence relations describe what happens in the initial partitioning of $2 n$ points into $n$ plus $n$ , or $2 n - 1$ points into $n$ plus $n - 1$ :

$$
\begin{array} { c } { { N _ { B } ( 2 n ) = 2 N _ { B } ( n ) + 1 } } \\ { { N _ { B } ( 2 n - 1 ) = N _ { B } ( n ) + N _ { B } ( n - 1 ) + 1 } } \end{array}
$$

The $+ 1$ in both formulas refers to the additional mother box that “glues together” two daughter partial trees at each stage. The solution to these recurrences is

$$
\begin{array} { r } { N _ { B } ( N ) = \operatorname* { m i n } ( M - 1 , ~ 2 N - \frac { 1 } { 2 } M - 1 ) } \end{array}
$$

where $M$ is the smallest power of 2 greater or equal to $N$ , that is,

$$
M = 2 ^ { \left\lceil \log _ { 2 } N \right\rceil }
$$

(You can verify this solution by induction, working out the various possibilities of the min function. Or — much more fun — you can write a program to verify it numerically for $N < 1 0 ^ { 9 }$ , say.)

![](images/2d00070a1095da26458eeacf6d31d91aa7bd8f0aa929d422b4bde570f54efa24.jpg)  
Figure 21.2.1. KD tree constructed from 1000 points in the plane. The first subdivision is visible as a fullheight vertical line about halfway across the figure. The next subdivisions are horizontal lines, extending halfway across the figure. The subdivisions alternate between horizontal and vertical, and partition into (nearly) equal numbers of points at each stage. This tree terminates when there are either one or two points in a box (one of which is usually on the box boundary).

# 21.2.1 Implementation of the KD Tree

We implement the KD tree as a structure that gets built from a vector of Points and contains methods that embody the principal applications that we will discuss below, mainly various kinds of nearest-neighbor problems.

template<Int DIM> struct KDtree   
Structure for implementing a KD tree. static const Doub BIG; Size of the root box, value set below. Int nboxes, npts; Number of boxes, number of points. vector< Point<DIM> $>$ &ptss; Reference to the vector of points in the KD tree. Boxnode<DIM> \*boxes; The array of Boxnodes that form the tree. VecInt ptindx, rptindx; Index of points (see text), and reverse index. Doub \*coords; Point coordinates rearranged contiguously. KDtree(vector< Point<DIM> $>$ &pts); Constructor. \~KDtree() {delete [] boxes;} Next, utility functions for use after the tree is constructed. See below. Doub disti(Int jpt, Int kpt); Int locate(Point<DIM> pt); Int locate(Int jpt); Next, applications that use the KD tree. See text. Int nearest(Int jpt); Int nearest(Point<DIM> pt); void nnearest(Int jpt, Int \*nn, Doub \*dn, Int n); static void sift_down(Doub \*heap, Int \*ndx, Int nn); Used by nnearest. Int locatenear(Point<DIM> pt, Doub r, Int \*list, Int nmax);   
};

Note that the KDtree structure keeps a reference to the vector of Points that created it. This is used in some of the applications and has the implication that the user should not modify the vector of points while its derived KD tree is in scope. The array coords is an internal representation of the points-vector that is used during the construction of the KD tree, and then is immediately returned to the memory pool.

What makes the KD tree fast to construct is the existence of fast partition algorithms, $O ( N )$ in time, that not only find the median value in an array of $N$ values, but also move all smaller values to one side of the array and all larger values to the other. We already met such an algorithm in $\ S 8 . 5$ , in the routine select. Here, we need a slight variant, selecti, that partitions an array of integers not by their values, but by using them to index a separate array of values that remain unaltered. Because we will want to partition subsegments of arrays, we pass all references to the arrays by address.

Int selecti(const Int k, Int \*indx, Int n, Doub \*arr)   
Permutes indx[0..n-1] to make arr[indx[0..k-1]]  arr[indx[k]]  arr[indx[k+1..n-1]]. The array arr is not modified. See comments in the routine select.   
{   
Int i,ia,ir,j,l,mid;   
Doub a;   
l=0;   
$\scriptstyle { \mathrm { i } x = n - 1 }$ ;   
for (;;) { if (ir <= l+1) { if ( $\scriptstyle \mathbf { i r } \ = = \ 1 + 1$ && arr[indx[ir]] $<$ arr[indx[l]]) SWAP(indx[l],indx[ir]); return indx[k]; else { mid=(l+ir) >> 1; SWAP(indx[mid],indx $[ 1 + 1 ]$ ); if (arr[indx[l]] $>$ arr[indx[ir]]) SWAP(indx[l],indx[ir]); if (arr[indx[l+1]] $>$ arr[indx[ir]]) SWAP(indx[l+1],indx[ir]); if (arr[indx[l]] $>$ arr[indx[l+1]]) SWAP(indx[l],indx[l+1]); $\dot { 1 } = 1 + 1$ ; $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { 1 } } } { \boldsymbol { \mathbf { r } } }$ ; ia $=$ indx[l+1]; a=arr[ia]; for (;;) { do $\dot { \bf 1 } + +$ ; while (arr[indx[i]] < a); do j--; while (arr[indx[j]] > a); if (j < i) break; SWAP(indx[i],indx[j]); indx[l+1] $=$ indx[j]; indx[j] $=$ ia; if (j $> = { \textbf { k } } .$ ) ir=j-1; if (j $< = { \bf \nabla } \mathbf { k } .$ ) $\mathbf { \vec { \tau } } _ { 1 } = \mathbf { \dot { \tau } }$ ; }   
}

The basic strategy for constructing the KD tree is this: Set up an array of integers that index the $N$ points (ptindx, below). Next, copy all the point coordinates into an array (coords) in which all the $x _ { 0 }$ coordinates are contiguous, followed by all the $x _ { 1 }$ coordinates, and so on through all the dimensions. Now use selecti to partition (and rearrange) the index of points according to the value of their $x _ { 0 }$ coordinates, with half the points on each side of the partition. These two halves, now viewed as separate arrays, contain the points in two new daughter boxes. Now partition each of them into half by the value of the $x _ { 1 }$ coordinate. And so on, recursively, going through the coordinates cyclically.

The recursion is so simple that it is easy to code it as a simple “pending task list,” thus avoiding the overhead of recursive function calls. A pending task consists of an index pointing to the box ready for further partitioning (the expectant mother, as it were) and a value that remembers which dimension is next to partition along. Because the tree is constructed “depth first,” the task list never grows larger than the log of the total number of boxes. Every new daughter box is born with a pointer to its mother, and pointers to its beginning and end elements in the points index array ptindx. Although these elements will generally be permuted in subsequent partitionings, none will ever be moved out of the range specified when a daughter box is first created. That is why the whole process can be done in a single pointindex array, with all boxes simply pointing into some subrange of that array.

The KDtree constructor, below, should now be straightforward to understand.

plate<Int DIM> KDtree<DIM>::KDtree(vector< Point<DIM> $>$ &pts) :   
s(pts), npts(pts.size()), ptindx(npts), rptindx(npts) {   
nstruct a KD tree from a vector of points.   
Int ntmp,m,k,kk,j,nowtask,jbox,np,tmom,tdim,ptlo,pthi;   
Int \*hp;   
Doub \*cp;   
Int taskmom[50], taskdim[50]; Enough stack for $2 ^ { 5 0 }$ points!   
for $( \mathtt { k } = 0$ ; k<npts; $\mathbf { k } { + } { + } \mathbf { \Gamma } .$ ) ptindx[k] $= \texttt { k }$ ; Initialize the index of points.   
Calculate the number of boxes and allocate memory for them.   
${ \texttt { m } } = { \texttt { 1 } }$ ;   
for (ntmp $=$ npts; ntmp; ntmp >>= 1) { m $< < = ~ 1$ ;   
}   
nboxes $=$ 2\*npts - $\mathrm { ~ ( ~ m ~ } > > \ 1 )$ ;   
if (m < nboxes) nboxes $= ~ \mathfrak { m }$ ;   
nboxes--   
boxes $=$ new Boxnode<DIM>[nboxes];   
Copy the point coordinates into a contiguous array.   
coords $=$ new Doub[DIM\*npts];   
for ( $\scriptstyle \dot { \ j } = 0$ , kk $_ { = 0 }$ ; $\mathrm { j } < \tt D I M$ ; ${ \dot { \mathsf { J } } } ^ { + + }$ , kk $+ =$ npts) { for $\scriptstyle ( \mathtt { k } = 0$ ; k<npts; $\mathbf { k } { + } { + }$ ) coords[kk+k] $=$ pts[k].x[j];   
Initialize the root box and put it on the task list for subdivision.   
Point<DIM> lo(-BIG,-BIG,-BIG), hi(BIG,BIG,BIG); Syntax OK for 2-D too.   
boxes[0] $=$ Boxnode<DIM>(lo, hi, 0, 0, 0, 0, npts-1);   
jbox $\qquad = \ 0$ ;   
taskmom[1] $\mathit { \Theta } = \mathit { \Theta } 0$ ; Which box.   
taskdim[1] $\qquad = \ 0$ ; Which dimension.   
nowtask $= ~ 1$ ;   
while (nowtask) { Main loop over pending tasks. tmom $=$ taskmom[nowtask]; tdim $=$ taskdim[nowtask--]; ptlo $=$ boxes[tmom].ptlo; pthi $=$ boxes[tmom].pthi; hp $=$ &ptindx[ptlo]; Points to left end of subdivision. $\mathtt { c p } \ =$ &coords[tdim\*npts]; Points to coordinate list for current dim. np $=$ pthi - ptlo + 1; Number of points in the subdivision. kk $=$ (np-1)/2; Index of last point on left (boundary point). (void) selecti(kk,hp,np,cp); Here is where all the work is done. Now create the daughters and push them onto the task list if they need further subdividing. hi $=$ boxes[tmom].hi; lo $=$ boxes[tmom].lo; hi.x[tdim] $=$ lo.x[tdim] $=$ coords[tdim\*npts $^ +$ hp[kk]]; boxes[ $: + +$ jbox] $=$ Boxnode<DIM>(boxes[tmom].lo,hi,tmom,0,0,ptlo,ptlo+kk); boxes $[ + +$ jbox] $=$ Boxnode<DIM>(lo,boxes[tmom].hi,tmom,0,0,ptlo+kk+1,pthi); boxes[tmom].dau1 $=$ jbox-1; boxes[tmom].dau2 $=$ jbox; if (kk $> 1 \dot { 2 }$ ) { taskmom[++nowtask] $=$ jbox-1; taskdim[nowtask] $=$ (tdim $^ { + 1 }$ ) % DIM; } if (np - kk $> 3$ ) { taskmom[++nowtask] $=$ jbox; taskdim[nowtask] $=$ (tdim $^ { + 1 }$ ) % DIM; }   
for $( \mathrm { j } = 0 ) \mathrm { i }$ ; j<npts; ${ \mathrm { j } } + + { \mathrm { . } }$ ) rptindx[ptindx[j]] $=$ j; Create reverse index.   
delete [] coords; Don’t need them anymore.

There are a small number of utility functions that are easy to provide. Although we generally prefer to have our distance (dist) functions be freestanding, it is useful to have a KDtree member routine that returns the distance between two points in a KD tree, referenced by their integer position in the underlying vector of points.

template<Int DIM> Doub KDtree<DIM>::disti(Int jpt, Int kpt) { Returns the distance between two points in the kdtree given their indices in the array of points, but returns a large value if the points are identical.

if (jpt $= =$ kpt) return BIG; else return dist(ptss[jpt], ptss[kpt]); }

There is a special reason for returning BIG when the two points are identical: Later, when we find a point’s nearest neighbor, we don’t want the invariable answer to be “itself!”

Another simple function takes an arbitrary Point as the argument and returns the index of the box that uniquely contains it. In this function we first see an example of traversing the tree hierarchically, starting at the root box and then choosing only one of two daughter boxes at each stage. Also, by keeping track of which dimension is next to be partitioned on (jdim, below), we need only check one of the point’s coordinates at each stage. Evidently, the whole process is ${ \cal O } ( \log N )$ in time, since there can be only that many levels in the tree.

template<Int DIM> Int KDtree<DIM>::locate(Point<DIM> pt) {   
Given an arbitrary point pt, return the index of which kdtree box it is in. Int nb,d1,jdim; $\mathbf { n b } \ = \ \mathbf { j d i m } \ = \ 0$ ; Start with the root box. while (boxes[nb].dau1) { As far as possible down the tree. d1 $=$ boxes[nb].dau1; if (pt.x[jdim] $< =$ boxes[d1].hi.x[jdim]) $\mathtt { n b } { = } \mathtt { d } 1$ ; else nb $\ c =$ boxes[nb].dau2; jdim $\begin{array} { r l } { = } & { { } + + } \end{array}$ jdim % DIM; Increment the dimension cyclically. } return nb;   
}

The actual Box can be obtained from the returned integer, say j, by referencing boxes[j] in the KDtree, since Boxnode is a derived class of Box.

A very similar utility returns the index of the box that contains one of the points used to construct the KDtree. This is not necessarily the same box as the above routine would return, because of the possibility of multiple ties in coordinate values, in which case some tied points can lie on one side of the median partition and others on the other side.

template<Int DIM> Int KDtree<DIM>::locate(Int jpt) {   
Given the index of a point in the kdtree, return the index of which box it is in. Int nb,d1,jh; jh $=$ rptindx[jpt]; The reverse index tells where the point lies in the nb $\mathit { \Theta } = \mathit { \Theta } 0$ ; index of points. while (boxes[nb].dau1) { d1 $=$ boxes[nb].dau1; if (jh $< =$ boxes[d1].pthi) nb=d1; else nb $=$ boxes[nb].dau2; } return nb;   
}

# 21.2.2 Applications of KD Trees

Most applications of KD trees make use of locality properties of its nested boxes. This is best seen in a few examples.

Suppose we want to know which of the $N$ points in a KD tree is closest to an arbitrary point p (not necessarily one of the points in the tree). Without the tree, this is evidently a calculation that requires $O ( N )$ operations, as we compare $\mathbf { p }$ to each candidate point in turn. However, if we have invested the ${ \cal O } ( N \log N )$ operations required to construct the tree, then we can proceed in the following way. First, find the box in which $\mathbf { p }$ lies, and find the closest point in the tree that lies in that box. This takes ${ \cal O } ( \log N )$ operations, as we saw above. The found point might in fact be the nearest neighbor (we don’t know yet), but in any case its distance is now an upper bound on how far away the true nearest neighbor can be.

Second, traverse the tree by a depth-first recursion (exactly the way we did when we constructed the tree). As we encounter each new box, we check whether it could possibly contain a point closer than the nearest point found so far. Since we start with a point that is already pretty close (in the same box as $\mathbf { p }$ ), most boxes get rejected at this step. When a box is rejected, we don’t need to open its daughter boxes, so a whole branch of the tree gets “pruned.” On average, only about ${ \cal O } ( \log N )$ boxes actually get opened, so the total work load to find the nearest point is ${ \cal O } ( \log N )$ .

If we are really interested in only a single point $\mathbf { p }$ , then the “slow,” $O ( N )$ , method would have been faster. But if we are repeating the operation for many different points ${ \bf p } _ { i }$ , comparing to the same $N$ points in the tree each time, then calling the following routine for each ${ \bf p } _ { i }$ in turn is a big win.

# kdtree.h

if (d < dnrst) { nrst $=$ ptindx[i]; dnrst $\qquad = \ \mathrm { ~ d ~ }$ ; } } Second stage, we traverse the tree opening only possibly better boxes. task[1] $\mathit { \Theta } = \mathit { \Theta } _ { 0 } ;$ ntask $\ l = \ 1$ ; while (ntask) { $\mathrm { ~ \bf ~ k ~ } =$ task[ntask--]; if (dist(boxes[k],pt) $<$ dnrst) { Distance to closest point in box. if (boxes[k].dau1) { If not an end node, put on task list. task $[ + + ]$ ntask] $=$ boxes[k].dau1; task[++ntask] $=$ boxes[k].dau2; } else { Check the 1 or 2 points in the box. for ( $\mathrm { i } =$ boxes[k].ptlo; $\div < =$ boxes[k].pthi; $\dot { 1 } + +$ ) { d $=$ dist(ptss[ptindx[i]],pt); if (d $<$ dnrst) { nrst $=$ ptindx[i]; dnrst $\mathit { \Theta } = \mathit { \Theta } \mathtt { d }$ ; } } } } } return nrst;

What if we want to know the nearest-neighbor point not of an arbitrary location, but of one of the points stored in the KD tree? The above routine won’t do. If we send it a point in the tree, it will give the obvious result that the point is its own nearest neighbor! We need to modify the routine so as to use disti from KDtree, which defined a point’s self-distance as being large, rather than small.

An additional useful feature is to find not the single nearest neighbor, but the $n$ nearest neighbors for some specified $n < N - 1$ . The trick here is to avoid making the algorithm $O ( n \log N )$ , which is what it would be if, for each candidate point, we compared the candidate to all $n$ of the best points so far. A good way to proceed is with a heap structure, as described in $\ S 8 . 3$ and used (for a very similar purpose) in the routine hpsel in $\ S 8 . 5$ . The work load then scales as $O ( \log n \log N )$ .

The following routine is coded so as to lose hardly any efficiency in the case $n = 1$ (find the single nearest neighbor) while using a heap structure in the case $n > 1$ .

template<Int DIM> void KDtree<DIM>::nnearest(Int jpt, Int \*nn, Doub \*dn, Int n) Given the index jpt of a point in a kdtree, return a list $\mathtt { n n } [ 0 \ldots \mathtt { n } - 1 ]$ of the indices of the n points in the tree nearest to point $\dot { \mathsf { J } }$ , and a list $\mathtt { d d } [ 0 \dots \cdot \mathtt { n } ^ { - 1 } ]$ of their distances.

Int i,k,ntask,kp;   
Int task[50]; Stack for boxes to be opened.   
Doub d;   
if ( $\textbf { \em n } >$ npts-1) throw("too many neighbors requested");   
for $\scriptstyle \dot { 1 } = 0$ ; i<n; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \rho } } } .$ ) dn[i] $=$ BIG;   
Find smallest mother box with enough points to initialize the heap.   
$\tt k p \tt =$ boxes[locate(jpt)].mom;   
while (boxes[kp].pthi - boxes[kp].ptlo < n) kp $=$ boxes[kp].mom;   
Examine its points and save the n closest.   
for ( $\dot { \bf 1 } =$ boxes[kp].ptlo; $\ \mathrm { i } < =$ boxes[kp].pthi; $\dot { \bf 1 } + +$ ) { if (jpt $= =$ ptindx[i]) continue;   
${ \texttt { d } } =$ disti(ptindx[i],jpt);   
if (d < dn[0]) { dn[0] $=$ d; nn[0] $=$ ptindx[i]; if (n>1) sift_down(dn,nn,n); Maintain the heap structure.   
}   
Now we traverse the tree opening only possibly better boxes.   
task[1] $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
ntask $\ l = \ 1$ ;   
while (ntask) { $\mathrm { ~ \bf ~ k ~ } =$ task[ntask--]; if $( \mathrm { k \Omega } = = \mathrm { k p } )$ continue; Don’t redo the box used to initialize. if (dist(boxes[k],ptss[jpt]) $<$ dn[0]) { if (boxes[k].dau1) If not an end node, put on task list. task[++ntask] $=$ boxes[k].dau1; task[++ntask] $=$ boxes[k].dau2; } else { Check the 1 or 2 points in the box. for ( $\dot { \bf 1 } =$ boxes[k].ptlo; $\dot { \bf 1 } < =$ boxes[k].pthi; i++) { d $=$ disti(ptindx[i],jpt); if (d $<$ dn[0]) { dn[0] $=$ d; nn[0] $=$ ptindx[i]; if $\cdot \mathtt { n } > 1$ ) sift_down(dn,nn,n); Maintain the heap. } } } }   
}   
return;

The following routine is used by the above for the sift-down process on the heap, differing from the sift_down used by hpsort $( \ S 8 . 3 )$ only in its tailored interface for the present application, and the fact that it simultaneously rearranges two arrays, the distances (forming a heap) and the corresponding point numbers.

template<Int DIM> void KDtree<DIM>::sift_down(Doub \*heap, Int \*ndx, Int nn) Fix heap[0..nn-1], whose first element (only) may be wrongly filed. Make a corresponding permutation in ndx[0.. $\mathtt { n n - 1 } ]$ . The algorithm is identical to that used by sift_down in hpsort.

Int $\mathrm { ~ n ~ } = \mathrm { ~ n ~ n ~ } \mathrm { ~ - ~ } \mathrm { ~ 1 ~ }$ ; Int j,jold,ia; Doub a; $\mathrm { ~ a ~ } =$ heap[0]; $\mathrm { ~ i ~ a ~ } = \mathrm { ~ n d x } [ 0 ]$ ; jold $\mathit { \Theta } = \mathit { \Theta } 0$ ; $\dot { \mathrm { ~ \scriptsize ~ j ~ } } = \mathrm { ~ \scriptsize ~ 1 ~ }$ ; while (j $< = { \mathrm { ~ \bf ~ n ~ } } .$ ) { if $( \mathrm { ~ j ~ } < \mathrm { ~ n ~ }$ && heap[j] $<$ heap[j $+ 1 ]$ ) j++; if ( $a \ > =$ heap[j]) break; heap[jold] $=$ heap[j]; ndx[jold] $=$ ndx[j]; jold $=$ j; ${ \mathrm {  ~ j ~ } } = ~ 2 * { \mathrm {  ~ j ~ } } + ~ 1 { \mathrm {  ~ \Omega ~ } }$ ; } heap[jold] $\qquad = \ \mathtt { a }$ ; ndx[jold] $=$ ia; }

As a final illustrative example, here is how to find all points in a KD tree that lie within a specified radius $r$ of some arbitrary location p.

template<Int DIM>   
Int KDtree<DIM>::locatenear(Point<DIM> pt, Doub r, Int \*list, Int nmax) {   
Given a point pt and radius r, returns a value nret such that list[0..nret-1] is a list of a   
kdtree points within a radius r of pt, up to a user-specified maximum of nmax points. Int k,i,nb,nbold,nret,ntask,jdim,d1,d2; Int task[50]; $\mathrm { n b ~ = ~ j d i m ~ = ~ n r e t ~ = ~ 0 ~ } ;$ if ( $\mathrm { ~ \bf ~ r ~ } < 0 . 0 )$ throw("radius must be nonnegative"); Find the smallest box that contains the ”ball” of radius r. while (boxes[nb].dau1) { nbold $=$ nb; d1 $=$ boxes[nb].dau1; ${ \tt d } 2 { \it \Delta \phi } = { \tt d } $ boxes[nb].dau2; Only need to check the dimension that divides the daughters. if (pt.x[jdim] $+ \mathrm { ~  ~ r ~ } < =$ boxes[d1].hi.x[jdim]) nb = d1; else if (pt.x[jdim] - $\scriptstyle \mathbf { \underline { { ~ r ~ } } } > =$ boxes[d2].lo.x[jdim]) $\mathrm { { n b } } ~ = ~ \mathrm { { d } } 2$ ; jdim $= \quad + +$ jdim % DIM; if (nb $= =$ nbold) break; Neither daughter encloses the ball. } Now traverse the tree below the starting box only as needed. task[1] $=$ nb; ntask $= ~ 1$ ; while (ntask) { $\mathrm { ~ \bf ~ k ~ } =$ task[ntask--]; if (dist(boxes[k],pt) > r) continue; Box and ball are disjoint. if (boxes[k].dau1) { Expand box further when possible. task $^ { , + + }$ ntask] $=$ boxes[k].dau1; task[++ntask] $=$ boxes[k].dau2; } else { Otherwise process points in the box. for ( $\mathrm { i } =$ boxes[k].ptlo; $\ \mathrm { i } < =$ boxes[k].pthi; $\mathbf { i } + +$ ) { if (dist(ptss[ptindx[i]],pt) $< = \texttt { r }$ && nret $<$ nmax) list[nret++] $=$ ptindx[i]; if (nret $= =$ nmax) return nmax; Not enough space! } } } return nret;   
}

You might wonder why the above routine doesn’t also use the tree structure to find cases where a box lies entirely inside the “ball” of radius $r$ , in which case it could add the box’s points to the output list without further opening of its daughters. The improvement is potentially a factor of $O ( \log n )$ , where $n$ is the typical number of neighbors returned. The resulting routine is slightly too long for us to include, however. A good exercise is to code this modification yourself. You’ll see that it is harder to check whether a box is inside a ball than vice versa: You have to check all $2 ^ { D }$ corners of the box, not just the diagonally opposite “low” and “high” ones.

# CITED REFERENCES AND FURTHER READING:

Bentley, J.L. 1975, “Multidimensional Binary Search Trees Used for Associative Searching,” Communications of the ACM,vol.18, pp. 509-517.   
de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry:Algorithms and Applications, 2nd revised ed.(Berlin: Springer), $\ S 5 . 2$ .   
Samet, H. 1990, The Design and Analysis of Spatial Data Structures (Reading, MA: Addison-Wesley).

# 21.3 Triangles in Two and Three Dimensions

Not since the time of Euclid has the lowly triangle attracted as much attention as it does today in computer graphics. Triangles and triangulation (the decomposition, or approximation, of complicated geometrical objects using only triangles) are at the heart of practically every computer-generated image.

Three points, call them a, b, c, define a triangle. They are its vertices. If the points are two-dimensional, the triangle lies in the two-dimensional plane. If the points have higher dimensionality, then the triangle floats in the corresponding $D$ - dimensional space (most commonly $D = 3$ ). For now, consider only the former case, with $D = 2$ , so that a has coordinates $( a _ { 0 } , a _ { 1 } )$ , and similarly for $\mathbf { b }$ and c.

Area. The area $\mathbf { \mathcal { A } } ( \mathbf { a b c } )$ of the triangle $\triangle$ abc can be written in a number of equivalent ways, including

$$
{ \begin{array} { r l } & { 2 { \mathcal { A } } ( \mathbf { a b c } ) = { \left| \begin{array} { l l l } { a _ { 0 } } & { a _ { 1 } } & { 1 } \\ { b _ { 0 } } & { b _ { 1 } } & { 1 } \\ { c _ { 0 } } & { c _ { 1 } } & { 1 } \end{array} \right| } } \\ & { \qquad = ( \mathbf { b } - \mathbf { a } ) \times ( \mathbf { c } - \mathbf { a } ) = ( b _ { 0 } - a _ { 0 } ) ( c _ { 1 } - a _ { 1 } ) - ( b _ { 1 } - a _ { 1 } ) ( c _ { 0 } - a _ { 0 } ) } \\ & { \qquad = ( \mathbf { c } - \mathbf { b } ) \times ( \mathbf { a } - \mathbf { b } ) = ( c _ { 0 } - b _ { 0 } ) ( a _ { 1 } - b _ { 1 } ) - ( c _ { 1 } - b _ { 1 } ) ( a _ { 0 } - b _ { 0 } ) } \\ & { \qquad = ( \mathbf { a } - \mathbf { c } ) \times ( \mathbf { b } - \mathbf { c } ) = ( a _ { 0 } - c _ { 0 } ) ( b _ { 1 } - c _ { 1 } ) - ( a _ { 1 } - c _ { 1 } ) ( b _ { 0 } - c _ { 0 } ) } \end{array} }
$$

Here $\times$ denotes the vector cross product, defined in two dimensions simply by

$$
\mathbf { A } \times \mathbf { B } = A _ { 0 } B _ { 1 } - B _ { 1 } A _ { 0 } \qquad { \mathrm { ( t w o d i m e n s i o n s ~ o n l y ) } }
$$

Below, when we consider triangles in three dimensions, it will be the vector cross product forms in equation (21.3.1) that give a generalized formula for the area. Let us also note in passing that the formulas for area are separately linear in each of the six coordinates $a _ { 0 } , a _ { 1 } , b _ { 0 } , b _ { 1 } ,$ $c _ { 0 }$ , and $c _ { 1 }$ .

Equation (21.3.1) can yield a value that is positive, zero, or negative: The area is a signed area. By convention (embodied in equation 21.3.1), the area is positive if a traversal from a to $\mathbf { b }$ to c goes counterclockwise (CCW) around the triangle, and negative if it goes clockwise (CW). The area is zero if and only if the three points are collinear, in which case the triangle is degenerate. (In the formulas that follow, we will generally assume the nondegenerate case.)

The absolute value $\left| \mathcal { A } \right|$ is the (unsigned) “area” of the triangle in the conventional geometrical sense. It can also be calculated directly from the side lengths $d _ { a b }$ , $d _ { b c }$ , and $d _ { c a }$ as follows:

$$
| \mathcal { A } | = \sqrt { s ( s - d _ { a b } ) ( s - d _ { b c } ) ( s - d _ { c a } ) }
$$

where $s$ is half the perimeter,

$$
s \equiv { \frac { 1 } { 2 } } ( d _ { a b } + d _ { b c } + d _ { c a } )
$$

(Does it go without saying that you compute the side lengths by taking the coordinate differences and using the Pythagorean theorem?)

![](images/272ff61df8aab3671b08739de5b058b772702e09874ff4f507079c9da2b5ab7b.jpg)  
Figure 21.3.1. Three kinds of triangle centers. (a) Incircle and incenter; bisectors of the three vertex angles meet at the incenter. (b) Circumcircle and circumcenter; perpendicular bisectors of the edges meet at the circumcenter. (c) Centroid; lines from the edge midpoints to the opposite vertices meet at the centroid.

Related Circles. Every nondegenerate triangle has an inscribed circle or incircle, which is the largest circle that can be drawn inside the triangle. The incircle is tangent to all three sides of the triangle. Lines from its center, the incenter, to each vertex bisect the angle at that vertex (see Figure 21.3.1). If $\mathbf { q }$ is the incenter point, with coordinates $( q _ { 0 } , q _ { 1 } )$ , then its location is given by

$$
q _ { i } = \frac { 1 } { 2 s } ( d _ { b c } a _ { i } + d _ { c a } b _ { i } + d _ { a b } c _ { i } ) ~ ( i = 0 , 1 )
$$

while its radius is given by

$$
r _ { \mathrm { i n } } = \left( \frac { ( s - d _ { a b } ) ( s - d _ { b c } ) ( s - d _ { c a } ) } { s } \right) ^ { 1 / 2 }
$$

Every nondegenerate triangle also has a circumscribed circle or circumcircle, which is the unique circle that goes through its three vertices. Suppose $\mathbf { Q }$ is the circumcenter point, with coordinates $( Q _ { 0 } , Q _ { 1 } )$ . Let $[ b a ] _ { 0 }$ and $[ b a ] _ { 1 }$ denote the coordinate differences $b _ { 0 } - a _ { 0 }$ and $b _ { 1 } - a _ { 1 }$ , respectively; and similarly for $[ c a ] _ { 0 }$ and $[ c a ] _ { 1 }$ . Then, in $2 \times 2$ determinant form,

$$
\begin{array} { c c } { { \displaystyle Q _ { 0 } = a _ { 0 } + \frac { 1 } { 2 } \left| \begin{array} { c c } { { ( [ b a ] _ { 0 } ) ^ { 2 } + ( [ b a ] _ { 1 } ) ^ { 2 } } } & { { [ b a ] _ { 1 } } } \\ { { ( [ c a ] _ { 0 } ) ^ { 2 } + ( [ c a ] _ { 1 } ) ^ { 2 } } } & { { [ c a ] _ { 1 } } } \end{array} \right| } } & { { \left| \begin{array} { c c } { { [ b a ] _ { 0 } } } & { { [ b a ] _ { 1 } } } \\ { { [ c a ] _ { 0 } } } & { { [ c a ] _ { 1 } } } \end{array} \right| } } \\ { { \displaystyle Q _ { 1 } = a _ { 1 } + \frac { 1 } { 2 } \left| \begin{array} { c c } { { [ b a ] _ { 0 } } } & { { ( [ b a ] _ { 0 } ) ^ { 2 } + ( [ b a ] _ { 1 } ) ^ { 2 } } } \\ { { [ c a ] _ { 0 } } } & { { ( [ c a ] _ { 0 } ) ^ { 2 } + ( [ c a ] _ { 1 } ) ^ { 2 } } } \end{array} \right| } } & { { \left| \begin{array} { c c } { { [ b a ] _ { 0 } } } & { { [ b a ] _ { 1 } } } \\ { { [ c a ] _ { 0 } } } & { { [ c a ] _ { 1 } } } \end{array} \right| } } \end{array}
$$

The circumcenter is, by definition, the same distance from all three vertices. Therefore the radius of the circumcircle is

$$
r _ { \mathrm { c i r c u m } } = \sqrt { ( Q _ { 0 } - a _ { 0 } ) ^ { 2 } + ( Q _ { 1 } - a _ { 1 } ) ^ { 2 } }
$$

where $Q _ { 0 }$ and $Q _ { 1 }$ are given above. (Obviously you can save the semi-final results in equation 21.3.7 for this computation, before adding $a _ { 0 }$ or $a _ { 1 }$ .)

Later, in $\ S 2 1 . 6$ , we will be calculating a lot of circumcircles. We use the following simple definition of a structure Circle, and a routine circumcircle() that directly implements equations (21.3.7) and (21.3.8).

![](images/a98a9dab3b012c5b5ae88d737a0a4a3f357f30e389c6dc9f439d4ec7fae2e2aa.jpg)  
Figure 21.3.2. Any point in the plane $\mathbf { q }$ can be expressed as a linear combination of a triangle’s three vertices. The coefficients $( \alpha , \beta , \gamma )$ , called barycentric coordinates, sum to 1 and are proportional to the areas of 4qbc, $\triangle \mathbf { q c a }$ , and $\triangle$ qab, respectively.

struct Circle {Point<2> center;Doub radius;Circle(const Point<2> &cen, Doub rad) : center(cen), radius(rad) {}  
};

Circle circumcircle(Point<2> a, Point<2> b, Point<2> c) { Doub a0,a1,c0,c1,det,asq,csq,ctr0,ctr1,rad2; $\mathtt { a 0 } \ =$ a.x[0] - b.x[0]; a1 $=$ a.x[1] - b.x[1]; $\mathtt { c 0 } \ =$ c.x[0] - b.x[0]; c1 $=$ c.x[1] - b.x[1]; det $=$ a0\*c1 - c0\*a1; if (det $\mathit { \Theta } = = \ 0 . 0$ ) throw("no circle thru colinear points"); det $=$ 0.5/det; asq $=$ a0\*a0 $^ +$ a1\*a1; csq $=$ c0\*c0 $^ +$ c1\*c1; ctr0 $=$ det\*(asq\*c1 - csq\*a1); ctr1 $=$ det\*(csq\*a0 - asq\*c0); rad2 $=$ ctr0\*ctr0 $^ +$ ctr1\*ctr1; return Circle(Point $\mathrm { \tt { < } } 2 \mathrm { \tt { > } }$ (ctr0 $^ +$ b.x[0], ctr1 $^ +$ b.x[1]), sqrt(rad2));

Centroid and Barycentric Coordinates. Distinct from both its incenter and its circumcenter is a triangle’s centroid, or center of gravity, M. This point lies at the intersections of the lines drawn from each vertex to the midpoint of the opposite side. Its coordinates are simply the means of the coordinates of the vertices,

$$
M _ { i } = { \textstyle \frac { 1 } { 3 } } ( a _ { i } + b _ { i } + c _ { i } ) \qquad ( i = 0 , 1 )
$$

The centroid is also the point $\mathbf { M }$ where the areas $\mathcal { A } ( \mathbf { a b } \mathbf { M } )$ , $\mathcal { A } ( \mathbf { b c M } )$ , and $\mathbf { \mathcal { A } } ( \mathbf { c a M } )$ are all equal. In $\ S 2 1 . 7$ we will be using a triangular mesh to interpolate a function. The significance of the centroid is that it is the point where a linearly interpolated function takes on the value that is the mean of the function values at the three vertices.

In fact, generalizing the idea of the centroid, any point $\mathbf { q }$ in the plane can be written as a linear combination of the three vertices a, b, c, with coefficients that sum to unity. These coefficients are called $\mathbf { q }$ ’s barycentric coordinates and can be intuitively expressed in terms of the area formulas for triangles (see Figure 21.3.2). The equations are

$$
\begin{array} { l } { \mathbf { q } = \alpha \mathbf { a } + \beta \mathbf { b } + \gamma \mathbf { c } } \\ { \alpha = \mathcal { A } ( \mathbf { b c q } ) / \mathcal { A } ( \mathbf { a b c } ) } \\ { \beta = \mathcal { A } ( \mathbf { c a q } ) / \mathcal { A } ( \mathbf { a b c } ) } \\ { \gamma = \mathcal { A } ( \mathbf { a b q } ) / \mathcal { A } ( \mathbf { a b c } ) } \end{array}
$$

with, by construction,

$$
\alpha + \beta + \gamma = 1
$$

The first line in equation (21.3.10) is thus equivalent to

$$
{ \bf q } = { \bf c } + \alpha ( { \bf a } - { \bf c } ) + \beta ( { \bf b } - { \bf c } )
$$

This can be viewed as the equation for a coordinate transformation, one that transforms from $( \alpha , \beta )$ coordinates to $( q _ { 0 } , q _ { 1 } )$ coordinates. Evidently, since it is linear, its inverse — the formulas for $\alpha$ and $\beta$ in equation (21.3.10) — must also be linear. But we knew this already, having remarked on the fact that the area formulas (21.3.1) are linear in all their coordinates, so linear in $q _ { 0 }$ and $q _ { 1 }$ in particular. Barycentric coordinates generalize to triangles in three or more dimensions in a useful way, as we will see below.

Note that $\alpha$ , $\beta$ , or $\gamma$ go to 1 as the point $\mathbf { q }$ approaches a, $\mathbf { b }$ , or c, respectively; and that along any edge of the triangle (say $\overline { { a b } }$ ) the coefficient of the opposite vertex (here, $\gamma$ ) vanishes. The point $\mathbf { q }$ is inside the triangle $\triangle$ abc if and only if $\alpha$ , $\beta$ , and $\gamma$ are all positive. In fact, this is a good way to test for a point’s “insideness” in a triangle. (You can of course omit calculating the denominator area in this application.)

Barycentric coordinates are also useful when you want to pick a uniformly random point $\mathbf { q }$ inside $\triangle$ abc: First pick $\alpha$ and $\beta$ as each uniformly random in $( 0 , 1 )$ . Next, if $\alpha + \beta > 1$ , modify them both by $\alpha  1 - \alpha$ and $\beta  1 - \beta$ . Finally, apply equation (21.3.12). The idea is that the first choice of $\alpha$ and $\beta$ is random in the parallelogram spanned by two sides of the triangle; then, if it is on the wrong side of the diagonal, we move it to the correct side by a reflection.

# 21.3.1 Triangles in Three Dimensions

Our favorite triangle is still defined by the three points a, $\mathbf { b }$ , and c, but these are now points in three dimensions, with coordinates (e.g., for a) $( a _ { 0 } , a _ { 1 } , a _ { 2 } )$ . The generalization of the signed area $\mathcal { A }$ (equation 21.3.1) is now a vector area $\vec { \mathcal { A } }$ whose direction is normal to the plane of the triangle and whose length is the area of the triangle. It is most easily written using a vector cross product, defined in three dimensions by

$$
{ \begin{array} { r l } & { \mathbf { A } \times \mathbf { B } = { \left| \begin{array} { l l l } { { \widehat { \mathbf { e } } } _ { 0 } } & { { \widehat { \mathbf { e } } } _ { 1 } } & { { \widehat { \mathbf { e } } } _ { 2 } } \\ { A _ { 0 } } & { A _ { 1 } } & { A _ { 2 } } \\ { B _ { 0 } } & { B _ { 1 } } & { B _ { 2 } } \end{array} \right| } } \\ & { \qquad = ( A _ { 1 } B _ { 2 } - A _ { 2 } B _ { 1 } ) { \widehat { \mathbf { e } } } _ { 0 } + ( A _ { 2 } B _ { 0 } - A _ { 0 } B _ { 2 } ) { \widehat { \mathbf { e } } } _ { 1 } + ( A _ { 0 } B _ { 1 } - A _ { 1 } B _ { 0 } ) { \widehat { \mathbf { e } } } _ { 2 } } \end{array} }
$$

where $\widehat { \mathbf { e } } _ { 0 } , \widehat { \mathbf { e } } _ { 1 }$ , and $\widehat { \mathbf { e } } _ { 2 }$ are respectively the unit vectors $( 1 , 0 , 0 ) , ( 0 , 1 , 0 )$ , and $( 0 , 0 , 1 )$ . Then we have (cf. equation 21.3.1)

$$
{ \begin{array} { r } { 2 { \vec { \mathcal { A } } } ( \mathbf { a b c } ) = ( \mathbf { b } - \mathbf { a } ) \times ( \mathbf { c } - \mathbf { a } ) } \\ { = ( \mathbf { c } - \mathbf { b } ) \times ( \mathbf { a } - \mathbf { b } ) } \\ { = ( \mathbf { a } - \mathbf { c } ) \times ( \mathbf { b } - \mathbf { c } ) } \end{array} }
$$

You calculate the positive scalar area $\mathcal { A } \equiv | \vec { \mathcal { A } } |$ by the usual square-root sum of the squares of $\vec { \mathcal { A } }$ ’s three components; or you can instead use equation (21.3.3), with $d _ { a b } = | \mathbf { a } - \mathbf { b } |$ , etc.

Plane Defined by Triangle. A point $\mathbf { q }$ lies in the plane defined by $\triangle$ abc if and only if the volume of the tetrahedron abcq is zero. The tetrahedral volume, in general, is given by

$$
{ \begin{array} { r l } & { \left| a _ { 0 } \quad a _ { 1 } \quad a _ { 2 } \quad 1 \right| } \\ & { = \left| b _ { 0 } \quad b _ { 1 } \quad b _ { 2 } \quad 1 \right| } \\ & { \left| c _ { 0 } \quad c _ { 1 } \quad c _ { 2 } \quad 1 \right| } \\ & { \qquad \left| d _ { 0 } \quad q _ { 1 } \quad q _ { 2 } \quad 1 \right| } \\ & { \qquad = \left( \mathbf { b } - \mathbf { a } \right) \cdot \left[ \left( \mathbf { c } - \mathbf { a } \right) \times \left( \mathbf { q } - \mathbf { a } \right) \right] } \\ & { \qquad = \left( \mathbf { c } - \mathbf { a } \right) \cdot \left[ \left( \mathbf { q } - \mathbf { a } \right) \times \left( \mathbf { b } - \mathbf { a } \right) \right] } \\ & { \qquad = \left( \mathbf { q } - \mathbf { a } \right) \cdot \left[ \left( \mathbf { b } - \mathbf { a } \right) \times \left( \mathbf { c } - \mathbf { a } \right) \right] } \end{array} }
$$

where “	” signifies vector dot product. You can also cyclically permute a, $\mathbf { b }$ , and c in the above equation, for a seemingly infinite number of variations of the same formula!

The volume $\mathcal { V }$ is signed and is positive if $\triangle$ abc is counterclockwise when viewed from outside (side away from $\mathbf { q }$ ), that is, the right-hand rule gives an outwardpointing normal.

The last form in equation (21.3.15) is particularly nice, because setting it to zero gives the equation satisfied by any point $\mathbf { q }$ in the plane defined by $\triangle$ abc:

$$
\mathbf { q } \cdot \mathbf { N } = D
$$

with

$$
\begin{array} { r l } & { \mathbf { N } = \left( \mathbf { b } - \mathbf { a } \right) \times \left( \mathbf { c } - \mathbf { a } \right) \quad ( \mathrm { o r c y c l i c ~ p e r m u t a t i o n ~ o f ~ } \mathbf { a } , \mathbf { b } , \mathbf { c } ) } \\ & { D = \mathbf { a } \cdot \mathbf { N } \quad ( \mathrm { o r , f o r ~ t h a t ~ m a t t e r } ) \quad = \mathbf { b } \cdot \mathbf { N } = \mathbf { c } \cdot \mathbf { N } } \end{array}
$$

We could also divide equation (21.3.16) by $| \mathbf { N } |$ , in which case the vector on the left will be $\hat { \bf N } = { \bf N } / | { \bf N } |$ , the unit vector normal to the plane, and $\widehat { D } = D / | \mathbf { N } |$ will be the plane’s distance from the origin.

With the same machinery, we can readily project any point $\mathbf { p }$ into a new point $ { \mathbf { b } } ^ { \prime }$ that lies in the plane of $\triangle$ abc:

$$
{ \bf p } \longrightarrow { \bf p } ^ { \prime } = { \bf p } + \frac { [ ( { \bf a } - { \bf p } ) \cdot { \bf N } ] { \bf N } } { | { \bf N } | ^ { 2 } }
$$

where $\mathbf { N }$ is as above. For a in this formula, you can substitute $\mathbf { b } , \mathbf { c }$ , or any other point in the plane.

We can project one triangle into the plane defined by another triangle by projecting its three points in turn. (This is a very common operation in rendering a triangulated three-dimensional model in the two-dimensional “camera plane” of your computer’s screen.)

Barycentric Coordinates. Barycentric coordinates are valid in three dimensions for points $\mathbf { q }$ in the triangle’s plane, and equation (21.3.10), in particular, still holds. To compute $( \alpha , \beta )$ , one can in principle calculate the various $\mathcal { A }$ ’s from (21.3.14), but an easier equivalent calculation is

$$
\begin{array} { r l } & { \alpha = \frac { \mathbf { b } ^ { \prime 2 } ( \mathbf { a } ^ { \prime } \cdot \mathbf { q } ^ { \prime } ) - ( \mathbf { a } ^ { \prime } \cdot \mathbf { b } ^ { \prime } ) ( \mathbf { b } ^ { \prime } \cdot \mathbf { q } ^ { \prime } ) } { \mathbf { a } ^ { \prime 2 } \mathbf { b } ^ { \prime 2 } - ( \mathbf { a } ^ { \prime } \cdot \mathbf { b } ^ { \prime } ) ^ { 2 } } } \\ & { \beta = \frac { \mathbf { a } ^ { \prime 2 } ( \mathbf { b } ^ { \prime } \cdot \mathbf { q } ^ { \prime } ) - ( \mathbf { a } ^ { \prime } \cdot \mathbf { b } ^ { \prime } ) ( \mathbf { a } ^ { \prime } \cdot \mathbf { q } ^ { \prime } ) } { \mathbf { a } ^ { \prime 2 } \mathbf { b } ^ { \prime 2 } - ( \mathbf { a } ^ { \prime } \cdot \mathbf { b } ^ { \prime } ) ^ { 2 } } } \end{array}
$$

(compute identical denominators only once) where

$$
\mathbf { a } ^ { \prime } \equiv \mathbf { a } - \mathbf { c } , \qquad \mathbf { b } ^ { \prime } \equiv \mathbf { b } - \mathbf { c } , \qquad \mathbf { q } ^ { \prime } \equiv \mathbf { q } - \mathbf { c }
$$

By the way, if $\mathbf { q }$ is not in the plane of $\triangle$ abc, you can still use equation (21.3.19). In that case, you get the $( \alpha , \beta )$ coordinates of the projected point in the plane. Also, notice what happens in the special case that $\triangle$ abc is a right triangle, with right vertex c, and with sides $\overline { { a c } }$ and $\overline { { b c } }$ of unit length, i.e., ${ d } _ { a c } = { d } _ { b c } = 1$ . Then the coordinate transformations, in both directions, are simply

$$
\begin{array} { c } { \displaystyle \mathbf { q } = \mathbf { c } + \alpha ( \mathbf { a } - \mathbf { c } ) + \beta ( \mathbf { b } - \mathbf { c } ) } \\ { \displaystyle [ \alpha , \beta ] = [ ( \mathbf { a } - \mathbf { c } ) \cdot ( \mathbf { q } - \mathbf { c } ) , ( \mathbf { b } - \mathbf { c } ) \cdot ( \mathbf { q } - \mathbf { c } ) ] } \end{array}
$$

In other words, we project into an orthonormal coordinate system in the plane by a simple change of origin (to c) and dot products with the two “axes” a  c and $\mathbf b - \mathbf c$ .

Frequently, barycentric coordinates are the coordinates of choice for operations in a plane in three dimensions that is (or can be) specified by a triangle. A trivial example is that we can test whether a projected point $\mathbf { p } ^ { \prime }$ is inside or outside of $\triangle$ abc by using equation (21.3.19) (or, if applicable, 21.3.21) to get $\alpha$ and $\beta$ , and then checking that $\alpha$ , $\beta$ , and $\gamma = 1 - \alpha - \beta$ are all positive.

Angle Between Two Triangles. The dihedral angle between two triangles (with a common edge, say) is the same as the angle between the normal vectors of the two triangles. The normal vectors are given by the vector area formula (21.3.14). The angle is best computed using equation (21.4.13), in the next section.

# CITED REFERENCES AND FURTHER READING:

Bowyer, A. and Woodwark, J. 1983, A Programmer’s Geometry (London: Butterworths), Chapter 4.

Schneider, P.J. and Eberly, D.H. 2003, Geometric Tools for Computer Graphics (San Francisco: Morgan Kaufmann), $\ S 3 . 5$ and Appendix C.

López-López, F.J. 1992, “Triangles Revisited,” in Graphics Gems III, Kirk, D., ed. (Cambridge, MA: Academic Press).

Glassner, A.S. 1990, “Useful 3D Geometry,” in Graphics Gems, Glassner, A.S., ed. (San Diego: Academic Press).

# 21.4 Lines, Line Segments, and Polygons

A line is defined by any two points through which it passes. Call them a and b. As in $\ S 2 1 . 1$ , the points can be two-dimensional, if the domain of interest is a plane, or three-dimensional (or higher), if the line is embedded in a higher-dimensional space. For now, consider only the two-dimensional case.

Parametrically, any point c that lies on the line defined by a and $\mathbf { b }$ must be a linear combination of those two points. One way to write this is

$$
\mathbf { c } = \mathbf { a } + s ( \mathbf { b } - \mathbf { a } ) ( - \infty < s < \infty )
$$

where $s$ is a parameter along the line. The chosen normalization is to make $s = 0$ at a and $s = 1$ at $\mathbf { b }$ . The part of the line between a and $\mathbf { b }$ has $0 \leq s \leq 1$ and is a line segment, denoted ab. The whole line is denoted ab.

The easiest way to get the equation satisfied by all points c on the line $\stackrel {  } { \mathbf { a b } }$ is to take the vector cross product of equation (21.4.1) with $\mathbf { ( b - a ) }$ on the right. Using the fact that the cross product of any vector with itself is zero, we get

$$
\mathbf { c } \times ( \mathbf { b } - \mathbf { a } ) = \mathbf { a } \times \mathbf { b }
$$

or writing out the components,

$$
c _ { 0 } ( b _ { 1 } - a _ { 1 } ) - c _ { 1 } ( b _ { 0 } - a _ { 0 } ) = a _ { 0 } b _ { 1 } - a _ { 1 } b _ { 0 }
$$

which is indeed a linear relation between the coordinates $c _ { 0 }$ and $c _ { 1 }$ . While it is tempting to divide this equation by $b _ { 0 } - a _ { 0 }$ to get an equation in that old familiar high school form “ ${ \dot { \boldsymbol { y } } } = m { \boldsymbol { x } } + b$ ,” one should often resist that temptation since, as written, equation (21.4.3) remains valid for the case of a vertical line, when $b _ { 0 } - a _ { 0 } = 0$ .

Intersection of Two Lines. In the plane, two lines $\stackrel {  } { \mathbf { a b } }$ and most always intersect. We can solve for the point of intersection by equating the two lines’ parametric forms,

$$
{ \bf a } + s ( { \bf b } - { \bf a } ) = { \bf x } - t ( { \bf y } - { \bf x } )
$$

and then solving the two equations (components 0 and 1) for the two unknowns $s$ and $t$ . The result is

$$
\begin{array} { c c l } { s = \displaystyle \frac { ( \mathbf { x } - \mathbf { y } ) \times ( \mathbf { a } - \mathbf { x } ) } { ( \mathbf { b } - \mathbf { a } ) \times ( \mathbf { x } - \mathbf { y } ) } = \frac { ( x _ { 0 } - y _ { 0 } ) ( a _ { 1 } - x _ { 1 } ) - ( x _ { 1 } - y _ { 1 } ) ( a _ { 0 } - x _ { 0 } ) } { ( b _ { 0 } - a _ { 0 } ) ( x _ { 1 } - y _ { 1 } ) - ( b _ { 1 } - a _ { 1 } ) ( x _ { 0 } - y _ { 0 } ) } } \\ { t = \displaystyle \frac { ( \mathbf { a } - \mathbf { x } ) \times ( \mathbf { b } - \mathbf { a } ) } { ( \mathbf { b } - \mathbf { a } ) \times ( \mathbf { x } - \mathbf { y } ) } = \frac { ( a _ { 0 } - x _ { 0 } ) ( b _ { 1 } - a _ { 1 } ) - ( a _ { 1 } - x _ { 1 } ) ( b _ { 0 } - a _ { 0 } ) } { ( b _ { 0 } - a _ { 0 } ) ( x _ { 1 } - y _ { 1 } ) - ( b _ { 1 } - a _ { 1 } ) ( x _ { 0 } - y _ { 0 } ) } } \end{array}
$$

Of course, the special case of parallel lines with no intersection is indicated by the vanishing of the denominators.

All those cross products might make you think that equation (21.4.5) has a geometrical interpretation. Indeed so. In Figure 21.4.1, the lines intersect at o. Segment $\overline { { { \bf { X 0 } } } }$ is therefore just $\mathbf { \overline { { X Y } } }$ scaled by $t$ , while $\overline { { \mathbf { a 0 } } }$ is similarly $\overline { { \mathbf { a b } } }$ scaled by $s$ . The area of $\triangle$ oxa is therefore given (cf. equation 21.3.1) by

$$
2 \mathcal { A } ( \mathbf { o x } \mathbf { a } ) = s t \ ( \mathbf { x } - \mathbf { y } ) \times ( \mathbf { a } - \mathbf { b } )
$$

![](images/2d9ca76a8f3a5df7e29daa09db25332994de16c5fdef319127f50ceeba84d65f.jpg)  
Figure 21.4.1. Geometrical construction that yields the intersection point of two lines in terms of ratios of triangle areas. See text for details.

By linearity of a triangle’s area with its height (holding the base fixed), we also have

$$
\mathcal { A } ( \mathbf { o x a } ) / \mathcal { A } ( \mathbf { y x a } ) = t \qquad \mathcal { A } ( \mathbf { o x a } ) / \mathcal { A } ( \mathbf { b x a } ) = s
$$

Equation (21.4.5) follows immediately from these relations and equation (21.3.1).

Point-to-Line Distance. What is the perpendicular distance $d$ from an arbitrary point $\mathbf { q }$ to the line ab that passes through points a and b? Evidently $d$ is the height of $\triangle$ abq when its base is the segment ab. Therefore, from the schoolbook “one-half base times height” formula,

$$
d = { \frac { 2 { \mathcal { A } } ( \mathbf { a b q } ) } { | \mathbf { a - b } | } } = { \frac { ( q _ { 0 } - b _ { 0 } ) ( a _ { 1 } - b _ { 1 } ) - ( q _ { 1 } - b _ { 1 } ) ( a _ { 0 } - b _ { 0 } ) } { { \sqrt { ( a _ { 0 } - b _ { 0 } ) ^ { 2 } + ( a _ { 1 } - b _ { 1 } ) ^ { 2 } } } } }
$$

Note that $d$ is signed, positive if it is to the left of the directed line from $\mathbf { a }$ to $\mathbf { b }$ , negative if it is to the right, and a good segue to our next topic.

# 21.4.1 Line Segment Intersections and “Left-Of" Relations

You can use equation (21.4.5) to test whether two line segments, $\overline { { \mathbf { a b } } }$ and $\mathbf { \overline { { X y } } }$ , intersect: Calculate $s$ and $t$ and then check if they are both in the range $( 0 , 1 )$ . (To keep our discussion brief, we won’t say much here, or in what follows, about the various degenerate cases where $s$ or $t$ or both are exactly 0 or 1. These are straightforward to figure out if your application so demands.)

A related, but slightly different, approach is to use the fact that the formulas for triangle areas given in equation (21.3.1) are signed. This means that, as equivalent statements, we have

$$
\begin{array} { r } { \mathcal { A } ( \mathbf { a b c } ) > 0 \quad \Longleftrightarrow \quad \left[ \begin{array} { l } { \mathbf { c } \mathrm { ~ i s ~ t o ~ t h e ~ } l e f t \mathrm { ~ o f ~ l i n e ~ } \overleftrightarrow { \mathbf { a b } } } \\ { \mathrm { ~ w h e n ~ i t ~ i s ~ t r a v e r s e d ~ i n ~ } } \\ { \mathrm { t h e ~ d i r e c t i o n ~ f r o m ~ } \mathbf { a } \mathrm { ~ t o ~ } \mathbf { b } } \end{array} \right] } \end{array}
$$

while $\mathbf { \mathcal { A } } ( \mathbf { a b c } ) < 0$ implies that c is to the right of the same line. We refer to either statement in (21.4.9) as a left-of relation.

A necessary and sufficient condition for two segments $\overline { { \mathbf { a b } } }$ and $\mathbf { \overline { { X y } } }$ to intersect is that $\mathbf { X }$ and $\mathbf { y }$ be on opposite sides of $\stackrel {  } { \mathbf { a b } }$ , and a and b be on opposite sides of . (We again omit discussion of the various special cases of collinearity.) This test, using the triangle area formulas in equation (21.3.1), involves evaluating four leftof relations, each computationally a cross product, which is just slightly more work than computing $s$ and $t$ (which share a denominator). However, you can sometimes use the same cross products, once computed, in other parts of your calculation. So, it is often a toss-up whether to use the $^ { 6 6 } S$ , $t ^ { \prime \prime }$ method or the “left-of” method — you should consider both.

Table 21.4.1. Relationship between two line segments classified by the signs of the areas of various triangles. Refer to Figure 21.4.2 for an illustration of each case.   

<table><tr><td rowspan=1 colspan=1>Fig.</td><td rowspan=1 colspan=1>△abx</td><td rowspan=1 colspan=1>△aby</td><td rowspan=1 colspan=1>△xya</td><td rowspan=1 colspan=1>△xyb</td><td rowspan=1 colspan=1>Intersection</td><td rowspan=1 colspan=1>Hull</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>1+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>1+</td><td rowspan=1 colspan=1>ab× xyab × xy</td><td rowspan=1 colspan=1>□axby□aybx</td></tr><tr><td rowspan=1 colspan=1>34</td><td rowspan=1 colspan=1>+1</td><td rowspan=1 colspan=1>1+</td><td rowspan=2 colspan=1>+</td><td rowspan=5 colspan=1>1+++1</td><td rowspan=7 colspan=1>axxy&gt;ba xxyabxxyxabxabxabyx xab</td><td rowspan=7 colspan=1>△ayx△byx△bxy△axy△yba△xba△xab△yab</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+</td><td rowspan=3 colspan=1>+1+</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>external</td><td rowspan=4 colspan=1>□ayxb□abxyabxyaxyb</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>external</td></tr><tr><td rowspan=2 colspan=1>1314</td><td rowspan=2 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>external</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>external</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+1</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+1</td><td rowspan=1 colspan=2>Not possible!Not possible!</td></tr></table>

Table 21.4.1 enumerates the 16 cases that you get if you compute all four possible “left-of” tests for two line segments. (Actually, only 14 are geometrically possible!) The table classifies each possibility as to whether the segments intersect (intersection denoted by $\times .$ , not to be confused with vector cross product!), whether the unidirectional extension of one segment (a ray) intersects the other segment, or (lastly) whether an ordinary line intersection occurs external to both segments. Also shown for each case is the outer hull of the two segments (the smallest triangle or quadrilateral enclosing both segments) and how it is traversed in clockwise order. Figure 21.4.2 shows an example of each possibility.

You can use the table to find combinations that test for specific circumstances.

![](images/b1758e3c22fd6c85a0f3f33ee5d00f9e35f0af2a3b83a5cc483edee1317af789.jpg)  
Figure 21.4.2. Two line segments, $a b$ and $x y$ , define four triangles (4abx, 4aby, $\triangle x y a$ , and $\triangle x y b )$ , each of which can have positive or negative area. Of the 16 combinations of signs, 14 (shown here) correspond to to possible intersection relationships between the line segments or their extensions as rays.

For example, if you need a test for whether the ray $\vec { \mathbf { a b } }$ intersects the segment $\mathbf { \overline { { X y } } }$ (including the possibility of the segments intersecting), you examine rows 1, 2, 3, and 6 in the table and read off a test that involves just three left-of relations:

$$
\mathbf { \mathcal { A } } ( \mathbf { a b x } ) \mathbf { \mathcal { A } } ( \mathbf { a b y } ) < 0 \qquad \mathrm { a n d } \qquad \mathbf { \mathcal { A } } ( \mathbf { a b y } ) \mathbf { \mathcal { A } } ( \mathbf { x y a } ) > 0
$$

Of course there are exactly equivalent tests using $s$ and $t$ , for this example (with $s$ and $t$ as in equation 21.4.4) $s > 0$ and $0 < t < 1$ .

Angle Between Two Vectors. Suppose that $\mathbf { U }$ and $\mathbf { V }$ are difference vectors along each of two lines, and that $\theta$ is the angle between the lines (measured from $\mathbf { U }$ to $\mathbf { V }$ ). In the previous notation, $\mathbf { U } = \mathbf { y } - \mathbf { x }$ and $\mathbf { V } = \mathbf { b } - \mathbf { a }$ . Elementary vector analysis tells us that

$$
\begin{array} { r } { \mathbf { U } \cdot \mathbf { V } = U _ { 0 } V _ { 0 } + U _ { 1 } V _ { 1 } = | \mathbf { U } | | \mathbf { V } | \cos ( \theta ) } \\ { \mathbf { U } \times \mathbf { V } = U _ { 0 } V _ { 1 } - U _ { 1 } V _ { 0 } = | \mathbf { U } | | \mathbf { V } | \sin ( \theta ) } \end{array}
$$

Many people try to get $\theta$ by using one or the other of the above relations, computing the vector norms and taking an inverse cosine or inverse sine. Big mistake! Not only are there quadrant ambiguities in the inverse trig functions, but there are also angles near the flat extrema of the sine and cosine functions where you can lose up to half of your significant figures in the answer. Not to mention the need to calculate square roots for the norms! The better approach is

$$
\theta = \mathtt { a t a n 2 } ( \mathbf { U } \times \mathbf { V } , \mathbf { U } \cdot \mathbf { V } ) = \mathtt { a t a n 2 } ( U _ { 0 } V _ { 1 } - U _ { 1 } V _ { 0 } , U _ { 0 } V _ { 0 } + U _ { 1 } V _ { 1 } )
$$

where atan2() is C’s or $\mathrm { C } { + } { + }$ ’s quadrant-sensitive arctangent function. That function allows either of its arguments to be zero and returns a value in the range $- \pi / 2$ to $\pi / 2$ . (An identical function exists in Fortran and most other languages.)

# 21.4.2 Lines in Three Dimensions

The immediate generalization of equation (21.4.12) to three-dimensional space gives the angle between two 3-vectors,

$$
\boldsymbol { \theta } = \mathsf { a t a n 2 } \left( | \mathbf { U } \times \mathbf { V } | , \mathbf { U } \cdot \mathbf { V } \right)
$$

Note the occurrence of the modulus of the vector cross product, which requires taking a square root.

Brevity constraints allow us to say only a little more about lines in three-dimensional space. The parameterization

$$
\mathbf { c } = \mathbf { a } + s \mathbf { v } ( - \infty < s < \infty )
$$

(equation 21.4.1 with $\mathbf { v } \equiv \mathbf { b } - \mathbf { a }$ ) still works, with a, $\mathbf { V }$ , and c now points in 3-space. The parameter $s$ at which a line intersects a plane specified by $\mathbf { N }$ and $D$ (see equation 21.3.16) is given by

$$
s = { \frac { D - \mathbf { a } \cdot \mathbf { N } } { \mathbf { v } \cdot \mathbf { N } } }
$$

with the denominator vanishing if the line is parallel to the plane.

The closest approach of a line to a point $\mathbf { q }$ occurs when

$$
s = { \frac { \left( \mathbf { q } - \mathbf { a } \right) \cdot \mathbf { v } } { | \mathbf { v } | ^ { 2 } } }
$$

You can also use this to see whether a line intersects a sphere in 3-space: Calculate the closest point on the line to the sphere’s center, and then check if the distance is less than the sphere’s radius (or compare squares of distances to avoid the square root).

Two lines, call them $\mathbf { a } + s \mathbf { v }$ and $\mathbf { x } + t \mathbf { u }$ , will not, in general, share a common point; rather, they will be skew to one another. However, their points of closest approach can be calculated as [2]

$$
s = { \frac { \operatorname* { d e t } \{ ( \mathbf { a } - \mathbf { x } ) , \mathbf { u } , \mathbf { u } \times \mathbf { v } \} \} } { | \mathbf { u } \times \mathbf { v } | ^ { 2 } } } \qquad t =  \frac { \operatorname* { d e t } \{ ( \mathbf { a } - \mathbf { x } ) , \mathbf { v } , \mathbf { u } \times \mathbf { v } \} \} }
$$

where det is the $3 \times 3$ determinant whose columns are the indicated 3-vectors. The denominator vanishes if the lines are parallel. If you really must check for an actual intersection, plug these values for $s$ and $t$ into the parametric forms for each line, and check whether the distance between two points thus obtained is less than some roundoff tolerance.

A common operation in computer graphics is to test whether a line intersects a triangle in three dimensions. To do this with methods already discussed, use equation (21.3.17) to get $\mathbf { N }$ and $D$ for the triangle’s plane. Then use equations (21.4.14) and (21.4.15) to get the line’s intersection with that plane. Finally, use equation (21.3.19) to get the barycentric coordinates $\alpha$ and $\beta$ of the intersection. If $\alpha$ , $\beta$ , and $\gamma \equiv 1 - \alpha - \beta$ are all positive, then the intersection is inside the triangle. See [4,1] for various ways to streamline this procedure.

![](images/4c9928eddd49e7475338713148160b1e2fbd0b4bc7df6b0d885e139a7fe9b451.jpg)  
Figure 21.4.3. Polygons are classified as simple if they have no intersecting edge, as in (a) and (b), or complex (c) otherwise. Simple polygons are either convex (a) or concave (b).

# 21.4.3 Polygons

We define a polygon as a vector of $N$ points (vertices), numbered from 0 to $N - 1$ , and the $N$ directed line segments that connect them in cyclic order, that is 0 to 1, 1 to 2, : : :, $N - 2$ to $N - 1$ , and (importantly!) $N - 1$ to 0. (In some formulas below we will use the convention that vertex $N$ is to be taken as meaning vertex 0.)

We consider two polygons to be the same if they differ only by a cyclical renumbering of the points, so that all their line segments are the same. However, if we reverse the order of traversing the points, we consider the resulting polygon to be different. (For example, the sign of its area will change.) If the boundary of a region cannot be traversed by a single cyclical vector (e.g., the region between an outer square and an enclosed triangle), we don’t call it a polygon; other conventions are of course also possible.

With the definition given, it is useful to classify a polygon as either simple, meaning that none of its $N$ line segments intersect, or complex if there are one or more segment intersections. We classify simple polygons according to whether they are convex or concave. A convex polygon can be defined either by (i) all $N ( N { - } 1 ) / 2$ line segments connecting two vertices lie in its interior (or on its boundary), or (ii) its exterior angles all have the same sign (zeros allowed). Whichever property is taken as the definition, the other becomes a theorem. Figure 21.4.3 shows examples of the three types.

For simple polygons, the sum of the exterior angles is always $\pm 2 \pi$ . That is, you turn through exactly one circle in driving around the polygon. If the polygon is concave, then the sign of the exterior angles must be taken into account when doing the sum. This is shown in Figure 21.4.4. The sign of the $2 \pi$ is positive for a counterclockwise (CCW) traversal, negative for clockwise (CW).

Complex (that is, self-intersecting) polygons can also have exterior angles that sum to $2 \pi$ , as the polygon in Figure 21.4.3(c), so the exterior angles do not provide, in general, any magical way of finding intersections. However, one small bit of magic does exist: If the exterior angles of a polygon are all of one sign (or zero), and if they sum to $\pm 2 \pi$ , then the polygon is both simple and convex. This provides a very rapid way to test for the simple-and-convex case, but it does not distinguish between simple-concave and complex polygons. Doing so requires a detailed check for intersecting edges (which we will implement in code below).

Winding Number. If you sit on a point p in the plane, and watch someone drive around a polygon, then they will drive around you some net integer number of times (with the usual sign convention, CCW being positive). This is the polygon’s winding number with respect to a point. For simple polygons, the winding number is 1 for points inside a CCW polygon, $^ { - 1 }$ for points inside a CW polygon, and 0 for points outside. For complex polygons, however, there are no simple rules. Figure 21.4.5 shows a complicated case. Note that interior regions of a complex polygon can have winding number 0, so a point’s winding number (alone) does not determine whether it is inside or outside a complex polygon. Note also that the sum of a polygon’s exterior angles, divided by $2 \pi$ , is not necessarily the winding number of that polygon with respect to any point in the plane.

![](images/68c528bf86d3264b5bb94cedb642b436956d9d244264ac3dafa4b07f4d4bf54a.jpg)  
Figure 21.4.4. The exterior angles of simple polygons sum to one full circle. (a) If the polygon is convex, all the angles have the same sign. (b) If the polygon is concave, one or more angles (here, the shaded angle) has opposite sign.

![](images/93cf8b562a3520a8f1da1158e40f3bf7d8ada969a780320e8864c9881e5be34b.jpg)  
Figure 21.4.5. Complex polygon with different winding numbers (indicated by integers) around points in different regions. The total winding number of the polygon (sum of exterior angles divided by $2 \pi$ ) is 3, a value not realized in any single region. Note that interior regions can have winding number 0.

Doubtless the worst way to compute a polygon’s winding number with respect to a point $\mathbf { q }$ is to add up the $N$ incremental angles between $\mathbf { q }$ and consecutive vertices ${ \bf p } _ { i }$ of the polygon, that is,

$$
\operatorname { W . N . } ( { \mathbf { q } } ) = \frac { 1 } { 2 \pi } \sum _ { i = 0 } ^ { N - 1 } \angle ( { \mathbf { p } } _ { i + 1 } { \mathbf { q } } { \mathbf { p } } _ { i } )
$$

(with the usual convention $\mathbf { p } _ { N } \equiv \mathbf { p } _ { 0 } ,$ ). Even using the trick in equation (21.4.12) to get the angles, there is an enormous amount of unnecessary computation in this approach.

Instead, we can observe that if a polygon winds $M$ times around $\mathbf { q }$ , then its edges must cross any ray from $\mathbf { q }$ to infinity a net of exactly $M$ times, where ray crossings in the CCW direction are counted as positive, CW as negative. In particular, if we take the ray to be the horizontal ray to the right of $\mathbf { q }$ , we can immediately reject edges that fail to cross the horizontal line that contains $\mathbf { q }$ , and then check for the ray crossing (and its sign) with a single “left-of” test [5]. These ideas are embodied in the following routine.

polywind(const vector< Point<2> > &vt, const Point<2> &pt) {

Return the winding number of a polygon (specified by a vector of vertex points vt) around an arbitrary point pt.

Int i,np, wind $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
Doub d0,d1,p0,p1,pt0,pt1;   
np $=$ vt.size();   
pt0 $=$ pt.x[0];   
pt1 $=$ pt.x[1];   
p0 $=$ vt[np-1].x[0]; Save last vertex as ”previous” to first.   
p1 $=$ vt[np-1].x[1];   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<np; $\dot { \bf 1 } + +$ ) { Loop over edges. $\mathrm { ~ d 0 ~ } =$ vt[i].x[0]; d1 $=$ vt[i].x[1]; if (p1 $< =$ pt1) { if (d1 $>$ pt1 && Upward-crossing edge. Is pt to its left? (p0-pt0)\*(d1-pt1)-(p1-pt1)\*(d0-pt0) > 0) wind++; } else { if (d1 $< =$ pt1 && Downward-crossing edge. Is pt to its right? (p0-pt0)\*(d1-pt1)-(p1-pt1)\*(d0-pt0) < 0) wind-} $\mathtt { p 0 = d 0 }$ ; Current vertex becomes previous one. $\mathtt { p 1 } \mathtt { = d 1 }$ ;   
}   
return wind;

Is there a similarly efficient way to find the total winding number of a polygon ${ \bf p } _ { i }$ $( i \ : = \ : 0 , \ldots , N \ : - \ : 1 )$ , that is, the sum of its exterior angles divided by $2 \pi 2$ Yes. Consider the derived polygon whose vertex points $\mathbf { q } _ { i }$ are given by the vector differences

$$
\mathbf { q } _ { i } = \mathbf { p } _ { i + 1 } - \mathbf { p } _ { i } \qquad ( i = 0 , \ldots , N - 1 )
$$

Then the winding number of this derived polygon around the origin is just the total winding number of the original polygon. (Draw a picture if this isn’t immediately obvious to you.) The routine polywind() can be used for the computation.

Point Inside Polygon. How can you tell whether an arbitrary point $\mathbf { q }$ is inside or outside a polygon [5]? Let us first assume that your polygon is known to be simple. For simple polygons, two commonly used approaches are the “winding number method” and the “Jordan curve theorem method.” However, when these are each implemented efficiently, they become virtually identical!

The winding number method is simply to compute the winding number of the polygon around the point (e.g., using polywind(), above). If the answer is $\pm 1$ , then the point is inside the polygon. If it is zero, it is outside. Any other answer indicates that the polygon wasn’t simple as assumed.

The Jordan curve theorem method observes that any ray from the point to infinity will cross the polygon an odd number of times if the point is inside, or an even number of times if it is outside [Figure 21.4.6(a)]. If we implemented this in code, it would be almost identical to the code in polywind except for one detail: Instead of incrementing or decrementing a counter at each ray crossing (according to the direction of the crossing), we would always increment it. Then, at the end, we would check whether the counter is even or odd. But if polywind as written returns 0, it must have encountered the same number of increments as decrements, hence an even number of crossings. And if it returns $\pm 1$ (the only other possible value for a simple polygon), it must similarly have encountered an odd number. So the two methods are really the same.

![](images/10c21a0c015b20914ff2b9698ec18a8417e84f33f77ed6e6bf8c0221220b557c.jpg)  
Figure 21.4.6. Is a point inside a polygon? (a) For a simple polygon, either the winding number, or the Jordan curve theorem (even or odd number of crossings of a ray) can be used. (b) For complex polygons, there is no simple test.

What if your polygon is not simple? As Figure 21.4.6(b) illustrates, you are in deep waters. Both the winding number method and the Jordan curve theorem method will say that the upper point in the figure is inside the complex polygon shown, and this seems intuitively correct. However, both methods will say that the lower point is outside the polygon. Indeed, there are some self-consistent ways of defining “insideness” for complex polygons that make this the case. The result is so counterintuitive, however, as to be useless in most practical applications. It is generally better just to avoid using the idea of “insideness” with complex polygons.

Classification of Polygons. We are now in a position to combine several of the ideas already introduced into a function that classifies any polynomial as either simple or complex, and (if it is simple) whether it is convex or concave, and whether it is CCW (total winding number 1) or CW (total winding number $^ { - 1 }$ ).

# Int ispolysimple(const vector< Point<2> $>$ &vt) {

Classifies a polygon specified by a vector of vertex points vt. Returns 0 if the polygon is complex (has intersecting edges). Returns $\pm 1$ if it is simple and convex. Returns $\pm 2$ if it is simple and concave. The sign of the returned value indicates whether the polygon is CCW $( + )$ or CW $( - )$ .

Int i,ii,j,jj,np,schg ${ \left. = 0 \right. }$ ,wind=0; Initialize sign change and winding number.   
Doub p0,p1,d0,d1,pp0,pp1,dd0,dd1,t,tp,t1,t2,crs,crsp $_ { 1 = 0 }$ .0;   
$\mathrm { n p } \ =$ vt.size();   
$\mathtt { p 0 } \ =$ vt[0].x[0]-vt[np-1].x[0];   
$\mathtt { p 1 } \ =$ vt[0].x[1]-vt[np-1].x[1];   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ,ii=1; i<np; $\dot { \bf 1 } + +$ ,ii++) { Loop over edges. if (ii $\begin{array} { r } { \mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ n p ~ } . } \end{array}$ ) $ { \mathrm { ~ \textrm ~ { ~ ~ } ~ } }  { \mathrm { 1 } }  { \mathrm { 1 } } { \mathrm { 1 } } = \mathrm { ~ 0 ~ }$ ; d0 $=$ vt[ii].x[0]-vt[i].x[0]; d1 $=$ vt[ii].x[1]-vt[i].x[1]; crs $=$ p0\*d1-p1\*d0; Cross product at this vertex. if (crs\*crsp $<$ 0) schg $= ~ 1$ ; Sign change (i.e., concavity) found. if (p1 <= 0.0) { Winding number logic as in polywind. if (d1 $> ~ 0 , 0$ && crs $> ~ 0 . 0$ ) wind++; } else { if (d1 $< = ~ 0 . 0$ && crs < 0.0) wind--; } $\mathtt { p 0 = d 0 }$ ; $\mathtt { p 1 } \mathtt { = d 1 }$ ; if (crs $! = ~ 0 . 0$ ) crsp = crs; Save previous cross product only if it has a   
} sign!

if (abs(wind) $\smash  ! = ~ 1 2$ ) return 0; Can already conclude polygon is complex. if (schg $\scriptstyle = = 0$ ) return (wind>0? 1 : -1); Polygon is simple and convex. Drat, we’ve exhausted all the quick tricks and now have to check all pairs of edges for intersections:

for ( $\scriptstyle { \dot { 1 } } = 0$ ,ii=1; i<np; $\dot { \bf 1 } + +$ ,ii $^ { + + }$ ) { if (i $\mathrm { \Omega _ { i } ~ = = ~ \mathrm { \Omega _ { n p } } }$ ) $\scriptstyle \dot { 1 } \dot { 1 } = 0$ ; $\mathtt { d 0 } \ =$ vt[ii].x[0]; ${ \tt d } 1 \ =$ vt[ii].x[1]; $\mathtt { p 0 } \ =$ vt[i].x[0]; $\mathtt { p 1 } \ =$ vt[i].x[1]; t ${ \bf \Phi } : { \bf p } = { \bf \Phi } 0 . 0$ ; for ( $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { 1 } } } + 1$ ,jj $= \dot { 1 } + 2$ ; j<np; j++,jj $^ { + + }$ ) { if (jj $\begin{array} { r } { \mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ n p ~ } . } \end{array}$ ) {if ( $\scriptstyle { \dot { 1 } } = = 0$ ) break; jj=0;} dd0 $=$ vt[jj].x[0]; dd1 $=$ vt[jj].x[1]; $\begin{array} { r l } { \tplus } & { { } = } \end{array}$ (dd0-d0) $^ *$ (p1-d1) - (dd1-d1) $^ *$ (p0-d0); if (t\*tp $< = ~ 0 . 0$ && j>i+1) { First loop is only to compute starting tp, pp0 $=$ vt[j].x[0]; hence test on j. pp1 $=$ vt[j].x[1]; t1 = (p0-dd0)\*(pp1-dd1) - (p1-dd1)\*(pp0-dd0); t2 = (d0-dd0)\*(pp1-dd1) - (d1-dd1)\*(pp0-dd0); if (t1\*t2 <= 0.0) return 0; Found an intersection, so done. } tp = t; }   
}   
return (wind>0? 2 : -2); No intersections found, so simple concave.

When ispolysimple finds that the quick indicators are not enough, and that it needs to check all pairs of edges for intersections, it does so by the obvious $O ( N ^ { 2 } )$ method of two nested loops. For small $N$ , say less than 10, this is likely as fast as any other strategy. If you are dealing with large numbers of large- $N$ polygons, however, you will want to substitute a method with better scaling in $N$ . One way, using the code from $\ S 2 1 . 8$ , would be to define a class for segments with a collides() method, then store the segments into a QO tree one at a time, looking for collisions at each step. (Don’t forget that adjacent edges of a simple polynomial are allowed to “collide” at their shared vertex.)

Area of Polygons. As a next topic, let us turn to the area of a polygon. The (signed) area of a polygon is the sum of the areas of each of its regions weighted by that region’s winding number. For simple polygons the area is thus what you would expect geometrically, except that its sign will be negative for a polygon traversed CW rather than CCW. (We previously saw this in the special case of triangles.) For a complex polygon like that shown in Figure 21.4.5, the answer is less intuitive (and generally less useful) since some regions, such as the interior region with winding number 0, are not counted at all, while others are counted (in this case) twice.

The great advantage of this definition of area, however, is that it results in a simple expression for the area that applies to both simple and complex polygons. Let $x _ { i }$ and $y _ { i }$ be, respectively, the 0 and 1 coordinates of the polygon’s vertex ${ \bf p } _ { i }$ , and let $\mathcal { A }$ be the polygon’s area. Then, in three equivalent forms,

$$
2 \mathcal { A } = \sum _ { i = 0 } ^ { N - 1 } x _ { i } y _ { i + 1 } - x _ { i + 1 } y _ { i }
$$

$$
\begin{array} { l } { \displaystyle = \sum _ { i = 0 } ^ { N - 1 } ( x _ { i + 1 } + x _ { i } ) ( y _ { i + 1 } - y _ { i } ) } \\ { \displaystyle = \sum _ { i = 0 } ^ { N - 1 } x _ { i } ( y _ { i + 1 } - y _ { i - 1 } ) } \end{array}
$$

Evaluation of any of these forms takes just one loop over the polygon’s vertices. (These formulas go back as far as Meister in 1769 and Gauss in 1795.)

Although we won’t derive equation (21.4.20) in detail, the middle form does have an intuitive interpretation. It sums the areas of trapezoids each with two points on the $y$ -axis $( x = 0$ ) at $y _ { i }$ and $y _ { i + 1 }$ , and with the other two points the points on the polygon at these $y$ ’s. In going around the polygon, negative-area trapezoids subtract from positive-area ones so as to leave just the area inside.

Interestingly, there are very similar formulas for the $x$ and $y$ coordinates of the centroid or center-of-mass of an arbitrary polygon [3],

$$
{ \begin{array} { l } { { \overline { { x } } } = { \frac { 1 } { 6 } } \displaystyle \sum _ { i = 0 } ^ { N - 1 } ( x _ { i + 1 } + x _ { i } ) ( x _ { i } y _ { i + 1 } - x _ { i + 1 } y _ { i } ) } \\ { { \overline { { y } } } = { \frac { 1 } { 6 } } \displaystyle \sum _ { i = 0 } ^ { N - 1 } ( y _ { i + 1 } + y _ { i } ) ( x _ { i } y _ { i + 1 } - x _ { i + 1 } y _ { i } ) } \end{array} } 
$$

Note the common subexpressions with equation (21.4.20), so that it is efficient to calculate the area and centroid position together.

Finally, a couple of polygon tidbits for your edification or amusement:

- If two simple polygons have the same area, then the first can be cut into a finite number of polygonal pieces that can be reassembled into the second. This is known as the Bolyai-Gerwien theorem. (The corresponding statement about polyhedra in three dimensions, “Hilbert’s Third Problem,” was proved false by Dehn in 1900.)   
The regular polygon with $N$ sides is constructible with a compass and straightedge if the factorization of $N$ contains only the factors 2, 3, 5, 17, 257, 257, and 65537 (whose odd members are the Fermat primes), with each odd factor occurring at most once. It is not known whether any other $N$ -gons are also constructible; but, if so, then their $N$ must contain a factor at least as   
large as $2 ^ { 2 ^ { 3 3 } } + 1$ . The product of the known Fermat primes, which is perforce the largest known constructible polygon with an odd number of sides, is $2 ^ { 3 2 } - 1 = 4 2 9 4 9 6 7 2 9 5$ , a number well known to computer trolls as the largest positive 32-bit integer. Go figure.

# CITED REFERENCES AND FURTHER READING:

Bowyer, A. and Woodwark, J. 1983, A Programmer’s Geometry (London: Butterworths).   
Schneider, P.J. and Eberly, D.H. 2003, Geometric Tools for Computer Graphics (San Francisco: Morgan Kaufmann), $\ S 1 1 . 1 . 2 [ 1 ]$   
de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry: Algorithms and Applications, 2nd revised ed. (Berlin: Springer), Chapter 2.   
O’Rourke, J. 1998, Computational Geometry in C, 2nd ed. (Cambridge, UK: Cambridge University Press), $\ S 7 . 4$ .   
Goldman, R. 1990, “Intersection of Two Lines in Three-Space,” in Graphics Gems, Glassner, A.S., ed. (San Diego: Academic Press).[2]   
Bashein, G. and Detmer, P.R. 1994, “Centroid of a Polygon,” in Graphics Gems IV, Heckbert, P.S., ed. (Cambridge, MA: Academic Press).[3]   
Sunday, D. $^ { 2 0 0 7 + }$ , at http://softsurfer.com/algorithm_archive.htm.[4]   
Haines, E. 1994, “Point in Polygon Strategies,” in Graphics Gems IV, Heckbert, P.S., ed. (Cambridge, MA: Academic Press).[5]   
Wikipedia $^ { 2 0 0 7 + }$ , “Polygon,” at http://en.wikipedia.org.

# 21.5 Spheres and Rotations

The surface of the Earth is called a 2-sphere by topologists, but a 3-sphere by geometers; so the term $n$ -sphere is somewhat unclear. We’ll say “sphere in $n$ dimensions” to avoid any ambiguity. (For Earth, $n = 3 .$ .) Sphere refers to the surface, ball to the interior volume.

A sphere of radius $r$ in $n$ dimensions, centered on the origin, is the locus of points for which

$$
x _ { 0 } ^ { 2 } + \dots + x _ { n - 1 } ^ { 2 } = r ^ { 2 }
$$

Points on the sphere in $n$ dimensions can be specified by $n - 1$ angular coordinates, roughly the analogs of latitude and longitude on the sphere in three dimensions,

$$
\begin{array} { c } { { x _ { 0 } = r \cos \psi _ { 0 } } } \\ { { \ } } \\ { { x _ { 1 } = r \sin \psi _ { 0 } \cos \psi _ { 1 } } } \\ { { \ } } \\ { { \ldots } } \\ { { \ } } \\ { { x _ { n - 2 } = r \sin \psi _ { 0 } \sin \psi _ { 1 } \ldots \cos \psi _ { n - 2 } } } \\ { { \ } } \\ { { x _ { n - 1 } = r \sin \psi _ { 0 } \sin \psi _ { 1 } \ldots \sin \psi _ { n - 2 } } } \end{array}
$$

All the angles except the last have the range

$$
0 \leq \psi _ { i } \leq \pi , \qquad i = 0 , \ldots , n - 3
$$

i.e., are “latitude-like.” The last angle is “longitude-like,”

$$
0 \leq \psi _ { n - 2 } \leq 2 \pi
$$

The surface area $S _ { n }$ of the sphere in $n$ dimensions has a simple recurrence,

$$
\begin{array} { l l } { { S _ { 1 } = 2 } } & { { \mathrm { ( t w o  p o i n t s ) } } } \\ { { S _ { 2 } = 2 \pi r } } & { { \mathrm { ( c i r c u m f e r e n c e ~ o f ~ c i r c l e ) } } } \\ { { S _ { n } = { \displaystyle \frac { 2 \pi r ^ { 2 } } { n - 2 } } S _ { n - 2 } , } } & { { n > 2 } } \end{array}
$$

The volume $V _ { n }$ of the $n$ -dimensional ball is equal to $r / n$ times the area of the enclosing sphere in $n$ dimensions, and also has a simple recurrence,

$$
{ \begin{array} { r l r } & { V _ { 1 } = 2 r \qquad } & { { \mathrm { ( l e n g t h ~ o f ~ l i n e ) } } } \\ & { V _ { 2 } = \pi r ^ { 2 } \qquad } & { { \mathrm { ( a r e a ~ o f ~ c i r c l e ) } } } \\ & { \qquad \cdots } \\ & { V _ { n } = { \frac { r } { n } } S _ { n } = { \frac { 2 \pi r ^ { 2 } } { n } } V _ { n - 2 } } \end{array} }
$$

Closed-form formulas require a gamma function,

$$
\begin{array} { l } { { S _ { n } = \displaystyle \frac { 2 \pi ^ { n / 2 } } { \Gamma ( \frac { 1 } { 2 } n ) } r ^ { n - 1 } } } \\ { { { \cal V } _ { n } = \displaystyle \frac { 2 \pi ^ { n / 2 } } { n \Gamma ( \frac { 1 } { 2 } n ) } r ^ { n } } } \end{array}
$$

As $n$ becomes large, the ratio of the volume of a ball to the volume of the circumscribed (hyper-) cube rapidly becomes small,

$$
{ \frac { V _ { n } } { 2 ^ { n } } }  0 , \qquad n  \infty
$$

# 21.5.1 Picking a Random Point on the Sphere

You don’t get a random point on the sphere in $n$ dimensions by picking uniformly random values for the $n - 1$ angles in equation (21.5.2), just as you don’t get a random point on the Earth’s surface by throwing darts at a Mercator map (or any other non-equal-area projection).

An elegant general method is to generate $n$ independent, identically distributed, normal (Gaussian) deviates of zero mean, say $y _ { 0 } , \ldots , y _ { n - 1 }$ (see $\ S 7 . 3 )$ , and then calculate a point $\mathbf { X }$ on the unit sphere in $n$ dimensions by

$$
\mathbf { x } = { \frac { \mathbf { y } } { | \mathbf { y } | } }
$$

or, in other words,

$$
x _ { i } = y _ { i } \Bigg / \sqrt { \sum _ { j = 0 } ^ { n - 1 } y _ { j } ^ { 2 } }
$$

This works because the spherically symmetric Gaussian distribution in $n$ dimensions trivially factorizes into a product of independent one-dimensional Gaussians. If you want a random point inside the enclosed $n$ -volume, generate an additional uniform random deviate $u$ in Œ0; 1 and calculate the point’s coordinates as

$$
x _ { i } = u ^ { 1 / n } y _ { i } \Bigg / \sqrt { \sum _ { j = 0 } ^ { n - 1 } y _ { j } ^ { 2 } }
$$

You can of course scale to any other radius of sphere.

Faster special methods are available for the spheres in two, three, and four dimensions. For two dimensions, the circle, pick $u _ { 0 }$ and $u _ { 1 }$ uniform in $[ - 1 , 1 ]$ , rejecting choices for which $u _ { 0 } ^ { 2 } + u _ { 1 } ^ { 2 } > 1$ . This picks a random point inside the unit circle. Now scale in the obvious way to get a point on the circle,

$$
x _ { 0 } = \frac { u _ { 0 } } { \sqrt { u _ { 0 } ^ { 2 } + u _ { 1 } ^ { 2 } } } , \qquad x _ { 1 } = \frac { u _ { 1 } } { \sqrt { u _ { 0 } ^ { 2 } + u _ { 1 } ^ { 2 } } }
$$

(We already discussed this method in $\ S 7 . 3$ , under Cauchy deviates.)

A faster method for three dimensions, also using only two random deviates, is due to Marsalgia [1]. Pick a point inside the unit circle $( u _ { 0 } , u _ { 1 } )$ as above. Then a random point on the sphere in three dimensions is

$$
\begin{array} { l } { { x _ { 0 } = 2 u _ { 0 } \sqrt { 1 - u _ { 0 } ^ { 2 } - u _ { 1 } ^ { 2 } } } } \\ { { \ } } \\ { { x _ { 1 } = 2 u _ { 1 } \sqrt { 1 - u _ { 0 } ^ { 2 } - u _ { 1 } ^ { 2 } } } } \\ { { \ } } \\ { { x _ { 2 } = 1 - 2 ( u _ { 0 } ^ { 2 } + u _ { 1 } ^ { 2 } ) } } \end{array}
$$

For the sphere in four dimensions, pick two independent points inside the unit circle as above, $( u _ { 0 } , u _ { 1 } )$ and $( u _ { 2 } , u _ { 3 } )$ . Then a random point on the sphere in four dimensions is [1]

$$
\begin{array} { r l } & { x _ { 0 } = u _ { 0 } } \\ & { x _ { 1 } = u _ { 1 } } \\ & { x _ { 2 } = u _ { 2 } \sqrt { \cfrac { 1 - u _ { 0 } ^ { 2 } - u _ { 1 } ^ { 2 } } { u _ { 2 } ^ { 2 } + u _ { 3 } ^ { 2 } } } } \\ & { x _ { 3 } = u _ { 3 } \sqrt { \cfrac { 1 - u _ { 0 } ^ { 2 } - u _ { 1 } ^ { 2 } } { u _ { 2 } ^ { 2 } + u _ { 3 } ^ { 2 } } } } \end{array}
$$

Unfortunately, there is no known generalization to higher dimensions.

# 21.5.2 Picking a Random Rotation Matrix

Don’t confuse this with picking a point on a sphere. A rotation matrix $\mathbf { M }$ in $n$ dimensions is an orthogonal $n \times n$ matrix. For a proper rotation, M must have determinant 1. The other possibility, determinant $^ { - 1 }$ , represents an improper rotation, decomposable into a proper rotation followed by a reflection. The rotation matrix M maps any point $\mathbf { X }$ to a new point $\mathbf { x } ^ { \prime }$ by

$$
\mathbf { x } ^ { \prime } = \mathbf { M } \cdot \mathbf { x }
$$

A general method for picking a uniformly random rotation matrix is to fill an $n \times n$ matrix $\mathbf { G }$ with independent, identically distributed, normal (Gaussian) deviates of zero mean. Then, use QRdcmp in $\ S 2 . 1 0$ to construct the $\boldsymbol { \mathcal { Q } R }$ decomposition, namely ${ \bf G } = { \bf Q } \cdot { \bf R }$ . Except for the possibility that it might have the wrong sign of determinant, the matrix $\mathbf { Q }$ is now a uniformly random rotation matrix. The method used in QRdcmp is to apply $n - 1$ Householder transformations, each of which is a reflection with determinant $^ { - 1 }$ . Thus, to get determinant 1, we do nothing to $\mathbf { Q }$ if $n$ is odd; if $n$ is even, we simply interchange any pair of rows in $\mathbf { Q }$ , giving the final answer.

For large $n$ the work of doing the decomposition scales as $O ( n ^ { 3 } )$ , which can be burdensome. For faster, but more complicated, methods, see [2,3].

Faster special methods are available for two and three dimensions. A random two-dimensional rotation matrix has components that are the sine and cosine of a random angle $\theta$ in $[ 0 , 2 \pi ]$ ,

$$
\left( \begin{array} { l l } { \cos \theta } & { \sin \theta } \\ { - \sin \theta } & { \cos \theta } \end{array} \right)
$$

We get the components without trigonometric function calls by using (21.5.12) to find a random point on the unit circle and then taking cos $\theta = x _ { 0 }$ and $\sin \theta = x _ { 1 }$ .

In the case of three dimensions, a fast method is to use equation (21.5.14) to generate a random point on the sphere in four dimensions, and then to construct the $3 \times 3$ orthogonal matrix,

$$
{ \left[ \begin{array} { l l l } { 1 - 2 ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } ) } & { 2 ( x _ { 0 } x _ { 1 } - x _ { 3 } x _ { 2 } ) } & { 2 ( x _ { 0 } x _ { 2 } + x _ { 3 } x _ { 1 } ) } \\ { 2 ( x _ { 0 } x _ { 1 } + x _ { 3 } x _ { 2 } ) } & { 1 - 2 ( x _ { 0 } ^ { 2 } + x _ { 2 } ^ { 2 } ) } & { 2 ( x _ { 1 } x _ { 2 } - x _ { 3 } x _ { 0 } ) } \\ { 2 ( x _ { 0 } x _ { 2 } - x _ { 3 } x _ { 1 } ) } & { 2 ( x _ { 1 } x _ { 2 } + x _ { 3 } x _ { 0 } ) } & { 1 - 2 ( x _ { 0 } ^ { 2 } + x _ { 1 } ^ { 2 } ) } \end{array} \right] }
$$

which will be uniformly random among all rotations [4,5].

# CITED REFERENCES AND FURTHER READING:

Marsaglia, G. 1972, “Choosing a Point from the Surface of a Sphere,” Annals of Mathematical Statistics,vol.43, pp. 645-646.[1]

Genz, A. 2000, “Methods for Generating Random Orthogonal Matrices,” in Monte Carlo and Quasi-Monte Carlo Methods,Proceedings of the Third International Conference on Monte Carlo and Quasi-Monte Carlo Methods in Scientific Computing (MCQMC98) (Berlin: Springer).[2]

Anderson, T.W., Olkin, I., and Underhill, L.G. 1987, “Generation of Random Orthogonal Matrices,” SIAM Journal on Scientific and Statistical Computing, vol. 8, pp. 625–629.[3]

Shoemake, K. 1985, “Animating Rotation with Quaternion Curves,” Computer Graphics, Proceedings of SIGGRAPH 1985, vol. 19, pp. 245–254.[4]

Shoemake, K. 1992, “Uniform Random Rotations,” in Graphics Gems III, Kirk, D., ed. (Cambridge, MA: Academic Press), pp. 124–132.[5]

# 21.6 Triangulation and Delaunay Triangulation

We can informally define a triangulation of a set of $N$ points in the plane as follows: Connect the given points by straight-line segments as many times as you can without any two segments crossing. When you can’t connect any more, you have a triangulation. Obviously there are many triangulations of a given set of points. Figure 21.6.1 shows three triangulations of the same set of 50 points. Two are “random,” where the informal definition was pretty much followed literally. The third one is a very special triangulation, called a Delaunay triangulation. In a sense that we will make more precise below, it is the triangulation whose triangles best avoid small angles and long sides.

![](images/11cdeb7cc639bb45b2322c0e953725fdc3f32445d3651e53347cf804e5cce30a.jpg)  
Figure 21.6.1. Three triangulations of the same 50 random points: (a) and (b) are “bad” (random) triangulations, while (c) is a “good” (Delaunay) triangulation. The number of lines and triangles is the same in each case.

![](images/4b38fe68131e78b71d2580862b591d57cdb05ec7e6cdc101ebe2a820384c6ca5.jpg)  
Figure 21.6.2. How to count lines and triangles in a triangulation. (a) Each triangle “uses up” $1 / 2$ of a point, and $_ { 3 / 2 }$ lines. (b) The $n$ points in the convex hull “use up” $n / 2 + 1$ points and $n / 2$ lines.

All triangulations of a given set of points have the same outer boundary, called the convex hull of the point set. This should be evident, again informally, from the definition of triangulation: A line segment (edge) on the outer convex boundary can’t interfere with any other actual or potential interior edges, so it will always be added before the stopping rule is reached. The number of points $n$ (and also edges) in the convex hull is at least three, and can be as large as $N$ , e.g., if the points all lie on a circle. (Here and below, we will ignore degenerate cases like “all points lie on a line.”)

It is surprising, perhaps, that all triangulations of a given point set have the same number of lines $( L )$ and triangles $( T )$ , given explicitly by the relations

$$
\begin{array} { c } { { L = 3 N - n - 3 } } \\ { { T = 2 N - n - 2 } } \end{array}
$$

The proof, known to Gauss, is very easy if you consult Figure 21.6.2. Since the interior angles of a triangle sum to $\pi$ radians, each triangle “uses up” half a point’s worth of angle. It is useful to think about each line as being two half-lines, representing the two possible directions of traversal in clockwise triangles. Then, each triangle uses up three half-lines. We must separately account for the vertices on the convex hull, as follows: Each such point uses up $\pi$ radians on its own (dark-shaded angles in the figure), plus (sum of the light-shaded exterior angles) $2 \pi$ additional radians in going around the convex hull. These considerations give the relations

![](images/ac7135ccacbdd646a3c4c0579567194346c663d3b20f57d43fced5df16f1c747.jpg)  
Figure 21.6.3. Example of a triangulation with $N = 1 2$ , $n = 6$ , $T = 1 6$ , and $L = 2 7$ , values that satisfy equation (21.6.1).

$$
\begin{array} { r l r l } { { 2 } \pi N = \pi T + \pi n + 2 \pi } & { } & { { } { \mathrm { ( a c c o u n t ~ f o r ~ r a d i a n s ) } } } \\ { 2 L = 3 T + n } & { } & { { } { \mathrm { ( a c c o u n t ~ f o r ~ h a l f - l i n e s ) } } } \end{array}
$$

which can be rearranged to give equation (21.6.1). Figure 21.6.3 shows the triangulation of Figure 21.6.2(b) with its points and triangles enumerated.

# 21.6.1 Delaunay Triangulation

Boris Nikolaevich Delone (1890–1980), a Russian mathematician also celebrated as a rock climber, first published the ideas behind Delaunay triangulation in 1934. Since his paper was written in French, his name was transliterated so as to be pronounced (approximately) correctly by French speakers. A better English pronunciation might be “dyeh-LOAN-yeh.”

Delaunay triangulations have a number of remarkable properties and can be defined in various abstract ways. However, we’ll take as the definition one very concrete property, shown in Figure 21.6.4. Consider all triangulations in which four points, $A , B , C , D$ ; are the vertices of two back-to-back triangles. Then, one can get a different triangulation by deleting the common edge ( $B D$ in the figure) and replacing it by the other diagonal of the quadrilateral ( $A C$ in the figure). A Delaunay triangulation is defined as one that always chooses the diagonal that gives the largest minimum angle for the six interior angles in the two triangles. The edge shown as $B D$ is thus illegal for a Delaunay triangulation, while $A C$ is termed legal. Changing a triangulation from an illegal edge to a legal one is called an edge flip. When any two triangles have a common edge, exactly one configuration, unchanged or edgeflipped, is legal (unless all four points lie on a circle, in which case both are legal).

This “largest minimum angle” property is geometrically equivalent to other statements about the points $A , B , C , D$ . One such statement is that the circumcircle of an illegal triangle, like $A B D$ or $B C D$ in part (a) of the figure, always contains another point, $C$ or $A$ , respectively. For a legal triangle, as in part (b) of the figure, this is never the case. One can use this as a starting point to prove the theorem:

- The circumcircle of any triangle in a Delaunay triangulation contains no other vertices.

![](images/a455ee9cb6a0afbdbe5d7bccf2b83cf048f180f403a52597d0117df233c41498.jpg)  
Figure 21.6.4. A Delaunay triangulation can be defined as one in which back-to-back triangles always have a larger minimum angle than they would have if their common edge were flipped to the other diagonal. Equivalently, any triangle’s circumcircle does not contain another vertex. A so-called edge flip converts (a) to (b) in the figure.

Although the largest minimum angle property was defined locally, for one quadrilateral at a time, it can be shown to imply a remarkable global theorem:

- Among all triangulations of a set of points, a Delaunay triangulation has the largest minimum angles, as defined by sorting all angles from smallest to largest and comparing lexicographically to the angles of any other triangulation.

Comparing lexicographically means: First compare the smallest angle; if there is a winner, stop. If there is a tie on the smallest angle, compare the second-smallest angle. And so on.

Another theorem is

- Two vertices are connected by a Delaunay edge if and only if there is some circle that contains them and contains no other vertices.

If the points in a set have generic positions, meaning that no three are collinear and no four lie on the same circle, then the Delaunay triangulation exists and is unique; any method for constructing it will give the identical set of triangles.

You might wonder whether a Delaunay triangulation is also a minimum weight triangulation, defined as the triangulation with the smallest total of edge lengths. The answer is, in general, no. While minimum weight triangulations might be useful in applications, it is not even known whether they can be constructed in less than time that grows exponentially with $N$ . Delaunay construction, on the other hand, is fast, ${ \cal O } ( N \log N )$ . So, in practice, Delaunay is what we’ve got!

So, how do we construct a Delaunay triangulation? Conceptually, we can start with any triangulation and then eliminate illegal edges, by edge flips, as long as possible. This must terminate in a Delaunay triangulation after a finite number of flips because (i) each flip changes and increases the lexicographic order in the list of angles, and (ii) there are only a finite number of possible triangulations. Although, as stated, this is not an efficient algorithm, it can be readily be turned into one, the so-called randomized incremental algorithm [1].

This algorithm, which we now implement, is “incremental” in that it adds points to the triangulation one at a time, maintaining a Delaunay triangulation at each stage. It is “randomized” in that the points are added in a random order. It turns out that the randomization (almost) guarantees ${ \cal O } ( N \log N )$ expected time for the algorithm. (Without randomization, one could encounter pathological cases with

![](images/4e5efbc3c4454458efa0442979fc0586d052eeffcbc06c8768f188151b3ed415.jpg)  
Figure 21.6.5. Steps in inserting a new point into a Delaunay triangulation. (a) Connect new point $P$ to vertices of enclosing triangle. (b) Check enclosing triangle for illegal edges (here, replace $Q R$ by $P S$ ). (c) Recursively check any new triangles created that have $P$ as a vertex. (Here, $R S$ is legal, so we terminate.)

$O ( N ^ { 2 } )$ running time.)

Figure 21.6.5 shows the procedure for adding a new point $P$ that lies within an existing triangle. First, connect it to the vertices of the enclosing triangle. This creates three new triangles. (We exclude the special case where $P$ is exactly on an existing line. More on this below.) Next, check whether the edges opposite $P$ in the three new triangles are legal or illegal. If they are illegal, do edge flips. Each edge flip creates two new triangles with $P$ as a vertex, and (therefore) with two edges opposite $P$ that now also need to be checked for legality. So the process is recursive, but it never wanders away from $P$ . That is the key point: The only edges that can be made illegal by inserting point a point $P$ are edges opposite $P$ in triangles that include $P$ . The proof that the algorithm is ${ \cal O } ( N \log N )$ uses this fact, and then bounds the average number of triangles of which $P$ can be a vertex by relations like those of equation (21.6.1). (For details in the proof, see [2].)

Since, up to now, we only know how to add a point $P$ that falls inside the triangulation, how can we get started? An easy way is to add three “fictitious” points to the set of points, forming a very large starting triangle that will enclose all the “real” points subsequently added. Then, at the very end, the fictitious points and all edges connecting to them are removed. Strictly speaking, the fictitious points must actually be treated as if at infinity (thus requiring special logic in the code whenever they are referenced). If their distance is merely finite, the constructed triangulation may be “not-quite” Delaunay. For example, its outer boundary (convex hull) could in unusual cases be left slightly concave, with small negative angles on the order of the diameter of the “real” point set divided by the distance to the “fictitious” points.

That’s enough general information. We next get into the details.

# 21.6.2 Implementation Details

Since most readers skip a section with this title, this is a good place for us to confess a couple of dirty tricks in our Delaunay implementation, whose purpose is to keep the code and its explication to manageable length. If you need a bullet-proof Delaunay code, with no such tricks, a Web search will turn up several that are freely available. Our code is short and fast, and fine for its intended purpose; but it is approximate in two respects: First, we don’t take the initial bounding triangle off to infinity (as we sanctimoniously advised, above). Instead, it lies at a distance of about bigscale (an adjustable parameter, default value 1000), measured in units of the bounding-box size of the set of points. Second, we don’t provide for the special case, mentioned above, where the point being added falls on an existing edge (or does so within roundoff tolerance). For generic point locations, this should “never” happen; but in real life it “always” happens, because users love to try test examples with points in regular patterns! When we detect this problem, we randomly alter the location of the offending point by a small fraction fuzz (another adjustable parameter, default $1 0 ^ { - 6 }$ ) of the bounding box dimensions.

A very important implementation detail, not yet discussed, is how to find in which existing triangle a new point lies. Conceptually, we might throw the triangles into a QO tree (-21.8), but this would not yield the desired ${ \cal O } ( N \log N )$ behavior for our algorithm. A better solution, well established in the literature, is to maintain a tree structure of the descendants of any given triangle that ever existed in the construction. That is, starting with the huge “root” triangle, whenever a triangle is subdivided into three new triangles, we set pointers to its three daughters. And, when two triangles are lost in an edge flip, and two new triangles are created, we make the new triangles daughters of both of the lost triangles (even though each lost triangle contains only a part of each new one). In this scheme a triangle has two or three daughters at most, so we can easily reserve space for the pointers explicitly (i.e., no expandable linked lists needed).

With this structure, it is very fast to locate a point within the existing triangulation: Start at the root triangle, and recursively pick whichever daughter contains the point. When you reach a terminal node in the tree, you will have found a triangle in the current triangulation that contains the point. We thus need a structure for a “triangle element” or Triel:

struct Triel {   
Structure for an element in a descendancy tree of triangles, each having at most three daughters. Point<2> \*pts; Pointer to the array of the points. Int p[3]; The triangle’s three vertices, always in CCW order. Int d[3]; Pointers for up to three daughters. Int stat; Nonzero if this element is “live.” void setme(Int a, Int b, Int c, Point<2> \*ptss) { Set the data in a Triel. pts $=$ ptss; p[0] $=$ a; p[1] $=$ b; ${ \mathfrak { p } } [ 2 ] \ = \ { \mathfrak { c } } ;$ ; d[0] $= \textrm { d } [ 1 ] ~ = ~ \textrm { d } [ 2 ] ~ = ~ - 1$ ; The values $^ { - 1 }$ mean no daughters. stat $\ l = \ 1$ ; Create as “live.” } Int contains(Point<2> point) { Return 1 if point is in the triangle, 0 if on boundary, $^ { - 1 }$ if outside. (CCW triangle is assumed.) Doub d; Int i,j,ztest $\mathit { \Theta } = \mathit { \Theta } 0$ ; for (i=0; i<3; $\dot { 1 } + +$ ) { ${ \dot { ] } } \ =$ (i+1) %3; d $=$ (pts[p[j]].x[0]-pts[p[i]].x[0]) $^ *$ (point.x[1]-pts[p[i]].x[1]) (pts[p[j]].x[1]-pts[p[i]].x[1])\*(point.x[0]-pts[p[i]].x[0]); if (d < 0.0) return $^ { - 1 }$ ; if ( $\mathrm { ~ d ~ } = = \mathrm { ~ 0 ~ . 0 } ,$ ) ztest $\ c = ~ 1$ ; return (ztest? 0 : 1); }   
};

We create an big enough array of Triels at the start, and use integers to point to array elements. We’ve omitted any explicit constructor or assignment operators in Triel, since they are not needed for our use here. Be sure to add them if you use Triel in any other way.

We will need a way to do two other fast lookups: (1) Given a point and opposite edge in a triangle, find the fourth point in the quadrilateral, that is, the point (if any) on the other side of the given edge. (2) Given three points, find the index of their triangle (if it exists) in an array of Triel elements. Our strategy is to use hash memories (respectively called linehash and trihash) for these two functions. In particular, whenever we create a triangle (always CCW) with vertices $A , B , C$ , we store an index pointing to each point under a specially constructed key,

$$
\mathtt { l i n e h a s h } ( h ( B ) - h ( C ) )  A
$$

where the function $h$ is a 64-bit hash function, and “et cyc.” means do the same thing for the other two cyclic permutations of $A , B , C$ . The trick here is that, if we ever want to find the point on the other side of edge $B C$ , we just look for a key $h ( C ) - h ( B )$ (“negative” of the key in equation 21.6.3) in the hash table. The similar trick for storing and retrieving Triels is that, when we create a Triel at location $j$ in the storage array, we set

$$
\mathrm { \ t r i h a s h } ( h ( A ) \ \hat { \ } - \ h ( B ) \ \hat { \ } - \ h ( C ) ) \gets j
$$

where ^ is the XOR operation. Since this key is symmetric in $A , B , C$ ; we can find a triangle knowing its vertices in any order.

Since we are computing hash keys “by hand,” we can signal the two hash memories to use a null (therefore fast) hash of their own. That, and a utility for determining whether a point is inside the circumcircle of three other points, are the following two code fragments:

Doub incircle(Point<2> d, Point<2> a, Point<2> b, Point<2> c) Return positive, zero, or negative value if point d is respectively inside, on, or outside the circle through points a, b, and c.

Circle cc = circumcircle(a,b,c); Routine defined in $\ S 2 1 . 3$ .   
Doub radd $=$ SQR(d.x[0]-cc.center.x[0]) $^ +$ SQR(d.x[1]-cc.center.x[1]);   
return (SQR(cc.radius) - radd);

# }

# struct Nullhash {

Null hash function. Use a key (assumed to be already hashed) as its own hash. Nullhash(Int nn) {} inline Ullong fn(const void \*key) const { return $^ *$ ((Ullong \*)key); }   
};

These are all the preliminaries we need before declaring the Delaunay structure.

# struct Delaunay {

Structure for constructing a Delaunay triangulation from a given set of points. Int npts,ntri,ntree,ntreemax,opt; Number of points, triangles, elements in the Doub delx,dely; Triel list, and maximum of same. Size vector< Point<2> $>$ pts; of the bounding box. vector<Triel> thelist; The list of Triel elements. Hash<Ullong,Int,Nullhash> \*linehash; Create the hash memories with null hash Hash<Ullong,Int,Nullhash> \*trihash; function. Int \*perm; Delaunay(vector<Point<2> $>$ &pvec, Int options $\mathit { \Theta } = \mathit { \Theta } _ { 0 } )$ ; Construct the Delaunay triangulation from a vector of points. The variable options is used by some applications. Ranhash hashfn; The raw hash function. Doub interpolate(const Point<2> &p, const vector<Doub> &fnvals, Doub defaultval ${ = } 0$ .0); The next four functions are explained in detail below. void insertapoint(Int r); Int whichcontainspt(const Point<2> &p, Int strict $\mathit { \Theta } = \mathit { \Theta } 0 )$ ; Int storetriangle(Int a, Int b, Int c); void erasetriangle(Int a, Int b, Int c, Int d0, Int d1, Int d2); static Uint jran; Random number counter. static const Doub fuzz, bigscale;   
};   
const Doub Delaunay::fuzz $\ l = \ 1$ .0e-6; Adjust if you wish. See text.   
const Doub Delaunay::bigscale $=$ 1000.0; Adjust if you wish. See text.   
Uint Delaunay::jran $=$ 14921620;

The variable jran is used in conjunction with the hash function as a convenient random number generator. The function interpolate() is for the application of interpolating a function on an irregular mesh, to be discussed in $\ S 2 1 . 7$ . Everything else should become clear as we proceed.

The action starts with the constructor. We compute a bounding box for the set of points, construct and store the “huge” root triangle enclosing the points, create a random permutation to be the order in which points are added, and then (for the real work) call the function insertapoint() for each point in turn. After that there is just some cleanup housekeeping.

Delaunay::Delaunay(vector< Point<2> $>$ &pvec, Int options) : npts(pvec.size()), ntri(0), ntree(0), ntreemax(10\*npts+1000), opt(options), pts(npts+3), thelist(ntreemax) {   
Construct Delaunay triangulation from a vector of points pvec. If bit 0 in options is nonzero,   
hash memories used in the construction are deleted. (Some applications may want to use them   
and will set options to 1.) Int j; Doub xl,xh,yl,yh; linehash $=$ new Hash<Ullong,Int,Nullhash>(6\*npts+12,6\*npts+12); trihash $=$ new Hash<Ullong,Int,Nullhash>(2\*npts+6,2\*npts+6); perm $=$ new Int[npts]; Permutation for randomizing point order. $\mathbf { x } 1 \ = \ \mathbf { x } \mathbf { h } \ =$ pvec[0].x[0]; Copy points to local store and calculate their $\mathrm { { y } 1 ~ = ~ \mathrm { { y h } ~ = ~ } }$ pvec[0].x[1]; bounding box. for $( \ j = 0$ ; j<npts; ${ \mathrm { j } } + + { \mathrm { . } }$ ) { pts[j] $=$ pvec[j]; perm[j] $=$ j; if (pvec[j].x[0] < xl) xl $=$ pvec[j].x[0]; if (pvec[j].x[0] $>$ xh) xh $=$ pvec[j].x[0]; if (pvec[j].x[1] $<$ yl) yl $=$ pvec[j].x[1]; if (pvec[j].x[1] $>$ yh) yh $=$ pvec[j].x[1]; } delx $=$ xh - xl; Store bounding box dimensions, then construct dely $=$ yh - yl; the three fictitious points and store them. pts[npts] $=$ $\mathtt { P o i n t } < 2 > ( 0 \_ 5 * ( \mathrm { x 1 \_ + \ x h } )$ , yh $^ +$ bigscale\*dely); pts[npts+1] $=$ Point<2>(xl - 0. $^ { 5 \ast }$ bigscale\*delx,yl - 0.5\*bigscale\*dely); pts[npts+2] $=$ Point<2>(xh $^ +$ 0.5\*bigscale\*delx,yl - 0.5\*bigscale\*dely); storetriangle(npts,npts+1,npts $+ 2 )$ ; Create a random permutation: for (j=npts; j>0; j--) SWAP(perm[j-1],perm[hashfn.int64(jran $^ { + + }$ ) % j]); for ( $\scriptstyle { \dot { \ j } } = 0$ ; j<npts; ${ \mathrm { j } } + + { \mathrm { . } }$ ) insertapoint(perm[j]); All the action is here! for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<ntree; ${ \dot { \mathsf { J } } } ^ { + + }$ ) { Delete the huge root triangle and all of its conif (thelist[j].stat $>$ 0) { necting edges. if (thelist[j].p[0] $> =$ npts thelist[j].p[1] >= npts || thelist[j].p[2] $> =$ npts) { thelist[j].stat $\begin{array} { r l } { \mathbf { \Phi } } & { { } = \mathbf { \Phi } - \mathbf { 1 } \mathbf { \Phi } } \end{array}$ ; ntri--; } if (!(opt & 1)) { Clean up, unless option bit says not to. delete [] perm; delete trihash; delete linehash; }   
}

The guts of the algorithm as previously described are in insertapoint(). We first locate the triangle that contains the new point. (Failure here can mean only that the point lies on an existing line, in which case we fuzz the point’s location, as we confessed above, and try again.) We store three new triangles and delete the old one. Then, we locate and fix any illegal edges, doing the recursion by a simple last-in-first-out stack of pending edges to check.

# void Delaunay::insertapoint(Int r) {

Add the point with index r incrementally to the Delaunay triangulation.

Int i,j,k,l,s,tno,ntask,d0,d1,d2;   
Ullong key;   
Int tasks[50], taski[50], taskj[50];   
for $( \ j = 0$ ; j<3; ${ \mathrm { j } } + + { \mathrm { . } }$ ) { tno $=$ whichcontainspt(pts[r],1); if (tno $> = ~ 0 ^ { \cdot }$ ) break;

Stacks (3 vertices) for legalizing edges. Find triangle containing point. Fuzz if it lies on an edge. The desired result: Point is OK.

pts[r].x[0] $+ =$ fuzz $^ *$ delx $^ *$ (hashfn.doub(jran $^ { + + }$ )-0.5); pts[r].x[1] $+ =$ fuzz $^ *$ dely $^ *$ (hashfn.doub(jran ${ . + + }$ )-0.5); if $( { \mathrm { j } } { \mathrm { \Omega } } = = { \mathrm { \Omega } } 3 )$ ) throw("points degenerate even after fuzzing"); ntask $\mathit { \Theta } = \mathit { \Theta } 0$ ; $\begin{array} { r l } { \dot { \bf 1 } } & { { } = } \end{array}$ thelist[tno].p[0]; ${ \dot { \mathrm { ~ \bf ~ j ~ } } } =$ thelist[tno].p[1]; $\mathrm { ~ \bf ~ k ~ } =$ thelist[tno].p[2]; The following line is relevant only when the indicated bit in opt is set. This feature is used by the convex hull application and causes any points already known to be interior to the convex hull to be omitted from the triangulation, saving time (but giving in an incomplete triangulation). if (opt & 2 && i $<$ npts && j $<$ npts && k < npts) return; ${ \tt d } 0 \ =$ storetriangle(r,i,j); Create three triangles and queue them tasks $: + + :$ ntask] $\mathbf { \Phi } = \mathbf { \Phi } _ { \mathbf { T } }$ ; taski[ntask] $=$ i; taskj[ntask] $= \ j$ ; for legal edge tests. ${ \tt d } 1 { \it \Delta \phi } =$ storetriangle(r,j,k); tasks[++ntask] $\mathbf { \Phi } = \mathbf { \Phi } _ { \mathbf { T } }$ ; taski[ntask] $=$ j; taskj[ntask] $\mathit { \Theta } = \mathit { \Theta } \mathbf { k }$ ; $\mathrm { ~ d } 2 \ =$ storetriangle(r,k,i); tasks[++ntask] $= x$ ; taski[ntask] $= \texttt { k }$ ; taskj[ntask] $\mathbf { \Sigma } = \mathbf { \Sigma } _ { \mathrm { ~ i ~ } }$ ; erasetriangle(i,j,k,d0,d1,d2); Erase the old triangle. while (ntask) { Legalize edges recursively. $\mathbf { s } =$ tasks[ntask]; $\mathrm { i } =$ taski[ntask]; j=taskj[ntaskkey $=$ hashfn.int64(j) - hashfn.int64(i); Look up fourth point. if ( ! linehash->get(key,l) ) continue; Case of no triangle on other side. if (incircle(pts[l],pts[j],pts[s],pts[i]) > 0.0){ Needs legalizing? $\mathtt { d 0 } \ =$ storetriangle(s,l,j); Create two new triangles d1 $=$ storetriangle(s,i,l); erasetriangle(s,i,j,d0,d1,-1); and erase old ones. erasetriangle(l,j,i,d0,d1,-1); key $=$ hashfn.int64(i)-hashfn.int64(j); Erase line in both directions. linehash->erase(key); key $\mathit { \Theta } = \mathit { \Theta } 0$ - key; Unsigned, hence binary minus. linehash->erase(key); Two new edges now need checking: tasks $^ { + + }$ ntask] $=$ s; taski[ntask] $= ~ 1$ ; taskj[ntask] $\mathit { \Theta } = \mathit { \Pi } _ { \dot { ] } } \mathit { \Psi } _ { : }$ ; tasks $[ + +$ ntask] $\qquad = \ \mathtt { s }$ ; taski[ntask] $=$ i; taskj[ntask] $\mathbf { \omega } = \mathbf { \varepsilon } _ { 1 } ;$ } }

The only pieces left are the utility functions for finding the triangle that contains a point, and for storing and erasing a triangle. When we “erase” a triangle, we actually only mark it as inactive in the current triangulation, and we set its daughters in the descendancy tree, as already discussed.

# Int Delaunay::whichcontainspt(const Point<2> &p, Int strict) {

Given point p, return index in thelist of the triangle in the triangulation that contains it, or return $^ { - 1 }$ for failure. If strict is nonzero, require strict containment, otherwise allow the point to lie on an edge.

Int i,j, $\mathtt { k } = 0$ ;   
while (thelist[k].stat $< = ~ 0$ ) { Descend in tree until reach a “live” triangle. for ( $\scriptstyle \dot { 1 } = 0$ ; i<3; $\dot { 1 } + +$ ) { Check up to three daughters. if ( $( { \bf j _ { \alpha } } =$ thelist[k].d[i]) < 0) continue; Daughter doesn’t exist. if (strict) { if (thelist[j].contains(p) > 0) break; } else { Yes, descend on this branch. if (thelist[j].contains(p) $> = ~ 0$ ) break; } } if (i == 3) return -1; No daughters contain the point. k = j; Set new mother.   
}   
return k; Normal return.

void Delaunay::erasetriangle(Int a, Int b, Int c, Int d0, Int d1, Int d2) { Erase triangle abc in trihash and inactivate it in thelist after setting its daughters.

Ullong key; Int j; key $=$ hashfn.int64(a) ^ hashfn.int64(b) ^ hashfn.int64(c); if (trihash->get(key,j) $\scriptstyle = = 0 .$ ) throw("nonexistent triangle"); trihash->erase(key); thelist[j].d[0] $=$ d0; thelist[j].d[1] $=$ d1; thelist[j].d[2] $=$ d2; thelist[j].stat $\qquad = \ 0$ ; ntri--

# Int Delaunay::storetriangle(Int a, Int b, Int c) {

Store a triangle with vertices a, b, c in trihash. Store its points in linehash under keys to opposite sides. Add it to thelist, returning its index there.

Ullong key;   
thelist[ntree].setme(a,b,c,&pts[0]);   
key $=$ hashfn.int64(a) ^ hashfn.int64(b) ^ hashfn.int64(c);   
trihash->set(key,ntree);   
key $=$ hashfn.int64(b)-hashfn.int64(c);   
linehash->set(key,a);   
key $=$ hashfn.int64(c)-hashfn.int64(a);   
linehash->set(key,b);   
key $=$ hashfn.int64(a)-hashfn.int64(b);   
linehash->set(key,c);   
if ( $^ { + + }$ ntree $= =$ ntreemax) throw("thelist is sized too small");   
ntri $^ { + + }$ ;   
return (ntree-1);

You might wonder how to get the answer out of our Delaunay structure. We have not provided a function for this, because it so much depends on what you want to do with the answer. The general idea, however, is that you just loop through thelist $[ j ]$ for $0 \leq j <$ nlist. Each element is a Triel. If its value of save is $\leq 0$ , ignore it and go on. If it is 1, then the element represents a triangle in the final Delaunay triangulation. There should be ntri of these elements in all. The element’s array $\mathtt { p } [ ]$ has integers that point to the triangle’s three points in your vector of points. Several routines in the next section mine the Delaunay structure for points, edges, or triangles and can be used as template examples.

Figure 21.6.6 shows sample output for a Delaunay triangulation of 300 points.

# CITED REFERENCES AND FURTHER READING:

Guibas, L.J., Knuth, D.E., and Sharir, M. 1992, “Randomized Incremental Construction of Delaunay and Voronoi Diagrams,” Algorithmica, vol. 7, pp. 381–413.[1]   
Lischinski, D. 1994, “Incremental Delaunay Triangulation,” in Graphics Gems IV, Heckbert, P.S., ed. (Cambridge, MA: Academic Press). [Shows use of linked data structure instead of our use of hash memory.]   
de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry: Algorithms and Applications, 2nd revised ed. (Berlin: Springer),Chapter 9.[2]   
O’Rourke, J. 1998, Computational Geometry in C, 2nd ed. (Cambridge, UK: Cambridge University Press), $\ S 5 . 3$ .

![](images/8e5b2ec2c44415465097e416652c5e9b616b043529c3d038127ed18f670da6ae.jpg)  
Figure 21.6.6. Delaunay triangulation of 300 points randomly chosen within a circle, as computed by the routines in this section.

# 21.7 Applications of Delaunay Triangulation

Emerging from the thicket of detail that was needed to implement the Delaunay triangulation, we are now ready to make use of it in several important applications. In this section we assume that you have a vector of points (say, vecp), and that you have invoked the code in -21.6 to construct a Delaunay structure. This usually means writing just the one line of code,

Delaunay mygrid(vecp);

So, what next?

# 21.7.1 Two-Dimensional Interpolation on an Irregular Grid

This is probably the most-asked-for algorithm that was missing from the previous two editions of Numerical Recipes. The basic setup is very simple. You are given a set of $N$ points in the plane. You triangulate that set with a “good” triangulation, that is, one favoring short lines and big angles — in other words, Delaunay. You evaluate a function of interest at each of the points, and store the values in a vector (in the same order as the vector of points, of course).

Now it is easy to interpolate the function at a new point $\mathbf { p }$ that lies within the triangulation, that is, specifically, within the convex hull of your set of points. First, locate which triangle the point falls in. This takes only ${ \cal O } ( \log N )$ operations if you use the whichcontainspt() method of the Delaunay structure. Then, linearly interpolate between the three function values at the three triangle vertices. The linear interpolation is uniquely defined, because (imagining your function plotted in the third dimension above the plane in which $\mathbf { p }$ lies) three points uniquely define a plane in three dimensions .

Constructively, the linear interpolation is easily done using barycentric coordinates as defined in equation (21.3.10), which in turn reduces to using the triangle area formula (equation 21.3.1) three times. Appropriately normalized, each barytropic coordinate value is exactly the weight of its corresponding vertex.

These ideas are implemented in the following function:

# Doub Delaunay::interpolate(const Point<2> &p, const vector<Doub> &fnvals, Doub defaultval) {

Triangular grid interpolation of a function. Given an arbitrary point p and a vector of function values fnvals at the points that were used to construct the Delaunay structure, return the linearly interpolated function value in the triangle in which p lies. If $\mathtt { p }$ lies outside of the triangulation, instead return defaultval.

Int n,i,j,k;   
Doub wgts[3];   
Int ipts[3];   
Doub sum, ans $= ~ 0 . 0$ ;   
$\mathrm { ~ n ~ } =$ whichcontainspt(p); Locate the point in the triangulation.   
if ( $\mathrm { ~  ~ \cdot ~ n ~ } < \mathrm { ~  ~ 0 ~ }$ ) return defaultval; Point outside of convex hull.   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<3; $\dot { 1 } + +$ ) ipts[i] $=$ thelist[n].p[i];   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ , $\scriptstyle { \dot { \mathsf { J } } } = 1$ , $\mathrm { k } = 2$ ; i<3; $\dot { \bf 1 } + +$ , $\mathrm { j } + +$ ,k++) { Calculate the barycentric coordinates, proif $( { \ j } \ = = \ 3 )$ ) $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; portional to the weights. if $( \textbf { k } = = \textbf { 3 }$ ) $\mathtt { k } = 0$ ; wgts[k] $=$ (pts[ipts[j]].x[0]-pts[ipts[i]].x[0])\*(p.x[1]-pts[ipts[i]].x[1]) (pts[ipts[j]].x[1]-pts[ipts[i]].x[1]) $^ *$ (p.x[0]-pts[ipts[i]].x[0]);   
}   
sum $=$ wgts[0] $^ +$ wgts[1] $^ +$ wgts[2]; Normalization of the weights.   
if (sum $\ c = 0 .$ ) throw("degenerate triangle");   
for ( $\scriptstyle { \dot { 1 } } = 0$ ; i<3; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \rho } } } .$ ) ans $+ =$ wgts[i]\*fnvals[ipts[i]]/sum; Linear interpolation.   
return ans;

# }

Keep in mind that you should not expect high accuracy from linear interpolation. The interpolated function is piecewise linear, and continuous within the convex hull, but it has discontinuous derivatives in the direction perpendicular to the triangle’s edges. On a triangle edge, it interpolates between the two function values at each end of the edge. You need a lot of triangles to get a reasonable representation of any function with much detailed structure.

# 21.7.2 Voronoi Diagrams

Around 1907, the Ukrainian mathematician Georgy Fedoseevich Voronoi revisited a problem that had been previously discussed by Dirichlet as early as 1850: Given $N$ points, or sites, in the plane, each site p defines a region that is closer to $\mathbf { p }$ than to any of the other $N - 1$ sites. That region is called p’s Voronoi region. What are the properties of the Voronoi regions, and how can we construct them?

If you imagine that everyone in a city shops at the closest supermarket (“as the crow flies”), then the Voronoi regions map out the districts served by each supermarket. If you imagine that fires are simultaneously set at sites in a forest, and that they spread circularly at a fixed speed, then the Voronoi regions are the areas burned by each different fire.

Figure 21.7.1, an example of a Voronoi diagram, shows the Voronoi regions around 40 sites chosen randomly in the plane. Yes, the boundaries of the Voronoi regions are polygons, although possibly open and extending to infinity. It is obvious, in fact, that the boundary of a site $\mathbf { p }$ ’s Voronoi region must consist of line segments each lying on the perpendicular bisector of the line connecting $\mathbf { p }$ to some other site, say $\mathbf { q } _ { i }$ . That is because the perpendicular bisector is the locus of points equidistant from $\mathbf { p }$ and $\mathbf { q } _ { i }$ . So the real questions are, for a given $\mathbf { p }$ , which are the $\mathbf { q } _ { i }$ ’s that contribute boundary segments? and is there a fast way to compute their intersections (the vertices of the Voronoi diagram)?

![](images/1a8d2f8e3f1a4580cf756f3474a5133ba1dbe9d0286457c92708c21fbe9cf53b.jpg)  
Figure 21.7.1. Voronoi diagram for 40 random sites. Each site has a Voronoi region, the area closer to it than to any other site. The boundaries of the Voronoi regions are straight-line segments that lie on the perpendicular bisectors between pairs of sites.

Remarkably, these questions are completely answered by the Delaunay triangulation of the Voronoi sites. (In fact, many texts start with the Voronoi diagram as fundamental, and then consider Delaunay triangulation as an application. We find it easier to go the other way.)

Some facts are

- Every edge in a site p’s Voronoi region boundary lies on the perpendicular bisector of a Delaunay edge that connects to $\mathbf { p }$ .   
- In fact, every Delaunay edge corresponds to exactly one Voronoi edge, and vice versa.   
- The vertices of the Voronoi diagram are exactly the circumcenters of the Delaunay triangles.   
- The Voronoi diagram and the Delaunay triangulation are dual graphs (but don’t worry if you don’t know what this means)

Figure 21.7.2 shows the key ideas in the proof of the first two facts above. We already know that the boundary is made of some perpendicular bisector segments. We need to show that (i) every one of a point’s Delaunay edges does contribute a segment, and (ii) lines drawn from that point to any other sites don’t contribute any segments.

Part (a) of the figure shows a piece of Delaunay triangulation around site $o$ . The perpendicular bisectors of $O A$ and $O C$ meet at the point $X$ , which is therefore the center of the circle containing $A$ , $o$ , and $C$ . The issue is whether the Delaunay edge $O B$ can be “blocked” by the other two edges. Now, $B$ must lie inside the circumcircle just mentioned; otherwise, the edge $O B$ would have been an illegal edge when the Delaunay triangulation was constructed. But this means that the perpendicular bisector of $O B$ , labeled $U V$ , must “cut off the corner” at $X$ . Thus it does contribute a segment to the boundary.

![](images/a4119f99d01e945daf4e983af5e451cee993aae4abfcba081f091bd8350d1c7e.jpg)  
Figure 21.7.2. Key ideas in the proof that every Delaunay edge contributes exactly one Voronoi edge, lying on its perpendicular bisector. (a) Delaunay requires $B$ to lie inside the circle $A O C$ , hence its bisector must clip the corner inside $X$ . (b) Delaunay requires any other site $P$ to lie outside of the circle $A O B$ , hence its bisector can’t clip the corner inside $X$ .

![](images/b959753465ddd1f262613fca798a4b2a12cc3c790ae6683aa345a81de399d604.jpg)  
Figure 21.7.3. The circumcenters of the Delaunay triangles around a point $o$ are the vertices of $o$ ’s Voronoi region (shown as shaded), because the perpendicular bisectors of the Delaunay edges meet at these circumcenters. Notice that a Voronoi edge need not actually intersect the Delaunay edge with which it is associated, as $S R$ and $o c$ .

Part (b) of the figure shows a Delaunay triangle $O A B$ whose edges $O A$ and $O B$ are contributing perpendicular bisector segments to the Voronoi boundary around $O$ . Point $P$ is some other site. Can it somehow worm its way in close enough to contribute a segment of its own bisector, between the other two? Evidently not: We know that the circumcircle of any Delaunay triangle contains no other sites. Since $P$ must lie outside the circumcircle, its bisector $U V$ can’t cut off the corner at $X$ .

The fact that the Voronoi vertices are the circumcenters of Delaunay triangles is an immediate consequence of the previous discussion (see Figure 21.7.3). The circumcenters are where the perpendicular bisectors of the edges meet. Since every Delaunay edge contributes a segment, every such circumcenter must be a vertex. Notice, however, that not every Delaunay triangle contains its own circumcenter (as $O C D$ in the figure), so that a segment on the boundary of a Voronoi region need not actually intersect the Delaunay edge with which it is associated (as $R S$ and $O C$ in the figure).

We can count the number of edges and vertices in a Voronoi diagram with $N$ sites ( $\scriptstyle { n }$ of which are on the convex hull) simply by knowing that its dual is the Delaunay triangulation and using equation (21.6.1). The number of Voronoi edges is thus $L$ in that equation, while the number of Voronoi vertices is $T$ . The number of Voronoi regions is by definition $N$ . The unbounded Voronoi regions are exactly those whose points lie on the convex hull of the sites, so there are $n$ of these. It turns out (not immediately obviously) that the average number of edges in one Voronoi region (averaged over all the sites) does not exceed six.

Turning to the implementing code, it is convenient to have a structure for holding Voronoi edges, and also their association with the site that they surround (as an integer pointer to a list of sites).

# struct Voredge {

Structure for an edge in a Voronoi diagram, containing its two endpoints and an integer pointer to the site of which it is a boundary.

Point<2> p[2];   
Int nearpt;   
Voredge() {}   
Voredge(Point<2> pa, Point<2> pb, Int np) : nearpt(np) { p[0] $=$ pa; p[1] $=$ pb;   
}

Now it is straightforward to define a Voronoi structure, as a derived class of the Delaunay structure. The constructor creates a Delaunay triangulation of the sites, and then loops over the sites. For each, it first finds any one triangle with the site as a vertex, and then works its way around the site in a circle, navigating counterclockwise from one triangle to the next by looking up their common edge in the linehash hash memory. Each triangle’s circumcenter is a Voronoi vertex, and a Voronoi edge is stored for each two consecutive circumcenters as the site is circumnavigated.

# struct Voronoi : Delaunay {

Structure for creating a Voronoi diagram, derived from the Delaunay structure. Int nseg; Number of edges in the diagram. VecInt trindx; Will index triangles. vector<Voredge> segs; Will be array of all segments. Voronoi(vector< Point<2> $>$ pvec); Construct Voronoi diagram from array of points.   
};   
Voronoi::Voronoi(vector< Point<2> $>$ pvec) : Delaunay(pvec,1), nseg(0), trindx(npts), segs(6\*npts+12) {   
Constructor for Voronoi diagram of a vector of sites pvec. Bit ”1” sent to the Delaunay con  
structor tells it not to delete linehash. Int i,j,k,p,jfirst; Ullong key; Triel tt; Point<2> cc, ccp; Create a table so that, given a point numfor $\scriptstyle ( { \dot { \mathsf { J } } } = 0$ ; j<ntree; ${ \mathrm { j } } + + { \mathrm { . } }$ ) { ber, we can find one triangle with it as if (thelist[j].stat $\scriptstyle < = 0 .$ ) continue; a vertex. tt $=$ thelist[j]; for $\scriptstyle ( \mathtt { k } = 0$ ; k<3; $\mathrm { k } { + } { + }$ ) trindx[tt.p[k]] = j; } Now loop over the sites. for ( $\scriptstyle \cdot p = 0$ ; p<npts; $\mathbb { p } ^ { + + }$ ) {

tt $=$ thelist[trindx[p]]; if (tt.p[0] $\scriptstyle = = \ p ,$ ) {i = tt.p[1]; ${ \dot { \mathrm { ~  ~ } } } =$ tt.p[2];} Get the vertices into canonelse if (tt.p[1] $\scriptstyle = = \ p$ ) {i $=$ tt.p[2]; ${ \mathrm { ~ j ~ } } =$ tt.p[0];} ical order. else if (tt.p[2] $\mathbf { \Phi } = \mathbf { \Phi } _ { \mathsf { P } }$ ) {i $=$ tt.p[0]; j $=$ tt.p[1];} else throw("triangle should contain $\mathbb { P } ^ { \mathfrak { \ " } } .$ ); jfirst $= \ j$ ; Save starting vertex and its circumcircle. ccp $=$ circumcircle(pts[p],pts[i],pts[j]).center; while (1) { Go around CCW, find circumcenters and store segments. key $=$ hashfn.int64(i) - hashfn.int64(p); if ( ! linehash->get(key,k) ) throw("Delaunay is incomplete"); cc $=$ circumcircle(pts[p],pts[k],pts[i]).center; segs[nseg $+ + ] =$ Voredge(ccp,cc,p); if (k $= =$ jfirst) break; Circumnavigation completed. Normal way out. $\mathsf { c c p } \ = \ \mathsf { c c }$ ; $\dot { \mathsf { J } } { } ^ { = } \dot { \mathsf { \Phi } }$ ; $\dot { \bf \Phi } _ { 1 } = \bf k$ ; } } }

The result of the Voronoi construct is available by looping through the segs array from 0 to nseg-1. Each array element is a Voredge that stores the endpoints, and also the site number with which it is associated. Note that each segment appears twice in the list, with opposite sense, as it is associated in turn with the sites on its two sides.

If you read our confession about dirty tricks in the previous section, you’ll want to keep in mind that the “open” Voronoi polygons are actually closed by segments that lie at a distance of order bigscale times the size of the bounding box of the sites. Those segments are included in segs but appear only once, since there is no site on their other side.

# 21.7.3 Other Applications

Nearest Neighbors, Again. A line segment that connects a point to its nearest neighbor among a set of points will be an edge in the set’s Delaunay triangulation. Informal proof: The nearest neighbor obviously must contribute a boundary to the Voronoi diagram. Formal proof (using a theorem mentioned above): The circle whose diameter connects a point to its nearest neighbor can’t contain any other points (they’d be closer than the nearest neighbor), so that diameter must be a Delaunay edge.

Since we can construct the Delaunay triangulation in ${ \cal O } ( N \log N )$ time, it follows that we can use it to find all nearest neighbors of a set of $N$ points in ${ \cal O } ( N \log N )$ time. The process is as follows: (i) Construct Delaunay. (ii) For each point, circumnavigate it. (We saw how to do this in our implementation of Voronoi, above.) (iii) Pick the shortest of the edges with the point at one end.

Convex Hull. Sometimes you may need to know the convex hull of a set of points in the plane for some other application. Although it might seem wasteful to construct the whole Delaunay triangulation just to get the hull, doing so is not too bad a method. Better efficiency can be achieved by ignoring, during the triangulation, points that are found to be already inside interior triangles. To sort the edges into the order of a CCW polygon, we create a nextpt table of edge destinations as we go, then chain through it once to output the vertices of the convex hull in proper order.

# struct Convexhull : Delaunay {

Structure for constructing the convex hull of a set of points in the plane. After construction, nhull is the number of points in the hull, and hullpoints[0..nhull-1] are integers pointing to points in the vector pvec that are in the hull, in CCW order.

Int nhull; Int \*hullpts; Convexhull(vector< Point<2> $>$ pvec); Construct from a vector of points. };

Convexhull::Convexhull(vector< Point<2> $>$ pvec) : Delaunay(pvec,2), nhull(0) { Constructor for convex hull of a vector of points pvec. Bit ” $2 "$ sent to the Delaunay constructor tells it to ignore interior points when it can, for extra speed.

Int i,j,k,pstart;   
vector<Int> nextpt(npts);   
for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ; j<ntree; ${ \mathrm { j } } + + { \mathrm { , } }$ ) { Triangles with stat $\ c = - 1$ may contain if (thelist[j].stat $\ ! = ~ - 1 )$ continue; hull segments. for $^ { \prime } \mathrm { i } { = } 0 , \mathrm { k } { = } 1$ ; i<3; i++,k++) { Need two valid points to qualify. if $( \mathrm {  ~ k ~ } ) = = \mathrm {  ~ 3 ~ }$ ) $\mathtt { k } = 0$ ; if (thelist[j].p[i] $<$ npts && thelist[j].p[k] $<$ npts) break; if ( $\scriptstyle \dot { 1 } = = 3$ ) continue; Case where failed to qualify. ++nhull; Yes! Put its other end in the lookup table, and save nextpt[(pstart $=$ thelist[j].p[k])] $=$ thelist[j].p[i]; its value in case it’s   
} the last one we find.   
if (nhull $\scriptstyle = = 0 .$ ) throw("no hull segments found");   
hullpts $=$ new Int[nhull]; Now we know how many, can allocate.   
$\scriptstyle { \dot { \mathsf { J } } } = 0$ ; One chain through the lookup table, start   
$\begin{array} { r l } { \dot { \bf 1 } } & { { } = } \end{array}$ hullpts[j $+ + ] \ =$ pstart; ing with pstart, gives the answer.   
while (( $\dot { \bf { \nabla } } \dot { \bf { \sigma } }$ nextpt[i]) $! =$ pstart) hullpts[j++] = i;

Largest Empty Circle Problem. The largest empty circle whose center lies (strictly) inside the convex hull of a set of points in the plane has its center on a Voronoi vertex. So, you can find it by looping through the Voronoi vertices, calculating the radius of the largest circle centered on each one, and taking the maximum of these. Even better, loop through the Delaunay triangles, calculate the circumcenter of each, and pick the one with the largest circumradius (since Delaunay circumcenters are exactly Voronoi vertices). Think of yourself as finding the best location for a fast-food restaurant within the (convex) city limits, one that best avoids all the other fast-food restaurants.

Avoiding Obstacles. If you want to navigate around the plane staying as far as possible from a set of points, your path will be along the edges of a Voronoi diagram. Think of yourself as a fighter pilot avoiding enemy radars.

Minimum Spanning Tree. The minimum spanning tree (sometimes Euclidean minimum spanning tree) is the set of line segments of shortest total length that connect $N$ points (see, e.g., Figure 21.7.4). Think of it as the highway map of the cheapest highway system that lets you visit all $N$ cities. It is topologically a tree (i.e., has no loops) because if it did have a loop, you could save highway money by deleting one of the loop’s segments.

The important theorem is: The minimum spanning tree is a subset of the Delaunay edges. You might think this isn’t very useful, since it doesn’t tell you which subset. Fortunately, there is a fast algorithm, Kruskal’s algorithm, for doing the construction. The basic idea is to sort all the Delaunay edges by length, and then add them one at a time to the growing tree, in order from smallest to largest.

Your tree starts off growing in multiple disconnected components, but when you have added exactly $N - 1$ segments, it will be a single piece, and the answer. There is only one catch: As you add segments, you must not add a segment if both its ends are already in the same component (else it would form a loop). So, you have to maintain an “equivalence class” relation for each vertex, making it equivalent to all other vertices in its connected component. We already know how to do this efficiently, as in $\ S 8 . 6$ ’s routine eclass. In the code below, there is a similar logic of sweeping up pointers to single “mother” representatives. Do this properly, and the method is ${ \cal O } ( N \log N )$ .

![](images/23f76da6d401494b204ac6cbb46708a57253888c131e319085adab38da8beaf5.jpg)  
Figure 21.7.4. Minimum spanning tree of 1001 points at random locations within a circle. The tree is composed of 1000 segments that connect all the points with the shortest total length and is a subset of the Delaunay triangulation of the same points.

Kruskal’s algorithm is a so-called greedy algorithm, since it just takes the best edge at each step willy nilly. It is rare for a greedy algorithm to yield the true global optimum; but this is the happy case where it does.

# struct Minspantree : Delaunay {

Structure for constructing the minimum spanning tree of a set of points in the plane. After construction, nspan is the number of segments (always $=$ npts1), and minsega[0..nspan-1] and minsegb[0..nspan-1] contain integers pointing to points in the vector pvec that are the two ends of each segment.

Int nspan; VecInt minsega, minsegb; Allocate arrays for the output. Minspantree(vector< Point<2> > pvec); };

inspantree::Minspantree(vector< Point<2> $>$ pvec) :

Delaunay(pvec,0), nspan(npts-1), minsega(nspan), minsegb(nspan) {

Constructor for the minimum spanning tree of a vector of points pvec. The Delaunay constructor gives the triangulation. We need only find the correct subset of edges.

Int i,j,k,jj,kk,m,tmp,nline, $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ 0 ~ }$ ;   
Triel tt;   
nline $=$ ntri $^ +$ npts -1; Number of edges in the triangulation.   
VecInt sega(nline); Allocate working space for two ends of each edge,   
VecInt segb(nline); edge length, and index on which we will sort.   
VecDoub segd(nline); Also the ”mother” tree for equivalence classes.   
VecInt mo(npts);   
for $\scriptstyle \dot { \mathcal { I } } = 0$ ; j<ntree; $\ j + + )$ ) { Find all edges in the triangulation, store them if (thelist[j].stat $\scriptstyle = = 0$ ) continue; and their lengths. tt $=$ thelist[j]; for ( $\mathbf { i } = 0 , \mathbf { k } = 1$ ; i<3; i++,k++) { if ( $k = = 3$ ) $\mathtt { k } = 0$ ;

if (tt.p[i] $>$ tt.p[k]) continue; Ensure we get each edge only once. if (tt.p[i] $> =$ npts || tt.p[k] $> =$ npts) continue; No edges connectsega[n] $=$ tt.p[i]; ing to fictitious segb[n] $=$ tt.p[k]; points. segd[n] $=$ dist(pts[sega[n]],pts[segb[n]]); $\mathtt { n } + +$ ; } Indexx idx(segd); Sort the edges by creating an index array. for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ; j<npts; ${ \mathrm { j } } + + { \mathrm { . } }$ ) mo[j] = j; Initialize equivalence relation tree. $\texttt { n } = \texttt { - } 1$ ; for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ; i<nspan; i++) { Add exactly nspan segments. for (;;) { Loop for the shortest valid segment n. jj $\mathbf { \dot { \omega } } = \mathbf { \dot { \omega } } \mathbf { j } \mathbf { \omega } = \mathbf { \dot { \omega } }$ idx.el(sega, $+ + \mathtt { n } )$ ; kk $= { \textbf { k } } =$ idx.el(segb,n); while (mo[jj] $\ ! =$ jj) jj $=$ mo[jj]; Track each end to its highest anceswhile (mo[kk] $\ ! =$ kk) kk $=$ mo[kk]; tor. if (jj ! $\downarrow =$ kk) { The segment is valid only if it connects different minsega[i] $=$ j; highest ancestors. minsegb[i] $=$ k; $\qquad { \textbar { 1 1 } } =$ mo[jj] $=$ kk; Now, equate the highest ancestors, and retrace $\mathrm { ~ j ~ j ~ } = \mathrm { ~ j ~ }$ ; our steps pointing all nodes encountered to while (mo[jj] $! = \mathrm { ~ m } )$ ) { that highest node, necessary for speed of the tmp $=$ mo[jj]; algorithm. mo[jj] $= ~ \mathfrak { m }$ ; jj = tmp; } kk $= \texttt { k }$ ; while (mo[kk] $! = \mathrm { ~ m } )$ ) { tmp $=$ mo[kk]; mo[kk] $= ~ \mathfrak { m }$ ; kk $=$ tmp; } break; A segment has been successfully added. } } }

# CITED REFERENCES AND FURTHER READING:

de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry:Algorithms and Applications, 2nd revised ed. (Berlin:Springer),Chapters 7 and 11.

O’Rourke, J. 1998, Computational Geometry in C, 2nd ed. (Cambridge, UK: Cambridge University Press), Chapter 5.

# 21.8 Quadtrees and Octrees: Storing Geometrical Objects

Different from a KD tree is another kind of box tree, usually called a quadtree in two dimensions or a octree in three dimensions. Yes, we know that it ought to be spelled “octtree,” not “octree,” but the latter usage has become standard. We’ll refer to quadtrees and octrees generically as “QO trees” and thus avoid linguistic controversy.

![](images/404be769d57b6f334ccf96ae94d5a1d7ea58316909bc6a5f18b12ff2356c9eb4.jpg)  
Figure 21.8.1. In a quadtree, the initial square 1 is first subdivided into squares 2, 3, 4, and 5. At the next level of subdivision, 2 is subdivided into 6, 7, 8, 9; 3 into 10, 11, 12, 13; and so forth.

QO trees start with a finite-sized box, usually square or cubical, rather than the near-infinite box used in the KD tree. A QO tree then subdivides each box not in one dimension at a time (as a KD tree) but rather in all dimensions. Thus, a square is subdivided into four daughter squares, a cube into eight daughter cubes — quite a brood. The coordinates of the subdivisions are taken to exactly bisect the mother box in each dimension, so all the boxes at one level of the tree are congruent, differing from the original box by a fixed power-of-two factor. Figure 21.8.1 illustrates this in the case of two dimensions.

QO trees thus provide a kind of addressing scheme for two- or three-dimensional space. Accordingly, they can be used to store and retrieve finite-sized geometrical objects that fit into the boxes of the tree at one or another level, and to test for intersections of such objects, for nearness relationships, and so on. The general idea (although there can be variations on this) is to store each object in the smallest box that completely contains it — or, in the case of a zero-sized object like a point, in the appropriate box at the deepest level of tree that we care to implement. Then, when doing a collision or nearness test, we traverse only those parts of the tree that are relevant, much as we did in the applications of KD trees.

Although we will illustrate only the most elementary of applications, QO trees are often at the heart of more complicated algorithms, for example [1-3],

- Hidden polygon removal in the visual plane (which projected polygons intersect a given pixel in the visual field?)   
- Fast gravitational or Coulomb N-body calculations (store fictitious objects on various scales that sweep up the multipole moments of the collections of point masses that they contain) [4,5,6]   
- Mesh generation (choose a local mesh scale to match the scale in the QO tree at which obstacles or boundaries are stored; the concept of a balanced QO tree is often used)   
- Image compression (store slowly varying parts of the image as objects high in the tree, and prune unnecessary daughters).

A main weakness of QO trees follows just from their geometrical regularity. If a finite-sized object being stored in a QO tree falls on the boundary between two boxes of about its size, then it can’t be stored in either of them. Instead, it gets stored in the larger — sometimes very much larger — box that first completely contains it. If $N$ “small” objects are stored, then the number that fall on boundaries of the highest-level boxes scales in two dimensions as $N ^ { 1 / 2 }$ , or in three dimensions as $N ^ { \bar { 2 } / 3 }$ . These objects will thus end up stored in just a few boxes at the top of the tree, and they will participate in almost all operations that check for collisions or nearness. Thus, QO trees can usually effect a time savings that turns a naive algorithm scaling as $N$ into one that scales as $N ^ { 1 / 2 }$ (in the two-dimensional case); but only rarely, or with specialized methods, can they get to that Nirvana of $\log N$ or constant scaling. Still, the square- (or, in three dimensions, cube-) root of a large number can be a large factor, and well worth saving in time. So QO trees are good to know about.

![](images/216a4fa563a2e14bd0d1ddc482f4ba75a07e1720450a8bd63fcb674692674908.jpg)  
Figure 21.8.2. Quadtree shown in tree form. Because of its regularity, a quadtree’s relationships can be described numerically. For example, the mother of box $_ n$ is the integer part of $n / 4$ . The left daughter of box $_ { n }$ is $4 n - 2$ .

That same geometrical regularity of QO trees allows them to be implemented, at least optionally, as an efficient hash structure where most boxes in the tree, if they are empty, require no storage space. We will give such an implementation here, both for its intrinsic advantages and because it is fairly concise to code, using the Hash and Mhash classes from $\ S 7 . 6$ .

The key observations follow from Figure 21.8.2, which shows a QO tree laid out in tree form. The boxes are numbered as in Figure 21.8.1, starting with box 1 at the root of the tree. With this numbering scheme, there exist simple numerical relations between the mother and daughter boxes. This enables one to navigate the tree — up, down, and sideways — without the use of any stored pointers. In particular, if $k \geq 1$ is a box’s number, the following relationships hold in $D$ (for us, two or three) dimensions:

$$
\begin{array} { c } { { \mathrm { m o t h e r } \left( k \right) = \lfloor ( k + 2 ^ { D } - 2 ) / 2 ^ { D } \rfloor } } \\ { { \mathrm { l e f t m o s t d a u g h t e r } \left( k \right) = 2 ^ { D } k - 2 ^ { D } + 2 } } \\ { { \mathrm { r i g h t m o s t d a u g h t e r } \left( k \right) = 2 ^ { D } k + 1 } } \\ { { \mathrm { t o t a l b o x e s ~ t h r o u g h ~ l e v e l ~ p = \lfloor ( 2 ^ { D } ) ^ { p } - 1 \rfloor / ( 2 ^ { D } - 1 ) } } } \end{array}
$$

Note that the integer divide by $2 ^ { D }$ implied by the $\lfloor \ \rfloor$ notation can be implemented simply as a right shift by $D$ bits. You should check the formulas in (21.8.1) against Figure 21.8.2 to be sure that you understand how they work. The “levels” of the tree are numbered starting with $p = 1$ for (only) box 1. Notice that the mother of box 1 computes to 0, indicating that it has no mother; this is convenient for testing when to exit loops over ancestry.

Before we get to implementation details for the implementing class Qotree, we need to discuss the prerequisites for a class of geometrical objects to be stored in the tree. Qotree will be templated by a type parameter elT representing those objects. To store an object myel of type elT, you must be sure to provide a method myel.isinbox() whose argument is a Box, and which returns 1 if myel is in the Box, or 0 otherwise. Similarly, to erase an object, you need to provide an $= =$ operator, to decide (by comparison) which is the object to be erased. Those two methods are all that Qotree needs for itself. However, many applications of Qotree (including some that we illustrate later in this section) need either or both of the methods myel.contains() and myel.collides(), the first returning whether myel contains a given point, the second returning whether myel collides with another element of type elT.

Here is a simple example of a class, representing a circle (when DIM is 2) or sphere (when DIM is 3), that has these methods and can thus be stored and processed with a Qotree:

template<Int DIM> struct Sphcirc {   
Circle $\mathrm { \ ( D I M } { = } 2 )$ ) or sphere $\mathtt { D I M } = 3$ ) object, with methods suitable for use with Qotree. Point<DIM> center; Doub radius; Sphcirc() {} Default constructor is needed to make arrays. Sphcirc(const Point<DIM> &mycenter, Doub myradius) Construct by explicit center : center(mycenter), radius(myradius) {} and radius. bool operator $= =$ (const Sphcirc &s) const { Test if identical. return (radius $= =$ s.radius && center $= =$ s.center); } Int isinbox(const Box<DIM> &box) { Is the circle/sphere inside a box? for (Int i=0; i<DIM; $\dot { \bf 1 } + +$ ) { if ((center.x[i] - radius $<$ box.lo.x[i]) || (center.x[i] $^ +$ radius $>$ box.hi.x[i])) return 0; return 1; } Int contains(const Point<DIM> &point) { Is a given point inside the circle/sphere? if (dist(point,center) $>$ radius) return 0; else return 1; } Int collides(const Sphcirc<DIM> &circ) { Does it collide with another circle/sphere? if (dist(circ.center,center) $>$ circ.radius+radius) return 0; else return 1; }   
};

# 21.8.1 A Hashed QO Tree Implementation

We will implement the QO tree using two hash memories. First, there is an Mhash multimap memory (called elhash) whose keys are box numbers and whose stored elements are the geometrical objects that may be stored in the QO tree, with possibly multiple objects in a single box. Second, there is a single-valued Hash memory (called pophash) that associates an integer with every box that either (i) contains one or more elements (is “populated”), or (ii) is an ancestor to a box that is populated. In that integer, bit 0 (least significant bit) is used to indicate whether the box is populated, while bits $1 \ldots 2 ^ { D }$ (that is, 1 : : : 4 or 1 : : : 8) are used to indicate which (if any) daughters are themselves either populated or are an ancestor to a populated box. In other words, pophash, combined with the relationships in equation (21.8.1), substitutes for the entire structure of doubly linked pointers that might more conventionally implement the tree.

The maximum number of levels $p _ { \mathrm { m a x } }$ that we can represent is limited only by the largest value that can be represented by the integer type that stores box numbers $k$ . Using 32-bit signed integers, 16 levels are possible in two dimensions, since $( 4 ^ { 1 6 } - 1 ) / 3 < \breve { 2 } ^ { 3 1 } - 1$ (cf. equation 21.8.1). In three dimensions, 11 levels can be represented, since $( 8 ^ { 1 1 } - 1 ) / 7 <$ $2 ^ { 3 1 } - 1$ . Often there is no need for this much resolution $( \sim \mathsf { 1 0 } ^ { 9 }$ boxes), so we will provide for setting a smaller value of $p _ { \mathrm { m a x } }$ , a good idea since the time to traverse one branch of the tree from root to leaf (a frequently occurring “atom” in other procedures) scales linearly with $p _ { \mathrm { m a x } }$ .

template<class elT, Int DIM> struct Qotree {   
Quadtree $\left( \mathtt { D I M } = 2 \right)$ ) or octree $\scriptstyle \left( \mathtt { D I M } = 3 \right)$ ) object to store geometrical objects of type elT. static const Int PMAX $=$ 32/DIM; Roughly how many levels fit in 32 bits. static const Int $\mathsf { Q } \mathsf { O } \ = \ \mathsf { ( 1 } \ \ll \ \mathsf { D } \mathtt { I } \mathsf { M } )$ ; I.e., 4 for quad-, 8 for oct-. static const Int $\mathbb { Q } \mathbb { L } \ = \ \left( \mathbb { Q } \mathbb { O } \ - \ 2 \right)$ ; Offset constant to leftmost daughter. Int maxd; Doub blo[DIM]; Doub bscale[DIM]; Mhash<Int,elT,Hashfn1> elhash; Contains stored elements hashed by box #. Hash<Int,Int,Hashfn1> pophash; Contains node population info. Qotree(Int nh, Int nv, Int maxdep); The constructor. See below. void setouterbox(Point<DIM> lo, Point<DIM> hi); Set scale and position. Box<DIM> qobox(Int k); Return the box whose number is k. Int qowhichbox(elT tobj); Return smallest box containing tobj. Int qostore(elT tobj); Store an elT object in the Qotree. Int qoerase(elT tobj); Erase an elT object in the Qotree. Int qoget(Int k, elT \*list, Int nmax); Retrieve all objects in box k. Int qodump(Int \*k, elT \*list, Int nmax); Retrieve all objects. Int qocontainspt(Point<DIM> pt, elT \*list, Int nmax); See below. Int qocollides(elT qt, elT \*list, Int nmax); See below.   
};

template<class elT, Int DIM> Qotree<elT,DIM>::Qotree(Int nh, Int nv, Int maxdep) : elhash(nh, nv), maxd(maxdep), pophash(maxd\*nh, maxd\*nv)

Constructor for a quad- $\mathtt { ( D I M = 2 ) }$ ) or oc- $\mathtt { ( D I M = 3 ) }$ ) tree that can store a max of nv elements of type elT, using hash tables of length nh (typically $\approx \mathtt { n v }$ ). maxdep is the number of levels to be represented.

if (maxd $>$ PMAX) throw("maxdep too large in Qotree"); setouterbox(Point<DIM>(0.0,0.0,0.0),Point<DIM>(1.0,1.0,1.0)); Default scale. }

template<class elT, Int DIM>   
void Qotree<elT,DIM>::setouterbox(Point<DIM> lo, Point<DIM> hi) {   
Sets the scale of Qotree to an outer box defined by points lo and hi. Must be called before any elements are stored in the tree.   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<DIM; $\mathrm { j } { + + } )$ { blo[j] $=$ lo.x[j]; bscale[j] $=$ hi.x[j] - lo.x[j];   
}

You will normally call setouterbox() immediately after invoking the qotree constructor to create a QO tree. Otherwise, you get the default box with a corner at the origin and unit size in each dimension.

Right away, we need two utility routines. The first takes a box’s number (e.g., as in Figure 21.8.1) and returns the actual box (as a Box<DIM>). The second takes an object of the type to be stored in the tree (elT) and returns the number of the smallest box that contains it. It does this by starting at the top of the tree, trying each possible daughter, and moving deeper into the tree only when a containment is found.

template<class elT, Int DIM>   
Box<DIM> Qotree<elT,DIM>::qobox(Int k) {   
Returns the box indexed by k. Int j, kb; Point<DIM> plo, phi;   
Doub offset[DIM];   
Doub del $= ~ 1 , 0$ ;   
for $( \ j = 0$ ; j<DIM; $\mathrm { j } { + } { + } )$ offset[j] $= ~ 0 . 0$ ;   
while (k > 1) { Up through ancestors until get to root. kb $=$ (k + QL) % QO; Which daughter is $\mathtt { k 7 }$ Add its offset. for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<DIM; ${ \dot { \mathsf { J } } } ^ { + + }$ ) { if (kb & $( 1 < < \mathrm { ~ j ~ } )$ offset[j] $+ =$ del; $\mathrm { \bf ~ k ~ } = \mathrm { \bf ~ \left( ~ k ~ + ~ \frac { } { } ~ \frac { } { } ~ \right) ~ } > > \mathrm { \bf ~ D I M } ;$ Replace k by its mother, del $* = ~ 2 , 0$ ; where offsets will be twice as big.   
}   
for $( \ j = 0$ ; j<DIM; $\mathrm { j } { + + } )$ { At the end, scale the offsets by the final del to plo.x[j] $=$ blo[j] $^ +$ bscale[j]\*offset[j]/del; make them metrically correct. phi.x[j] $=$ blo[j] $^ +$ bscale[j] $^ *$ (offset[j] $^ { + 1 }$ .0)/del;   
}   
return Box<DIM>(plo,phi); Construct the box and return it.

# template<class elT, Int DIM>

Int Qotree<elT,DIM>::qowhichbox(elT tobj) {

Return the box number of the smallest box that can contain an element tobj, without regard to whether tobj is already stored in the tree.

Int p,k,kl,kr,ks $^ { = 1 }$ ; Answer is box 1 unless a smaller box found.   
for ${ \tt ( p = } 2$ ; $\mathrm { p } < =$ maxd; $\mathtt { p } ^ { + + }$ ) { Go down through the levels. $\mathrm { k 1 ~ = ~ 0 0 ~ ^ { \circ } ~ ^ { \circ } ~ ^ { \mathrm { k s } ~ - ~ } ~ \mathsf { Q L } }$ ; Leftmost daughter. $\mathbf { k } \mathbf { r } \ = \ \mathbf { k } \mathbf { l } + \mathbf { 0 } 0 - \mathbf { 1 } ;$ ; Rightmost daughter. for (k=kl; $\mathtt { k } < = \mathtt { k } \mathtt { r }$ ; $\mathtt { k } { + } { + }$ ) { Do any daughters contain tobj? if (tobj.isinbox(qobox(k))) $\left\{ \begin{array} { r l } \end{array} \right. \mathrm { k s } = \mathrm { ~ k ~ } _ { 1 }$ ; break; } } if $( \textbf { k } > \textbf { k r } )$ ) break; No. Therefore, discontinue descent here.   
}   
return ks;

Now we are ready to store elements into the tree, or to erase elements previously stored. With qowhichbox(), above, and the methods that belong to the Mhash, it is trivial to do the actual store or erase. Trickier to code is to create or erase the trail of “breadcrumbs” in pophash that connect the box to its ancestors. When we erase, we must be sure not to cut off the trail to any remaining elements in the same box, or to elements in descendant boxes.

template<class elT, Int DIM>   
Int Qotree<elT,DIM>::qostore(elT tobj){   
Store the element tobj in the Qotree, and return the box number into which it was stored. Int k,ks,kks,km; $\mathbf { k } \mathbf { s } ~ = ~ \mathbf { k } \mathbf { k } \mathbf { s } ~ = ~ \mathbf { \Omega }$ qowhichbox(tobj); elhash.store(ks, tobj); Store the element in elhash pophash[ks] $\mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf \Sigma \mathbf { \Sigma } \mathbf { \Sigma } \mathbf \Sigma \Sigma \mathbf { } \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \ S \Sigma \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S $ ; and mark its box as populated. while (ks > 1){ Now leave trail of breadcrumbs to the root mother. km $=$ (ks $^ +$ QL) >> DIM; Mother of ks. $\mathrm { ~ \bf ~ k ~ } = \mathrm { ~ \bf ~ k s ~ } - { \bf ~ \tau }$ (QO\*km - QL); Which daughter of km is ks. $\mathtt { k s } ~ = ~ \mathtt { k m }$ ; Now set the daughter bit in the mother. pophash[ks] $| = \mathbf { \Gamma } ( 1 \ < < \ \mathbf { \Gamma } ( \mathbf { k } { + } 1 ) ) \ \rangle$ ; } return kks;   
} template<class elT, Int DIM>   
Int Qotree<elT,DIM>::qoerase(elT tobj) {   
Erase the element tobj, returning the box number into which it was stored or 0 if the element was not found in the Qotree. Note logic very similar to qostore. Int k,ks,kks,km;   
Int \*ppop;   
ks $=$ kks $=$ qowhichbox(tobj); Find the box.   
if (elhash.erase(ks, tobj) $\ c = 0 .$ ) return 0; It ain’t there! if (elhash.count(ks)) return kks; Sisters still in same box, so we are done.   
ppop $=$ &pophash[ks];   
\*ppop &= \~((Uint)1);   
while (ks > 1) { if (\*ppop) break; pophash.erase(ks); km $=$ (ks $^ +$ QL) $> >$ DIM; $\mathrm { ~ \bf ~ k ~ } =$ ks - (QO\*km - QL); k $\mathrm { ~ s ~ } = \mathrm { ~ k m ~ }$ ; ppop $=$ &pophash[ks]; \*ppop $\& =$ \~((Uint)(1 << (k+1)));   
return kks; Must now erase any unneeded breadcrumbs.   
Unmark the pop bit.   
Up through the ancestors...   
Box is populated or has daughters, so done.   
Erase unneeded (zero) pophash entry.   
Mother of ks.   
Which daughter of km is ks.

Unset the daughter bit in the mother.

Finally, we need methods to retrieve elements previously stored, either those in a given box (by number), or else all the elements in the tree. In the former case, the Mhash does all the work. In the latter case, however, we must provide the machinery for a recursive search of the tree, since at any stage we may encounter a box with multiple populated daughters. Notice that the calling routine is responsible for supplying storage (as an array list[]) for the result and declaring the maximum number nmax of elements that it is prepared to accept.

# template<class elT, Int DIM>

Int Qotree<elT,DIM>::qoget(Int k, elT \*list, Int nmax)

Retrieve all (or up to nmax if it is smaller) elements that are stored in box k of the Qotree. The elements are copied into list[0..nlist-1] and the value nlist ( $\leq$ nmax) is returned.

Int ks, pop, nlist; ks $\mathit { \Theta } = \mathit { \Theta } \mathbf { k }$ ; nlist $\qquad = \ 0$ ; pophash.get(ks,pop); if ((pop & 1) && elhash.getinit(ks)) { while (nlist $<$ nmax && elhash.getnext(list[nlist])) {nlist++;} return nlist; }

#

# template<class elT, Int DIM>

Int Qotree<elT,DIM>::qodump(Int \*klist, elT \*list, Int nmax) {

Retrieve all (or up to nmax if it is smaller) elements that are stored anywhere in the Qotree, along with their corresponding box numbers. The elements are copied into list[0..nlist-1] and the value nlist ( $\leq$ nmax) is returned. The box numbers are copied into klist[0..nlist-1].

Int nlist, ntask, ks, pop, k;   
Int tasklist[200]; Stack of pending box numbers as we recur  
nlist $\qquad = \ 0$ ; sively traverse the tree.   
ntask $\ c = ~ 1$ ;   
tasklist[1] $\ l = \ 1$ ;   
while (ntask) { As long as tasks remain... ks $=$ tasklist[ntask--]; if (pophash.get(ks,pop) $\ c = 0 .$ ) continue; Box empty and no daughters. if ((pop & 1) && elhash.getinit(ks)) { The box is populated, so we output while (nlist $<$ nmax && elhash.getnext(list[nlist])) { its contents. klist[nlist] $=$ ks; nlist++; } } if (nlist $= =$ nmax) break; No more room for output! $\mathrm { ~ \bf ~ k ~ } =$ QO\*ks - QL; Leftmost daughter. while (pop $> > = ~ 1$ ) { Loop over the daughter bits in pop. if (pop & 1) tasklist[++ntask] $= \mathrm { ~ k ~ } ;$ Daughter exists. Add to task list. k++; Next daughter. }   
}   
return nlist;

The additional functions declared in Qotree pertain to applications, as we now discuss.

# 21.8.2 QO Tree Elementary Applications

Two important building blocks for applications of QO trees are, first, a routine that returns a list of all stored elT elements that intersect (i.e., contain) a specified point; and, second, a routine that returns a similar list of all stored elT elements that intersect (i.e., collide with) a specified elT element.

An element that intersects a point will evidently be stored in a box that is an ancestor to the box that the point is in, or else in the same box as the point. It takes just one pass down through the levels of the tree to find all such elements.

template<class elT, Int DIM> Int Qotree<elT,DIM>::qocontainspt(Point<DIM>pt, elT \*list, Int nmax) { Retrieve all (or up to nmax if it is smaller) elements in Qotree that contain the point pt. The elements are copied into list[0..nlist-1] and the value nlist $\leq$ nmax) is returned.

Int j,k,ks,pop,nlist;   
Doub bblo[DIM], bbscale[DIM];   
for $\scriptstyle \dot { \ j } = 0$ ; j<DIM; $\mathrm { j } { + } { + } )$ { bblo[j] $=$ blo[j]; bbscale[j] $=$ bscale[j]; }   
nlist $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
ks $= ~ 1$ ; Start at the top of the tree.   
while (pophash.get(ks,pop)) { Descend as long as something is there. if (pop & 1) { The box is populated, so we check its conelhash.getinit(ks); tained elements, while (nlist $<$ nmax && elhash.getnext(list[nlist])) if (list[nlist].contains(pt)) {nlist++;} returning any that contain } pt. } if ((pop $> > = \ 1 ) = = \ 0 \ ,$ ) break; The box has no daughters, so we are done. for $( \mathrm { k } = 0$ , $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<DIM; ${ \mathrm { j } } + + )$ { Compute k, the single daughter containing bbscale[j] $* = ~ 0 , 5$ ; pt. if (pt.x[j] $>$ bblo[j] $^ +$ bbscale[j]) { k $+ = \ ( \mathrm {  ~ 1 ~ } \ll \mathrm {  ~ j ~ } )$ ; bblo[j] $+ =$ bbscale[j]; } } $\mathrm { i f } ( ( \mathrm { p o p } > > \mathrm { k } ) \& \ 1 ) = = 0 )$ ) break; No such daughter exists in the tree. $\mathrm { k s ~ = ~ 0 0 ~ * ~ k s ~ - ~ 0 L ~ + ~ k } ;$ ; Daughter exists and is the next node to check.   
1   
return nlist;

When an element $A$ intersects another element $B$ , either $A$ and $B$ are in the same box, or else $A$ is in an ancestor box to $B$ , or else $B$ is in an ancestor box to $A$ . Equivalently, for a fixed $A$ , we can find all intersecting $B$ ’s by searching $A$ ’s box, its ancestors, and its descendants. The latter search requires a task list stack, as we have seen before (e.g., in qodump).

# qotree.h

# template<class elT, Int DIM>

Int Qotree<elT,DIM>::qocollides(elT qt, elT \*list, Int nmax) {

Retrieve all (or up to nmax if it is smaller) elements in Qotree that collide with an element qt (which needn’t be in the tree itself). The elements are copied into list[0..nlist-1] and the value nlist $\mathbf { \beta } ( \leq \mathtt { n m a x } )$ is returned.

Int k,ks,kks,pop,nlist,ntask;   
Int tasklist[200];   
nlist $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
k $\begin{array} { r } { \mathrm { ~  ~ \tau ~ } _ { \mathrm { S } } ~ = ~ \mathrm { k s } ~ = ~ } \end{array}$ qowhichbox(qt);   
ntask $\qquad = \ 0$ ;   
while (ks $> 0$ ) {   
Stack of pending box numbers.   
kks saves the starting box.   
Put the starting box and all its ancestors on the task list.

tasklist $[ + +$ ntask] $=$ ks; ks = (ks + QL) >> DIM; Move to mother. } while (ntask) { ks $=$ tasklist[ntask--]; if (pophash.get(ks,pop) $\scriptstyle = = 0$ ) continue; Box empty and no daughters. if (pop & 1) { The box is populated, so we check its contained elhash.getinit(ks); elements, while (nlist $<$ nmax && elhash.getnext(list[nlist])) { if (list[nlist].collides(qt)) {nlist++;} returning any that col-} lide with qt. } if (ks $> =$ kks) { Recurse only for descendants, not ancestors! $\mathrm { ~ \bf ~ k ~ } =$ QO\*ks - QL; Leftmost daughter. while (pop $> > = ~ 1$ ) { if (pop & 1) Daughter exists. Add to task list. tasklist[ $^ { + + }$ ntask] k; k++; Next daughter. } } 1 return nlist;

As an example of a simple application of a QO tree, let’s replicate the functionality of KDtree::locatenear (-21.2) with a routine that finds all stored points within a specified radius $r$ of a test point. Using the class Sphcirc, points are represented as circles/spheres of zero radius, the test point as a circle/sphere of radius $r$ , and we use qocollides to find the collisions.

We implement this application as a structure, Nearpoints, whose constructor creates the QO tree out of a vector of points, and whose member function locatenear can then be called to find all stored points within any specified radius of any specified point.

# template <int DIM> struct Nearpoints {

Object for constructing a QO tree containing a set of points, and for repeatedly querying which stored points are within a specified radius of a specified new point.

Int npts;   
Qotree<Sphcirc<DIM>,DIM> thetree;   
Sphcirc<DIM> \*sphlist;   
Nearpoints(const vector< Point<DIM> $>$ &pvec) : npts(pvec.size()), thetree(npts,npts,32/DIM) Constructor. Creates the QO tree from a vector of points pvec. Int j,k; sphlist $=$ new Sphcirc<DIM>[npts]; Point<DIM> lo $=$ pvec[0], hi $=$ pvec[0]; Find bounding box for the points. for (j=1; j<npts; j++) for ( $\scriptstyle 1 = 0$ ; k<DIM; $\mathrm { k } { + } { + } \mathrm { \Gamma }$ ) { if (pvec[j].x[k] $<$ lo.x[k]) lo.x[k] $=$ pvec[j].x[k]; if (pvec[j].x[k] $>$ hi.x[k]) hi.x[k] $=$ pvec[j].x[k]; } for $( \mathrm { k } = 0$ ; k<DIM; $\mathtt { k } { + } { + }$ ) { Expand it by $10 \%$ so that all points lo.x[k] $- =$ 0.1\*(hi.x[k]-lo.x[k]); are well interior. hi.x[k] $+ =$ 0.1\*(hi.x[k]-lo.x[k]); } thetree.setouterbox(lo,hi); Set the tree’s outer box and store all the points. for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<npts; ${ \dot { \mathsf { J } } } ^ { + + }$ ) thetree.qostore(Sphcirc<DIM>(pvec[j],0.0));   
}   
\~Nearpoints() { delete [] sphlist; }   
Int locatenear(Point<DIM> pt, Doub r, Point<DIM> \*list, Int nmax) {

Once the tree is constructed, this function can be called repeatedly with varying points pt and radii $\mathbf { r }$ . It returns n, the number of stored points within radius r of pt (but no larger than nmax), and copies those points into list[0..n-1].

Int j,n; $\mathrm { ~ n ~ } =$ thetree.qocollides(Sphcirc<DIM>(pt,r),sphlist,nmax); for ( $\scriptstyle { \dot { \mathbf { J } } } = 0$ ; $\scriptstyle { \dot { \mathsf { J } } } < { \mathsf { n } }$ ; ${ \mathrm { j } } + +$ ) list[j] $=$ sphlist[j].center; return n; } };

In practice, the routine above is rather slower than KDtree::locatenear for this application, because there is a lot of overhead involved in copying Point and Sphcirc elements around, and in computing Boxes as we drill down the tree. By contrast, KDtree is lean and mean, since it only stores points and, in our implementation, copies them internally to a fast store of coordinates.

Unlike the KD tree, however, the technique illustrated here can be generalized to much more complicated situations. For example, instead of being simple points, the stored objects could be broadcast reception areas for FM radio stations on a given frequency, and we might want to know where collisions occur with proposed new stations. The collides() function between two broadcast areas might involve a lengthy calculation taking into account their powers, the surrounding detailed topography, and so on. In such a case, the overhead of the QO tree might well be negligible as we seek to minimize the number of calls to collides().

As a second example of a simple application, consider a square Petri dish on which spores land, in random positions, one at a time. Each such spore quickly grows into a circular colony that just touches the nearest existing colony (or the edge of the dish), and then stops. (Don’t ask us why. This is only an example.) What does the dish look like after $N$ spores have landed?

Rather than give the code in detail, a simple description should suffice: The objects stored in the QO tree are circles. Looping over the number of spores, we pick a random location for each in turn. If the QO tree method qocontainspt() indicates that the location lies within an already-stored colony, go on to the next spore. Otherwise, start with a small trial radius and increase it (by doubling, e.g.) until qotreecollides() first indicates collisions. Now adjust the trial radius to be the minimum of distances to the colliding elements, add that colony to the tree, and go on to the next spore.

Figure 21.8.3 shows an example of the resulting configuration, after 1000 colonies have grown. (Another 3592 spores landed inside existing colonies and died immediately.)

# CITED REFERENCES AND FURTHER READING:

de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry: Algorithms and Applications, 2nd revised ed. (Berlin: Springer), Chapter 14.[1]   
Samet, H. 1990, The Design and Analysis of Spatial Data Structures (Reading, MA: Addison-Wesley).[2]   
Samet, H. 1990, Applications of Spatial Data Structures: Computer Graphics, Image Processing, and GIS (Reading, MA: Addison-Wesley).[3]   
Pfalzner, S. and Gibbon, P. 1996, Many-Body Tree Methods in Physics (Cambridge, UK: Cambridge University Press).[4]   
Greengard, L., and Wandzura, S., eds. 1998, “Fast Multipole Methods,” special issue of IEEE Computational Science and Engineering,vol.5, no.3 (July-September),pp.16-56.[5]   
Gumerov, N.A., and Duraiswami, R. 2004, Fast Multipole Methods for the Helmholtz Equation in Three Dimensions (Amsterdam: Elsevier).[6]

![](images/16cdb71e80be9eafc4a7cf67e388f1f727454d5c0f09c1f4aa465beee28751e8.jpg)  
Figure 21.8.3. Spores land randomly on a square (!) Petri dish, and grow to colonies that barely touch the nearest pre-existing colony, or the edge of the dish. A QO tree can be used to keep track of collisions. Here, 1000 colonies have grown to their maximum size.

# Less-Numerical Algorithms

# 22.0 Introduction

You can stop reading now. You are done with Numerical Recipes, as such. This final chapter is an idiosyncratic set of “less-numerical recipes” that, for one reason or another, we have decided to include between the covers of an otherwise morenumerically oriented book. Authors of computer science texts, we’ve noticed, like to throw in a token numerical subject (usually quite a dull one — quadrature, for example). We find that we are not free of the reverse tendency.

Our selection of material is not completely arbitrary. In $\ S 9 . 0$ we promised to provide a simple plotting routine. Another promised topic, Gray codes, was already used in the construction of quasi-random sequences $( \ S 7 . 8 )$ and here needs only some additional explication. Two other topics, on diagnosing a computer’s floating-point parameters, and on arbitrary precision arithmetic, give additional insight into the machinery behind the casual assumption that computers are useful for doing things with real numbers (as opposed to integers or characters). The latter of these topics also shows a very different use for Chapter 12’s fast Fourier transform.

The three other topics (checksums, Huffman, and arithmetic coding) involve different aspects of data coding, compression, and validation. The material here is intended to be somewhat less abstract, and somewhat more practical, than the discussion of coding in $\ S 1 6 . 2$ , where coding was used to illustrate statistical aspects of state estimation. If you handle a large amount of data (numerical data, even), then a passing familiarity with these subjects might at some point come in handy. In $\ S 1 3 . 6$ , for example, we already encountered a good use for Huffman coding.

But again, you don’t have to read this chapter. (And you should learn about quadrature from Chapters 4 and 17, not from a computer science textbook!)

# 22.1 Plotting Simple Graphs

Yes, we all have our favorite plotting or graphics packages, and our favorite ways of generating plots from within $\mathrm { C } { + } { + }$ programs. But wait: Are your $\mathrm { C } { + + }$ programs generating long text files of numbers, just so that you can read those numbers into a separate plotting or graphics package? If so, you might benefit from this section.

![](images/004b61c6d541197b4e91fdd6f7579a33cd110c20ae664f4188347b9f432dfe15.jpg)  
Figure 22.1.1. Simple plot generated using the objects PSpage and PSplot, which are wrappers for generating PostScript.

We find it useful to have on hand a couple of short $\mathrm { C } { + } { + }$ objects, implemented in simple source code, that generate simple plots. (By “simple,” we mean “like most of the figures in this book.”) We are then able to make plots from anywhere in our programs, whether as an aid in debugging or as final output. Equally important, we can make changes to the plotting source code at will, adding features or modifying the look of the plot.

One way of accomplishing these goals is by means of a $\mathrm { C } { + + }$ “wrapper” that does no more, nor less, than to write out a valid PostScript [1] file, which can be viewed or printed using a PostScript viewer such as the freely available Ghostscript/GSview [2]. In fact, the viewer can readily be invoked by a method within the wrapper object, so that the plot simply pops up in its own window on your screen.

An example will make this clearer. Figure 22.1.1 shows a sample plot that has a couple of $x$ ; $y$ scaled boxes, some lines and points of varying types, and some text labels. Here is the code that generates the figure:

x1[i] $=$ 5.\*i/499.;   
y1[i] $=$ exp(-0.5\*x1[i]);   
y2[i] $=$ exp(-0.5\*SQR(x1[i]));   
y3[i] $=$ exp(-0.5\*sqrt(5.-x1[i]));   
x2[i] $=$ cos(0.062957\*i);   
y4[i] $=$ sin(0.088141\*i);

# }

PSpage pg("d:\\nr3\\newchap20\\myplot.ps") PSplot plot1(pg,100.,500.,100.,500.);   
plot1.setlimits(0.,5.,0.,1.);   
plot1.frame();   
plot1.autoscales();   
plot1.xlabel("abscissa");   
plot1.ylabel("ordinate");   
plot1.lineplot(x1,y1);   
plot1.setdash("2 4");   
plot1.lineplot(x1,y2);   
plot1.setdash("6 2 4 2");   
plot1.lineplot(x1,y3);   
plot1.setdash("");   
plot1.pointsymbol(1.,exp(-0.5),72,16.);   
plot1.pointsymbol(2.,exp(-1.),108,12.);   
plot1.pointsymbol(2.,exp(-2.),115,12.);   
plot1.label("dingbat 72",1.1,exp(-0.5));   
plot1.label("dingbat 108",2.1,exp(-1.));   
plot1.label("dingbat 115",2.1,exp(-2.));   
Instantiate a page.   
Instantiate a plot on the page. Position is specified in pt $( 7 2 { \mathsf { p t } } =$ 1 in, or $2 8 ~ { \mathsf { p t } } = 1 ~ { \mathsf { c m } }$ ).

Unsets dash.

PSplot plot2(pg,325.,475.,325.,475.);   
plot2.clear();   
plot2.setlimits(-1.2,1.2,-1.2,1.2);   
plot2.frame();   
plot2.scales(1.,0.5,1.,0.5);   
plot2.lineplot(x2,y4); Instantiate a second plot.   
Erase what’s underneath it. pg.close();   
pg.display();

Pop up a window displaying the plot file.

The general idea is that a PSpage object (pg in the example above) represents a whole sheet of paper, or window on the screen. It can contain one or more PSplot objects. In the above example there are two: plot1 and plot2. PSplot objects can be separate on the page, or overlapping. Each has its own $x , y$ coordinate system, its own $x$ - and $y$ -axis labels, and so forth. With no more explanation than this, you should be able to find a program line above that corresponds to each feature in the figure. The last line makes the plot pop up on our screen.

Point symbols are referenced by their character number in the Zapf Dingbats font, which is built into PostScript. If you want to see all the possible symbols, a Web search for “LaTeX Postscript Dingbats” will turn up several charts. Or, just write a program to plot them all. (Hint: There are possibly useful symbols from 33 to 126, and from 161 to 254.)

A Webnote [3] gives the complete source code for the PSpage and PSplot objects, which is only about 150 lines long. In the course of writing this book, our personal version of the code expanded to about 450 lines. This is an order of magnitude or two less than the standard packages that are available in open source code, GNUPLOT, for example [4]. It is a question of trading off capability (theirs much greater) for ease of modifying the source code (you be the judge).

If you choose to go down this road, you’ll soon want to learn more of PostScript as a language. A good reference is [5].

# CITED REFERENCES AND FURTHER READING:

Adobe Systems, Inc. 1999, PostScript Language Reference, 3rd ed. (Reading, MA: Addison-Wesley).[1]   
Ghostscript and GSview $^ { 2 0 0 7 + }$ , at http://www.cs.wisc.edu/\~ghost/.[2]   
Numerical Recipes Software 2007, “Code for PSpage and PSplot,” Numerical Recipes Webnote No. $^ { 2 6 }$ ,athttp://www.nr.com/webnotes?26 [3]   
GNUPLOT $^ { 2 0 0 7 + }$ , at http://www.gnuplot.info.[4]   
McGilton, H., and Campione, M. 1992, PostScript by Example (Reading, MA: Addison-Wesley).[5]

# 22.2 Diagnosing Machine Parameters

A convenient fiction is that a computer’s floating-point arithmetic is “accurate enough.” If you believe this fiction, then numerical analysis becomes a very clean subject. Roundoff error disappears, and many finite algorithms are exact. Only manageable truncation error (-1.1) stands between you and a perfect calculation. Sounds rather naive, doesn’t it?

Yes, it is naive. Notwithstanding, we have adopted this fiction throughout most of this book. To do a good job of answering the question of how roundoff error propagates, or can be bounded, for every algorithm that we have discussed would be impractical. In fact, it would not be possible: Rigorous analysis of many practical algorithms has never been made, by us or anyone.

Almost all processors today share the same floating-point data representation, namely that specified in IEEE Standard 754-1985 [1], and therefore the same strengths and weaknesses as regards roundoff error. But this was not always so! The history of computing is full of machines with strange floating-point representations by modern standards. Many early computers had 36-bit words, typically partitioned as a sign bit, 8 bits of exponent, and 27 bits of mantissa. The influential IBM 7090/7094 series was of this type. The legendary CDC 6600 and 7600 machines, designed by Seymour Cray, had 60-bit words (sign, 11-bit exponent, 48-bit mantissa). A particularly odd design was the IBM STRETCH, whose 64 bits were allocated to an exponent flag bit, 10 exponent bits, the exponent sign, a 48-bit mantissa, its sign, and three flag bits. The exponent flag bit was used to signal overflow or underflow, while the other flag bits could be set by the user to indicate — anything! So let us all be grateful for IEEE 754.

Likewise, almost all numerical computing today is done in double precision, that is, in 64-bit words, what $\mathrm { C } { + } { + }$ defines as double and we denote as Doub. This, also, was not always so. It has happened (one might argue) because the availability of memory has increased even more rapidly than the appetite for it in numerical computation. Many programmers born before 1960 still feel a small frisson when they type double instead of float. Indeed, the vast majority of routines in this book will work just fine, for the vast majority of applications, with merely float precision. In most cases, the use of double simply serves to reinforce an erroneous belief in the above “convenient fiction.”

Still, every once in a while, you will need to know what the limitations of your machine’s floating-point arithmetic actually are — the more so when your treatment of floating-point roundoff error is going to be intuitive, experimental, or casual. This will certainly be true if you ever encounter a processor with nonstandard (that is, non-IEEE compliant) hardware. Such processors still do exist, though generally hidden away in embedded special-purpose devices.

If you are lucky, then calls to the methods in the $\mathrm { C } { + } { + }$ standard library class numeric_limits will tell you what you need to know. It is a good idea to familiarize yourself with that class, including some of its esoterica, like round_style and has_denorm [2].

A more experimental approach is to use methods that were developed to ferret out machine parameters in the bad old days before standards [3,4], especially parameters that were supposed to be transparent to the (ordinary) user. The object Machar, listed in full in a Webnote [5], gives an implementation of a number of of these methods. The quantities determined are

- ibeta is the radix in which numbers are represented, almost always 2, but historically sometimes 16, or even 10.   
- it is the number of base-ibeta digits in the floating-point mantissa $M$ .   
- machep is the exponent of the smallest (most negative) power of ibeta that, added to 1:0, gives something different from 1:0.   
- eps is the floating-point number ibetamachep, loosely referred to as the “floating-point precision.”   
- negep is the exponent of the smallest power of ibeta that, subtracted from 1:0, gives something different from 1:0.   
- epsneg is ibeta $\mathtt { n e g e p }$ , another way of defining floating-point precision. Not infrequently, epsneg is 0.5 times eps; occasionally eps and epsneg are equal.   
- iexp is the number of bits in the exponent (including its sign or bias).   
- minexp is the smallest (most negative) power of ibeta consistent with there being no leading zeros in the mantissa.   
- xmin is the floating-point number ibetaminexp, generally the smallest (in magnitude) useable floating value.   
- maxexp is the smallest (positive) power of ibeta that causes overflow.   
- xmax is $( 1 - \mathsf { e p s n e g } ) \times \mathsf { i b e t a } ^ { \mathrm { m a x e x p } }$ , generally the largest (in magnitude) useable floating value.   
- irnd returns a code in the range 0 : : : 5, giving information on what kind of rounding is done in addition, and on how underflow is handled. See below.   
- ngrd is the number of “guard digits” used when truncating the product of two mantissas to fit the representation.

The parameter irnd needs some additional explanation. In the IEEE standard, bit patterns correspond to exact, “representable” numbers. The specified method for rounding an addition is to add two representable numbers “exactly,” and then round the sum to the closest representable number. If the sum is precisely halfway between two representable numbers, it should be rounded to the even one (low-order bit zero). The same behavior should hold for all the other arithmetic operations, that is, they should be done in a manner equivalent to infinite precision, and then rounded to the closest representable number.

If irnd returns 2 or 5, then your processor is compliant with this standard. If it returns 1 or 4, then it is doing some kind of rounding, but not the IEEE standard. If irnd returns 0 or 3, then it is truncating the result, not rounding it — not desirable.

<table><tr><td rowspan=1 colspan=4>Sample Results Returned by Machar</td></tr><tr><td rowspan=1 colspan=1>precision</td><td rowspan=1 colspan=2>IEEE-compliant processorfloat          double</td><td rowspan=1 colspan=1>historicalDEC-VAX</td></tr><tr><td rowspan=1 colspan=1>ibeta</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>it</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>53</td><td rowspan=1 colspan=1>24</td></tr><tr><td rowspan=1 colspan=1>machep</td><td rowspan=1 colspan=1>-23</td><td rowspan=1 colspan=1>-52</td><td rowspan=1 colspan=1>-24</td></tr><tr><td rowspan=1 colspan=1>eps</td><td rowspan=1 colspan=1>1.19 × 10-7</td><td rowspan=1 colspan=1>2.22 × 10-16</td><td rowspan=1 colspan=1>5.96 × 10-8</td></tr><tr><td rowspan=1 colspan=1>negep</td><td rowspan=1 colspan=1>-24</td><td rowspan=1 colspan=1>-53</td><td rowspan=1 colspan=1>-24</td></tr><tr><td rowspan=1 colspan=1>epsneg</td><td rowspan=1 colspan=1>5.96 × 10-8</td><td rowspan=1 colspan=1>1.11 × 10-16</td><td rowspan=1 colspan=1>5.96×10-8</td></tr><tr><td rowspan=1 colspan=1>iexp</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>minexp</td><td rowspan=1 colspan=1>-126</td><td rowspan=1 colspan=1>-1022</td><td rowspan=1 colspan=1>-128</td></tr><tr><td rowspan=1 colspan=1>xmin</td><td rowspan=1 colspan=1>1.18 × 10-38</td><td rowspan=1 colspan=1>2.23×10-308</td><td rowspan=1 colspan=1>2.94 × 10-39</td></tr><tr><td rowspan=1 colspan=1>maxexp</td><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>1024</td><td rowspan=1 colspan=1>127</td></tr><tr><td rowspan=1 colspan=1>xmax</td><td rowspan=1 colspan=1>3.40 × 1038</td><td rowspan=1 colspan=1>1.79 × 10308</td><td rowspan=1 colspan=1>1.70 × 1038</td></tr><tr><td rowspan=1 colspan=1>irnd</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>ngrd</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr></table>

The other issue addressed by irnd concerns underflow. If a floating value is less than xmin, many computers underflow its value to zero. Values $\mathrm { i r n d } = 0 , 1$ ; or 2 indicate this behavior. The IEEE standard specifies a more graceful kind of underflow: As a value becomes smaller than xmin, its exponent is frozen at the smallest allowed value while its mantissa is decreased, acquiring leading zeros and “gracefully” losing precision. This is indicated by $\mathrm { i r n d } = 3 , 4$ ; or 5.

Sometimes results can be compiler-dependent. For example, some compilers underflow intermediate results ungracefully, yielding irnd $= 2$ rather than 5.

Call the report method in Machar to see the comparison between its results and those returned by numeric_limits. Some values returned by Machar for IEEE compliant processors are given in the table above and compared with an important historical processor, the DEC-VAX. This processor, like its predecessor PDP-11, used a representation with a “phantom” leading 1 bit in the mantissa. You can see that this achieved a smaller eps for the same wordlength but could not underflow gracefully, since there were no denormalized numbers.

# CITED REFERENCES AND FURTHER READING:

IEEE Standard for Binary Floating-Point Numbers,ANSI/IEEE Std 754-1985 (New York: IEEE, 1985).[1]   
Josuttis, N.M. 1999, The $C { + } { + }$ Standard Library: A Tutorial and Reference (Boston: Addison-Wesley), $\ S 4 . 3 . [ 2 ]$ 1   
Cody, W.J. 1988, “MACHAR: A Subroutine to Dynamically Determine Machine Parameters,” ACM Transactions on Mathematical Software,vol.14, pp. 303-311.[3]   
Malcolm, M.A. 1972, “Algorithms to Reveal Properties of Floating-Point Arithmetic,” Communications of the ACM, vol.15,pp.949-951.[4]   
Numerical Recipes Software 2007, “Code for Machar,” Numerical Recipes Webnote No. 27, at http://www.nr.com/webnotes?27 [5]   
Goldberg, D. 1991, “What Every Computer Scientist Should Know About Floating-Point Arithmetic,” ACM Computing Surveys, vol. 23, pp. 5–48.

# 22.3 Gray Codes

A Gray code is a function $G ( i )$ of the integers $i$ that for each integer $N \geq 0$ is one-to-one for $0 \leq i \leq 2 ^ { N } - 1$ , and that has the following remarkable property: The binary representations of $G ( i )$ and $G ( i + 1 )$ differ in exactly one bit. An example of a Gray code (in fact, the most commonly used one) is the sequence 0000, 0001, 0011, 0010, 0110, 0111, 0101, 0100, 1100, 1101, 1111, 1110, 1010, 1011, 1001, and 1000, for $i = 0 , \ldots , 1 5$ . The algorithm for generating this code is simply to form the bitwise exclusive-or (XOR) of $i$ with $i / 2$ (integer part). Think about how the carries work when you add one to a number in binary, and you will be able to see why this works. You will also see that $G ( i )$ and $G ( i + 1 )$ differ in the bit position of the rightmost zero bit of $i$ (prefixing a leading zero if necessary).

The spelling is “Gray,” not “gray”: The codes are named after one Frank Gray, who first patented the idea for use in shaft encoders. A shaft encoder is a wheel with concentric coded stripes, each of which is “read” by a fixed optical sensor or conducting brush. The idea is to generate a binary code describing the angle of the wheel. The obvious, but wrong, way to build a shaft encoder is to have one stripe (the innermost, say) present on half the wheel, but absent on the other half; the next stripe is present in quadrants 1 and 3; the next stripe is present in octants 1, 3, 5, and 7; and so on. The optical or electrical sensors together then read a direct binary code for the position of the wheel.

The reason this method is bad is that there is no way to guarantee that all the brushes will make or break contact exactly simultaneously as the wheel turns. Going from position 7 (0111) to 8 (1000), one might pass spuriously and transiently through 6 (0110), 14 (1110), and 10 (1010), as the different brushes make or break contact. Use of a Gray code on the encoding stripes guarantees that there is no transient state between 7 (0100 in the sequence above) and 8 (1100).

Of course we then need circuitry, or algorithmics, to translate from $G ( i )$ to $i$ . Figure 22.3.1(b) shows how this is done by a cascade of XOR gates. The idea is that each output bit should be the XOR of all more significant input bits. To do $N$ bits of Gray code inversion requires $N - 1$ steps (or gate delays) in the circuit. (Nevertheless, this is typically very fast in circuitry.) In a register with word-wide binary operations, we don’t have to do $N$ consecutive operations, but only $\ln _ { 2 } N$ . The trick is to use the associativity of XOR and group the operations hierarchically. This involves sequential right-shifts by $1 , 2 , 4 , 8 , \ldots$ bits until the wordlength is exhausted. Here is a piece of code for doing both $G ( i )$ and its inverse: