# ODD-EVEN TRANSPOSITION SORT (ONE-DIMENSIONAL MESH PROCESSOR ARRAY):

Parameter $n$ Global $_ i$ Local $^ { a }$ {Element to be sorted) t {Element taken from adjacent processor] begin for $i \gets 1$ to $n / 2$ do for all $P _ { j }$ ,where $0 ~ \leq ~ j ~ \leq ~ n - 1$ do if $\begin{array} { r l r } { j } & { { } < } & { n - 1 } \end{array}$ and $\mathsf { o d d } ( j )$ then {Odd-even exchange] $\begin{array} { l } { t \iff s u c c e s s o r ( a ) } \\ { s u c c e s s o r ( a ) \iff \mathsf { m a x } ( a , t ) } \\ { a \gets \mathsf { m i n } ( a , t ) } \end{array}$ {Get value from successor] {Give away larger value] {Keep smaller value] endif ifeven $( j )$ then {Even-odd exchange} t←successor(a) {Get value from successor] $s u c c e s s o r ( a ) \ \gets \mathsf { m a x } ( a , t )$ {Give away larger value} $a \gets \mathsf { m i n } ( a , t )$ {Keep smaller value} endif endfor endfor end

FIGURE10-2 Odd-even transposition sort algorithm for the one-dimensional mesh processor array model.

FIGURE 10-3 Odd-even transposition sort of eight values on the one-dimensional mesh processor arraymodel.

Indices: 0 1 2 34 5 6 7 Initial values: GHF DE CB A After odd-even exchange: G $\mathbf { F } < \mathbf { H }$ D<E B <C After even-odd exchange: $\mathbf { F } { < } \mathbf { G }$ D<H B<E A LC After odd-even exchange: F D ${ \bf - G }$ B<H A<E C After even-odd exchange: D ${ < } \mathrm { F }$ $\mathbf { B } < \mathbf { G }$ A<H C <E After odd-even exchange: D $\mathrm { ~ B ~ } { < } \mathrm { F }$ A<G C<H E After even-odd exchange: $\mathbf { B } < \mathbf { D }$ A<F C<G E<H After odd-even exchange: B A ${ < } \mathbf { D }$ C<F E<G H After even-odd exchange: A $\mathrm { < B }$ $\mathbf { C } < \mathbf { D }$ E<F G<H

Proof. The proof is based upon the fact that after $i$ iterations of the outer for loop, no element can be farther than $n - 2 i$ positionsaway from its final, sorted position. Hence $n / 2$ iterations are sufficient to sort the elements, and the time complexity of the parallel algorithm is $\Theta ( n )$ ,given $n$ processing elements.

In Sec.10.2 we derived a lower bound of $\Theta ( n )$ for sorting $n$ elements on the one-dimensional mesh processor array model. Hence odd-even transposition sort is an optimal parallel algorithm for this model.

# 10.4 BITONIC MERGE

In 1968 Batcher introduced a parallel-sorting algorithm with time complexity $\Theta ( \log ^ { 2 } n )$ (Batcher 1968). This algorithm, called bitonic merge, is the basis for polylogarithmic time-sorting algorithms on several models of parallel computation. The fundamental operation is called compare-exchange: two numbers are routed into a comparator,where they are exchanged,if necessary,so that they are in the proper order (Fig. 10-4).

Definition 10.1. A bitonic sequence is a sequence of values $a _ { 0 } , \ldots , a _ { n - 1 }$ ,with the property that (1) there exists an index $i$ ,where $0 \leq i \leq n - 1$ ,such that $a _ { 0 }$ through $a _ { i }$ is monotonically increasing and $a _ { i }$ through $a _ { n - 1 }$ is monotonically decreasing,or (2) there exists a cyclic shift of indices so that the first condition is satisfied.

If you look at a graph of a bitonic sequence, it contains at most one “peak" and one “valley” (see Fig.1O-5). Remember that the sequence “wraps around" from the last element to the first.

![](images/0ef914acfe2be239042ee3d78ba1ceedeb848a46ccd51e42d1d29e07ab9aa97d.jpg)  
FIGURE10-4 Two comparators. (a) Low-to-high comparator. (b) High-to-low comparator.

![](images/5da04219cc90391076cf96d061e4410c2effd6b77b6464dcb68d33c59e548670.jpg)  
FIGURE 10-5The first three sequences are bitonic sequences; the last sequence is not.

A single compare-exchange step can split a single bitonic sequence into two bitonic sequences, as Lemma 10.1 states.

Lemma 10.1. If $_ n$ is even, then $n / 2$ comparators are sufficient to transform a bitonic sequence of $n$ values,

$$
a _ { 0 } , a _ { 1 } , a _ { 2 } , \dotsc , a _ { n - 2 } , a _ { n - 1 }
$$

into two bitonic sequences of $n / 2$ values,

and

$$
\begin{array} { r l } & { \operatorname* { m i n } ( a _ { 0 } , a _ { n / 2 } ) , \operatorname* { m i n } ( a _ { 1 } , a _ { n / 2 + 1 } ) , \dots , \operatorname* { m i n } ( a _ { n / 2 - 1 } , a _ { n - 1 } ) } \\ & { \operatorname* { m a x } ( a _ { 0 } , a _ { n / 2 } ) , \operatorname* { m a x } ( a _ { 1 } , a _ { n / 2 + 1 } ) , \dots , \operatorname* { m a x } ( a _ { n / 2 - 1 } , a _ { n - 1 } ) } \end{array}
$$

such that no value in the first sequence is greater than any value in the second sequence.

Informal proof.Figure 10-6a contains a generic bitonic sequence before it is split in half.By definition,thesequence containsat most one peak and one valley.We will use $n / 2$ comparators to compare every element in the first half of the sequence with the corresponding element in the second half of the sequence. Figure 10-6b shows the two halves overlayed. Figure 1O-6c highlights the first half of the transformed sequence containing the minimum values emitted by the comparators. The sequence is bitonic, because it contains the vally from the original sequence,plus, at most, one newly introduced peak. Figure 1O-6d highlights the second half of the transformed sequence that contains the maximum values emitted by the comparators. The sequence is bitonic, because it contains the peak from the original sequence, plus,at most, one newly introduced valley.Figure 1O-6e illustrates the transformed sequence.

![](images/8a75935f3321f2f9b26847879b6e1910ae33fbec313787ac4f173210f35c1862.jpg)  
FIGURE 10-6 First part of informal proof of Lemma 10.1. (a) Original bitonic sequence. (b) First half of sequence overlayed onsecond half of sequence.(c) Minimum values.(d) Maximum values. (e) Transformed sequence.

We use proof by contradiction to demonstrate that no value in the first half of the final sequence is greater than any value in the second half of the final sequence. If a value in the first half of the final sequence is greater than a value in the second half, then the minimum value returned by one comparator is greater than the maximum valuereturned by another comparator (Fig. 10-7a).However, if this is true, then the original, nonoverlapped sequence would contain two peaks and two valleys (Fig.10-7b). In other words, it would not be bitonic. Hence our initial assumption must be false,and no value in the first half of the final sequence is greater than any value in the second half.

We leave a more formal proof to the reader, as Prob. 10.11.

Given a bitonic sequence, a single compare-exchange step divides the sequence into two bitonic sequences half its length (Fig. 10-8). Applying this step recursively yields a sorted sequence. In other words, given a bitonic sequence of length $n = 2 ^ { k }$ ,where $k > 0$ ,then $k$ compare-exchange steps are sufficient to yielda sorted sequence (Fig. 10-9). Figure 10-10 illustrates in detail how a bitonic sequence of length 16 is sorted in four compare-exchange steps.

Theorem 10.5. A list of $n = 2 ^ { k }$ unsorted elements can be sorted by using a network of $2 ^ { k - 2 } k ( k + 1 )$ comparators in time $\Theta ( \log ^ { 2 } n )$ .(See Batcher 1968.)

Proof. Bitonic merge takes a bitonic sequence and transforms it into a sorted list that can be thought of as half a bitonic sequence of twice the length.If a bitonic sequence of length $2 ^ { m }$ is sorted into ascending order,whileanadjacent sequence of length $2 ^ { m }$ is sorted into descending order, then after $m$ compare-exchange steps the combined

FIGURE 10-7 Second part of informal proof of Lemma 10.1. (a) Suppose the jth element of the first half of the final sequence is greater than the kthelement of thelast half of thefinal sequence.(b) If that is true,the original sequence could notbea bitonic sequence.

![](images/5bddbd6d4ca6a9a7ef4706f9d9ca75b31bff713ace89dd0cb2d9e09e3e22c98d.jpg)

![](images/e374f431e12c5f643d95582f9261e1c3e5774dc727ee99ed0ffdaf090f554ae7.jpg)  
FIGURE 10-9 it intoasorted sequence.inthisexamplesevencompare-exchange stepstransforma bitonic sequence of length 128 intoa sorted sequence of length 128

sequence of length $2 ^ { m + 1 }$ is a bitonic sequence. A list of $_ n$ elements to be sorted can be viewed as a set of $n$ unsorted sequences of length1oras $n / 2$ bitonic sequences of length 2. Hence we can sort any sequence of elements by successively merging larger and larger bitonic sequences. Given $n = 2 ^ { k }$ unsorted elements,a network with $k ( k + 1 ) / 2$ levels suffices.Each level contains $n / 2 = 2 ^ { k - 1 }$ comparators. Hence the total number of comparators is $2 ^ { k - 2 } k ( k + 1 )$ . The parallel execution of each Ievel requires constant time. Note that $k ( k + 1 ) / 2 = \log n ( \log n + 1 ) / 2$ Hence the algorithm has complexity $\Theta ( \log ^ { 2 } n )$ ·

![](images/a0d102290549852dbd5ff757082b6bd671de6a4cf5eaa70376e074ff09d40fc3.jpg)  
FIGURE 10-10 Sorting a bitonic sequence of length 16 by using bitonic merge.

The graphs in Fig. 10-11 illustrate how a series of bitonic merges sorts a list. Each graph represents a list at some stage of the sort. Unsorted elements form a “cloud” (see the first graph). The sorted elements form a diagonal line (see the final graph). The intermediate graphs show the form of the list after each of $\log n$ iterations. In this case $n = 1 2 8$ and $\log n = 7$ Figure 10-9 illustrates what happens on the seventh,and final, iteration. The entire set of $n$ elements has been transformed into a single bitonic sequence,and $\log n$ bitonic merges of shorter and shorter bitonic sequences are enough to complete the sort.

Figure 10-12 shows in detail how a bitonic merge sorts a list of eight elements. The boxes marked with a plus represent comparators that put the smaller value above the larger value. The boxes marked with a minus are comparators that put the larger value above the smaller value.

# 10.4.1 Bitonic Merge on the Shuffle-Exchange Network

Theorem 10.6. A list of $n = 2 ^ { k }$ unsorted elements can be sorted in time $\Theta ( \log ^ { 2 } n )$ with a network of $2 ^ { k - 1 } \binom { k ( k - 1 ) + 1 } { \cdot }$ comparators using the shuffle-exchange interconnection scheme exclusively. (See Stone 1971.)

![](images/d0803293aea01d0364b29848073ffb8718c85553a53495e11e52ec19d4b93d57.jpg)  
FIGURE 10-11 Iterations of bitonic mergesort. The list has 128 elements； hence the sort requires log128=7iterations.Iterationi hasi compare-exchange steps,for1≤i≤7.

![](images/9f35bcad37d8c311c4528b1dd29f8db9f28807eb0ef0f1c28ad486ff15b4d4c9.jpg)  
FIGURE10-12 Bitonic merge-sort of an unsorted list of eight elements.

Stone realized that Batcher's bitonic sorter always compares elements with indices that differ by exactly one bit in their binary representations.Recall that the perfect shuffe routes the element at position $i$ to the position found,by cyclically rotating the binary representation of $i$ one bit to the left. Hence two indices with binary representations differing by exactly one bit can be routed to the same comparator by performing a suitable number of shuffles. Figure 10-13 shows how bitonic merge can be implemented by using the shufe-exchange interconnectionscheme exclusively.Contrast this figure withFig.1O-1O,where the connections between comparators vary from stage to stage. An entire sort can be accomplished with the shuffle-exchange interconnection. A sort of eight elements appears in Fig.10-14.Both algorithms require $k$ bitonic merges to sort 2k elements,but while the ith merge of Batcher’s algorithm requires i steps, for a total of $k ( k + 1 ) / 2$ steps,the second through kth iterations of Stone's algorithm require $k$ steps, for a total of $k ( k - 1 ) + 1$ steps. For a sort of eight elements thereis one extra step in iteration2,corresponding to the vertical tier of blank boxes in Fig. 10-14. The blank boxes do not perform a compareexchange operation; they output the values in the same order as they were input. These boxes are used when a number of shuffles are required before the elements to be compared are routed into the same comparator. Note that since the connections between the comparators are the same from step to step,only a single tier of comparators is required (see Fig.10-15).

![](images/2e2ee971213857402514da92143f8a51befe6322bf7f1a1ac0445b8a62267a38.jpg)  
FIGURE 10-13 Sorting a bitonic sequence of length 16 by using Stone's perfect shuffle.

A parallel algorithm implementing Batcher's bitonic merge-sort algorithm on the shuffle-exchange processor array model appears in Fig. 10-16. The only tricky part of the algorithm is determining if a pair of elements being compared should be be sorted low to high or high to Iow. Stone’salgorithm uses a mask vector M to indicate the kind of sort to be done by a particular processing element. A value of O corresponds to a plus comparator; a value of 1 corresponds to a minus comparator.

![](images/09a65a1aef3db360d66cce49640503f2435ee7fa950c56e4cf92f9a359a25c35.jpg)

FIGURE 10-14 Bitonicmerge-sort ofanunsortedlistofeight elements,byusing Stone'sperfectshuffle interconnection.

![](images/0b6491f0a28f537324295ae02cc7e66d670de7e0d88ccd10fb12ba1ea934a610.jpg)  
FIGURE 10-15 Sorting machine based upon perfect shuffle connection (Sedgewick 1983).

This algorithm requires $\log n ( \log n + 1 ) / 2$ compare-exchange steps, $\log n ( \log n - 1 )$ shuffle steps of the vector $\mathbf { A }$ ,and $2 \log n - 1$ shuffles of the vectors $\mathbf { M }$ and R. The time complexity of this algorithm is $\Theta ( \log ^ { 2 } n )$ with $n$ processors.

# 10.4.2 Bitonic Merge on the Two-Dimensional Mesh Network

Theorem 10.7. An algorithm exists to sort $n = m ^ { 2 } = 2 ^ { k }$ elements on the twodimensional mesh processor array model in time $\Theta ( { \sqrt { n } } )$ . (See Thompson and Kung 1977.)

Parameter n {Size of array} Global $j , k$ Local $^ { a }$ {Element to be sorted) $m$ {Mask bit that indicates kind of comparison to perform) $r$ {Bit used to compute mask bit} begin {Compute initial value of the mask $M$ } for all $P _ { i }$ where $0 ~ \leq ~ i ~ \leq ~ n - 1$ do $r \gets i$ modulo 2 $m \gets r$ endfor for $k \gets 1$ to log $n$ do for all $P _ { i }$ where $0 ~ \leq ~ i ~ \leq ~ n - 1$ do $m  m \oplus r$ {Exclusive OR} $s h u f f l e ( m ) \ \Leftarrow \ m$ endfor endfor {Now do the sort} COMPARE-EXCHANGE $( a , m )$ for $k \gets 1$ to log $n \mathrm { ~ - ~ } 1$ do forall $P _ { i }$ where $0 ~ \leq ~ i ~ \leq ~ n - 1$ do shuffle ${ \bf \Xi } ( r ) \Leftarrow { r }$ $m  m \oplus r$ {Exclusive OR} for $j \gets 1$ tolog $\textit { n } - k - 1$ do shuffle(a)a $s h u f f l e ( m ) \ \Leftarrow \ m$ endfor endfor for $j  \log n - k$ to log $n$ do for all $P _ { i }$ where $0 \leq \ i \ \leq \ n - 1$ do shuffl $e ( a ) \ \Leftarrow \ a$ shuffle(m)m endfor COMPARE-EXCHANGE $( a , m )$ endfor endfor end

FIGURE 10-16 Implementation of bitonic merge-sort algorithm on the shuffle-exchange SIMD model.

Reference $^ { a }$ {Element of list to be sorted) $m$ {Mask bit indicating sort order} $t$ {Value retrieved from successor processor element begin for all $P _ { i }$ where $0 ~ \leq ~ i ~ \leq ~ n - 1$ do if even(i) then $t $ exchange(a) if $\textbf { \textit { m } } = \textbf { 0 }$ then {Sort low to high} exchange(a) $\Leftarrow \boldsymbol { \mathsf { m a x } } ( a , t )$ $a \gets \mathsf { m i n } ( a , \ t )$ else {Sort high to low) $e x c h a n g e ( a ) \ \Leftarrow { \mathsf { m i n } } ( a , t )$ $a \gets \mathsf { m a x } ( a , \ t )$ endif endif endfor end

Summary The algorithm is an adaptation of Batcher's bitonic merge to the mesh. Given n = 2k elements,bitonic merge-sort consists of k iterations,where each iteration i has i compare-exchange steps. Each compare-exchange requires two data routings: thefirst routing brings together theelements to becompared,and the second routing redistributes them. Figure 10-18 illustratesa network based on bitonic merge that sorts 16 elements (Knuth 1973). Each row represents the position of an element.

![](images/e258df72d156d15a307eba26ed82a474ac992bffdf90562953a664bc1d0c5b09.jpg)  
FIGURE 10-17 Compare-exchange routine called by bitonic merge sort algorithm for shufle-exchange processorarray. The even-numbered processing elementsassume the role of comparators.

Arrows represent compare-exchanges.To perform a compare-exchange, the element at the position marked by the tail of the arrow is routed to the position marked by the arrowhead.After the two elements are compared, the smaller is routed back to the tail position.

Note that elements in positions that differ in their least significant bit are compared every iteration,while elements in positions that differ in their most significant bit are compared only on the last iteration. An eficient implementation of bitonic merge on the two-dimensional mesh processor array model must have the property that, if bit $i$ is less significant than bit $j$ ,a compare-exchange on bit i cannot require more data routings than a compare-exchange on bit $j$ .One way to satisfy this condition is to use a “shuffed row-major”addressing scheme,illustrated fora $4 \times 4$ mesh in Fig.10-19a. The advantage of this scheme is that “shufling” operations occur on square subsections of the mesh, reducing the number of routing operations.

The direction of routing necessary at each compare-exchange step depends upon the index of the particular processor.Figure 10-20 ilustrates the bitonic merge sort of 16 elements on a $4 \times 4$ mesh.In general,toot $n = m ^ { 2 } = 2 ^ { k }$ elements by using this algorithm requires $\log n$ phases. The total number of routing steps performed is

$$
\sum _ { i = 1 } ^ { \log n } \sum _ { j = 1 } ^ { i } 2 ^ { \lfloor ( j - 1 ) / 2 \rfloor }
$$

which is $\Theta ( { \sqrt { n } } )$ .The total number of comparison steps is

$$
\sum _ { i = 1 } ^ { \log n } i
$$

which is @(log² n). Thus the worst-case time complexity of bitonic merge on the twodimensional mesh processor array model is $\Theta ( { \sqrt { n } } )$ ,making itanoptimalalgorithm for this model.

The function mapping that lists elements into the mesh-connected network is the index function. The bitonic merge algorithm sorts the list based on the

FIGURE 10-19 Threeindex functionsmapinglist elements intoa two-dimensional mesh.(a)Shuffled row-major order.(b) Row-major order. (c) Snakelike row-major order.

![](images/93f2848cc42b1f25e4f2ecd0a346a8f5003557c4ac26b8b1c05ceb972da79028.jpg)

![](images/ef48e3d77a951486822fc2ce7969537c1a8cbcfc9cfbd9f079dc7ab158bff5b6.jpg)  
Stage3

百百 器 shuffled-row order.What if the sorted list mustbe arranged in the mesh in row order (Fig. 10-19b) or snakelike order (Fig.10-19c)? Theorem 10.8 shows that if each processing element has enough memorythe sorted list can be quickly rearranged to the desired order.

![](images/7e8a5fc60ff7b9fa0777bf15431134db454f653dcb7370c0e8daae922dbb8999.jpg)  
Stage 4   
FIGURE 10-20 Sorting values into shuffled row-major order on the two-dimensional mesh processor arraymodel.(TompsonandKung(1977).Copyght $\circledcirc$ 1986AssociationforComputing Machinery.Reprintedbypermission.)

Theorem 10.8. If $n = m ^ { 2 }$ elements have already been sorted with respect to some index function, and if each processing element can store $m$ elements,then the $n$ elements can be sorted with respect to any other index function in $\Theta ( { \sqrt { n } } )$ time. (See Thompson and Kung [1977].)

# 10.4.3 Bitonic Merge on the Hypercube Network

Bitonic merge always compares elements whose indices differ in exactly one bit. Since processors in the hypercube processor array model are connected if their indices differ inexactly one bit, it is easy to implement bitonic merge on this model. Processors replace comparators. Instead of routing pairs of elements to comparators, processors route data to adjacent processors, where the elements

Global $d$ {Distance between elements being compared) Local $^ a$ {One of the elements to be sorted} $t$ {Element retrieved from adjacent processor) begin for $i \gets 0$ to $m - 1$ do for $j \gets i$ downto 0 do $d \gets 2 ^ { j }$ for all $P _ { k }$ where $0 ~ \leq ~ k ~ \leq ~ 2 ^ { m } - 1$ do if $k$ mod $2 d \ < \ d$ then $t ~ \Leftarrow ~ [ k + d ] a$ {Get value from adjacent processor] if $k$ mod $2 ^ { i + 2 } ~ < ~ 2 ^ { i + 1 }$ then $[ k + d ] a \ \Leftarrow \mathsf { m a x } \ ( t , \ a )$ {Sort low to high..} $\alpha \ \gets \mathsf { m i n } \ ( t , \ a )$ else $[ k + d ] a \Leftarrow \mathsf { m i n } ~ ( t , ~ a )$ {..or sort high to low} a←max $( t , \ a )$ endif endif endfor endfor endfor end

are compared. Assume $n$ elements are to be sorted, where $n = 2 ^ { m }$ for some positive integer $m$ . The parallel algorithm appears in Fig. 10-21.

Clearly the complexity of the parallel for allstatement is $\Theta ( 1 )$ .Hence the complexity of this parallel algorithm is $\Theta ( m ^ { 2 } ) = \Theta ( \log ^ { 2 } n )$ ，given $n = 2 ^ { m }$ processors.

# 10.5 QUICKSORT-BASED ALGORITHMS

In Sec. 10.5 we will develop three parallel-sorting algorithms suitable for implementation on MIMD computers. Developing parallel algorithms is easiest when a cost optimal PRAM algorithm exists, in which the processor interactions match the underlying architecture. Unfortunately,we do not have that luxury when it comes to sorting. The cost-optimal PRAM-sorting algorithm of Leighton has time complexity $\Theta ( \log n )$ with $n$ processing eementsutits enormous constant of proportionality makes it impractical to use (Leighton 1984). Bitonic merge-sort has cost @(n log² n), which is higher than the cost of the best sequential-sorting algorithms. For this reason we turn to the best general-purpose sequential sorting algorithm-quicksortas the basis for our parallel algorithms.

Quicksort is a sorting algorithm commonly used on serial computers. Its popularity is due to its asymptotically optimal average-case behavior of O(n log n) (Baase 1978).

Quicksort is a recursive algorithm that repeatedly divides an unsorted sublist into two smaller sublists and a supposed median value. One of the smaller sublists contains values less than or equal to the median value; the other sublist contains values greater than the median. The median value, located between the two smaller sublists, is in its correctly sorted position, since all the values to the left are less than or equal to the median value,and all the values to the right are greater than the median value. Given an initially unsorted list, then, the quicksort algorithm chooses one element as the supposed median (e.g.,the first element).After a single partitioning step, the list is divided into two sublists, and the algorithm recursively partitions each of the sublists. Quicksort is an example of an algorithm that uses the divide-and-conquer approach. Once a list has been partitioned, the two unsorted sublists form independent problems that can be solved simultaneously.

Consider the following parallel quicksort algorithm. A number of identical processes,one per processor,execute the parallel algorithm. The elements to be sorted are stored in an array in global memory. A stack in global memory stores the indices of subarrays that are still unsorted. When a process is without work, it atempts to pop the indices for an unsorted subarray off the global stack. If it is successful,theprocessorprtiionsthesbarayedonaupposedan element, into two smaller arrays, containing elements less than or equal to the supposed median value or greater than the supposed median value, respectively. After the partitioning step,identical to the partitioning step performed by the serial quicksort algorithm,the process pushes the indices for one subarray onto the global stack of unsorted subarrays and repeats the partitioning process on the other subarray.Figure 10-22 illustrates this parallel algorithm.

What speedup can be expected from this parallel quicksort algorithm? Note that it takes $k - 1$ comparisons to partition a subarray containing $k$ elements.The expected speedup is computed by assuming that one comparison takes one unit of time and finds the ratio of the expected number of comparisons performed by the sequential algorithm to the expected time required by the parallel algorithm. To simplify the analysis,assume that $n = 2 ^ { k } - 1$ and $p = 2 ^ { m }$ ,where $m \textless k$ Also assume that the supposed median is always the true median, so that each partitioning step always divides an unsorted subarray into two subarrays of equal size.

With these assumptions the number of comparisons made by the sequential algorithm can be determined by solving the following recurrence relation:

$$
T ( n ) = { \left\{ \begin{array} { l l } { n - 1 + 2 T ( ( n - 1 ) / 2 ) { \mathrm { ~ f o r ~ } } n = 7 , 1 5 , 3 1 , \ldots } \\ { 2 } & { { \mathrm { f o r ~ } } n = 3 } \end{array} \right. }
$$

![](images/48e01db1a48d4a2d34852b2aa8f6078f8fc077974e500a0038c7df5572b2a36b.jpg)  
Step 2: Partition

![](images/85fede139bca35ed9c0f265d78ac7dbca738c02e483c3c1b619057a71a9eae65.jpg)

FIGURE 10-22 llustration of a parallel quicksort algorithm for UMA multiprocessors. A process fetches the indices of an unsorted subarray from a shared stack of index pairs.The process uses the quicksort partitioning step to divide the interval into two subintervalsand a median. The process puts the indices of one unsorted subinterval back on the stack and keeps theother indexpair,repeating the partitioning step.

![](images/9949646db2a781b54686eece5ced1828ae6a5e59b88ada990180461785a53d31.jpg)

# FIGURE 10-23

A view of the beginning of parallel quicksort,when the the number of unsorted intervais is less than or equal to the number of processes.The analysis assumes $n = 2 ^ { k } - 1$ and everypartitioning step dividesan interval exactly in half.

The solution to this recurrence relation is

$$
T ( n ) = ( n + 1 ) \log ( n + 1 ) - 2 n
$$

The parallel algorithm has two phases.First, there are more proceses to be sorted than arrays (see Fig. 10-23). For example, when the algorithm begins execution there is only a single unsorted array.All but one of the processes must wait whileasingleprocess partitions thatarray.This iteration,then,requires $n { - } 1$ time units to perform $n { - } 1$ comparisons.If we assume $p \ge 2$ ,two processes can partition the two resulting subarrays in $( n - 1 ) / 2 - 1 = ( n - 3 ) / 2$ time units, performing $n - 3$ comparisons. Similarly,if $p \geq 4$ ,the third iteration requires time at least $[ ( n - 1 ) / 2 - 1 ] / 2 - 1 = ( n - 7 ) / 4$ to perform $n - 7$ comparisons. For the first log p iterations, there are at least as many processes as partitions, and the time required by this phase of the parallel quicksort algorithm is

$$
T _ { 1 } ( n , p ) = 2 ( n + 1 ) ( 1 - 1 / p ) - \log p
$$

The number of comparisons performed is

$$
C _ { 1 } ( n , p ) = ( n + 1 ) \log p - 2 ( p - 1 )
$$

In the second phase of the parallel algorithm there are more subarrays to be sorted-than processes. All the processes are active. If we assume that every process performs an equal share of the comparisons, then the time required is simply the number of comparisons performed divided by p. Hence

$$
\begin{array} { l } { { C _ { 2 } ( n , p ) = T ( n ) - C _ { 1 } ( n , p ) } } \\ { { \ } } \\ { { T _ { 2 } ( n , p ) = { \frac { C _ { 2 } ( n , p ) } { p } } } } \end{array}
$$

The estimated speedup achievable by the parallel quicksort algorithm is the sequential timedividedby the paralel time:

$$
{ \mathrm { S p e e d u p } } = { \frac { T ( n ) } { T _ { 1 } ( n , p ) + T _ { 2 } ( n , p ) } }
$$

For example, the best speedup we could expect with n = 65,535 and p = 16 is approximately 5.6. Why is speedup so low? The problem with quicksort is its divide-and-conquer nature. Until the first subarray is partitioned, there are no more partitionings to do. Even after the first partitioning step is complete, there are only two subarrays to work with. Hence many processes are idle at the beginning of the parallel algorithm’s execution, waiting for work.

Figure 10-24 contains pseudocode for a UMA multiprocessor-oriented paralel quicksortalgorithm,hichusestherategywehavedscussed.uction INITIALIZE.STACK initializes the shared stack containing the indices of unsorted subarrays. When a process calls function STACK.DELETE, it receives the indices of an unsorted subarray if the stack contains indices; otherwise, the “low” index is greater than the “high” index, meaning there is no useful work to do at this point. Function STACK.INSERT adds the indices of an unsorted subarray tothe stack. Since all these functions access the same shared data structure, their execution must be mutually exclusive. Function ADD.TO.SORTED increases the count of elements that are in their correct positions and execution of this function,too,must be mutually exclusive. We use monitors to implement these functions.

As the pseudocode algorithm shows, we use the familiar strategy of switching from quicksort to insertion sort when the size of the array tobe partitioned falls below a predetermined threshold (Sedgewick 1988).

Figure 10-25 compares the predicted speedup with the actual speedup achieved by a Sequent C implementation of the algorithm sorting 65,535 integers on a lightly loaded Symmetry multiprocessor. The correlation is reasonably good,considering theanalysismade the simplifying assumption that each partitioning step always divides an unsorted subarray into two subarrays of equal size.

Global n {Size of array of unsorted elements] $a [ 0 . . . ( n - 1 ) ]$ {Array of elements to be sorted} sorted {Number of elements in sorted position} min.partition {Smallest subarray that is partitioned rather than sorted directly) Local bounds {Indices of unsorted subarray} median {Final position in subarray of partitioning key} begin sorted $ \ 0$ INITIALIZE.STACK() for all $P _ { i }$ ,where $0 ~ \leq ~ i ~ < ~ p$ do while (sorted $< n )$ do bounds STACK.DELETE() while (bounds.low $<$ bounds.high) do if (bounds.high-bounds.low $<$ min.partition) then INSERTIO.T (aunds.lowu) ADD.TO.SORTED (bounds.high- bounds.low + 1) exit while else median PARTITION (bounds.low, bounds.high) STACK.INSERT (median $+ 1$ ,bounds.high) bounds.high median-1 if bounds.low $=$ bounds.high then ADD.TO.SORTED (2) else ADD.TO.SORTED (1) endif endif endwhile endwhile endfor end Multiprocessor-oriented paralelquicksort algorithm.A shared stack contains the indicesofunsortedsubarrays.ProcessesmustexecutefunctionsSTACK.DELETE( ADD.TO.SORTED()，and STACK.INSERT() inside critical sections to ensure mutual exclusion.

# 10.5.2 Hyperquicksort

We have seen that the speedup achieved through the parallel quicksort algorithm is constrained by the time taken to perform the initial partitioning steps,when notall processors areacive.A numberof paralealgorithms have been developed to put all processors to work immediately. Here we describe one such algorithm,hyperquicksort, suitable for implementation on hypercube multicomputers.

![](images/5a37394642e67d2abea31e4c6c043b602ab13a7dcabea25debb0933b7a8dc9f2.jpg)  
FIGURE 10-25 Predicted speedup (dashed line) and actual speedup (solid line) of parallel quicksortalgorithm.Actual speedup datacollected onalightly loaded 20- processorSequentSymmetryrunning the PTX operating system.

Given a list of values initially distributed evenly among the processors of a multicomputer, we define the list to be sorted when (1) every processor's list of values is sorted,and (2) the value of the last element on Pi’s list is less than or equal to the value of the first element on Pi+1’s list,forO ≤i ≤p-2.Note that the sorted values need not be distributed evenly among the processors.

To developanefficient algorithm,we apply the strategyof letting each processor solve a subproblem using the most eficient sequential algorithm, then using a communication-efficient parallel algorithm to generate the final solution from the partial solutions.

In the first phase of hyperquicksort each processor uses quicksort to sort its local Iist of values. At this point every processor has a sorted list of values,satisfying condition (1) of the sortedness requirement, but not condition (2). Hyperquicksort is a recursive algorithm that uses a divide-and-conquer approach to fulfill the second condition. During each step of the second phase of the algorithm,a hypercube is split into two subcubes.Each processor sends values to its partner in the other subcube, then each processor merges the values it keeps with the values it receives.The effect of this split-and-merge operation is to divide a hypercube of sorted values into two hypercubes so that each processor has a sorted list of values,and the largest value in the lower hypercube is less than the smallest value in the upper hypercube. After $d$ such split-and-merge steps,the original $2 ^ { d }$ processor hypercube has been divided into $2 ^ { d }$ single-processorhercbsadonditio2)isifed.heis illustrated in Fig. 10-26.

The split-and-merge step divides a $d$ -dimensional hypercube into two hy\~ percubes of dimension $d - 1$ .Recall that each processor's values are sorted. A designated processor in the $d$ -dimensional hypercube broadcasts itsmedian value to the $2 ^ { d } - 1$ other processors in the hypercube. Every processor uses this splitter value to divide its list into two portions: those less than or equal to the spliter and those greater than the splitter. Every processor $P _ { i }$ in the lower half of the hypercube sends the upper portion of its sorted list--those values greater thanthespliter-toitspartner intheupper half,processor $P _ { i } \otimes 2 ^ { d - 1 }$ (where $\otimes$ denotes the bit-wise "exclusive or"operation). Every processor $P _ { i }$ in the upper half of the hypercube sends the lower portion of its sorted list-those values less than or equal to the splittr-to its partner in the lower half, processor $P _ { i } \otimes 2 ^ { d - 1 }$ Each processr merges thelistitreceives withthelistiteeps to form a new sorted list. Here, all values less than or equal to the splitter are in lower (d -1)-dimensional hypercube, and all values greater than the splitter are in the upper (d -1)-dimensional hypercube. Figure 10-27 presents the hyperquicksort algorithm in pseudocode.

![](images/215363ca7a51543394036f11de03ab908c2caf6f6fd69149be95f47c6e5f43d6.jpg)  
llustration of the hyperquicksort algorithm.In this example 32 elements are being sortedonatwoimesioalercube.(a)itiallyachpocessorightets. (b)Eachprocessorperforms sequential quicksort onitsownlist.ProcessorObroadcasts itsmedianvlue48totheotherprocessors.(c)Processorsinthelowerhlfofthe hypercube send values greater than 48 to processors intheupper half of the hypercube. Theprocessors in the upper half send values lessthan orequal to48.(d) Each processor merges the elements it kept with the elements it received.Processor O broadcasts its median vauetoprocessor1andprocessor2broadcastsitsmedianvaluetoprocessor 3.(e)Processorsswapvaluesacrossanother hypercubedimension.(f) Each processor merges the elements it kept with the elements it received.At this point the list is sorted.

# HYPERQUICKSORT (HYPERCUBE MULTICOMPUTER):

Global n {Initial number of elements per processor] d {Dimension of hypercube] i {Dimension number of current hypercube} Local logical.num {Unique processor number] partner {Processor's partner in the exchange} root {Root processor of current hypercube] splitter {Median of root processor's sorted list} begin for all $P _ { j }$ ,where $0 ~ \le ~ j ~ < ~ 2 ^ { d }$ do Sort n values using sequential quicksort algorithm if $d \ > \ 0$ then for $i \gets d$ downto 1 do root ← root of the binary i-cube containing processor logical num if logical.nun $n = r o o t$ then splitter medianof the sorted listheld byprocessor logicalnum endif Processor root broadcasts splitter to other processors in binary i-cube Use splitter topartitionsorted values intolowlist,high list partner logical_num $\otimes 2 ^ { ( i - 1 ) }$ { Bitwise exclusive “or” } if logical.num $>$ partner then Send low list to processor partner Receive another high list from processor partner else {logical.num $<$ partner} Send high list to processor partner Receive another low list from processor partner endif Merge two lists intoa single sorted listof values endfor endif endfor end Pseudocode version of hyperquicksort algorithm.

Suppose at the start of the algorithm each processor has $n$ values. The expected time complexity of the initial quicksort step is $\Theta ( n \log n )$ .Assuming that each processor keeps $n / 2$ values and transmits $n / 2$ values in every splitand-merge step,the expected number of comparisons needed to merge the two lists into a single ordered list is $\Theta ( n )$ . Since the split-and-merge operation is executed for hypercubes of dimension $d , d - 1 , \dotsc , 1$ ,the expected number of comparisons performed over the split-and-merge phase of the algorithm is $\Theta ( n d )$ ,and the expected number of comparisons performed during the entire algorithm is $\Theta ( n ( \log n + d ) )$ ·

Let $\lambda$ denote message Iatency and $\beta$ denote the the time needed to transmit a value from one processor to an adjacent processor. Given a $d$ -dimensional cube, broadcasting the splitter value requires communication time $d ( \lambda + \beta )$

Assuming each processor passes half its values, the time needed to send $n / 2$ sorted values and receive $n / 2$ sorted values from the partner processor is $2 \lambda + n \beta$ . The expected communication time for the split-and-merge phase is $\textstyle \sum _ { i = 1 } ^ { d } ( i ( \lambda + \beta ) + 2 \lambda + n \beta ) = d ( d + 1 ) ( \lambda + \beta ) / 2 + d ( 2 \lambda + n \beta )$ Since the original quicksort phase requires no interprocessor communications, this value is the expected communication time of the entire hyperquicksort algorithm.

If we know the computation speed, message initiation time, and communication speed of a particular hypercube architecture,we can use this analysis to predict the speedup achievable by the hyperquicksort algorithm. For example, sequential quicksort implemented in C on the NCUBE 3200 requires about 12.2 microseconds per comparison, while $\lambda = 5 0 0$ microseconds and $\beta = 1 1$ microseconds (Quinn 1989).

Figure 10-28 compares the predicted and actual speedup of the hyperquicksort algorithm sorting 16,384 integers on an nCUBE 3200 hypercube multicomputer (Quinn 1989). The predicted speedup is somewhat optimistic. Because the median of a single processor's list is almost certainly not the median of the entire set of values, it is likely that, at the end of the hyperquicksort algorithm, some processors will contain more values than others. This uneven distribution affects the execution time, because processors with more values must spend more time merging. It also afects the communication complexity, because communication time is a function of message length.

One way to make the final distribution of values more balanced is to modify the step that selects the splitter. Rather than let a single processor choose its

![](images/a4eb38f288c00a3bb973237aa931c137fb94ba6c0c70620089701c7f7b69f0f0.jpg)

FIGURE 10-28 Predicted speedup (dashed line)and actual speedup (solid line) of hyperquicksort algorithm sorting 16,384 integers onan nCUBE 3200 hypercube multicomputer (Quinn 1989).

median to be the splitter for a d-dimensional hypercube,calculate the spliter as the mean of all 2d processors’ median values. Implementing this modification means introducing a fan-in step before the broadcast step every time the split-and-merge is performed, doubling the communication time. We call this algorithm modified hyperquicksort.

Quinn (1989) implemented the modified hyperquicksort algorithm and discovered that for lists of this size, hyperquicksort slightly outperforms modified hyperquicksort. The modified hyperquicksort algorithm does a better job balancing the number of elements managed by each processor,reducing the variance in the time the processors spend merging their lists. However, this time savings is wiped out by the increase in time spent passing messages to compute the new splitter value.

# 10.5.3 Paralel Sorting by Regular Sampling

The following algorithm, developed by Li et al. (1992), has been shown effective for a wide variety of MIMD architectures. Li et al. call their algorithm "parallel sorting by regular sampling;” henceforth we shall refer to it as the PSRS algorithm.

The PSRS algorithm has four phases (Fig. 10-29). Assume the list has $n$ elements. In phase one each of the $p$ processors uses the sequential quicksort algorithm to sort a contiguous set of no more than $\lceil n / p \rceil$ elements.The $n$ elements now form $p$ independent lists of size no more than $\lceil n / p \rceil$ .Each procesor selectsdata itemsat local indices 1, $( n / p ^ { 2 } ) + 1$ $( 2 n / p ^ { 2 } ) + 1$ ，.., $( p - 1 ) ( n / p ^ { 2 } ) + 1$ as a regular sample of its locally sorted block.

In the second phase of the algorithm one processor gathers and sorts the local regular samples. It selects $p - 1$ pivot values from the sorted list of regular samples. The pivot values are at indices $p + \lfloor p / 2 \rfloor$ ， $2 p + \lfloor p / 2 \rfloor$ ， ， $( p - 1 ) p + \lfloor p / 2 \rfloor$ in the sorted list of regular samples. At this point each processor partitions its sorted sublist into $p$ disjoint pieces, using the pivot values as separators between the pieces.

In the third phase of the algorithm each processor $_ i$ keeps its ith partition and assigns the $j$ th partition to processor $j$ .In other words,each processor keeps one partition and reassigns $p - 1$ other partitions to other processors.

During the fourth phase of the algorithm each processor merges its $p$ partitions intoa single list. The values on this list are disjoint from the values on the lists of the other processors. The concatenation of the processor's individual lists forms the final sorted list.

To simplify the following analysis of the PSRS algorithm, we assume that $p$ processors sort $n$ distinct elements, where $p$ is even, $n = p ^ { 2 } k$ and $k$ isa positive integer. For a more rigorous analysis,see Li et al. (1992).

Definition 10.2. Let $X = \{ X _ { 1 } , \ldots , X _ { n } \}$ denote the list of $n$ elements to be sorted.

![](images/86594fafbb6f64948e3ad879e3b94d17e8b00337e9ad7c31ce298871d190bd4a.jpg)  
This example ilustrates how three processors would sort 27 elements using the PSRS algorithm. (a) Original unsorted list of 27 elements. (b) Each processor sorts its share of thelist (nine elements) using sequential quicksort algorithm. (c) Select regular samples from eachsorted subist (firstfourthand seventh elements).One processororts these elements using sequential quicksort. Choose pivot elements (fourth and seventh elements).(d) Use pivots computed instep (c) to divide each sorted sublist into three parts.(e) Copy sorted sublists into new array so that elements having the same relation to the pivots are placed together.(f) Each processor merges its sorted sublists.

Definition 10.3. Let $Y = \{ Y _ { 1 } , Y _ { 2 } , \dots , Y _ { p ^ { 2 } } \}$ denote the sorted set of $p ^ { 2 }$ regular samples selected from the $p$ sorted sublists of $X$

Definition 10.4. Let $N ( c o n d )$ denote the number of elements of $X$ which satisfy a certain boolean condition cond.

For example, $N ( \leq Y _ { 2 } )$ is the number of elements of $X$ less than or equal to $Y _ { 2 }$ ,the second regular sample selected from the sorted sublists of $X$

First we establish a lower bound on the number of elements in X less than or equal to certain elements of the sample set $Y$

Lemma 10.2. For $1 \leq i \leq p$

$$
\begin{array} { r } { N ( \le Y _ { ( i - 1 ) p + p / 2 } ) \ge \left\{ \begin{array} { l l } { \frac { p } { 2 } , } & { \mathrm { i f ~ } i = 1 } \\ { \frac { n } { p ^ { 2 } } ( ( i - 1 ) p - \frac { p } { 2 } ) + p , } & { \mathrm { i f ~ } i > 1 } \end{array} \right. } \end{array}
$$

Proof.When i=1, Y(i-1)p+p/2 is Yp/2. Since the elementsof Yare sorted, thereare p/2 elements of Y less than or equal to Yp/2. The elements of Y are selected from X. Hence there are at least p/2 elements of X less than or equal to Yn/.

Each element of Y represents a set of n/p² elements of X with equal or greater value.When i >1,the sum (i-1)p+ p/2 is greater than p. This means that when we consider the samples Y1, Y2,.., Y(i-1)p+p/2, some samples must have come from the same processor. If Yj and Yk are from the same processor and j < k,then all of the n/p² elements of X represented by Yj must be less than or equal to Yk. This in turn is less than or equal to Y(i-1)p+p/2. For the p samples representing the largest elements of Y associated with each processor,we only know that the samples themselves are less than or equal to Y(i-1)p+/2. Hence the number of elements of X less than or equal to elements of $Y$ is

$$
\begin{array} { l } { { N ( \leq Y _ { ( i - 1 ) p + p / 2 } ) = \displaystyle \frac { n } { p ^ { 2 } } ( ( i - 1 ) p + \displaystyle \frac { p } { 2 } - p ) + ( 1 ) p \hfill } } \\ { { \hfill } } \\ { { = \displaystyle \frac { n } { p ^ { 2 } } \left( ( i - 1 ) p - \displaystyle \frac { p } { 2 } \right) + p } } \end{array}
$$

Now we determine an upper bound on the number of elements of $X$ greater than certain elements of the sample set $Y$

Lemma 10.3. For $1 \leq i \leq p$

$$
N ( > Y _ { i p + p / 2 } ) \geq \frac { n } { p ^ { 2 } } ( ( p - i ) p - \frac { p } { 2 } + 1 ) - 1
$$

Proof. There are p²-(ip+p/2) = (p-i)p-p/2 samples greater than Yip+p/2. That means the $( n / p ^ { 2 } ) ( ( p - i ) p - p / 2 )$ elements of $X$ associated with these samples are all greater than Yip+p/2.Then/p2-1elementsofX immediately followingYipp2 are also greater than $Y _ { i p + p / 2 }$ .Hence

$$
\begin{array} { l } { { N ( > Y _ { i p + p / 2 } ) \geq \displaystyle \frac { n } { p ^ { 2 } } ( ( p - i ) p - \displaystyle \frac { p } { 2 } ) + ( \displaystyle \frac { n } { p ^ { 2 } } - 1 ) } } \\ { { \qquad \geq \displaystyle \frac { n } { p ^ { 2 } } ( ( p - i ) p - \displaystyle \frac { p } { 2 } + 1 ) - 1 } } \end{array}
$$

Definition 10.5. Let $\Phi _ { i }$ denote the number of $X$ elements merged by processor $i$ in phase four of the PSRS algorithm.

Theorem 10.9. An upper bound on $\operatorname* { m a x } _ { 1 \leq i \leq p } \Phi _ { i }$ is $2 n / p - n / p ^ { 2 } - p + 1$

Proof. We begin by deriving upper bounds for $\Phi _ { i }$ for each of the three cases $i = 1$ ， $i = p$ ,and $1 < i < p$

Case 1: $i = 1$

All the X elements merged by procesor 1 must be less than or equal to Yp+p/2. By Lemma 10.3we know that

$$
N ( > Y _ { p + p / 2 } ) \geq { \frac { n } { p ^ { 2 } } } ( ( p - 1 ) p - { \frac { p } { 2 } } + 1 ) - 1
$$

Hence

$$
\begin{array} { l } { \displaystyle \Phi _ { 1 } = N ( \le Y _ { p + p / 2 } ) \le n - \frac { n } { p ^ { 2 } } ( ( p - 1 ) p - \frac { p } { 2 } + 1 ) - 1 } \\ { \displaystyle \Phi _ { 2 } = \frac { n } { p ^ { 2 } } ( p + \frac { p } { 2 } - 1 ) + 1 } \end{array}
$$

Case 2: $i = p$

All the $X$ elements merged by processor $p$ must be greater than $Y _ { ( p - 1 ) p + p / 2 }$ .By Lemma 10.2 we know that

$$
N ( \leq Y _ { ( p - 1 ) p + p / 2 } ) \geq { \frac { n } { p ^ { 2 } } } ( ( p - 1 ) p - { \frac { p } { 2 } } ) + p
$$

Hence

$$
\Phi _ { p } = n - N ( \leq Y _ { ( p - 1 ) p + p / 2 } ) \leq \frac { n } { p ^ { 2 } } ( p + \frac { p } { 2 } ) - p
$$

Case 3: $1 < i < p$

The number of elements merged by processor $_ i$ is equal to $n - N ( \leq Y _ { ( i - 1 ) p + p / 2 } )$ $- N ( > Y _ { i p + p / 2 } )$ . Applying Lemmas 10.2 and 10.3:

$$
\begin{array} { l } { \Phi _ { i } \ \le n - \left( \displaystyle \frac { n } { p ^ { 2 } } ( ( i - 1 ) p - \displaystyle \frac { p } { 2 } ) + p \right) - \left( \displaystyle \frac { n } { p ^ { 2 } } ( ( p - i ) p - \displaystyle \frac { p } { 2 } + 1 ) - 1 \right) } \\ { \qquad \le \displaystyle \frac { n } { p ^ { 2 } } ( 2 p - 1 ) - p + 1 } \end{array}
$$

The largest upper bound for $\Phi _ { i }$ comes from Case 3. Hence an upper bound on the number of X elements merged by any processor in phase four of the PSRS algorithm is $2 n / p - n / p ^ { 2 } - p + 1$

Now that we have established an upper bound on the number of elements that any processor may have to merge in phase four of the PSRS algorithm, we can analyze the algorithm's computational complexity.

In phase one each processor performs quicksort on $n / p$ elements. The computational complexity is $O ( ( n / p ) \log ( n / p ) ) ~ = ~ O ( n / p \log n )$ (Actually, $O ( n \log n )$ is the expected time complexity of performing quicksort on a list of $n$ elements; the worst-case time complexity is $O ( n ^ { 2 } )$ . However,we will assume $O ( n \log n )$ complexity in our analysis. If we must use the worst-case complexity in the analysis,we could substitute mergesort or another algorithm with worst-case time complexity $O ( n \log n )$ .)

In phase two of the algorithm one processor sorts the $p ^ { 2 }$ elements of Y. This step has complexity $O ( p ^ { 2 } \log p ^ { 2 } ) = \bar { O } ( p ^ { 2 } \log p )$

In phase three of the algorithm each processor sends portions of its section of $X$ to the other processors. Since each processor has $n / p$ elements, the complexity is $O ( n / p )$ (ignoring messge-startup times on distributed memory systems).

In the fourth phase of the algorithm each processor merges p sorted sublists. From Theorem 10.9 we know that no processor has more than 2n/p elements to merge. The time complexity of the merge phase is $O ( n / p \log p )$ P

The overall computational complexity of the PSRS algorithm is O((n/p) log n +p2log p+n/plog p). If n ≥ p3,the first term dominates,and the complexity of the algorithm is $O ( ( n / p ) \log n )$ ,which iscost optimal.

Li et al. (1992) have implemented the PSRS algorithmon a varietyof different MIMD architectures. Figure 10-30 illustrates the speedup achieved by the PSRS algorithm on the BBN TC2000,a NUMA multiprocessor. Figure 10-31 presents the speedup achieved on the iPSC/860 multicomputer. The algorithm achieves good speedup on both architectures.

Li et al. (1992) have also measured the relative deviation in size between the largest partition merged in phase four and the average partition size. Their experiments show that if the elements are selected froma uniform random distribution, the largest partition size is usually no more than a few percent larger than $n / p$ , the averge partition size.

Looking back at our three quicksort-based parallel sorting algorithms, we see that hyperquicksort and the PSRS algorithm achieve better speedup and are more scalable than parallel quicksort. Hyperquicksort and the PSRS algorithm reflect better attention to the parallel algorithm design strategies we have developed. In particular, they are data-parallel algorithms,each processor performs the most eficient sequential algorithm on its share of the data,and grain size is maximized.

# FIGURE 10-30

![](images/8f99f9f17c1d1c71d5c3907a2c2ea0856ff8fd40563a06d178bc22f4801f809d.jpg)  
Speedup achieved by the PSRS sorting algorithm on the BBN TC200, a NUMA multiprocessor (Li et al. 1992).

![](images/70e9d4d0f3c0414035e4380478281b9c184f592cca715016653ffb5e9505c360.jpg)  
FIGURE 10-31 Speedup achieved by the PSRS sorting algorithm on the Intel iPSC/860 multicomputer (Li et al. 1992).

Random read and random write are frequently used data movement operations on distributed-memory computers. Each operation involves two sets of processing elements: the source processors and the destination processors. Source processors send a record containing a key and its associated data. Destination processors receive a record.A processing element may be both a source and a destination.

In a random read operation, each destination processing element specifies the record key it wishes to receive, or else it specifies a null key，meaning it does not wish to receive a record. Several destination-processing elements can specify the same key. In a random write operation, each source-processing element sends a record to a specified destination-processing element, or else it specifies a null address,meaning it does not wish to send a record. Several source-processing elements may specify the' same address,in which case the record actually received by the destination processing element is determined by some constant-time commutative, associate, binary operation. For example, the record kept could be the one with the minimum key.

Many portions of parallel algorithms implemented on multicomputers are characterized by no communication or regular communication.

Consider the following code fragment:

for $i \gets 1$ to $n$ do $a [ i ]  [ i ] + c [ i ]$ endfor

If arrays $a , b$ ,and $c$ are partitioned identically among the processors, the additions can be performed without any communications.Each processor will work on values it controls.

Sometimes communication patterns are regular. Here is an example of a regular communication:

for $i \gets 1$ to $n$ do $a [ i ]  \mathsf { m i n } ~ ( a [ 0 ] , a [ i ] )$ endfor

The processor owning $a [ 0 ]$ can broadcast the value to other processors,and they can independently perform the mininum operation on elements of array $^ { a }$ they control.

Other algorithms, however,are characterized by irregular paterns of communication that are data dependent. This means they cannot be precomputed at compile time. Consider the following code segment:

for $i \gets 1$ to $n$ do $a [ b [ i ] ]  c [ i ] + d [ i ]$ endfor

The extra level of indirection means that, in general, the processor controlling the variables $c [ i ]$ and $d [ i ]$ doesn't own $a [ b [ i ] ]$ . In this case one way to implement the algorithm is to have each processor compute $c [ i ] + d [ i ]$ for its value of $i$ ,compute index $b [ i ]$ ,then send the sum to the processor controlling $a [ b [ i ] ]$ .We call this communication patrn random write-every processor generates a group of data values destined for arbitrary locations in the multicomputer.

Here is another example of a irregular communication pattern:

for $i \gets 1$ to $n$ do $a [ i ]  b [ c [ i ] ]$ endfor

In this case each processor computes index $c [ i ]$ , then must fetch the value stored at location $b [ c [ i ] ]$ . We call this communication pattern random read. Every processor generates a list of addresses in the multicomputer-(processor, offset) pairs-from which values must be retrieved.

What is the best way to implement random write and random read algorithms on a multicomputer? In most cases it doesn't make sense for every processor to generate one message for every data element it needs to store or fetch. The message-passing overhead would be too high. A better strategy is to bundle messages. There are two ways to do this.

One message-bundling strategy binds messages according to their destination processor. Each processor sends a messge to each of the other $p - 1$ processors.

![](images/aa245e91534a228a7c1a3f15d1563b47a54d011864cb0119b6e9a6fb3a675488.jpg)  
FIGURE 10-32 A high-level view of random write on a multicomputer, from the processor 19. (a) The processor begins with a list of triples.Each triple contains a value $v$ ,aprocessornumber $k$ andanaddressa.Value $v$ should be written at memory location a on processor $k$ One letter ismailed for each triple. For each triple,processor 19 labels the envelope with the processor number and encloses the value/address pair inside. (b) The letters areabout to be routed. (c) Letter routing has been completed. (d) Processor 19 now has all the letters addressed to it. (e) For each value/address pair, processor 19 writes the value at the specified address. (Courtesy Hatcher and Quinn [1991].)

This strategy may be sensible if the underlying hardware has circuit-switched routing and there are a large number of data items going to the same destination.

A second message-bundling strategy uses sorting to route packets to the correct processor. Given that every address is in the form of a (processor, offset) pair,a sorting algorithm can route data so that each processor receives those packets with a matching processor number.

Figures 1O-32 and 10-33 illustrate the phases of sort-based random write and random read algorithms,respectively.

# 10.7 SUMMARY

Sorting is an important utility on both serial and parallel computers. It is the foundation of many important parallel algorithms.On distributed-memory models, for example, random read and write are used in sorting.

In this chapter we have seen how a modified CRCW PRAM with $\pmb { n }$ processing elements can sort $_ n$ elements in constant time (if processor spawning time is not counted). We have explored lower bounds for sorting on several different processor organizations, and we have seen how odd-even transposition sort is an optimal algorithm for processor arays organized as a one-dimensional mesh.

Batcher's bitonic merge algorithm, although not directly implementable in VLSI,is the basis for the sorting algorithms used in processor arrays organized as shuffle-exchange networks and hypercubes,as well as multicomputer models.Sorting can be performed in $\Theta ( \mathrm { l o g } ^ { 2 } n )$ time onthe shuffle-exchange and hypercube processor array models, given $n$ processing elements.The twodimensional mesh-processor array model cannot sort $_ n$ elements in polylogarithmic time; the bisection width puts a lower bound of $\Theta ( { \sqrt { n } } )$ for sorting on thismodel.

![](images/96d5d184c5851574471db12dbbbf6011b01fc1c09d21d4a37aaf6a7c00479142.jpg)  
33A high-level view of random read，from the perspective of physical processor 19. (a)Processor 19 beginswitha listof quadruples.Eachquadruple containsa source processor $P _ { s }$ ,asourceaddress $A _ { s }$ ,adestination processor $P _ { d }$ ，anda destination address $P _ { a }$ Inthis figure we are assuming that the processor sending the requests is also the destinationprocessor;hence $P _ { d }$ is19.The valuecurrentlyataddress $A _ { s }$ on processor $P _ { s }$ must be written at address $A _ { d }$ on processor 19.One letter ismailed for eachquadruple.The letter isaddressedto processor $P _ { s }$ Inside the letter area slip of paper containing $A _ { s }$ andareturn envelope addressed toprocessor19. Inside the return envelope isanother piece of papercontaining $A _ { d }$ (b)Outgoing letters.(c) incoming letters.(d)Processor19examinesitsmail.Thesearetherequests fromotherprocessors forvaluesstored inprocessor19'smemory. (e) Foreachrequest,processor19reads thevaluefrom theaddressrequested,filsintheblankvaue fieldandstuffsthe value/addresspair in thereturn envelope.(f) Outgoing letters.(g) Incoming letters. (h)Processor19hasreceived thevaluesit requested.(i) Forevery value/addresspair， processor 19 writes the value at the address indicated. (Courtesy of Hatcher and Quinn [1991].)

We looked at three quicksort-based algorithms for sorting on MIMD computers. The first algorithm,parallel quicksort, is targeted for a UMA multiprocessor, because it assumes every processor has fast access to every unsorted element, as well as to a shared stack containing indices of unsorted subarrays.

The analysis of parallel quicksort demonstrates that divide-and-conquer algorithms may achieve unsatisfactory speedup if they do not get all the processors involved in the computation fast enough. The hyperquicksort algorithm demonstrates that sorting may be performed efficiently on multicomputers. Finally, the PSRS algorithm has been applied to a variety of MIMD architectures and has achieved reasonably good speedup on them all. An attribute of the PSRS algorithm is that an upper bound on the amount of work performed by any processor can be derived analytically.

# 10.8 BIBLIOGRAPHIC NOTES

Parallel sorting algorithms have been the object of much study. In fact, an entire book has been devoted to the topic: Parallel Sorting Algorithms (Akl 1985). Two survey articles on parallel sorting are by Lakshmivarahan, Dhall, and Miller (1984); and Bitton et al. (1984). Knuth (1973) also discusses parallel sorting algorithms, including odd-even transposition sort.

Atjai, Komlós, and Szemerédi (1983) describe an algorithm that uses $\Theta ( n \log n )$ processors to sort $n$ elements in time $\Theta ( \log n )$ . Leighton (1984) shows how this algorithm can be used to sort $n$ elements in time $\Theta ( \log n )$ by using $n$ processors, which is asymptotically optimal. However, Leighton points out that the constant of proportionality of this algorithm is immense and that unless $n > 1 0 ^ { 1 0 0 }$ ,these algorithms would be slower in practice than other parallel sorting algorithms. Other $O ( \log n )$ time PRAM sorting algorithms in the literature include Hirschberg (1978); Preparata (1978); and Reischuk (1981). Rajasekaran and Reif (1989) discuss sublogarithmic time randomized parallel sorting algorithms.

In contrast, some papers have described parallel sorting algorithms for constant-valence, fixed connection networks. Batcher’s bitonic sorter,already discussed in this chapter, is such a sorter.It uses $n$ processors to sort $n$ elements in time $O ( \log n )$ . Preparata and Vuillemin (1981) have achieved the same time complexity with the same number of processors using the cube-connected cycles network. Reif and Valient (1987) have devised a randomized $O ( \log n )$ algorithm that sorts $n$ elements on an $n$ -node cube-connected cycles network.

Other references to parallel sorting algorithms based on bitonic merge include Baudet and Stevenson (1978); Brock et al. (1981); Flanders (1982); Kumar and Hirschberg (1983); Lorin (1975); Meertens (1979); Nassimi and Sahni (1979,1982); Perl (1983); Preparata (1978); Preparata and Vuillemin (1981); Rudolph (1984);and Schwartz (1980). Inaddition to the bitonic merge-sort discussed inthischapter,Thompsonand Kung (1977) present anothersorting algorithm for the two-dimensional mesh-processor array model,called the $s ^ { 2 }$ way odd-evenmerge,hichalsoanort ${ \bar { n } } = m ^ { 2 }$ elements in time $\Theta ( { \sqrt { n } } )$

Papers on bitonic merge sort include Bilardi and Nicolau (1986); Brock et al. (1981); Hoey and Leiserson (1980); Kleitman et al. (1981); Knuth (1973); Leighton (1983); Meertens (1979); Schwartz (1980);and Stone (1978).

Early references to odd-even transposition sort include Demuth (1956), Knuth (1973),and Kung (1980). Besides the references cited earlier in the chapter,other implementations of theodd-even transposition sort include Chen et al. (1978a, 1978b); Kramer and van Leeuwen (1982); Kumar and Hirschberg (1983); Lee, Chang,and Wong (1981);and Miranker, Tang,and Wong (1983). Baudet and Stevenson (1978) generalized the algorithm so that each processor sorts a subsequence, rather than a single value.

Thompson and Kung (1977) discuss the row-major, snakelike row-major, and shuffled row-major processor numbering schemes on processor arrays organized as two-dimensional meshes.Nassimi and Sahni (1979) discuss the lower bound for sorting on this model. They also describe algorithms to sort elements into row-major order and snakelike row-major order.

Muller and Preparata (1975) first proposed the idea of sorting by using a tree of processors to augment a mesh-connected processor array. Leighton (1981) derives lower bounds for several computations performed on this model. Other references to sorting algorithms based on treelike networks of processors include Aggarwal (1984),Bentley and Kung (1979),Horowitz and Zorat (1983), Meadandoay (98)tout (983a)ndimoto(982a98b).le menting tree machines in VLSI is the subject of papers by Bhatt and Leiserson (1982),Leiserson (198o),eadandem (1979),uzoandyder (1981), and Valiant (1981).

Todd (1978) describes how to perform mergesort on a pipeline of processors.

Muller and Preparata (1975) have proposed a parallel enumeration sort. Other implementations of enumeration sorts appear in Hsiao and Snyder (1983); Leighton (1981); Nath,Maheshwari,and Bhatt (1983);andYasuura,Tgaki, and Yajima (1982).

Other sorting networks are discussed in Armstrong and Rem (1982); Atjai et al. (1983); Carey et al. (1982); Chen et al. (1978a,1978b); Chin and Fok (1980); Chung et al. (1980a,1980b); De Bruijn (1984); Dowd et al. (1983); Hong and Sedgewick (1982); Lee et al. (1981); Miranker et al. (1983); Moravec (1979); Mukhopadhyay (1981); Mukhopadhyay and Ichikawa (1972); Tseng and Lee (1984a, 1984b); Winslow and Chow (1981,1983); and Wong and Ito (1984).

Valiant (1975), Hirschberg (1978),Horowitz and Zorat (1983), Kruskal (1983)，Preparata (1978), Reischuk (1981), Shiloach and Vishkin (1981), Borodin and Hopcroft (1985),and Cole (1988) have proposed parallel sorting algorithms for PRAM models.

Alon and Azar (1988) compare the average complexity of deterministic and randomized PRAM sorting algorithms. Auf der Heide and Wigderson (1987) and Azar and Vishkin (1987) prove lower bounds on the complexity of sorting on CRCW PRAM models.

The tree sorter of Bentley and Kung (1979) and the rebound sorter of Chen et al. (1978b) incorporate sorting time into data I/O time.

Chabbar (198O) presents a parallel enumeration sort for the MIMD model. Bilardi and Nicolau (1989) describe a parallel bitonic sort for multiprocessors.Besides the earlier citations, other references for MIMD quicksort algorithms include Chen et al. (1984),Evans and Yousif (1985),Francis and Pannan (1992), Heidelberger (1990), Lorin (1975), Robinson (1977),and Singh et al. (1991).

Various authors have proposed MIMD sorting algorithms that have two phases: a phase in which each processor quicksorts its own subset of the data, followed by a phase in which processes cooperate to merge their sorted subsets. References to such algorithms in the literature include work by Francis and Mathieson (1988); Quinn (1988); Wheat and Evans (1992). Evans and Yousif (1986) proposed a two phase sort in which each processor uses the two-way merge algorithm during the first step to sort its share of the elements.

Winslow and Chow (1983) and Yang et al. (1987) have explored sorting algorithms that rely upon good, initial data partitioning to allocate about the same number of elements to each processor,at which point the processors sort their portion of the elements.

Robinson (1977), Tolub and Wallach (1978), and Varman and Doshi (1992) have described parallel-sorting algorithms for MIMD computers based on merging. Tolub and Wallach (1978) also discuss a parallel bucket sort. Quinn (1988) discusses parallel shell sort.

Loui (1984) derives upper and lower bounds for sorting on distributed computers. References to distributed sorting algorithms include Rotem et al. (1983) and Wegner (1982).

Parallel external sorting algorithms are discussed in Akl and Schmeck (1984); Bonuccelli et al. (1984); Lee et al. (1981); and Yasuura et al. (1982).

10-1 Rewrite the CRCW PRAM enumeration sort algorithm so that it requires only $n ( n - 1 ) / 2$ processing elements, yet still executes in constant time.   
10-2 Use the proof technique of Theorems 10.1 and 10.2 to derivea lower bound for sorting on the shuffle-exchange processor array model.   
10-3 Use the proof technique of Theorem 10.3 to derive a lower bound for sorting on the one-dimensional mesh processor array model.   
10-4 Usethe proof technique of Theorem10.3 to derivea lower bound for sorting on the two-dimensional mesh processor array model.   
10-5 Sorting on the two-dimensional mesh processor array model has complexity $\Omega ( { \sqrt { n } } )$ .How would the complexity change if the processing elements on the left edge were connected to processing elements on the right edge,and the processing elements on the top edge were connected to processing elements on the bottom edge,giving every processing element four neighbors?   
10-6 Derive a lower bound for sorting n elements on the hypercube processor array model with $n$ nodes,where the elements are distributed one-per-node before and after the sort.   
10-7 Use odd-even transposition sort to sort these sequences: (a) 5,8,3,2,4,6,4,1 (b) 1, 3,5,7,2,4,6,8

10-8 Do you think it is accurate to describe odd-even transposition sort as a parallel bubble sort? Justify your answer.

10-9Which of the following sequences are bitonic sequences?

(g) 8,4, 2, 1, 2,5, 7, 9   
(h) 1, 9, 7, 3, 2, 5

10-10 Proveor disprove: Allsequences containing fewer than four elements are bitonic sequences.   
${ \bf 1 0 . 1 1 * }$ Prove Lemma 10.1.   
10-12 Show how the following 16 values would be sorted by Batcher's bitonic merge algorithm: 7, 9,10,2,3,6,16,1, 14,5,15,8,4,11, 13,12.   
10-13 In general the bitonicsortof $2 ^ { k }$ numbers requires how many comparison steps, with each step using $2 ^ { k - 1 }$ comparators?   
10-14 Show how the following 16 values would be sorted by te shuffe-exchange network implementation of btonic mergesort: 7,9,10,2,3,6,16,1,145, 15, 8, 4, 11, 13, 12.   
10-15 How many shuffle-exchange steps does Stone's bitonic sorter require for $n$ values,where $n = 2 ^ { k }$ and each step uses $n / 2$ comparators?   
$\mathbf { 1 0 . 1 6 ^ { * } }$ Given a $_ n$ -element processor array organized as a $j$ dimensional mesh,proe that bitonic sort can be performed in time $\Theta ( n ^ { 1 / j } )$ ,using the $j$ -wayshuffled row-major index scheme.   
$1 0 . 1 7 ^ { \ast }$ Prove that the bound in the previous exercise is optimal.   
10-18 Why must Stone's perfect-shuffle algorithm carry a mask vector,while the hypercube-based algorithm does not?   
10-19 A problem with the parallel quicksort algorithm presented is that too many processes wait too long before getting work to do. Find at least two ways to modify the parallel algorithm so that more processes are busy sooner.   
10-20 What is the worst-case time complexity of the parallel quicksort algorithm?   
10-21 What is wrong with the following termination condition for the parallel quicksort algorithm? The processes should halt when the stack containing indices of unsorted subarrays is empty.   
10-22 Under what conditions, if any,is hyperquicksort cost optimal?   
10-23 Predict the performanceof thehyperquicksort,modifiedhyperquicksort,and PSRS algorithms,assuming the elements are already sorted when thealgorithm begins execution.   
${ \bf 1 0 . 2 4 ^ { * } }$ Theorem 10.9 assumes no two elements of $X$ have the same value. Derive an upper bound on the number of elements of $X$ any processor may have to merge in phase four of the PSRS algorithm, when any value may appear as many as $d$ times.

# 11

This chapter describes parallel algorithms used to solve the problems of searching an ordered table for the existence of a particular key, inserting keys into an ordered table,and deleting keys. Efficient sequential algorithms have been developed to allow dictionary operations to be performed in logarithmic time relative to the size of the table,an enormous improvement over the linear time needed if keys were kept in an unordered list. Sometimes it is important for multiple processes to perform dictionary operations concurrently. For example, it is probable that a parallel compiler must allow more than one process to access the symbol table simultaneously.

Search algorithms operate on elements, called keys, stored in a table of finite size. The goal is to organize the table and implement the algorithms so that functions such as inserting keys and their associated data into the table, deleting keys and data from the table,and searching for keys in the table, execute as quickly as possible.

This chapter is divided into two principal sections. Section 11.1 studies the inherent complexity of parallel search algorithms.We find that using multiple processors to perform a single operation is not particularly efficient-speedup is only logarithmic in the number of processors used. Section 11.2 presents two algorithms that perform batch searching; that is,they allow a number of searches to proceed concurrently. The first algorithm, developed by Elis (1980b)， allows concurrent search and insertion on AVL trees. The second algorithm, credited to Manber and Ladner (1982),allows deletions as well, although the AVL property is sacrificed.

# 11.1 COMPLEXITY OF PARALLEL SEARCH

How quickly can the search for a single key be performed on a parallel computer? It is useful to have a bound on the number of operations required to perform a particular function on a parallel computer, because we then have a standard by which to gauge various proposed algorithms.The CREW PRAM model is frequently used to find this bound.

Theorem 11.1. Given positive integers k,n,and p, where n = (p+1)\*-1,searching for a key in an n-element table while using the CREW PRAM model requires ≤ $\lceil \log ( n + 1 ) / \log ( p + 1 ) \rceil$ comparisons.hisbound istight. (SeeKruskal98983].)

Proof. We use induction on k to show that [log(n +1)/log(p+1)l comparisons are sufficient.Basis:Let k = 1. Then n= (p+1)1 -1 = p. Clearly one comparison step is sufficient for $p$ processors to determine whether the keyis in the table,and $\lceil \log ( p + 1 ) / \log ( p + 1 ) \rceil = 1 .$ Induction:Assume true forall tables of size $( p + 1 ) ^ { j } - 1$ ， where 1 ≤ j < k. To search a list of size (p+1)-1, during the first comparison processor $i$ for $1 \leq i \leq p$ ,compares the key with the table element indexed by $i ( p + 1 ) ^ { k - 1 }$ .After this step,either one of thetable elements has matched the key or else the key lies inside one of the unexamined subsections of the table. All these unexamined subsections have size $( p + 1 ) ^ { k - 1 } - 1$ .By the induction hypothesis, $k - 1$ comparison steps are suficient to search any of these subtables (Fig.11-1).

The second step of the proof is to show that the bound is tight. During the first parallel comparison step,only $p$ elements of the table are compared with the key. There must be one or more contiguous unexamined segments of the table with length at least

$$
{ \Bigg [ } { \frac { n - p } { p + 1 } } { \Bigg ] } \geq { \frac { n - p } { p + 1 } } = { \frac { n + 1 } { p + 1 } } - 1
$$

![](images/2d3d107767680a5ac260baad27aa113b0708f54bf155c886b5ef6a94bed007b8.jpg)  
FIGURE 11-1 First induction step for Theorem 11.1.

An inductive argument shows that after $k$ parallel comparison steps there must be one or more contiguous unexamined segments of the table with length at least

$$
\frac { n + 1 } { ( p + 1 ) ^ { k } } - 1
$$

Thus the number of steps required by any parallel algorithm in the worst case is at least the minimum $k$ ,satisfying

$$
\begin{array} { r l r } {  { n + 1 / ( p + 1 ) ^ { k } - 1 \le 0 } } \\ & { } & { ~ } \\ { \Rightarrow } & { k \ge \log ( n + 1 ) / \log ( p + 1 ) } \\ & { } & { ~ } \\ { \Rightarrow } & { k = \lceil \log ( n + 1 ) / \log ( p + 1 ) \rceil } \end{array}
$$

Using the results of Theorem 11.1, we can calculate the speedup achieved by the parallel algorithm searching an ordered list. Taking the number of comparisons made by the sequential binary search algorithm in the worst case, divided by the least number of comparisons made by the parallel algorithm in the worst case, we find that

$$
S = { \frac { \lceil { \log ( n + 1 ) } \rceil } { \lceil { \log ( n + 1 ) } / { \log ( p + 1 ) } \rceil } } \approx \log ( p + 1 )
$$

In other words, the speedup achieved through parallelization is logarithmic in the number of processors used.

What conclusions should we draw from this theorem? Since the CREW PRAM model can require as many as $\lceil \log ( n + 1 ) / \log ( p { + } 1 ) \rceil$ comparison steps, it is safe to assume that any realistic model of parallel computation will require at least that many comparison steps in the worst case. More realistic models could also have other time-consuming operations, such as data routing and process synchronization. Thus real parallel computers will experience speedup that is no more than logarithmic in the number of processors used,and it is not fruitful to attempt to speed up a single search. We cannot make much improvement on the sequential algorithm, which has logarithmic complexity.

Our strategy for the rest of Chap.11,then,is to speed upa series of searches. Search algorithms are not used for final results;they are frequently called subalgorithms for larger problems.Thus,it would beuseful to develop a method to perform searches,insertions,and deletions in parallel.

# 11.2 SEARCHING ON MULTIPROCESSORS

A logical way to approach the problem is to store the search tree in a shared memory and assign processors individual requests, making a single processor responsible for responding toa command to insert,delete,or search.This is the strategy behind both the following algorithms.

Ellis (1980b) has suggested a parallel algorithm that allows concurrent inserting and searching to take place in AVL trees. Here are some important definitions to aid us in our discussion of this algorithm.

Definition 11.1. The height of a rooted tree is the length of the longest path from the root to a leaf node. The "empty tree"-tree without even a root-has height $^ { - 1 }$ ， (See Aho,Hopcraft,and Ullman [1974].)

Definition 11.2. An AVL tree is a binary tree having the property that for any node $v$ in the tree,the difference in height between the leftand right subtrees of node $v$ is no more than 1.

Baer and Schwab (1977) have shown that AVL tree construction is the asymptotically optimal way of keeping binary search trees balanced when searching and inserting are the only operations performed.As keys are added to the AVL tree, two types of rotations are sufficient to keep the tree balanced: single rotation and double rotation. Both rotations occur when the two subtrees of a particular node do not have the same height and the height of the taller subtree increases.Theserotations,illustrated inFig.11-2quire $O ( \log n )$ time.

Sequential Insertion Algorithm Each node $v$ of an AVL tree has four fields associated with it. $K e y ( v )$ contains a unique key; left(v) is a pointer to the left subtree and $r i g h t ( \upsilon )$ is a pointer to the right subtree. $B a l ( \boldsymbol { v } )$ is an integer whose value is O if the left and right subtrees are balanced,whose value is $^ { - 1 }$ if the left tree is taller than the right subtree,and whose value is $+ 1$ if the right tree is taller than the left subtree.

The sequential insertion algorithm has three phases. In the first phase the tree is searched to find the appropriate place to attach the new leaf node.During the search a pointer is set to indicate the last node encountered with subtrees of a different height. This node,hereafter referred to as node $c$ ,is called the critical node. If every node along the search path has balanced subtrees, then the root is the critical node. The first phase ends by inserting the new leaf node.

Phase 2 consists of traversing all the nodes on the path between the newly inserted node $v$ and the critical node $c$ .For each such node $w$ ,if $k e y ( \upsilon ) <$ $k e y ( w )$ ，then $b a l ( w )$ is given the value $^ { - 1 }$ ; otherwise, $b a l ( w )$ is given the value $+ 1$

Phase 3 modifies the value of $b a l ( c )$ and rotates the tree if necessary. If $b a l ( c ) = + 1$ and $\upsilon$ was inserted in the left subtree, or if $b a l ( c ) = - 1$ and $v$ was inserted in the right subtree, then $b a l ( c )$ is changed to O and no rotation is necessary. If $c$ is the root node and $b a l ( c ) = 0$ ,then $b a l ( c )$ is set to $^ { - 1 }$ or $+ 1$ ， depending upon whether the insertion was into the left or right subtre.

![](images/86b7d4b58f0f2adb897fc8a2fbd37203cabd2bcfa27dfd780cd85bc9228e0057.jpg)  
FIGURE 11-2 Rotations to keep AVL tree balanced. (a) Single rotation. (b) Double rotation.

Otherwise v was inserted into the subtree with greater height,and a single or double rotation must be performed.

Parallel AlgorithmThe goal of the parale algorithm is to keepas many search and insertion processes active as possible. It is not possible for each process to ignore the other processes. For example, consider the AVL tree of Fig.11-3a. Assume that two processes are active: the first is inserting the value37,and the second issearching for the value13.After the value37is inserted into the tree,a single rotation must be performed to preserve the AVL property.This rotation requires that the values of certain left and right pointers be changed. The process of changing these pointers is illustrated in Fig.11-3b and c. (Figure 11-3d is a redrawing of Fig. 11-3c.) Suppose that the process searching for key 13 follows the right child of node 6 and the left child of node 25,when the tree is in the state depicted by Fig. 11-3b. The value 13 would not be found, even though it is in the tree.Another contention problem could occur if two processes attempted to rotate subtrees that have nodes in common.

![](images/c459928eb2a8e0ea8acf2c1e5fdfcb110389fdf780d358dcdbe3291f3d2a3001.jpg)  
FIGURE 11-3 Transformations in AVL tree as value 37 is added.

Ellis solves contention problems by adding three lock fields to each node. These lock fields enable search processes to be locked out of a rotating subtree. They also enable an insert process to lock subsequent insert processes out of the entire subtree rooted by the parent of the critical node.

Three lock fields are added to each node of the AVL tree: $\rho$ lock, $\alpha$ lock, and $\xi$ lock. A process performing a search must hold a node's $\rho$ lock before examining the contents of that node. The $\alpha$ locks are set by an insert process to keep other insert processes off the path from the parent of the critical node to the point of insertion. The $\xi$ locks exclude search processes from nodes involved in a rotation.More than one search process can share a single $\rho$ lock, and multiple search processes can hold a node's $\rho$ lock while a single insert process holds node's alpha lock.However, $\alpha$ locksand $\xi$ locks may not be shared,and if an insert process holds a node's  lock,then no other processes can hold the $\alpha$ lock or the $\rho$ lock.

In the case of a single rotation, the $\xi$ locks of the critical node and its parent must be set. A double rotation requires that the $\xi$ locks be set on the critical node,the parent of the critical node,and the child of the critical node lying along the insertion path. Table 11.1 illustrates what locks are held on an AVL tree at various times during the execution of four processes performing insert or search operations.

During execution of Ellis's algorithm, a process performing an insertion sets $\alpha$ locks as it traverses the tree. The $\alpha$ locks from the parent of the critical node through the place of insertion remain locked during insertion and rotation. This locking strategy excludes other processes from performing insertions along the entire subtree rooted by the parent of the critical node. Hence the number of concurrent insertions is quite limited. (Elis 198ob) has designed another parallel algorithm requiring that fewer nodes be locked, allowing more insertions to take place concurrently.

TABLE 11-1 EXECUTION OF ELLIS'S ALGORITHM.   

<table><tr><td>Task Insert 51</td><td>Search for 46 Insert 25 Search for 17</td></tr><tr><td>Lock α 26 Lock ρ 26 Unlock ρ 26 Lock α 34 Lock p 34</td><td></td></tr><tr><td>Lock α 49 Unlock p 34 Lock p 49</td><td></td></tr><tr><td>Current state illustrated in Fig.11-4a</td><td></td></tr><tr><td>Lock α 66 Insert key 51 Terminate Lock §26 Lock §34</td><td>Unlock p 49 Waiting for α 26</td></tr><tr><td>Current state illustrated in Fig. 11-4b Rotate at 34</td><td></td></tr><tr><td>Release all locks Terminate</td><td>Lock α 26 Lock α 20 Lock α 23 Insert key 25 Lock ρ 26 Waiting for §26</td></tr><tr><td>Current state illustrated in Fig. 11-4c</td><td></td></tr><tr><td></td><td>Unlock p 26 Lock §26 Lock ρ 20</td></tr></table>

![](images/7009117e3a9e4123ba452750023ec1a3eccf6c6d5e90ede15e853204bd1d821d.jpg)  
FIGURE 11-4 Paralel search and insertion in an AVL tree.

To summarize, Ellis’s algorithm assigns individual processes to search for or insert particular keys.A number of searches and insertions can take place concurrently.The algorithm has three important weaknesses.First, itdoes not allowdeletions tobeprformed.econd,itsffers fromcontentionforasred resource-processes performing insertions prevent other insertion proceses from accessing entiresubtrees.Third,the parallel algorithm has a lot of overhead.Even a search process must lock and unlock every node it examines.

# 11.2.2 Manber and Ladner's Algorithm

Manber and Ladner (1982) have suggested a parallel searching algorithm for the UMA multiprocessor model that allows deletions but sacrifices the AVL tree property. Manber and Ladner's algorithm does not try to maintain a balanced tree.They hope that the insertions and deletions will be random enough to maintain a reasonably balanced tree. (A study by Eppinger (1983) suggests that this hope is justified only under certain conditions.） In return for this concession, their algorithm is much simpler, because insertion and deletion processes do not have the responsibility of rotating the tree. An interesting feature of this algorithm is the use of maintenance processes to physically delete nodes.

Every node $v$ in the search tree has 1O fields associated with it:

Key(v),according to which the nodes are ordered   
$D a t a ( \upsilon )$ , a pointer to the data associated with the key   
$L e f t ( v )$ ,a pointer to the left subtree of $v$   
$R i g h t ( v )$ , a pointer to the right subtree of $v$   
Parent(v), a pointer to the parent of $v$   
Garbage(v), set to true when the node has been removed from the tree   
Redundant(v), set to true when the node hasa copy in the tree   
$C o p y ( v )$ ,which when true means $v$ is a copy of another node   
Userlock(u),a lock that can be set by a delete process   
Mlock(v),a lock that can be set by a maintenance process

The root of the tree is a special-purpose node with key $\infty$ It contains nd data and cannot be deleted. This simplifies the parallel algorithms.

There are two reasons why nodes need to be locked. First, a node needs to be locked to ensure that only one process ata time updates its data. Second,nodes need to be locked to make sure that two or more processes cannot attempt to change the shape of the tree at the same place at the same time. These two purposes are not independent; for example, one process cannot be allowed to delete a node while another process is updating it. Thus,one kind of lock, the userlock,is used for both purposes.

Every key is associated with a unique node. If the key is in the tree, its associated node contains the key. If the key is not in the tree, its associated node would be the parent of the key node if the key were inserted in the tree.Hence internal nodes are associated with a single key，while leaf nodes may be associated with a number of keys corresponding to a range of values. The basic operations of update, insert,and delete involve a single node. These operations begin by performing a strong search (defined later),which finds the node associated with the key and locks the userlock of that node.If the userlock is already locked,the process performing the operation is blocked until the node is unlocked. Only one basic operation can be performed on a particular node atone time. Incontrast toEllis'salgorithmhowever,allbasic operations can be performed by locking only one node. This provides much more latitude for concurrency. Note that except for the data field, all fields of a node may be examined while the node is locked. This allows a search to work its way through a locked interior node.

Basic User OperationsThe basic user operations are strong search, weak search, update,insert,and elete. This section escribes these orations.

Since searching does not change the tree, its parallel implementation is similar to the sequential algorithm. However, there is one important factor to consider. What happens if the search is performed and the result of the search reported, but another process has modified the tree between the time when the search was terminated and the result was reported? Sometimes this factor is irrelevant to the computation;at other times this factor may be crucial. Therefore we define two different search algorithms.

Weak search returns a result that is not guaranteed to be up-to-date. Weak search should be used whenever possible, because it does not require locking any nodes. Thus the parallel algorithm has no overhead and a process performing a weak search interferes with no other processes.

Strong search looks for a given key and returns the node $v$ associated with that key. To make sure that v will remain the node associated with the key as long as it is needed, the process performs a weak search, then locks v. After node v is locked,however,a check is done to ensure that v is still the node associated with the key. Between the time when v is found and when u is locked, three different events could invalidate the association between the key and v. First, v might have been removed from the tree [that is,garbage(v) set to true].Second, if key(v) is not the key being searched for,another node might have been inserted into the tree that is now the node associated with the key. Third, v might have become a redundant node [that is,redundant(v) set to true]. Redundant nodes are created as a side effect of deletions. Thus, when strong search returns a node, that node is guaranteed to be the one associated with the key and is locked. The node is unlocked only after the operation-update, insert,orelet--isoleted.

In Manber and Ladner's algorithm deletion is simple, because the deletion process must only logically delete the node.Maintenance proceses take care of physically deleting the node. The delete process uses strong search to find the node $v$ associated with the key and lock it.Assuming the key values match, data(u) is set to nil. The delete process puts $v$ on aspecial maintenance list,the delete list, so that a maintenance process can come along later and physically delete the node.

Concurrent insertion begins by performing a strong search for the node $v$ associatedwiththekeyIfaodeassociated withtheeyisoundtmay have been logically deleted [that is,data(v) isnil]. If sothe process adds the new data field, unlocks $\upsilon$ ,and terminates. If $v$ has not been logically deleted, the process reports that the node already exists，unlocks $v$ ，and terminates.

Assuming the key is not in the tree, then v is the leaf node that becomes the parent of the inserted node,and the insertion is performed identically to the sequential algorithm. After the correct child pointer of v has been set to indicate the inserted node, the process unlocks $v$ and terminates.

Maintenance Processes The maintenance processes physically delete nodes from the search tree. Recall that when a node is deleted, its pointer is put on a deletion list. Idle maintenance processes access this list to get pointers to nodes needing deletion.

If node $v$ is to be deleted and $v$ has only one child, the deletion is simple. The pointer from v's parent to $v$ isredirected to v's child, and v is effectively detached from the tree (see Fig. 11-5). (If $v$ is a leaf node, then the pointer from v's parent to $v$ is made nil.)

How soon can node $v$ be reused? Although v is no longer a part of the tree, another process may have accessed $v$ while it was being detached. The purpose of the boolean garbage(v) is to alert such a process that $v$ is no longer a part of the tree. Since parent(u) still points to its parent, an otherwise stranded search process can get back into the tree and continue.

As we have seen, v cannot be reused immediately. Manber and Ladner suggest that the garbage collection algorithm of Kung and Lehman (1980) be used.This algorithm uses three lists of nodes: the passive garbage list, the active garbage list, and the available list. When a maintenance process first removes a node from the tree, the node is put on the passive garbage list. This list grows until a maintenance process is ready to perform garbage collection. Garbage collection begins by copying a group of nodes from the passive garbage list into the active garbage list and noting which processes are active at the time of the copy. When all these processes have terminated, the active garbage list is appended to the available list. Since the only processes that can access nodes on the passive garbage list are those that were active when the copy to the active list was made,the nodes are truly inactive and suitable for reuse once these processes have terminated.

The physical deletion algorithm is more complicated if the node u has two children. Conceptually the deletion is performed in two steps (see Fig.11-6). First, the node $w$ having the largest key less than $k e y ( v )$ is found (Fig. 11-6a). Node $w$ has,at most,one child (since it cannot havea right child).Hence it is easy to delete $w$ by using the algorithm described earlier (Fig. 11-6b).

![](images/052c69a022e0fdb7d5e0434bfa471847966eb191b79cc16166ba06c25a435449.jpg)

![](images/cc0bc9919d608199733779fed90cd04cc815ac709b4a7604fefaf5cb033b0ffa.jpg)  
FIGURE 11-6 Conceptual idea of deletion of a node with two children.

The second step is to replace v with w (Fig. 11-6c). Since w is the immediate predecessor of v, the tree remains consistent. However,we must implement the deletion in a slightly different way to ensure that a copy of w is always accessible to a process searching for it.

The algorithm used by Manber and Ladner is illustrated in Fig. 11-7. First, create a copy of w,called w'. Note that data(w') =data(w) and copy(w') =true. Second,set left(w') to point to left(u) and right(w') to point to right(u).Third, set right(w) to point to w',and set redundant(w) to true. What happens if a process searching for node w is on the way from node u to w when this operation takes pace?hisprocess mayoeample,nttoerttoeight of node w.When the process encounters node w,it will find that redundant(w) = true and will therefore follow right(w) to w',where it will continue to node t. Fourth,remove node v by setting the appropriate child pointer of parent(v) to point to $w ^ { \prime }$ and setting garbage(v) to true.

Node w cannot be deleted immediately，because there may be processes looking for $w$ along the way from $\pmb { u }$ to $w$ .Amethod similar tothe garbagecollection algorithm solves the problem. We put node $w$ on a passive redundancy list. Nodes on the passive redundancy list become available for physical deletion only after all the processes alive at the time of the substitution terminate. Once $w$ is available for physical deletion, the process is straightforward, since $w$ has only a single child. The phases of the deletion process are summarized in Fig. 11-8.

![](images/47ced6f211958f4233a36711036eb4bb76177d060cdf9fcfe91873feb8384514.jpg)  
FIGURE 11-7 Deletion of a node with two children.

![](images/9b947a2005d1e590d23f8d4a1a78885a9a001385fb30fc49528d35b4a538db95.jpg)  
FIGURE 11-8 Phases of the deletion process of Manber andLadner'salgorithm

# 11.3 SUMMARY

It is hard to use processors eficiently if we want to speed up a single search operation. The sequential algorithm has logarithmic complexity,and the speedup achieved by the parallel algorithm can be,at most,logarithmic in the number of processors used. Achieving even this modest speedup is difcult on real parallel computers. Hence the goal should be to perform a series of searches, insertions, and deletions as quickly as possible.

This chapter has described parallel algorithms to implement searching, inserting,and deleting on UMA multiprocessors. Both algorithms associate processes with particular operations to be performed. Locks must be used to keep processes from interfering with each other during critical operations.A primary difference between the two algorithms is that Elis's algorithm may require locking a number of nodes logarithmic in the size of the tree,whereas Manber and Ladner's algorithm never requires more than a single node to be locked.

Ellis's algorithm allows searching and inserting to take place in AVL trees. A process inserting a key must lock the subtree rooted by the parent of the node to be rotated. Hence the amount of concurrency among inserting processes is limited. Search processes must lock and unlock every node they examine. Although more than one search process can share such a lock, the frequency of the lock-unlock operation adds to the overhead of the parallel algorithm.

Manber and Ladner's algorithm requires that no search,insert, delete,or update process lock more than a single node of the search tree. This greatly improves the efficiency of the parallel algorithm. The delete process simply marks a node for deletion. Separate maintenance processes,which must lock three nodes, perform the physical deletion of nodes from the search tree. The algorithm does not maintain a balanced tree. Manber and Ladner hope that the insertions and deletions will be random enough to keep the tree reasonably balanced. Evidence published after Manber and Ladner's work suggests that this hope is justified only under certain conditions (Eppinger 1983).

Our description of parallel searching has avoided the topic of memory bank conflicts. This important issue is addressed in Probs. 11-10 and 11.11.

# 11.4 BIBLIOGRAPHIC NOTES

Most books on data structures, including Wirth (1976) and Helman and Veroff (1986),discuss Ates.

This chapter does not describe Ellis's second parallel search and insertion algorithm for AVL trees. It can be found in Ellis (1980b). In addition to her work on AVL trees,Ellis (198Oa) has described algorithms allowing concurrent search and insertion in 2-3 trees. Code for all Manber and Ladner's procedures described in this chapter appears in Manber and Ladner (1982).

Two early papers discussing concurrent insertion into and balancing of binary search trees are Wong and Chang(1974) and Chang (1974). Work on concurrent access to trees holds interest for designers of data base systems. Kung and Lehman (198o) discuss the concurrent manipulation of binary search tres; Lehman and Yao (1981) describe concurrent algorithms for B\* trees. These algorithms have tree rotations require no more than a small, constant number of nodes to be locked.

Baer et al. (1983) investigate a number of algorithms to perform batch searching on processor arrays and UMA multiprocessors. Their paper focuses on the important problem of avoiding memory bank conflicts.Carey and Thompson (1984) have proposed a systolic algorithm for implementing search trees on MIMD computers. Ottman et al. (1982) have designed searching algorithms suitable for implementation in VLSI. Potter (1985) briefly describes the ease of searching on Goodyear’s MPP,a 2-D mesh SIMD computer. Ramamoorthy et al. (1978) have proposed a searching machine based upon associative memory.

# 11.5 PROBLEMS

11-1 Fill in the inductive argument of te second step of the proof of Theorem 11.1 by proving that after $k$ parallel computation steps there must be one or more contiguous, unexamined segments of the table with length at least

$$
{ \frac { n + 1 } { ( p + 1 ) ^ { k } } } - 1
$$

11-2 Given an $n \times n \ 2 – \mathrm { D }$ mesh SIMD model containing a sorted list of $n ^ { 2 }$ items and $n \log n$ items tosearch for,what is the time needed tocompleteall $n \log n$ searches?

11-3Is Elis's algorithm control parallel or data parallel? Explain your answer.   
11-4 In the context of Ellis's algorithm,provide an example showing how two processes performing rotations could contend with each other if the entire subtree rooted by the parent of the node to be rotated were not locked.   
11-5 Is Manber and Ladner's algorithm control parallel or data parallel? Explain youranswer.   
11-6 Provide an example showing why physical deletion of a node with two children cannot be performed as shown in Fig. 11-6.   
11-7 Provide an example showing why deleted nodes must be put on both the passive garbage list and the active garbage list before being put on the list of available nodes.   
11-8 In the context of Manber and Ladner’s algorithm, explain which nodes need to be locked by a maintenance process and why.   
11-9 Explain how to implement the update operation of Manber and Ladner's algorithm. An update operation finds a node associated with a specified key and changes the data field of that node to point to a different data item.

11-10 Assume a UMA multiprocessor with four CPUs and four memory banks. Assume a table $A$ of $n$ keys is to be searched,where $a [ 1 ] < a [ 2 ] < \cdots < a [ n ]$ and $a [ i ]$ is stored in memory bank $i$ ,modulo 4. Furthermore,make the simplifying assumption that the processors work in lockstep and that every processor fetches and compares an element of $A$ every memory cycle.If two processors $P _ { i }$ and $P _ { j }$ ,where $i < j$ ,try to access the same memory bank in the same cycle, processor $P _ { i }$ gets the value it desires,while $P _ { j }$ must repeat the access attempt on the next cycle. It is helpful to think of the binary search of an array as the traversal of a binary tree.See Fig.11-9 for an example of a binary tree representing an array of 2O keys. Given all these assumptions, suppose that $n = 2 0$ and $a [ i ] = i$ for $1 \leq i \leq 2 0$ .Suppose processor $P _ { 0 }$ is searching for value 13, $P _ { 1 }$ is searching for 4, $P _ { 2 }$ is searching for 10,and $P _ { 3 }$ is searching for 17. Draw a table showing the execution of the batch search for these keys. In particular,indicate which memory bank a processor accesses (or fails to access) each memory cycle.

![](images/4a2a39f0c4cf8ea96cdf47caa9ab6c254b22fe487955992daee2455a5d1ec341.jpg)  
FIGURE 11-9 A binary search of a 20-key table can be viewed asa search of this tree.

11-11 Repeat the previous exercise, with the following modifications.Suppose $n = 3 1$ and $a [ i ] = i$ for $1 \leq i \leq 3 1$

# 12

One way the early use of parallel computers has resembled the early use of sequentialcomputers has been the emphasis on numerical algorithms.However, as the field of parallel algorithms matures,the emphasis can be expected to shift to nonnumerical algorithms because more and more problems being solved on computers are symbolic in nature. This chapter examines a number of parallel algorithms developed to solve problems in graph theory. These problems relate to searching graphs and finding connected components, minimum-cost spanning trees, and shortest paths in graphs.

A review of elementary graph theoretic terminology appears in Appendix A.

PRAM algorithms for searching graphs arecovered in Sec.12.1.Section 12.2 presents three algorithms for finding the connected components of a graph.Sections 12.3 and 12.4 cover the al-pairs shortest path and single-source shortest path algorithms, respectively. In Sec.12.5 we describe the paralelization of two algorithms to solve the minimum-cost spanning tree problem. The primary references for this chapter are Quinn and Deo (1984) and Quinn and Yoo (1984).

# 12.1 SEARCHING A GRAPH

Given a CREW PRAM model of computation with $p$ processing elements, Reghbati and Corneil (1978) have determined the number of operations required for three parallel graph-searching algorithms. Recall that depth-first search of anarbitrary graph is most likely inherently sequential, since it isa $\mathcal { P }$ -complete problem (Sec. 2.5). Reghbati and Corneil thus consider a parallel variant of depth-first search, called $p$ -depth search (defined later),as well as parallel breadth-depth and parallel breadth-frst search.

For these algorithms an adjacency matrix is not a suitable representation of the graph to be searched, since the process of searching through the elements of the matrix to find edges consumes too much processor time. Hence Reghbati and Corneil use adjacency lists to represent the graph.

How quickly can a graph be searched? Initially a master list of vertices still to be searched contains a single vertex. Each processor examines one or more edges emanating from a vertex being searched. If the edge leads to a previously undiscovered vertex, it is added to that processor's partial list, containing vertices to be added to the master list. At certain intervals the partial lists formed by the processors are linked and combined with the master list. Assume that the only operations that consume time are the vertex selection process and the list-linking and combining process. Assume that it takes one of these active operations to select a vertex.For the sequential algorithm,only one active operation is required for the lone processor to add a new vertex to the master list. Let $n$ denote the number of vertices, $d _ { i }$ denote the degree of vertex $i$ ,and $m$ denote the number of edges ina graph. It is clear, then, that an upper bound for a sequential algorithm to search a graph is

$$
T _ { 1 } = \sum _ { i = 1 } ^ { n } ( d _ { i } + 1 ) = 2 m + n
$$

since vertex $i$ can be added to a partial list only once, and $d _ { i }$ is the maximum number of times that vertex $i$ can be chosen as the vertex from which searching is to be done.

# 12.1.1 P-Depth Search

In $p$ -depth search, $p$ edges incident upon a selected vertex are simultaneously searched. (Inther wordsprocessorsareasigned todgesne procesr per edge.) One of the most recently searched vertices is then chosen as the point from which the search is continued. This procedure ends when the master list of vertices having unexplored edges is empty.Figure 12-1b illustrates $p$ -depth search for $p = 2$ .Note that if $p = 1$ ,the result is a depth-first search.

Theorem 12.1. Given $p \ge 2$ processors,an upper bound on the number of active operations required by $p$ -depth search on the CREW PRAM model is

$$
\sum _ { i = 1 } ^ { n } \left\lceil { \frac { d _ { i } + 1 } { p } } \right\rceil ( \lceil \log p \rceil + 1 )
$$

(See Reghbati and Cormeil [1978].)

![](images/7afdd2af51af1e23839155dabcc574aee887c26a7a53f2c78dc4bc3d53df1971.jpg)  
FIGURE 12-1 Parallel algorithms to search graphs.Parenthesized numbers indicate order edges aretraversed.(a) Graph to be searched. (b) Two-processor p-depth search.(c) Twoprocessor parailel breadth-depthsearch.(d) Two-processor parallel breadth-first search. (Quinnand Deo (1984).Copyright1986 Associationfor Computing Machinery. Reprinted bypermission.)

Proof. The new vertices found at each state of the algorithm can be added to the master list of vertices in [log p] + 1 active operations,by linking lists in a treelike manner. The number of times that searching begins at vertex i is f(di +1)/p]. Therefore, the number of active operations required for parallel p-depth search is

$$
T _ { p } ^ { 1 } = \sum _ { i = 1 } ^ { n } \left\lceil \frac { d _ { i } + 1 } { p } \right\rceil ( \lceil \log p \rceil + 1 )
$$

$$
\begin{array} { l } { 1 \leq \displaystyle \sum _ { i = 1 } ^ { n } \left( \frac { d _ { i } + 1 } p + 1 \right) \left( \lceil \log p \rceil + 1 \right) } \\ { \displaystyle \qquad \leq \frac { T _ { 1 } ( \lceil \log p \rceil + 1 ) } { p } + n ( \lceil \log p \rceil + 1 ) } \end{array}
$$

Note that in order for $p$ -depth search to require fewer active operations than a sequential search, the term $( \lceil \log p \rceil + 1 ) / p$ must be less than 1. Hence $p \geq 4$ is a necessary condition for $p$ -depth search to require fewer active operations than a sequential search.

# 12.1.2 Breadth-Depth Search

A breadth-depth search proceeds by examining all the edges adjacent to a vertex before selecting one of the most recently reached vertices and continuing the search from there. In a parallel breadth-depth search,each processor keeps track of the new vertices it has discovered. Once all the edges from a vertex have been examined, these partial lists are linked and added to the master list. Since this parallel algorithm requires that partial lists link and combine with the master list less often than a $p$ -depth search, the algorithm requires fewer active operations. Figure 12-1c illustrates parallel breadth-depth search.

Theorem 12.2. Given $p \ge 2$ processors,parallel breadth-depth search requires no more than

$$
\sum _ { i = 1 } ^ { n } \left( \left\lceil { \frac { d _ { i } } { p } } \right\rceil + 1 + \left\lceil \log p \right\rceil + 1 \right)
$$

active operations on the CREW PRAM model. (See Reghbati and Corneil [1978].)

Proof. It requires $\lceil \log p \rceil + 1$ active operations to link the vertices found during exploration from vertex $i$ .Thereare $\lceil d _ { i } / p \rceil + 1$ examination steps beginning from vertex $_ i$ .Hence parallel breadth-depth search has an upper bound of

$$
\begin{array} { l } { \displaystyle T _ { p } ^ { 2 } = \sum _ { i = 1 } ^ { n } \left( \left\lceil \frac { d _ { i } } { p } \right\rceil + 1 + \lceil \log p \rceil + 1 \right) } \\ { \displaystyle \qquad \leq \frac { T _ { 1 } } { p } + n ( \lceil \log p \rceil + 3 ) } \end{array}
$$

# 12.1.3 Breadth-First Search

Parallel breadth-first search requires even fewer link-and-combine steps, because processors examine all vertices at level $i$ of the search tree before moving on to level i + 1 (Fig.12-1d). Thus, there is only one link-and-combine step for each level of the search tree.

Theorem 12.3. Given $p \ge 2$ processors on the CREW PRAM model, the number of active operations required by parallel breadth-first search is

$$
T _ { p } ^ { 3 } = \sum _ { i = 1 } ^ { n } \left( \left\lceil { \frac { d _ { i } } { p } } \right\rceil + 1 \right) + L \lceil \log p \rceil
$$

where L is the distance of the vertex farthest from the start vertex (Reghbati and Corneil 1978.)

Proof.This is left to thereader.

# 12.2 CONNECTED COMPONENTS

There are three common approaches to finding the connected components of an undirected graph. The first approach uses some form of search, such as depth-first or breadth-first. The second approach finds the transitive closure of the graph's adjacency matrix. Letting A denote the adjacency matrix of the original undirected graph G and B denote the transitive closure of A,we compute B by [log n] plus-min multiplications of A. (A plus-min multiplication is analogous to matrix multiplication, with scalar multiplication replaced by scalar addition and scalar addition replaced by the minimum operation.) The third approach collapses vertices into larger and larger sets of vertices until each set corresponds to a single connected component.

Hirschberg has used the third method to develop a connected components algorithm for processor arrays (Hirschberg 1976; Hirschberg et al. 1979). Although the algorithm is based on the CREW PRAM model of parallel computation,it has been widely studied and merits discussion.

Theorem 12.4. The connected components of an undirected graph can be found in (log²n) time on the CREW PRAM model with (n2) processors (Hirschberg 1976).

Summary of Algorithm. The primary data structure is the adjacency matrix. Instead ofcomputing thetransitiveosureoweverdacentvrticesarecomindit supervertices,which are themselves combined until each remaining supervertex represents a connected component of the graph.Like the transitive closure algorithm on the CREW PRAM model, this algorithm hasa complexity of (log²n),but requires only $n ^ { 2 }$ processors.

Each vertex is always a member of exactly one supervertex,and every supervertex is identified by its lowest-numbered member vertex,the root.The paralel algorithm iterates through three stages.Inthe first,the lowest-numbered neighboring supervertex of each vertex is found. The second stage connects each supervertex root to the root of the lowest-numbered neighboring supervertex. In the third stage all newly connected supervertices are collapsed into larger supervertices.Since the number of supervertices is reduced by a factor of at least 2 in each iteration, $\lceil \log n \rceil$ iterations are sufficient to collapse each connected component into a single supervertex. The operation of this algorithm is illustrated in Fig.12-2.

Theorem 12.5. The connected components of an undirected graph can be found in $\Theta ( \log ^ { 2 } n )$ time on the CREW PRAM model with $\Theta ( n \lceil n / \log n \rceil )$ processors (Hirschberg et al. 1979).

Summary of Algorithm.Hirschberg's originalalgorithm uses $n ^ { 2 }$ processors to assign values to the matrix containing the root numbers of neighboring supervertices.

![](images/a4fb392fc2c3906a57d1152ed66f51c806e9bac33d347e6393c200971a2fa70b.jpg)  
FIGURE12-2Hirschberg'sconnected-component algorithm.(QuinnandDeo(1984).Copyright $\circledcirc$ 1986 Association forComputing Machinery.Reprintedbypermission.

By applying Brent's theorem it is easy to see that $\lceil n / \log n \rceil$ processors are sufficient to assign $n$ values and find the minimum of $n$ elements,th in $\Theta ( \log n )$ time.Each processor can assign values to $\log n$ elements,instead of only one element, without increasing the time complexity of thealgorithm.Similarly,in the first phase of minimization,each processor can find the minimum of logn values,rather than two values,without increasing the complexityof the algorithm.Hirschberg'salgorithm thus can be implemented by using $n \left\lceil n / \log n \right\rceil$ processors,intead of $n ^ { 2 }$ ·

Theorem 12.6. The connected components of an undirected graph can be found in (log²n) time on the CREW PRAM model with (n[n/log² nl) processors (Chin et al. 1981; 1982).

Summary of Algorithm. Every vertex is involved during each iteration of Hirschberg's algorithm. Chin et al. noted that by restricting participation in each iteration to a representative vertex of each supervertex (the root) and by removingisolated supervertices from further consideration, the algorithm requires fewer processors.

Nassimi and Sahni (198ob) have adapted Hirschberg's algorithm to the qdimensional mesh-connected SIMD model. Let us examine their algorithm for the particular case of a two-dimensional processors mesh. At various points in the parallel algorithm the processors execute a random read or a random write, as described in Chap.10. Procedure RANDOM.READ has two arguments.The first argument denotes the address that receives the data; the second argument denotes the value to be read. For example, after statement

# RANDOM.READ (a,[b]c)

has executed, the value of local variable a of every unmasked processor is identical to the value of variable c of the processor indexed by the value of local variable $^ b$

Procedure RANDOM.WRITE has two arguments. The first argument denotes the value written;the second argument is the address to which the value is Written. For example, when the statement

# RANDOM.WRITE (a, [b]c)

executes, the value of local variable $^ { a }$ of every active processor is written to variable $c$ of the processor indexed by the value of local variable $^ b$ Ifmore than one value is writen to the same location, then the minimum of these values is the resultant value.

The complexity of performing a random read or a random write on the 2-D mesh SIMD model with $p$ processing elements is $\Theta ( p )$

The algorithm uses a new function called BITS. BITS $( i , j , k )$ returns the value of bits $j$ through $k$ of integer value $i$ ,where bit O is considered to be the least significant bit. If $j < k$ the function returns O. For example,

$$
\begin{array} { r l } { ( 1 7 , 3 , 1 ) = 0 } & { { } \quad \mathsf { B I T S } ( 1 0 , 3 , 2 ) = 2 } \\ { ( 1 6 , 4 , 4 ) = 1 } & { { } \quad \mathsf { B I T S } ( 1 5 , 2 , 3 ) = 0 } \end{array}
$$

Given a graph $G$ with $n = 2 ^ { k }$ vertices, the 2-D mesh SIMD algorithm shown in Figs.12-3 and12-4 finds the connected components of $G$ .Assume that the maximum degree of any vertex in $G$ is $d$ Letadj $( i , j )$ ,where $1 \leq i \leq n$ and $1 \leq j \leq d$ ,denote the edges of $G$ stored as anadjacency list. If vertex $i$ has $d _ { i } \ < d$ edges, then $a d j ( i , j ) = \infty$ for $d + i + 1 \leq j \leq d$ .This adjacency list is stored in the local memory of processing element $P ( i )$ .Assume that $p = 2 ^ { k }$ and that the processing elements are numbered in shuffled row-major order.

Parameter d {Maximum vertex degree) n {Number of vertices} Global e {Edge being considered] iteration {Iteration, number) Local candidate {Root of neighboring vertex} neighbor[1...d] {Neighboring vertices) r {Root number} 1. begin {Initially every node is a tree unto itself) for all $P _ { i }$ where $1 ~ \leq ~ i ~ \leq ~ n$ do $r \gets i$ endfor {Merge trees) 5. for iteration $ 0$ to $\lceil \log \ n \ \rceil \ - 1$ do {It is not known whether there is a neighboring tree} for all $P _ { i }$ where $1 ~ \leq ~ i ~ \leq ~ n$ do candidate $ \infty$ endfor {Look for the lowest-numbered neighboring root) for $\textit { e } \gets 1$ to $d$ do for all $P _ { i }$ where $1 ~ \leq ~ i ~ \leq ~ n$ do FETCH.AND.COMPARE(neighbor[e],r,candidate) endfor endfor 16 forall $P _ { i }$ where $1 ~ \leq ~ i ~ \leq ~ n$ do UPDATE.SUPERVERTEX.NUMBERS(candidate,r) endfor {Collapse supervertices) 17. REDUCE $( r , n )$ 18. endfor 19.end

In addition to the edges of vertex i,each processing element $P ( i )$ has a local variable r that corresponds to the pointer of the supervertex root in Hirschberg's algorithm,and another local variable tmpused as temporary storage.Procedure REDUCE corresponds to the third stage of Hirschberg's algorithm, collapsing vertices so that every vertex in a supervertex points to the root.

FETCH.AND.COMPARE (u,r， candidate) Value $v$ {Neighboring vertex} r {Vertex'scurrent root number] Reference candidate {Lowest-numbered neighboring root] Local tmp {Value fetched from other processor) begin   
1. RANDOM.READ (tmp,[u]r)   
2 if $t m p = ~ r$ then $t m p  \infty$   
4. endif   
5. candidate min( candidate, tmp)   
6.end   
UPDATE.SUPERVERTEX.NUMBERS(candidate, r) Value candidate, $r$ begin {Each supervertex root gets the minimum of the root numbers of neighboring supervertices)   
1. RANDOM.WRITE(candidate， $[ r ] r$ {Take care of supervertices with no neighbors}   
2. if $r ~ = ~ \infty$ then   
3. $r \gets i$   
4. endif {Make sure no cycles are formed)   
5. if $r \ > \ i$ then   
6. RANDOM.READ $( r , ~ [ r \ ] r )$   
7. endif   
8.end

REDUCE $( r , n )$ ：   
Reference $r$ Value $n$   
1. begin   
2. for $b \gets 1$ to log $_ n$ do   
3. forali $P _ { i }$ do   
4. if $\mathsf { B } | \mathsf { T S } ( r , \mathrm { l o g } \ n - 1 , b ) = \mathsf { B } | \mathsf { T S } ( i , \mathrm { l o g } \ n - 1 , b )$ then   
5. RANDOM.READ $( r , ~ [ r ] r )$   
6. endif   
7. endfor   
8. endfor   
9.end

Theorem 12.7. The connected components of an undirected graph $G$ with $n = 2 ^ { k }$ vertices and maximum vertex degree $d$ can be found in time $O ( d n \log n )$ on the 2-D mesh SIMD model having $n$ processors (Nassimi and Sahni 1980b). Complexity Analysis. This is left to the reader.

Theorem 12.8. Suppose the adjacency matrix of an undirected graph $G$ with $n$ vertices is stored in the base of a pyramid SIMD computer of size $n ^ { 2 }$ .Then the connected components of $G$ can be found in time $O ( { \sqrt { n } } )$ (Miller and Stout 1987). Summary of Algorithm.Miller and Stout, like authors previously mentioned,have based their algorithm on the work of Hirschberg. Their innovation is the effective use of the pyramid's topology. As the algorithm progresses, there are fewer and fewer supervertices (min trees) to be combined. When the forest of min trees is to be relabeled, data are moved up the pyramid,where the combining step can be performed on a mesh of appropriate size.

# 12.3 ALL-PAIRS SHORTEST PATH

A variant of matrix multiplication can be used to solve a number of graph problems, including the all-pairs shortest-path problem. The proof of Theorem 12.9 describes the transformation needed.

Theorem 12.9. Given an $n$ -vertex weighted graph, the all-pairs shortest-path problem can be solved in $\Theta ( \log ^ { 2 } n )$ time on the hypercube SIMD and shufle-exchange SIMD models, given $n ^ { 3 } = 2 ^ { 3 q }$ processors (Dekel etal.1981).

Proof. Let $G$ be an $n$ -vertex weighted graph. Our goal is to produce an $n \times n$ matrix A such that $a _ { i , j }$ is the lengthof theshortestpath from $_ i$ t0 $j$ in $G$ Let $a _ { i , j } ^ { k }$ denote the length of the shortest path from $i$ to $j$ with,at most, $k - 1$ intermediate vertici $G$ $a _ { i , j } = a _ { i , j } ^ { n - 1 } .$ In this example, $a _ { i , i } ^ { 1 } ~ = ~ 0$ ，for all $i$ ， $1 ~ \leq ~ i ~ \leq ~ n$ ,and for all distinct $i$ and $j$ $a _ { i , j } ^ { 1 }$ is the weight of the edge from $i$ to $j$ ; if no such edge exists, $a _ { i , j } ^ { 1 } = \infty$ . It follows from the princiit Henee $\mathbf { A } ^ { n - 1 }$ may be computed from A1 by repeated plus-min multiplications. By substituting plus for multiplyand min for plus, $\lceil \log n \rceil$ matrix multiplications are sufficient to generate the matrices $\mathbf { A } ^ { 2 }$ ， $\mathbf { A } ^ { 4 } , \ldots , \mathbf { A } ^ { n - 1 }$ Recall thatasinglematrixmultiplicationhas complexity $O ( \log n )$ on the hypercube SIMDand shuffle-exchange SIMD models, given $n ^ { 3 } = 2 ^ { 3 q }$ procesors.Thus theal-pairs shortest-path problemcan be solved in (log²n) time on the hypercube SIMD and shuffle-exchange SIMD models, given $n ^ { 3 } = 2 ^ { 3 q }$ processors.

# 12.4 SINGLE-SOURCE SHORTEST PATH

In a single-source shortest-path problem we must find the shortest path from a specified vertex s, the source, to all other vertices in a weighted, directed graph.Let weight $( u , v )$ represent the length of the edge from $u$ t0 $v$ if no such edge exists, then weighi $( u , v ) = \infty$

![](images/eabcbf7f94139aa7ea192f30826c810c716ea0307f831267d2c46ae310796436.jpg)  
FIGURE 12-5 Execution of Moore's single-source, shortest path algorithm.

A sequential algorithm, developed by Moore (1959), solves this problem (see Fig. 12-5). In Moore's single-source shortest-path algorithm, distance(v) is initially assigned the value $\infty$ ,for all $v \in V - \{ s \}$ . The distance from $s$ to itself is,of course, zero.Aqueue contains vertices from which further searching must be done; initially it contains $s$ . As long as the queue remains nonempty, thevertex $u$ from the head of the queue is removed, and all edges $( u , v ) \in E$ are examined. If distanc $\varrho ( u ) + w e i g h t ( u , v ) < d i s t a n c e ( v )$ , a new shorter path to v has been found (through $u$ ).In this case distance $( \upsilon )$ is revised and $v$ is added to the tail of the queue, if it is not already in the queue. The algorithm continues this process until the queue is empty. Moore's algorithm is shown in Fig. 12-5.

Procedure INiTiALiZE, called in line 3 of Fig. 12-6, initializes the distance of every nonsource vertex to $\infty$ and the distance of $s$ to zero. The for loop in lines 12 to 2O corresponds to the search for shorter paths to vertices directly reachable from vertex $u$

# SHORTEST PATH (SISD):

Parameter n {Number of vertices in graph}   
Global distance {Element i contains distance from $s$ to i} S {Source vertex) weight {Contains weight of every edge]

1. begin   
2. for $i \gets 1$ to $_ n$ do   
3. INITIALIZE(i)   
4. endfor   
5. insert $s$ into the queue   
6. while the queue is not empty do   
7. SEARCH()   
8. endwhile   
9.end

SEARCH(): Local "new.distance {Distance to u if pass through u} $\boldsymbol { n }$ {Examined edge leaves this vertex} $\boldsymbol { v }$ {Examined edge enters this vertex]   
10. begin   
11. dequeue vertex $u$   
12. for every edge $\{ u , v \}$ in the graph do   
13. new.distance distance(u) + weight({u,v})   
14. if new.distance $<$ distance(v) then   
15. distance $( v ) $ new.distance   
16. if $v$ is not in the queue then   
17. enqueue vertex $v$   
18. endif   
19. endif   
20. endfor   
21.end

This algorithm is amenable to parallelization. There are two methods to consider. The first makes the for loop in lines 12 to 20 parallel. Any given vertex is likely to have several outgoing edges and could all be explored in parallel.The second method is to paralelize the while loop in lines 6to8.At any time in the execution of the algorithm, there are probably many vertices in the queue. It should be possible to explore edges from more than one vertex at a time. Which method is better? There are at least two reasons to favor the second method. First, the second method produces larger-grained tasks for the processes to perform, thus,by Design Strategy 5 it would be more likely to produce reasonable speedup. Second, the parallelizability of the first method is limited by the number of edges leaving each vertex. If the graph is relatively sparse,i.e.relatively few edges per vertex,the number of processes that can be used is too constrained.

Consider the following parallel algorithm,based on the second method described.The queue is initialized with thesource vertex,thenanumberof asynchronous processes are created. Each of these processes completes the steps of deleting a vertex from the queue, examining its outgoing edges, and inserting vertices with shorter paths into the queue.

The for loop in lines 2 to 4 of the sequential algorithm is easily transformed to a parallel for loop by using the prescheduling method. The parallel for loop occupies lines 2 to6of the paralel algorithm shownin Fig.12-8.The while loop of lines 6 to 8 of the sequential algorithm must be changed toreflect the existence of a number of asynchronous processes performing the SEARCH procedure in parallel. Clearly it is not appropriate for a process to terminate when it discovers that the queue is empty. (Why?) Hence a more complicated method must be used. In the following algorithm two variables are used together to determine when there is no more work todo.The first variable,waiting,is an array that keeps track of processes waiting for work. The second variable, the boolean halt,is set to the value true only when allthe processesare waiting and the queue is empty. Procedure INITIALIZE initializes every entry in array waiting to false.Lines 6 to 8 of the sequential algorithm become lines 8 to 11 of the parallel algorithm.

How must the SEARCH procedure be modified? Because enqueuing and dequeuing are not atomic operations, the queue must be locked whenever an element is enqueued or dequeued. Second,beforea process compares the newly found distance tovertex v,new.distance,to the current shortestdistance to $v$ ， distance(v),variable distance(v) must be locked.Otherwise,both processes could find themselves trying to update distance(v) simultaneously,resulting in the wrong value (see Fig. 12-7).Finally, if a process finds that the queue is empty,it sets its entry in array waiting to true.If process 1 is waiting,then it checks to see whether every process is waiting. If every process is waiting,the value of halt is set to true.Notice that the queue must be locked while process 1 checks to see if every process is waiting. The parallel algorithm appears in two parts in Figs. 12-8 and 12-9.

How much speedup can be achieved by this algorithm? Initially, creating more processes decreases the total execution time of the algorithm, because the outgoing edges of several vertices can be examined in parallel. However, since each process demands exclusive control of the queue to insert or delete vertices, maximum speedup is eventually constrained.

Design Strategy 8 Change data structures to reduce the amount of contention for thesame shared resource.

There would be no contention between the processes if each process maintained a private list of vertices to be searched,inserting and deleting elements

![](images/9815b65871e22782c145f3fc2b44383e4fcc98bce5c90cf51c6b528a1e1906bc.jpg)  
FIGURE12-7 If locking is not used,two processes may attempt to update the value of distance(v) simultaneously,causing anerror.

<table><tr><td rowspan=1 colspan=1>Current value of distance (9)</td><td rowspan=1 colspan=1>Process1</td><td rowspan=1 colspan=1>Process2</td></tr><tr><td rowspan=1 colspan=1>28282828282224</td><td rowspan=1 colspan=1>Dequeue vertex 4Consider edge (4,9)new.distance 22new.distance &lt; distance (9)distance(9)22..</td><td rowspan=1 colspan=1>Dequeue vertex 7Consider edge (7, 9)new.distance 24new.distance &lt; distance (9).distance (9)24.</td></tr></table>

FIGURE12-8 Parallel version of Moore's single-source shortest pathalgorithm,suitable for implementation on a UMA multiprocessor.

# SHORTEST PATH (UMA MULTIPROCESSOR):

Parameter n {Number of vertices in graph} $p$ {Number of processes} Global distance {Element i contains distance from s to vertex i} halt {Set to true when it is time for processes to stop) s {Source vertex} weight {Contains weight of every edgel] 1. begin 2. for all $P _ { i }$ where $1 ~ \leq ~ i ~ \leq ~ p$ do 3. for $j \gets i$ to $_ n$ step $p$ do 4. INITIALIZE(j) 5. endfor 6. endfor 7. enqueue $s$ 8. halt false 9. for all $P _ { i }$ where $1 ~ \leq ~ i ~ \leq ~ p$ do 10. repeat SEARCH (i) until halt 11. endfor 12.end

SEARCH (i): Value i {Process number} Local new.distance {Distance to v if go through u) u {Vertex edge leaves] $v$ {Vertex edge enters)   
1.begin   
2. lock the queue   
3. if the queue is empty then   
4. waiting ${ \bf \Xi } ( i ) \gets$ true   
5. if $i \ = \ 1$ then   
6. halt waiting(2) and waiting(3)and...and waiting $( p )$   
7. endif   
8. unlock the queue   
9. else   
10. dequeue $\pmb { u }$   
11. waiting ${ \bf \Xi } ( i ) \gets$ false   
12. unlock the queue   
13. for every edge $\{ u , v \}$ in the graph do   
14. new.distance distance(u) + weight({u,u})   
15. lock (distance $( v )$ ）   
16. if new.distance $<$ distance(v) then   
17. distance $( \upsilon ) \~ $ new.distance   
18. unlock ( distance(v))   
19. if $v$ is not in the queue then   
20. lock the queue   
if v is not in the queue then enqueue $v$ endif unlock the queue endif else unlock (distance(u) endif   
28. endfor   
29. endif   
30.end

on its own. If the variance in the size of these lists were large, however, then letting each process handle its own list could cause a severe imbalance in the workloads. A middle course is to let each process insert elements into its own private space, then join these lists,so that deletions can occur by leting each of the $p$ processes examine every $p$ th element of the combined list,baancing the work done by each process (Fig. 12-10).

The linked array is a data structure designed to allow the joining of varioussized lists so that the inserting and searching of list elements are done in

![](images/d4e311a972672738ed47ac4a5c650750cf957035be8ea8457ffafa3ebde5eb4e.jpg)

![](images/e20f33ea3a5278c45f1b8cb6c1a606f73c33dce6ec252f2083ba25b78a265b22.jpg)  
Each processordeletes every $p$ th element.Noconflicts.

FIGURE 12-10 Logical form of linked array.

parallel without contention (Quinn 1983; Quinn and Yoo 1984). Assume that in a single iteration no processor ever inserts more than $w$ elements. The linked array,inthat case,contains $p ( w + p )$ elements, $w + p$ elements per process. In contiguous group of $w + p$ locations a process may store the names of elements to be searched in the next iteration. If processor i, $1 \ \leq$ $i \ \leq \ p$ ，generates the names of $e _ { i }$ elements to be considered in the next iteration, then locations $( i - 1 ) ( w + p ) + 1$ through $( i - 1 ) ( w + p ) + e _ { i }$ contain these names. Locations $( i - 1 ) ( w + p ) + e _ { i } + 1$ through $( i \mathrm { ~ - ~ } 1 ) ( w + p ) +$ $e _ { i } + p$ contain the values $- i ( w + p + 1 )$ down to $- [ i ( w + p ) + p ]$ ,respectively.

In the next iteration, when the elements with names in the linked array are to be examind,procr $i$ ， $1 \leq i \leq p$ ,examines every pth location, beginning with location $i$ .If the value encountered is greater than zero,that is the vertex to be searched. If the value is less than zero,it isa pointer,and the processor immediately jumps to the index indicated (the absolute value).When the pointer has value less than $- p ( w + p )$ , the search terminates.

Theorem 12.10. Given a set of n elements stored in a linked array and p ≥ 1 processors,the diference between the greatest number of elements searched by any processor and the least number of elements,is less than or equal to 1 (Quinn 1983).

Proof.This is left to the reader.

Procedure EXAMiNE in Fig. 12-11 illustrates how a process removes its share of elements from an array containing vertex numbers and pointers.

The space overhead of linked arrays can be high. Unlessit can be guaranteed that not all the insertions will be done by a single processor, then the space allocated to the linked array must be approximately p times the space allocated to a simple array.A data-parallel version of Moore’s algorithm can be devised to use the linked array. In a single iteration each process has a number of vertices to examine. Every process compiles its own list of vertices to which

EXAMINE $( a , i , p , w )$ ：

Value $a [ 1 . . p \times ~ ( w + p ) ] ,$ {Array containing vertex numbers and pointers i， {Process number} $p$ ， {Number of processes) $w$ {Size of subarray allocated to each process) Local $j$ {Index into a} 1. begin 2. $j \gets i$ 3. while $j ~ \le ~ p ~ \times ~ ( w + p )$ do 4. if $a [ j ] ~ < ~ 0$ then 5. $j \gets - a [ j ]$ {Follow pointer) 6. else 7. manipulate vertex whose value is $a [ j ]$ 8. $j ~  ~ j ~ + ~ p$ 9. endif 10. endwhile 11.end

shorter paths have been found and builds links to the next process's list. In the next iteration these lists are examined in parallel. Two arrays are used. In any iteration one array is being read while the other array is being writen. In the next iteration the roles of the two arrays are reversed.

Quinn and Yoo (1984) have compared the speedup achieved by a linkedarray version of Moore's algorithm with the speedup achieved by a sequential deque version of Pape-d'Esopo's algorithm (a variant of Moore's algorithm that uses a double-ended queue, or deque) on a UMA multiprocessor. Processes executing this new algorithm must spend time traversing links and synchronizing with each other,adding to the overhead of the algorithm. Thus the slope of the speedup curve is less than that of the asynchronous parallel algorithm that uses the sequential deque. However, the problem of excess contention for a shared data structure is eliminated in this algorithm,and the maximum speedup achieved is higher.

# 12.5 MINIMUM-COST SPANNING TREE

Determining the minimum-cost spanning forest of a weighted graph is a simple variation of determining connected components. At each iteration the minimum edge,rather than the minimum labeled vertex,is found. Hence,similar complexity results exist for the minimum-cost spanning forest problem. For example, consider Theorem 12.11.

Theorem 12.11. Suppose the weight matrix of a weighted, undirected graph G with n vertices is stored in the base of a pyramid SIMD computer of size n2. Then the minimum-cost spanning forest of G can be found in time O(√n) (Miller and Stout 1986).

If the graph is connected, the minimum-cost spanning forest is a single tree.Efforts to find the minimum-cost spanning tree of a weighted, connected, undirected graph have focused on three classical sequential algorithms: Sollin's (1977) algorithm,the Prim-Dijkstra algorithm (Prim 1957; Dijkstra 1959), and Kruskal’s (1956) algorithm.Next we will discuss parallel algorithms based on Sollin's algorithm and Kruskal’s algorithm.

# 12.5.1 Sollin's Algorithm

The most obvious candidate for investigation is a sequential algorithm attributed to Sollin. In this algorithm we start with a forest of $n$ isolated vertices, with every vertex regarded as a tree. In an iteration, the algorithm determines for each tree the smallest edge joining that tree to another tree. All such edges are added to the forest, except that two trees are never joined by more than one edge. (Ties between edges,which would cause a cycle,are resolved arbitrarily.） This process continues until there is only one tree in the forest-the minimum-cost spanning tree. Since the number of trees is reduced by a factor of at least 2 in each iteration,Sollin's algorithm requires at most $\lceil \log n \rceil$ iterations to find the minimum-cost spanning tree. An iteration requires at most $O ( n ^ { 2 } )$ comparisons to find the smallest edge incident on each vertex. Thus the sequential algorithm has complexity $O ( n ^ { 2 } \log { n } )$ . Sollin's algorithm is illustrated in Fig.12-12. Pseudocode for the algorithm appears in Fig. 12-13. Note that this algorithm uses sets to keep track of which vertices are in which trees. The FIND function, passed a te $v$ ,returns the name of the set (tree) v is in. The procedure UiON, passed two vertices $v$ and $w$ ,performs the set union of the sets containing $v$ and $w$ ; in other words,itconnects the trees containing vertices v and $w$ .Hopcroft and Ullman (1973) showed how these two operations can be performed extremely eficiently. Readers unfamiliar with these two operations can find descriptions in the above-mentioned reference or in a variety of texts on algorithms, including Aho et al. (1974).

How should this algorithm be parallelized for the UMA multiprocessor model?According to Design Strategy 5,parallelization should be done on the outermost loop possible. Unfortunately，we cannot make the while loop parallel, because there are precedence constraints between iterations.Each of the trees existing on iteration $i$ must be joined with the nearest tree before iteration $i + 1$ can begin. Hence parallelization must be done inside the while loop.Lines 7 to 9 can be made paralel through the prescheduling method; each processor is responsible for $1 / p$ of the trees.The for loop in lines 10 to 17 can also be made paralel through prescheduling.This is most efficiently done byassigning eachprocessoritsfairshareofthevertices,thenallowingit to examine every outgoing edge from this set.

![](images/0e6959c7218b7387e435daccefb88ca7d3e390327cf5ede55e0a50c8e91a9a9f.jpg)  
FIGURE 12-12 Sollin's minimum-cost spanning tree algorithm.

Parallelizing the loop in lines 18 to 24 is more complicated. The complicating situation is illustrated in Fig. 12-14. Suppose one processor is attempting to connect tree $A$ with its closest neighbor $B$ ,whileanoterprocessorisattemting to connect tree $B$ with its closest neighbor $A$ .Variable edge[A] contains edge $\{ v _ { A } , w _ { A } \}$ with length $k$ Variable $e d g e [ B ]$ contains edge $\{ v _ { B } , w _ { B } \}$ ,also with length $k$ If both processors perform the test in line 20 before either processor performs the UNiON operation in line 22, then both edges will be added to $T$ ， an error. Therefore,if the loopin lines18 to 24is to bemade paralel, trees $\mathsf { F l N D } ( v )$ and $\mathsf { F l N D } ( w )$ must be locked before line 20 and unlocked after line 23,since we canallow only one processor at a time tooperate in this critical section. Given that only one tree can be locked at a time, we must be careful to avoid deadlock. One way to prevent this is to lock the lower-numbered tree first.

Theorem 12.12. The parallel version of Solin's algorithm already described has complexity $O ( \log n ( n ^ { 2 } / p + n / p + n + p ) )$

Proof. A series of $n$ UNION and FIND operations has worst-case time complexity $O ( n \log ^ { * } n )$ : the time spent per individual operation amortizes to $O ( \log ^ { * } n )$ ,virtually a constant. Hence we make the simplifying assumption that UNiON and FIND are constant-time operations. The parallelization of the for loop in lines 7 to 9 has

Parameter n {Number of vertices}   
Global closest[] {Distance of closest tree} edge[] {Edge connecting tree with closest tree} i $T$ {Minimum-cost spanning tree} $v , w$ {Endpoints of edge under consideration} weight[] {Contains edge weights}

1. begin   
2. for $i \gets 1$ to $n$ do   
3. Vertex $i$ is initially in set i   
4. endfor   
5. $T \gets \emptyset$   
6. while $\vert T \vert ~ < ~ n - 1$ do   
7. for every tree $i$ do   
8. closest[i] $ \infty$   
9. endfor   
10. for every edge $\{ v , w \}$ do   
11. if $\mathsf { F I N D } ( v ) \neq \mathsf { F I N D } ( w )$ then   
12. ifweight $[ \{ v , w \} ] <$ closest $[ \mathsf { F I N D } ( v ) ]$ then   
13. $c l o s e s t [ \mathsf { F I N D } ( v ) ] \gets \mathsf { w e i g h } t [ \{ v , w \} ]$   
14. $e d g e [ \mathsf { F I N D } ( v ) ] \gets \{ v , w \}$   
15. endif   
16. endif   
17. endfor   
18. for every tree i do   
19. $( v , w ) $ edge[i]   
20. if $\mathsf { F I N D } ( v ) \neq \mathsf { F I N D } ( w )$ then   
21. ${ \cal T } ~  ~ { \cal T } ~ \cup ~ \{ ( v , w ) \}$   
$\mathsf { U N I O N } ( v , w )$   
23. endif   
24. endfor   
25. endwhile   
26.end

FIGURE 12-13 Sequential version of Solin's minimum-cost spanning tree algorithm.

![](images/1c621ce29a583186c65268de8d1aea7e63dc88a9708fe297701a2afa4e2207d8.jpg)  
FIGURE 12-14 A complication that arises in the parallelization of Sollin'sminimumcost spanning tree algorithm.