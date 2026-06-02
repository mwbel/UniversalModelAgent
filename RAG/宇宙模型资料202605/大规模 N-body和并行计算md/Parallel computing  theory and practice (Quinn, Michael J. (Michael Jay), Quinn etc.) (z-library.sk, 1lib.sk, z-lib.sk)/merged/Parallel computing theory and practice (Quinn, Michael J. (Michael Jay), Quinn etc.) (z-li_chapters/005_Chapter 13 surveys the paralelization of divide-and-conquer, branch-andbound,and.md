Chapter 13 surveys the paralelization of divide-and-conquer, branch-andbound,andalpha-betasearchalgorithms.Section13.1discusses thethre kinds of search trees that arise from combinatorial optimization algorithms. Section 13.2 summarizes parallel methods to solve divide-and-conquer problems. Section 13.3 introduces the branch-and-bound algorithm, using the 8-puzzle as an example. The section ends by describing a well-known algorithm to solve the traveling salesperson problem. In Sec. 13.4 we present parallelizations of the branch-and-bound algorithm for multiprocessors and multicomputers. We also show how parallel branch-and-bound algorithms can exhibit anomalous behavior that sometimes results in superlinear speedup. Section 13.5 contains an overview of the sequential alpha-beta algorithm, commonly used to search game trees,and Sec. 13.6 describes methods used to parallelize the alpha-beta search algorithm.

There are two kinds of combinatorial search problems. An algorithm to solve a decision problem must find a solution that satisfies all the constraints. An algorithm that solves an optimization problem must also minimize (or maximize) an objective function associated with solutions. All examples of combinatorial search in this chapter are optimization problems.

A search problem can be represented by a tree. The root of the tree represents the initial problem to be solved. The nonterminal nodes are either AND nodes or OR nodes.An AND node represents a problem or subproblem that is solved only when all its children have been solved; an OR node represents a problem or subproblem that is solved when any of its children has been solved. Every nonterminal node in an AND tree is an AND node (Fig. 13-1a). The search tree corresponding to a divide-and-conquer algorithm is an AND tree, since the solution toa problem is found by combining the solutions to allits subproblems. Every nonterminal node in an OR tree is an OR node (Fig. 13-1b). Branchand-bound algorithms yield OR trees, since the solution to a problem can be found by solving any of its subproblems. An AND/OR tree is characterized by the presence of both AND nonterminal nodes and OR nonterminal nodes (Fig. 13-1c). Game trees are examples of AND/OR trees.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/8d3e0bfef3a2968de345f75a93185986a19a540cd7de46dc580fa5348c7aef7b.jpg)

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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/c47e9c13c807a999d24a047488874abd644b0138b3e85c86471438a8060b641b.jpg)

to examine as few alternative moves as possible. A means for achieving that goal is to associate with each state an estimate of the minimum number of tile moves needed to solve the puzzle, given the moves made so far.

One such function adds the number of tile moves made so far to the Manhattan distance between each out-of-place tile and its correct location. [The Manhattan distance between two tiles with (row, column) coordinates $( x _ { 1 } , y _ { 1 } )$ and $( x _ { 2 } , y _ { 2 } )$ is $| x _ { 1 } - x _ { 2 } | + | y _ { 1 } - y _ { 2 } | . ]$ Given such a function, the search can be concentrated on the portions of the state space tree that contain the most promising moves. The search always proceeds from the node having the smallest function value. If two or more nodes have the same value, then the node farthest from the root of the state space tree is examined. If two or more nodes the same distance from the root have the same value, then one node is chosen arbitrarily. The branch-and-bound search of an 8-puzzle appears in Fig. 13-4. Note that the algorithm requires that far fewer nodes be examined than in the breadth-first search.

Now that we have given a concrete example, we will define the branch-andbound technique. Given an initial problem and some objective function $f$ to be minimized, a branch-and-bound algorithm attempts to solve it directly. If the problem is too large to be solved immediately,it is decomposed into a set of two or more subproblems of smaller size. Every subproblem is characterized by the inclusion of one or more constraints. The decomposition process is repeated until each unexamined subproblem is decomposed, solved, or shown not to be leading to an optimal solution to the original problem.

In the 8-puzzle example, the problem is to put the pieces in order. The objective function $f$ is the number of moves needed to order the pieces. If only a single move is necessary to order the pieces, the algorithm solves the problemdirectly.Otherwise,itdecomposes the problem by generatinganumber of subproblems, one per legal move.

As we have seen in the case of the 8-puzzle, the decomposition process applied to the original problem may be represented by a rooted tree, called the state space tree. The nodes of this tree correspond to the decomposed problems, and the arcs of the tree correspond to the decomposition process. The original problem is the root of the tree. The leaves of the tree are those partial problems that are solved or discarded without further decomposition.

A branch-and-bound tree is distinguished in two important ways from trees representing divide-and-conquer algorithms. First, the tree is an OR tree (Fig.13-1b); the solution to any subproblem is a solution to the original problem.Hence the entire tree need not be searched. In fact, the state space tree representing a branch-and-bound algorithm may be infinite. This is the second important difference between branch-and-bound trees and divide-and-conquer trees.

Recall that the goal of the branch-and-bound technique is to solve the problem by examining a small number of elements in this tree. Assume that a minimum cost solution f\* is desired. A lower bounding function g is calculated for each decomposed subproblem as it is created. This lower bound represents the smallest possible cost of a solution to that subproblem, given the subproblem's constraints. On any path from the root to a terminal node, the lower bounds are always nondecreasing.In addition, the lower bound $g ( x )$ at every leaf node $x$ representing a feasible solution is identical to the valueof the objective function $f ( x )$ for that subproblem.Leaf nodes representing infeasible solutions have the value $\infty$ Figure13-5 is another exampleof a state space tree.The values inside the nodes are the lower bounds of the corresponding subproblems. Nodes corresponding to feasible solutions are represented by heavy circles. The best solution to this problem has cost 18; i.e., the value of $f ^ { * }$ is 18.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/f2633bfcfd90e00d88a3b90f50730167ac8622c340e93b73771d087126e52f80.jpg)  
13-4 Thebranchandboundsearch forasolution toanarrangementof the8-puzzeidentica to that of Fig.13-3.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/b1ad16e8c2b9433a69dc4786f9225f908ce7ed8ddd1fa9a40ce326b3d8cf0924.jpg)  
FIGURE 13-5 Another example of a state space tree. The values inside the nodes are the lower bounds of the solutions to the corresponding subproblems.Nodes corresponding to feasible solutionsare represented by heavy circles. The best solution to this problem has cost 18.Thenumbers near the nodes represent the order in which they are examined by the best-first search strategy.

At any point during the execution of a branch-and-bound algorithm there exists a set of problems that have been generated but not yet examined. A search strategy determines the order in which the unexamined subproblems are examined. The best-first (best-bound) search strategy selects the unexamined subproblem with the smallest lower bound. In the case of a tie, the subproblem deepest in the state space tree (i.e., the subproblem with the most constraints) is chosen. Ties unresolved by the deepness heuristic are broken arbitrarily. The numbers near the nodes in Fig.13-5 indicate the order in which the nodes are examined by the best-first search strategy.

A branch-and-bound algorithm can be characterized by how subproblems are generated, how a particular subproblem is selected as the point to continue the search, how hopeless subproblems are discarded,and how the algorithm terminates. Any of these steps can be performed in parallel.

# 13.3.1 Traveling Salesperson Problem

The traveling salesperson problem (TSP) can be solved by a branch-and-bound algorithm. The TSP is defined as follows: Given a set of vertices and a nonnegative cost $c _ { i , j }$ associated with each pair of vertices $i$ and $j$ ,find a circuit containing every vertex in the graph so that the cost of the entire tour is minimized. An example of a weighted graph and its traveling salesperson tour are given in Fig. 13-6.

Little et al. (1963) devised a famous branch-and-bound algorithm to solve the traveling salesperson problem. When an unsolvable problem is encountered, it is broken into two subproblems representing tours that must include or exclude a particular edge. The edge to be used as the added constraint for the subproblems is chosen so that the lower bound on the solution cost of the subproblem, excluding that edge,is maximized. In other words, when a problem is broken into subproblems, the algorithm examines the minimum increase in the tour length, when various edges are excluded,and chooses the edge where exclusion has caused the largest increase in the tour length.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/11c1063daddf4c22313055444d29fe78b499af902bef751d9920ee79f411e584.jpg)  
RE 13-6 A weighted graph and its traveling salesperson tour (solid lines).

Reduction is used to find a lower bound on the cost of the tour, given the constraints made so far. The reduction algorithm works as follows: For every vertex i in the graph, the length ci of the shortest edge leading to vertex i is found.If ci > O,then the lower bound can be increased by ci,if ci is subtracted from the length of every edge leading to vertex i. After this step has been performed, the rows can be reduced in a similar fashion. For every vertex i in the graph, the length r; of the shortest edge leading from vertex i is found. If ri >O, then the lower bound can be increased by ri if ri is subtracted from the length of every edge leading from vertex i. An example of matrix reduction appears in Fig. 13-7.

A problem is broken into subproblems that are easier to solve because the subproblems contain additional constraints. In this algorithm, for example, including an edge reduces the number of edges that must be added to complete the tour, while excluding an edge reduces the number of candidate edges.By driving up the lower bound as quickly as possible, the goal is to limit the number of subproblems (nodes in the state space tree) that must actually be examined. Figure 13-8 contains a high-level description of a best-first branch-and-bound algorithm using the best-first variant ofLittleet al.'s problem decomposition heuristic.

Figure 13-9 presents the state space tree corresponding to this algorithm's search for the traveling salesperson tour of the graph shown in Fig. 13-7. Each node in the state space tree represents a set of possible tours satisfying constraints specified by the path from the root to that node. The root represents the set of all possible tours. Since reducing the weight matrix of the directed graph results in the value 25 being assigned to the root,a lower bound on the length of any tour is 25. The edge whose exclusion causes the greatest increase in the lower bound is $^ { ( B , C ) }$ . Hence the two children of the root represent the alternatives of including or excluding edge $( B , C )$ . Every tour explored in the Ieft subtree must contain edge $^ { ( B , C ) }$ ,but no tour explored in the right subtree may contain edge $^ { ( B , C ) }$ . Given its constraint, each child node of the parent can be reduced, and lower bounds on all solutions based on that constraint can be determined. The lower bound of the left child is 31, while the lower bound on the right child is 29. In other words, tours that contain edge (B,C) must have length at least 31,while tours that do not contain edge $^ { ( B , C ) }$ must have length at least 29. Hence the right child is the next node to be explored. Excluding edge $( E , C )$ causes the greatest increase in the lower bound.The value in the right child-32-is a lower bound on all solutions that do not have edge (B,C) or edge (E,C). The value in the left child-31-is a lower bound on all solutions that do not have edge $( B , C )$ ,but do have edge $( E , C )$

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/e2dca6529ab04397839dbb8c1cf5b0ddace148ebf28d67bcc2f71d44bef898d3.jpg)  
FIGURE 13-7 An example of matrix reduction used by Litte et al.'s traveling salesperson algorithm. A lowerbound on thelength of the traveling salesperson tourof this graph is 25.

Since there are two unexplored nodes with the same lower bound (31), we explore the node deeper in the tree. This processcontinues until atour is

TRAVELING SALESPERSON (SISD): begin reduce weight matrix, determining the root's lower bound initially only the root is in the state space tree {The root represents the set of all possible tours} repeat select the unexamined node in the state space tree with the smallest lower bound if the node represents a tour then exit the loop endif select the edge whose exclusion increases the lower bound the most for the two cases representing the inclusion and exclusion of the selected edge do create a child node with the correct constraint find the lower bound for the child node endfor forever   
end

FIGURE 13-8 Ahigh-level description of a sequential best-first branch-and-bound algorithm to solve thetraveling salespersonproblem.Thealgorithm is based on the problem decomposition heuristicdevisedbyLittle etal.

# FIGURE 13-9

The state space tree corresponding to a best-first branch-and-bound search for a traveling salesperson tour of the graph shown in Fig.13-7.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/f6c71eeb6ef2a91e60a651924ce8ea3f56c56cbd61010bea38e8e1f90a0215c6.jpg)

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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/b5cec580b3f7a7fb8efbdbd16a591c5988b194e3806e154d4488bb0aa9bedcc1.jpg)  
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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/4de7e349ff97819e1e51c960987ca18693c9b3e57d48268666391ab20d157328.jpg)  
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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/ce74686ecec714ed9922b7ead0bd103bb30999dabcdbc555599440992c2c5889.jpg)  
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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/69daa8c98e4c88c90137b48b422b14b25d04331c4b48d6cb1f87507a128b7fec.jpg)  
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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/baba139e3c3a3bb01247eb71b8a41c2c691e725a085bb28499b1a475123c52a2.jpg)  
FIGURE 13-18 An illustration of alpha-beta search. The number inside each node is the value of the position.In the case of leaf nodes,an evaluation function computes the value of the position.Inthe case of interiornodes,thevalue iscomputed from the valuesof its children.Highlighted circlesrepresent nodes inwhich pruning occurs.

except that nodes not examined by the alpha-beta algorithm are not included. When the algorithm begins execution, $\alpha = - \infty$ and $\beta = \infty$ . The algorithm traverses the nodes of the tree in preorder;the values of $\alpha$ and $\beta$ converge as the search progresses.

The nodes drawn in heavy lines in Fig. 13-18 represent places where pruning occurs. To explore the conditions under which pruning happens let us consider an arbitrary interior node in the search tree. When the search reaches this node, we know that some choice of moves that has already been considered leads to a value of at least $\alpha$ for the player moving first. We also know that correct play on the part of the opponent will ensure that the first player cannot get a value more than $\beta$ .Hence $\alpha$ and $\beta$ define a window for the search.

If the interior node pos is a MAX-NODE, then it is the first player’s move. If val,the value of the game tree searched from node pos is greater than $\alpha$ then $\alpha$ is changed to val, a beter line of play has been found for player one.

Analogously, if the interior node pos is a MiN-NODE, then it is the second player's move. If val, the value of the game tree searched from node pos is less than $\beta$ ,then $\beta$ is changed to val; a better line of play has been found for player two.

However,if at any time the value of $\alpha$ exceeds the value of $\beta$ ,there is no need to search further. It is in the best interests of one of the players to block the line of play leading to node pos.

For example, consider the node labeled A in Fig. 13-18. The value returned from the search of the first child of A is 3, which is greater than 2, the value $\beta$ . It is not in the second player's interest to allow play to reach this position, since there is another line of play guaranteeing a value no higher than 2. Hence there is no point in continuing the search from this game position.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/3cbf26f1e9d874621ecdfb2fccd1d648d46462f961cc0da6c984a1947f282164.jpg)  
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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/842ca6fe6790250cced4d63e58f8057dff5de7ab239441c43da4742b65bf1153.jpg)

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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/9ee8564327f294aa442dc116935ae4a6c8941796141ebb05d2e039831e29ad20.jpg)

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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/5a752a41298342baf43b68c20d066f051841192f04a74b47d76f00cdb9a8a869.jpg)

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/fb92463a0a26b4b96d81efd4f292d59bbef887f62b619c3996e8903d2b578f26.jpg)  
FIGURE A-2 A weighted directed graph and its corresponding weight matrix. Depending upon the algorithm,nonexistent edges maybe representedasO oras $\infty$ in the weight matrix. In this example nonexistent edges are represented as 0.

<table><tr><td colspan="6">ABCDE 05070</td></tr><tr><td rowspan="2">A</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>B00700</td></tr><tr><td rowspan="3"></td><td></td><td></td><td></td><td></td><td>C03002</td></tr><tr><td></td><td></td><td></td><td></td><td>D60200</td></tr><tr><td></td><td></td><td></td><td></td><td>E00410</td></tr></table>

is similar to an adjacency matrix, except that the value of the matrix element at row $i$ and column $j$ gives the weight of the edge from vertex $i$ to vertex $j$ . Nonexistent edges may be represented by either O or $\infty$ entries, depending upon the particular problem being solved. Figure A-2 illustrates a weighted directed graph and its weight matrix.

Another representation stores a graph as a list of edges and a cardinal number indicating the number of vertices. A third representation uses adjacency lists—a list,for every vertex,of the edges leaving that vertex.A fourth representation, often used to represent digitized picture input, consists of a two-dimensional boolean matrix.If we label the elements 1 and O, then the set of vertices consists of the matrix elements having the value 1; the set of edges is the set of all pairs of vertically or horizontally adjacent 1s.

A path from $v _ { 1 }$ to $\upsilon _ { i }$ in a graph $G = ( V , E )$ is a sequence of edges $( v _ { 1 } , v _ { 2 } )$ ， $( v _ { 2 } , v _ { 3 } )$ ， $( v _ { 3 } , v _ { 4 } ) , \ldots$ $( v _ { i - 2 } , v _ { i - 1 } )$ ， $( v _ { i - 1 } , v _ { i } )$ ,such that every vertex is in $V$ ,every edge is in $E$ , and no two vertices are identical.

A cycle in a graph $G = \left( V , E \right)$ is a sequence of edges $( v _ { 1 } , v _ { 2 } )$ ， $( v _ { 2 } , v _ { 3 } )$ ， $( v _ { 3 } , v _ { 4 } )$ ，··， $( v _ { i - 1 } , v _ { i } )$ ， $( v _ { i } , v _ { 1 } )$ , such that every vertex is in $V$ ,every edge is in $E$ ,and only the first and last vertices in the sequence of edges are identical. A graph without cycles is said to be acyclic.

There are two common shortest-path problems. Given a weighted, directed graph $G = ( V , E )$ ,theall-psestoistfd pair of vertices $i$ ， $j \in V$ , the shortest path from $i$ to $j$ along edges in $E$ .Given a weighted, directed graph $G = ( V , E )$ and a vertex $s \in V$ , the single-source shortest-pthoistondree $i \in V$ ,the shortest path from $s$ to $i$ along edges in $E$ .FigureA-3 illustrates these two kinds of shortest-path problems.

A subgraph of a graph $G$ is a graph with vertices and edges in $G$

An undirected graph is connected if, for every pair of vertices i and j in $G$ , there is a path from $i$ to $j$ .The connected component problem is to find, for some undirected graph G, the minimal set of subgraphs such that every subgraph is connected (Fig. A-4). This problem is also known as the component Iabeling problem, since by the end of the algorithm every component's vertices share a label unique to that component. The connected 1s problem is the connected component problem applied to digitized picture input (the fourth graph representation described earlier).

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/03d410464c1ea776de726c4cae0e97ce09c22523cbd00911d7ec5192b9d102e6.jpg)  
FIGURE A-3 Shortest-path problems. (a) Al pairs. (b) Single source.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/fcd235f5de52782dffbe3eeaeef3c9ef5d5a5c8fcd22023827bda5b95b873f72.jpg)  
FIGURE A-4 Connected components.

A tree is a connected, undirected acyclic graph. A spanning tree for a graph $G$ is a subgraph that is a tree containing every vertex of $G$ .The weight of a spanning tree of a weighted graph is the sum of the weights of the tree's edges. Given a weighted,undirected graph $G$ , a minimum-cost spanning tree of $G$ is a spanning tree with the smalest possible weight among all spanning trees of $G$ (see Fig. A-5).

In some problems involving trees a particular vertex is designated as the root. In these problems the height of the tree is the maximum distance from the root of the tree to a leaf. Every edge $\left( u , ~ v \right)$ in a rooted tree establishes a parent-child relationship between the two vertices. The parent is the vertex closer to the root; the child is the vertex farther from the root.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/57577207cf80e40b34a2f84c06bf77e3622afa2b3ed5c5dbc2eabc09d8adb75b.jpg)  
FIGURE A-5 Minimum-cost spanning tree problem. (a) Weighted graph. (b) Minimum-cost spanning tree.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/ea1dd72291fd7c620da8bf10037b9cca9699ca8d43ba086cab92d0734fdc04b1.jpg)  
FIGURE A-6 Complete binary trees of height one, two, and three.

A binary tree is a rooted tree in which no node has more than two children. A complete binary tree isa binary tree of height $n$ having $2 ^ { n + 1 } - 1$ nodes (of which $2 ^ { n }$ are leaves). Figure A-6 illustrates complete binary trees of height one, two,and three.

A binomial tree of height O is a single node. For all $i > 0$ ,a binomial tree of height $i$ is a tree formed by connecting the roots of two binomial trees of height $i - 1$ with an edge and designating one of these roots to be the root of thenew tree.A binomial tree of height $n$ has $2 ^ { n }$ nodes. Figure A-7 illustrates binomial trees of height one through four.

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/125945e88899b444a3a14be4540a86fab9b3649a727d9bb1430f5bfcfc385bd9.jpg)  
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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/72a0f4d2ea604977aa51362083f4e3ec14bbffbb753bc48df4a2864662aba7b4.jpg)  
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

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0006_pages_0351-0420/auto/images/3f87e1dd17254f85c4cb82d3721b0ed1e7cc91fb9b57f96c443acc52ab0256ac.jpg)  
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


<!-- chunk 0007: pages 421-472 -->
Chen,J., E.L. Dagless, and Y. Guo. 1984. Performance measurements of scheduling strategies and parallel algorithms for a multiprocessor quick sort.IEE Proceedings Part E,Computersandigital Techniques,vol.31ar.,pp.4.   
Chen,M. C. 1986. Crystal: A synthesis approach to programming parallel machines. In M.T.athd.Hcubeuroesss986,rssia pp. 87-107.   
Chen,M. C.1987. Very-high-level paralel programming in Crystal. In M. T. Heath, ed.,Hypercube ultiprocessors987Aress,Pdelpia,Ap.947   
Chen, T.C., K. P.Eswaran, V. Y.Lum,and C. Tung. 1978a. Simplified odd-even sort usingmultiple shift-registerloops.International JournalofComputer and Informa tionScience,vol.7o.,.14.   
Chen,T. C., V. Y. Lum,and C.Tung. 1978b.The rebound sorter: An efficient sort enginefor large files.InProceedings of the4th International Conferenceon Very Large Data Bases,pp.312-318.   
Chen,Y. K.,and T. Feng. 1973. A parallel algorithm for maximum flow problem. In Proceedings ofthe1973ComputerConferenceonParallelrocesingAug.p.60   
Cheong, H.,and A. V. Veidenbaum.199o. Compiler-directed cache management in multiprocessrs.tere7   
Cheriton,D.R.,H. A. Goosen,andP. D. Boyle.1991. Paradigm: A highly scalable shared-memoryulticomputerahitecture.Computereb.,.3346.   
Cheriton,D.R.a976.ngroal on Computing,vol.5,no.4ec.,pp.42.   
Chern,M. Y.,and T. Murata.1983a. A fast algorithm for concurrent LU decompositionand matrix inversions.In Proceedings of the 1983 International Conference on Parallel Processing,EEE,ewYork,ug.,6   
Chern,M.Y.andT.Murata.1983b.Eficientmatrix multiplicationsonacocrnt data-loadingarrayprocessor.InProceedingsof the1983 InternationalConference on ParalelProcessing,EEE,ewYorkug.,p994.   
Cheung,J.,S.hall,S.Lakshmvaraan,L. Miller,andB.Walker.1982.Anewclass of two stage parallel sorting schemes.In Proceedings of the ACM‘82 Conference, ACM,New York,Oct., pp.26-29.   
Chin,F.I.,and K.S.Fok.198o.Fast sortingalgorithmsonuniformladders (multiple shiftrgisteroos).Eciouterso.uly pp. 618-631.   
Chin,F.Y.,J.Lamand1.N.Chen.1981.Optimalparalelalgorithms for theconected component problem.In Proceedings ofthe 1981 International Conferenceon Parallel Processing,IEEE,New York,Aug.,pp.1775.   
Chin,F.Y.,J.Lam,andI.N.Chen.1982.Efcient parallelalgorithmsforsomegraph problems.Communications of the AC,vol.25,no.9,Sept.,pp.659-665.   
Choi,H.A.andB.Narahari.1991.Efcientalgorithms for mappingand partitioing a class of parallel computers.Tech.rept. GWU-IIST-91-04,George Washington University,Washington,   
Chow,P.,Z. G. Vranesic,andJ.L.Yen.1983. A pipeline distributed arithemeticPFFT processor.EEEctionsonCompuersol.C2,no.12ec.,.   
Chronopoulos,A.T.,and C.W.Gear.1989.On theeficient implementationof preconditioned s-step conjugate gradient methods on multiprocessors with memory hierarchy.arallel Computing,vol.11,pp.37-3.   
Chu,E.,and A. George. 1987. Gaussian elimination with partial pivoting and load balancing on a multiprocessor. Parallel Computing,vol. 5, pp. 65-74.   
Chung,K. M.,F.Luccio,and C. K. Wong.1980a. On the complexity of sorting on magnetic bubble memory systems. IEEE Transactions on Computers,vol. C-29, no. 7, July, pp. 553-563.   
Chung, K.-M., F. Luccio,and C. K. Wong. 198ob. Magnetic bubble memory structures for efficient sorting and searching. In Proceedings IFIP Congress: Information Processing, vol. 80, pp. 439-444.   
Church,K.W.1987.Phonological Parsing in Speech Recognition,Kluwer Academic Publishers,oston,   
Cichelli, R. J.1973.Research progress report in computer chess. SIGART Newsletter, vol. 41, Aug., pp. 32-36.   
Clocksin,W.F.,and C.S.Melish.1981.Programming in Prolog. Springer-Verlag, New York.   
Cocke,J.1988. The search for performance in scientific processors.Communications of the ACM,vol.31,no.3,Mar.,pp.250253.   
Coffman,E.G.,Jr.andP.J.Denning.1973.OperatingSystems Teory.PrenticeHall, Englewood Cliffs, NJ.   
Coffman,E.,Jr.,andR.Graham.1972.Optimal scheduling for two processor systems. Acta Informaticavol.1,.3.   
Cole,R. 1987. Slowing down sorting networks to obtain faster sorting algorithms. Journal of the ACm,vol.34,Jan.,pp.200208.   
Cole,R.1988.aalelmergeort.AJouralnomputing,ol.17,o.4ug. pp. 770-785.   
Cole,R.,and U. Vishkin.1986. Approximate and exact parallel scheduling with applications to list,tree,and graph problems.In Proceedings of the 27th Annual IEEE Symposium on Foundations of Computer Science, pp.478-491.   
Colmerauer,A., H. Kanoui, R. Pasero,and P.Roussel.1973.Unsysteme de comunication homme-machine en Francais.Rapport, Groupe Intelligence Artificielle,Universite d'Aix arseille,Luminy,rnce.   
Conery,J.987ralelEeutoficrogms.uweradeicbs, Norwell, .   
Conery,J.S.,andKibler.D.F.981.Paralelinterpretationof logic programs.In Pro ceedings of the Conference on Functional Programming Languages and Computer Architecture.ACM Press,Oct.,pp.163-170   
Conway,M.E.1963.Amultiprocessorsystemdesign.InProceedingsAFIPFalJint Computeree4aooe   
CookS.Ae System Sciencesvol.9no.,p.1.   
Cook,S.A9ofrosicetles In Proceedings of the 1983 International Foundation of Computation Theory Conferenceeenee pp. 78-93.   
Cook,S.A.1985.A taxonomyof problems withfastparallel algorithms.Information and Control,vol.64,..   
Corinthios,M. J.,and K. C. Smith. 1975. A parallel radix-4 fast Fourier transform computer.IEEErsactionsonomutersol.C-24o.1Jan.92.   
Cormen, T.H.,C.E.Leiserson,andR. L.Rivest.199o. Introduction to Algorithm MIT Press,Cambridge.   
Cosnard, M.,M. Marrakchi,and Y. Robert. 1988. Parallel Gaussian elimination on an MIMD computer.Paralel Computing,vol.6,pp.275-296.   
Cosnard,M.dobert986.exityfrallelQctoztionol of the ACM,ol.3,no.Oct.,.   
Crane,B.A.1968. Path finding with associative memory. IEEE Transactions on Com puters,vol.C-17o.7lyp.6.   
Crane,B. A., M. J. Gilmartin,J. H. Huttenhof,P. T.Rux,andR.R. Shively.1972. PEPE computer architecture. COPCON72 igest, IEEE,New York, pp.57-60.   
Cybenko, G.,D.W. Krumme,and K.N. Venkataraman. 1986. Hypercube embedding is NP-complete.In Proceedings of the First Conference on Hypercube Multiprocessors, SIAM Press,delpa,PA,.47   
Cypher,R.E., J. L. C. Sanz,and L. Snyder. 1990. Algorithms for image component labeling on SIMD mesh-connected computers. IEEE Transactions on Computers, vol. C-39,no.2,Feb.,pp.61.   
Cyre,W.R.ndG.J.Lpovski972Ongeneratingmultipliersforacelarfast Fourier transform processor. IEEE Transactions on Computers,vol. C-21no.1, Jan., pp. 83-87.   
Das,C.R.,J. T. Kreulen,M. J. Thazhuthaveetil,andL. N. Bhuyan.199o.Dependability modeling for ultiprocessors.Computervol.23Oct.,9.   
Das,S. K., N. Deo,and S.Prasad. 1990a. Paralel graph algorithms for hypercube computers.ParallelComputingvol.13,pp.1458.   
Das,S. K., N. Deo,and S. Prasad.199ob.Two minimum spanning forest algorithms onfixed-sizehcubecomputers.ralelmputingol.5,.77   
Davis,A.LandR..Keer.982.Data fow programgraphs.Compuerol.14 no. 2, Feb., pp. 26-41.   
De Bruijn,N.G.1984.Some machines definedby directed graphs.Theoretical Computer Science,vol.32,pp.30919.   
Decker,1. C.,D.M.FalcaoandE. Kaskurewicz.992.Paralelimplemenatioof a power system dynamic simulation methodology using the conjugate gradient method. IEEE Tranactionsonowertems,ol.7,eb.,p.465.   
deGroot,A.D.965.Thoughtand Choice inChes.Mouton,TheHague.   
Dehne,F.,A.G.Ferreira,andA.Rau-Chaplin.199o.Paralelbranchandbound on fine-grained hypercube multiprocessors.ParallelComputingvol.15,pp.29.   
Dekel,E.,D.assimindS.ai.981.Parallelmatriadgaphalgori. Journal on Computing,vol.10,no.4, Nov., pp. 657-675.   
Dekel,E.,andS. Sahni.1982.Aparallel matching algorithm for convex bipartite graphs.InProceedingsofthe1982InternationalConferenceonParalelProcesing IEEE,New York,Aug., pp.178-184.   
De Keyser,J.,andD.Roose.1991.A software tool forload balancedadaptive multiple gridsondistributedmemorycomputers.InTheSixth DistributedMemoryComputing Conference Proceedings.EEEComputerSocietyPress,Loslamitos,CA,. 128.   
Deminet, J.1982.Experiencewith multiprocessor algorithms.IEEETransactions on Computers,vol.C-31, no.4,Apr.,pp.27.   
Demuth,H.B.956.Electronicatasorting.Ph..dissertation,Staford Urity Stanford, CA.   
Dennis, J. B.,and E. C. Van Horn. 1966. Programming semantics for multiprogrammed computations.Communications of the ACM, vol. 9,no. 3, Mar., pp. 143-155.   
Deo,N.1974.Graph Theory with Applications to Engineering and Computer Science. Prentice-Hall, Englewood Cliffs,N.   
Deo,N., C. Y. Pang,and R. E. Lord. 1980. Two parallel algorithms for shortest path problems.In Proceedingsof the 1980 International Conference on Parallel Processing,IEEE, New York, Aug., pp. 244-253.   
Deo,N.,and Y. B. Yoo. 1981. Parallel algorithms for the minimum spanning tree problem.In Proceedings of the 1981 International Conference on Parallel Processing, IEEE,New York,Aug., pp. 188-189.   
Dere,W.Y.,and D.J. Sakrison.197o. Berkeley array processor. IEEE Transactions on Computers, vol. C-19, no. 5,May, pp. 444-447.   
Desai,B.C. 1978.The BPU: A staged parallel processing system to solve the zero-one problem. In Proceedings ICs '78,Dec., pp.802-817.   
Dijkstra, E.W.1959.A note on two problems inconnexion with graphs.Numererische Mathematik,vol.1, pp.269-271.   
Dijkstra,E.W.1968a. The structure of the ‘THE’ multiprogramming system. Communications ofthe ACM,vol.11,no.5,May,pp.341-346.   
Dijkstra, E.W.1968b.Cooperating sequential processes.In F.Genuys,ed., Programming Languages,Academic Press,New York.   
Dimitriadis,S.,and Karplus.W.J.199o. Multiprocessor implementationof algoritms for ordinary diferential equations. Simulation,vol.55,Oct.,pp.236-246.   
Dinning,A. 1989. A survey of synchronization methods for parallel computers. Computer, July, pp. 66-77.   
Dongarra,J.J.,andL.Johnsson.1987.Solving banded systems ona parallel processor. Parallel Computing,vol.5, pp.219-246.   
Dongarra, J. J., and A. H. Sameh. 1984. On some parallel banded system solvers. Parallel Computing,vol.1,pp.223-235.   
Dongarra,J.J.,1.S.uff,D.C.Sorenson,andH.A.vanderVorst.1991.SolvingLinear Systems on Vector and Shared Memory Computers.SAMPressPhiladelphia.   
Doshi,K.A.,andP.J. Varman.1987.Optimal graphalgorithmsona fixed-size linear array.IEEE Transactions on Computers,vol. C-36,no.4,Apr.,pp.460-470.   
Douglas,C.C.andB.F.Smith.1989.Using symmetries and antisymmetries toanalyzea paralelmultigrid algorithm: theelliptic boundary valueproblem case.SIAM JournalonNumericalAnalysis,vol.26,Dec.,.4461.   
Douglass,R.J.1984.Characterizing theparalelisminrule-basedexpert systems.ech. Rept.LA-U84-3428,Losamos atioalboratoryosamos   
Dowd,M.,erl,L.dold.ks.983.eacedsortetk.In Proceedings of the Conference on Principles of Distributed Computing, pp.161- 172.   
Dragon,K. M.,and J.L. Gustafson.1989. A low-cost hypercube load-balance algorithm. In Proceedingsofthe Fourth ConferenceonHypercubes,Concurrent Computersand Applications,pp.583-589.   
Driscoll, J. R., H. N. Gabow,R.Shrairman,andR.E. Tarjan.1988.Relaxed heaps: An alternative to Fibonacci heaps with applications to parallel computation. Communications oftheACM,vol.31,no.11Nov.,pp.3454. ivi., aid r. A. Driggs. 1982. Perrormance of synchronized iterative processes in multiprocessor systems. IEEE Transactions on Software Engineering,vol. SE-8, no. 4, July, pp. 419-431.   
Dubois,M.,and F.A. Briggs. 1991. The run-time efficiency of parallel asynchronous algorithms.IEEE Transactions on Computers,vol. C-40,no.11,Nov.,.60 1266.   
Dubois, P. F. 1982. Swimming upstream: Calculating table lookups and piecewise functions.InG.odrigue,ed.,rallelomputations,AcademicPress,eork pp. 129-151.   
Duff,I.S.986.Parallelimplementationofmultifrontal schemes.ParallelComputing, vol. 3, pp. 193-204.   
Duncan,R.99.Asureyfrallelomuterrtecures.mputerb.5 16.   
Duncan,R.99raleerectursIdsinutol. AcademicssranoL.   
Dyer,C.R. 1981. A VLSI pyramid machine for hierarchical parallel image processing. In Proceedings PRIP,pp.381-386.   
Dyer, C. R. 1982.Pyramid algorithms and machines. In K. Preston andL. Uhr,eds., Multicomputers and Image Processing Algorithms and Programs,Academic Press, New York, pp. 409-420.   
Dyer,C. R.,and A. Rosenfeld.1981. Parallel image processing by memory augmented cellular automata.IEEE Transactions on Patern Analysis and Machine Inteligence, vol. PAMI-3, pp. 29-41.   
Eager，D.L., J. Zahorjan, and E. D. Lazowska. 1989. Speedup versus efficiency in parallelsEteso.8ar. 423.   
Eckstein, D. M. 1979.BFS and biconnectivity. Tech.Rept. 79-11,Dept. of Computer Science,Iowa tateUversityofienceandechnologyms.   
Eckstein,D.M.,andD.A.Alton.1977a.Paralel searching of non-sparse graphs. Tech.rept.72ept.ofomuterience,Uversityofowaowaity   
Eckstein,D.M.andD.A.Alton.977b.Parallel gaphprocesingusingdert search.In Proceedings of the Conferenceon TheoreticalComputerScienceUniver sity of Waterloo,Waterloo, Ontario,pp.21-29.   
Eggers,S.J.,and R. H. Katz. 1989. The effectof sharing on the cacheand bus performanceof parallel programs.InProceedingsoftheThird InternationalConferenceon Architectural Support for Programming Languages andOperating Systems,APOs III, p. 257-270.   
Ein-Dor,P.1985. Grosch's law re-revisited: CPU power and the cost of computation. Communications of the ACM,vol.28,no.2,Feb.,pp.42151.   
El-Dessouki, O. I.,and W. H. Huen.1980. Distributed enumeration on network computers.IEEE Transactions on Computers,vol. C-29,no.9, Sept., pp.8125.   
El-Horbaty,E. M.,andA.E.H. Mohamed.1992.A synchronous algorithm for shortest paths on a tree machine. Parallel Computing,vol. 18, pp.103-107.   
Ellis,C.98a.Couetsarchadinrtionin-3tres.Acta Ifomticaol.14 pp. 63-86.   
Ellis,C.198ob.Concurrent search and insertioninAVLtrees.IEEE Transactions on Computers, vol. C-29, no. 9, Sept., pp. 811-817.   
Ellis, J. A.1991. Embedding rectangular grids into square grids. IEEE Transactions on Computers, vol. C-40, no.1, Jan., pp. 46-52.   
Elmagarmid, A. K. 1986. A survey of distributed deadlock detection algorithms. ACM Sigmod Records,Sept., pp.37-45.   
Enslow,P.H.,ed.974.Multiprocessors and Paralel Processing. John Wiley & Sons, New York.   
Enslow,P.H.1977.Multiprocessor organization-Asurvey.Computing Surveys,vol.9, no. 1, Mar., pp. 102-129.   
Eppinger, J. L. i983. An empirical study of insertion and deletion in binary search trees.Communications of theACM,vol.26,no.9,ept.,pp.66-669.   
Esfahanian, A. H.,and S.L. Hakimi. 1985. Fault-tolerant routing in De Bruijn communication networks. IEEE Transactions on Computers, vol. C-34, pp. 777-788.   
ETA.1984.Kuck and Associates to develop advanced preprocessor for ETA10.ETA Systems i/o, vol. 1, no.2, Fall, p.2.   
Evans,D.J.ed.982.ParalelProcessingSystems.CambridgeUniversityPrssCam bridge.   
Evans,D.J.1984.ParalelS.O.R.iterativemethods.ParalelComputingvol.1pp.3 18.   
Evans,D.J.,andY.Yousif.1985.Analysis of the performanceof the paralel quicksort method. BIT, vol. 25, pp. 106-112.   
Evans,D.J.and N.Y.Yousif.1986.Theparalel neighboursortand2-waymerge algorithm.ParallelComputing,vol.3,Mar.,p.590.   
Evans,D.J.1990.Aparalel sorting-mergingalgorithm for tightly coupled multipro cessors.Prallel oming,ol.14,.1.   
Even,S.974.Parallelismintape-soring.Communications oftheACvol.7,no.4 Apr., pp. 202-204.   
Faber,V.,O..LubeckndA.BWite,Jr.1986.perlinearspeedupoft sequential gorithmisotposble.raleComputingvol.3pp.9260   
Fagin,B.S.andA.M.Despain.199o.The performanceofparallel Prolog programs. IEEE Traiosutersl.9.12ec.,p.45.   
Falk,H.197coregaEeu6 70.   
Fang,Z., P.Tang,P.C.YewandC.Q.Zhu.1990.Damicprocessorself-scheuling forgeneralalelstdloosctiosonutersol97, July, pp. 919-929.   
Feierbach, G.,and D. Stevenson. 1979. The ILLIAC IV. In C. R. Jesshope and R. W. Hockneyee Maidenead,d,   
Feldman,J.A.1979. High level programming for distributed computing.Communicationsofthe.e   
Feldmann,R.en,P.etzO.bger99trd treesearch.IVaPGoarisadL..ls.lle Algorithmonellgediogok6 101.   
Felten,E.W.,ndS.W.Otto.1988.Ahighly paralelchessprogram.InProceedings of the International Conference on Fifth Generation Computer Systems I988.ICOT, pp. 1001-1009. Dec, pp. 12-27.   
Ferguson,C.,and R.E.Korf.1988. Distributed Tree Search and its application to alpha-beta pruning. In Proceedings AAAl-88, pp. 128-132.   
Fich,F.E., P. Ragde, and V. Wigderson. 1988. Relations between concurrent-write models of parallel computation. SAM Journal on Computing,vol.17,no.3, June, pp. 606-627.   
Finkel,R.ndJ.Fishburn.982.Parallelisminalpha-beta.Artificial Intelligenceol. 19, no. 1, Sept., pp.89-106.   
Fishburn,J.P.i981.Analysisofspeedupindistributedalgorithms.Ph.D.distation University of Wisconsin-Madison.   
Fishburn,J.P.andR.A.Finkel.1982.Quotient networks.IEEETransactioson Computers,vol.C-31no.4,Apr.,pp.2895.   
Fisher,D.C.1988.Your favorite parallel algorithms might not be as fast as you think. IEEETraotes.72b..   
Flanders, P. M. 1982.A unified approach to a class of data movements on an array processor.EEEciosoCutersol.1o9et.,9.   
Flanders, P.M., D. J. Hunt, S. F.Reddaway,and D.Parkinson.1977. Efficient high speed computing with the Distributed Array Processor.In High Speed Computer and Algorithmieic,o.   
Flanders,P.M.,andS.F.Reddaway.1984.Sorting on DAP.InM.Feilmeier,G.Joubertd pp. 247-252.   
Flatt,H.P.,andK. Kennedy1989.Performanceof paralel processors.ParallelComputing, vol. 12, pp. 1-20.   
Floyd,R.W.962.Agorithm97:ortestpath.CommunicationsoftheCol.5, no. 6, June, p. 345.   
Flynn,M. J.1966. Very high-speed computing systems.Proceedings of the IEEE, vol. 54, no. 12, Dec., pp.190--1909.   
Flynn,M.J.972.omecomputerrganzationsandtheirectiveness.IEEETransactions on Computers,vol. C-21,no. 9,Sept., pp. 948-960.   
Fortune,S.andJ.Wylle.1978.Paralelism inrandomaccess machines.Proceedings of the 1Oth Annual ACM Symposium on Theory ofComputing, pp.114-118.   
Foster,C.C.1976.Content-Addressable Paralel Processors.Van Nostrand Reinhold, New York.   
Foster,I.T.,andS. Taylor.1988.Flat Parlog:A basis forcomparison.International Journal of Parallel Programming,vol.16,no.2.   
Foster,I.,andS.Taylor.1990.Strand:New Concepts inParalelProgramming.Prentice Hall, Englewood Clifs,NJ.   
Foster,M. J.,and H. T. Kung.198o. Design of special-purpose VLSI chips—Example and opinions. Computer, vol.13, no. 1,Jan., pp. 26-40.   
Fox,G. C. 1988. What have we learnt from using real parallel machines to solve real problems? In Proceedings of the Third Conference on Hypercube Concurrent ComputersandApplicationsACMPress,New York,p.97-955.   
Fox,G.C.1989.1989-The first year of the parallel supercomputer.In Proceedings of the Fourth Conferenceon Hypercubes,Concurrent Computersand Applicaion, pp. 1-37.   
Fox,G. C.,and S. W. Otto.1984. Algorithms for concurrent processors. Physics Today, vol. C-37, May, pp. 50-59.   
Fox,G.C.,M. A. Johnson,G.A.Syzenga, S. W. Otto,J.K. Salmon,andD.W. Walker. 1988.Solving Problems on Concurrent Processors,vol.1,General Techniquesand Regular Problems.Prentice Hall,Englewood Clis,.   
Francis,R.S.andI. D.Mathieson.1988.A benchmark parallel sort for shared memory multiprocessors.EEEanctionsonComuters,l.C37,no.12,ec., 9 1626.   
Francis,R. S.,andL. J. H. Pannan. 1992. A paralel partition for enhanced paralel QuickSort. Parallel Computing,vol. 18, pp. 543-550.   
Frenkel,K.A.986.Evaluating two massively parallel machines.Communications of the ACM,vol.29,no.8,Aug.,pp.75758.   
Fritsch,G., W.Kleinoeder, C.U.Linster,andJ.Volkert.1983.EMY85-The Erlanger multi-processor system for a broad spectrum of applications. In Proceedings oftheI98ellenE pp. 325-330.   
Fromm, H.J.,U. Hercksen, U. Herzog, K. H. John,R. Klar,and W. Kleinoder.1983. Experiences with performance measurement and modeling of a processor array. IEEE Traitesl.2.,1   
Fuller,S.H.,and P.N. Oleinick.1976.Initial measurements of parallel programs in a multi-miniprocessor.In Proceedings ofthe 13th IEEEComputer Society International Conference,IEEE,New York,pp.358-363.   
Fujii,M., T.Kasami,and K. Ninamiya.1969. Optimal sequencing of two equivalent processors.AMJournal ofApplied athematics,vol.i7,pp.784789.   
Fung,L.1977.Amassivelypallel procesingcomuter.In.J.Kuck,D.H.Lawrie andA.H.ehs.igheedmuteoithgasatioei Press,London,pp.203-204.   
Fussll,D.，andR.Turimella.988.Separation pairdetection.InProceedings of AWOC88,tureoteIeree9grego pp. 149--159.   
Fusell,D.cdandriell989.nngtrd nentsbylocalreplacements.Inroceedingofthe6thInternationalCollqmon AutomatagedinguretesIteree Springer-Verlag,New York,pp.379-393.   
GabowH.98Atriotossll of theACM,vol.29,no.3,July,pp.766780.   
Gajski,D.D.,D.A.Padua,D.J. KuckandR. H. Kuhn.1982.Asecond opiioon dataflow machinesandlanguages.Computer,Feb.,pp.58-69.   
Galil,Z.197sleebctica7   
Galil,Z.,and W.J.Paul.1981.Aneficient general purpose parallelcomputer.In Proceedings of the 13th Annual ACM Symposium on Theory of Computing，ACM, New York,yp.247262.   
Galil,Z.andJul9eetgealoealelterJl of theACM,ol.,no.2Apr.,.6   
Gallivan, K.A.,R.J.Plemmons,and A.H.Sameh.199o.Paralel algorithms for dense linearalgebracomputations.AReview,vol.32ar.,.5.   
Garey,M.R.andD.S.Johnson.1979.Computers and Intractability:AGuide tothe Theory of N-Completeness.W.H.FreemanSan Francisco.   
Gavrll,F.19/5.Merging With parallel processors.Communications of the ACM,vol.18, no. 10, Oct., pp.588-591.   
Gehringer,E.F.A.K.JonesandZ.Z.Segall98.e $\mathbf { C } \mathbf { m } ^ { * }$ testbed.Computer, Oct., pp. 40-53.   
Geist,G. A.,and M.T.Heath.1986.Matrix factorization ona hypercube multicomputer. InM.T.t pp. 161-180.   
Gelernter,D.1985.Generative communication inLinda.ACM Transactions on Programming Languages andSystems,vol.7,no.1,pp.12.   
Gentleman, W.M.1978.Some complexityresults formatrixcomputationsonparallel computers.JournaloftheAC,vol.25no.1,Jan.,p.1.   
Ghosh,R.K.,andG.P.hattacharjee.1986.Parallelagorithmforshortestpaths.IEE ProceedintEegl3r.   
Gibbons,A.ndWyter.988.EfentPrallelgoithms.CmbidgeUity Press, Cambridge.   
Gilbert,E.J.1983.Algorithm partition tools for a high-performance multiprocesor. Ph.D.disatiardityd   
Gillogly,J.978.Performanceanalysisof thetechnologycesprogam.Phss tation, Carnegie-ellon University,ittsburgh,   
Gilmore, P.A.1974.Matrix computations on an associative processor. In Lecture NotesinCouterencel.24allelrocesng.ringereagok pp. 272-290.   
Glasgow, J.,M. Jenkins, C.McCrosky,andH. Meijer.1989.Expressing parallelalgo rithms in Nial.Parallel Computing,vol.11, pp.331-347.   
Goldberg,A. V.,S. A.Plotkin,andP.M. Vaidya. 1988.Sublinear-time paralel algorithms for matchingand related problems.In Proceedings of the 29th Annual IEEE Symposium on Foundations of Computer Science, IEEE Computer Society，Wash-ington, DC, pp. 174-185.   
Goldberg,M.,and T. Spencer. 1989. A new parallel algorithm for the maximal independent set problem. SIAM Journal on Computing,vol. 18,Apr.,pp.419-427.   
Golden,B.,L.BodinT.Doyle,andW.Stewart,Jr.98o.Approximate traveling salesmanalgorithms.OperationsResearch,ol.28,no.3,ayJune,art2p.694 711.   
Goldschlager,L. M.1977. The monotone and planar circuit value problems are log space complete for P.GACTNews,vol.9,no.2,ummer,p.-29.   
Goldschlager,L. M.1978. A unified approach to models of synchronous paralel machines.In Proceedingsofthe IOthAnnualACMSymposiumonTheoryofComputing, ACM, New York,May,pp.89-94.   
Goldschlager, L. M. 1982. A universal interconnection patrn for parallel computers. Journal ofthe ACM,vol.29,no.4,Oct.,pp.106.   
Goldschlager, L. M., R.A. Shaw,and J. Staples. 1982. The maximum flow problem is log space complete for $P$ Theoretical Computer Science,vol.21,Oct.,pp..   
Goodman, S.E.,and S.T.Hedetniemi. 1977.Introduction to the Design and Analysis of Algorithms. McGraw-Hill,New York,p.265.   
Gottlieb，A. 1986.An overview of the NYU Ultracomputer project. Ultracomputer Note 100, Ultracomputer Research Laboratory,Div. of Computer Science, Courant Institute of Mathematical Sciences. New York University.   
Gottlieb,A., R. Grishman, C. P. Kruskal, K. P. McAuliffe, L. Rudolph, and M. Snir. 1983. The NYU ultracomputer: Designing an MIMD shared memory parallel computer.IEEE Transactionson Computers,vol.C-32,no.2, pp.75189.   
Graham,R.L. 1966.Bounds for certain multiprocessing anomalies. The Bell System TechnicalJoral,v.,p.   
Graham,R.L. 1969. Bounds on multiprocessing timing anomalies. SIAM Journal on Appliedmticol.2r..   
Graham,R.L.1972. Bounds on multiprocessing anomalies and packing algorithms. In Proceedings AF 1972 Spring Joint ComputerConference,pp.205-217.   
Graunke,G.,andS.Thakkar.199o.Synchronizationalgorithmsfor shared-memory multiprocessors. Computer,June, pp. 60-69.   
Greenberg,D. S.1987.Optimal expansion embeddings of meshes in hypercubes. Tech.rept.LEU/C/-35,ept.ofomputerience,YaleUiverityew Haven, CT, Aug.   
Gregory，S.987.aralelogicrogramminginrlog.ddison-Wesleyeing, MA.   
Greif,1.1977Ageforalobesectio.Commcatisoth ACM,vol.2,no.12,ec.,pp..   
Gropp,W.D987SolvingDEsonooselycoupedparalelproceos.Parallel Computing,vol.5,pp.165-173.   
Grosch,H. A.1953. Highspeed arithmetic: The digital computer as aresearch tool. Journaloftiletyeri..   
Grosch,H.A.975.rosch'sawrevisited.Compuerworld,vol.8,no.16,Apr.24.   
Gu,Q.P.,and T.Takaoka.1990.Asharperanalysis of aparalelalgorithmfortheall pairs shortestpathproblem.aralelComputingol.16,p.67.   
Guan,X.,and M. A. Langston. 1991. Time-space optimal parallel merging and sorting. IEEETs   
Guibas,L. J., H. T. Kung,and C. D. Thompson. 1979. Direct VLSI implementation of combinatorialproblems.InProceedingsoftheConferenceon VeryLargeScale Integratioeiote Pasadena, pp.509-525.   
Gupta,A.K.andS.E.Hambrusch.1991.Embeddingcomplete binarytreesinto bterfly 863.   
Gupta,A. K.,and S.E.Hambrusch.1992.Loadbalanced tree embedings.Parallel Computing,ol.8,14.   
Gupta,A.,and W. D.Weber.1992. Cache invalidation paterns in shared-memory multiprocessors.Esctionsonomputersol.C-41o.7ulyp94 810.   
Gurd,J. R., C.C.KirkhamandI. Watson.985.The anchester prototype dataflow coute   
Gustafson,J.L.988.Reevaluating Amdahl'slaw.CommunicationsoftheAC,ol.21 no.5,May,pp.523.   
Gustafson, J.L.,G.R. MontryandR.E. Benner.1988. Development of paralel methods for a 1024-processor hypercube. SIAM Journal on Scientific and Statistical Computing,vol.9,no.4,July,pp.68.   
Habermann,A.N.972.Parallelneighborsort.Tech.rept.,Carnegie-MellonUnisity, Pittsburgh, P.   
Hagerup,T.1990.Planar depth-first search in $O ( \log n )$ parallel time.SIAMJournal on Computing,ol.9o.4Aug.,.04.   
Haggvist,R.andP.Hell.1981.Parallel sorting withconstant time forcomparisons. SIAMJouralonmputingol.o.3,ug..   
Halliday,D.,and R.Resnick. 1974. Fundamentals of Physics.Rev.ed. John Wiley& Sons, New York.   
Halstead,R.H.,Jr.986.Paralel symboliccomputing.Computer,vol.19,no.8Aug. pp. 35-43.   
Hambrusch,S.E.1982. The complexityof graph problems on VLSI.Ph.D.dissertation, The Pennsylvania State University, University Park.   
Hambrusch,S.E.1983.VLSI algorithms for theconnected component problem.SIAM Journal on Computing,vol. 12,pp.354-365.   
Han,Y.,andR.A.Wagner.99.Aneficentandastparallelcoectedomoent algorithm.JournaloftheACvol.37,Julyp.626642.   
Handler,W.1977. The impact of classificationschemes on computer architecture. Proceedings of the 1977 International Conference on Paralel ProcessingIEEE New York,Aug., pp.7-15.   
Hansen, P.,and K. W.Lih. 1992. Improved algorithms for partitioning problems in parallel,ielidstedingEcio vol. C-41, no. 6, June, pp. 769-770.   
Harary,F.1969.Graph Theory.Addison-Wesley,Reading,MA.   
Harrison,P.G.and N.M.Patel.1990.The representation ofmultistage interconection networks in queuing models of paralel systems. Journal of the ACM,vol. 37, no. 4, Oct., pp. 863-898.   
Harrison,T.J.,and M. W. Wilson.1983. Special-purpose computers. In A. Ralston,ed. EncyclopediaofComputerScienceand Engineering,2ded.Van Nostrand-Reinhold, New York, pp.1385-1393.   
Hatcher,P.J.,andM.J.Quinn.1991.ata-ParallelProgrammingonMMDComput ers,MITPress,Cambridge.   
Hatcher, P.J.，M. J. Quinn, R. J. Anderson, A. J. Lapadula, B. K. Seevers, and A. F.Bennett. 1991a. Architecture-independent scientific programming in Dataparallel C:reecseties.Inercompuing'9ework 208-217.   
Hatcher, P. J., M. J. Quinn, A. J. Lapadula, R. R. Jones, and R. J. Anderson. 1991b. A production-quality $C ^ { * }$ compiler for a hypercube multicomputer. In Proceedings of the Third ACM SIGPLAN Symposium on Principles and Practice of Paralel Programming, pp.73-82.   
Hatcher,P. J., M. J. Quinn,A. J. Lapadula, B. K. Seevers, R. J. Anderson， and R.R.Jones.1991c. Data-parallel programming on MIMD computers. IEEE Transactions onarallel andistributedSystems,vol.2,no.3,Julypp.37-83.   
Havel,I.,and J.Moravek.1972. B-valuations of graphs. Czechoslovak Mathematical Journal, vol. 22,pp.33851.   
Hayes,J.P.1988.Computer Architecture and Organization,2d edition.McGraw-Hill, New York.   
Haynes,L. S., R. L. Lau, D. P. Siewiorek, and D. Mizell. 1982. A survey of highly parallel computing. Computer, vol. 14, no. 1, Jan., pp. 9-24.   
He, X., and Y. Yesna. T988. A neariy opumal paraner aigorium ior consuucung depun first spanning trees in planar graphs. SIAM Journal on Computing,vol. 17,no. 3, June, pp. 486--491.   
Heath,L. S., A.L. Rosenberg,and B. T. Smith.1988. The physical mapping problem for paralel architectures.Journal of the ACM,vol.35,July, pp. 603-634.   
Heath,M. T.,E. Ng,and B. W. Peyton.1991.Parallel algorithms for sparse linear systems. SIAM Review,vol. 33, Sept.,pp. 420-460.   
Heidelberger,P.,A. Norton,andJ. T. Robinson.199o. Parallel quicksort using fetchand-add.IEEE Transactionson Computers,vol.C39,no.1,Jan.,pp.33138.   
Heller, D.1978. A survey of parallel algorithms in numerical linear algebra. SIAM Review,vol.20, pp.74077.   
Helman,P.andR. Veroff.986.IntermediateProblemSolvingandData Structur: Walls and Mirrors.Benjamin/Cummings,Menlo Park,CA.   
Helmbold,D.andE.Mayr.987.TwoprocessrchedulingisinNC.AJoual on Computing,vol.16,no.4,Aug.,pp.7759.   
Hennessy,J.L.and D.A.Patterson.1990.Computer Architecture:A Quantittive Approach,organ Kaufmann,an ateo, .   
Herter,C. G., T. M. Warschko, W. F. Tichy,and M. Philippsen.1993. Triton/1:A massively-parallel mixed-mode computer designed to support high level languages. InProceedings oftheInternational ParallelProcessingSymposium.   
Higbie,L.C.972.heOcmputers:Associativearrayprocessors.InCCN 72 Digest.IEEE,New York,pp.287-290.   
Hill,M.DdJ.us99cheoideratioouiprocssr mers.Communicationsofthevol.33,no.ug.,1.   
Hillis,W.D.,and G.L.Steele,Jr.986.Data parallelalgorithms. Communications of theACM,vol.29,no.12,ec.,p..   
Hillis,W.D.andG.L.Steele,Jr.987.Update toataparallelalgorithms.Commu nications oftheol.30o.Ja   
Hirschberg,D.S.1976.Parallelalgorithmsforthe transitiveclosureandtheconected component problem.In Proceedings of the8thAnnual ACM Symposium on theTheory ofComputing,AC,New ork,ayp.57   
Hirschberg.978stralelinggsomucatsofe vol. 21, no. 8,Aug., pp. 657-666.   
Hirschberg,D. S. 1982. Parallel graph algorithms without memory conflicts.In Proceedings of the 20th Allerton Conference,Oct.,pp.257-263.University ofIllinois, Urbana-Champaign.   
Hirschberg, D. S., A. K. Chandra, and D. V. Sarwate. 1979. Computing connected components on parallel computers. Communications of the ACM, vol. 22, no. 8, Aug., pp. 461-464.   
Ho,C.T.,and S.L. Johnsson.1987. On the embedding of arbitrary meshes in Boolean cubes with expansion two dilation two.In Proceedings of the International ConferenceonPraelsing191   
Hoare,C.A.R.962.Quicksort.The Computer Journal,vol.5,pp.15.   
Hoare,C. A. R. 1974. Monitors: An operating system structuring concept. Communicationsoftheol.7o.ct.,.   
Hoare,C.A.R.1978.Communicating sequential proceses.Communications of the ACM, vol. 21, no. 8, Aug., pp. 666-677.   
Hockney, R. W.1965. A fast direct solution of Poisson's equation using Fourier analysis.JournaloftheCol.no.an,   
Hockney,R.W.andC.R.Jesshope.981.ParallelComputers:Architecture,Proram ming andlgorithms.amlger,ristol,lad   
Hoey,D.and C. E. Leiserson. 198o. A layout for the shuffle-exchange network. In Proceedings of the 198o International Conference on Parallel Processing，IEEE, New York, Aug.,p.329-336.   
Holt,R. C.,G.S. Graham,E.D.Lazowska,and M. A.Scot.1978.Structured Concur rent Programming withOperating System Applications.Addison-WesleyReading, MA.   
Hong,J.-W., K. Mehlhorn,and A. Rosenberg. 1983. Cost trade-offs in graph embeddings,with applications.Journal of the ACM,vol.30,no.4,Oct.,pp.709-728.   
Hong,Z.,and R. Sedgewick. 1982. Notes on merging networks. Proceedings of the 14th Annual ACymposiumon the Theoryofomputing,ACM,New York,ay pp. 296-302.   
Hopcroft, J.E.,and J. D. Ullman. 1973. Set-merging algorithms. SIAM Journal on Computing,vol.2,pp.294-303.   
Hopcroft,J.E.andJ.D.Ullman.1979.Introduction toAutomata TheoryLanguages and Computation.ddisonWesleyeaing.   
Hoppe,H. C.,and H. Muhlenbein. 1986. Paralel adaptive full-multigrid methods on messge-based multiprocessors.Paralel Computing,vol.3,pp.269287.   
Horowitz,E.1979. VLSI architectures for matrix computations. In Proceedings of the1979 ternationaloerenceonrallelrocessingEE,ew Yorkg pp. 124-127.   
Horowitz,E.andS.Sahni978.FundamentalsofComputerAgorithms.Computer Science Press,Potomac,.   
Horowitz, E.,and A. Zorat. 1983. Divide and conquer for parallel processing. IEEE TransactionsonComputers,vol.C32,no.6,June,pp.55.   
Hsiao,C.C.,andL.Snyder.1983. Omni-sort: A versatiledata processngoperation for VLSI.InProceeingsofthe1983InternationalConferenceonParalelProcesing, IEEE, New York, Aug., pp. 222-225.   
Hu,T. Paralel sequencing and assmbly line problems. Operations Research,vol.9, pp. 841-848.   
Huang，Y.,and Y. Paker. 1991. A parallel FFT algorithm for transputer networks. Parallel Computing,vol.17,pp.895-906.   
Hudak,P.1986. Para-functional programming.Computer,vol.19,no.8,Aug.,pp.60 70.   
Hull,M.E.C.1984.Aparalelviewofstablemarriages.IformationProcessingLetters, vol.18,Feb., pp. 6--66.   
Huntbach,M.M,andBurton.1988.Alpha-beta search onvirtual tree machines.Information Sciences,vol.44, pp.317.   
Hwang, K. 1984. Supercomputers: Design and Applications. IEEE Computer Society Press, Silver Spring, MD.   
Hwang,K.,andF.A.Briggs.1984.Computer Architectureand Parallel Processing. McGraw-Hill,ewk.   
Hwang,K.,and Y. H. Cheng. 1982. Partitioned matrix algorithms for VLSI arithmetic system. IEEE Transactions onComputers, vol. C-31,no.12,Dec.,pp.1215-1224.   
Hwang,K.,S.P.SuandL.M.Ni.981. Vectoromputerarchitectureand procesng techniques.In.ovits,ed.,dvances inomputers,ol.2Academic Presew York, pp. 115-197.   
Hyafil,L.976.Bounds for selection.AMJournal on Computing,vol.5,no.1,Feb., pp. 109-114.   
Hyatt,R.M.,B.W.Suter,and H.L.Nelson.1989.Aparalelalpha/beta treesearching algorithm.Parallel Computing,vol.10,pp.299-308.   
Ibaraki,T.1976a. Computational eficiencyof approximate branch-and-bound algorithms.MathematicalOperations esearch,vol.1,no.3,pp.98.   
Ibaraki,T. 1976b. Theoretical comparisons of search strategies in branch-and-bound algorithms.InternationalJournalofomputerandInformationScence,vol.5o.4 pp. 315-344.   
Ichiyoshi, N., T. Miyazaki,and K. Taki.1987. A distributed implementationof Flat GHConthe Multi-PSI.In Proceedingsof the Fourth InternationalConference on Logic Programming,MPress,Cambridge,pp.257-275.   
Imai,M.,T.FukumaraandY.Yoshida.1979.Apaalelizedbranchand-boundal gorithm: Imlemtaiondfency.temmputertolsol. pp. 62-70.   
Irani,K.B.,and K.W. Chen.1982. Minimization of interprocessor communication forparalelutaioEctisouterso. pp. 1067-1075.   
Isloor,S.S.andT.A.Marsland.980.hedeadlock problem:Anoverview.Computer Sept., pp. 58--77.   
Jacobi, C. G. J. 1845. Uber eine Neue Auflosungsart der bei der Methode der KleinstenQuadrate VrkommendenLereneichungenAstrchr.ol.22 pp. 297-306.   
JaJa,J.992.Antrouciontoralelgorih.disoWeseyeai   
JaJa,J.andJ.Simon.982.Paralllalgorithmsingraphtheory:anaritytesting.A Journalonomuino.1oy   
Jamieson,L.H., D.Gannon,and R. J. Douglass,eds.1987. The Characteristicsof Paralel Algorithm.ss,Cmdge   
Janakiram,V.K.，D.P.AgrawalandR.ehrotra.1988.Arandomized rallel backtrackinglgorithm.EEEactionsonomutesol.C7oc pp. 1665-1676.   
Jess, J. A. G.,and H. G. M. Kees. 1982. A data structure for parallel L/U decomposition. IEEETracuteso.a.   
Jesshope, C.R. 1980. Implementation of fast RADIX 2 transforms on array processors. IEEETraeso.an.   
Johnson,D.S.1983.The NP-completeness column:Anongoing guide. Journal of Algorithmsvol.4,p   
Johnsson, S.L.,and C. T. Ho. 1989. Optimum broadcasting and personalized communications inyercubes.EEE ransactions on omputers,vol.C38,no.9ept. pp. 1249-1268.   
Jones,A. K.,and E. F. Gehringer, eds.1980. The Cm\* multiprocessor project: A research review.Tech.rept.CMU-CS-80-131,Dept.ofComputer Science,Carnegie Mellon Usiy   
Jones,A. K.,and P.Schwarz. 1980.Experience using multiprocessor systems—A status report.ACoutingueso.2.2Je5.   
Jones,N.D.1975.Space-bounded reducibility among combinatorial problems.Journal ofComputer Science and SystemSciences,vol.11,pp.68-85.   
Joseph, M., V.R. Prasad,and N. Natarajan.1984. A Multiprocessor Operating Sys tem.Prentice-all,nglewoods,.   
Kale,L.V.andV.A.Saletore.99o.Parallel state-space search forafirst solution with consistent linear speedups. International Journal of Parallel Programming,vol.19, no. 4, pp. 251-293.   
Kanevsky， A.,and V. Ramachandran. 1987. Improved algorithms for graph fourconectivity.InProceedingsofthe28thAnnualIEEESymposiumonFoundationsof Computereeteety   
Kang,Y.M.,R.B.illerandR.A.Pick.1986.CommentsonGrosch'slawre revisited: CPU power and the cost of computation. Communications of the ACM, vol. 29, no.8,Aug.,pp.779-781.   
Karlin,A. R.andE. Upfal.1988.Parallel hashing-aneficient implementationof shared memory.JouraloftheAC,ol.35,o.4pp.692.   
Karp,A.H.987.Programming forparallelism.Computer,May,pp.4-57.   
Karp,A.H.ndR.G.bbII988.Acomprisoof12 pralelortandalecs. IEEE Software,vol.5,no.5,Sept.,p.566.   
Karp,A.H.dH.att99eurgralelcofo nications oftheAC,vol.33,no.5,ay,pp.53943.   
Karp,A. H.,andJ.Grestadt.987.Animproved paralelJacobi methodfordiago nalizing asymmetric matrix.Parallel Computing,vol.5,pp.281-294.   
Karp,R.M.,andV.Ramachandran.199o.Paralelalgorithmsforshared-memorymachines.InJeeticleee Elsevier Science Publishers,North Holand, pp.869-941.   
Karp,R.M.,and A.Wigderson.1985. A fast parallel algorithm for the maximal independent set problem.Journal oftheACMvol.32,no.4,Oct.,pp.76773.   
Kasahara,H.and S.Narita.1984.Practical multiprocessor schedulingalgorithms for efficient paralel processing.EEEransactionsonComputers,vol.C-33,no.1 Nov., pp. 1023-1029.   
Kedem, Z. M.,and A. Zorat.1981. On relations between input and communication/comparison in VLSI (preliminary report). In Proceedingsof the 22d Annual Symposium onFoundationsofComputerScience,EEE,New York,Oct.,p.37-44.   
Keller,R.M. 1976. Formal verification of parallel programs. Communications of the ACM,vol.19,no.7,July,pp.374.   
Khuller,S.andB.chieber.1991.Ecientparallelalgorithmsforting $k$ -connectivity and finding disjoint s-t paths in graphs.SAMJournal on Computing,vol.20Apr. pp. 352-375.   
Kim,H.J.，and J.G.Lee. 1990. A paralel algorithm solving a tridiagonal Toeplitz linear system.Parallel Computing,vol.13,pp.289-294.   
Klein,P. N., and J. H. Reif. 1986. An effcient parallel algorithm for planarity. In Proceedings of the 27th Annual IEEE Symposium on the Foundations of Computer Science, pp.465-477.   
Kleitman, D., F. T. Leighton, M.Lepley，andG.L. Miller.1981. New layouts for the shuffle-exchange graph.In Proceedings of the 13th Annual ACM Symposium on Theoryofomputing,ACM,ew York,ay,.2792.   
Knuth,D.E.97.heArtofomputerProgrammingvol.3.Addison-Wesleyeading, MA.   
Knuth,D.E.1976.Big omicronand big omega andbig theta. SIGACTNews,Apr.June, pp. 18-23.   
Knuth,D.E.,andR.W. Moore.1975. Ananalysis of alpha-beta pruning.Artificial Intelligence,vol.6,pp.293-326.   
Kogge,P.M.,and H. S. Stone. 1973.A parallel algorithm for the efficient solution of a general class of recurrence equations. IEEE Transactions on Computers, vol.C-22, no. 8, Aug., pp. 786-793.   
Kosaraju,S.R.1979.Fast parallel processing array algorithms for some graph problems. In Proceedings of the 1ith Annual ACM Symposium on Theory of Computing,ACM, New York,aypp.31236.   
Kosaraju, S.R.,and M.J. Atallah.1988. Optimal simulations between mesh-conected arrays of processors.Journal of the ACM,vol.35,no.3,July,pp.635-650.   
Kowalik,J.S.,ed.985.Paralel DComputation:HEPSupercomputernd It Applications.Mress,Cambridge,   
Kowalski,R.1979.Logic for ProblemSolving.North-Holland,New York.   
Kozen,D.9oeityofielysedeas.Inoceedinge9t AnnualAiingewk 177.   
Kramer,M.R.andJ.van Leeuwen.1982.Systoliccomputationand VLSI. Tech.rept. RUU-CS-8-9,kgropIormatica,RiiversiteitUtrht   
Krechel,A.H.JundK.9aleto of thesolutionoftriagoallinearstems.rallelComputingol.1449.   
Krumme, D.W.,and K. Venkataraman.1986.On the NP-hardness of a certain construction.Tech.rept86-1,ept.ofomputerience,uftsUniv.,edrd   
Kruskal, C.P.1982.Results in parallelsearching,merging,and sorting. Proceedings of the1982 IetleeeeloingEEk pp. 196-198.   
Kruskal, C. P.1983. Searching,merging and sorting in parallel computation. IEEE Transactionsoutersol.21Oct.,4946   
Kruskal, C.P.,and A. Weiss.1984. Allocating independent subtasks on parallel processors.In Proceedings of the 1984 International Conference on Paralel Processing, pp. 183-187.   
Kruskal, J. B.1956. On the shortest subtree of a graph and the traveling salesman problem.Poceedinsftemricntemticaletyol.eb 50.   
Kucera,L.1982.Paralel computation and conflicts inmemory access. Information Processing Leters, vol. 14, no.2,Apr., pp.9-96.   
Kuck,D. J. 1977. A survey of parallel machine organization and programming. ComputingSurveys,vol.9,no.1ar..9.   
Kuck,D.J.1978.The Structure ofComputers andComputations,vol.1,Wiley &Sons, New York.   
Kuhn,R.H.,and D.A.Padua.1981.Tutorial on Parallel Processing. IEEE Computer Society Press,Los Angeles.   
Kulkarni, A. V.,and D.W.L. Yen.1982. Systolic processing and an implementation for signal and image rocessng.EEE ransactionsonomputersvol.C31o. Oct., pp.1000-1009.   
Kumar, M.,and D. S.Hirschberg.1983. An efficient implementation of Batcher's odd-even mergealgorithmanditsapplication inparallel sortingschemes.IEEE TransactionsonComputers,vol.C-32,no.3,ar.,pp.254-264.   
Kumar,S.P.,and J. S.Kowalik.1984.Parallel factorization of a positive definite matrix onan MIMD computer.In Proceedings of the 1984 International Conference onParallelrocessing,EE,NewYrkAug.p.424.   
Kumar,V.andL.Kanal.1983.A general branch-and-bound formulationforunderstanding and synthesizing AND/OR tree search procedures. Artificial Intelligence, vol. 21, pp. 179-198.   
Kumar, V.,and L. Kanal. 1984. Parallel branch-and-bound formulations for AND/OR treesearch.IEEETransactionsonatternAnalysisndMachine Intelligencevol. PAMI-6,no.6,ov..767   
Kumar, V. P.,and S.M. Reddy.1987. Augmented shuffe-exchange multistage interconnectiontworks.ComputerJune,.40.   
Kung,H.T.976.Synchronized and asynchronousparalelalgorithms for multipro cessors.InJ.F.Traubed.,AlgorithmsandComplexityNewirectionsandecent Results,Academic Press,New York,pp.15-0.   
Kung,H.T.98ohetructureofparalellgorithms.In.Yovits,e.dvancesin Computers,vol.19,Academic Press,New York,pp.65-112.   
Kung,H.T982.Wsstlicarcitecturs?Comuterol.15,no.1,Jan,p46.   
Kung,H.T.andP.L.Lehman.98o.Concurrntmaipulationofbinaryseachtrees. ACM Transactions onatabase Systems,vol.5,Sept.,pp.35482.   
Kung,H. T.,and C.E. Leiserson.198o. Systolic arrays for VLSI. In C. Mead and L.Conwayds.,trouction to ytemsdison-Wesleyeading pp. 260-292.   
Kung,S. Y., K. S. Arun,R. J. Gal-Ezer,and D. V. Bhaskar Rao. 1982. Wavefront array processor: Languages, architecture, and applications. IEEE Transactions on Computers,vol. C-31,no.11,Nov.,pp.105-1066.   
KuttiS.K8allialn vol. 2, pp. 353-359.   
Ladner,R. E. 1975. The circuit value problem is log space complete for $P$ .SIGACT News, vol. 7, no. 1, Jan., pp.18-20.   
Lai,T.H.,and S.Sahni.1984.Anomalies in paralel branch-and-boundalgorithms. Communications oftheACM,vol.27,no.6,June,pp.594-602.   
Lakshmivarahan,S.,andS.K.Dhall.1990.AnalysisandDesignofParallelAlgorithms: Arithmeticand atrix Problems.cGraw-Hill,ework.   
Lakshmivarahan,S., S. K. Dhall,and L.L.Miller.1984.Parallel sortingalgorithms. In M.C.ovits,ed.csinuters.ademicrsk pp. 295-354.   
Lambiote, J.J., Jr.,and D. D. Korn.1979. Computing the fast Fourier transform on a vector computer.athematics ofomputation,vol.33,Julypp.97-992.   
Lamport,L. 1977.Proving the correctness of multiprocess programs. IEEE Transactions on Software Engineering,vol. SE-3, no.7,Mar.,pp.125-143.   
Lang,H. W., M. Schimmler, H.Schmeck,and H. Schroder. 1983. A fast sortingalgo rithm for VLSI. In Proceedings of the 1Oth International Colloquium on Automata Languages, and Programming, pp. 408-419.   
Lang,T.,and H. S. Stone.1976.A shufle-exchange network with simplified control. IEEE Transactions on omputing,vol. -25,Jan. pp.5-56.   
Lansdowne,S.T.,R.E. Cousins,and D.C.Wilkinson.1987.Reprogramming the Sieve of Eratosthenes. Computer, vol. 20, Aug., pp. 90-91.   
Lawrie,D. H.1975.Access and alignment of data in an array processor. IEEE Transactions on Computers,vol.C-24, no. 12,ec., pp.11451155.   
Lea,W. A. 198o. Speech recognition: past, present,and future. In Trends in Speech Recognitiniceall,lewdis,8   
LeBlanc,T.J.1986.Shared memory versus message-passing in a tightly-coupled multiprocessor: A case study.Butterfly Proj. rep.3,Computer Science Dept., University of Rochester,ochester,.   
L'Ecuyer,P.1988.Efcient and portable combined random number generators. Communicationsof the AC,vol.31,no.6,June,pp.742-749,774.   
Lee,C. C., S. Skedzielewski, and J. Feo.1988. On the implementation of applicative languages on shared-memory multiprocessors. GPAN Notices, ol.23, no.9, Sept., Proceedings of the ACM/SIGPAN PPEALS1988--Paralel programming: experience with applications, languages,and systems,pp.188-197.   
Lee,D.T., H. Chang,and C. K. Wong.1981. An on-chip compare/steer bubble sorter. IEEETracotesl.36e   
Lee,S.Y.,and J. K.Aggarwal.1987.Amappingstrategy forparallel procesing. EEE Transactions onComputers,vol.C-36,no.4,Apr., pp.433-442.   
Lehman,P.L.,andS.B.Yao.1981.Efcient locking for concurrent operations on B-trees.Acioneemol.6.4ec.   
Leighton,F.T.1981.New lower bound techniques for VLSI. In Proceedings of the 22dAnnualoioteeceEEew pp. 1-12.   
Leighton,F..1983.Complexity ssuesinVI.Press,Cambridge.   
Leighton,F.T.1984.Tightboundsonthecomplexityofparallelsorting.InProceedings ofthe16thAnualCmposiumonToryofomputingACMNewYrky pp. 71-80.   
Leighton,F99tructotlelordteure Trees Hyercubes.rganufmannan te,.   
Leighton,F.T.,.J.Newman,A.G.Ranade,andE.J.Schwabe.1992.Dyamictree embeddingsinbuterfiesandhypercubes.SA Journal onComputingol.21 no. 4, Aug., pp. 639-654.   
Leiserson,C.E.98o.Area efficient graphlayouts.In Proceedings of the21st Annual Symposiumoniofuerece,EE,wYkct 281.   
Leiserson,C.E.983.Area-Eficent VIComputation.MIPress,Cambridge.   
Leiserson, C.E.,and J.B.Saxe.1981. Optimizing synchronous systems.In Proceedings ofthe22dualSmpsiumonFdationfomuerence,EEeok Oct., pp. 23-36.   
Leler,W.1990.Linda meets Unix.Computer,Feb.,pp.43-54. . 1yoo. A generaiized message-passing mechanism for communicating sequential ss.Eiotersol.7 651.   
Levialdi,S.1972. On shrinking binary picture patterns. Communicationsof the ACM, vol. 15,no.Jan.,   
Levialdi,'S. 1985. A pyramid project using integrated technology. In S.Levialdi, ed., Integrated cnologyorallelIge rocssingcademicrsswork   
Levin,E. 1989. Grand challenges to computational science. Communications of the ACM, vol. 32, no. 12, Dec., pp. 1456-1457.   
Levine,R.D.98.upercomputers.ientificAmericanol.246,no.1,Jan 135.   
Levit,K.N.,and W. T. Kautz.1972. Cellular arrays for the solution of graph problems. Communicaifteo.5t   
Lewis,T.G.,and H. El-Rewini.1992.Introduction to Parallel Computing.Prentice Hall, Englewood Cliffs, NJ.   
Li, G. J., and B. W. Wah. 1984a. How to cope with anomalies in paralel approximate branch-and-bound algorithms. In Proceedings of the National Conference on Artificial Ielligencep5   
Li, G.J.,and B.W. Wah. 1984b. Computational efficiency of parallel approximate branch-and-bound algorithms.In Proceedings of the 1984 International Conference on ParalleroesingE,wokug.,   
Li,G.J.,and B. W. Wah. 1985.MANIP-2: A multicomputer architecture for solving logicprogrammingproblems.InProceedingsof the1985InterationalCoerence onPaallesinEE   
Li,L.M.,and C. T. King. 1988. On partitioning and mapping for hypercube computing. International Journal of Parallel Programming.   
Li, X.,P.Lu,J.eerJ.ion,P.S.WogadH.Si992.Ont tility of parallel sorting byregular sampling.Tech.rept.TR91-06,Mar.Dept.of Computinittaad   
Lillevik,S.L991.heTuchstone3gigaopDLAprottye.InSxthDstribted Memory Computing Conference Proceedings,pp.671-677.   
Lin,F.C.,andK.L.Cung.99o. Acostoptimal paralel trdiagoal sytemsolver. Parallel Computing,vol.15,pp.99.   
Lin,R.,andS.Olariu1992.Afstcostoptimal parallelagorithmfor thelowest common ancestor problem. Parallel Computing,vol. 18, pp.511-516.   
Lin,Y. J.,V. Kumar,and C.Leung.1986.An inteligent backtrackingalgorithm for parallel execution oflogic programs.In Proceedings of the Third International Conference on Logic Programming, pp.55-69.   
Lincoln,N.R.1982.Technologyand design trade-ofs in the creationof a modern supercomputer.EEEransactionsonomputersvol.C-31no.5,ay3 362.   
Lindstrom, G.,and P.Panangaden.1984. Stream-based execution of logic programs. In Proceedings of the1984 International SymposiumonLogic Programming,Feb., pp. 168-176.   
Lint,B.,and T.Agerwala.1981.Communication issues inthedesignand analysis of parallel algoriths.EEEasctionsonoftware Engineeringol.SEo2 Mar., pp. 174-188.   
Lipovski, G.J.,and M. Malek. 1987. Parallel Computing:Theory and Comparisons. Wiley& Sons,New York.   
Lipton,R.J.,and J. Valdes.1981. Census functions: An approach to VLSI upper bounds (preliminary version).In Proceedings of the 22d Annual Symposium on Foundations ofComputer Science,IEEE,New York,Oct., pp.1-22.   
Liskov,B.L., and R. Scheifler. 1982. Guardians and actions: Linguistic support for robust,distributed programs. In Proceedings of the 9th ACM Symposium on Reliability inDistributed Software and atabase Systems,IEEE,New York,pp.53-60.   
Little, J. D. C., K. G. Murty, D. W. Sweeney, and C. Karel. 1963. An algorithm for the traveling salesman problem. Operations Research,vol. 11，no.6, Nov.-Dec., pp.972-989.   
Livingston,M.,andQ.F.Stout.1987.Embeddings inhypercubes.InProceedings of theSixth International Conference on Mathematical Modeling.   
Livny，M. 1983. The study of load balancing algorithms for decentralized distributed processing systems.Ph.D. dissertation, Weizmann Institute of Science.   
Lloyd,J.W.1984.Foundations ofLogic Programming.Springer-Verlag,New York.   
Lo, V. M. 1988. Heuristic algorithms for task assgnment in distributed systems.IEEE Transactions on Computers,vol.C-37,no.11,Nov.,pp.38497.   
Lord,R. E.,J. S. Kowalik,and S.P. Kumar. 1983. Solving linear algebraic equations on an MIMD computer. Journal of the ACM,vol. 30,no.1, Jan., pp.103-117.   
Lorin,H.1972.Parallelismin Hardware andSoftware:RealandApparent Concurency. Prentice-Hall, Englewood Cliffs,NJ.   
Lorin,H.1975.Sorting and Sort Systems.Addison-Wesley,Reading,MA.   
Loui,M.C.1984.The complexity of sorting on distributed systems.Information and Control,vol. 60,pp.7.   
Lubeck,O.,J.Moore,andR.Mendez.1984.Abenchmark comparison of three computers: Fujitsu VP-200, Hitachi S810/20 and Cray X-MP/2. Preprint LA-UR-84-3584, Los Alamos National Laboratory, Los Alamos, N.   
Lubeck, O. M. 1988. Supercomputer performance: the theory, practice, and results. In Advancesinersl.2deicrssado6.   
Luby,M.1986. A simple parallel algorithm for the maximumal independent set problem.SIAMJournal on Computing,vol.15,Nov.,pp.1036-1053.   
Lucas,R.,TankndJ.eman.98.Apaleutiomethodorrgee systems of equations.IEEE Transactions on Computer-Aided Design,vol.CAD-6, Nov., pp. 981-990.   
Luk,F.T.1980. Computing the singular-value decomposition on the ILLIAC IV.ACM Transactionsonathematical oftware,vol.6,no.4ec.,p.9.   
Madala,S.,and J.B.Sinclair.1991.Performanceof synchronousparalelalgorithms with regular structures.IEEE Transactions on Paralel and Distributed Systems, vol.2,no.Jan.,1.   
Madnick,S.EandJ.J.onovan.1974.OperatingSystems,McGraw-Hill,NewYork   
Manber,U.,and R.E.Ladner. 1982.Concurrency control in a dynamic search structure. Tech.repttereit   
Manoharan, S.,and P. Thanisch. 1991. Assigning dependency graphs onto processor networks.raelomputingol.767.   
Marrakchi,M.,andY.Robert.1989. Optimalalgorithms for Gaussian eliminationon an MIMDcomputer.Parallel Computing,vol.12.pp.183-194. ，and iM. Campben. T98z. Parallel search of strongly ordered game trees. Computing Surveys,vol.14,no.4,Dec., pp.551.   
Marsland, T. A.,and P. G. Rushton. 1974. A study of techniques for game-playing programs.InJ.ose,ed.dvancesinCyberneticsandSstemsol.1ro Breach,1   
Martelli,A.，and U.Montanari.1973.Aditive AND/OR graphs.Proceedingsofthe InternationalJointConferenceonArtificial Intellgence,   
Mashburn, H. H. 1979. The C.mmp/Hydra: An architectural overview. Tech. rept., Dept. of Computer Science, Carnegie-Mellon University,Pittsburgh, A.   
Mateti, P.,and N. Deo.1981. Parallel algorithms for the single source shortest path problem. Tech. rept. CS-81-078, Computer Science Dept.,Washington State University,Pullman.   
McGraw, J.R.,and T.S.Axelrod.1988.Exploiting multiprocessors: Isses and options. In Programming Parallel Processors,pp.7-25.Addison-Wesley,Reading,MA.   
Mead,C.ndL.oway.98.Introuctiontostems.ddisoWesleyad ing,MA.   
Mead, C.,and M. Rem. 1979. Cost and performance of VLSI computing structures. IEEE Journal onSolid StateCircuits,vol.SC-14,no.2, pp.455-462.   
Meertens,L.G.L. T.1979.Bitonic sort on ultracomputers.Tech.rept.117/79 Sept. Dept. of Computer Science, The Mathematical Centre,Amsterdam.   
Meggido, N.1983. Applying parallel computation algorithms in the design of serial algorithms.Jalofte.0o.4ct.,p   
Mehlhorn, K., and U. Vishkin. 1984. Randomized and deterministic simulations of PRAMS by parallel machines with restricted granularity of parallel memories. Acta Informica.   
Mendelson,H.987.Economiesof scaleincomputing:Grosch'sIawrevisited.Com municationsofteCo.2e.   
Metcalf,M.,and J. Reid.199o. Fortran 90 Explained.Oxford Science Publications, Oxford, England.   
Meurant,G.1987.Multitasking theconjugate gradientmethodontheCRAYX-P/48. ParallelCuingol.5p   
Mierowsky,C.S.TaylorE.Shapiro,J.Levyand.afra.1985.Theesigand implementationofflatConcurrentProlog. Tech.rept.CS85-09,Weizmann Inst.Science,ehovotel.   
Miler,G.L.andJ.H.Reif.985.Paralleltreecontractionanditsapplication.In Proceedings ofthe26thAnnual IEEE Symposium onthe FoundationsofComputer Science,pp.478-489.   
Miller,G.L.andJ. H.Reif.1991.Paralel trecontraction part2: Furtherapplications. SIAMJouralonuingl.20o.6ec.,p.1   
Miler,R.dFtout984a.outatialgetryoedcom puter.InProceedingsoftheI984InteationalCoferenceonParalelProcsing IEEE,New York, Aug., pp.66-73.   
Miler,R.andQ.F.Stout.1984b.Convexityalgorithms for pyramidcomputers.In Proceedingsofthe984 Inteaionaloferenceonrallel rocesngEE New York,Aug.,pp.177-184.   
Miler，R.,and Q.F.Stout.1985a.Geometric algorithms for digitized pictures on a mesh-connected computer. IEEE Transactions on Patern Analysis and Machine Intelligence, vol. PAMI-7, pp. 216-228.   
Miller, R.,and Q. F. Stout. 1985b. Pyramid computer algorithms for determining geometric properties of images.In Proceedings of the 1985 ACM Symposium on Computational Geometry, pp.263-277.   
Miller,R.,and Q.F. Stout. 1987. Data movement techniques for the pyramid computer. SIAM Journal onComputing,vol.16,no.1,Feb.,pp.38-60.   
Minsky,M.,and S. Papert. 1971. On some associative parallel and analog computations. In E.J. Jacks,ed.,Associative Information Techniques,American Elsevierew York.   
Miranker,G.,L. Tang,and C.K.Wong. 1983.A “zero-time”VLSI sorter.IBM Journal of Research andDevelopment,vol.27,no.2, pp.14148.   
Missirlis, N.M.1987. Scheduling parallel iterative methods on multiprocessor systems. Parallel Computing,vol.5,pp.295-02.   
Misra,J.,and Chandy,K.M. 1982.A distributed graph algorithm: Knot detection. ACM Transactions on Programming Languages and Systems, vol. 4, no.4,Oct., pp. 678-686.   
Mohan,J. 1983.Experience with two parallel programs solving the traveling salesman problem. In Proceedings of the 1983 International Conference on Paralll Processing, IEEE,New York,Aug., pp.191-193.   
Moitra,A.1987.Parallel algorithms for some computational problems.In Advances in Computers, vol. 26,Academic Press,Orlando,FL,pp.93-153.   
Moore,E.F.1959.Theshortest path throughamaze.In Proceedings ofthe International Symposium on the Theory of Switching,vol.2,pp.285-292.   
Moravec,H.P979.Fullintercoectedmultipleomputerswithpelidoing nets.IEEE Transactions on Computers,vol.C-28,no.10,Oct.,pp.795-801.   
Moto-oka,T.,ed.982.FifthGenerationComputerSystems.orth-olland,Nework.   
Mudge,T.N.,J.P.HayesandD.C.Winsor.1987.Multiple busarchitectures.Computer, June, pp.42-48.   
Mukhopadhyay, A. 1981. WEAVESORT—A new sorting algorithm for VLSI. Tech. rept. TR-53-81, University of Central Florida,Orlando.   
Mukhopadhyay, A. and T. Ichikawa. 1972. An $n$ step parallel sorting machine.Tech. rept.72-03,Dept.ofComputer Science,UniversityofIowa.   
Muller,D.E.,and F.P. Preparata.1975. Bounds and complexities of networks for sorting and for switching. Journal of the ACM,vol.22,no.2,Apr.,pp.195-201.   
Mundie,D.A.ndD.A.Fisher.986.Parallel processing inAda.Computer,vol.19, no. 8, Aug., pp. 20-25.   
Naor,J.,M.NaorndA.A.Schafer.989.Fastparallelalgorithmsforchordal gaphs. SIAMJournalonComputing,vol.18Apr.,p.49.   
NassimiD.andS.Sahni.1979.Bitonicsort onameshconnected parallelcomputer. IEEE Traiers.8J   
NassimiD.and S.Sahni.198Oa.Anoptimal routingalgorithmfor mesh-conected paralelcotes.Jalfthel.   
Nassimi,D.andS.Sahni.198ob.Findingconnectedcomponentsandconnectedones onameshoctedalelter.Aualntigo.o.4 Nov., pp. 744-757.   
Nasimi,D.andS.Sahni.1981.Data broadcasting inSIMDcomputers.IEEETrans actions onComputers,vol.C-30,no.2,pp.107. unu S. saim. T9oz. Faraner permutation and sorting algorithms and a new generalized connection network.Journal of the AC,vol.29,no.3,Julyp.642 667.   
Nath,D.,and S.N.Maheshwari.982.Paralelalgorithms for theconnected components and minimal spanning tree problems. Information Processing Letters, vol.14,no.1, Mar., pp. 7-11.   
Nath,D., S. N.Maheshwari,and P.C. P. Bhatt.1983. Eficient VLSI networks for parallel processing based on orthogonal trees. IEEE Transactions on Computers, vol. C-32no.Je,.   
Nau,D. S.1982. An investigation of the causes of pathology in games. Artificial Intelligenceol..   
Nebesky,L.1974. Oncubes and dichotomic trees.Casopis Pro Pestovani Matematiky， vol. 99, pp. 164-167.   
Newborn,M. 1989.Computer chess: ten years of significant progress. In Advances in Computers,vol.29.Academic Press,Orlando,FL.pp.197-250.   
Ng,K. W.,and H. F.Leung.1988. A competition model for parallel execution of logic programs.InProceedingsoftheFifthInternationalConferenceonLogicProgam ming, pp. 55-69.   
Nitzberg, B.,and V. Lo.1991.Distributed shared memory:A survey of issues and algorithms.Computer,Aug.,pp.52-60.   
Norton,A.,and A.J. Silberger.1987. Parallelization and performance analysis of the Cooley-Tukey FFT algorithm for shared-memory architectures. IEEE Transactions onCompues..y91   
Nussbaum,DndA.garal.1991.alabilityofparalelmachines.Commuicaio of the ACM,vol.34,no.3,Mar., pp.56--61.   
O'Leary,D. P.1987. Parallel implementation of the block conjugate gradient algoritm. ParallelComputing,vol.5,pp.127-139.   
Oleinick,P.N.982.ParalelgorithmsonaMultprocesr.UMesearchres, Ann Arbor, MI.   
Orcutt,S.E.1974.Computerrganiationandalgorithms forvery highspeedcompu tations.d   
Orenstein,J.A.,T.H.MerrettandL. Devroye.1983.Linear sorting with O(logn) processors. BIT, vol. 23, pp.170-180.   
Organick,E.I.1985. Algorithms,concurrent processors,and computer sience education: or,“Think concurrent or capitulate?” ACM SGSE Bulletin,vol.17,no.1, Mar.   
Ortega,J.M1988.heijkformsoffactorzationmethodsI.Vectorcomputers.Paralel Computing, vol. 7, pp. 135-147.   
Ortega,J.M.,andC.H.Romine.1988. Theijk formsoffactorizationmethods I.Par allel systems.Parallel Computing,vol.7, pp.149--162.   
Ortega,J.M.andR.G.Voigt.1985.Soutionofpartialdiferentialequationsonector and parallel computers. AReview, vol. 27, no. 2, June,pp.149-240.   
Osterhaug,A.1986.Guide to Paralel Programming on Sequent Computer Systems. Sequent Computer Systems, Beaverton, R.   
Ostlund,N.S.,P.G.Hibbard,andR.A.Whiteside.1982.Acasestudyintheapplication of a tightly coupled multiprocessor to scientific computations. In G.Rodrigue,ed., Parallel Computations. Academic Press. New York.pp.315-364.   
Ottman, T. A., A. L. Rosenberg,and L. J. Stockmeyer. 1982. A dictionary machine (for VLSI). IEEE Transactions on Computers, vol. C-31, no. 9, Sept., pp. 892-897.   
Owicki, S.,and D. Gries. 1976. Verifying properties of parallel programs: An axiomatic approach.Communications ofthe ACM,vol.19,no.5,May,pp.279-285.   
Owicki, S.,and L.Lamport. 1982. Proving liveness properties of concurrent programs. ACM Transactions on Programming Languages and Systems, vol. 4, no. 3,July pp. 455-495.   
Oyama,T.,Kitahara,T.,and Y.Serizawa. 199o. Parallel processing for powersystem analysis using band matrix. IEEE Transactions on Power Systems,vol.5,Aug. pp. 1010-1016.   
Paige,R. C.,and C. P. Kruskal. 1985. Parallel algorithms for shortest path problems. In Proceedings of the 1985 International Conference on Parallel Processing,Aug., pp. 14-20. IEEE,New York.   
Pancake, C. M.,and D. Bergmark. 1990. Do parallel languages respond to the needs of scientific programmers? Computer,Dec.,pp.1-3.   
Papadimitriou, C. H.,and M. Yannakakis. 199o. Towards an architecture-independent analysis of parallel algorithms.SIAMJournal on Computing,vol.19,Apr.,pp.322- 328.   
Pape,U. 1974.Implementation and efciency of Moore-algorithms for the shortest route problem.Mathematical Programming,vol.7,no.2,Oct.,pp.2.   
Parker,D.S.,Jr.98o.Notes onshuffle/exchange-typeswitching networks.IEEE Transactions onComputers,vol.C-29,no.3,Mar.,pp.21-22.   
Parkinson,D.,and M.Wunderlich.1984.A compact algorithm for Gaussian elimination over GF(2) implemented on highly parallelcomputers. Parallel Computing,vol.1, pp. 65-73.   
Patrick,M.L.,D.A.Reed,andR. G. Voigt.1987.The impactof domain partitioning on the performance of a shared memory multiprocessor.Parallel Computing,vol.5, pp. 211-217.   
Paul,G.1978.Large-scale vectorarrayprocessors.IBesearcheport RC 7306, Sept.   
Pease,M.C..968.AnadaptioftheastFouriertrafofrpaelpresing Journal oftheACMvol.15,no.2,Apr.,p.64   
Pease,M.C.II.1977. The indirectbinary $n$ cubemicroprocessor array.IEEE Transactions onomuterso.26o.5,ay.   
Perl,Y. 1983. Bitonic and odd-even networks are more than merging. Tech. rept., Rutgers University,New Brunswick, NJ.   
Perrott,.8.allelgiei   
Peters,F.1981.Tree machineand divide-and-conquer algorithms.In CONAR '81, LectureNotesinomputeriece11rngerVerg   
Peterson,G.L91.ytsboutteutalecsionrbem.Iormaiono ing Leters,vol.12,no.3,June,pp.516.   
Peterson, G. L. 1982. An $O ( n \log n )$ unidirectionalalgorithm for thecircularextrema problem. ACM Transactions on Programming Language and Systems vol.4,no.4, pp. 758-762.   
Piskoulisjski99aalspalfouti agonal Toeplitz linear system of equations. Parallel Computing,vol. 18, pp. 431- 438.   
Polychronopoulos, C. D.,and D. J. Kuck. 1987. Guided self-scheduling: A practical scheduling scheme for parallel supercomputers. IEEE Transactions on Computers, vol. C-36, no.12,Dec.,pp.1425-1439.   
Potter,J.L.985.Programming the MPP.InJ.L.Potter,ed.he MassivelyParallel Processor,ress,Cambridge,pp.1-229.   
Powley, C., Ferguson,C.,and R.E. Korf.199o. Paralel heuristic search: Two approaches.InV.Kumar,P.S.Gopalakrishnan,andL.N.Kanal,eds.,Parallel go rithms for Machine Intelligenceand Vision.Springer-Verlag,New York,pp.42-65.   
Pradhan,D. K.1985. Fault-tolerant multiprocessor link and bus network architectures. IEEE Traaciosonutersol.C34,.1,5.   
Preparata,F.P.1978.New paralel sorting schemes. IEEE Transactions on Computers, vol. C-27,no.7Julypp.66   
Preparata,F.P.,and J. Vuillemin.1981. The cube-connected cycles: A versatile network for parallelomtation.mmicationsof thel.24,o.5,ay 309.   
Price,C. C.1982. A VLSI algorithmfor shortest path through a directed acyclic graph. CongressusNumerantium,vol.34,pp.671.   
Price,C. C. 1983. Task assignment using a VLSI shortest path algorithm.Tech. rept., Dept.ofComuteriece,epenF.usintate Uesityacodo   
Prim,R. C.1957. Shortest connection networksand some generalizations.Bell System Technical Journal,vol.36,pp.1389-1401.   
Quinn,M.J.983.hedesignandanalysisofalgorithmsanddatastructuresforteef ficient solution of graph theoreticproblems on MIMDcomputers.Ph.D.dissrtation, Computer Science Dept.,Washington State University,Pullman.   
Quinn.J98talelgteeb problem. BIT, vol. 25, pp. 473-476.   
Quinn,M.J.1988. Parallel sorting algorithms for tightly coupled multiprocessors. Parallel Computing,vol.6,pp.34957.   
Quinn,M. J.1989. Analysis and benchmarking of two paralel sorting algorithms: hyperquicksortandquickmerge.BIT,vol.29,pp.29250.   
Quinn,M.J.1990.Analysis and implementation of branch-and-boundalgorithms on a hypercubemicouter.Eacioonputersl.C9 pp. 384-387.   
Quinn,M.JandN.Deo.1984.Paalelgraphalgorithms.ComputingSurveysol.1, no. 3, Sept., pp. 319-348.   
Quinn,M.J.,andN.Deo.1986.An upper bound for the speedup of paralel best-bound branch-and-boundalgorithms.B,vol.26,no.1,ar.,p.   
Quinn,M. J.andP.J.Hatcher.1990.Dataparalelprogammingonmulticomputers. IEEE Software,vol.7, no.5, Sept.,pp.69-76.   
Quinn,M.J.andY.B.oo984.Datatruuresfortheeientsouionof gah theoretic problems on tightly-coupled MIMDcomputers.In Proceedings of the 1984 Internatielsi 438.   
Quinn,M. J.,P.J.Hatcher,andK. C.Jourdenais.1988. Compiling $\mathbf { C } ^ { * }$ programs for ahypercube multicomputer.In Proceedings of the ACM/SIGPLAN PPEALS 1988 Parallel rogramming:Experience withpplications,anguages,andystems PLAN Notices vol.23, no.9,Sept.,pp.57-65.   
Radicati di Brozolo, G.,and Y.Robert. 1989.Parallel conjugate gradient-like algorithms for solving sparse nonsymmetric linear systems on a vector multiprocessor. Parallel Computing, vol. 11, pp.223-239.   
Raghavendra,C.S.,and V.K.Prasanna Kumar.1986.IEEE Transactions on Computers, vol. C-35, no. 7, July, pp. 662-669.   
Rajasekaran, S., and J. H. Reif. 1989. Optimal and sublogarithmic time randomized parallel sorting algorithms. SIAM Journal on Computing, vol.18, June,pp. 594 607.   
Ramakrishnan, I. V.,and P.J. Varman.1984. Modular matrix multiplication on a liear array.IEEE Transactions on Computers,vol. C-33,no.11,Nov., pp. 952-958.   
Ramamoorthy, C. V., and L.-C. Chang. 1971. System segmentation for the parallel diagnosis of computers.EEE ransactions onComputers,vol. C-20no.2b., pp. 153-161.   
Ramamoorthy,C.V.,J.L.Turner,and B.W.Wah.1978.A design of a fast cellular associative memory for ordered retrieval. IEEE Transactions on Computers,vol. C-27, no. 9, Sept., pp.800-815.   
Raskin,L. 1978. Performance evaluation of multiple processor systems. Ph.D. dissertation, Carnegie-ellonUversity,ittsburgh,.   
Reale,F.199o. A tridiagonal solver for massively parallel computer systems. Paralel Computing,no.16, pp.361-368.   
Reddaway,S.F.1979.The DAP approach. InC.R. Jesshope andR.W. Hockney, eds.,Int England, pp. 311-329.   
Redinbo,G.R.1979.Finitefieldarithmeticonanarrayprocessor.IEEETransactions on Computers,vol.C-8,no.7,Julypp.46.   
Reed,D.A.,L. M.Adams,and M.L. Patrick.1987.Stencilsand problem partitionings: Their influence on the performanceof multiple processor systems.IEEE Transactions on Computers,vol.C-36,no.7,Julypp.848.   
Reed,D.AndR..uimoto.987.uicomputer Networks:sgeaed Parallel Processing.ress,mbidge.   
Reed,D.A.,andD.C.Grunwald.1987.The performanceof multicomputer intercon nection networks. Computer, June, pp. 63-73.   
Reed,D.A..trick95.allatieluioofsse: Modelsandarchitectures.ParallelComputing,vol.2,p.4567.   
Reghbati,E.andD.G.Cormeil.1978.Paralel computations ingraph theoryA Journaloningol.2..   
Reif,J.H.98rictaorodne4l Symposiumoryotineorky14   
Reif,J.98t vol. 20, pp. 229-234.   
Reif,J. H.,and P. Spirakis. 1982. The expected time complexity of parallel graph and digraph algorithms. Tech.rept. TR-11-82,Aiken Computation Laboratory, Harvard University,Cambridge.   
Reif,J. H.,and L. G. Valiant.1987. A logarithmic time sort for linear size networks. JournaloftheACol.4o.1an.,6.   
Reingold,E.M.,J.Nievergelt,andN.Deo.977.CombinatorialAlgorithms:eory andPractice.icall   
Reischuk; R. 1981. A fast probabilistic parallel sorting algorithm. In Proceedings of the22d Annual IEEE Symposium on Foundations ofComputer Science,IEEE,New York, Oct., pp.212-219.   
Ribbens, C.J.1989. A fast adaptive grid scheme for elliptic partial diffrential equations.ACasactionson themicalotwareol.5,ept,p.79197.   
Ritchie,D. M.,and D. Thompson. 1974. The UNIX timesharing system. Communications oftheol.17o.7uly675.   
Robert,Y.,and D. Trystram. 1988. Comments on scheduling parallel iterative methods onmultiprocessorsems.rallelomputingl.75.   
Robinson, J. T.1977.Analysis of asynchronous multiprocessor algorithms with applications to sorting.In Proceedings of the 1977 International Conference on Parallel Processing,IEEE,New York,Aug.,pp.128135.   
Robinson, J. T.1979. Some analysis techniques for asynchronous multiprocessor algorithms.IEEcreein5Ja   
Rodeheffer, T. L.,and P. G. Hibbard. 1980. Automatic exploitation of parallelism on a homogeneous asynchronous multiprocessor. In Proceedings of the 1980 InternationalCoeenlleocinEEk   
Romine, C. H.,and J. M. Ortega. 1988. Paralel solution of triangular systems of equations.ParalelComputing,vol.6,pp.14.   
Rosenberg,A.L.1979.Preserving proximity in arrays.SIAM Journalon Computing, pp. 443-460.   
Rosenfeld,A. 1985. The prism machine: An alternative to the pyramid. Jourmal of Parallelandstribueduingo.2o4ov.,.   
Rosenkrantz,D.,R.StearsandP.Lewis.1974.Approximatealgorithmforthetael ingsalespersonproblem.InProceedingsofthe15thAnnualSymposiumonSwitching and AutomtaryEEE,ew York,ct.,.   
Rotem, D.,N.,Santoro,and J. B.Sidney.1983.Distributed sorting.Tech.rept.SC-TR-#34 Dec.,choolofomputerience,Carleton UniversityOtowatrio   
Roussel,P.975.OG:ueldereferenceetdutilsationGoupeItelligence Artificielle,Uveritedi-reille,umyc   
Rudolph,L.1984.A robust sorting network.In Proceedings of the 1984 Conference on AdvancedResearchinV.Press,Cambridge,Jan.,p.6-33.   
Ruzzo,W.,and L. Snyder.1981. Minimum edge length planar embeddings of trees. In H.T.KngB.roullndG.ees.VSytend Springer-Verlag, New York, pp. 119-123.   
Saad,Y.dM.H.ultz988.ologicalprortieoferubs.Eans actions on Computers,vol.C-37, no.7,July, pp.867-872.   
Saad; Y.,and M. H. Schultz.1989.Data communication in paralelarchitectures.Parallel Computing,vol. 11, pp. 131-150.   
Sadayappan,P.,and F.Ercal. i987. Nearest-neighbor mapping of finite element graphs onto processor meshes.IEEE Transactionson Computers,vol.C-36,no.12ec, pp. 1408-1424.   
Sadayappan,P.,.rcalndJ.Ramanujam.1990.Custer partitioningapproaches to mapping parallel programs onto a hypercube.Parallel Computing,vol. i3, pp.1-16.   
Sahni, S. 1984. Scheduling multipipeline and multiprocessor computers. IEEE Transactions on Computers,C-33,no.7,July,pp.637--645.   
Saltz, J. H., and M. C. Chen. 1987. Automated problem mapping: 1ne Crystal runtime system. In M. T. Heath, ed., Hypercube Multiprocessors 1987, SAM Press, Philadelphia, pp. 130-140.   
Samatham, M. R., and D. K. Pradhan. 1989. The De Bruijn multiprocessor network: A versatile parallel processing and sorting network for VLSI. IEEE Transactions on Computesl.,.4Ar.,1   
Samathan, M. R.,and D. K. Pradhan. 1991. (Correction) The De Bruijn multiprocessor network: A versatile parallel processing and sorting network for VLSI. IEEE Transactions onomputers,vol.-4,no.1,Jan.,p.1.   
Sameh,A. 1977. Numerical parallel algorithms-A survey.In D.Kuck,D. Lawrie, and A. Sameh, eds.High Speed Computer and Algorithm Organization,Academic Press,Orlando,FL,pp.28.   
Sameh,A.,and D.Kuck. 1978. On stable parallel linear system solvers. Journal of the ACM, vol. 25,no.1, pp.81-91.   
Sang,F. C.,and I. H. Sudborough. 1990. Embedding large meshes into smallones. In Proceedings of the IEEE Symposium on Circuits and Systems.   
Satyanarayanan, M. 198o. Multiprocessing: An annotated bibliography. Computer, vol. 13, no. 5, May, pp. 101-116.   
Savage,C.1977.Paralelalgorithmsfor graph theoretic problems.Ph.D.dissertation, University of Illinois,Urbana.   
Savage,C.1981.Asstolicdatastructurechipforoectivityproblems.InH.TKung, R.F.SprollG.er.i Science Press,Rockville,.   
Savage,C.,and J.JaJa.1981.Fast,eficient parallelalgorithms forsome graph problems.SIAMJournal onComputing,vol.10,no.4,ov.,.682690   
Savage,J.E.1981.Planar circuit complexityand the performanceof VLSIalgorithms. InH.T.KungR.F.oullnG..teele,Jr.s.semd tations,Comuter ience res,ockville,,.666.   
Schaefer,D.HandJ..sher.982.Beyondthesupercomputer.IEEESetrum vol. 19, no.3,Mar., pp. 32-37.   
SchaeferJ98edrlld Computing,vol.6, pp.90114.   
SchendelU8rioticalosraellis Horwood, Chichester, England.   
Schieber, B. S.,and U. Vishkin.1988.On finding lowest common ancestors:Simplificationandpralelzation.AJournalonomputingvol.17no6e pp. 1253-1262.   
Schroder,H.983.artitionortsfor.normatikFachberichteo. 116.   
Schwartz,J.T.1980.Ultracomputers.ACM Transactions on Programming Languages and Systems vol. 2, no.4, pp. 484-521.   
Scott,D.S.,and J.Brandenburg.1988.Minimal mesh embeddings in binary hypercubes. IEEE Tracionsonomuters,vol.C7no.1Oct.,.84.   
Sedgewick,.988.goritms.2ded.disoWeseyeading   
Seitz,C.L pp. 22-33.   
Shapiro,E.Y.1983a.The fifth generation project-A tripreport.Communications of the ACM,vol.26,no.9,Sept.,pp.67641. go5u. Aigorunmic rrogram Debugging. Mi1 Press, Camoridge.   
Shapiro,E.Y.1983c.The Bagel: A systolic Concurrent Prolog machine (lecture notes). WeizmannIteet   
ShapiroE.Y1985.Systolicprogramming:Aparadigmof parallel procesing.Tech. rept.C846steee   
Shapirote Aug., pp. 44--58.   
Shaw,A.C.974.heLgicaleignofOperatingstems.renticeHallEngleod Cliffs, NJ.   
Shiloach, Y.,and Vishkin, U. 1981. Finding the maximum,merging and sorting in a paralelotaioel.algol..r..   
Shiloach, Y.,and U. Vishkin.1982a. An O(logn) parallelconnectivity algorithm.Journal ofAlgorithms,vol.,no.1,ar.,pp.6.   
Shiloach,Y.andU.Vishkin.1982b.An $O ( n ^ { 2 } \log { n } )$ parallel MAX-FLOW algorithm. Journal ofAlgorithms,vol.3,no.2,June,pp.12146.   
Sheu,J.-P.,N.-L.KuoandG.-H.Chen.1990.Grahsearchalgorithmsandmaimum bipartitematchingalgorithmonthehypercubenetworkmodel.ParalelComputing, vol. 13, pp. 245-251.   
Shroder,H.983.Partitionsortsfor VSI.Informatik Fachberichte,vol.73,.101 116.   
Shyu,C.-H.199o.A parallel algorithm for finding a maximum weight clique of an interval graph.Paralel Computing,vol.13,pp.253-256.   
Siegel,H.J.1977.Theuniversalityofvarious types of SIMDmachine interconnection networks.In Proceedingsof the4thAnnual International SymposiumonComputer Architecture,IEEE,New York,Mar.,pp.70-79.   
Siegel, H. J.1979a. Interconnection networks for SIMD machines.Computer, vol.12, no. 6, June, pp. 57-65.   
Siegel,H.J.1979b.A model of SIMD machines and acomparison of various interconnection networks. IEEE Transactions on Computers,vol. C-28,no. 12, Dec., pp. 907-917.   
Siegel,H.J.1985.InterconnectionNetworksforLarge-Scale ParallelProcessing:The ory and Case Studies.Lexington Books,Lexington,A.   
Simmen,M.1991. Comments on broadcast algorithms for two-dimensional grids. Parallel Computing,vol.17, pp.19112.   
Simons,B.B.,and M. K.Warmuth.1989.A fast algorithm for multiprocessor scheduling of unit-length jobs. SIAM Journal on Computing,vol. 18,Aug.,pp. 690-710.   
Singh,V.,V.Kumar,G.Agha,andC.omlinson.1991.Efcientalgorithmsforparallel sorting on mesh multicomputers.International Journal of Parallel Programming, vol. 20, no. 2, pp. 95-131.   
Singhal, M.989.eadlock etectionin distributed systems. Computer,Nov.,p.37 48.   
Skillcorn,D.B.1988.A taxonomy for computer architectures. Computer,Nov.,pp.46 57.   
Slagle,J. R.,and J. K. Dixon. 1969.Experiments with some programs that search game trees. Journal of the ACM, vol. 16, no. 2, Apr., pp. 189-207.   
Smith, B. J. 1978.A pipelined shared resource MIMD computer. In Proceedings of the1978IeialereoallelosingEE pp.6-8.   
Smith, J. 1986. Parallel algorithms for depth-frst searches I: Planar graphs. SIAM Journal on Computing,vol.15, no.3, pp.14-30.   
Snir,M.1985.Onparallel searching.SAMJournal onComputing,vol.14,no.3,Aug., pp. 688-708.   
Sollin, M.1977. Analgorithm atributed to Sollin. In S. E. Goodman and S. T. Hedetniemi，eds. Introduction to the Design and Analysis of Algorithms, McGraw-Hill, New York, sec. 5.5.   
Sridhar,M.A.1988.On the connectivity of the De Bruijn graph. Information Processing Letters,vol. 27,pp.315318.   
Stenstrom,P.1988. Reducing contention in shared-memory multiprocessors. Computer, Nov., pp. 26-37.   
Stenstrom,P.99o.A survey ofcache coherence schemes for multiprocessors.Computer, June, pp. 12--24.   
Stewart,G.W.973.Introductionto atrix Computations.Academic Press,New York.   
Stockman,G.1979.Aminimaxalgorithmeterthanalpha-beta?Artificial Intelligence, vol. 12, pp. 179-196.   
Stone,H.S.1971.Parallel processing withtheperfect shufle.IEEE Tansactions on Computers, vol. C-20, no. 2, Feb., pp. 153-161.   
Stone,H.S.973.Problemsof paalelcomputation.InJ.F.Traub,ed.,Complexityof Sequentialli 16.   
Stone,H.S.1978.Sorting with STAR.IEEE Transactions onSoftware Enginering, vol. SE-4, no. 2, Feb., pp. 138-146.   
Stone,H.S.198o.Parallel computers.InH.S.Stoneed.,Introduction toComuter Architecture,ieeesearch soates,ago.8   
Stout,Q.F.1983a. Sorting,merging,selecting and filtering on tree and pyramid machines.InProcedingsofthe198InteaionalConferenceonaralelrocsing IEEE, New York,Aug.,p.21221.   
Stout,Q.F.983b.Mesh-connected computers withbroadcasting.IEEETransactions on Computers,vol. C-32,no.9,Sept.,pp.8630.   
Stout,Q.F.1985a.Pyramidcomputersolutionsoftheclosestpair problem.Journalof Algorithms,vol.6,pp.012.   
Stout,Q.F.1985b. Tree-based graph algorithms for some parallel computers (prelim. ver.).InProcingofe985IteatonalCoferenceonarallelPg IEEE,New York,Aug.,pp.727-730.   
Stumm,M.,andS.Zhou.1990. Algorithms implementingdistributed shared mmory. Computer,ay,pp.5464.   
Sun,X.-H, Zhang,H.,and L. M. Ni. 1992. Efficient tridiagonal solvers on multicom puters.EEces..   
Swan,R.J.,A.Bechtolsheim,K.-W.Lai,and J. K. Ousterhout.1977. Theimplementation of theCm\* multi-microprocessr.In Proceedings of the National Computer Conference.rsn655.   
Swarztrauber,P.N.987.ultiprocessorFs.ParalelComputing,vol.5,9 210.   
Tabak,D.99rssticall.   
Tanaka, H. 1986. A parallel inference machine. Computer,Aug., pp.48-54. penne searcing and sorung oduies as components of a data flow database computer. In Proceedings IFIP Congress: Informationossn..   
Tanimoto,S.L.1981. Towards hierarchical celular logic:Design considerations for pyramid machines.Tech.rept.8-201,Dep.ofComputer Science,Unvesityof Washington, ttle.   
Tanimoto, S. L. 1982a. Sorting, histogramming,and other statistical operations on a pyramid machine.ech.rept8-02,Dept.ofComputer iene,Ueityof Washington, ttle.   
Tanimoto,S.L.1982b.Programming techniques for hierarchical paralel image procesors.In K.PrestonandL.Uhreds.Multicomputers and Image ProcesingAlgo rithmsandPrograms.AcademicPressNew York,pp.4429.   
TanimotoS.L.ndA.inger.98O.tructuredComputerVision:chineection through HierarccalomutationrcturesAdeicrss,ok.   
Tantawi, A.N.,andD.Towsley.1985. Optimal load balancing in distributed computer systems.Journal of theACM,vol.32, no.2,pp.445-465.   
Tarjan,R. E.and U. Vishkin.1984.Finding biconnectedcomponentsand computing treefunctions inlogarithmicparallel time (extended summary). InProcedingsof the 25thAnnual SymposiumonFoundationsofComputerScience.IEEEPrep.12 20.   
Tarjan,R.E.,and U.Vishkin.1985. Anefficient parallelbiconnectivity algorithm. SIAM Journal of Computing, vol. 14, pp. 862-874.   
Taylor,S.,.fraandE.apio.987.AralllimemtationofatCot Prolog.InternationalJournalofralelProgramming,vol.5,no.3,pp.245275.   
Teller,P.J.99.aslaio-looasdeferoisency.omputerJune,p.66.   
Thakar,S.,.ubois,A..LaundrieandG..Sohi99.Scalablesharedr multiprocessor architectures.Computer,June, pp.71-73.   
Thinking Machines Corporation.1989.Connection Machine CM-200 Series Technical Summary. Cambridge,MA.   
Thinking Machines Corporation. 1991. $C ^ { * }$ Programming Guide. Version 6.0.2,Cambridge,MA.   
Thomasian, A.,and P. F. Bay. 1986. Analytic queueing network models for parallel processing of task systems.IEEE Transactions on Computers, vol. C-35, no.12, Dec., pp. 1045-1054.   
Thompson, C.D.1979. Area-time complexity of VLSI. In Proceedings of the 11th Annual ACSymposiumoneory ofomputing,ACM,New York,ay,p. 88.   
Thompson, C. D. 1980. A complexity theory for VLS1. Ph.D. dissertation, Dept. of Computerience,regie-ellonversityitsurgh,   
Thompson,C.D.983a.ourier transforms inI.IEEETransactionsonComputers vol. C-32, no. 11, Nov., pp. 1047-1057.   
Thompson,C.D.1983b. The VLSIcomplexity of sorting. IEEE Transactions on Computers, vol. C-32, no.12, Dec., pp. 1171-1184.   
Thompson, C. D.,and H. T. Kung. 1977. Sorting on a mesh-connected parallel computer.Communications of the ACM,vol.20,no.4,Apr.,pp.263-271.   
Thurber,K.J.1976.Large Scale Computer Architecture-Parallel and Associative Processors. Hayden Book Co., Hasbrouck Heights,NJ. muruer Tarancr processorarcntccturcs 1113 Computer esign,Jan.,pp.89-97.   
Thurber,K.J.1979b.Parallel processor architectures-Part II: Special purpose systems. Computer Design,Feb., pp.103-114.   
Tick,E.1991.Parallel Logic Programming.MIT Press,Cambridge.   
Tiwari,P.1986.An efficient parallel algorithm for shifting the root of a depth frst spanning tree.Journal ofAlgorithms,vol.7,pp.105-119.   
Todd,S.1978.Algorithms and hardware for a merge sort using multiple processors. IBMJouralerchdveloentol.22o.5,.7.   
Tolub,S.andY.Wallach.1978.Soring onanM-tyeparallel procesingstem. Euromicro Journal,vol.4,pp.161.   
Towsley,D.1986.Approximate models of multiple bus multiprocessor systems.IEEE Transactions onomputersvol.C35,no.3,ar.,pp.228.   
Troya,J.M.andM.rtega.989.Astudyof parallelbranchandboundalgor with best-bound-first search. Paralel Computing,vol.11,pp.121-126.   
Tseng,S. S.,andR. C. T.Lee.1984a.A new paralel sorting algorithm based upon min-mid-max operations. BIT,vol. 24, pp.187-195.   
Tseng,S.S.andR.C.T.Lee.1984b.Aparallelalgorithm tosolvethestablemariage problem. BIT,vol. 24,pp.308-316.   
Tsin,Y.H.986.Findinglowestcommonancestorsinparalel.IEEETransactionson Computers,vol.C-35,no.8,Aug.,pp.764769.   
Tsin,Y. H.andF.Y.Chin.984.Eficient paralelalgorithms foraclassof graph theoreticproblems.AMJournalonComputingvol.13Aug.,.99.   
Tucker,A.B.1988.ComputerScience:A Second Course Using Modula-2.McGraw-Hill, New York.   
Uhr,L. 1972. Layered “recognition cone” networks that preprocess, classify,and describe.IEEies.7ul   
Uhr,L.198gottrcurdomuterdtwosdes Orlando, FL.   
Uliman,J.D.1975.N-completescheduling problems.Journalof Computerand System Sciences vol.10,pp.8493.   
Ullman,l MD.   
Uliman, J. D.,andM. Yannakakis.1991. High-probability parallel transitive-closure algorithms.Ali.1..   
Ullman,S.,and B.Narahiri.199o.Mapping binary precedence trees into hypercubes and meshes.In Proceedings of the Second IEEE Symposium on Parallel and Distributed Processing, pp. 838-841.   
Upfal,E.1984.A probabilistic relationbetween desirable and feasible models of parallel computation.In Proceedings of the16th Annual ACM Symposium on Theory of Computing, pp. 258-265.   
Upfal,E.,and A.Wigderson.1987. How to share memory in a distributed system. Journalof theAC,vol.34,no.1,Jan.,pp.6.   
Uresin,A.andM.ubois.99o.Paralelasynchronousalgorithms forisreteata. Journal of the ACM,vol.37,no.3,July,pp.588-606.   
U.S.Department of Defense.1981. Programming language Ada: Reference Manual, vol.i06,Lecture Notes in Computer Science.Springer-Verlag,New York.   
vanant,L.G.19/5. Paralelism incomparson problems. SAM Journal on Computing, vol. 4, Sept., pp.348-355.   
Valiant,L.G.1981.Universalityconsiderationsin VLSIcircuits.IEEETransactions on Computers,vol. C-30,no.2,Feb.,pp.5140.   
Valiant,L.G990.Abrdgingmodelforaralelcomputation.Communicationsofthe ACM,vol.33, no.8,Aug.,pp.10111.   
van der Vorst, H.A.1987a.Large tridiagonal andblock tridiagonal linearsystems on vector and paralelcomputers. Paralel Computingvol.5,pp.454.   
vander Vorst,H.A.1987b.Analysisofaparalelsolution methodfortridiagonal linar systems.Parallel Computing,vol. 5, pp. 303-311.   
van Scoy,F.L.1976.Parallel algorithms incellular spaces.Ph.D.dissertation,School ofEngineeringandApplied Science,Universityof Virginia,Charloteille.   
van Scoy,F.L.1980.The parallel recognition of classes of graphs.IEEE Transactions on Computers,vol.C-29,no.7,July,pp.5670.   
van Voorhis,D.C.971.Onsorting networks.Ph.D.dissrtation,Stanford University Stanford, .   
van Wijngaarden, A., B. J. Mailloux,J. L. Peck, C. H. A. Koster, M. Sintzoff, C. H. Lindsey, L. G. L. T. Meertens,and R. G. Fisker. 1975. Revised report on the algorithm language ALGOL68. Acta Informatica, vol. 5, nos. 1-3, pp. 1-236.   
Varman,P.J.,and K.Doshi.1992.Sorting with linear speedup ona pipelined hypercube. IEEE Transactionsonomutersol.C41no.1,an.,9   
Vazirani, U.,and V.Vazirani.1985.The two-processorscheduling problemis inRNC. InProceedingsofthe 17thAnnualACMSymposiumon Theory ofComputing,pp.11- 21.   
Vazirani, U.V.,and V.V. Vazirani.1985.The two-processor scheduling problem is in random NC. SAM Journal on Computing,vol. 18, no. 6, Dec.,pp.1i40-1148.   
Vishkin, U.1983.Implementation of simultaneousmemory access inmodels that forbid it. Journal ofAlgorithms,vol. 4, no.1, Mar.,pp.45--50.   
Vishkin,U.,and A.Wigderson, Inpress.Trade-offs between widthand depth inparallel computation. SIAM Journal on Computing.   
Vitanyi, P. M. B.988.Localitycommunication,and interconnect length inmulticomputers.SAJournal onCompuingvol.17,no.4Aug.,.659672.   
Vrsalovic,D.,E.F.Gehringer,Z.Z.SegallandD.P.Siewiorek.1985.The influence of parallel decomposition strategies on the performance of multiprocessor systems. In Proceedings of the 12th Annual International Symposium on Computer Architecture, ACM SIGARCH Newsletter,no. 13, June, pp. 396-405.   
Vuillemin, J.E.1983.A combinatorial limit to the computing power of VLSI circuits. IEEE Transactions on Computers,vol.C-32, no.3,Mar.,pp.294-00.   
Wah,B. W.,and K.L.Chen.1984. A partitioning approach to the design of selection networks.IEEE Transactions on Computers,vol. C-33,no.3,Mar.,pp. 261-268.   
Wah,B. W., and Y. W. Eva Ma. 1984. MANIP-A multicomputer architecture for solving combinatorial extremum-search problems. IEEE Transactions on Computers, vol. C-33, no.5,May, pp.377-390.   
Wah, B. W., G.-J.,Li, and C. F. Yu. 1984. The status of MANIP-A multicomputer architecture for solving combinatorial extremum-search problems. In Proceedings of the l1th Annual International Symposiumon Computer Architecture, IEEE,New York,Mar., pp. 56-63.   
Wah,B. W., G.LiandC.-F.Yu.1985. Multiprocessing of combinatorial searchprob lems.Comteo.oe,   
Wah,B.W.,GdC.uurosnr lems.InV.L.l.le forMachneIellgencedVisonrgeeagwork145.   
Wah,B.W.andE.Y.W.a.984.ANI-multicomputerarchitectureforsolving combinatorial extremumsearch problems.IEEETransactions onComputers,vol.C 33,no.5,May,pp.37790.   
Wah,B.W.,andC.F.Yu.1982.Probabilistic modelingof branch-and-bound alg rithms.ProceedingsofCOC,Nov.,p.647-653.   
Warren,D.H.D.,L.M.ereiraandF.ereira.1977.OG—helangugead its implemeatiedithP.oticesl.2oi SIGARTNewsletter64(August1977),p.1115.   
Warshall,Sl Jan., pp. 11-12.   
Watson,I.ndJ.urd91.acticalataoouter.teo.o2 Feb., pp. 51-57.   
Wagner,A.,andD.G.Corneil.1990.Embedding trees inahypercube isN-complete. SIAMJouraluinol.9.4e,   
Weaver,H.J.1983.Applications of Discreteand Continuous Fourier Analysis.John Wiley& Sons,New York.   
Wegner,L.M.1982.Sortingadistributed file inanetwork.InProceedingsofthe1982 ConferenceonfoationieceSemsar.0   
Weide,B.W.1981.Analyticalmodels toexplainanomalous behaviorof paralelalgo rithms.In Proceedings ofthe 198l International Conferenceon Parallel Processing, Aug., IEEE,New York,pp.183-187.   
Wheat,M.,and D. J. Evans.1992.Anefficient parallel sorting algorithm for shared memorymuliocssrsralleluingol8.   
Wilson,G.V.993.Aglossaryofparallelomputing terminologyIEEEParallel& Distributedhnologyemndicionsol.o.1eb.,   
Winslow,L.E.,andY.-C.Chow.1981.Paralelsorting machines: Their speedandefciency.In Proceedings of theAFIPS1981National Computer Conference,pp.163 165.   
Winslow,L.E.,and Y.-C.Chow.1983. The analysis and design of some new sorting machines.IEEE Transactions on Computers,vol.C-32,no.7,July,pp.677-683.   
Wirth,N.96.gorithmsatatructures=Progams.reiceall,nleo Cliffs, NJ.   
Wirth,N.1977a.Modula:Alanguagefor modular multiprogramming.Software Practice andExperieeol.7.   
Wirth,N.9eeofula.oftwareacicedxpienceol. 65.   
Wirth,N.1977c.Designand implementation of Modula.Software Practice and Experience,vol. 7, pp.67-84.   
Wold,E.H.,and A.M.Despain.1984.Pipelineand paralel-pipeline FFT processors for VLSI imlemetatios.EEctiosonomputersl.33,oy pp. 414-426.   
Wolfe,M.J.989.Optimizingupercompilersforupercomputers.PitmanPubliing, Long,England,and  Press,Cambrdge.   
Wolstanl, Y. 198y. Mapping parallel programs to multicomputers: a dynamic approach. Parallelngl.   
Wong,C.K.,and S.-K.Chang.1974.Paralel generation of binarysearch trees.IEEE Transactionsonoutersol.-3o.,r.,..   
Wong,F.S.,and M. R. Ito. 1984. Parallel sorting on a re-circulating systolic sorter. TheComrl..   
Wu,A.Y85ingofeotobsoualfad Distributed Computing,vol.2,pp.-49.   
Wu,C.L.,and T. Y. Feng.1981. Universality of the shufle exchange network. IEEE Transactioe..5   
Wulf,W.A.,R.vinadS..rison.981.H/C.mmp:AnExal Computerystem.c-Graw-Hill,ewrk.   
Wylie,J.C.979.Thecomplexityofprallelomputations.PhD.dissertationept. of Computer cience, Cornell University, Ithaca, N.   
Yadlin,Y.,andD.A Caughey,Block multigrid implicitsolution of the Euler equations of compressible fuid flow. AAA Journal,vol. 29,May,pp.712-719.   
Yang,C.-B.,R.C.T.Leeand W.-T.Chen.199o.Parael graphalgorithmsbasedupon broadcast communications. IEEE Transactions on Computers,vol. C-39,no. 12, Dec., pp. 1468-1472.   
Yang,M. C. K., J. S. Huang,and Y.-C. Chow. 1987. Optimal parallel sorting scheme by order statistics. SAMJournal on Computing, vol.16, no. 6,Dec., pp. 9901003.   
Yasuura,H.,N. Tagakiand S. Yajima.1982. The parallel enumeration sorting scheme for VLSI.EEETransactionsonComputers,vol.C-31,no.12ec.,p.19201.   
Yau,S.S.,and H. S.Fung.1977.Associative processor architecture—A survey.Computing Surveys,vol. 9, no. 1, Mar., pp. 3-27.   
Yoo,Y.B.1983. Parallel processing for some network optimization problems.Ph.D. dissertation, Computer Science Dept.,Washington State University,Pullman.   
Yu,C.F.,and B.W. Wah. 1983. Virtual-memory support for branch-and-bound algorithms.In Proceedings Compsac,Nov.,pp.618-626.   
Yu,C.F.,and B.W.Wah. 1984. Efficient branch-and-bound algorithms ona two-level memory hierarchy. In Proceedings Compsac, Nov., pp. 504-514.   
Yu,D.C.,and H. Wang.1990.A new parallelLU decomposition method. IEEE Transactions on Power Systems,vol.5,Feb., pp.303-310.   
Zhang,C. N.,and D. Y. Y. Yun.1984. Multi-dimensional systolic networks for discrete Fourier transform.In Proceedings of the Eleventh Annual International Symposium onComputer Architecture,GARCH Newsletter,pp.215-222.   
Zima,H.,and B.Chapman.199o.Supercompilers for Parallel and Vector Computers. ACM Press, New York.   
Znati, T.F., R.G. Melhem,and K. R. Pruhs.1991. Dilation based bidding schemes for dynamic load balancing on distributed processing systems.In The Sixth Distributed Memory Computing Conference Proceedings,pp.129-136.

5

5.85

←,31,123   
$\Leftarrow , 1 2 4$   
$\beta$ ,172   
λ,14,172   
$\sigma ( k )$ ,180   
x,14,172   
Activation steps,30   
Active garbage list,304   
Active operation,310,312   
Acyclic graph,368,376   
Adjacency lists,368   
Adjacencymatrix,367,76   
Alfonso X,255   
Algorithm: control-parallel (see Control parallelism) data-parallel (see Data parallelism) parallel see Multicomputer algorithms,Multiprocessoralgorithms,PRAMalgorithms, Processor array algorithms) sequential see Sequential algorithms)   
All-pairs shortest-path search,318-368,376   
Alpha-beta search,354-365,376 parallel, 359--365 sequential, 354-359   
ALT construct, occam, 116-117   
Alternation,116   
Amdahleffect,17,82,223,76   
Amdahl's law,17,-82,76   
Ametek,4   
Amplitude,200   
AMTDAP,54,86,213   
ANDtree,337-338,376   
AND/OR tree,337-338,365,376   
Anomalies,speedup,80-81,352-354,365   
ANSI, 95   
ARBITRARYPRAM,28,376   
Architecture: multicomputer (see Multicomputer architectures) multiprocess or (see Multiprocessor architectures) processor array (see Processor array architectures)   
Argumentsagainst high-level parallelism,19   
Array,processor (see Processorrray)   
Articulation points, 333   
Aspiration search,358-360,376   
Assembly line, 6   
Assignmntocesscm111   
Associative memory,18,307   
Associative processor, 334   
Astrophysics,2   
Asynchronous algorithm,159,253,376   
AVLtree,297-301,307,377   
$\mathbf { B } ^ { * }$ tree,307   
Back end,74,92   
Back substitution algorithm, 220-223   
Backtrack,339   
Balance,Sequent (see Sequent Balance)   
Balanced binary tree,138   
Banded linear system solvers,252   
Bandwidth,75,77 bisection,88,77   
Bank,191,308,377   
Barrier synchronization,91,104,125,377   
Batch search,294,307,377   
BBN: Butterfly Plus,365 TC2000,57,70-72,79,189,285   
Benchmarking practices,86   
Bennett,A.F., 3   
Biconnected components,33   
Binary $n$ cubenetwork,57,377 (see also Hypercube)   
Binary semaphore, 151   
Binary tree: compared to other networks,61 embedding in2-Dmesh,135-136 embeddinginhypercube,137-138 fundamental paradigm,31 graph defined,370,377 networkdefined,5455 reasonable model,86   
Binomial tree: defined,70, embedding in 2-D mesh,136-137 embedding in hypercube,138-139   
Biology,3   
Bipartite graph,138,333   
Bisection bndwidth,8,77   
Bisection width,53,25758,77   
BIT function85-186   
Bitrveral,   
BIT.COMPLEMENTfunction,185-186   
Bitonicmerge,260-272,290,377   
Bitonic sequence,260-265,377   
Bit-parallel arithmetic,5   
Bit-parallel memory,5   
BITS function,315   
Bit-serial processors,64   
Block matrix uliliction899, 196,377   
Block-oriented data distribution,193-196, 243-244   
Bolt,Beraneknd Newman,Inc.(se)   
Bound andbanch,63,77   
Branch and bound: anomalies,352-354 best-first search strategy,342 definition,40-342,77 eight-puzzleeamle,339-340 multicomputer implementation,347-352 multiprocessor implementation,346-347 references inliterature to,364-365 traveling salesperson example,342--346   
Breadtehlle   
Breadthel   
Brent'stherem,4446,14,77   
Broadcast:, r2-Dmesh, 176 conjugate gradient,249 defined,31,77 gaussian elimination withpartial pivoting,232,236 hypercube,170-171   
BSPmodel,49   
Buffer deadlock,151-152,377   
Burroughs Corporation,4   
Bus,common,68   
Busy-waiting,377   
Butterfly: compared with other networks,61 defined,57,377 fast Fourier transform,206 inBBN TC2000,70-71 reasonable model, 86   
Butterfly network (seeButerfly)

C:   
nCUBE,109-112   
Sequent,104-19   
C\*,99-103   
Cache:   
coherency,69,87   
copy-back policy,70   
memory,5,69-70,377   
.write-through policy,69-70   
California Institute of Technology，4,87,   
217   
Caltech (see California Instituteof Technol  
ogy)   
Cancellation lemma,373-374   
Cards,playing,20   
Carnegie-Mellon University,4,6-87   
Cell modeling,3   
Centralized load balancing algorithm,143,   
377   
Centralized shared memory, 67   
Chain,149,377   
Chaining,377   
Channel,5,114-15,78   
Checkers,354   
Cheriton and Tarjan’s minimum-cost span  
ning treealgorithm,333   
Chess,354,359-361,365   
Child,370,8   
Chordal graphs,334   
Chua,B.,3   
Circuit problem,218-219   
Circuit value problem,48   
Circuit-switchedmessagerouting7374,132   
Claim adjustorsaogy,58   
Classical science,2   
Classifying architectures,78-80   
Classifyinggorihs,9   
C-Linda,118-122   
Cm\*，4,87,190-191,346-347,359   
C.mmp,4,86   
cobegin...coend statement,149   
Coffman-Graamhedulinggoithm,46   
149   
Cole,R., 201   
Color cost problem,333   
Combinatorial sarch,666   
Combining messages,236   
Common bus,68   
COMMON PRAM,28,378   
Communicating sequential process   
Commicad   
Communicatio-computationtradeoff,6   
237,360   
Comparator,260-378   
Compare-exchange,260-263,378   
COMPARE-EXCHANGE,269   
Compileraleling128   
Completearyree78   
Componentbeingproblem,78   
Complexmer

Complexity,26,27,295,78   
Computational fluid dynamics,2   
Computational geometry255   
Computer: parallel (see Multicomputerarchitectures, Multiprocessorcitues, array architectures) sequential,26-27,62-63,74,385 vector,61,387   
Computing,high-speed,2   
Concurrent Pacal,06   
ConcurrentProlog,127   
Congestion,   
Conjugate gradient,248-251,253   
Connectedts89 378   
Connected graph,68, 378   
Connected sroblem,368,78   
Connection Machine (see Thinking Machines)   
Contemporary science,2   
Contention,   
Control parallelism: asynchronous algorithm,159 defined,8, pipelined algorithm,8 scalability,9 Sieve of Eratosthenes,9-13 when tochoose,159   
Convergenceteria8   
Convolutionalgorithm,203-204   
Copy-backcache,77   
Corinthians I,90   
Cosmic Cube,4,8   
Cosmology，2   
Cost,27,378   
Cost criteria,27   
Cost oal,4,   
Cray X/MP,4   
Cray Y/MP,5   
Cray-1,61,8   
CRCWPRAM:   
defined,, enumeration sort, 256-257 lower bounds on sorting,291   
CREWPRAM:   
comparedtoCRCWPRAM,256 connectedcomponents,313-315 defined,28,78 graph coloring,42-43 list rankingalgorithm,34-35   
merging lists,40-42 minimum-cost spanning tree, 333   
prefix sumsalgorithm,2-34   
preorder tree traversal, 36-40   
reduction, 159   
searchinga graph,309-313   
searchinga table,295   
Critical node,297,78   
Critical n,9i,6,,,   
Crossbar switch,68   
Cube-connected cycles:   
basis for processor arrays,63   
compared with other networks,61 defined, 58--59,379 reasonable model,6 sortingalgorithm,290   
Cube-connected network (see Hypercube)   
Cubical,7   
Cyber-205,61   
Cycle: condition of deadlock,152 graph theoretic definition,68,379   
Cyclicrei   
DAP (see AMT DAP)   
Data flow analysis,379   
Data flow computing,87   
Data flow diagram (see Data flow graph)   
Datafowga29 379   
Data flow language,128   
Data parallelism: becomes SPMD on MIMD machines,169 contrasted with pipelining,7-8 defined, 6,79 indicated by forall statement,124 prescheduling versus self-scheduling,158 Sieveoftothees218   
Data pipelining,5   
Data stream,78,379   
Data-parallel algorithm (see Data parallelism)   
DataVault,67   
de Bruijn network,60-61,85-86,379   
Deadlock,151-152,154,379   
Decisionproblem,37379   
Deepness heuristic,342   
Dense linear systemovers229-237,252   
Depth,149,379   
Depth-irsthallel,433   
Deque,325,379   
Design strategies, paralel (see Parael algorithm design strategies)   
Determincel,   
DFT,201,379 (See also Discrete Fourier transform)   
Diagonallyttri   
Diameter,53,379   
Dictionary operations,294-308   
Digitized picture input,68   
Dilation,13,79   
Direct-Connect odule,C/2774   
Directed gaph,367,79   
DiscreteFuriertrasorm9873,379   
Discretizion teil,   
Distributedload balancing algorithms,143   
Distributed memory: $\mathbf { C } ^ { * }$ programming model, multicos,,4 PRAMel, processor arrays,62,131 pseudocode variables,122   
Distributedsared memory,67,70,87   
Distributed sorting,292   
Distributed Tree Search,361-365   
Divide and conquer: combinatorial search,338

defined, 379 fast Fourier transform,206 picomputation,119,121-122 quicksort, 273 represented by binary tree,31 DMA,73,75 Double rotation of AVL tree, 298 DTS (see Distributed Tree Search) Dynamicdecomposition,379 Dynamicload balancing,multicomputer,142 143 Dynamic programming, 365 Dynamic scheduling,380 east keyword,edoce5 Edge,367,380 Effective branching factor358380 Efficiency，08 scaled,8-84 8-puzzle,339-341 Einstein,A.,217 Elementarypralelalgorithms,57-177 Ellis'sagorithm297-301 Embedding,133-142,380 2-D meshinto2-D mesh,134-135 binomial treeinto2-Dmesh,136-137 binomial treeintoercube8139 completebinary treeinto2-Dmesh15 136 complete binary tree into hypercube,137- 138 defined,1 graphs into hypercubes,137-138 grids into hypercubes,153 ring into 2-Dmesh,134 ringsandmeshesinto hypercube,139- 142 Encore Multimax,68 Enumerationsort,256-25791,80 Environmental modeling,3 Enzyme activity,3 EREWPRAM,28,333,380 eval fuctio,ida2 Evaluation function,354 Even-odd exhange,58,80 Exchange,380 exchangeord,oe Exhaustive search,339 Expected space and time complexity26, 380 Extel igall Fact,380 Fan-in,31,249,252,80 Fast Fouriertrasform205213,380 iterativealgorithm,208-209 parallelalgorithm,207-213 recursive algorithm,207 Fetch-and-add,56 FFT (see Fast Fourier transform) 15-puzzle,339 Fifth-generationcomputer380 Filter,low-s,4216 FIND,326-328 First order recurrence relations52

Flat Concurrent Prolog,129   
FlatGHC,129   
Flynn's toomy0   
forallstatetoe   
forsatement   
Fork,380   
FORTRAN77,93,95   
Fortran90,95-99   
Forward substitution,253   
Fourier analysis,198,380   
Framebuffer,64-67   
Frequecyl,9   
From,367,380   
Frontend: multicomputer,91-93,380 processor array,62-64,380   
Fully distributed load balancing algorithm, 143,380   
Functional units: multiple,18 pipelined, 5   
Gadzooks hypercube multicomputer, 177   
Gametree: defined,354, pathological 365 perfectly ordered,361 searching,354-359   
Gantt chrt,45,8   
Garbage colection04   
Garbage list,304   
Gaussian elimination,229-237,80 with partial pivoting,230-237,380   
Gauss-eidel goithm,44245   
Genetic engineering,3   
Genome sequencing,3   
Gigabyte,380   
Gigaflops,380   
Globalkeyord,sde   
Global memory (see Shared memory)   
Global ocean circulation,3   
Global weather modeling,3   
Go,354   
Goodyear Aerospace Massively Parallel Processor,54,86   
Graham's list'scheduling algorithm,145- .146   
Grain size,188,236,80   
Grand challenge problems,2   
Graph,367,381   
Graph algorithms: all-pairs shortest path,318 connectedcomponents,118 graph coloring,42-43,381 minimum-cost spanning tree,325-331 searching,310-313 single-source shortest path,318-325   
Graph,ipartite8   
Graph theoretic'terminology,67-370   
Graph theoryelevance of ortingto255   
Graycode,140142,192,2474   
Great Seal of the United States,52   
Gregor,J.A.,3   
Grosch's law, 19   
Halving lemma,206,374   
Hamiltoanircit,5   
Heap,parallel,329-331   
Height,297,369,1   
Herrick, $\mathrm { R } _ { \infty }$ 336   
Hexagonal mesh, 155   
Heywood,J.,25   
High-level languages, 93   
High-level parallelism,4   
High-speed computing,1-2   
Hirschbergsoritm,114,3   
HITECH,359   
Host processor (see Front end)   
Hot spot,191,08,   
H-tree,136   
Hypercube: all-pairs shortest path,318 bitonic merge,271-272 Connection Machine CM-200,63 compared to other networks,61 defined, 57-58,381 embedding graphs in,137-142 fast Fouriertranform,206-213 graph algorithms,333 hyperquicksort,76 matrix multiplication,183-186,191-196 nCUBE2,74-75 reduction algorithm, 160-163 traveling salesperson problem,347-352   
Hypercube network(seeHypercube)   
Hyperquicksort,6   
Hypertree: compared to other networks,61 Connection MachineCM-5,75 defined 55-56,381 reasonable model, 86   
ICL Distributed Array Processor (see AMT DAP)   
IF construct, occam,5117   
if.efodec   
ILLIAC IV,4, 86   
Image processing,255   
Imaginarymnt,   
Imaginaryrt   
Immediate redecessor14781   
Immediatecer   
infuncia,   
Independentstftasks,47   
Indexfui7   
Information,8   
Initial tasks,147,381   
Inmos Limited,1   
INNER.PRODUCT,249,251   
inp function,C-Linda,   
Input procs1   
Instructioneing   
Instruction cycle, 5   
Instructionlook-ahead,5,   
[nstruction pipelining,5,8   
Instruction prefetching,5   
Instructioream   
Insurance claims adjustors analogy,158   
Intel, 4 80386/80387 microprocessor68-69 i860 XPmicroprocessor,76-78 iPSC,73,213,363 iPSC/2,73-74 iPSC/860,73,285-286 Paragon XP/S,5,54,72,76-79 Touchstone DELTA,88   
Interleaved memory,5,81   
Internal sort,5,   
Interpolation,inultigidmetos46   
Inversedi 381   
Inverse Gray code,140-141   
iPSC (see Intel iPSC)   
Irregular meshes42,14   
ISO,95   
Iterative deepening,359,381   
Iterative methods for solving linear systems, 237-251   
Jacobialgorithm,237-244   
Jacobi overeion246   
Jung,C.G.,198   
Kasantzakis, N., 157   
$k$ -connectedomots3   
Key,294,381   
Knapsack problem, 354, 381   
Kruskal’sithm3   
Landscaping example, 9   
Language,paralle (seeParallel progamming languages)   
Lattice,53   
Left subscripting, 124   
Length,chain,149,8   
Level,149,81   
Level of parallelism,131   
Light,speed of, 5   
Light-weight threads 381   
Linda,118,127   
Linear equation,218,381   
Linear system,218,82   
Linked array，325,382   
List ranking,34-35,382   
List schedulingalgorithm,Graham's,145 146   
Load,134,382   
Load balancingalgorithms,143   
Local keyword,1   
Local memory (see Distributed memory)   
Localityof reference,382   
lockfui   
Lock operation,5   
Logarithmiccost criterion,27,82   
Logarithmic-time parallel sortingalgorithms, .290   
Logic programming,128-129   
Loosely coupled multiprocessor (see Multiprocessores memory access)   
Lower boud,atrixultipcio 181   
Lower bound,on searching,295-296   
Lower bound, on sorting, 257-258,292   
Lower trngulartrix,92   
Lowest common ancestors,333   
Loyd, S.,39   
LU decomposition   
Luke,1   
Mailboxanalogy,288-289   
Mainframe computer performance growth, 4-5   
Maintenance processes, 304-306   
ManberandLadner'salgorithm,302-306   
Manttanance,34   
Manip,364   
Mapping,132-142,154   
Masking processing elements,62   
MasPar: MP-1,54 MP-2,5   
MassivelyParallel rocessor,Goodyearerospa 54,86   
Master/workeralgorithm,9120   
Materials design,2   
Matrix: diagonallydominant,2 lower triangular,219 positive definite,220 symmetric,220 tridiagonal,19 upper triangular, 219   
Matrix multiplication,179-197,318 1-D mesh SIMD, 196 2-D mesh SIMD,180-184 block,189-190,193-196 hypercube,183-187,191-196 multicomputers,191-196 multiprocessors,187-191 NUMAis processor arrays,180-187 sequential, shuffle-exchange, 186-187 UMAmuloco VLSI algorithms,196-197   
Matrixreduction,34344   
Matrix traspose,176   
MATRIX.VECTOR.PRODUCT,249,   
Maximum-capacity path,334   
Maximum clique,   
Maximum flow,48,334   
Maximum independent set,334   
Maximum matching,333   
Max-tourament,235,82   
MAX.TOURNAMENT,236   
Mechanicsaisial,   
Medicine,'3   
Megabyte,82   
Megaflops,382   
Meiko Computing Surface,73   
Memoryk   
Memory,cache (see Cachememory)   
Memorytedeei ory)   
Memory,shared (see Shared memory)   
Memoryur   
Mergesort,91   
Merging sorted lists,40-42   
Mesh: bitonic merge,267-271 compared to other networks,61 connected componentsalgorithm,315-318 data routing,176 defined,5-54, embedding graphsin,134-137 embedding in hypercube,139-142 hexagonal, lower bounds on matrix multiplication, 180-181 lower bounds on parallel sorting,257- 258 matrix multiplication,181-184 mergesort,291 multidimensional, 140-141 odd-evenerge rt90 odd-eventraspositionsort58260 Paragon XP/S,76 processor numbering schemes,270,291 reasonable model,86 reduction,162,164-167   
Message tency   
Message   
Message routing: circuit-switched,774 store-and-forward,73,132   
m_fork,entC5,   
m-getmid,quent C,   
m_get_numprocs,Sequent C,105   
Microprocessors: Intel 80386/80387,68 Intel i860 XP,78 Motorola 88100/88200,70 performancegrowth,45   
Microsecond,   
Millisecond,   
MIMD,79,2   
(Seealsoicoeris   
Minicomputer performance growth,4-5   
Minimax35455,82   
Minimum-cost spanning forest,325-326   
Minim3 369-370,382   
Minsky'secure   
Min-tourmnt,5,   
MISD,79,82   
m_kilirocs,equent C,16   
m_lock,qtC,,   
Modeling,2-3   
Modified hyperquicksort,281   
Modula,106   
Module,memory, (See also Memory bank)   
Molecular dynamics,4   
Monitor,106-107,382   
Moore'salgorithm1920   
Motorola 88100/88200,70   
MPP, Goearoce,,6   
m_set_procs, Sequent C,105,108-109   
Multicomputer algorithms: broadcast,170-171 fastFourertrao0623 graph problems,333 hyperquicksort,61 matrix multiplication,191-196 sorting,292 traveling salesperson problem,347-352 variancecomputation,91-94   
Multicomputer architectures: Connection Machine CM-5,75-76 Cosmic Cube,87 nCUBE2,74-75 overview,72-74,86,8 Paragon XP/S,76-78   
Multigrid methods,246-248,253   
Multilisp,127   
Multimax,e6   
Multiple functional units,5,158   
Multipleim stream,79,382   
Multipleinstructionstream,singledataream 79,382   
Multiplexed message routing,133   
Multiplication: matrix (see Matrix multiplication) polynomial, 203-205   
Multiprocessing,5   
Multiprocessoralgorithms: back substitution,220-223 batch searching,296-306 combinatorial search,338 matrix multiplicaion,7-191 minimum-costspanning tree,31 odd-evenreduction,224-229 reduction,165-170 single-source shortest path,318-325 sorting,291-292 traveling salesperson problem, 346-347 variance utation92   
Multiprocessor architectures: cause of superlinear speedup,81 $\mathbf { C m ^ { * } }$ 87 C.mmp,86 Flynn's taxonomy,79 non-uniform memoryaccess,7687 383 overview,67-68,70 Paradigm,87 Symmetry,68-70 TC2000,70-72 uniform memory access,67-68,86-87, 387   
Multiprogramming,382   
Multistage networks85   
m_unlock,SequentC,6,1   
Muthusamy,Y.,   
Mutual exclusion:   
defined,8   
implemented via lock and unlock,125   
implementedvia monitors,106-107   
necessary for deadlock, 151

synchronization method,91,104 Nanoinstructions,64 Nanosecond, NC,47-48,50,33 nCUBE,4,58,74 C programminglanguage,93,109-112 nCUBE 2,73-75,79 nCUBE 3200: alpha-beta search speedup, 365 fast Fouriertransforspeedup,210, 213 gaussian elimination speedup, 237 hyperquicksort speedup,280 Jacobialgorithmparallizability,239 240 matrix multiplication speedup,193, 195 prefix sums speedup,174--175 traveling salesperson speedup,349- nCUBE/10,73 351 NEC SC-3,5 Necklace,60,83 shrt,60,85 Network: binary $n$ -cube (see Hypercube) binary tree (see Binary tree) butterfly (see Buttrfly) cube-connected cycles (see Cube-connected cycles) cube-connected (see Hypercube) de Bruijn (see deBruijnnetwork) hypercube (see Hypercube) mesh (see Mesh) omega,60,383 prism,85-86 pyramid,56,61,85,384 shfe-exange (see Sufe-ecge) Network flow problems252 New York Uersity68,6 NEWS grid,66, Nondetermsticdel Nonlinear problems,252 Nonlocal ables, Nonnumerical algorithm,178 Nonpreemption, Nonsimple task graph,149 Non-uniform memoryaccessmultiprocessor,see Multiprocessor northeyrd Notatione $\mathcal { N P }$ 46-48 $\mathcal { N P }$ complete,46-48,137,153154 $\mathcal { N P }$ -hard,145 nread,nCUBE C,1,112,124 nthrootsofitymlex,204, 374,378 NUMA multiprocessor (see Multiprocessor) Numericalintegration5,1 Numerical simulation,2 nwrite,nUBE C,1,1,124 Oak Ridge National Laboratory3 Objective function,4

Occam, 113-118   
Ocean circulation, 3   
Odd-even exchange,58,83   
Odd-evenmerge sort90   
Odd-even ordering(seeRed-black coloring)   
Odd-evenruction22422952,8   
Odd-evenit891   
Omega network,60-61,68,8   
1-D mesh (see Mesh)   
Optimal schedule,145,147,83   
Optimization problem,337,383   
OR tree,337-338,340,365,383   
Ordinary diferential equations,253   
Oregon Graduate Institute of Science and Technology,201   
Oregon State University,3   
Othello, 363-364   
out function,C-Linda,1   
Output rocesscm11   
Overhead,c   
Overhead,arch,6   
$\mathcal { P }$ ,46-48   
P operation on binary semaphore,151   
Pape-d'Esopo'sgorithm,5   
PAR construct,cam   
Paradigm,87   
Para-functional programming,127   
Paragon XP/S (see Intel Paragon XP/S)   
Paralel algorithmdesign strategies,375 #1,find cost-optimal PRAM algorithm, 159 #2, considerdata parallelismfirst68 #3,make best useof resources,171 #4,use bestsuetialgoithm,12 #5,maximize grain size,188,320,326 #6,increase locality,190 #7,change temporal orderof dataaccesses, 191 #8, changedata structures,321   
Parallel algorithms (see Control paralelism, Data parallelism,Multicomputeralgorithms,ulorois algorithms,Processorarrayalgorithms)   
Parallel spirationarch35960   
Parallel computation thesis,47,83   
Parallel computer6 (Seealso Multicomputerarchitectures,Multiproceso ray architecture)   
Parallel computing,6,83   
Paralleldatadistriution   
Parallel languages: high-level, issues,91 (See also Paralel programming languages)   
Parallel ix (See also Prefix sums)   
Paralle processing: defined,6, practical,45   
Parallel processing unit,63-64   
Parallel program development svstem. 132   
Parallel programming languages, 90-130 C\*,99-103 C-Linda,11122 Fortran 90,95--99 nCUBE C,19-11 occam,113-118 pseudocode,122-127 Sequent C,104-109   
Parallel sorting by regular sampling,281- 286   
Parallel subtreeeauation59-360   
Parallelism,4,383 control (see Control parallelism) data (see Data parallelism) level,   
Parallelizability   
Parallelization,83   
Parallelizing compilers,128   
Parameter keyword,122   
Parent,370,83   
Paris,64   
Parlog,129   
Parsytec SuperCluster,73   
Partial diferetaleuos,4241 246,253   
Partial pivoting, 230   
Partial sum,383   
Particle-in-cellsimulation142   
Partitionedalgorithm (see'Data paralelism)   
Path,368,383   
Pathological game trees,365   
Pattern recognition,200   
$\mathcal { P }$ complete,4748,310,3   
pcoord function, $\mathbf { C } ^ { * }$ 101   
P-depthsrch,lel,   
Perfect shuffle,59,176,265,267,384 (See also Shuffle-exchange)   
Perfectlyrdered game tree,358,383   
Performance growth,omputer,45   
Permutation,208-210,214,255,868   
Pharmacology,3   
Phonemes,200   
Photocopier example, 6   
Physics,relativistic,2   
Pi computation: $\mathbf { C } ^ { * }$ implementation,103 C-Lindaimplementations1 description ofalgorithm,93-95 Fortran90implementation,99 nCUBE Cietaio1 occam implementation,117 pseudocode implementations,126-127 Sequent Cimlementation108   
Picosecond,   
Pipelinedalgorithm,6,,8   
Pipelined functional units,5   
Pipelinedvector processor61754   
Pipelining,6-8,384   
Pivot row,230,84   
Planarity testing,   
Playing cards,20   
Plus-min multiplication,313   
Ply, 359, 384   
Pointer jumping,3435,38,384   
Polylogarithmicfuction4784   
Polylogariceeity4 264,384   
Polynomialmultipliation,5   
Polynomial time,47   
Positivedefierix   
PP-PRAM,49   
PRAM: models,27-30,384 pronunciation,'25 spawning processes,30   
PRAM algorithms: connectedcomponents,115 enumerationsort,256-257 graph coloring,42-43 list ranking,34-35 merging two sorted lists,40-42 minimum-cost spanningtree,333 prefix sums,32-34 preorder tree traversal,36-40 reduction,31-32,159 searchinga graph,309-313 searchinga table,295 sorting,290-291   
Precedence sychronization,95   
Predecessoreyord,24   
Prefix sums,3233,45-46,172-175,384   
Preordertree traversal algorithm,6-40   
Prescheduledata-pallelgorit 384   
Primality testing,9-10   
Prim-Dijkstra'salgorithm   
Primitiverootofunity201-203   
Principalnthrootofunity73,84   
Principal variation splitting,365   
PRIORITY PRAM,28,384   
Priority queue,349-351   
Prism network,586   
Private memory (see Local memory)   
Process creationand coordination,91   
Processeationtime,150   
Processor array algorithms: bitonicmerge,267-271 bitonic merge,271-272 broadcast, 170-171 connected components,315-318 matrix multiplication,181-186 mergesort, 291 odd-even merge sort,90 odd-even transposition sort, 258-260 reduction, 160-167   
Processorarrayarchitectures: classifiedinlynn'staxoomy79-80 Connection achine C-200,6-67 overview,61-63,384 references in literature to, 86   
Processorl   
Processor organizations,53-61   
Production systems,129   
Projection,in multigrid methods,247

Prolog,128   
Concurrent,127   
Protein folding,3   
Proust, M.,178   
Pruning,alpha-beta, 355   
Pseudocodeription17   
Ptolemaic system,255   
PVS,365   
Pyramid network,56,61,6   
QIX,128   
QR factorization, 252   
Quantum chemistry,2   
Queuing models,154   
Quicksort,lle,   
RAM (see Random access machine)   
Randomaccess machine,2684   
Random read,286-289,315,384   
RANDOM.READ,315,317   
Randomuniform gametree,384   
Random write,286-288,315,384   
RANDOM.WRITE,315,317   
Randomizedralelagorithms091   
Rank,385   
rd function, C-Linda,119   
rdp function, C-ina,   
Ready list (ready queue),32,144,150   
Real part ofaomplex umber1,85   
Reasonable pael mdel,5   
Rebound sorter,291   
Receiver initiated load balancingalgorithms,   
143,385   
Recurrencerationfte5   
Red-black coloring,245   
REDUCE,316-317   
Reduction   
2-D mesh,162,164-167   
CREWPRAM,31-32,44-45   
defined,31,   
hypercube,160-163   
Litle et al.'salgorithm,343-344   
shufe-exange,61616165   
UMA multiprocessor,165-170   
Referenceeyword,12   
Relativistic physics,2   
Relaxation,in multigrid methos,246   
Relaxed algorithm (see Asynchronous algo  
rithm)   
Replicator constructocam,116   
Resource waiting,152   
Ring,134,139-142,191195   
RNC,154,332   
Roethke,T.,9   
Rogers,S.,   
Root,369,385   
Root ofunityimie1   
RotationinAVLtrees,298   
Routing:   
circuit-switched,   
store-andrward,   
Routingalgorithms,176   
Row-majorder70,291

Row-oriented data distribution, 241,243- 244   
RP-RAM,49   
Rule-based expert systems,129   
Scalability,9,87   
Scalable algorithmsandarchitectures,9,7, 385   
Scaled efficiency,83-84,385   
Scaled speedup,81-84,385   
Scan,33,67,385   
Schedule,145,85 optimal,145,147   
Scheduling algorithm: Coffman-Graham,146-148 Graham,145-146   
Science,classical vs.contemporary2   
ScientificComutingssociates1   
Search: breadth-depth,311-312 breadth\~first,311-313 depth-first,48, p-depth,310-312 strong,303 weak,303   
Search overhead,60,85   
Search tree,296   
Searching on multiprocessors,296-306   
Seevers,B.K.,169,175   
Segment,6,85   
Self-scheduledat-rallellgor5, 385   
Semaphore,151   
Semi-distributed load balancingalgorithms, 143,385   
Sender initiated load balancing algorithm, 143,385   
SEQ construct,cam,115117   
Sequence,toic,665,77   
Sequent: Balance,69,167-169,365 Cprogramming language,93,104-109 Symmetry:architecture,68-71 back substitution'speedup,223 matrix multiplicationspeedup,189 MIMD category,79 odd-even reductionspeedup,227, 229 quicksort speedup, 275,277 Sollin'sgorthspeeup,329 System Bus,68-70   
Sequential algorithm: alpha-beta search,356 Back substitution,221 Coffman-Graham scheduling algorithm,14 148 conjugate gradient,250-251 defined,85 fast Fourier transform (FFT),207-208 gaussian elimination,231 Graham’s listscheduling algorithm,145- 146 heap construction,331 Jacobi agoim9,4

heap construction, 331 Matrix multiplication,79 minimum-cost spanning tree,28 Moore'salgorithm,320 odd-even uctio shortest path, 320 Sieve of Eratosthenes,9-10 Sollin'salgorithm328 traveling salesperson,345 tridiagonal system soer,225 Sequentialcomputer,2627,62-674, Sequential programs,93 Serial,8 shape, C\*,100,385 Shared address space,70 Shared dataagageupportfor04,106 Shared memory: Fortran 90 model,96 hot spot,191,308,381 Linda model, 118 NUMA multiprocessor,67 PRAMmodel,78 Pseudocode costructs,122,4125 ready list stored in,144 role in reduction algorithm,165 Sequentel, Sequent Symmetry,68 UMA multiprocessor,67 Sharediablestetionor08 Shell sort,allel,92 Short necklace,60,385 Sorest 369 shuffle eyword,pseudocode,5 Shuffle: defined,385 (See also Shuffe-exchange) Shuledojoder7 Shuffle-exchange: all-pairs shortest path,318 basis for processor arrays,63 bitonicmerge,264-269 compared to other networks, 61 defined,59605 lower bounds on sorting,258 matrix multiplication,186-187 pseudocode support for,124 reasonable model, 86 reduction,160-161,164-165 relation to omega network,85 Sieve of Eratosthenes: control-allelgorith1 data-paralleloit sequential algorithm, 9-10 Signal frequency，990 Signal strength,199 SIMD,79,385 (See also Processor array) SIMDAG,49 SIMD-SM model,49 Simple task graph,149,86 Simpson'sRule,10

Single instructionstream,multipledtastra (see Processor array)   
Single instructionream,ingledataam (seeSequtl computer)   
SingleProgam,ultileata9,169   
Single rotation of AVL tree,298   
Single-soueh 368,386   
Sinusoidal functions,19-200   
SISD,79,386 (See alsoalgori tialcomputer)   
s_lock,Sequent C,106-10   
Slotnick,D.,4   
SM SIMD model,49   
Snakelikerow-majororder,270,291   
Sollin'sagorithm,629,33   
Solomon,4   
Solution to a linear system,218,386   
SOR (see Successive overrelaxation)   
Sorting,pallel: bitonic merge,260-272 enumeration sort,256-257 hyperquickort,728 lower bounds,257-258 odd-even transposition sort, 258-260 parallel sortingbyregular sampling,281- 286 quicksort, 273-277 random read and random write, 286-290   
Sortingnetworks,67291   
Source vertex18,86   
south ord,oce5   
Spacecomplexity，6   
Spanning tree,369,386   
SPARC CPU,75   
Sparse linear system solvers,237-251,253   
Spatial locality,386   
Spawning PRAM processes,30   
Spectral analysis, 199   
Spectral decomposition,214   
Speech analysis,199-201   
Speed of light limitations,5   
Speedup,6,80,87,86 anomalies,80-81,352-354,365 scaled,81-84,5 superlinear,80-81,353-354,387   
Spin lock,386   
Spinning,386   
Split-and-merge,277   
SPMD,109,169,386   
SP-RAM,49   
Spread,67,386   
SSB,68   
$S S S ^ { * }$ 365   
Stable-marriageproblem,334   
Stack otoru   
Stage,6,386   
Stanford University,87   
State space tree,339-340,342,345,386   
Static scheduling,143-150

deterministic models, 144-147 nondeterministicmodels,47150 Statistical mechanics,2 Steady-stateemperaturedistributio29 220,239-241,244-245 Stencil,53 Store-and-forardrouting786 Strassen'so79,196 Stream,dataorinsrucion,79 Strong search,0,8 Strongly connected components,333 Strongly ordered gametrees,65 Subgraph,368,86 Subtreeeinlel6 Succesiver Succed Suffix sums,34,86 Summation(see Reduction) Sun workstation,63 s.unlock, Sequent C,16-107 Supercomputer,6,, performance growth of,4-5 Superconductivity, Superlinearspeedup8081,554,387 Symmetric mtrix,208 SymmetrySequent (seeSequent try) Synchronizaion,rier,91,4,25,377 System Link and Interrupt Controller, Sequent, 69 System of linear equations,218,387 Systolic array,79 T414 Transputer,113 T800 Transputer,73 Table,294,387 Task graph,144,149,387 Task scheduling,145-148 Taylor series,373 Temporal locality,387 Terabyte,387 Terminologyrallel procesing59 Test and Cotroltem000,72 Thinking Machines,63,99 ConnectionachineCM0,58,667 79 ConnectionMachineCM-5,5,56,73,75 76,78-79 Throughput,6,87 Tightly coupled multiprocessor (see Multiprocessor architectures,uniform memoryaccess) Timecomplexity,26,387 To,367,387 Toeplitz linear systems,252 Touchstone DELTA (see Intel,Touchtoe DELTA) Tournament,235,387 Transitive closure,313 Transputer,73,3,1 Travelingsalesperson problem,333,342- 346,365,387 Tree:,369,387

AND,337-338,376 AND/OR,337-338,365,376 binary (see Binary tree) complete binary(seeComplete binary tree) defined,369,87 OR,337-338,340,365,383 search,296 state space,339-340,342,345,386 Treesorter,291 Tridiagonal linear system solvers,224-229, 252 Tridiagonal matrix,219,387 Triton/1,61 Truth table,64-65 TSP,see Traveling salesperson problem Tuple space,118,87 Turbulence,'2 2-D mesh (see Mesh) Two-processor unit time scheduling,154 Ultracomputer,686,256 UMAmultiprocessor (see Multiprocessor) Undirected graph,367,387 Uniformcost iterion,27 Uniform memory access multiprocessor (see Multiprocessor) UNION,326-328 Unit element,, Unit time edulingtwroces4 Universal computer,86 University of Illinois,4 University of Karlsruhe, 61 University of Manchester,87 UNIX,76,104 unlock function,pseudocode,125 Unlockoatio Upper bounds: searching,295-296 sorting,292 Upper triangular matrix,219,387 Upper triangular system solvers,22-223 Utilization,145,387 Voperationonbinarysemapore151 VAL,128 Value keyrd,sedd Variancecomputation,91-94 Vectorcomputer,617 (See also Pipelined vector processor,Processor array architectures) Vectorreal76 Vectorizing compiler128 Vertex,367,387 Vertex collase,313 Virtual memory,25,78 Virtual proo6 Virtual treemachine,365 VLSI algorithms,87,1,07 VME bus,70,72 von Neumann model of computing, 25 Weak search,303,387 Weakly connectedcomponents,33 Weight,367,369,387 Weight matrix,367,87

Weighted graph,367,387   
WeitekWTL1167,68   
west keyword,pseudocode5   
Westinghouse Electric Company,4   
where statement, $\mathbf { C } ^ { * }$ ,101-102   
While construct,pseudocoe23   
White House,294   
whoami,nCUBE C,11-12   
Widget machine example,7-8   
Width,149,388   
with statement, $\mathbf { C } ^ { * }$ ,100-102   
Worst-case space and time complexity,26，   
388   
Write,random,286-288,315,384   
Write-throughcache,69,88   
X3J3cmmitee,,95   
Zeroelemnt,7   
0-1 knapsack problem,354   
Zero-sum game, 354

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0007_pages_0421-0472/auto/images/a2ea2ae19275d3b6244c231ba67cc10106d2b036a4f55a1de181d678c5470981.jpg)

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0007_pages_0421-0472/auto/images/2956b7316a6022d480c6ffcc33f6bdd99c1e7f010f92fbc5fe4c08238e13fec3.jpg)

![](../chunks/Parallel computing theory and practice (Quinn, Michael J. (Michael Jay), Quinn etc.) (z-li_part_0007_pages_0421-0472/auto/images/8ff39cb573d2b0964b5ec81aa0b0cabd74cb781d89a94c134dd6b20eadc58915.jpg)

This text provides an exceptional introduction to parallel computing by balancing theoryand practice.The emphasis is ondesigninganalyzing and implementing parallelalgorithms'suitableforexecutiononrealparalelcomputers.Earlychapterssettheagebyintroducingeyonceptsllstratingfudamentalllel algorithmsanddesribing aystoincorpoategevel pralllismintod wareand software.Later chapters explore thedevelopment of paralel algorithms formatrixmultipicationthefastFouriertransformsolvinglinearsems sorting,sarcing，gahoreticoblemsnd omintorial sh Numerous graphs ilustrate the speedups that can be achieved onactual paralel hardwareby implementing the parallel algorithmsdeveloped in the text.Asa result,/studentslearnhowtomakeeicientuseofemergingparallelcomputer technology.

A numberof additional featuresmake this book distinctive：

It surveyssomeoftemostpopularparalelomputearcitecturesincluding Thinkingte Symmetry (TM)

Itcovers someofthemost popularparalel programming languages, including Fortran 90, ${ \sf C } ^ { \star }$ Lindaand OCCAM

Aglossaryofparallel computing terminology contains all the terms defined in the text

More than 200 exercises cover the gamutfrom proofs to programming assignments

Theexceptionallylarge bibliographyprovidesample opportunities for further study

LibraryofCongresscallnumberssimplifyaccesstofreqntly cited journalsand proceedings

# Also from McGraw-Hill:

Hwan Programmability9
