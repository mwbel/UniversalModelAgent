![](images/f4f6e88257478f0fc4e05a90b0365c7881e3aeb76644cea5a31c248538640ce7.jpg)  
FIGURE 12-15 Speedup of a parallel implementation of Sollin'salgorithmona Sequent Symmetry,givena $3 5 0 \times 3 5 0$ grid graph (Barr et al. 1989).

complexity $O ( n / p + p )$ .The paralelization of the for loop in lines 10 to 17 has complexity $O ( n ^ { 2 } / p + p )$ .Theparallelizationof theforloopin lines18to 24has complexity $O ( ( n / p ) p + p )$ .The factor of $p$ in the last Ioop occurs because in the worst case, a processor wanting to lock a particular tree $A$ may have to wait for every other processor to lock and unlock A.Remember that the outer while loop executes at most [logn] times. The overall complexity of the parallel version of Sollin'salgorithm,this $O ( \log n ( n ^ { 2 } / p + n / p + n + p ) )$

The complexityof this parallel algorithm is minimized when $p = O ( { \sqrt { n } } )$ If $p \ll n$ ,we can expect the parallel algorithm to achieve good speedup.

Barr et al. (1989) have implemented a parallel version of Sollin's algorithm on the Sequent Symmetry.Figure 12-15 illustrates the speedup achieved by their algorithm on a $3 5 0 \times 3 5 0$ vertex grid graph (where the verticesandedges form a 2-D mesh without wraparound connections).

# 12.5.2 Kruskal’s Algorithm

In Kruskal’s algorithm initially the graph consists of a forest of isolated vertices.The edges are scanned in increasing order of their weights,and every edge thatconnects two disjoint trees is added to the minimum-cost spanning tree. (In other words,all edges that do not cause cycles with previously selected edges are selected.) The algorithm halts when the graph consists of a single tree, a minimum-cost spanning tree. Figure 12-16 illustrates Kruskal's algorithm.

Lemma 12.1. A UMA multiprocessor with $\lceil \log m \rceil$ processors can remove an element from an $m$ -element heap in constant time (Yoo 1983).

![](images/e6b464458eb10bb360eae84329285dedcdff84d41fb5469c3dba1fe220ecaece.jpg)  
FIGURE 12-16 Kruskal's minimum-cost spanning tree algorithm.

![](images/88c3eba215c9eee7dc82ef97e42e4c90d0a4db93f296b8a94e3e6749f0cb8be3.jpg)  
FIGURE 12-17 Yoo's pipelined algorithm to empty heap (Quinn and Deo 1984).

Description of Algorithm. This pipelined algorithm is illustrated in Fig. 12-17. An array is used to implement the heap in the usual way,with the root of the heap being stored in the first element and the left and right children of node $i$ being stored in elements $2 i$ and $2 i + 1$ .The heap is a full binary tree with $p$ levels, $p$ being the number of processors. Some nodes in the bottom level of the tree are assigned the value $\infty$ ，if necessary， to fill the tree. During the course of an algorithm's execution,a nodeis full if itcontains a value (including $\infty$ ).A node is empty if its value has been transmited to its parent and no replacement value has been received from any of its children. The array flag indicates what levels contain an empty node; $f l a g \left( i \right) = e m p t y$ if level $i$ has an empty node,otherwise $\begin{array} { r } { f l a g \left( i \right) = f u l l } \end{array}$ If $f l a g ( i ) = e m p t y$ , then empty_node(i) indicates which node is empty. For all $i$ ， where $2 \leq i \leq p$ ,processor $i$ is assigned the task of keeping all the nodes at level $i - 1$ full. If $\mathcal { H } a g ( i - 1 ) = e m p t y$ and $\begin{array} { r } { f l a g ( i ) = f u l l } \end{array}$ ,then processor $i$ fills the empty node at Ievel $i - 1$ with the appropriate child at level $i$ .Then $\begin{array} { r } { f l a g ( i - 1 ) } \end{array}$ becomes full, and $\it { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm { \Omega } \mathrm  \Omega \mathrm { \Omega } \mathrm { \Omega } \mathrm \mathrm { \Omega } \mathrm { \Omega \Omega } \mathrm  \mathrm \Omega \mathrm { \Omega } \mathrm { \Omega } \mathrm \mathrm { \Omega \Omega } \mathrm \mathrm  \Omega \mathrm \Omega \mathrm { \Omega } \mathrm \mathrm { \Omega \Omega } \mathrm \mathrm \mathrm  \Omega \Omega \mathrm \Omega \mathrm \Omega \mathrm { } \mathrm \mathrm \mathrm  \Omega \Omega \Omega \mathrm \Omega \mathrm \mathrm \Omega \mathrm \mathrm { \Omega \Omega \Omega } \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm  \Omega \Omega \Omega \mathrm \mathrm \Omega \mathrm \mathrm \mathrm \mathrm \mathrm  \Omega \Omega \Omega \Omega \mathrm \mathrm \Omega \mathrm \Omega \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \Omega \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm  \Omega \Omega \Omega \Omega \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \Omega \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm $ becomes empty. When a leaf node is emptied, it is filled with an $\infty$ Eventually the $\infty$ 's fill the tree. Processor 1 empties node 1 whenever it is full and terminates the procedure when node 1 has the value $\infty$ (i.e., when the heap is empty).

Yoo has alsodescribeda parallel method forinitializing a heap.Thecommon sequential algorithm is described in Fig. 12-18.

Parameter $^ { d }$ {Depth of heap)   
Global $k , v , w$ {Particular heap elements) $k e y \{ 1 . . . ( 2 ^ { d + 1 } - 1 ) \}$ (The heap) l {Level number}

1. begin   
2. for $l  d - 1$ downto 0 do   
3. for each nonleaf node $v$ at level $\mathbf { \xi } _ { l }$ do   
4. $k \gets$ key[u]   
5. repeat   
6. $w ~ $ child of $v$ with the smaller key   
7. if $\begin{array} { l } { k \ > \ k e y [ \omega ] } \end{array}$ then   
8. $k e y [ \boldsymbol { v } ] ~  ~ k e y [ \boldsymbol { w } ]$   
9. $\ v \  \ w$   
10. else   
11. exit loop   
12. endif   
13. until $v$ is a leaf node   
14. $k e y [ \upsilon ] \ \gets \ k$   
15. endfor   
16. endfor   
17.end   
Seauential algorithm for

The for loop in lines 3 to 15 can be made parallel in a straightforward manner by using prescheduling; each processor makes its share of the nonleaf nodes into heaps at level l. A better method is to allow heap construction to occur at a node once both its children have been made into heaps (Yoo 1983). This method eliminates the requirement that processors synchronize as they reach the end of every level.

Theorem 12.13. The minimum-cost spanning tree of a weighted, undirected, connected graph with $_ { m }$ edges can be found in time $O ( m )$ on a UMA multiprocessor with $\lceil \log m \rceil$ processors (Yoo 1983).

Summary of Algorithm. The first step is to make a heap out of the edges of the weighted graph,based ontheir lengths.Inthesecond step,asingle procesepeat edly removes an edge from the heap and determines whether it is an element of the minimum-cost spanning tree, while the remaining processes repeatedly restore the heap.Recall that the edge is an element of the minimum-cost spanning tree if it connects two unconnected subtrees.Determining whether an edge connects two unconnectedreesdifsrytig ereb in virtually constant time by using the effcient FiNDand UNiON algorithms described earlier. The pipelined processes emptying the heap can provide a new edge in constant time. Since the heap contains $m$ edges,the worst-case time complexity is $O ( m )$ ，

Several graph algorithms have been presented in this chapter. Three parallel graph-searching algorithms were defined,and their complexity was analyzed for the CREW PRAM model. Many algorithms appear to solve the connected components problem. Most of these algorithms are related to Hirschberg's algorithm, which uses the vertex-collapsing approach.

Variants of matrix multiplication can be used to solve a variety of graph theoretic problems. We showed how to modify Dekel's parallel matrix multiplication algorithm to solve the all-pairs shortest-path problem (Dekel et al. 1981).

Implementation of a variant of Moore's algorithm to solve the single-source shortest-path problem illustrates two important ideas (Deo et al. 1980). First, contention for a single resource-a queue-severely impairs the speedup achievable by their algorithm on a UMA multiprocessor. Second, implementing halting conditions for asynchronous algorithms is not always a straightforward task.Another single-source shortest-path algorithm, based on the linked array concept, eliminates the resource contention problem. Being data-parallel, rather than asynchronous, the improved algorithm also has a cleaner halting condition. Replacing the queue with the linked array is an example of parallel algorithm Design Strategy 8: Change data structures to reduce the amount of contention for the same shared resource.

We examined parallelizations of two minimum-cost spanning tree algorithms for UMA multiprocessors.Sollin's algorithm has a straightforward parallelization.Kruskal’s algorithm also has an effcient parallelization for a small number of processors, because it is possible to pipeline the initialization and the emptying of a heap.

# 12.7 BIBLIOGRAPHIC NOTES

A more detailed description of graph theoretic terms can be found in numerous texts: Harary (1969); Deo (1974);Reingold et al. (1977). Moitra (1987) and Quinn and Deo (1984) have surveyed parallel graph algorithms.

Reif (1985) proved that the problem of finding a depth-first search tree of a general graph is $\mathcal { P }$ -complete. Aggarwall and Anderson (1988) and Aggarwall et al. (1990) published $\mathcal { R N C }$ algorithms for computing depth-first search trees in undirected and directed graphs,respectively. Deterministic algorithms for depth-first search have been described by Aggarwal et al. (199O), Chaudhuri (1990), Goldberg et al. (1988),and Hagerup (1990). Tiwari (1986) has explored the related problem of finding the depth-first spanning tree of a graph with a specified root, given the depth-first spanning tree of the same graph with a different root.

A parallel breadth-first PRAM search algorithm different from the one described in this chapter has been devised by Alton and Eckstein (1979).

Most connected compbnents algorithms in the literature use Hirschberg's approach of collapsing vertices. A number of graph problems are related to the connected components problem, including finding weakly connected components and strongly connected components in a digraph, finding lowest common ancestors,finding articulation points,finding biconnected and k-connected components, and planarity testing. References to connectivity-related algorithms in the literature include Attalah (1983); Attalah and Kosaraju (1982); Belkhale and Banerjee (1992); Cole and Vishkin (1986); Cypher et al. (1990); Eckstein (1979a); Doshi and Varman (1987); Fussell and Thurimella (1988);Fussell et al.(1989); Guibas et al. (1979); Hambrusch (1982,1983); Han and Wagner (1990); Kanevsky and Ramachandran (1987); Khuller and Schieber (1991); Kosaraju (1979); Levialdi (1972); Levit and Kautz (1972); Lipton and Valdes (1981); Miller and Reif (1991); Miller and Stout (1985a,1987);Nassimi and Sahni (1980b); Nath and Maheshwari (1982); Reghbati and Corneil (1978); Reif (1982); Reif and Spirakis (1982); C. Savage (1977, 1981); Savage and Ja'Ja’ (1981); Shiloach and Vishkin (1982a); Shyu (199O); Tsin and Chin (1984); Tarjan and Vishkin (1985); vanScoy (1976);Wyllie (1979),andYang etal.(1990).

Lin and Olariu (1992), Schieber and Vishkin (1988),and Tsin (1986) have presented algorithms to solve the lowest common ancestor problem.

Browning (1980a, 1980b) has designed multicomputer algorithms that use an exponential number of processors to solve the maximum clique, color cost, and traveling salesperson problems.

Dekel and Sahni (1982) have developed an EREW PRAM algorithm to find the maximum matching of a convex bipartite graph.

Determining the minimum-cost spanning forest of a graph can be seen as a simple variation of determining connected components.At each iteration the minimum edge, rather than the minimum labeled vertex,is found. Hence it is not surprising that Chin et al. (1982) have modified Hirschberg’s algorithm to solve the minimum-cost spanning tree problem by using the CREW PRAM model. Deo and Yoo (1981) have implemented parallelizations of Kruskal’s, Sollin's, and Prim-Dijkstra's minimum-cost spanning tree algorithms on the Denelcor HEP. They report that Cheriton and Tarjan's (1976) minimum-cost spanning tree algorithm, when parallelized,is identical to the parallel version of Sollin's algorithm. Other references to parallel minimum-cost spanning tree algorithms in the literature include Bentley (1980);Atallah (1983); Atallah and Kosaraju (1984);Doshi and Varman (1987); Hambrusch (1982); Hirschberg (1982);Kucera (1982);Levit and Kautz (1972)；Reif (1982);and Savage (1977).

A number of papers describe parallel graph algorithms for hypercube multicomputers.Das et al. (199Oa) present a variety algorithms,including algorithms for checking bipartiteness,finding a spanning forest,and determining connected components.Das et al. (199ob) describe two algorithms to solve the minimumcost spanning forest problem. Sheu et al. (1990) give algorithms for breadth-first search, depth-first search,and maximum matching in a bipartite graph.

Crane (1968) has proposed a paralel single-source shortest-path algorithm for use on an associative processor. Other shortest-path algorithms in the literature and not already described in this chapter include those by Ahuja et al. (1990); Arjomandi (1975); Driscoll et al. (1988); El-Horbaty and Mohamed (1992); Ghosh and Bhattacharjee (1986); Gu and Takaoka (199O); Kucera (1982); Levitt and Kautz (1972); Mateti and Deo (1981); and Price (1982, 1983).

Shiloach and Vishkin (1982b) have developed a parallel algorithm for finding the maximum flow ina directed, weighted graph. Their algorithm is based upon the usual layered network approach. Chen and Feng (1973) and Chen (1975) discuss parallel algorithms for the maximum-capacity path problem.

PRAM algorithms for the maximum independent set problem have been proposed by Goldberg and Spencer (1989) and Karp and Wigderson (1985), and Luby (1986).

Chandrasekharan and Sitharama Iyengar (1988) and Naor et al. (1989) discuss parallel algorithms for chordal graphs.

Parallel algorithms for the stable-marriage problem have been discussed by Hull (1984), Quinn (1985), and Tseng and Lee (1984b).

# 12.8 PROBLEMS

12-1 Ilustrate the search trees resulting from $p$ -depth search,parallel breadth-depth search, and parallel breadth-first search of the graph in Fig. 12-19. Assume the following: $p = 3$ ,the search begins at vertex 1,and adjacent vertices are always explored in increasing order of the vertex numbers.

![](images/c77b7c77c0bb8a8a1d4f5815a55426522e374bdf08cbff281c4d0dfaff2b5244.jpg)

12-6 In the parallel version of Moore's algorithm for the UMA multiprocessor model, why is it not appropriate for a process to terminate when it discovers that the queue is empty?   
12-7 Explain why the queue must be locked when process 1 examines the status of the array waiting in the UMA multiprocessor version of Moore's algorithm.   
12-8 Explain why the test to see if v is in the queue must be repeated on line 21 of Fig.12-9. Recode lines 19-25 so that there is no need to repeat the test. Under what circumstances will the new version execute faster than the version shown in this book?   
12-9 Prove Theorem 12.10.   
12-10\* Use of a linked array is one way to avoid the shared-data structure contention problem encountered by the parallel single-source shortest-path algorithm using a single queue (Deo et al. 1980). Devise a parallel single-source shortest-path algorithm by using another data structure that avoids (or at least reduces) contention.   
12-11 Why is the number of trees in Sollin's algorithm reduced by at least a factor of 2 every iteration?   
12-12 Give an example of a graph in which Solin’s algorithm requires only a single iteration to produce a minimum-cost spanning tree.   
12-13 Give an example of a graph in which Sollin’s algorithm requires flogn] iterations to produce a minimum-cost spanning tree.   
12-14 Write a parallel version of Sollin's algorithm for the UMA multiprocessor model.   
12-15 Explain how Yoo's parallel heap-emptying algorithm can be modified if p < $\log m$ processorsare available.

# 13

Attempt the end,and never stand tooubt; Nothing'sso hardbutsearch willfind it out

Robert Herrick,"Seek and Find,” Hesperides

Combinatorial algorithms perform computations on discrete, finite mathematical structures (Reingold et al. 1977).Combinatorial search is the process of finding “one or more optimal or suboptimal solutions in a defined problem space”(Wah et al. 1985),and has been used for such problems as laying out circuits in VLSI to minimize the area dedicated to wires, finding traveling salesperson tours, theorem proving,and game playing.

Chapter 13 surveys the paralelization of divide-and-conquer, branch-andbound,andalpha-betasearchalgorithms.Section13.1discusses thethre kinds of search trees that arise from combinatorial optimization algorithms. Section 13.2 summarizes parallel methods to solve divide-and-conquer problems. Section 13.3 introduces the branch-and-bound algorithm, using the 8-puzzle as an example. The section ends by describing a well-known algorithm to solve the traveling salesperson problem. In Sec. 13.4 we present parallelizations of the branch-and-bound algorithm for multiprocessors and multicomputers. We also show how parallel branch-and-bound algorithms can exhibit anomalous behavior that sometimes results in superlinear speedup. Section 13.5 contains an overview of the sequential alpha-beta algorithm, commonly used to search game trees,and Sec. 13.6 describes methods used to parallelize the alpha-beta search algorithm.

There are two kinds of combinatorial search problems. An algorithm to solve a decision problem must find a solution that satisfies all the constraints. An algorithm that solves an optimization problem must also minimize (or maximize) an objective function associated with solutions. All examples of combinatorial search in this chapter are optimization problems.

A search problem can be represented by a tree. The root of the tree represents the initial problem to be solved. The nonterminal nodes are either AND nodes or OR nodes.An AND node represents a problem or subproblem that is solved only when all its children have been solved; an OR node represents a problem or subproblem that is solved when any of its children has been solved. Every nonterminal node in an AND tree is an AND node (Fig. 13-1a). The search tree corresponding to a divide-and-conquer algorithm is an AND tree, since the solution toa problem is found by combining the solutions to allits subproblems. Every nonterminal node in an OR tree is an OR node (Fig. 13-1b). Branchand-bound algorithms yield OR trees, since the solution to a problem can be found by solving any of its subproblems. An AND/OR tree is characterized by the presence of both AND nonterminal nodes and OR nonterminal nodes (Fig. 13-1c). Game trees are examples of AND/OR trees.

![](images/8d3e0bfef3a2968de345f75a93185986a19a540cd7de46dc580fa5348c7aef7b.jpg)

# 13.2 DIVIDE AND CONQUER

Divide and conquer is a problem-solving methodology that involves partitioning a problem into subproblems, solving the subproblems,and then combining those solutions into a solution for the original problem. The methodology is recursive; that is, the subproblems themselves may be solved by the divideand-conquer technique. The odd-even reduction algorithm in Chap. 9 and the quicksort algorithm of Chap. 10 are examples of the divide-and-conquer technique.

The divide-and-conquer problem solution can be represented by an AND tree, since the solution toany problem represented byan interior node requires the solution of allits subproblems,represented by the children of that node. In other words,every node in the tree must be examined.

Three ways of executing divide-and-conquer algorithms on MIMD computers have been proposed. The first method is to build a tree of processors that corresponds to the search tree. This method has two disadvantages: The root processorcan become abottleneck,sinceit is theconduit forall input and output; and any particular processor tree, having a fixed interconnection structure, is appropriate for only some divide-and-conquer algorithms. A second method is to use a virtual tree machine that has a robust interconnection network, such as a multicomputer with a hypercubic processor organization. Since the virtual links between problems and subproblems may not be actualized by physical links, we need a good algorithm to map subproblems to processors in order to minimize communication times. The third method suggests using UMA multiprocessors to execute divide-and-conquer algorithms. The shared global memory facilitates access to subproblems by the various processes.

The parallel search of an AND tree can be divided into three phases. In the first phase problems are divided and propagated throughout the parallel computer. For most of the first phase there are fewer tasks than processors,and processors idle until they are given a problem to divide and propagate. In the second phase all the processors stay busy computing. In the third phase there are again fewer tasks than processors, and some processors combine results while other processors idle. Hence the maximum speedup achievable is limited by the propagation and combining overhead.

Backtrack is a familiar form of exhaustive search. The branch-and-bound method is a variant of backtrack that takes advantage of information about the optimality of partial solutions to avoid considering solutions that cannot be optimal. As an example of the branch-and-bound technique,consider the 8-puzzle (Fig. 13-2),a simplified version of the 15-puzzle invented by Sam Loyd in 1878. The 8-puzze consists of eight tiles, numbered one through eight, arranged on a 3 × 3 board. Eight locations contain exactly one tile; the ninth location is empty. The object of the puzzle is to repeatedly fill the hole with a tile adjacent to it in the horizontal or vertical direction until the tiles are in row-major order.

Given an initial board position and a mechanism for generating legal moves from any position,it is possible to construct a tree of board positions that can be reached from the initial position. This tree is called the state space tree (Fig. 13-3). One way to solve the puzzle is to pursue a breadth-first search of this state space tree until the sorted state is discovered. However, the goal is

# FIGURE 13-2

<table><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Hole</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>6</td></tr></table>

The 8-puzzle, a simplified version of the 15-puzzle invented by Sam Loyd in 1878.

# FIGURE 13-3

A portion of the state space tree corresponding to the search fora solution to a particular arrangement of the 8-puzzle.

![](images/c47e9c13c807a999d24a047488874abd644b0138b3e85c86471438a8060b641b.jpg)

to examine as few alternative moves as possible. A means for achieving that goal is to associate with each state an estimate of the minimum number of tile moves needed to solve the puzzle, given the moves made so far.

One such function adds the number of tile moves made so far to the Manhattan distance between each out-of-place tile and its correct location. [The Manhattan distance between two tiles with (row, column) coordinates $( x _ { 1 } , y _ { 1 } )$ and $( x _ { 2 } , y _ { 2 } )$ is $| x _ { 1 } - x _ { 2 } | + | y _ { 1 } - y _ { 2 } | . ]$ Given such a function, the search can be concentrated on the portions of the state space tree that contain the most promising moves. The search always proceeds from the node having the smallest function value. If two or more nodes have the same value, then the node farthest from the root of the state space tree is examined. If two or more nodes the same distance from the root have the same value, then one node is chosen arbitrarily. The branch-and-bound search of an 8-puzzle appears in Fig. 13-4. Note that the algorithm requires that far fewer nodes be examined than in the breadth-first search.

Now that we have given a concrete example, we will define the branch-andbound technique. Given an initial problem and some objective function $f$ to be minimized, a branch-and-bound algorithm attempts to solve it directly. If the problem is too large to be solved immediately,it is decomposed into a set of two or more subproblems of smaller size. Every subproblem is characterized by the inclusion of one or more constraints. The decomposition process is repeated until each unexamined subproblem is decomposed, solved, or shown not to be leading to an optimal solution to the original problem.

In the 8-puzzle example, the problem is to put the pieces in order. The objective function $f$ is the number of moves needed to order the pieces. If only a single move is necessary to order the pieces, the algorithm solves the problemdirectly.Otherwise,itdecomposes the problem by generatinganumber of subproblems, one per legal move.

As we have seen in the case of the 8-puzzle, the decomposition process applied to the original problem may be represented by a rooted tree, called the state space tree. The nodes of this tree correspond to the decomposed problems, and the arcs of the tree correspond to the decomposition process. The original problem is the root of the tree. The leaves of the tree are those partial problems that are solved or discarded without further decomposition.

A branch-and-bound tree is distinguished in two important ways from trees representing divide-and-conquer algorithms. First, the tree is an OR tree (Fig.13-1b); the solution to any subproblem is a solution to the original problem.Hence the entire tree need not be searched. In fact, the state space tree representing a branch-and-bound algorithm may be infinite. This is the second important difference between branch-and-bound trees and divide-and-conquer trees.

Recall that the goal of the branch-and-bound technique is to solve the problem by examining a small number of elements in this tree. Assume that a minimum cost solution f\* is desired. A lower bounding function g is calculated for each decomposed subproblem as it is created. This lower bound represents the smallest possible cost of a solution to that subproblem, given the subproblem's constraints. On any path from the root to a terminal node, the lower bounds are always nondecreasing.In addition, the lower bound $g ( x )$ at every leaf node $x$ representing a feasible solution is identical to the valueof the objective function $f ( x )$ for that subproblem.Leaf nodes representing infeasible solutions have the value $\infty$ Figure13-5 is another exampleof a state space tree.The values inside the nodes are the lower bounds of the corresponding subproblems. Nodes corresponding to feasible solutions are represented by heavy circles. The best solution to this problem has cost 18; i.e., the value of $f ^ { * }$ is 18.

![](images/f2633bfcfd90e00d88a3b90f50730167ac8622c340e93b73771d087126e52f80.jpg)  
13-4 Thebranchandboundsearch forasolution toanarrangementof the8-puzzeidentica to that of Fig.13-3.

![](images/b1ad16e8c2b9433a69dc4786f9225f908ce7ed8ddd1fa9a40ce326b3d8cf0924.jpg)  
FIGURE 13-5 Another example of a state space tree. The values inside the nodes are the lower bounds of the solutions to the corresponding subproblems.Nodes corresponding to feasible solutionsare represented by heavy circles. The best solution to this problem has cost 18.Thenumbers near the nodes represent the order in which they are examined by the best-first search strategy.

At any point during the execution of a branch-and-bound algorithm there exists a set of problems that have been generated but not yet examined. A search strategy determines the order in which the unexamined subproblems are examined. The best-first (best-bound) search strategy selects the unexamined subproblem with the smallest lower bound. In the case of a tie, the subproblem deepest in the state space tree (i.e., the subproblem with the most constraints) is chosen. Ties unresolved by the deepness heuristic are broken arbitrarily. The numbers near the nodes in Fig.13-5 indicate the order in which the nodes are examined by the best-first search strategy.

A branch-and-bound algorithm can be characterized by how subproblems are generated, how a particular subproblem is selected as the point to continue the search, how hopeless subproblems are discarded,and how the algorithm terminates. Any of these steps can be performed in parallel.

# 13.3.1 Traveling Salesperson Problem

The traveling salesperson problem (TSP) can be solved by a branch-and-bound algorithm. The TSP is defined as follows: Given a set of vertices and a nonnegative cost $c _ { i , j }$ associated with each pair of vertices $i$ and $j$ ,find a circuit containing every vertex in the graph so that the cost of the entire tour is minimized. An example of a weighted graph and its traveling salesperson tour are given in Fig. 13-6.

Little et al. (1963) devised a famous branch-and-bound algorithm to solve the traveling salesperson problem. When an unsolvable problem is encountered, it is broken into two subproblems representing tours that must include or exclude a particular edge. The edge to be used as the added constraint for the subproblems is chosen so that the lower bound on the solution cost of the subproblem, excluding that edge,is maximized. In other words, when a problem is broken into subproblems, the algorithm examines the minimum increase in the tour length, when various edges are excluded,and chooses the edge where exclusion has caused the largest increase in the tour length.

![](images/11c1063daddf4c22313055444d29fe78b499af902bef751d9920ee79f411e584.jpg)  
RE 13-6 A weighted graph and its traveling salesperson tour (solid lines).

Reduction is used to find a lower bound on the cost of the tour, given the constraints made so far. The reduction algorithm works as follows: For every vertex i in the graph, the length ci of the shortest edge leading to vertex i is found.If ci > O,then the lower bound can be increased by ci,if ci is subtracted from the length of every edge leading to vertex i. After this step has been performed, the rows can be reduced in a similar fashion. For every vertex i in the graph, the length r; of the shortest edge leading from vertex i is found. If ri >O, then the lower bound can be increased by ri if ri is subtracted from the length of every edge leading from vertex i. An example of matrix reduction appears in Fig. 13-7.

A problem is broken into subproblems that are easier to solve because the subproblems contain additional constraints. In this algorithm, for example, including an edge reduces the number of edges that must be added to complete the tour, while excluding an edge reduces the number of candidate edges.By driving up the lower bound as quickly as possible, the goal is to limit the number of subproblems (nodes in the state space tree) that must actually be examined. Figure 13-8 contains a high-level description of a best-first branch-and-bound algorithm using the best-first variant ofLittleet al.'s problem decomposition heuristic.

Figure 13-9 presents the state space tree corresponding to this algorithm's search for the traveling salesperson tour of the graph shown in Fig. 13-7. Each node in the state space tree represents a set of possible tours satisfying constraints specified by the path from the root to that node. The root represents the set of all possible tours. Since reducing the weight matrix of the directed graph results in the value 25 being assigned to the root,a lower bound on the length of any tour is 25. The edge whose exclusion causes the greatest increase in the lower bound is $^ { ( B , C ) }$ . Hence the two children of the root represent the alternatives of including or excluding edge $( B , C )$ . Every tour explored in the Ieft subtree must contain edge $^ { ( B , C ) }$ ,but no tour explored in the right subtree may contain edge $^ { ( B , C ) }$ . Given its constraint, each child node of the parent can be reduced, and lower bounds on all solutions based on that constraint can be determined. The lower bound of the left child is 31, while the lower bound on the right child is 29. In other words, tours that contain edge (B,C) must have length at least 31,while tours that do not contain edge $^ { ( B , C ) }$ must have length at least 29. Hence the right child is the next node to be explored. Excluding edge $( E , C )$ causes the greatest increase in the lower bound.The value in the right child-32-is a lower bound on all solutions that do not have edge (B,C) or edge (E,C). The value in the left child-31-is a lower bound on all solutions that do not have edge $( B , C )$ ,but do have edge $( E , C )$

![](images/e2dca6529ab04397839dbb8c1cf5b0ddace148ebf28d67bcc2f71d44bef898d3.jpg)  
FIGURE 13-7 An example of matrix reduction used by Litte et al.'s traveling salesperson algorithm. A lowerbound on thelength of the traveling salesperson tourof this graph is 25.

Since there are two unexplored nodes with the same lower bound (31), we explore the node deeper in the tree. This processcontinues until atour is

TRAVELING SALESPERSON (SISD): begin reduce weight matrix, determining the root's lower bound initially only the root is in the state space tree {The root represents the set of all possible tours} repeat select the unexamined node in the state space tree with the smallest lower bound if the node represents a tour then exit the loop endif select the edge whose exclusion increases the lower bound the most for the two cases representing the inclusion and exclusion of the selected edge do create a child node with the correct constraint find the lower bound for the child node endfor forever   
end

FIGURE 13-8 Ahigh-level description of a sequential best-first branch-and-bound algorithm to solve thetraveling salespersonproblem.Thealgorithm is based on the problem decomposition heuristicdevisedbyLittle etal.

# FIGURE 13-9

The state space tree corresponding to a best-first branch-and-bound search for a traveling salesperson tour of the graph shown in Fig.13-7.

![](images/f6c71eeb6ef2a91e60a651924ce8ea3f56c56cbd61010bea38e8e1f90a0215c6.jpg)

discovered, at which point the algorithm terminates. The tour contains edges $( E , C )$ ， $( A , D )$ ， $^ { ( C , B ) }$ ， $( B , A )$ ,and $( D , E )$

# 13.4 PARALLEL BRANCH-AND-BOUND ALGORITHMS

The first two parts of Sec. 13.4 describe parallelizations of the branch-andbound algorithm for multiprocessors and multicomputers, respectively. We use as our problem domain the traveling salesperson problem described in Sec.13.3. All the parallel algorithms described in this section use the branching and bounding heuristics developed by Little et al.

The final part of this section discusses anomalies in parallel branch-andbound algorithms-conditions under which adding processors may result in slowdown or superlinear speedup.

# 13.4.1 Multiprocessor Algorithms

Mohan (1983) has developed two paralelizations of the traveling salesperson algorithm presented in Fig.13-8. The first parallel algorithm involves a parallelization of the for loop; the second parallel algorithm executes the repeat loop in parallel.

As presented before, the for loop has a natural parallelism of 2-each node has only two children. However,by selecting $k$ edges to be considered for inclusion or exclusion,the number of children of each node increases to $2 ^ { k }$ ， since constraints reflecting all combinations of inclusion and exclusion must begenerated.The modified algorithm is shown in Fig.13-10. Clearly this data-parallel algorithm is appropriate for $2 ^ { k }$ processors.

The second algorithm creates a number of processes that asynchronously explore the tree of subproblems until a solution has been found. Each process repeatedly removes the unexplored subproblem with the smallest lower bound from the ordered list of unexplored subproblems. Then it decomposes the problem (unless it can be solved directly),and inserts the two newly created subproblems in their proper places in the ordered list of problems to be examined. A process must have exclusive control of the list in order to insert and delete elements, but the time taken for these tasks is relatively small compared to the time needed to decompose a problem. Thus contention for this list should not be a significant inhibitor of speedup.

The speedup of these two parallel algorithms on Cm\* (a NUMA multiprocessor) is contrasted in Fig.13-11. The first algorithm achieves extremely poor speedup.The additional processors spend most of their time creating nodes that are never explored, because their lower bounds are too high. Mohan's second algorithm achieves, with 16 processors,a speedup of about 8 when solving a 30-vertex TSP. The major obstacle to higher speedup is the number of nonlocal memory references made by the processors.

TRAVELING SALESPERSON (UMA MULTIPROCESSOR):   
begin reduce weight matrix,determining the root's lower bound initially only the root is in the state space tree while,true do select the unexamined node in the state space tree with the smallest lower bound if the node represents a tour then exit the loop endif select the k edges whose exclusion increases the lower bound the most for the 2 cases representing allinclusion-exclusion combinations of the selected edges do create a child node with the correct constraints find the lower bound for the child node endfor endwhile   
end

![](images/b5cec580b3f7a7fb8efbdbd16a591c5988b194e3806e154d4488bb0aa9bedcc1.jpg)  
FIGURE 13-10 High-level description of a parallel traveling salesperson algorithm developed by Mohan (1983).Thealgorithm isdesignedforimplementationona UMA multiprocessor,but it does not achieve good speedup.   
FIGURE 13-11 ThespeedupofMohan’stwoparalelalgorithmstosolvethetravelingsalesperson problemwith30verticeson $\mathsf { C m } ^ { \star }$

# 13.4.2 Multicomputer Algorithms

Quinn (199O) has implemented four variants of an algorithm to solve the traveling salesperson problem on hypercube multicomputers. The algorithm uses distributed priority queues of unexamined subproblems-one queue per processor. The performance of the parallel algorithm depends upon the heuristic the processors use to exchange unexamined subproblems with each other. Major portions of this subsection first appeared in Quinn (1990).

Let $p = 2 ^ { d }$ denote the number of processors. Assume that the branching factor of the state space tree is $k$ ； i.e.,assume that each node in the tree has $k$ children. Let $N$ be the minimum number of constraints that must be added to the original problem in order to produce a subproblem that is solvable.In other words,any solution node must have depth $\geq N$ in the state space tree. Let $\chi$ be the time needed to examine a subproblem and either solve it or decompose it into $k$ subproblems. Let $\lambda$ be the time needed to transfer a subproblem from one processor's priority queue to another processor's queue, and assume that both the sender and the receiver processors must devote time $\lambda$ to the transfer.

The asynchronous branch-and-bound algorithm distributes the unexamined subproblems among the processors. In each of its iterations every processor with a nonempty priority queue removes the unexamined subproblem with the smallest lower bound and either solves the problem directly or divides it into $k$ subproblems. (Note: Although each processor iterates through a sequence of operations, there is no synchronization among processors.) If a processor divides a problem into $k$ subproblems,it puts the subproblems into its priority queue, then uses a heuristic to send $m$ of its unexamined subproblems to neighboring processors,where $m < k$ .At the beginning of execution, Processor O contains the original problem in its priority queue. Because each processor distributes $m$ subproblems every iteration, $I ( p ) = \lceil \log _ { m + 1 } p \rceil$ iterations are sufficient to provide every processor with at least one unexamined subproblem.

In order for a solution to be found and guaranteed optimal, two conditions must be met. First, at least one of the solution nodes (and hence all of its ancestors in the state space tree) must be examined. Second, processors must examine all nodes in the state space tree whose lower bounds are less than the cost of the optimal solution. The execution time of the algorithm is determined by whichever event occurs last. The event occuring last is determined by the number of processors and the shape of the state space tree.

To derive an expression for the execution time of the parallel algorithm, we first determine the amount of time needed to examine all of the worthwhile nodes in the state space tree. Assuming that subproblems are exchanged evenly among processors, every iteration requires time $\chi + 2 m \lambda$ ：time $\chi$ to decompose or solve a subproblem, time $m \lambda$ to send $m$ subproblems to other processors, and time mλ to receive (on average) $m$ subproblems from other processors. If S is the number of worthwhile subproblems in the state space tree, $I ( p )$ is the numberofiterations beforeallprocessorsareactively involved, and G(p) is the number of worthwhile subproblems examined in the first I(p) iterations, then S-G(p) worthwhile subproblems remain to be examined after the first I(p) iterations. If the percentage of worthwhile node examinations performed by the p processors after the first I(p) iterations is E(p), the number of additional iterations required to examine all worthwhile subproblems is [(S- G(p))/(pE(p))1. Multiplying the time per iteration by the number of iterations, we see that the amount of time needed to examine all worthwhile subproblems is

$$
( \chi + 2 m \lambda ) \Biggl ( I ( p ) + \Biggl \lceil \frac { S - G ( p ) } { p E ( p ) } \Biggr \rceil \Biggr )
$$

Second, we determine the amount of time needed for the search to reach a solution node, the length of the critical path. Let M denote the depth of the solution node in the state space tree.Let T(p) denote the number of transfers on the critical path from the root of the state space tree to the solution node.In other words, T(p) is the number of times that subproblems leading to the solution are transferred from one processor's priority queue to another processor's queue. Every transfer incurs a penalty of x/2+λ. The λ term is the time needed to perform the transfer. The x/2 term is the expected delay before the subproblem can be evaluated by the destination processor,since the destination processor is likely to be in the middle of decomposing another subproblem when the transfer begins. The total amount of time needed for the search to find a solution is

$$
( M + 1 ) ( \chi + 2 m \lambda ) + T ( p ) ( \chi / 2 + \lambda )
$$

Since the asynchronous algorithm completes when both previously mentioned conditions are met, the execution time of the algorithm is the maximum of the times in expressions 13.1 and 13.2.

Quinn has tested the model by implementing four parallel best-first, branchand-bound algorithms to solve the traveling salesperson problem. All these algorithms use the reduction heuristic of Litle etal.The algorithms have been implemented on a 64-processor nCUBE 3200 hypercube multicomputer.

All four algorithms have been executed on the same set of ten 30-vertex graphs. The edge weights are asymmetrical and randomly chosen from a uniform distribution of integer values ranging from O through 99.Every algorithm begins with Processor O possessing the original problem,and relies upon successive subproblem decomposition steps to work toward a solution.

During an iteration every processor with a nonempty priority queue removes the unexamined subproblem with the smallest lower bound and either solves the problem directly or divides it into two subproblems. It sends one unexamined subproblem to a neighboring processor and receives (on average) one unexamined subproblem from a neighboring processor. Quinn determined the parameters needed for the analytical model by recording the actions taken by the processors during their solution of the ten 30-vertex problem instances. Ail these parallel algorithms had the following parameters: $S = 5 5 9$ ， $k = 2$ $m = 1$ ， $\chi = 1 2 5$ msec, and $\lambda = 1$ msec. Values of $G ( p ) , E ( p )$ ,and $T ( p )$ varied from algorithm to algorithm.

All four algorithms use the following rule to distribute subproblems among the processors. Let $p = 2 ^ { d }$ be the number of processors. On iteration i Processor $j$ sends the unexamined subproblem to Processor $r$ ，where $r$ is found by inverting bit (i mod $d$ of $j$ .With this distribution rule $I ( p ) = \log _ { 2 } p$

Each algorithm has a unique heuristic for choosing which unexamined subproblem to send to a neighboring processor. Algorithm 1 puts the newly created subproblem with the edge inclusion constraint into the priority queue and sends the subproblem with the edge exclusion constraint. Algorithm 2 puts the newly created subproblem with the smaller lower bound into the priority queue and sends the subproblem with the higher lower bound. Algorithm 3 puts both newly created subproblems on its priority queue, then deletes the second-best problem from the priority queue and sends it. Algorithm 4 puts both newly created subproblems on its priority queue,then deletes the best problem from the priority queue and sends it.

<table><tr><td>Processors</td><td>Alg. 1</td><td>Alg. 2</td><td>Alg. 3</td><td>Alg. 4</td></tr><tr><td>1 Actual Predicted</td><td>1.00 1.00</td><td>1.00 1.00</td><td>1.00 1.00</td><td>1.00 1.00</td></tr><tr><td>2</td><td>Actual 1.88 Predicted 1.90</td><td>1.87 1.90</td><td>1.89 1.96.</td><td>1.93 1.96</td></tr><tr><td>4</td><td>Actual 3.52 Predicted 3.58</td><td>3.43 3.58</td><td>3.73 3.85</td><td>3.65 3.85</td></tr><tr><td>8</td><td>Actual Predicted</td><td>5.67 5.43 5.76 5.69</td><td>6.59 7.09</td><td>6.50 7.09</td></tr><tr><td>16</td><td>Actual Predicted</td><td>7.39 7.58</td><td>6.86 10.20 7.00 11.33</td><td>9.12 10.51</td></tr><tr><td>32</td><td>Actual Predicted</td><td>8.07 7.89</td><td>7.96 12.92 7.89 15.20</td><td>11.50 12.91</td></tr><tr><td>64</td><td>Actual Predicted</td><td>7.01 7.34 9.05 6.27</td><td>12.57 13.74</td><td>12.99 13.10</td></tr></table>

Actual and predicted speedups of asynchonrous branch-and-bound algorithms 1,2, 3, and4onnCUBE320o.Valuesrepresentaveragesover ten30-vertexinstancesof the traveling salespersonproblem withasymmetrical integer distances.

The upper entries of Fig. 13-12 indicate the speedup measured on the nCUBE 3200 for each of these four algorithms. The lower,italicized values are the speedups predicted by Quinn's model. Despite the simplifying assumptions, most notably the assumption that all subproblem decompositions require the same amount of time, the model is a reasonably accurate predictor of speedup.

For the solution of a 30-vertex traveling salesperson problem on 64 processors,execution time is dominated by the time needed to examine all worthwhile subproblems. Hence the difference in speedup among the four asynchronous algorithms is a reflection of how well they kept processors busy doing useful work.Figure 13-13 plots the percentage of worthwhile subproblem examinations as a function of distance from Processor O, the processor given the initial problem,as the algorithms execute on a six-dimensional hypercube. The "distance” between two processors is the length of the shortest path in the hypercube linking them. The significant differences in the curves illustrate how a simple change in the subproblem distribution heuristic can have a dramatic effect on the efficiency of the parallel algorithm, by increasing or decreasing the percentage of time various processors spend examining useful subproblems.

![](images/4de7e349ff97819e1e51c960987ca18693c9b3e57d48268666391ab20d157328.jpg)  
FIGURE 13-13 Percentage of worthwhile subproblem examinations for asynchronous algorithmssolving30-vertextraveling salespersonprobiemona64-processor nCUBE3200hypercubemulticomputer.

Because the execution times of the asynchronous algorithms on the 30-vertex traveling salesperson problem are dominated by the time needed to solve all worthwhile subproblems, Fig. 13-12 does not validate expression 13.2. To illustrate the precision of this part of the model, we present the performance of Algorithm 4,solving 10 instances of the 20-vertex traveling salesperson problem. For this smaller-sized problem the speedup of Algorithm 4 is constrained bythe time needed to traverse the critical path,because: (1) the state space tree has relatively few worthwhile subproblems,and (2) subproblems leading to the solution are frequently transferred from one processor to another. Figure 13-14 contrasts the actual and predicted speedups of this algorithm.

We can use the model to predict the performance of these algorithms on other multicomputers, because changing the value of $\lambda$ does not affect the values of the other parameters.

To summarize, multicomputer implementations of parallel branch-and-bound algorithms that keep unexamined subproblems in a single priority queue have a

FIGURE 13-14 Actual and predicted speedups for Algorithm 4solving 20-vertex traveling salesperson problem. Values represent averages over ten problem instances.

<table><tr><td>Processors</td><td>Actual</td><td>Predicted</td></tr><tr><td></td><td>1.00</td><td>1.00</td></tr><tr><td></td><td>1.63</td><td>1.87 2.00</td></tr><tr><td>28</td><td>1.92</td><td>2.01</td></tr><tr><td>16</td><td>1.90</td><td>2.01</td></tr><tr><td></td><td>2.04</td><td></td></tr><tr><td>32 64</td><td>2.26 2.21</td><td>2.01 2.04</td></tr></table>

number of disadvantages. One processor must have a disproportionately large memory,and that processor is involved in every communication. Distributing the unexamined subproblems among the processors balances the memory requirements,reduces thenumberof communications,and distributes the messages over the network, which can result in a more practical algorithm that actually achieves higher speedup.Whether or not the potential for higher speedup is realized depends upon the effectiveness of the subproblem-distribution heuristic in assigning processors useful work.

# 13.4.3 Anomalies in Parallel Branch and Bound

In this section we present Lai and Sahni's (1984) analysis of the speedups theoretically achievable by a parallel branch-and-bound algorithm. We must make a few assumptions in order for the analysis to be manageable. Assume that the time needed to examine any node in the tree and decompose it is constant for all nodes in the state space tree. Furthermore,assume that execution of the parallel algorithm consists of a number of “iterations.” During each iteration every processor examines a unique subproblem, if one is available, and decomposes it. Given a particular branch-and-bound problem to be solved and a particular lower bounding function g, define I(p) to be the number of iterations required to find a solution node when $p$ processors are used.

The first theorem shows that increasing the number of processors can actuall increase the number of iterations required to find a solution.

Theorem 13.1. Given n1 < n2 and k > O, there exists a state space tree such thal $k I ( n _ { 1 } ) < I ( n _ { 2 } )$ (See Lai and Sahni[1984].)

Proof. Consider the state space tree shown in Fig. 13-15. All nodes labeled "=" have the same lower bound, which happens to be the value of the least-cost answer node (node A). Nodes labeled “>" have a lower bound greater than the value of the least-cost answer node. When n1 processors conduct the search, on the first iteration the root node is expanded into n1 +1 children nodes. The second iteration consists of expanding the ni leftmost nodes at level 2 into n1 nodes at level 3. Of the nodes at level 3,n1-1 of them cannot lead to the solution and are discarded. On iteration 3 the remaining nodeat level 3 and node B are expanded. Since the node at level 3 leads to the solution node, the algorithm terminates. Hence I(n1)= 3.

When n2 processors conduct the search, the first iteration is the same: The root node is expanded into n1 +1 children nodes. On the second iteration, however,all n1+1 nodes at level 2 are expanded,yielding n1+n2 nodes at level 3. Since only n2 nodesat level 3canbe expanded on iteration 3,itcould happen that then2 rightmost nodes would be the nodes chosen. If we assume the processors expanded the n2 rightmost nodesat level 3,n2 nodes at level 4 would be created,and iterations4,5, 6,..,3k could be devoted toa wild-goose chase,expanding nodes down the right partof the tree. The solution node A would be expanded on iteration 3k +1. Hence I(n2)=3k +1.Combining the two results yields kI(n1) =3k <3k+1= I(n).

![](images/ce74686ecec714ed9922b7ead0bd103bb30999dabcdbc555599440992c2c5889.jpg)  
Astatespace treeillustrating that increasing thenumber of processorsmayactually increase the execution time of a branch-and-bound algorithm.

Because many nodes have a lower bound equal to the value of the least-cost answer node $f ^ { * }$ -we see theanomaly described in the Theorem 13.1.What would happen if $g ( x ) \neq f ^ { * }$ ，whenever $x$ is not a solution node?

Definition 13.1. A node $x$ is critical if $g ( x ) < f ^ { * }$

Theorem 13.2. If $g ( x ) \neq f ^ { * }$ whenever $x$ is not a solution node, then $I ( 1 ) \geq I ( n )$ for all $n > 1$ (See Lai and Sahni (1984).)

Proof. By the definition of the best-first branch-and-bound heuristic, only critical nodesand least-cost answer nodes can be expanded. In addition, every critical node must be expanded before any least-cost answer node is expanded. Hence if the number of critical nodes is $m$ ,then $I ( 1 ) = m$ .When $n > 1$ ,at least one of the nodes expanded each iteration must be a critical node (Prob. 13-5). Hence a least-cost answer node must be examined no later than iteration $m$ .Thus if the number of critical nodes is $m$ ,then $I ( n ) \leq m$ .Therefore $I ( 1 ) \geq I ( n )$ for all $n > 1$

The following theorem proves that increasing the number of processors can actually cause a disproportionate decrease in the number of iterations required to find a solution node.

Theorem 13.3. Given $n _ { \mathrm { 1 } } ~ < ~ n _ { 2 }$ and $k > n _ { 2 } / n _ { 1 }$ , then there exists a state space tree such that $I ( n _ { 1 } ) / I ( n _ { 2 } ) \geq k > n _ { 2 } / n _ { 1 }$ (See Lai and Sahni [1984].)

Proof. This is left to the reader as Prob. 13-6.

Theorem 13.4. If $g ( x ) \neq f ^ { * }$ whenever $x$ is not a least-cost answer node, then $I ( 1 ) / I ( n ) \leq n$ for $n > 1$ (See Lai and Sahni [1984].)

Proof. Let $m$ be the number of critical nodes. Then $I ( 1 ) = m$ (Theorem 13.2). All critical nodes mustbe expanded before the parallel branch-and-bound algorithm can terminate (Prob. 13-7). Hence $I ( n ) \geq m / n$ ,or $I ( 1 ) / I ( n ) \leq n$

Lai and Sahni have found anomalous behavior in some instances of the 0-1 knapsack problem,butthey conclude thatanomalous behaviorisarely eountered in practice and that, in general, (1) increasing the number of processors will not increase execution time (assuming the problem is large enough)，and (2) superlinear speedup cannot be expected.

# 13.5 ALPHA-BETA SEARCH

The most successful computer programs to play two-person zero-sum games of perfect information, such as chess,checkers,and go, have been based on exhaustive search algorithms. These algorithms consider series of possible moves and countermoves, evaluate the desirability of the resulting board positions, then work their way back up the tree of moves to determine the best initial move.

Given a trivial game, the minimax algorithm can be used to determine the best strategy. Figure 13-16a represents the game tree of a hypothetical game, with rules left unstated, played for money. Dotted edges represent moves made by the first player; solid lines represent moves made by the second player. The root of the tree is the initial condition of the game. The leaves of this game tree represent outcomes of the game. Interior nodes represent intermediate conditions. The outcomes are always put in terms of advantage to the first player. Thus positive numbers indicate the amount of money won by the first player,while negative numbers indicate the amount of money lost by the first player. The algorithm assumes that the second player tries to minimize the gain of the first player, while the first player tries to maximize his or her own gain, hence the name of the algorithm.Figure 13-16b is the same tree with the values of the interior nodes filled in. The value of this game to the first player is 2. If the first player plays the minimax strategy,he or she is guaranteed to win at least two dollars.

Stockman (1979) has pointed out that a game tree is an example of an AND/OR tree. The AND nodes represent positions where it is the second player's turn to move. The OR nodes represent positions where it is the first player's turn to move.

Nontrivial games such as chess have game trees that are far too complicated to be evaluated exactly. For example, de Groot has estimated that there may be 384 positions inachess game tree (de Groot 1965).Thus current chess-playing programs examine moves and countermoves only to a certain depth, then, at that point, estimate the value of the board position to the first player. Of course, evaluation functions are unreliable. If a perfect evaluation function existed, the meed for searching would be eliminated (Prob. 13-9). As we have seen. all possible moves and countermoves from a position $p$ to some predetermined lookahead horizon can be represented by a game tree. The minimax value of the game tree can be found by applying the evaluation function to the leaves of the tree (the terminal nodes), then working backward up the tree. If it is the second player's move at a particular nonterminal node in the game tree, the value assigned is the minimum over all its children nodes. If it is the first player's move, the value assigned is the maximum over all its children nodes.

![](images/69daa8c98e4c88c90137b48b422b14b25d04331c4b48d6cb1f87507a128b7fec.jpg)  
FIGURE 13-16 (a) A game tree. Dotted edges represent the moves available to the first player; solid edgesrepresent movesavailable to the second player.(b) The same tree with thevalues of the interior nodes filled in.

Given a game tree in which every position has $b$ legal moves, it is easy to see that a minimax search of the game tree to depth $d$ examines $b ^ { d }$ leaves.

It is generally true that the deper the search, the beter the quality of play. That is why alpha-beta pruning has proven to be valuable. Alpha-beta pruning,a form of branch-and-bound algorithm,avoids searching subtrees whose evaluation cannot influence the outcome of the search,i.e.，cannot change the choice of move. Hence it allows a deeper search in the same amount of time.

The alpha-beta algorithm, displayed in Fig. 13-17, is called with four arguments: pos, the current condition of the game; $\alpha$ and $\beta$ ,the range of values over which the search is to be made; and depth, the depth of the search that is

Reference $\alpha$ {Lower cutoff value} $\beta$ {Upper cutoff value)   
Value pos (Position) depth {Search depth}   
Parameter max.c {Maximum possible number of moves]   
Local c[1..max.c] {Children of pos in game tree) cutoff {Set to TRUE when okay to prune] i {Iterates through legal moves] val {Value returned from search] width {Number of legal moves]   
begin ifdepth $\leq ~ 0$ then return (EVALUATE(pos)) {Evaluate terminal node] endif width GENERATE.MOVES(pos) ifwidth $= ~ 0$ then return (EVALUATE $( p o s )$ {No legal moves) endif cutoff FALSE $i \gets 1$ while $i \ \leq$ width and cutoff $=$ FALSE do val ALPHA.BETA (c[i], $\alpha$ ， $\beta$ ,depth-1) if pos is MAX-NODE and val $> \alpha$ then $\alpha ~ $ val else if pos is MIN-NODE and ual $< \beta$ then $\beta \mathrm { ~  ~ }$ val endif endif if $\alpha ~ > ~ \beta$ then cutoff TRUE endif $i  i + 1$ endwhile if pos is MAX-NODE then return $\alpha$ else return $\beta$ endif   
end

FIGURE 13-17 Sequential alpha-beta algorithm.

to be made. The function returns the minimax value of the position pos. The original board position is a MAX-NODE. Every child of a MAX-NODE is a MIN-NODE. Every child of a MIN-NODE is a MAX-NODE.

To illustrate the workings of the alpha-beta algorithm,consider the game tree in Fig. 13-18. This tree represents the same game as that in Fig. 13-16.

![](images/baba139e3c3a3bb01247eb71b8a41c2c691e725a085bb28499b1a475123c52a2.jpg)  
FIGURE 13-18 An illustration of alpha-beta search. The number inside each node is the value of the position.In the case of leaf nodes,an evaluation function computes the value of the position.Inthe case of interiornodes,thevalue iscomputed from the valuesof its children.Highlighted circlesrepresent nodes inwhich pruning occurs.

except that nodes not examined by the alpha-beta algorithm are not included. When the algorithm begins execution, $\alpha = - \infty$ and $\beta = \infty$ . The algorithm traverses the nodes of the tree in preorder;the values of $\alpha$ and $\beta$ converge as the search progresses.

The nodes drawn in heavy lines in Fig. 13-18 represent places where pruning occurs. To explore the conditions under which pruning happens let us consider an arbitrary interior node in the search tree. When the search reaches this node, we know that some choice of moves that has already been considered leads to a value of at least $\alpha$ for the player moving first. We also know that correct play on the part of the opponent will ensure that the first player cannot get a value more than $\beta$ .Hence $\alpha$ and $\beta$ define a window for the search.

If the interior node pos is a MAX-NODE, then it is the first player’s move. If val,the value of the game tree searched from node pos is greater than $\alpha$ then $\alpha$ is changed to val, a beter line of play has been found for player one.

Analogously, if the interior node pos is a MiN-NODE, then it is the second player's move. If val, the value of the game tree searched from node pos is less than $\beta$ ,then $\beta$ is changed to val; a better line of play has been found for player two.

However,if at any time the value of $\alpha$ exceeds the value of $\beta$ ,there is no need to search further. It is in the best interests of one of the players to block the line of play leading to node pos.

For example, consider the node labeled A in Fig. 13-18. The value returned from the search of the first child of A is 3, which is greater than 2, the value $\beta$ . It is not in the second player's interest to allow play to reach this position, since there is another line of play guaranteeing a value no higher than 2. Hence there is no point in continuing the search from this game position.

![](images/3cbf26f1e9d874621ecdfb2fccd1d648d46462f961cc0da6c984a1947f282164.jpg)  
FIGURE 13-19 Alpha-beta pruning of a perfectly ordered game tree. The number inside each node indicates itsclassificationas either type1,type2,or type 3.The root of the tree isa type 1node.Thefirstchild ofa type1node isa type1node.All otherchildrenofa type1 nodeare type 2 nodes.The firstchild ofa type 2 node isa type 3node;all other children of a type 2 node may be pruned. All children of a type 3 node are type 2 nodes.

To what extent can alpha-beta pruning reduce the number of leaf nodes that must be examined? The algorithm does the most pruning on a perfectly ordered game tree, that is, a game tree in which the best move from each position is always searched first (see Fig. 13-19). Assuming a perfectly ordered game tree with a search depth of $d$ and uniform branching factor $^ b$ Slagle and Dixon (1969) have shown that the number of leaf nodes examined by the alpha-beta algorithm is

$$
O p t ( b , d ) = b ^ { \lceil d / 2 \rceil } + b ^ { \lfloor d / 2 \rfloor } - 1
$$

In other words, in the best case it is possible for the alpha-beta algorithm to examine no more than approximately twice the square root of the number of nodes searched by the minimax algorithm.

Definition 13.2. The effective branching factor of an algorithm searching a game tree of depth $d$ is the $d$ th rootof thenumberofleaf nodesevaluatedbythealgorithm.

Casting Slagle and Dixon'sresult interms of this dfinition,an al-beta searchreduces theefectivebranching factor from $b$ to $\sqrt { b }$ when searching a perfectly ordered game tree.

Of course,a perfectly ordered search is not possible in practice.However, experimental evidence indicates that sequential alpha-beta algorithms often search no more than 50 percent more nodes than would be searched if the tree were perfectly ordered. Hence in practice the alpha-beta search algorithm exhibits much higher performance than minimax.

Two common enhancements to the alpha-beta search algorithm are aspiration search and iterative deepening. Aspiration search makes an estimate of the value v of the board position at the root of the game tree, figures the probable error e of that estimate, then calls the alpha-beta algorithm figuring the probable error e of that estimate, then calls the alpha-beta algorithm with the initial window (u-e, v-e). If the value of the game tree does indeed fall within this window 6f values, then the search will complete sooner than if the algorithm had been called with the initial window (-oo, oo). If the value of the game tree is less than v-e, then the search will return the value v-e,and the algorithm must be called again with another window, such as (-oo, v -e). Similarly, if the value of the game tree is greater than v +e, then the search returns the value v +e, and another search will have to be done with a modified initial window,such a $( \upsilon + e , \infty )$

Another variant on the standard alpha-beta algorithm is called iterative deepening. Each level of a game tree is called a ply and corresponds to the moves of one of the players. Iterative deepening is the use of a (d-1)-ply search to prepare for a $d$ -ply search. This technique has three advantages (Marsland and Campbell 1982). First, it allows the time spent in a search to be controlled. The search can continue deeper and deeper into the game tree until the time allotted has expired. Second, results of the (d- 1)-ply search can be used to improve the ordering of the nodes during the d-ply search, making the node ordering similar to perfect ordering,and allowing the alpha-beta search to execute morequickly.Finally,the value returned froma $( d - 1 )$ -ply searchcan be used as the center of the window for a $d$ -ply aspiration search.

# 13.6 PARALLEL ALPHA-BETA SEARCH

# 13.6.1 Parallel Move Generation and Position Evaluation

Alpha-beta search has a number of opportunities for parallel execution. One approach is to parallelize move generation and position evaluation. The custom chess machine $\mathrm { H I T E C H ^ { \mathrm { \tiny { T M } } } }$ ，with 64 processors organized as an $8 \times 8$ array,has taken this route.However,the speedup thatcan be achieved with this approach is limitedby the parallelism inherent in these activities.Further improvements in speedup lie in parallelizing the search process.

# 13.6.2 Parallel Aspiration Search

Another straightforward paralelization of the alpha-beta algorithm is done by performing an aspiration search in paralel. If three processors are available, then each processor can be assigned one of the windows $( - \infty , v - e )$ ， $( \upsilon - e , \upsilon + e )$ ,and $( \upsilon + e , \infty )$ . Ideally the processor searching $( \upsilon - e , \upsilon + e )$ will succeed, but allthree processors willfinish no later than asingle procesor searching the window $( - \infty , \infty )$ .More processors can be accommodated by creating more windows with smaller ranges.Baudet (1978a,1978b) explored parallel aspiration on the $\mathbf { C m ^ { * } }$ NUMA multiprocessor.

Work on parallel aspiration for the game of chess has led to two conclusions. First, the maximum expected speedup is typically five or six, regardless of the number of available processors. This is because Opt(b,d) isa lower bound on the cost of alpha-beta search, even when both α and β are initially set equal to the value eventually returned from the search. Second, parallel aspiration search can sometimes lead to superlinear speedup when two or three processors are being used.

# 13.6.3 Parallel Subtree Evaluation

Many believe that significant speedups can only be,achieved by allowing processors to examine independent subtrees in parallel. There are two important overheads to be considered. Search overhead refers to the increase in the number of nodes that must be examined owing to the introduction of parallelism. Communication overhead refers to the time spent coordinating the processes performing the searching. Search overhead can be reduced at the expense of communication overhead by keeping every processor aware of the current search window. Communication overhead can be reduced at the expense of search overhead by allowing processors to work with outdated search windows.

For example, consider this simple method of performing alpha-beta search in parallel. Split the game tree at the root, and give every processor an equal share of the subtrees.Let every processor perform an alpha-beta search on its subtrees. Each processor begins with the search window $( - \infty , \infty )$ ,and no processor ever notifies other processors of the changes in its search window. Clearly this algorithm minimizes communication overhead. What is the speedup achievable by this method?

Theorem 13.5. Given a perfectly ordered uniform game tree of depth $d$ and branching factor $^ b$ ,the number of node examinations performed by alpha-beta search in the first branch's subtree is

$$
b ^ { \lceil ( d - 1 ) / 2 \rceil } + b ^ { \lfloor ( d - 1 ) / 2 \rfloor } - 1
$$

(See Hyatt et al.[1989].)

Proof. Slagle and Dixon (1969) showed that the minimum number of nodes examined fromatype1nodeof depth $d$ is $b ^ { \lceil ( d - 1 ) / 2 \rceil } + b ^ { \lfloor ( d - 1 ) / 2 \rfloor } - 1$ In a perfectly ordered game tree,the first childof a type1 node is alsoa type 1 node,so we simply replace $d$ with $d - 1$ in their expression.

Theorem 13.5 demonstrates that the examination of the first branch of a perfectly ordered game tree takes a disproportionate share of the computation time.For example,consider a 10-ply search of a perfectly ordered tree that has a branching factor of 38 (such as a chess game tree).The minimum number of node examinations is 158,470,335. The minimum number of node examinations in the first branch is 81,320,303. By Amdahl's law it is clear that if only one processor is responsible for searching the first move's subtree, speedup will be Iess than two.

In addition, because every processor's search must begin with -oo and as the values for α and β,respectively, the parallel algorithm will not prune as many subtrees as the sequential algorithm. A complete elimination of communication overhead creates significant search overhead.

Let's look at the other extreme. What must be done to eliminate search overhead completely? We will make the assumption that the game tree is perfectly ordered. Look at Fig. 13-19.If we want to eliminate search overhead,we must ensure the parallel algorithm prunes the same nodes as the sequential algorithm. First consider searching the subtree of a type 1 node. The first child is a type 1 node;the remaining children are type 2 nodes. Searching subtrees rooted by type 2 nodes requires up-to-date values of α and β in order to prune all but the first children of the type 2 nodes. To get up-to-date values, the search of the subtrees rooted by type 2 nodes cannot begin until the search of the subtree rooted by the type 1 node has finished,returning α and β. However,once the values of α and β are known,all type 2 nodes may be searched in parallel without processor interaction.

Next, let’s look at the search of a subtree of a type 2 node.Since all but the first child are pruned, there is no parallelism to be exploited.

Finally,consider the search of a subtree of a type 3 node. All its children are type2 nodes,and these nodes may be searched in paralel without processor interaction.

In practice, search trees are not perfectly ordered, but this exercise has demonstrated that a parallel alpha-beta algorithm can significantly reduce search overhead by delaying the search of some subtrees until more accurate bounds information is available.

# 13.6.4 Distributed Tree Search

Ferguson and Korf (1988) have developed a parallel tree searching algorithm called DistributedTreeearch (D),which,whenevaluatinggame trees,as achieved good speedups. Although the DTS algorithm is suitable for solving a variety of tree search problems,we will describe itsuse as a tool to perform parallel alpha-beta search.

The DTS algorithm executes by assigning processes to nodes of the search tree. Each process controls one or more physical processors.When the algorithm begins execution,asingle process, called the root process,isasiged to the root node of the search tree.It controls the entireset of physical processors performing the search.

When a process is assigned to a nonterminal node, it generates the children of that node by evaluating the legal moves. The process assigns processors to the children nodes based upon the processor allocation strategy. For example, if the search is using a breadth-first processor allocation scheme,one processor is allocated to each child node until there are no more processors to allocate. At this point a new process is created for each child node that is allocated at least one processor. The parent process suspends operation until it receives a message from another process.

When a process is assigned to a terminal node, it returns the value of that node and its set of allocated processors to the parent, then terminates.

The first child process to complete the search of its subtree sends a message with its values of $\alpha$ and $\beta$ to the parent. It returns its set of processors to the parent and terminates. The parent process wakes up when it receives the message from its child. It reallocates the freed processors to one or more of its active child processes. It may also send one or more of its child processes new values of $\alpha$ and $\beta$ . The reallocation of processors from quicker processes to slower processes produces efficient load balancing.Notice that in this scheme a child process may be awakened by its parent,which is passing along additional processors. After reallocating processors,parent processes suspend operation until they receive another message. When all child processes have terminated, the parent process returns $\alpha$ ， $\beta$ ，and the set of processors to the parent and terminates. When the root process terminates, the algorithm has completed.

Three implementation details improve the performance of the DTS algorithm. First, every blocked process should share a physical processor with one of its child processes. In this way all processors stay busy. Second,when a blocked parent process is awakened, it should have higher priority for execution than processes corresponding to nodes deeper in the search tree. Third, when the search reaches a point where there is only a single processor allocated to a node, the process controlling the processor should execute the standard sequential alpha-beta search algorithm.

Theorem 13.6. Given a uniform game tree with depth $^ d$ and branching factor $b$ ,if thealpha-beta algorithm searches the tree with effective branching factor $b ^ { x }$ (where $0 . 5 \le x \le 1 $ ), then DTSwith $p$ processors and breadth-first allocation will achieve a speedup of $O ( p ^ { x } )$

Proof. The execution time of the sequential algorithm is proportional to the number of leaf nodes it evaluates, or $O ( ( b ^ { x } ) ^ { d } ) = O ( b ^ { x d } )$ . The DTS algorithm with breadthfirst allocation distributes processors evenly among the branches of the search tree, until there is one processor per node. This occurs at depth $O ( \log _ { b } p )$ . The time complexity of this part of the search is also $O ( \log _ { b } p )$ , since allocations at the same level in the tree occur in parallel. Once the search has reached a point where there is one processor per node, every processor performs the sequential alpha-beta algorithm on the remaining subtree of depth $O ( d - \log _ { b } p )$ .The time needed for these searches is $O ( b ^ { x ( d - \log _ { b } p ) } )$ ,since theeffective banchingfactoris $b ^ { x }$ .Propogating values back to the root has time complexity $O ( \log _ { b } p )$ .The overall time complexity of the DTS algorithm is $O ( \log _ { b } p + b ^ { x ( d - \log _ { b } p ) } )$ .As the depth $d$ grows,the secondtermdominates, and the parallel time complexity is O(bx(d-logb p). The speedup is the sequential time complexity divided by the parallel time complexityor

$$
O \left( \frac { b ^ { x d } } { b ^ { x ( d - \log p _ { b } p ) } } \right) = O \left( b ^ { x d - x ( d - \log p ) } \right) = O \left( b ^ { ( \log _ { b } p ) x } \right) = O ( p ^ { x } )
$$

To test the DTS algorithm, Ferguson and Korf (1988) have implemented the game of Othello. Their node-ordering function results in an effective branching factor of about b.66. The program implements parallel alpha-beta search using the DTS algorithm. Ferguson and Korf executed the algorithm on 40 midgame positions using 1, 2, 4, 8, 16,and 32 nodes of an Intel iPSC hypercube multicomputer. They estimated the speedup achieved by the program by dividing the number of node evaluations performed by the sequential algorithm by the number of node evaluations performed per processor by the parallel algorithm. For example, they estimate an average speedup of 10 for 32 processors. Figure 13-20 plots the speedup achieved by their algorithm.

Ferguson and Korf have implemented another processor allocation strategy,called bound-and-branch, which corresponds closely to the algorithm described at the end of the last subsection. When the search reaches a type 1 node,all processors are allocated to the leftmost child. After the search returns with cutoff bounds from the subtree rooted by the leftmost child, the processors are assigned to the remaining children nodes in a breadth-first manner. When the search reaches a node having type 2 or 3, cutoff bounds already exist, and the processors are assigned in breadth-first fashion.

Ferguson and Korf have empirically determined that the bound-and-branch strategy achieves higher speedup than the breadth-first allocation strategy,even when the node ordering is not perfect. They have implemented a version of the Othello program that uses iterative deepening and the bound-and-branch

![](images/842ca6fe6790250cced4d63e58f8057dff5de7ab239441c43da4742b65bf1153.jpg)

# FIGURE 13-20

Speedup achieved by the DTSalgorithm forgame of Othello on Intel iPSC. Solid line represents boundand-branch processor allocationstrategy;dashed linerepresents breadth-first strategy (Fergusonand Korf 1988）.

processor allocation strategy. The actual speedup achieved by the program is 12 on 32 processors.

# 13.7 SUMMARY

One way to differentiate between combinatorial search problems is to categorize them by the kind of state space tree they traverse. Divide-and-conquer algorithms traverse AND trees: the solution to a problem or subproblem is found only when the solution to all its children is found. Branch-and-bound algorithms traverse OR trees: the solution to a problem or subproblem can be found by solving any of its children. Game trees contain both AND nonterminal nodes and OR nonterminal nodes.

Parallel combinatorial search algorithms for all these trees have been proposed. The speedup achievable through the paralel search of an AND tree is limited by propagation and combining overhead.

Mohan (1983) has implemented programs to solve the traveling salesperson problem on a NUMA multiprocessor. Quinn (1990) has implemented programs to solve the same problem on hypercube multicomputers. Their work demonstrates the potential for implementing branch-and-bound algorithms on MIMD computers. The fundamental problem faced by designers of parallel branch-andbound algorithms is keeping the efficiency of the processors high by focusing the search on the nodes the sequential algorithm examines.

Lai and Sahni (1984) have given examples of state space trees for which parallel best-first branch-and-bound algorithms can show anomalous behavior, such as superlinear speedup. Experiments they have performed with the simulated parallel solution of the O-1 knapsack problem show that anomalous behavior can really occur, albeit rarely.

Alpha-beta search has proven to be an efficient method for evaluating game trees. Several improvements on the standard alpha-beta search have been invented, including aspiration search and iterative deepening. Several methods have been proposed to parallelize alpha-beta search. These methods include parallel move generation and evaluation, parallel aspiration search,and the parallel search of independent subtrees. Only the third method seems to have enough parallelism to scale to massively parallel machines. Minimizing communication overhead can cause an unacceptable amount of search overhead, and vice versa.Ferguson and Korf (1988) have developed the bound-and-branch strategy to keep an acceptable balance while minimizing the two kinds of overhead.

# 13.8 BIBLIOGRAPHIC NOTES

Ibaraki (1976a, 1976b) has analyzed sequential branch-and-bound algorithms.

Imai et al. (1979) wrote an early paper describing a paralel branch-andbound algorith.Wahetal.(1984985)ssiutersif ically designed to execute best-first branch-and-bound algorithms. They also describe parallelism in dynamic programming. Kumar and Kanal (1983) recast branch-and-bound algorithms to encompass AND/OR tree search as well as OR tree search. Other papers on parallel branch-and-bound algorithms include Dehne et al. (1990), Janakiram et al. (1988), Kalé and Saletore (1990), Kumar and Kanal (1984),Li and.Wah (1984a, 1984b),Troya and Ortega (1989),and Wah et al. (1990).

Balas et al. (1991) have used a parallel branch-and-bound algorithm to solve a 30,000-city traveling salesperson problem on the Butterfly Plus NUMA multiprocessor.

Deriving results similar to those of Lai and Sahni (1984), Quinn and Deo (1986)describe anomalous behaviorof branch-and-bound algorithms.

Knuth and Moore (1975) analyzed the sequential alpha-beta algorithm.

Marsland and Campbell (1982) wrote an early survey paper describing the parallel search of strongly ordered game trees. Their treatment is much more detailed than the one presented in this chapter, and they cover many more interesting variations of parallel alpha-beta search. Parallel alpha-beta search has also been explored by Finkel and Fishburn (1982).

Hyatt et al. (1989) develop the mathematics for predicting the performance of parallel implementation of the principal variation splitting (PvS) algorithm. They also describe an enhancement that improves the performance of the parallel algorithm in most test cases, and they have implemented their parallel PVS algorithm on a Sequent Balance.

Huntbach and Burton (1988) describe the implementation of parallel alphabeta search on the virtual tree machine,a network of processors.Schaeffer (1989) also describes parallel alpha-beta search algorithms on computer networks.

Bhattacharya and Bagchi (199o) describe a parallelization of the $S S S ^ { * }$ search algorithm.Their work is based on the DTSalgorithmdescribed in this chapter.

Newbor (1989) hassurveyed the progressincomputer chess during the 1980s and briefly describes parallel search techniques.

Felten and Oto (1988)present the results of implementing a parallel chess program on the nCUBE 3200 multicomputer. They report a speedup of up to 100on a 256-processor system. Their algorithm has many similarities to the DTS algorithm, but it has manyother enhancements as well.

Earlier in the chapter we pointed out that the quality of play usually improves as the game tree search is depened. Nau has shown that this rule of thumb is not true for an infinite class of pathological game trees.However, he adds that “pathology does not occur in games such as chess or checkers” (Nau 1982).

13-1 Explain this statement by Wah etal. (1985): Multiprocessing is generally used to improve the computational eficiency of solving a given problem,not to extend the solvable problem space of the problem (their italics).

13-2Given a divide-and-conquer algorithm whose complexity is described by the recurrence relation

$$
\begin{array} { l } { { T ( n ) = \Omega ( n ) + k T \left( \displaystyle \frac { n } { k } \right) } } \\ { { { } } } \\ { { T ( 1 ) = \Omega ( 1 ) } } \end{array}
$$

derive a lower bound on the complexity of a parallel divide-and-conquer algorithm,assuming that the decomposition step [with complexity $\Omega ( n ) ]$ cannot be made parallel.

13-3Using the 8-puzzle as an example, explain why it is likely that a depth-first search of the state space tree would not yield a solution.   
13-4 Justify the deepness heuristic used by the best-first search strategy to choose between unexamined subproblems sharing the smallest lower bound.   
13-5 In the context of Theorem 13.2, why must at least one critical node be examined every iteration when $p > 1 2$   
${ \bf 1 3 - 6 ^ { * } }$ Prove Theorem 13.3.   
13-7 In the contextof Theorem 13.4, why must allcritical nodes be expanded before the algorithm can terminate?   
13-8 Explain the difficulties faced by an implementor of a parallel best-first branchand-bound algorithm on a multicomputer. Describe possible solutions to these difficulties.   
13-9 If a perfect evaluation function existed, the need for searching would be eliminated. Explain.   
13-10 Use the minimax algorithm to evaluate the game tree of Fig. 13-21.

![](images/9ee8564327f294aa442dc116935ae4a6c8941796141ebb05d2e039831e29ad20.jpg)

FIGURE 13-21 A game tree.③ ② ⑥ ②①①⑤

13-11 Use the alpha-beta algorithm to evaluate the game tree of Fig. 13-21.   
13-12 Extend theperfectlyordered game treeofFig.13-19byone level toillustrate how nodes are pruned at level 4. Assume a branching factor of 2.   
13-13 Reorganize the game tree of Fig. 13-16a so that it is a perfectly ordered game tree.Indicate which subtrees would be pruned by the alpha-beta algorithm.   
13-14 Explain why sequential depth-first search is simply a special case of DTS,when the DTS algorithm is provided only a single processor.   
${ \bf 1 3 - 1 5 ^ { * } }$ Prove this theorem: Given a perfectly ordered game tree,the bound-and-branch allocation strategy causes the parallel DTS algorithm to evaluate the same nodes as the sequential alpha-beta algorithm.

This section consolidates the definitions of graph theoretic terms used throughout this book. It also contains brief descriptions of data structures used to represent graphs.

A graph $G = ( V , E )$ consists of $V$ ,a finite set of vertices, and $E$ ,a finite set of edges between pairs of vertices. In an undirected graph the edges have no orientation; in a directed graph every edge is an ordered pair $( u , v )$ and is said to go from $\boldsymbol { u }$ to $v$ See Fig. A-1.

A weighted graph has a real number, called the weight, assigned to each edge. Depending upon the context, it may be more appropriate to think of the weight of a weighted graph's edge as a length, a time, a probability, or some other attribute.

The number of vertices in a graph is referred to by the letter $n$ ,and $\dot { m }$ denotes the number of edges in a graph.

Four graph representations are common. An unweighted graph can be represented by an $n \times n$ matrix,with one row and one column for each vertex. The element at row $i$ and column $j$ is equal to 1 if and only if there is an edge from vertex $i$ to vertex $j$ ; the value is O otherwise. This matrix is called an adjacency matrix. Weighted graphs can be represented by a weight matrix, that

FIGURE A-1 Undirected and directed graphs. Undirected graph $G$ hasvertices $^ { A , B , C }$ ,and $D$ and edges $( A , B )$ ， $( A , C )$ ， $( A , D )$ and $^ { ( B , D ) }$ .Directed graph $G ^ { \prime }$ hasvertices $H , I , J$ ,and $\kappa$ andedges $( H , I ) , ( H , J ) , ( J , H )$ and $( J , K )$ Edge $( H , J )$ goes from $H$ to $J$ .Edge $( J , H )$ goes from $J$ to $H$

![](images/5a752a41298342baf43b68c20d066f051841192f04a74b47d76f00cdb9a8a869.jpg)

![](images/fb92463a0a26b4b96d81efd4f292d59bbef887f62b619c3996e8903d2b578f26.jpg)  
FIGURE A-2 A weighted directed graph and its corresponding weight matrix. Depending upon the algorithm,nonexistent edges maybe representedasO oras $\infty$ in the weight matrix. In this example nonexistent edges are represented as 0.

<table><tr><td colspan="6">ABCDE 05070</td></tr><tr><td rowspan="2">A</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>B00700</td></tr><tr><td rowspan="3"></td><td></td><td></td><td></td><td></td><td>C03002</td></tr><tr><td></td><td></td><td></td><td></td><td>D60200</td></tr><tr><td></td><td></td><td></td><td></td><td>E00410</td></tr></table>

is similar to an adjacency matrix, except that the value of the matrix element at row $i$ and column $j$ gives the weight of the edge from vertex $i$ to vertex $j$ . Nonexistent edges may be represented by either O or $\infty$ entries, depending upon the particular problem being solved. Figure A-2 illustrates a weighted directed graph and its weight matrix.

Another representation stores a graph as a list of edges and a cardinal number indicating the number of vertices. A third representation uses adjacency lists—a list,for every vertex,of the edges leaving that vertex.A fourth representation, often used to represent digitized picture input, consists of a two-dimensional boolean matrix.If we label the elements 1 and O, then the set of vertices consists of the matrix elements having the value 1; the set of edges is the set of all pairs of vertically or horizontally adjacent 1s.

A path from $v _ { 1 }$ to $\upsilon _ { i }$ in a graph $G = ( V , E )$ is a sequence of edges $( v _ { 1 } , v _ { 2 } )$ ， $( v _ { 2 } , v _ { 3 } )$ ， $( v _ { 3 } , v _ { 4 } ) , \ldots$ $( v _ { i - 2 } , v _ { i - 1 } )$ ， $( v _ { i - 1 } , v _ { i } )$ ,such that every vertex is in $V$ ,every edge is in $E$ , and no two vertices are identical.

A cycle in a graph $G = \left( V , E \right)$ is a sequence of edges $( v _ { 1 } , v _ { 2 } )$ ， $( v _ { 2 } , v _ { 3 } )$ ， $( v _ { 3 } , v _ { 4 } )$ ，··， $( v _ { i - 1 } , v _ { i } )$ ， $( v _ { i } , v _ { 1 } )$ , such that every vertex is in $V$ ,every edge is in $E$ ,and only the first and last vertices in the sequence of edges are identical. A graph without cycles is said to be acyclic.

There are two common shortest-path problems. Given a weighted, directed graph $G = ( V , E )$ ,theall-psestoistfd pair of vertices $i$ ， $j \in V$ , the shortest path from $i$ to $j$ along edges in $E$ .Given a weighted, directed graph $G = ( V , E )$ and a vertex $s \in V$ , the single-source shortest-pthoistondree $i \in V$ ,the shortest path from $s$ to $i$ along edges in $E$ .FigureA-3 illustrates these two kinds of shortest-path problems.

A subgraph of a graph $G$ is a graph with vertices and edges in $G$

An undirected graph is connected if, for every pair of vertices i and j in $G$ , there is a path from $i$ to $j$ .The connected component problem is to find, for some undirected graph G, the minimal set of subgraphs such that every subgraph is connected (Fig. A-4). This problem is also known as the component Iabeling problem, since by the end of the algorithm every component's vertices share a label unique to that component. The connected 1s problem is the connected component problem applied to digitized picture input (the fourth graph representation described earlier).

![](images/03d410464c1ea776de726c4cae0e97ce09c22523cbd00911d7ec5192b9d102e6.jpg)  
FIGURE A-3 Shortest-path problems. (a) Al pairs. (b) Single source.

![](images/fcd235f5de52782dffbe3eeaeef3c9ef5d5a5c8fcd22023827bda5b95b873f72.jpg)  
FIGURE A-4 Connected components.

A tree is a connected, undirected acyclic graph. A spanning tree for a graph $G$ is a subgraph that is a tree containing every vertex of $G$ .The weight of a spanning tree of a weighted graph is the sum of the weights of the tree's edges. Given a weighted,undirected graph $G$ , a minimum-cost spanning tree of $G$ is a spanning tree with the smalest possible weight among all spanning trees of $G$ (see Fig. A-5).

In some problems involving trees a particular vertex is designated as the root. In these problems the height of the tree is the maximum distance from the root of the tree to a leaf. Every edge $\left( u , ~ v \right)$ in a rooted tree establishes a parent-child relationship between the two vertices. The parent is the vertex closer to the root; the child is the vertex farther from the root.

![](images/57577207cf80e40b34a2f84c06bf77e3622afa2b3ed5c5dbc2eabc09d8adb75b.jpg)  
FIGURE A-5 Minimum-cost spanning tree problem. (a) Weighted graph. (b) Minimum-cost spanning tree.

![](images/ea1dd72291fd7c620da8bf10037b9cca9699ca8d43ba086cab92d0734fdc04b1.jpg)  
FIGURE A-6 Complete binary trees of height one, two, and three.

A binary tree is a rooted tree in which no node has more than two children. A complete binary tree isa binary tree of height $n$ having $2 ^ { n + 1 } - 1$ nodes (of which $2 ^ { n }$ are leaves). Figure A-6 illustrates complete binary trees of height one, two,and three.

A binomial tree of height O is a single node. For all $i > 0$ ,a binomial tree of height $i$ is a tree formed by connecting the roots of two binomial trees of height $i - 1$ with an edge and designating one of these roots to be the root of thenew tree.A binomial tree of height $n$ has $2 ^ { n }$ nodes. Figure A-7 illustrates binomial trees of height one through four.

![](images/125945e88899b444a3a14be4540a86fab9b3649a727d9bb1430f5bfcfc385bd9.jpg)  
FIGURE A-7 Binomial trees of height one through four.

In this section we review how to perform arithmetic on complex numbers. The material in this section closely follows the presentation of Weaver (1983).

A complex number is an ordered pair of real numbers, denoted $( x , y )$ .We call x the real part of the complex number and y the imaginary part. Two complex numbers $( x _ { 1 } , y _ { 1 } )$ and $( x _ { 2 } , y _ { 2 } )$ are equal if and only if $x _ { 1 } = x _ { 2 }$ and $y _ { 1 } = y _ { 2 }$ ·

Let $z _ { 1 } = ( x _ { 1 } , y _ { 1 } )$ and $z _ { 2 } = ( x _ { 2 } , y _ { 2 } )$ be two complex numbers. The sum of these complex numbers is

$$
z _ { 1 } + z _ { 2 } = ( x _ { 1 } + x _ { 2 } , y _ { 1 } + y _ { 2 } )
$$

Let $z _ { 1 } = ( x _ { 1 } , y _ { 1 } )$ and $z _ { 2 } = ( x _ { 2 } , y _ { 2 } )$ be two complex numbers. The product of these complex numbers is

$$
z _ { 1 } z _ { 2 } = ( x _ { 1 } x _ { 2 } - y _ { 1 } y _ { 2 } , x _ { 1 } y _ { 2 } + y _ { 1 } x _ { 2 } )
$$

Addition and multiplication with complex numbers is commutative, associative, and distributive.

Any real number $x$ can be represented as the complex number $( x , 0 )$

Three special complex numbers are the zero element, the unit element, and the imaginary unit element.

The zero element, denoted 0, is the complex number $( 0 , 0 )$

The sum of any complex number $z$ and the zero element is $z$

$$
z + \mathbf { 0 } = ( x , y ) + ( 0 , 0 ) = ( x + 0 , y + 0 ) = ( x , y ) = z
$$

The product of any complex number $z$ and the zero element is $\mathbf { 0 }$

$$
z \mathbf { 0 } = ( x , y ) ( 0 , 0 ) = ( x \times 0 - y \times 0 , x \times 0 + y \times 0 ) = ( 0 , 0 ) = \mathbf { 0 }
$$

The unit element, denoted 1, is the complex number $( 1 , 0 )$

The product of any complex number $z$ and the unit element is $z$ ：

$$
z \times { \bf 1 } = ( x , y ) ( 1 , 0 ) = ( x \times 1 - y \times 0 , 1 \times y + 0 \times x ) = ( x , y ) = z
$$

The imaginary element, denoted $i$ ,is the complex number $( 0 , 1 )$ . The imaginary element is the square root of $^ { - 1 }$ ：

$$
{ \mathrm { \Omega } } i ^ { 2 } = ( 0 , 1 ) ( 0 , 1 ) = ( 0 \times 0 - 1 \times 1 , 0 \times 1 + 1 \times 0 ) = ( - 1 , 0 ) = - 1
$$

Theorem B.1. Every complex number $z = ( x , y )$ can be represented as $x + i y$

Proof. The real number $x = ( x , 0 )$ . The product of real number $y$ with the imaginary element $i$ is

$$
i y = ( 0 , 1 ) ( y , 0 ) = ( 0 \times y - 1 \times 0 , 0 \times 0 + y \times 1 ) = ( 0 , y )
$$

Hence

$$
x + i y = ( x , 0 ) + ( 0 , y ) = ( x , y )
$$

See Fig. B-1. We have represented the complex number $z$ as $x + i y$ ,where the horizontal axis corresponds to the real part of $z$ and the vertical axis corresponds to the imaginary part of $z$

We can also think of $z$ as a vector having length $r$ and angle $\theta$ ,where $\theta$ is measured counterclockwise from the real axis. Note that

$$
\begin{array} { r } { x = r \cos \theta } \\ { y = r \sin \theta } \end{array}
$$

Using these equations we can write $z = x + i y = r ( \cos \theta + i \sin \theta )$

![](images/72a0f4d2ea604977aa51362083f4e3ec14bbffbb753bc48df4a2864662aba7b4.jpg)  
FIGURE B-1 Every complex number $z$ can be represented as an ordered pair of real numbers $( x , y )$ ,where $x$ is the real part and $y$ isthe imaginary part. It can also be represented as a vector having length $r$ and angle $\theta$ ，where $\theta$ is measured counterclockwise from the real axis.

When we study the discrete Fourier transform we want to represent z in exponential form, which we derive here. Using Taylor series we can show

$$
\begin{array} { l } { { \sin \theta = \theta - \displaystyle \frac { \theta ^ { 3 } } { 3 } + \frac { \theta ^ { 5 } } { 5 } - \frac { \theta ^ { 7 } } { 7 } + \dots } } \\ { { \mathrm { c o s } \theta = 1 - \displaystyle \frac { \theta ^ { 2 } } { 2 } + \frac { \theta ^ { 4 } } { 4 } - \frac { \theta ^ { 6 } } { 6 } + \dots } } \\ { { \mathrm { e } ^ { i \theta } = 1 + i \theta - \displaystyle \frac { \theta ^ { 2 } } { 2 } - \frac { i \theta ^ { 3 } } { 3 } + \frac { \theta ^ { 4 } } { 4 } + \frac { i \theta ^ { 5 } } { 5 } + \dots } } \\ { { \mathrm { } } } \\ { { = ( 1 - \displaystyle \frac { \theta ^ { 2 } } { 2 } + \frac { \theta ^ { 4 } } { 4 } + \dots ) + i ( \theta - \displaystyle \frac { \theta ^ { 3 } } { 3 } + \frac { \theta ^ { 5 } } { 5 } + \dots ) } } \end{array}
$$

Combining these equations yields

$$
e ^ { i \theta } = \cos \theta + i \sin \theta
$$

and

$$
e ^ { - i \theta } = \cos \theta - i \sin \theta
$$

Recall that $z = x + i y = r ( \cos \theta + i \sin \theta )$ .Hence

$$
z = r e ^ { i \theta }
$$

is another way to represent a complex number.

One property of the exponential representation of complex numbers is that it simplifies multiplication and division. Let z1 = r1e91 and z2 = r2e be two complex numbers. Then

$$
\begin{array} { l } { { z _ { 1 } z _ { 2 } = r _ { 1 } e ^ { \theta _ { 1 } } r _ { 2 } e ^ { \theta _ { 2 } } = r _ { 1 } r _ { 2 } e ^ { \theta _ { 1 } + \theta _ { 2 } } } } \\ { { \ } } \\ { { z _ { 1 } / z _ { 2 } = ( r _ { 1 } e ^ { \theta _ { 1 } } ) / ( r _ { 2 } e ^ { \theta _ { 2 } } ) = ( r _ { 1 } / r _ { 2 } ) e ^ { \theta _ { 1 } - \theta _ { 2 } } } } \end{array}
$$

A complex nth root of unity is a complex number $\omega$ such that $\omega ^ { n } = \bf { 1 }$ ,the unit element.

There are exactly $n$ complex nth roots of unity, representated by $e ^ { 2 \pi i k / n }$ for $k = 1 , 2 , \ldots , n - 1$

The complex number $e ^ { 2 \pi i / n }$ ,denoted $\omega _ { n }$ , is the principal nth root of unity.

Figure B-2 illustrates the principal eighth root of unity and its powers, the other complex eighth roots of unity.

Lemma B.1. (Cancellation lemma) For any integers $n \ge 0 , k \ge 0$ ,and $d > 0$ $\omega _ { d n } ^ { d k } = \omega _ { n } ^ { k }$

![](images/3f87e1dd17254f85c4cb82d3721b0ed1e7cc91fb9b57f96c443acc52ab0256ac.jpg)  
FIGURE B-2 The principal eighth root of unity and its powers.

Proof.

$$
\omega _ { d n } ^ { d k } = \left( e ^ { 2 \pi i / d n } \right) ^ { d k } = \left( e ^ { 2 \pi i / n } \right) ^ { k } = \omega _ { n } ^ { k }
$$

Corollary B.1. For any even integer $n > 0$ ， $\omega _ { n } ^ { n / 2 } = \omega _ { 2 } = - 1$

Proof.

$$
\omega _ { n } ^ { n / 2 } = \omega _ { ( n / 2 ) 2 } ^ { ( n / 2 ) 1 } = \omega _ { 2 } ^ { 1 } = \omega _ { 2 } = - 1
$$

Lemma B.2. (Halving lemma) If $n$ is an even positive number, then the squares of the $n$ complex nth roots of unity are identical to the $n / 2$ complex $( n / 2 ) \mathrm { t h }$ roots of unity.

Proof. By the cancelation lemma we know that if $\omega _ { { \frac { n } { n } } / 2 } ^ { k }$ $k$ is nonnegative then $( n / 2 ) \mathrm { t h }$ $( \omega _ { n } ^ { k } ) ^ { 2 } =$ root

$$
( \omega _ { n } ^ { k + n / 2 } ) ^ { 2 } = \omega _ { n } ^ { 2 k + n } = \omega _ { n } ^ { 2 k } \omega _ { n } ^ { n } = \omega _ { n } ^ { 2 k } = ( \omega _ { n } ^ { k } ) ^ { 2 }
$$

The following list contains each parallel algorithm design strategy and the page number on which it appears:

1. If a cost optimal CREW PRAM algorithm exists, and the way the PRAM processors interact through shared variables maps onto the target architecture, a PRAM algorithm is a reasonable starting point (p. 159). 2. Look for a data-parallel algorithm before considering a control-parallel algorithm (p. 168). 3. As problem size grows,use the algorithm that makes best use of the available resources (p. 171). 4. Let each procesor perform the most eficient sequential algorithm on its share of the data (p. 172). 5. If load balancing is not a problem, maximize grain size (p. 188). 6. Reduce average memory latency time by increasing locality (p.190). 7.Eliminate contention for shared resources by changing temporal order of data accesses (p. 191). 8. Change data structures to reduce the amount of contention for the same shared resource (p. 321).

Acyclic Refers to a graph without any cycles.   
Adjacency Matrix A boolean matrix that indicates if there is an edge from $i$ to $j$ for each pair of vertices $i$ and $j$ in a graph.   
All-Pairs Shortest-Path Problem Given a weighted graph, find the shortest path between every pair of vertices.   
Alpha-Beta Pruning An algorithm used to determine the minimax value of a game tree.Alpha-beta pruning prevents the search of subtrees whose evaluation cannot influence the outcome of the search.   
Amdahl Effect (1) As the problem size increases,the fraction $f$ of inherently sequential operations decreases, making the problem more amenable to parallelization, (2) For any fixed number of processors, speedup is usually an increasing function of problem size.   
Amdahl’s Law If $f$ is the fraction of operations in a computation that must be performed sequentially,the maximum speedup that can be achieved with $p$ processors is $\leq 1 / ( f + ( 1 - f ) / p )$   
AND TreeA search tree with nonterminal nodes that are all AND nodes.   
AND/OR Tree A search tree with both AND and OR nonterminal nodes.   
Applicative Language A language that performs allcomputations by applying functions to values.   
ARBITRARY PRAM CRCW PRAM with the atribute that if multiple processors simultaneously write tothesame global register,oneof thecompeting processors is arbitrarily chosen the“winner,” and its valueis writen into theregister.   
Aspiration Search Enhancement to alpha-beta algorithm that attempts to reduce the number of positions evaluated by beginning the search with an alpha-beta“window” smaller than $( - \infty , \infty )$   
Asynchronous Algorithm A control-paralel algorithm that is not pipelined.   
AVL Tree Binary tree having the property that, for any node v in the tree, the difference in height between the left and right subtrees of node u is no more than 1.   
Bandwidth (1) Data transfer rate;(2) the value 1+2k, where k is the largest number of columns from the main diagonal any nonzero element of a matrix can be.   
Bank Unit of interleaved memory,allowing only a single read or write at & time. Also called a module.   
Barrier A synchronization point. No process may continue execution beyond the barier until all processes have reached thebarier.   
Batch Search A concurrent search for a number of keys.   
Binary $n$ Cube Hypercube.   
Binary Tree A rooted tre in which no node has more than two children.   
Binary Tree Network A network in which the nodes are arranged as a complete binary tree.   
Binomial Tree A recursively defined tree with 2 nodes and depth k.   
Bisection Bandwidth Bisection width of processor organization multiplied by link bandwidth.   
Bisection Width The minimum number of edges that must be removed in order to divide a network into two halves of identical size (within one).   
BitonicMergeAparalelalgorithm tomerge twobitonic sequences oflength $2 ^ { k }$ into asinglebitonic sequenceof length $2 ^ { k + 1 }$ in $k + 1$ steps.   
Bitonic Sequence A sequence of numbers ao,a1.,an-1 with the property that (1) there exists an index i, O ≤i ≤n-1,such that ao through ai are monotonically increasing and ai through an-1 are monotonicaliy decreasing, or (2) there exists a cyclic shift of indices so that condition 1 is satisfied.   
Block Matrix Multiplication Algorithm analogous to standard matrix multiplication, where matrices replace scalars, standard matrix multiplication replaces scalar multiplicationadtrixdiiacsar   
Bound and Branch Processor allocation strategy for paralel alpha-beta search.   
Branch and Bound Algorithm for searching OR trees with the goal of finding an optimal solution while minimizing the total number of nodes examined.   
Brent’s Theorem Given $A$ ,a parallelalgorithmwithcomputationtime $t$ , if parallel algorithm A performs $m$ computational operations, then $p$ processors can execute algorithm $A$ in time $t + ( m - t ) / p$   
Broadcast When one processor sends a value or set of values to all other processors.   
Buffer Deadlock A kind of deadlock that can occur in multicomputers when message buffers fill up.   
Busy-WaitingUsing processor cycles to test a variable until it assmes a desired value. Also called spinning.   
Buterfly Network A processor organization containing $( k + 1 ) 2 ^ { k }$ nodes, divided into $2 ^ { k }$ columns and $k + 1$ rows,orranks in which edges form"butterfly”patterns.   
Cache MemorySmall,fast memory unit used as abuer between a processor and primary memory.   
Centralized Load Balancing Algorithm Load balancing algorithm that makes a global decision about the reallocation of work to processors.   
Chain A totally ordered task graph.   
Chaining Method of increasing concurrency by connecting the output of one or more pipelines to the input of another pipeline.

Channel (1) I/O processor, (2) In the programming language occam, a point-to-point, synchronous communication link from one process to another process.

Child The vertex $u$ or $v$ farther from the root, given an edge $( u , v )$ establishing a parent-child relationship between two vertices in a rooted tree.

Circuit-Switched Message Routing Message-passing scheme in which a circuit is setup from the source processor to the destination processor,and the message flows in a pipelined fashion through the intermediate processors. None of the intermediate processors stores the message.

COMMON PRAM CRCW PRAM with the restriction that if multiple processors simultaneously write to the same global register,they must be writing the same value.

Communication Overhead In a parallel game-tree search, the time spent coordinating the processes performing the searching.

Comparator A device that performs the compare-exchange operation in bitonic merge

Compare-Exchange Fundamental operation of bitonic merge algorithm. Two numbersare brought together,compared,thenexchanged,if necessary,sothat they are in the proper order.

Complete Binary Tree A binary tree of height $n$ having $2 ^ { n + 1 } - 1$ nodes (of which $2 ^ { n }$ are leaves).

Complex nth Root of Unity A complex number $\omega$ such that $\omega ^ { n } = 1$

Complex Number Ordered pair of real numbers. First element is real part; second element is imaginary part.

Complexity Measure of time or space used by an algorithm. Without adjective, refers to time complexity.

Component Labeling Problem Given an undirected graph $G$ ,find the minimal set of subgraphs such that every subgraph is connected. Also known as the connected component problem.

Connected Given undirected graph $G$ ,the property that for every pair of vertices i and $j$ in $G$ , there isa path from $i$ to $j$ in $G$

Connected 1s Problem Connected component problem applied to digitized picture input,where each pixel isa bit.

Connected Component Problem Given an undirected graph $G$ ,find the minimal set of subgraphs such that every subgraph is connected. Also known as the component labeling problem.

Control Parallelism Paralelism achieved through the simultaneous application of different operations to different data elements.

Copy-Back Cache Caching policy in which values in modified cache block are not copied to system memory until cache block is swapped out or another processor tries to access a data item in that block.

Cost Product of the time complexity of an algorithm and the maximum number of processors used.

Cost Optimal Parallel algorithm for which the cost is in the same complexity class as an optimal sequential algorithm.

CRCW PRAM Concurrent read, concurrent write PRAM.

CREW PRAM Concurrent read, exclusive write PRAM.

Critical Node The root of a subtree about which a rebalancing will take place when a node is inserted into an AVL tree.

Critical Section A sequence of operations that must appear to be executed as an atomic operation.

Cube-Connected Cycles Network A butterfly network whose lowest and highest ranks have been combined into a single rank.

Cube-Connected Network Hypercube.

Cubical Describes a graph that can be embedded into a hypercube with dilation 1.

Cycle Same as path, except the first and last vertices are identical.

Cyclic Reduction Recursive algorithm used to solve tridiagonal linear systems. Alsc called odd-even reduction.

Data-Flow An architecture in which the sequence of instruction execution depends not on a program counter,but on the availability of data.

Data-Flow Analysis Process of finding the data dependencies among instructions.

Data-Flow Graph (1) Machine language for a data-flow computer; (2) result of data flow analysis.

Data Parallelism The use of multiple functional units to apply the same operation simultaneously to elements of a data set.

Data Stream Sequence of data manipulated by an instruction stream.

de Bruijn Network A network with n = 2 nodes labeled O,1,...,n -1. Two edges leave each node. From node i one edge leads to node (2i modulo n); the other edge leads to node ( $2 i$ modulo $n$ $+ 1$ -

Deadlock A situation in which a set of active concurrent processes cannot proceed because each holds nonpreemptible resources that must be acquired by some other process.

Decision Problem A problem with a solution (if any) that is found by satisfying a set of constraints.

Depth Maximum level of any task in a task graph.

Deque A double-ended queue; i.e.,a list of elements on which insertions and deletions can be performed at both the front and the rear.

Deterministic Model A task model in which precedence relations between tasks and the execution time needed by each task are fixed and known before the schedule is devised.

DFT Discrete Fourier transform.

Diagonally Dominant Refers to a matrix in which the magnitude of each diagonal element is greater than the sums of the magnitudes of the other matrix elements in the same row.

Diameter The largest distance between any two nodes in a network.

Dilation $\operatorname* { m a x } \{ d i s t [ \phi ( u ) , \phi ( v ) ] | ( u , v ) \ \in \ E \}$ ，given $\phi$ ,a function that embeds graph $G = ( V , E )$ into graph $G ^ { \prime } = ( V ^ { \prime } , \ E ^ { \prime } )$ ,and where $d i s t [ a , b ]$ is the distance between vertices $^ a$ and $b$ in $G ^ { \prime }$ ·

Directed Graph Graph with ordered edges.

Discrete Fourier Transform The matrix-vector product $F _ { n } x$ ,where $x$ isan $n$ -element vector, $\omega _ { n } = e ^ { 2 \pi i / n }$ ,and $f ( i , j ) = \omega _ { n } ^ { i j }$ for $0 \leq i$ ， $j < n$

Divide and Conquer A problem-solving methodology that involves partitioning a problem into subproblems, solving the subproblems,then combining the subproblem solutions into a solution for the original problem.

Dynamic Decomposition A task-allocation policy that assumes tasks are generated at execution time.

Dynamic Scheduling see Self-scheduled.

Edge Component of a graph. An edge is a pair of vertices. If the edge is directed, the pair is ordered; if the edge is undirected, the pair has no order.

Effective Branching Factor Given an algorithm searching a game tree of depth $d$ ， the dth root of the number of leaf nodes evaluated by the algorithm.

Efficiency Ratio of speedup to number of processors used.

Embedding A function mapping $V$ to $V ^ { \prime }$ ， given two graphs $G = ( V , E )$ and $G ^ { \prime } =$ $( V ^ { \prime } , E ^ { \prime } )$ ·

Enumeration Sort A sort that finds the position of each element by determining the number of elements that precede it in the ordered list.

EREW PRAM Exclusive read,exclusive write PRAM.

Even-Odd Exchange Phase of odd-even transposition sort.

Exchange One link type in a shuffe-exchange network. Exchange links connect nodes whose addresses differ in the least significant bit.

Expected Space Complexity A function $f ( n )$ equal to the average amount of space used by an algorithm over all possible inputs of size $n$

Expected Time Complexity A function $f ( n )$ equal to the average amount of time required by an algorithm over all possible inputs of size $n$

Fact In the context of logic programming, a fact is a Horn clause with a head but no body.

Fan-in Algorithm in which a setof values is combined to yield a single result. Same as reduction.

Fast Fourier Transform $\Theta ( n \ \log \ n )$ algorithm for performing the discrete Fourier transform.

FFT Fast Fourier transform.

Fifth-Generation Computer A computer system capable of knowledge processing.

Fork A method of specifying concurrency.Similar to a procedure call,but the calling process continues execution. See Join.

Fourier Analysis Study of representing continuous functions by a potentially infinite series of sinusoidal (sine and cosine) functions.

Frequency In the context of the discrete Fourier transform, the number of complet cycles a sinusoidal wave completes between time O and time $2 \pi$

From Preposition denoting the originating vertex of an edge in a directed graph.

Front End Sequential computer component found in processor arrays, as well as some multicomputers.

Fully Distributed Load Balancing Algorithm Load balancing algorithm in which processors exchange information with neighboring processors and use this informa tion to make local changes in the allocation of work.

Game Tree State space tree representation of a game position.

Gantt Chart Diagram used to illustrate a deterministic schedu

Gaussian Elimination Algorithm used to solve arbitrary linear systems.

Gaussian Elimination With Partial Pivoting Variant of gaussian elimination in which rows are interchanged when necessary to bring the largest element into the pivotal position.

Gigabyte $2 ^ { 3 0 }$ bytes.

Gigaflops Billion floating-point operations per second.

Grain Size Relative number of operations done between synchronizations in a MIMD algorithm.

Graph Set consisting of V,a finite set of vertices,and E,a finite set of edges between pairs of vertices.

Graph Coloring Problem Determine whether vertices of a graph can be colored with c colors so that no two adjacent vertices are assigned the same color.

Gray Code An encoding G of the integers 0,..,2k - 1 having the following properties: (1) $G ( i ) = G ( j ) \Rightarrow i = j$ (2) $G ( i )$ and $G ( i + 1 )$ differ in exactly one bit position, for all $i$ in the range O through $n \sim 2$ （3） $G ( 2 ^ { k } - 1 )$ and $G ( 0 )$ differ in exactly one bit position.

Height In graph theory, the length of the longest path from the root of a tree to any of its leaves.

Hot Spot Memory bank experiencing too much contention from processors.

Hypercube Boolean k-cube. Every processor has a unique address in the range from 0 to 2k-1. Processors whose addresses differ in exactly 1 bit are connected.

Hypertree Graph formed by computing the cross-product of a $k$ -ary tree of height $d$ and an upside-down binary tree of height $^ d$

Imaginary Element The complex number (0,1),denoted $i$

Imaginary Part Second component of complex number.

mmediate Predecessor Task at the tail of an edge representing a precedence relation.

Immediate Successor Task at the head of an edge representing a precedence relation.

Independent Describes a set of tasks in a task graph such that no task is the prede cessor of another.

Index Function Function mapping lists elements into a mesh-connected network.

Information Collection of related data objects.

Initial Tasks Tasks with no predecessors in the task graph

Instruction Buffering,Instruction Look-Ahead Prefetching instructions used to pre vent the CPU from waiting for an instruction to be fetched.

Instruction Pipelining Allowing more than one instruction to be in some stage of execution at the same time.

Instruction Stream Sequence of instructions performed by a CPU.

Interleaved Memory Memory divided into a number of modules or banks that can be accessed simultaneously.

Internal Sort Algorithm that orders a table of elements contained entirely in primary memory.

Inverse Discrete Fourier Transform Function that maps a sequence over frequency to another sequence over time.

Iterative Deepening Use of a $( d - 1 )$ -ply search to prepare for a $( d )$ -ply search.

Key Unique object of a search.

Knapsack problem Given a finite set of objects,each with a weight and a value, find the subset of these objects having greatest value,whilealso satisfying the constraint that the total weight of these objects must be no greater than a specified weight limit.

Length Number of tasks in a chain of a task graph.

Level Given a task $T$ in a task graph $G$ , refers to the maximum chain length from an initial task in $G$ to $T$

Light-Weight Threads Processes that can be created and destroyed with relatively few instructions.

Linear Equation An equation of the form $a _ { 1 } x _ { 1 } + a _ { 2 } x _ { 2 } + \cdot \cdot \cdot + a _ { n } x _ { n } = b$ ，where $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ are variables and $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ and $^ { b }$ are constants.

Linear System A finite set of linear equations. Also called a system of linear equations.

Linked Array Data structure designed to allow the joining of various sized lists so that the inserting and deleting of the list elements can be done in parallel without contention.

List Ranking Suffix sums applied to a list of Os and 1s when the associative operation isaddition.

Load Given an embedding $\phi : G \to G ^ { * }$ ",the maximum number of vertices of $G$ thai aremapped to a single vertex of $G ^ { \prime }$ 。

Locality of Reference The observation that references to memory tend to cluster. Temporal locality refers to the observation that a particular datum or instruction, once referenced,is often referenced again in the near future.Spatial locality refers to the observation that once a particular location is referenced,a nearby location is often referenced in the near future.

Logarithmic Cost Criterion Cost criterion that assumes the cost of performing an instruction is proportional to the length of the operands. The integer n requires $\lfloor \log n + 1 \rfloor$ bits of memory,hence the name.

Lower Triangular A matrix with no nonzero elements above the main diagonal.

LU Decomposition Process of factoring a matrix A into a product of a lower triangular matrix $\mathbf { L }$ and an upper triangular matrix U.

Max-Tournament Tournament returning the identity of the processor submiting the maximum value.

Megabyte $2 ^ { 2 0 }$ bytes.

Megaflops Million floating-point operations per second.

Mesh Network A processor organization in which the nodes are arranged into a $q$ -dimensional lattice and communication is allowed only between neighboring nodes

Message Latency Message startup time. Same as message-passing overhead.

Message-Passing Overhead Message startup time. Same as message latency.

Microsecond $1 0 ^ { - 6 }$ seconds.

Millisecond $1 0 ^ { - 3 }$ seconds.

MIMDMultiple-instruction stream, multipledata stream (category of Flynn's taxonomy). See Multicomputer and Multiprocessor.

Minimax Algorithm used to determine the value of a game tree.

Minimum-Cost Spanning Tree Given graph $G$ , a spanning tree with the smalles possible weight among all spanning trees of $G$

Minsky's Conjecture Speedup achievable by a paralel computer increases as the logarithm of the number of processing elements.

Min-Tournament Tournament returning the identity of the processor submitting the minimum value.

MISD Multiple-instruction stream, single data stream (category of Flynn's taxonomy).

Module Unit of interleaved memory,allowing onlya singleread or write ata time. Also called a bank.

Monitor A structure consisting of variables representing the state of some resource, procedures to implement operations on that resource,and initialization code.

Multicomputer A multiple-CPU parallel computer lacking a shared memory

Multiprocessor A shared memory multiple-CPU parallel computer.

Multiprogramming gAllowing more than one program to be in some state of execution at the same time.

Mutual Exclusion Ensuring a shared resource is accessed by only a single process at a time.

Nanosecond $1 0 ^ { - 9 }$ seconds.

NC Class of problems solvable in polylogarithmic time on a PRAM using a polyno-mial number of processors.

Necklace The nodes through which a data item travels by following a sequence of shuffle links in a shuffle-exchange network.

NEWS Grid A subset of wires in a Connection Machine router that forms a Cartesian mesh.

Nondeterministic Model A task model in which the execution time of each task is represented by a random variable.

Non-Uniform Memory Access Multiprocessr A multiprocessor that does not support constant-timememory access"Inmost NUAarchitecturesmemory isorganized hierarchically,so that some portions can beread and written more quickly by some processors than by others" (Wilson 1993).

NUMA Non-Uniform Memory Access.

Odd-Even Exchange Phase of odd-even transposition sort.

Ddd-Even Reduction Recursive algorithm used to solve tridiagonal linear systems

Also called cyclic reduction.

Omega Network A composition of $k$ shuffle-exchange networks, each of size $2 ^ { k }$

Optimal Schedule A schedule that minimizes the total execution time.

Optimization Problem A problem whose solution involves satisfying a set of constraints and minimizing (or maximizing) an objective function.

OR Tree A state space tree whose nonterminal nodes are all OR nodes.

Parallel Computation Thesis The class of problems solvable in time $T ( n ) ^ { o ( 1 ) }$ by a PRAM is equal to the class of problems sovable in work space $T ( n ) ^ { o ( 1 ) }$ by a RAM, if $T ( n ) \geq \log n$

Parallel Computer A multiple-processor computer capable of parallel processing.

Parallel Computing The process of solving problems on parallel computers.

Parallelism. The use of multiple resources to increase concurrency.

Parallelizability The ratio between the time taken by a parallel computer executing a parallel algorithm on one processor and the time taken by the same parallel computer executing the same parallel algorithm on $p$ processors.

Parallelization The process of making an algorithm parallel.

Parallel Prefix See Prefix Sums.

Parallel Processing Information processing that emphasizes the concurrent manipulation of data elements belonging to one or more processes solving a single problem

Parent The vertex $\boldsymbol { u }$ or $v$ closer to the root, given an edge $( u , v )$ establishing a parent-child relationship between two vertices in a rooted tree.

Partial Sum See Prefix Sums.

Path A sequence of edges $( v _ { 1 } , v _ { 2 } )$ ， $( v _ { 2 } , v _ { 3 } )$ ， $( v _ { 3 } , v _ { 4 } )$ ，...， $( v _ { i - 2 } , v _ { i - 1 } )$ ， $( v _ { i - 1 } , v _ { i } )$ in a graph $G = ( V , E )$ such that every vertex is in $V$ , every edge is in $E$ ,and no two verticesare identical.

${ \mathcal P }$ complete Describes a problem to which every other problem in $\mathcal { P }$ can be transformed in polylogarithmic parallel time using a PRAM with a polynomial number of processors.

Perfectly Ordered Game Tree Game tree in which the best move from each position is always examined first.

Perfect Shuffle See Shufffe.

Picosecond $1 0 ^ { - 1 2 }$ seconds.

Pipelined Algorithm In the context of MIMD models, a pipelined algorithm is the software analog to pipelining in hardware. The algorithm is divided into an ordered set of segments in which the output of each segment is the input of its successor.

Pipelined Computation Computation that achieves concurrency through the division of the task into a number of stages (segments) that may execute simultaneously, where the output of one stage is the input of the next stage.

Pipelined Vector Processor Vector computer implemented through the use of pipelined functional units. Examples include the Cray-1 and the Cyber-205.

Pipelining Increasing concurrency by dividing a computation into a number of steps and allowing a number of tasks to be in various stages of execution at the same time.

Pivot Row In the context of gaussian elimination, the row used to drive to zero all nonzero elements below the main diagonal in a particular column.

Ply Level of a game tree.

Pointer Jumping Parallel algorithm used to collapse linked list in logarithmic time.

Polylogarithmic The set $\log n ^ { o ( 1 ) }$

Polylogarithmic Time Complexity Time complexity that isa polylogarithmic function of the problem size.

Positive Definite Refers toa matrix that issymmetric,diagonally dominant,and has positive elements on the main diagonal.

PRAM Model of parallel computation consisting of a control unit, global memory, and an unbounded set of processors,each with its own private memory.

Prefix Sums Given a set of n values a1, a2,...,an， and an associative operation , the computation of the n quantities ai,a1 ④ a2,...,a1 a2④... an。

Prescheduled Describes a data-parallel algorithm in which the number of data items perfunctional unit is determined before any of the data items are processed.

Principal nth Root of Unity The complex number $e ^ { 2 \pi i / n }$ ，

PRIORITY PRAM CRCW PRAM with the attribute that if multiple processors simultaneously write to the same global register,the processor with the lowest index succeeds in writing its value into the register.

Processor Array Vector computer implemented as a sequential computer connected to a set of identical synchronized processing elements capable of simultaneously performing the same operation on different data.

Pyramid Network A complete 4-ary rooted tree augmented with additional interprocessor links so that the processors in every tree level form a 2-D mesh network.

RAM Random access machine.

Random Access Machine Model of a one-address computer consisting of a memory, a read-only input tape, a write-only output tape, and a program.

Random-Read A communication step in which processors generate lists of addresses-(processor, offset) pairs--from which values must be retrieved.

Kandom Uniform Game Tree A game tree whose terminal node values are randomly chosen from some uniform distribution.

Random-Write eA communication step in which processors generate lists of addresses-(processor,offset) pairs-where values are to be stored.

Rank Row of a butterfly network.

Real Part First component of complex number.

Reasonable A paralel model in which the number of processors with which each can communicate directly is bounded by a constant.

Receiver Initiated Load Balancing Algorithm A load balancing algorithm in which processors with too litle work take work from other processors.

Reduction (1) Algorithm in which a set of values is combined via an associative binary operator to yield a single result (sameas fan-in),(2) in the algorithm for the traveling salesperson problem, (Little et al.1963),the process of determining the increase in the lower bound as the result of including or excluding an edge.

Root Designated vertex of a tree.

Scalable Algorithm An algorithm in which the level of parallelism increasesat least linearly with the problem size.

Scalable Architecture An architecture that continues to yield the same performance per processor,albeit on a larger problem size,as the number of processors increases.

Scaled Eficiency Scaled speedup divided by number of processors used.

Scaled Speedup Ratio between how long a given optimal sequential program would have taken had it been able to run on a single processor of a paralel computer, and the length of time that a parallel program requires, when executing on multiple processors of the same parallel computer.

Scan See Prefix Sums.

Schedule An allocation of tasks to processors.

Search Overhead In a game-tree search, the increase in the number of nodes that must be examined owing to the introduction of parallelism.

Segment Fundamental unit of a pipeline. Also calld a stage.

Self-Scheduled Describes a data-parallel algorithm in which data items are dynamically scheduled to functional units at run time.

Semi-Distributed Load Balancing Algorithm A load balancing algorithm in which processors are divided into regions. Within each region a centralized algorithm distributes the workload among processors.A higher level scheduling mechanism balances the workload between regions.

Sender Initiated Load Balancing Algorithm A load balancing algorithm in which processors with too much work send work to other processors.

Sequential Algorithm An algorithm designed to run on a sequential computer.

Sequential Computer A computer with an instruction set that includes operations on scalar variables only.

Serial Sequential.

Shape Specifies the way parallel data are organized in $\mathbf { { C } ^ { * } }$

Short Necklace A necklace of length less than $k$ in a shuffle-exchange network containing $2 ^ { k }$ nodes.

Shuffle One link type in a shuffle-exchange network. For every node $i$ in a shuffleexchange network of size $n = 2 ^ { k }$ , the shuffle link leads to node $2 i$ modulo $n - 1$ ， except that the shuffle link from node $n - 1$ goes to node $n - 1$

Shuffle-Exchange Network Processor organization containing $2 ^ { k }$ nodes, labeled, $0 , 1 , . . . , 2 ^ { k - 1 }$ ，with two connections per node, called shuffle and exchange.

SIMD Single-instruction stream, multiple-data stream (category of Flynn's taxonomy). See Processor Array.

Simple Task Graph， A task graph with a polynomial representation that can be factored so that every variable appears exactly once.

Single-Source Shortest-Path Problem Problem of finding the shortest path from a single designated vertex (the source) to all the other vertices in a weighted,directed graph.

SISD Single-instruction stream, single-data stream (category of Flynn's taxonomy).

Solution A substitution of values for variables in a linear system such that every equation is satisfied.

SOR Successive overrelaxation.

Source In the single-source shortest-path problem,the vertex from which all distances are calculated.

Space Memory.

Space Complexity Memory used by an algorithm as a function of problem size

Spanning Tree Given a graph $G$ , a tree that includes every vertex in $G$

SpatialLocality Theobservation that onceaparticularlocation isreferenced,anearby location is often referenced in the near future.

Speedup Ratio between the time needed for the most efcient sequential algorithm to perform a computation and the time needed to perform the same computation on a machine incorporating pipelining and/or parallelism.

Spin Lock Shared variable used for busy waiting.

Spinning Describes an active process that continually tests the value of a spin lock, waiting for it to change. Also called busy waiting.

SPMD Single program, multiple data programming style. Programs written in this style are loosely synchronous. Between synchronization points--usually barrier synchronizations on a multiprocessor and communication functions on a multicomputerprocessors asynchronously execute the same program but manipulate their own por-tion of the data.

Spread Form of broadcast on the Connection Machine that may incorporate a scan operation.

Stage Fundamental unit of a pipeline. Also called a segment.

State Space Tree Representation of the decomposition of an original problem into subproblems through the addition of constraints.

Store-and-Forward Message Passing Message routing scheme in which every intermediate processor along the message's path must store the entire message before forwarding it to the next processor down the line.

Strong Search An algorithm that searches for a given key,locks the node associated with that key,and returns the node.

Subgraph Given graph $G$ , a graph with vertices and edges in $G$

Successive Overrelaxation A variant of the Gauss-Seidel algorithm that computes the new value of each element of the solution vector through a combination of its old value and the new value generated by the standard Gauss-Seidel algorithm

Sutfix Sums Given a set of n values ai, a2,.,al and an associative operator , the computation of the n quantities a1 ④ a2④...④an-1 ④an,...,an-1 ④ an,an.

Supercomputer A general-purpose computer capable of solving individual problems at extremely high computational speeds,compared with other computers built during the same time.

Superlinear Speedup Speedup that exceeds the number of processors used.

Symmetric Refers to a matrix A having the property that $a _ { i , j } = a _ { j , i }$ for $1 \leq i$ ， $j \le n$

System of Linear Equations Finite set of linear equations. Also called a linear system.

Table Finite set of keys.

Task Graph A directed graph representing a computation. Nodes denote tasks and edges denote precedence constraints between tasks.

Temporal Locality The observation that a particular datum or instruction,once referenced, is often referencedagain in the near future.

Terabyte $2 ^ { 4 0 }$ bytes.

Throughput Number of results produced per time unit.

Time See Time Complexity.

Time Complexity Time used by an algorithm as a function of problem size.

To Preposition denoting the destination vertex of an edge in a directed graph.

Tournament A variant of reduction with operation minimum or maximum in which the value returned is the identity of a processor submiting the “winning" value (i.e., the result of the reduction)

Traveling Salesperson Problem Given a weighted graph,find a minimum-weight cycle containing every vertex exactly once.

Tree Connected, undirected, acyclic graph.

Tridiagonal Refers to a linear system A with the property that $| i - j | > 1 \Rightarrow a _ { i , j } = 0$

TSP Traveling Salesperson Problem

Tuple Space A shared associative memory used by Linda programs.

UMA Uniform Memory Access.

Uniform Memory Access Multiprocessor A multiprocessor in which all processors work through a central switching mechanism to reach a shared global memory.

Undirected Graph A graph with edges that have no orientation.

Uniform Cost Criterion Assumes every RAM instruction takes one unit of time to execute and every register requires one unit of space.

Unit Element The complex number $( 1 , 0 )$ ,denoted1.

Upper Triangular A matrix with no nonzero element below the main diagonal.

Utilization Parallelizability divided by the number of processors used.

Vector Computer A computer with an instruction set that includes operations on vectorsaswellasscalars.

Vertex Component of a graph. Also called a node.

Virtual Processors Processing elements in an abstract model of parallel computation supported by some programming languages, such as $\mathbf { C } ^ { * }$

Weak Search A search algorithm that searches for a key and returns the node that contained the key at the time it was examined. Weak search is not guaranteed to provide an up-to-date result.

Weight (1) Real number assigned to an edge in a weighted graph; (2) sum of the weights of a spanning tree's edges.

Weighted Graph Graph with a real number assigned to each edge.

Weight Matrix A matrix indicating,for each pair of vertices $i$ and $j$ ,the weight of the edge from vertex $i$ tovertex $j$ ·

Width The size of the maximal set of independent tasks in a task graph.   
Worst-Case Space Complexity A function $f ( n )$ equal to the greatest amount of space used by an algorithm over all possible inputs of size $n$   
Worst-Case Time Complexity A function $f ( n )$ equal to the greatest amount of time spent by an algorithm over all possible inputs of size $_ n$   
Write-Through Cache Caching policy in which every data write is sent directly to system memory，and all copies of the data item in other processors’caches are invalidated.   
Zero element The complex number , denoted 0.

$( 0 , 0 )$

QA76.6.A8 ACM Transactions on Mathematical Software   
QA76.7.A281 ACM Transactions on Programming Languages and Systems   
QA76.A265 Acta Informatica   
QA76.A4 Advances in Computers   
Q335.A7 Artificial Intelligence   
QA76.N62 BIT   
QA76.C539 Communications of the ACM   
QA76.C545 Computer   
QA76.C55 Computer Journal, The   
QA76.C592 Computing Surveys   
QA76.6.I161 IEEE Software   
TK1.I47 IEEE Spectrum   
TK6540.I62 IEEE Transactions on Computers   
QA76.58.I44 IEEE Transactions on Parallel and Distributed Systems   
TK6540.I62 IEEE Transactions on Pattern Analysis and Machine Intelligence   
TK1001.I467 IEEE Transactions on Power Systems   
TK6540.I62 IEEE Transactions on Software Engineering   
Q350.I5 Information and Control   
QA76.I51 Information Processing Leters   
Call Number Title   
QA76.5.I564 International Journal of Parallel Programming   
QA76.A69 Journal of the ACM   
QA76.6.J69 Journal of Algorithms   
QA76.J6 Journal of Computer and System Sciences   
QA76.5.J73 Journal of Parallel and Distributing Computing   
T58.A2.07 Operations Research   
QA76.6.P3491 Parallel Computing   
QA267.A27 Proc. of the Annual ACM Symposium on the Theory of Computing   
TK7885.A1.S9 Proc.of the Annual Symposium on Foundations of Computer Science   
QA76.6.L58741 Proc. of the International Conference on Logic Programming   
QA76.6.I52 Proc.of the International Conference on Parallel Processing   
QA76.5.S94 Proc. of the Annual International Symposium on Computer Architecture   
QA297.S6 SIAM Journal on Computing   
QA1.S44 SIAM Review   
TJ211.S531 SIGACT News   
QA76.S58 Software Practice and Experience   
Ackerman, W.B.1982. Data flowlanguages.Computer,vol.14,no.2,Feb.,pp.15-25.   
Adams, G. B., II, D. P. Agrawal, and H. J. Siegel. 1987. A survey and comparison of fault-tolerantultisageiterconectiontworks.ComputerJune,.7   
Afrati,F.,C.H. Papadimitriou,and G.Papageorgiou.1985.Thecomplexity of cubical graphs. Information and Control, vol. 66, pp.53-60.   
Agerwala,T.,and B.Lint.1978. Communication in parallel algorithms for boolean matrix multiplication.In Proceedings of the 1978 International Conference on Parallel Processing, IEEE, New York. Aug., pp. 146-153.   
Aggarwal, A. 1984.A comparative study of X-tree,pyramid and related machines. Proceedings of the 25th Annual Symposium on Foundations of Computer Science, IEEE, New York, Oct., pp. 89-99.   
Aggarwal,A.,andR.J. Anderson.1988. A random NC algorithm for depth first search. Combinatorica,vol.8,..   
Aggarwal, A., R. J. Anderson, and M. Y. Kao. 1990. Parallel depth-first search in general directed graphs.IAMJournal onComputing,vol.19,no.2,Apr.,pp.397 409.   
Aho,A.,J.Hopcroft,and J. Ullman.1974.The Design and Analysis of Computer Algorithms.Addison-Wesley,Reading,   
Ahuja,N.,and S. Swamy. 1984. Multiprocessor pyramid architecture for"bottom-up image analysis. IEEE Transactions on Pattern Analysis and Machine Inteligence, PAMI-6, no. 4, July, pp. 463-474.   
Ahuja,R.K., K. Mehlhorn, J. B. Orlin,and R. E. Tarjan. 1990.Faster algorithms for the shortest path problem. Journal of the ACM, vol. 37, no.2,Apr., pp. 215-223.   
Ahuja,S., N. Carriero,and D. Gelernter.1986.Linda and friends. Computer,vol.19, no. 8, Aug., pp. 26-34.   
Aigner,M.1982.Parallel complexity of sorting problems. Journal ofAlgorithms,vol. 3, pp. 79-88.   
Ajtai,M., J. Komlos, and E. Szemeredi. 1983. An O(n log n) sorting network. In Proceedings of the 15th Annual ACM Symposium on the Theory of Computing,ACM, New York, May, pp.1-9.   
Akl, S. G. 1982. A constant-time parallel algorithm for computing convex hulls. BIT, vol. 22, no. 2, pp. 130-134.   
Akl, S.G. 1984a.An optimal algorithm for parallel selection. Information Processing Letters,vol. 19, no. 1, pp.47-50.   
Akl, S. G. 1984b. Optimal parallel algorithms for computing convex hulls and for sorting. Computing,vol.33,no.1,pp.111.   
Akl, S.G.985.Parallel Sorting Algorithms.Academic Press,Orlando,FL   
Akl,S.G.989.heeignandalysisofaralelgorithms.reniceHallle wood Cliffs, NJ.   
Akl, S.G., D. Barnard, and R. Doran.1982. Design,analysis,and implementation of a parallel tree search algorithm. IEEE Transactions on Pattern Analysis and Machine Intelligence,-4,ar., .9203.   
Akl, S. G., and H. Schmeck. 1984. Systolic sorting in a sequential input/output environment. In Proceedings of the 22d Annual Allerton Conference on Communication, Control,ndmuting,ct.p.6-955.   
Alaghband, G.,and H.F.Jordan.1989.Sparse gaussan elimination with controled filin ona shared memory multiprocessor.IEEE Transactions on Computers,vol.C-38, no. 11, Nov., pp. 1539-1557.   
Alef,M.1991. Conceptsforefficientmultigrid implementations onUPRENUM-like architectures.PrallelComputing,vol.17,.6.   
Aleliunas,R.and A.L.Rosenberg.1982. On embedding rectangular grids in square grids.IEEErasactions onComputers,C-31,no.9,p.0913.   
Allan,S.J.andR.R. Oldehoeft.1985.HEPSAL:Parallel functional programming. InJ.S.Kowalikdrallel mutation:HueomuedI Applicatioss,dge,p   
Allen,M.BI.eadG.ider.88.Numeicaleliginece and Engineering.John Wiley & Sons,New York.   
Almasi,G.S.andA.Gottieb.989.HghlyParallelComputing.BenjaminCummins Redwood City, CA.   
Alon,N.,and Y.Azar.1988.Theaveragecomplexityofdeterministicand randomized parallelcomparisosortingalgorithms.AJournalonComputingol.o.6 Dec., pp.1178-1192.   
Alt, H.T.Hagerup,K.Mehhorn,andF.P.Preparata.1987.Deterministicsimulation of idealizedparalelcomputersonmorerealisticones.SAMJouralonComputing, vol.16,no.5,Oct.,pp.35.   
Alton,D.A.,and D.M. Eckstein.1979.Parallel breadth-first search of p-sparse graphs. In Proceedings of the West Coast Conference on Combinatorics,Graph Theory and Computing.Cogressus Numerantiuml.26.   
Amdahl, G.1967.Validity of the single processor approach to achieving large scale computing capabilities.InAConerence Proceedings,vol.30,Apr.,on Books,Washington,DC,pp.4485.   
Anderson,A.89.ipeoessing:Atemsveiewrticelw York.   
Anarews, G. R. I981. Synchronizing resources. ACM Transactions on Programming Languages and Systems,vol. 3, no. 4, Oct., pp. 405430.   
Andrews,G.R.1982. Thedistributed programming language SR-Mechanisms,design andimplemtaiotware cticedrienceol.28ug. 754   
Andrews, G. R.,and F.B.Schneider. 1983.Concepts and notations for concurrent programming. Computing urveys,vol. 15,no.1,Mar., .43.   
Angus,I. G., G.C.Fox,J. S.Kim, and D. W.Walker.1990.Solving Problems on Concurrent rocessors,vol.II, SoftwareforConcurrent rocessors.renticeall, Englewood Cliffs,NJ.   
Anton,H.1981.ElementaryLinearAlgebra. 3ded.John Wiley& Sons,New York.   
Archibald, J.，and J. L. Baer. 1986. Cache-coherence protocols: Evaluation using a multiprocessor simulation model. ACM Transactions on Computer Systems,vol. 4, no. 4, pp. 273-298.   
Arjomandi,E.1975.Astudyof paralelism ingraph theory.Ph.D.dissertation,Uni versity oforontontario,ada.   
Armstrong,P.,and M.Rem.1982.A serial sorting machine. Computers and Electrical Engineeringvol.o.   
Atallah,M. J.1983. Algorithms for VLSI networks of processors.Ph.D.dissertation, The Johnsokinsiversityaltire   
Atallah,M. J. 1988. On multidimensional arrays of processors. IEEE Transactions on Computers,vol.37,no.10,Oct., pp.130613.   
Atallah, M.J.,R. Cole,and M. T. Goodrich. 1989. Cascading divide-and-conquer:A techniquefoiralelgoritAoualnomuiol8 no. 3, June, pp. 499-532.   
Atallah, M. J.,and S. R. Kosaraju.1984. Graph problems on a mesh-connected processorarray.JouraloftheACl.31,no.,Julyp.6967.   
Athas，W. C.， and C.L. Seitz. 1988. Multicomputers: Message-passing concurrent computers. Computer, Aug., pp. 9-24.   
AufderHeide,F.MandA.Wigderson1987.Thecomplexityof paralelorting. SIAMJouralonCompuing,ol.16o.eb..   
Averbuch,A.,.rGdkyan9re MIMD machine.Parallel Computing,ol.15,p.674.   
Aykanat,C.,F.Ozguner,F.Ercal,andP.dayapan.988.Ierativealgorithmorso lutionof large sparse systems oflinearequations on hypercubes.IEEETransactions onComputersl.7.2ec.,p.18   
Azar,Y.,and U.Vishkin.1987.Tight comparison boundson thecomplexityofparallel sorting.Aouralonouingl.6o.3,ue,.64.   
Baase,S.1978.Computer Algorithms: Introduction to Design and Analysis.Addison-Wesley, Reading,M.   
Babb,R.G.I.988.ogmmingrallelroceorsdioWesleyng, MA.   
Baccelli,F.,and Z.Liu.199o. On the execution of paralel programs on multiprocessor systems—A queuing theory approach.Journal of the ACM,vol.37,no.2Apr. pp. 373-414.   
Backus,J.1978. Can programming be liberated from the von Neumann style? A functional style and itsalgebra of programs.Communications oftheACMvol.21,no.8 Aug., pp. 613-641.   
Bader,G.,and E. Gehrke. 1991. On the performance of transputer networks for solving linear systems of equations. Parallel Computing, vol.17, pp. 1397-1407.   
Baer,J.L.1980. Computer Systems Architecture. Computer Science Press,Potomac, MD.   
Baer,J. L.1982. Techniques to exploit paralelism. In D. J. Evans, ed., Parallel Processing Systems:An Advanced Course, Cambridge University Press,Cambridge, pp. 75-99.   
Baer,J. L., H. C. Du, and R. E. Ladner. 1983.Binary search in a multiprocessing environment.IEEE Transactions on Computers,C-32,no.7,July,p.667-677.   
Baer,J.L.,and B. Schwab.1977.A comparison of tree-balancing algorithms.Communications oftheC,vol.20,no.5,ay,pp.   
Balas,E., D. Miller,J.PeknyandP. Toth.1991. A parallel shortestaugmenting path algorithm for the asignment problem.Journal of the ACM,vol. 38,no.4,Oct., pp. 985-1004.   
Balzer, R. M. 1971. PORTS--A method for dynamic interprogram communication and job control.In Proceedings of the AFIPS Spring Joint Computer Conference,vol.38, AFIPS PresonVA,p.9.   
Bambos,N.and J.Walrand.1991. On the stabilityand performance of parallel processing systems.Journal of the ACM,vol. 38,no.2,Apr.,pp.429-452.   
Bampis, E., and J. C.Konig. 1991. Impact of communications on the complexity of theParallelGaussianElimination.ParalelComputing,vol.17,.55-61.   
Banerjee,U.988.DependenceAalysis forupercomputing.uwerAdemicPub lishers,rwell,   
Barnes,G.H.,R.M. Brown, M. Kato,D.J.Kuck,D.L.Slotnick,andR.A.Stokes. 1968.The Illiac IVmputer.EEE ransactions onomputers,C7noan., pp. 84-87.   
Bar-On, I. 1987.A practical paralel algorithm for solving bandsymmetrypositive definite systems of linear equations.ACM Transactions on Mathematical Software, vol. 13,Dec., pp.323-32.   
Barr,R. S.,R. V.Helgaonand J. L. Kennington.1989.Minimal spanning trees:An empiricalieigtioofraeloit.raelmutng.2 52.   
Batcher,K. E.1968.Sorting networks and their applications. In Proceedings of the AF 314.   
Batcher, K. E. 1979. The STARAN Computer. In C. R. Jesshope and R. C. Hockneye Maidenhead,d,   
Batcher,K. E. 198o. Design of massively paralel processor. IEEE Transactions on Computersvol.,o.,   
Baudet,G.M.978a.Asychronous iterative metods for multiprocesors.Joualof theACM,   
Baudet, G.M. 1978b.The design and analysis of algorithms forasynchronous multiprocesorsei   
Baudet,G.,and D.Stevenson. 1978.Optimal sorting algorithms for paralel computers. IEEETractoonomutersl.o.1,an..   
BBN.1985. ButterflyrM parallel processor overview. Vers. 1. Tech. rept., BBN Laboratories,Inc.,Dec.Cambridge,MA.   
Beck,B.,andD. Olien.1989. A parallel-programming process model. IEEE Software May, pp. 63-72.   
Belkhale, K. P.，and P. Banerjee. 1992. Paralel algorithms for geometric connected component labeling ona hypercube multicomputer.IEEE Transactions on Comput ers,vok41no.6,Je,pp.6909.   
Bell, G. 1989. The future of high performance computers in science and engineering. Communications of the ACM,vol.32,no.9,Sept.,pp.19111.   
Ben-Ari98.plerrentrogammnticealleo Cliffs, NJ.   
Bentley, J. L. 1980. A parallel algorithm for constructing minimum spanning trees. JounalofAgitsl.   
Bentley,J.L., and D. J. Brown.1980. A general class of recurrence tradeoffs. In Proceedings of the 2Ist Annual Symposium on Foundations of Computer Science, IEEE,New York, Oct., pp.217-228.   
Bentley, J. L. and H. T. Kung. 1979. A tree machine for searching problems. In Proceedings of the 1979 International ConferenceonParallel Processing,IEEE,New York,Aug.,pp.257-266.   
Berg,H. K.,W. E. Boebert, W.R.Franta,and T.G. Moher.1982. Formal Meth ods ofProgramVerificationndpecification.rentice-Hall,nglewods, Chap.6.   
Bergland, G. D. 1972. A paralel implementation of the Fast Fourier Transform algorithm.IEEE Transactions on Computers,vol.C-21,no.4,Apr.,pp.366-370.   
Berliner, H.,and C. Ebeling. 1986. The SUPREM architecture: A new intelligent paradigm.ligce.   
Berman,F.1987.Experience withanautomatic solution to the mapping problem In L. Jamieson,D.Gannon,and R.Douglass,eds.,The Characteristics of Parallel Algorithmssge,4.   
Berman,F.ndLyder.987.Omapigpralelalgorithsintpaeh tectures.JoualofallelndstributedCmpuinol.458.   
Bermond, J. C., P. Michallon, andD. Trystram. 1992. Broadcasting in wraparound meshes with parallel monodirectional links.Parallel Computing,vol.18,pp.639- 648.   
Bernhard,R.1982.Computingat thespeed limit.IEEESpectrum,vol.19,no.7, pp. 26-31.   
Berntsen,J.989.ommatioentatrixultiaioob.a allel Computing,vol.12,pp.42.   
Bertsekas,DP.J.Nisils8alelndstrutedoto Numericalethds.Prentice-Hallnglewoods,   
Bettayeb,S.,Z.Miller,andI. H.Sudborough.1988.Embedding grids intohypercubes. In Proceedings of the 3d Aegean WorkshoponComputing.   
Bhatt,S.N.dC.E.eeon982.owtsbletreeacns.Inroedng ofthe14thAnnalCSymposiumoneoryofomputing,ACewokay pp. 77-84.   
Bhatt,S.,F. Chung, T.Leighton,and A.Rosenberg.1986. Optimal simulations of tree machines.In Proceedings of the 27th Annual Symposiumon Foundations of Computer Science,IEEE Press,New York,pp.274-282.   
Bhattacharya,S.andA.Bagchi.199o.Searching game treesinparallel using $\mathrm { S } \mathrm { S } \mathrm { S } ^ { \ast }$ In Proceedings AAAl-90, pp. 42-47.   
Bhuyan, L. N., Q. Yang, and D. P. Agrawal. 1989. Performance of multiprocessor interconnection networks.Computer,Feb.,pp.5-37.   
Bilardi, G., and A. Nicolau. 1986. Bitonic sorting with $O ( n \log n )$ comparisons. In Proceedings of the 2Oth Annual Conference on Information Sciences and Systems, pp. 336-341.   
Bilardi, G.,and A. Nicolau. 1989. Adaptive bitonic sorting: An optimal parallel algorithm for shared-memory machines. SIAM Journal on Computing,vol. 18,no. 2, Apr., pp. 216-228.   
Bilardi, G., M. Pracchi, and F. P. Preparata. 1981. A critique and an appraisal of VLSI models of computation. In H. T. Kung,B. Sproul,and G. Steele, eds. VLsi Systems and Computations,Springer-Verlag,New York,pp.81-88.   
Bilardi,G.andF.P.Preparata.1983. A VLSI optimal architecture for bitonic sorting. In Proceedings of the7thConference on Information Science Systems,pp.1-5.   
Bilardi,G.,andF.P.Preparata. 1984a.A minimum area VLSI architecture for $O ( \log n )$ time sorting.In Proceedings of the 16th Annual ACM Symposium on Theory ofComputing,ACM,New York,May,pp.64-70.   
Bilardi, G.,and F.P.Preparata.1984b.An architecture for bitonic sorting with optimal VLSIperforce.EEctiouters.3,o7July64 651.   
Bini,D. 1984. Parallel solution of certain Toeplitz linear systems.SIAM Journal on Computing, vol. 13, May, pp.268-276.   
Bitton,D.,D. J. DeWitt, D. K. Hsaio, and J. Menon.1984. A taxonomy of paralel sorting.AC Computing urveys,vol.16,no.3,ept.,pp.2818.   
Biton-Friedland,D.1982.Designanalysis and implementation of parallel exteral sortingalgorithms...ssrtation,UiversityofWiscosindison.   
Bjprstad,P.E.987.Aargescalespasesecondarysorageirectnear atio solver for structural analysisand itsimplementation on vector and parallel architectures.Parallel Computing, vol. 5, pp. -12.   
Blelloch,G.E.990Vectorodelsforata-arallelComputing.res,am bridge.   
Blelloch, G.E.，and S. Chatterjee1990. VCODE:A data-paralel intermediate language.In Proceedings of the Third Symposiumon the Frontiers ofMassively Parallel Computation. IEEE Press,New York.   
Bodnar,B.L.,and A.C.Liu.1989.Modeling and performance analysis of single-bus tightly-coupled multiprocessors.IEEE Transactions on Computers,vol.38,no.3, Mar., pp. 464-470.   
Bokhari,S.981.Onthe maping problem.IEEETransactionsonComputersvol. C-30, no. 3, pp.207-214.   
Bokhari,S.H987ultiprocessingteieveofratostees.ompuel. no. 4, Apr., pp. 50-58.   
Bokhari.8balele puting.EEie.7   
Bonomo,J.P.,and W.R.Dyksen. 1989.Pipelined iterative methods for shared memory machines.lel99   
Bonuccell,M.A.,E.LodiandL.Pagli.984.Externalsorting in VSI.IEEETras actions onComputers,vol.C-33,no.10,Oct.,pp.9934.   
Boreddy,J.andA.Paulraj.199o. On theperformanceof transputer arrays for dense linearsstems.alleling.   
Borodin, A., and J. Hopcroft. 1985. Routing, merging, and sorting on parallel models of computation.Journal ofComputer and SystemSciences,vol.30,pp.30145.   
Brass,A.,andG.S.Pawley. 1986.Two and three dimensional FFTs on highly parallel computers.raelComputingo.3,.6184.   
Brent,R.P.1974.The parallel evaluation of general arithmetic expressions.Journal oj theA   
Brigham,E.O.973.TheFastFourierTransform.Prentice-Hall,Englewoodifs NJ.   
BrinchHansen,P.973a.OperatingSystemPrinciples.Prentice-Hall,nglewoodfs, NJ.   
Brinch Hansen,P.1973b.Concurrent programming concepts.ACM Computing Surveys, vol. 5, no.4Dec.,pp.245.   
Brinch Hansen, P.1975.The programming language Concurrent Pascal. IEEE Transactionsoeeg2.   
Brinch97eetureoentrmicel glewood Cliffs, NJ.   
Brinch Hansen, P. 1978. Distributed processes: A concurrent programming concept. Communications of theACM,vol.21,no.11,Nov.,pp.934-941.   
Brinch Hansen,P.1981.Edison:A multiprocessor language.Software Practice and Experience,vol.11,no.4,Apr.,pp.3561.   
Brock,H. K., B. J. Brooks,and F. Sullivan. 1981. Diamond: A sorting method for vector machines.BIT,vol.21,pp.142152.   
Browning,S.A.1980a. The tree machine: A highly concurrent computing environment. Ph.D.dissertation,Caliornia Insituteof echnologyasadena,A   
Browning,S.A.98ob.Algorithms forthetreemachine.InC.MeadandL.Conway eds.Inrie   
Bucher,I. Y.,and M. L. Simmons. 1985. Performance assessment of supercomputers.PreprintLAU85-15o5,LosamosNationalLaboratoryLosamos,., M. Ginsberg.,tllad,.   
Burton,F.W.andM..Huntbach.984.Virtual tree machines.IEEETranctions onComputers,vol.C-33,no.,ar.,.80.   
CareyM.J,.sC.2.: tationofaecord-sortingstack.Tch.rept.UCB/CSD/102,Computerence Div.Universityofaliforniarkeley   
Carey,M.J.andC.D.oson.1984.Aneientimplementatonofsarchtrees on $\lceil \lg N + 1 \rceil$ processors.Etitsl.3 pp. 1038-1041.   
Carriero,N.andD.Gelernter.1988.Applicationsexperience withinda.Inroceed ingsoftheACMSymposiumonParalelProgramming:ExperiencewithApplications, Languages,and Systems,pp.173-187.   
CarrieroN.nd.Gelerter.989a.Lindainotext.ommunicaionsofthe vol. 32, no. 4, Apr., pp. 444-458.   
Carero,N.andD.Gelernter.1989b.How towrite parallel programs:A guide to the perplexed.AComputingurveysvol.21no.,ept.,p.   
Cariero,N.ndGelernter.99.HowtoWritePraelPrograms:AFirstourse. MIT Press, Cambridge.   
Carrero,N.,D.GelernterandJ.eichter.986.Distributeddatastructuresinida. In Proceedings of the ACM Symposium on Principles of Programming Languages.   
Chabbar, E.198o. Controle et gestion du parallelisme: tris synchrones et asynchrones. Thesis, Université de Franche-Comte,France.   
Chaiken, D., C. Fields, K. Kurihara, and A. Agarwal. 1990. Directory-based cache coherence in large-scale multiprocessors. Computer, June, pp. 49--58.   
Chamberlain,R.M. 1988. Gray codes, Fast Fourier Transforms and hypercubes.Parallel Computing,vol.6,pp.23.   
Chan,M. Y. 1991. Embedding of grids into optimal hypercubes. SIAM Journal on Computing,vol.20,no.5, Oct., pp.834864.   
Chan,M. Y.,and F. Y.L. Chin. 1988. On embedding rectangular grids into hypercubes. IEEE Transactions on Computers,vol.C-37,no.10,Oct.,pp.128588.   
Chan,T.F.,and Y.Saad. 1986.Multigrid algorithms on the hypercube multiprocessor. IEEE Transactions on Computers,vol. C-35,no.11, Nov., pp.969-977.   
Chandra,A. K. 1976. Maximal parallelism in matrix multiplication. IBM Tech. rept. RC6193, Thomas J.Watson Research Center, Yorktown Heights, NY.   
Chandra,A.K.,andL.J. Stockmeyer.1976.Alternation. In Proceedings of the 17th Annual Symposium on Foundations of Computer Science,IEEE,New York,Oct., pp. 98-108.   
Chandrasekharan, N.,and S. Sitharmama Iyengar. 1988. NC algorithms for recognizing chordal graphs and $k$ trees.IEEETaactionsonomutersol.C37noct pp. 1178-1183.   
Chang，S.-K.1974. Paralel balancing of binary search trees. IEEE Transactions on Computers,vol. C-23,no.4,Apr., pp. 441-445.   
Chang, J.，and A. M. Despain.1985. Semi-intelligent backtracking of Prolog based on a static data dependency analysis.In Proceedings of the IEEE Symposium on Logic Programming, Aug., pp.43-70.   
Charlesworth,A. E.and J.L. Gustafson.1986. Introducing replicated VLSI to supercomputing: the FPS-164/MAX scientific computer. Computer,vol.19, no.3,Mar., pp. 10-22.   
Chatterjee,S., G.E.Blelloch,and A.L. Fisher.1991. Size and access inference for data-paralel programs. In Proceedings of the 1991 ACM SIGPLAN Conference on Design and Implementation of Programming Languages.   
Chaudhuri,P.199o.Findingandupdatingdepthfstspanningtresofacyclicdigaps in parallel.heComputerJournal,vol.33,June,pp.24251.   
Chazelle, B. M.,andL. M. Monier.1981a. A model of computation for VLSl with relatedcomplexity results.In Proceedings of the 13th Annual ACMSymposiumon TheoryofutingwYork,y5.   
Chazele,B.ndL..ier9.Otmalityin.InJ.P.Grad. 81,Academics,oon,78   
Chen,A. C.,and C.L. Wu. 1984. Optimum solution to dense linear systems of equations.In Proceedings of the 1984 International Conference on Parallel Processing, IEEE, New York,Aug.,pp.417-424.   
Chen,A. C.,and C.L. Wu. 1991. A parallel execution model of logic programs. IEEE Transactioed   
Chen,I. N.i975.A new parallel algorithm for network flow problems.In Parallel Processingteee pp. 306-307.