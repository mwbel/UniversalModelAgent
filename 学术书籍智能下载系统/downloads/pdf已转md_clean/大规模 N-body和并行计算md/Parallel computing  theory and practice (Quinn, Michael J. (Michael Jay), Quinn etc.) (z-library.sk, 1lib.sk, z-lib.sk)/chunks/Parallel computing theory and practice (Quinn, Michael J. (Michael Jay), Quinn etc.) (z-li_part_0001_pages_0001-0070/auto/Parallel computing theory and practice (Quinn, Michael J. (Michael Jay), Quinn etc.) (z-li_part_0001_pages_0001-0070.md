![](images/7a28ac116728a3e02e4dd1d438191d5e46dadddc27e77446c866ea9e09973289.jpg)

![](images/561a3f85161dcf9c757c021ab1f5df72db7392b14099f36e5e3bd7f64a213092.jpg)

# UNIVERSITY OF WESTMINSTER

![](images/323dfcb1a2baae87ae3a54259bdadf4dc7e68ab8f8dda4a8c178df50d0d05b12.jpg)

Failuretoreturnorrenewoverduebooksmayresultinsuspensionof borrowingrightsatallUniversityofWestminsterlibraries

Due for return on: 26.09.94 23. SEV 96 07.1I.94. 10 MAR 1999 2702.9531MAR2004 28.-03.85 17 JAN 2005 24.APR-95 15.MAY 95 29.JUN 95 05.DEC FEB 18MAR 96 Information Resource Services New Cavendish Street Library 115NewCavendish Street London W1M 8JS Telephone0719115000ext3627 0056

![](images/7ef7148034ba480a4ed028dc2ade7f380fba735d722e2d6be1d2c77f58f8001f.jpg)

# McGraw-Hill Series in Computer Science

SENIOR CONSULTING EDITOR

C.L.Liu，University of llinois at Urbana-Champaign

CONSULTING EDITOR

Allen B.Tucker，BowdoinCollege

Fundamentals of Computing and Programming   
Computer Organization and Architecture   
Systems and Languages   
Theoretical Foundations   
Software Engineering and Database   
Artificial Intelligence   
Networks，ParallelandDistributed Comuting   
Graphics and Visualization   
The MiT Electrical Engineering and Computer Science Series

# Networks, Parallel and Distributed Computing

Ahuja: Design and Analysis of Computer Communication Networks   
Filmanand Friedman: Coordinated Computing:Tools and Techniques for Distributed Software   
Hwang:AdvancedComputerrcitecture:aralelismcalabilityProgramit   
Keiser: Local Area Networks   
Kershenbaum: Telecommunications Network Design Algorithms   
Lakshmivarahan and Dhall: Analysis and Design of Parallel Computers   
Quinn: Parallel Computing: Theory and Practice

# PARALLEL COMPUTING

THEORY AND PRACTICE

SECOND EDITION

Michael J. Quinn Oregon State University

This book was set in Times Roman by Electronic Technical Publishing Services.   
The editor was Eric M.Munson;   
the production supervisor was Annette Mayeski.   
The coverwas designedby Carla Bauer.   
Project supervision was done by Electronic Technical Publishing Services.   
R.R.Donnelley& Sons Company was printer and binder.

# Figure Credits

Figures1-2and3-27:Reprinted fromComputerArchitecture:A QuantitativeApproachbyJohnL.HennessyandidAaeon99ithesoofebiserannn Inc., Figure2-1:Aho,Hopcroft,andUllman,TheDesignandAnalysisofComputerAlgorithms, $\circledcirc$ 1974, Addison-Weyeing,scutsge5,gure1.3.eidith Figure3-5:ReprintedfromComputational AspectsofVLsi byJeffreyD.Ullman $\circledcirc$ 1984,with the permissionofeshrerescechille Figure3-169122d:erntedro-elomin Computersby PhilipJ.HatcherandMichaelJ.Quinn, $\circledcirc$ 1991,withthe permissionof the publisher,TheMIT Press. Figure8-6:ReprintedfromIntroductiontolgorithmsbyThomasH.CormenChariesE.Leisersonand Ronald L.Rivest, $\circledcirc$ 1990,withthepermissionofthepublisher,cGraw-Hill,Inc. Figure9-1:avidHallidayandRobertResnick,FundamentalofPhysicsRevisedPrinting, $\circledcirc$ 1974,John Wiley& Sons,Inc.Reprinted bypermissonofJohn Wiley& ons,Inc. Figure10-15:RobertSedgewick,Agorihms $\circledcirc$ 1983,AsoWseyengssc 465(figure).Reprinted with permission. Figure1018:DonaldE.Knuth,TheArtofomputerProgramming,Volume3,ortingandearcing $\circledcirc$ 1973,AdioWeyeaingssettsge37igure6etedith QuotationatbeginningofChapter6:Zorba theGreek,COPYGHT $\circledcirc$ 1953by Simon& Schuster. $\circledcirc$ Renewed by Simon&Schuster.Reprinted by permission from Simon& Schuster,Inc.

# PARALLEL COMPUTING Theory and Practice

Copyright $\circledcirc$ 1994byMcGraw-Hill,Inc.Allrightsreserved.Previouslypublishedunderthe title of Designing EficientAlgorithmsfor Parallel Computers.Copyright $\circledcirc$ 1987by McGraw-Hill, Inc.All rightsreserved.Printedinthe United Statesof America.Exceptaspermittedunder the United States Copyright Act of 1976,no part of this publication may be reproduced or distributed inany form orbyanymeans,orstored inadata base orretrieval system,without the prior written permission of the publisher.

This book is printed on recycled,acid-free paper containinga minimum of $50 \%$ recycled deinked fiber.

1234567890 DOH DOH 909876543

# ISBN 0-07-051294-9

# Library of Congress Cataloging-in-Publication Data

Quinn,Michael J.(Michael Jay) Parallel computing:theoryand practice/Michael J.Quinn.一 2nd ed. p.cm.-(McGraw-Hillseries incomputer science.Networks, paralleland distributed computing) Rev.ed.of:Designingefficientalgorithmsforparallel computers.c1987. Includes index. ISBN 0-07-051294-9 1.Parallelcomputers.I.QuinnicelJ.(iclay). Designing efficient algorithmsforparallel computers.Il.Title. Ill.Series:McGraw-Hillcomputer cience series.Networks parallelanddistributedcomputing. QA76.5.Q56 1994 004'.35-dc20

MICHAEL J. QUINN is an associate professor of computer science at Oregon State University.He received his Ph.D.in computer science from Washington State University.He has also taught at the University of New Hampshire, and he worked for two years at Tektronix,Inc.asa software engineer before earninghis doctorate.Heisauthorof Designing Efcient Algorithms for Parallel Computers (McGraw-Hill, 1987) and co-author (with Philip J. Hatcher) of Data-Parallel Programming on MIMD Computers (The MIT Press,1991).Dr. Quinn has published dozens of technical papers in the areas of parallel algorithms and data-parallel programming environments. Currently he is editor-inchief of IEEE Parallel and Distributed Technology:Systems and Applications magazine.

![](images/51d6278509c8d1d2bf0d160847916097b14815f4b3231ab8df588a67fae6eb97.jpg)

Doubt thou the stars are fire;   
Doubt that the sun doth move; Doubt truth to be a liar;

![](images/c5dbad790f9bdeb7b98fbb1f502c6cf9080eac150fe98d30c42fb08d1a4e0843.jpg)

![](images/6cbab8ca7750749e3aef6b17f99a4b5176e9ba8d038e1614606fb4512a96566c.jpg)

PREFACE xV

# 1 Introduction

1.1COMPUTATIONAL DEMANDS OF MODERN SCIENCE   
1.2 ADVENT OF PRACTICAL PARALLEL PROCESSING

1.3PARALLEL PROCESSING TERMINOLOGY

1.3.1 Contrasting Pipelining and Data Parallelism   
1.3.2 Control Parallelism   
1.3.3 Scalability

1.4 THE SIEVE OF ERATOSTHENES 1.4.1 Control-Parallel Approach 1.4.2 Data-Parallel Approach 1.4.3 Data-Parallel Approach with I/O

1.5SUMMARY

1.6BIBLIOGRAPHIC NOTES

1.7PROBLEMS

# 2 PRAM Algorithms

25

2.1 AMODEL OF SERIAL COMPUTATION 20   
2.2 THEPRAM MODEL OF PARALLEL COMPUTATION   
2.3 PRAM ALGORITHMS 2.3.1 Parallel Reduction 31 2.3.2 Prefix Sums 32 2.3.3 List Ranking 34 2.3.4 Preorder Tree Traversal 2.3.5 Merging Two Sorted Lists 40 2.3.6 Graph Coloring 42   
2.4REDUCING THE NUMBER OF PROCESSORS 43

2.5 PROBLEMS DEFYING FAST SOLUTIONS ON PRAMS 468   
2.6 SUMMARY   
2.7 BIBLIOGRAPHIC NOTES 48   
2.8 PROBLEMS 50   
3 Processor Arrays, Multiprocessors, and Multicomputers 52   
3.1 PROCESSOR ORGANIZATIONS 53   
3.1.1 Mesh Networks 53   
3.1.2 Binary Tree Networks 54   
3.1.3 Hypertree Networks 55   
3.1.4 Pyramid Networks 56   
3.1.5 Butterfly Networks 57   
3.1.6 Hypercube (Cube-Connected) Networks 57   
3.1.7 Cube-Connected Cycles Networks 58   
3.1.8 Shuffle-Exchange Networks 59   
3.1.9 de Bruijn Networks 60   
3.1.10 Processor Organization Summary 61   
3.2 PROCESSOR ARRAYS 61   
3.2.1 Connection Machine CM-200 63   
3.3 MULTIPROCESSORS 67   
3.3.1 Uniform Memory Access (UMA) Multiprocessors 67   
3.3.2 Non-Uniform Memory Access (NUMA)   
Multiprocessors 70   
3.4 MULTICOMPUTERS 72   
3.4.1 nCUBE 2 v 74   
3.4.2 Connection Machine CM-5 75   
3.4.3 Paragon XP/S √ 76   
3.5 FLYNN'S TAXONOMY 78   
3.6 SPEEDUP, SCALED SPEEDUP, AND PARALLELIZABILITY 80   
3.6.1 Can Speedup Be Greater than Linear? 80   
3.6.2 Scaled Speedup 81   
3.7 SUMMARY 84   
3.8 BIBLIOGRAPHIC NOTES 85   
3.9 PROBLEMS 88

# 4 Parallel Programming Languages 90

4.1 PROGRAMMING PARALLEL PROCESSES 91   
4.1.1 An llustrative Example 91   
4.1.2 A Sample Application 93   
4.2 FORTRAN 90 95   
4.2.1 Fortran 90 Programmer's Model 96   
4.2.2 Fortran 90 Language Features 96   
4.2.3 Sample Program 98   
4.3 C\* 99   
4.3.1 C\* Programmer's Model 99   
4.3.2 Language Features 100   
4.3.3 Sample Program 103   
4.4 SEQUENT C 104   
4.4.1 Parallel Programming under DYNIX 104   
4.4.2 Monitors 106   
4.4.3 Sample Program 106   
4.5 nCUBEC 109   
4.5.1 The Run-Time Model 109   
4.5.2 Extensions to the C Language 110   
4.5.3 Sample Program 110   
4.6 OCCAM 113   
4.6.1 Programmer's Model 113   
4.6.2 Language Constructs 114   
4.6.3 Sample Program   
4.7 C-LINDA 118   
4.7.1 Programmer's Model 118   
4.7.2 C-Linda Language Constructs 118   
4.7.3 Sample Programs 119   
4.8 A NOTATION FOR EXPRESSING PARALLEL ALGORITHMS 122   
4.9 SUMMARY 126   
4.10 BIBLIOGRAPHIC NOTES 127   
4.11 PROBLEMS 129

# 5 Mapping and Scheduling 131

5.1 MAPPING DATA TO PROCESSORS ON PROCESSOR ARRAYS AND   
MULTICOMPUTERS 132   
5.1.1 Ring into 2-D Mesh 134   
5.1.2 2-D Mesh into 2-D Mesh 134   
5.1.3 Complete Binary Tree into 2-D Mesh 135   
5.1.4 Binomial Tree into 2-D Mesh 136   
5.1.5 Embedding Graphs into Hypercubes 137   
5.1.6 Complete Binary Tree into Hypercube 137   
5.1.7 Binomial Tree into Hypercube 138   
5.1.8 Rings and Meshes into Hypercube 139   
5.2 DYNAMIC LOAD BALANCING ON MULTICOMPUTERS 142   
5.3 STATIC SCHEDULING ON UMA MULTIPROCESSORS 143   
5.3.1 Deterministic Models 144   
5.3.2 Graham's List Scheduling Algorithm 145   
5.3.3 Coffman-Graham Scheduling Algorithm 146   
5.3.4 Nondeterministic Models 147   
5.4 DEADLOCK 151   
5.5 SUMMARY 152   
5.6 BIBLIOGRAPHIC NOTES 153   
5.7 PROBLEMS 154

# 6Elementary Parallel Algorithms 157

6.1 CLASSIFYING MIMD ALGORITHMS 157   
6.2 REDUCTION 159   
6.2.1 Hypercube SIMD Model 160   
6.2.2 Shuffle-Exchange SIMD Model 160   
6.2.3 2-D Mesh SIMD Model 162   
6.2.4UMA Multiprocessor Model 165   
6.3 BROADCAST 170   
6.4 PREFIX SUMS 172   
6.5 SUMMARY 175   
6.6 BIBLIOGRAPHIC NOTES 176   
6.7 PROBLEMS 176

# 7 Matrix Multiplication

178

7.1 SEQUENTIAL MATRIX MULTIPLICATION 179   
7.2 ALGORITHMS FOR PROCESSOR ARRAYS 180   
7.2.1 Matrix Multiplication on the 2-D Mesh SiMD Model 180   
7.2.2 Matrix Multiplication on the Hypercube SIMD Model 183   
7.2.3 Matrix Multiplication on the Shufle-Exchange SIMD   
Model 186   
7.3 ALGORITHMSFORMULTIPROCESSORS 187   
7.4 ALGORITHMS FOR MULTICOMPUTERS 191   
7.4.1Row-Column-Oriented Algorithm 191   
7.4.2Block-Oriented Algorithm 193   
7.5 SUMMARY 196   
7.6 BIBLIOGRAPHIC NOTES 196   
7.7 PROBLEMS 197

# 8 The Fast Fourier Transform

198

8.1 INTRODUCTION 198   
8.2 THE DISCRETE FOURIER TRANSFORM 201   
8.2.1 Inverse Discrete Fourier Transform 202   
8.2.2 Sample Application: Polynomial Multiplication 203   
8.3 THE FAST FOURIER TRANSFORM 205   
8.3.1 Implementation on a Hypercube Multicomputer 207   
8.4 SUMMARY 211   
8.5 BIBLIOGRAPHIC NOTES 213   
8.6 PROBLEMS 214

# 9 Solving Linear Systems 217

9.1 TERMINOLOGY 218  
9.2 BACK SUBSTITUTION 220  
9.3 ODD-EVEN REDUCTION 224  
9.4 GAUSSIAN ELIMINATION 229  
9.5 THE JACOBI ALGORITHM 237  
9.5.1 Sparse Linear Systems 239  
9.6 THE GAUSS-SEIDEL ALGORITHM 244  
9.7 JACOBI OVERRELAXATION AND SUCCESSIVE  
OVERRELAXATION 245  
9.8 MULTIGRID METHODS 246  
9.9 CONJUGATE GRADIENT 248  
9.10 SUMMARY 251  
9.11 BIBLIOGRAPHIC NOTES 252  
9.12 PROBLEMS 253

# 10 Sorting

255

10.1 ENUMERATION SORT 256   
10.2 LOWER BOUNDS ON PARALLEL SORTING 257   
10.3 ODD-EVEN TRANSPOSITION SORT 258   
10.4 BITONIC MERGE 260   
10.4.1 Bitonic Merge on the Shuffle-Exchange Network 264   
10.4.2 Bitonic Merge on the Two-Dimensional Mesh   
Network 267   
10.4.3 Bitonic Merge on the Hypercube Network 271   
10.5 QUICKSORT-BASED ALGORITHMS 272   
10.5.1 Parallel Quicksort 273   
10.5.2 Hyperquicksort 276   
10.5.3 Parallel Sorting by Regular Sampling 281   
10.6 RANDOM READ AND RANDOM WRITE 286   
10.7 SUMMARY 288   
10.8 BIBLIOGRAPHIC NOTES 290   
10.9 PROBLEMS 292

# 11 Dictionary Operations

294

11.1 COMPLEXITY OF PARALLEL SEARCH 295   
11.2 SEARCHING ON MULTIPROCESSORS 296   
11.2.1 Ellis's Algorithm 297   
11.2.2 Manber and Ladner's Algorithm 302   
11.3 SUMMARY 306   
11.4 BIBLIOGRAPHIC NOTES 307   
11.5 PROBLEMS 307

# 12 Graph Algorithms 309

12.1 SEARCHING A GRAPH 309   
12.1.1 P-Depth Search 310   
12.1.2 Breadth-Depth Search 312   
12.1.3 Breadth-First Search 312   
12.2 CONNECTED COMPONENTS 313   
12.3 ALL-PAIRS SHORTEST PATH 318   
12.4 SINGLE-SOURCE SHORTEST PATH 318   
12.5 MINIMUM-COST SPANNING TREE 325   
12.5.1 Sollin's Algorithm 326   
12.5.2 Kruskal's Algorithm 329   
12.6 SUMMARY 332   
12.7 BIBLIOGRAPHIC NOTES 332   
12.8 PROBLEMS 334

# 13 Combinatorial Search 336

13.1 INTRODUCTION 337   
13.2 DIVIDE AND CONQUER 338   
13.3 BRANCH AND BOUND 339   
13.3.1 Traveling Salesperson Problem 342   
13.4 PARALLEL BRANCH-AND-BOUND ALGORITHMS 346   
13.4.1 Multiprocessor Algorithms 346   
13.4.2 Multicomputer Algorithms 347   
13.4.3 Anomalies in Parallel Branch and Bound 352   
13.5 ALPHA-BETA SEARCH 354   
13.6 PARALLEL ALPHA-BETA SEARCH 359   
13.6.1 Parallel Move Generation and Position Evaluation 359   
13.6.2 Parallel Aspiration Search 359   
13.6.3 Parallel Subtree Evaluation 360   
13.6.4 Distributed Tree Search 361   
13.7 SUMMARY 364   
13.8 BIBLIOGRAPHIC NOTES 364   
13.9 PROBLEMS 365

# APPENDIXES

A Graph Theoretic Terminology 367   
B Review of Complex Numbers 371   
C Parallel Algorithm Design Strategies 375   
GLOSSARY 376   
CALL NUMBERS 389   
BIBLIOGRAPHY 391   
INDEX 435

This book began as a revision of Designing Efcient Algorithms for Parallel Computers. I have changed the title for three reasons. First, two-thirds of the material in this edition is new.I have discarded the chapters on logic programming and pipelined vector processors,updated and enhanced the remaining material from the original book,and added chapters on PRAM algorithms, mapping and scheduling, and parallel imperative programming languages. Second,substantial organizational changes were made to improve the pedagogy. Third,the title Parallel Computing:Theory and Practice is more appropriate for an introductory text. My goal in writing this book has been to provide seniors and graduate students in computer science and engineering with an easy to understand introduction to the field of parallel computing.

Chapter 1 provides the motivation for the study of parallel computing. It explains why higher performance computers are needed and why commercial parallel computers have appeared over the past decade. It introduces basic parallel processing terminology and highlights the difference between control parallelismand data parallelism. Chapter2 describes parallel algorithms for the PRAM, a theoretical model of parallel computation.

Chapter 3 begins with a discussion of nine fundamental processor organizations and continues with a description of three parallel computer architectures: the processor array, the multiprocessor, and the multicomputer. Several commercial parallel computers are presented as case studies. Chapter 4 summarizes the features of six parallel imperative programming languages. Both low-level and high-level languages are described. Chapter 5 concludes the introductory portion of the text with some important theoretical results in the areas of mapping and scheduling.

Chapters 6 through 13 cover the design,analysis,and implementation of parallel algorithms on parallel computers. The chapters are organized by problem domain.As much as possible, I have ordered the chapters by increasing level of difficulty. Chapter 6 describes three elementary parallel algorithms:

reduction,broadcast, and prefix sums. Chapter 7discusses parallel implementations of matrix multiplication and Chapter 8 covers the parallelization of the Fast Fourier transform.

Chapter 9 follows with the parallelization of a wide variety of algorithms to solve systems of linear equations. Chapter 1O presents some important results in parallel sorting. Chapter 11 discusses dictionary operations and illuminates trade-offs between the complexity of the underlying sequential algorithm and the potential for keeping a large number of processors busy doing useful work. Chapter 12 describes parallel graph algorithms. Chapter 13 contains both theoretical and practical results in the area of parallel algorithms for combinatorial search. These problems occur in artificial intelligence,operations research,and graph theory,as well as in other areas.

A number of features make this book atractive for classroom use. Parallel algorithmsare presented ina machine-independent,high-level pseudocode. Experimental results from implementations of parallel algorithms appear frequently. Each chapter ends with a set of exercises with the more dificult exercises denoted by an asterisk $( ^ { * } )$ . Appendix A contains a review of the basic terminology of graph theory. Appendix B is a review of complex numbers. It can be used as a supplement to the chapter on the fast Fourier transform. A summary of parallel algorithm design strategies is given in Appendix C. I have also provided a glossary of parallel computing. The bibliography is large and facilitates further exploration of topics surveyed in this book. A directory of Library ofCongress call numbers,which appears immediately before the bibliography, makes articles from the most frequently cited journals and conference proceedings easier to locate. Finally,an instructor's manual is available,which contains answers to most of the exercises.

This book is a reflection of my nine years’ experience teaching parallel computing to undergraduate and graduate students at the University of New Hampshire and Oregon State University.I recommend that instructors augment the exercises with actual programming assignments on a parallel computer, computer network, or simulator. Programming a parallel computer is a new, difficult,and exciting experience for most students,and they learn a great deal from their efforts. In addition, graduate students should read recent journal articles and conference papers. With these supplements, there is more than enough material for a one-semester course. I recommend Chapters 1,3,and 6 be covered in their entirety. Section 4-8 is a prerequisite for the material in the rest of the chapters. The instructor must decide whether to cover a few of the remaining chapters in their entirety or pick and choose interesting sections. For example, if I were teaching a one-semester course to undergraduates with access to a Sequent multiprocessor, I would lecture on Chapters 1 through 3, Sections 4-1, 4-4;4-8,5-3,and 5-4,and Chapters 6, 7, 9, and 10. If time permitted, I would also cover Sections 13-5 and 13-6.

1 am grateful to Eric Munson, my editor at McGraw-Hill, for encouraging me to complete this project. Holly Stark, his editorial asistant,provided me with many valuable reviews that led to significant improvements in the quality of the text.I thank the reviewers for their efforts: Marc Abrams, Virginia Tech; Johnnie Baker, Kent State University; Moon Jung Chung,Michigan State University; Clyde Kruskal,University of Maryland; S.Lakshmivarahan,University of Oklahoma; Donald Miller, Arizona State University; Russ Miller,SUNY, Buffalo;Bruce Parker,New Jersey Institute of Technology;Oberta A.loter beck,Hiram College;Pradip K.Srimani, Colorado State University;Boleslaw K. Szymanski,Rensselaer Polytechnic Institute; Pearl Wang, George Mason University;Layne Watson, Virginia Polytechnic Intitute.

Many students at Oregon State University read drafts of the manuscript and provided me with corrrections and suggestions. Two students made particularly important contributions to the book. Teri Rohne helped me complete the Bibliography by tracking down dozens of missing references. Phyl Crandall carefully read the galley proofs and pointed out numerous erors.

Phil Hatcher deserves much of the credit for the cover. He suggested the orchestra analogy during a brainstorming session in Boulder, Colorado.

Finally, thanks to everybody who thought enough of the first edition of this book to ask me when the second edition was going to appear. Your confidence helped me find the energy to complete the job.

# 1

What king marching to war against another king would not first sit down and consider whetherwith ten thousand men he could standup to the otherwhoadvanced against himwith twenty thousand?

For those interested in high-speed computing, studying parallel algorithms is no longer an academic exercise; it is a necessity.Many problems can be solved by massive parallelism. For these problems the fastest computers in the world are built of numerous conventional microprocessors. The emergence of highperformance, massively parallel computers demands the development of new algorithms to take advantage of this technology.

This book discusses designing,analyzing,and implementing parallel algorithms for computers that have numerous processors. These steps are not always easy.Many algorithms suitable for conventional, single-processor computers are not appropriate for parallel architectures. Many algorithms with inherent parallelism have a higher computational complexity than the best sequential counterpart. In either case, implementing an inappropriate algorithm wastes a parallel computer's resources.We will examine these trade-offs in later chapters and discuss how to choose a parallel algorithm that makes good use of the target architecture.

In the remainder of Chap. 1 we place our exploration of parallel algorithms in context. Section 1.1 describes how science relies upon numerical simulation and gives examples of problems that could benefit from faster computers. In Section 1.2 we see why,after 2O years in research laboratories, parallel computers finally entered the commercial market. Section 1.3 introduces some important terminology and gives examples of pipelining, data parallelism, and control parallelism. Section 1.4 is devoted to a sample application-the Sieve of Eratosthenes. Designing control-parallel and data-parallel algorithms in this application reveals problems that arise whenever a parallel program is developed.

Parallel computing has come of age. Let's begin our study.

# 1.1 COMPUTATIONAL DEMANDS OF CONTEMPORARY SCIENCE

Classical science is based on observation, theory, and experimentation. Observation of a phenomenon leads to a hypothesis. The scientist develops a theory to explain the phenomenon and designs an experiment to test that theory. Usually the results of the experiment require the scientist to refine the theory,if not completely reject it. Here, observation may again take center stage.

Classical science is characterized by physical experiments and models. For example,many high school physics students have explored the relationship between mass,force,and acceleration using paper tape,pucks,and anair table. Physical experiments allow the scientist to test a theory-e.g.,Newton's first law of motion-against reality.

Unfortunately, we cannot always use physical experiments to test theories because they may be too expensive or time-consuming, because they may be unethical, or because they may be impossible to perform. High-speed computers allow scientists to test their hypotheses in another way by developing a numerical simulation of a phenomenon. The scientist compares the behavior of the numerical simulation,which implements the theorytoobservationsof “real world’ phenomena.The differences cause the scientist to revise the theory and/or make more observations.

Contemporary ience,hen,iscaracterizedbybservationtheoryxr imentation, and numerical simulation. Numerical simulation is an increasingly important tool for scientists.Many important scientific problems are so complex that solving them via numerical simulation requires extraordinarily powerful computers.These complex problems,often called“grand challenges" for science, fall into several categories (Levin 1989):

1 Quantum chemistry, statistical mechanics,and relativistic physics   
2 Cosmology and astrophysics   
3 Computational fluid dynamics and turbulence   
4 Materials design and superconductivity

5 Biology, pharmacology, genome sequencing, genetic engineering, protein folding,enymeactivityandcelleling

6 Medicine, and modeling of human organs and bones   
7 Global weather and environmental modeling

Consider three practical examples.

Oceanographers at Oregon State University are developing a numerical simulation of global ocean circulation. Their goal is to learn how the southern oceans transport heat to the south pole,an important step toward understanding the global warming problem (Fig. 1-1). To obtain accurate results, the scientists plan to divide the ocean into 4,096 regions running east to west and 1,024 regions running north to south. In addition, they will divide the ocean into 12 layers,with deeper layers containing sea water with greater density. In all, their model ocean will have about 5O million three-dimensional cells. A single iteration of their model simulates ocean circulation for 1O minutes and requires about 3O billion floating-point calculations. The oceanographers want to use the model to simulate ocean circulation over a period of years.

High temperature superconductivity may bring about many revolutionary developments,including highly energy-efficient power transmission and ultrasensitive instrumentation. The development of new high-temperature superconducting materials is being slowed by the lack of an accepted theory.Researchers at Oak Ridge National Laboratory have used laws of quantum mechanics to develop a computer program that can predict the structural, vibrational, and electronic properties of new materials. More than 150 trillion floatingpoint operations must be performed to complete a single computational experiment.

![](images/655fa27c480a83cbc13a84feb80a22be3b26173aed81d77b96e430876213833a.jpg)  
FIGURE 1-1 Sample output of a southern ocean circulationmodel developedat Oregon State University by Andrew F.Bennett and Boon Chua. The image shows oceanpressure (elevation) between the latitudes $3 2 ^ { \circ }$ Sand $7 5 ^ { \circ } ~ S$ .(Courtesy John A.Gregor.)

Finally, consider this example from molecular dynamics (Levin 199o). About one hour of Cray X/MP time is needed to model a one-picosecond interaction between a protein and its surrounding water molecules. An actual physical process of interest may continue for almost a second. Modeling such an interaction on the same machine, using the same algorithm, would require 31,688 years.

For decades computer architects have incorporated parallelism into various levels of hardware in order to increase the performance of computer systems. To achieve the extremely high speeds demanded by contemporary science, architectures must now incorporate parallelism at the highest levels of the system. Today, the fastest computers in the world use high-level parallelism. These computers are leading to new scientific discoveries.

# 1.2 ADVENT OF PRACTICAL PARALLEL PROCESSING

It took more than 2O years for parallel computers to move from the laboratory to the marketplace. Daniel Slotnick at the University of Ilinois designed two early parallel computers: Solomon, constructed by Westinghouse Electric Company in the early i96Os,and the ILLIAC IV,assembledat Burroughs Corporation in the early 1970s. At Carnegie-Mellon University,two well-documented parallel computers--C.mmp and Cm\*-were constructed during the 1970s. In the early 198Os researchers at Caltech built the Cosmic Cube, the ancestor of multicomputers built by Ametek, Intel, and nCUBE.

Still, it was not until the mid-198Os that commercial parallel computers constructed with microprocessors became available. A study of the performance growth in various computer classes reveals why microprocessor-based parallel processing finally became practical. Examine Fig. 1-2. The performance-growth rate for minicomputers,mainframes,and traditional supercomputers has been just under $20 \%$ a year, while the performance growth rate for microprocessors hasaveraged $3 5 \%$ a year.

![](images/21fbbccd9bfa7bb6ff84d1d3badd9727ce66b22c1be5e2e31f3212f49036ebb7.jpg)  
FIGURE 1-2

Why has the performance of microprocessors increased faster than the performance of other kinds of processors? The performance of a single processor can be improved through either architectural or technological advances. Architectural improvements can increase the amount of work performed per instruction cycle, while technological advances can reduce the time needed per instruction cycle.By the mid-197Os the fundamental architectural advances-bitparallel memory,bit-parallel arithmetic,cache memory,channels,interleaved memory,instruction lookahead, instruction pipelining, multiple functional units, pipelined functional units,and data pipelining-had already been incorporated into supercomputer designs. Since then, improving the performance of individual processors has meant reducing the instruction-cycle time. This has become increasingly difficult, since the speed of electronic circuits is limited by the speed of light.

In contrast, microprocessors have been able to achieve more impressive performance gains, because they have had so far to go. Early microprocessors did not incorporate all the architectural advances already present in supercomputers,and their clock speeds were much slower. Architectural advances,coupled with reduced instruction-cycle times, have led to impressive performance gains for this class of computer.

The convergence in relative performance between microcomputers and traditional supercomputers has led to the development of commercially viable parallel computers consisting of tens, hundreds,or even thousands of microprocessors. At peak efficiency, microprocessor-based parallel computers such as Intel's Paragon $\mathbf { X P } / \mathbf { S } ^ { \mathrm { { T M } } }$ ,MasPar's $\mathbf { M P - } 2 ^ { \mathrm { T M } }$ , and Thinking Machines’ CM-$5 ^ { \mathrm { T M } }$ ,exceed the speed of traditional single-processor supercomputers, such as the Cray $\mathrm { Y / M P ^ { \mathrm { T M } } }$ and the NEC $\mathrm { S X } { - 3 ^ { \mathrm { T M } } }$ 。

Harnessing the power latent in massively parallel microprocessor-based computers,however,requires the development of reasonable architectures,operating systems, programming languages, and algorithms. Poor design choices can lead to dismal performance. This book addresses the problem of designing efficient algorithms for real parallel computers.

# 1.3 PARALLEL PROCESSING TERMINOLOGY

Most high-performance modern computers exhibit concurrency. For example, multiprocessing is a method used to achieve concurrency at the job or program level,while instruction prefetching is a method of achieving concurrency at the interinstruction level. However,it is not desirable to call every modern computer a parallel computer. The concurrency of many machines is invisible to the user. Hence we adopt the following definitions.

Parallel processing is information processing that emphasizes the concurrent manipulation of data elements belonging to one or more processes solving a single problem. A parallel computer is a multiple-processor computer capable of parallel processing.

A supercomputer is a general-purpose computer capable of solving individual problems at extremely high computational speeds, compared with other computers built during the same time. Of course, "extremely high” is a relative term. By this definition supercomputers have always existed. All contemporary supercomputers are parallel computers. Some have a relatively small number of extremely powerful processors; others are made up of a relatively large number of microprocessors.

The throughput of a device is the number of results it produces per unit time. There are many ways to improve the throughput of a device. The speed at which the device operates can be increased,or the concurrency-the number of operations that are being performed at any one time-can be increased.

Pipelining and data parallelism are two ways to increase the concurrency of a computation. A pipelined computation is divided into a number of steps, called segments, or stages. Each segment works at full speed on a particular part of a computation. The output of one segment is the input of the next segment. If all the segments work at the same speed, once the pipe is full the work rate of the pipeline is equal to the sum of the work rates of the segments. A pipeline is analogous to an assembly line: the flow of results is simple and fixed,precedence constraints must be honored,and it takes time to fill and drain the pipe. If we assume that each segment of the pipe requires the same amount of time, the multiplicative increase in the throughput is equal to the number of segments in the pipeline. Figure 1-3 illustrates pipelining in the context of a high-performance photocopier.

Data parallelism is the use of multiple functional units to apply the same operation simultaneously to elements of a data set. A $k$ -fold increase in the number of functional units leads to a $k$ -fold increase in the throughput of the system,if there is no overhead associated with the increase in parallelism.

Speedup is the ratio between the time needed for the most eficient sequential algorithm to perform a computation and the time needed to perform the same computation on a machine incorporating pipelining and/or parallelism. (This definition of speedup isintuitive,but informal. We will formalize the definition in Chap. 3.)

![](images/c78a245cb186de1c13e7fcfc65c4961788627f7385dbfb478012f42aeceb3a06.jpg)  
FIGURE 1-3 3A high-performance photocopier is an example of apipelined processor.By dividing the copy process into three pipelined stages,the throughput of the copier is increased threefold without increasing processing speed.

# 1.3.1 Contrasting Pipelining and Data Parallelism

An example will illuminate the difference between pipelining and data parallelism as well as provide a practical demonstration of speedup. Assume that it takes three units of time to assemble a widget. Furthermore, assume that this assembly consists of three steps-A,B,and C—and each step requires exactly one unit of time. A sequential widget-assembly machine makes a widget by spending one unit of time performing step A,followed by one unit of time performing step B,and one unit of time performing step C. Clearly a sequential widget-assembly machine produces one widget in three time units, two widgets in six time units,and so on, as shown in Fig. 1-4a. Consider how the output could be increased if the assembly were pipelined. Figure 1-4b illustrates a three-segment pipeline. Each of the subassembly tasks has been assigned to a separate machine. The first machine performs subassembly task A on a new widget every time unit and passes the partially assembled widget to the second machine. In a similar way the second machine performs subassemblytask B,and the third machine performs subassembly task C. The pipelined widget-assembly machine produces one widget in three time units,as does the sequential machine; but after the initial time to fill the pipe (assembly line), one widget appears every time unit. Hence the second widget appears at time unit four, the third widget at time unit five,and so on.

![](images/30da8b1a72988a41956b82b4eefcc6b1616ebabca28c9bad2fe2992b43bc1105.jpg)  
FIGURE 1-4 Threemethods to assemble widgets. (a) A sequential widget-assembly machine produces one widget every three units of time. (b) A threesegment pipelined widgetassembly machine produces the first widget in three units of time and successive widgets every timeunit thereafter. (c) A three-way data-parallel widgetassembly machine produces three widgets every three units of time.

Figure 1-4c shows a group of three data-parallel widget-assembly machines. Each machine performs every subassembly task,as does the sequential widget assembler. Throughput is increased by replicating machines. Another three widgets appear every three time units. Note that the time needed to produce four widgets is the same as the time needed to produce five or six widgets.

Figure 1-5 illustrates the speedup achieved by the pipelined and data-parallel widget machines. The x axis represents the number of widgets assembled; the y axis represents the speedup achieved. For any particular number of widgets i, the speedup is computed by dividing the time needed for the sequential machine to assemble i widgets by the time needed for the pipelined or dataparallel machine to assemble i widgets. For example, the sequential machine requires 12 time units to assemble four widgets,while the pipelined machine requires six time units to assemble four widgets. Hence the pipelined machine exhibits a speedup of two for the task of assembling four widgets.

# 1.3.2 Control Parallelism

Our discussion has focused on data-parallel and pipelined algorithms. Pipelining is actually a special case of a more general class of parallel algorithms, called control-parallel algorithms.In contrast to data parallelism, in which parallelism is achieved by applying a single operation to a data set, control parallelism is achieved by applying different operations to different data elements simultaneously. The flow of data among these processes can be arbitrarily complex. If the data-flow graph forms a simple directed path, then we say the algorithm is pipelined.

Most realistic problems can exploit both data parallelism and control parallelism. Realistic problems also have some precedence relations between different tasks.For example, consider the problem of performing an estate's weekly landscape maintenance as quickly as possible (Fig. 1-6). Suppose four chores must be performed: mowing the lawn, edging the lawn,checking the sprinklers, and weeding the flower beds. With the exception of checking the sprinklers,

FIGURE 1-5 Speedup achieved by pipelined and parallel widget-assemblymachines. Note that speedup is graphed as a function of problem size (number of widgetsassembled). This is unusual. Speedup is typically_graphedasa function of number of processors used.

![](images/e7193837c3305f99768d7f231c63037b05e1a329f4adc953eb7d3a76a3ac3005.jpg)

SPEEDY LANDSCAPE, INC. Work Assignments--Medici Manor   

<table><tr><td>Mow lawn Allan Bernice</td><td>Edge lawn Francis Georgia Weed garden Hillary Irene</td></tr></table>

which is easily performed by a single person, each of the remaining chores can be done more quickly by multiple workers. Increasing the lawn-mowing speed by creating a lawn-mowing team and assigning each team member a portion of the lawn is an example of data parallelism. Since there is no reason why the flower beds cannot be weeded at the same time the lawn is being mowed, we can assign another team to the weeding. Concurrent weeding and lawn mowing is an example of control parallelism. Precedence relations exist between checking the sprinklers and the three other tasks, since all of the other tasks must be completed before the sprinklers are tested.

# 1.3.3 Scalability

An algorithm is scalable if the level of parallelism increases at least linearly with the problem size. An architecture is scalable if it continues to yield the same performance per processor,albeit used on a larger problem size, as the number of processors increases. Algorithmic and architectural scalability are important, because they allow a user to solve larger problems in the same amount of time by buying a parallel computer with more processors.

Data-parallel algorithms are more scalable than control-parallel algorithms, because the level of control parallelism is usually a constant, independent of the problem size,while the level of data parallelism is an increasing function of the problem size. Almost every problem we will study in this book has a data-parallel solution.

# 1.4 THE SIEVE OF ERATOSTHENES

In this section we will explore methods to parallelize the Sieve of Eratosthenes, the classic prime-finding algorithm. We will design and analyze both controlparallel and data-parallel implementations of this algorithm.

We want to find the number of primes less than or equal to some positive integer $n$ . A prime number has exactly two factors: itself and 1. The Sieve of

Eratosthenes begins with a list of natural numbers 2,3, 4,...,n,and removes composite numbers from the list by striking multiples of 2,3,5,and successive primes (see Fig. 1-7). The sieve terminates after multiples of the largest prime less than or equal to $\sqrt { n }$ have been struck.

Note: The Sieve of Eratosthenes is impractical for testing the primality of "interesting" numbers---those with hundreds of digits-because the time complexity of the algorithm is Ω(n),and n increases exponentially with the number of digits. However,more reasonable factoring algorithms make use of sieve techniques in other ways.

A sequential implementation of the Sieve of Eratosthenes manages three key data structures: a boolean array whose elements correspond to the natural numbers being sieved, an integer corresponding to latest prime number found, and an integer used as a loop index incremented as multiples of the current prime are marked as composite numbers (Fig. 1-8a).

# 1.4.1 Control-Parallel Approach

First let's examine a control-parallel algorithm to find the number of primes less than or equal to some positive integer $n$ . In this algorithm every processor

FIGURE 1-7 Use of the Sieve of Eratosthenes to find all primes less than or equal to 30. (a) Prime is next unmarked natural number-2. (b) Strike allmultiples of 2, beginning with 22. (c) Prime is next unmarked natural number-3. (d) Strike all multiples of 3,beginning with $3 ^ { 2 }$ . (e)Prime is next unmarked natural number-5. (f) Strike all multiples of 5, beginning with $5 ^ { 2 }$ .(g) Prime is next unmarked natural number-7. Since $7 ^ { 2 }$ is greater than 30,algorithm terminates.Allremaining unmarked natural numbers are also primes.

(a) 23456789101112131415161718192021222324252627282930  
(b) 23A567891112]1341561781920212223242526272829[30]  
(c) 23456789101112131415161718192021222324252627282930  
(d)23456789101121314051617819202222324252622282930  
(e)23456789101112131415161718192021222324252627282930  
(f) 23456789101112131415161718192021222324252627282930  
(g)、23456789101112131415161718192021222324252627282930

![](images/18b321c317be6e175a36c74e806fa2d51c760d7514921b855d6274b059fbb4bb.jpg)  
FIGURE 1-8 Shared memory model for parallel Sieve of Eratosthenes algorithm. (a) Sequential algorithm maintainsarray of natural numbers,variable storing currentprime,andvariable storing index of loop iterating througharray of natural numbers. (b) in parallel model each processor has its own private loop indexand sharesaccess to other variables with all processors.

repeatedly goes through the two-step process of finding the next prime number and striking from the list multiples of that prime, beginning with its square. The processors continue until a prime is found whose value is greater than $\sqrt { n }$ .Using this approach,processors concurrently mark multiples of iferent primes.For example, one processor will be responsible for marking multiples of 2 beginning with 4.Whilethis processor marks multiplesof2anothermay be marking multiples of 3 beginning with 9.

We will base the control-parallel algorithm on the simple model of parallel computation illustrated in Fig. 1-8b. Every processor shares access to the boolean array representing the natural numbers,as well as the integer containing the value of the latest prime number found. Because processors independently mark multiples of different primes, each processor has its own local loop index.

If a group of asynchronously executing processors share access to the same data structure in an unstructured way,inefficiencies or errors may occur. Here are two problems that can occur in the algorithm we just described. First, two processors may end up using the same prime value to sieve through the array.Normally a processor accesses the value of the current prime and begins searching at the next array location until it finds another unmarked cell,which corresponds to the next prime. Then it updates the value of the integer containing'the current prime. If a second processor accesses the value of the current prime before the first processor updates it, then both processors will end up finding the same new prime and performing a sieve based on that value. This does not make the algorithm incorrect, but it wastes time.

Second, a processor may end up sieving multiples of a composite number. For example, assume processor A is responsible for marking multiples of 2, but before it can mark any cells,processor B finds the next prime to be 3,and processor C searches for the next unmarked cell. Because cell 4 has not yet been marked, processor C returns with the value 4 as the latest “prime" number. As in the previous example,the algorithm is still correct, but a processor sieving multiples of 4 is wasting time.

In later chapters we will discuss ways to design parallel algorithms thal avoid such problems.

For now, let's explore the maximum speedup achievable by this parallel algorithm,assuming that none of the time-wasting problems described earlier happen. To make our analysis easier, we'll also ignore the time spent finding the next prime and concentrate on the operation of marking cells.

First let’s consider the time taken by the sequential algorithm. Assume it takes 1 unit of time for a processor to mark a cell. Suppose there are $k$ primes less than or equal to $\sqrt { n }$ .We denote these primes $\pi _ { 1 } , \pi _ { 2 } , \ldots , \pi _ { k } .$ (For example, $\pi _ { 1 } = 2 , \pi _ { 2 } = 3$ ,and $\pi _ { 3 } = 5 .$ ） The total amount of time a single processor spends striking out composite numbers is

$$
\begin{array} { c } { { \displaystyle ( { n + 1 } ) - { \pi } _ { 1 } ^ { 2 } } } \\ { { \displaystyle ( 1 + 1 ) - { \pi } _ { 1 } ^ { 2 } } } \\ { { \displaystyle ( 1 - 1 ) + \lceil \frac { ( n + 1 ) - { \pi } _ { 2 } ^ { 2 } } { \pi _ { 2 } } \rceil + \lceil \frac { ( n + 1 ) - { \pi } _ { 3 } ^ { 2 } } { \pi _ { 3 } } \rceil + \cdots + \lceil \frac { ( n + 1 ) - { \pi } _ { k } ^ { 2 } } { \pi _ { k } } \rceil } } \\ { { \displaystyle  \qquad = \lceil \frac { n - 3 } { 2 } \rceil + \lceil \frac { n - 8 } { 3 } \rceil + \lceil \frac { n - 2 4 } { 5 } \rceil + \cdots + \lceil \frac { ( n + 1 ) - { \pi } _ { k } ^ { 2 } } { \pi _ { k } } \rceil } } \end{array}
$$

There are $\lceil ( n - 3 ) / 2 \rceil$ multiples of 2 in the range 4 through $n$ ， $\lceil ( n - 8 ) / 3 \rceil$ multiples of 3 in the range 9 through $n$ ,and so on. For $n = 1 { , } 0 0 0$ the sum is 1,411.

Now let’s think about the time taken by the parallel algorithm. Whenever a processor is unoccupied, it grabs the next prime and marks its multiples. All processors continue in this fashion until the first prime greater than $\sqrt { n }$ is found.For example,Fig.1-9 illustrates the time required by one, two,and three processors to find all primes less than or equal to 1,0oo. With two processors the parallel algorithm has speedup 2 (1,411/706). With three processors the parallel algorithm has speedup 2.83 (1,411/499). It is clear that the parallel execution time will not decrease if more than three processors are used, because with three or more processors the time needed for a single processor to sieve all multiples of 2 determines the parallel execution time. Hence an upper bound on the execution time of the parallel algorithm for $n = 1 , 0 0 0$ is 2.83.

Increasing $n$ does not significantly raise the upper bound on speedup imposed by a single processor striking all multiples of 2 (see Prob. 1-10).

# 1.4.2 Data-Parallel Approach

Let's consider another approach to parallelizing the Sieve of Eratosthenes. In our new algorithm,processors will work together to strike multiples of each newly found prime. Every processor will be responsible for a segment of the array representing the natural numbers. The algorithm is data parallel, because each processor applies the same operation (striking multiples of a particular prime) to its own portion of the data set.

Time   

<table><tr><td>0</td><td>100 ）2003004005006007008009001,000 1,100 1,200 1,300 1,400 1,500</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(a)</td><td></td><td>2</td><td>3</td><td>5</td><td>7</td><td>11 13</td><td>23 .29 1719 -31</td></tr></table>

![](images/27dfd2e1bb3250add7932810a2e5428f561ead7602b1a89c92f45a13775e706a.jpg)

![](images/33c394919c8cb3ceddbd287cceac7f12f02c2b59328bd4b22d68aeea72d7cd0b.jpg)  
FIGURE 1-9 Study of how adding processors reduces the execution time of the control-parallel Sieve of Eratosthenes algorithm when $n = 1 , 0 0 0$ .The number in the bar represents the prime whose multiplesare beingmarked.The length of the bar is the time needed to strike thesemultiples.(a) Single processor strikes out allcomposite numbers in1,411 units of time.(b) With two processors execution time drops to 706 time units. (c) With three or more processors execution time is 499 time units, the time needed for a processor to strike all multiples of 2.

Analyzing the speedup achievable by the data-parallel algorithm on the shared memory model of Fig. 1-8b is straightforward; we have left it as an exercise. Instead, we will consider a different model of parallel computation (Fig.1-10). In this model there is no shared memory,and processor interaction occurs through message passing.

Assume we are solving the problem on $p$ processors. Every processor is assigned no more than [n/p] natural numbers. We will also assume that p is much less than √n. In this case all primes less than √n,as well as the first prime greater than √n, are in the list of natural numbers controlled by the first processor. Processor 1 will find the next prime and broadcast its value to the other processors. Then all processors strike from their lists of composite numbers all multiples of the newly found prime. This process of prime finding and composite number striking continues until the first processor reaches a prime greater than $\sqrt { n }$ ， at which point the algorithm terminates.

Let's estimate the execution time of this parallel algorithm. As in the previous analysis, we ignore time spent finding the next prime and focus on the time spent marking composite numbers. However, since this model does not have a shared memory，we must also consider the time spent communicating the value of the current prime from processor 1 to all other processors.

![](images/0b8c85e727b07155c64bf3d8c8a65f28cc4d703861a650f79a3773a678c5bfba.jpg)  
FIGURE1-10 Private memory model for parallel Sieve of Eratosthenes algorithm. (a) Sequential algorithmmaintainsarray of natural numbers,variable storing current prime,and variable storing index of loopiterating througharray of natural numbers. (b) inparallel model each processor has its own copy of the variables containing the current prime and the loopindex.Processor1 finds primesand communicates them to the other processors. Each processor iterates through itsownportion of the array of natural numbers,marking multiples of the prime.

Assume it takes X time units for a processor to mark a multiple of a prime as being a composite number. Suppose there are k primes less than or equal to√n. We denote these primes π1,π2,..,πk. The total amount of time a processor spends striking out composite numbers is no greater than

$$
\left( \left\lceil \frac { \lceil n / p \rceil } { 2 } \right\rceil + \left\lceil \frac { \lceil n / p \rceil } { 3 } \right\rceil + \left\lceil \frac { \lceil n / p \rceil } { 5 } \right\rceil + \dots + \left\lceil \frac { \lceil n / p \rceil } { \pi _ { k } } \right\rceil \right) x
$$

Assume every time processor 1 finds a new prime it communicates that value to each of the other p-1 processors in turn. If processor 1 spends λ time units each time it passes a number to another processor, its total communication time for all $k$ primes is $k ( p - 1 ) \lambda$

To bring this discussion down to earth, suppose we want to count the number of primes less than 1,00o,0oo.It turns out that there are 168 primes less than 1,000, the square root of 1,000,000. The largest of these is 997. The maximum possible execution time spent striking out primes is

$$
\left( \left\lceil \frac { \lceil 1 , 0 0 0 , 0 0 0 / p \rceil } { 2 } \right\rceil + \left\lceil \frac { \lceil 1 , 0 0 0 , 0 0 0 / p \rceil } { 3 } \right\rceil + \dots + \left\lceil \frac { \lceil 1 , 0 0 0 , 0 0 0 / p \rceil } { 9 9 7 } \right\rceil \right) x
$$

![](images/ad7ea99b7f4c3079f13dbc7516e8d0679d00ab5c78437a99ac7dd85cafb61d92.jpg)  
FIGURE 1-11 Estimated speedup of the data-parallel Sieveof Eratosthenesalgorithm, assuming that $\eta = 1 , 0 0 0 , 0 0 0$ and $\lambda = 1 0 0 x$ .Note that speedup is graphed as a function of number of processors used. This is typical.

The total communication time is $1 6 8 ( p - 1 ) \lambda$

If we know the relation between $\chi$ and $\lambda$ , we can plot an estimated speedup curve for the parallel algorithm. Suppose $\lambda = 1 0 0 \chi$ . Figure 1-11 illustrates the estimated speedup of the data-parallel algorithm.

Notice that speedup is not directly proportional to the number of processors used. In fact, speedup is highest at 11 processors. When more processors are added, speedup declines.Figure 1-12 illustrates the estimated total execution time of the parallel algorithm along with its two components: computation time and communication time. Computation time is inversely proportional to the number of processors used, while communication time increases lineariy with the number of processors used. After 11 processors, the increase in communication time is greater than the decrease in computation time, and the total execution time begins to increase.

![](images/b1a8bb7e497f3729ead5255d11c1fd8c550cfe2ae0c5e74e7dc2ed62011bccdb.jpg)  
FIGURE 1-12 Total execution time of the data-parallel Sieve of Eratosthenesalgorithm is the sum of the time spent computing and the time spent communicating. Computation time isinversely proportional to the numberof processors;communication time is directly proportional to the number of processors.

# 1.4.3 Data-Parallel Approach with I/O

The prime-finding algorithms we have described are unrealistic, because they terminate without storing their results. Let's examine what happens when we execute a data-parallel implementation of the Sieve of Eratosthenes incorporating output on the shared-memory model of parallel computation.

The augmented shared memory model appears in Fig. 1-13. Assume only one processor at a time can access the I/O device. Let $i \beta$ denote the time needed for a processor to transmit $i$ prime numbers to that device.

Let's predict the speedup achieved by the data-parallel algorithm that outputs all primes to the I/O device. Suppose $n = 1 , 0 0 0 , 0 0 0$ There are 78,498 primes less than 1,0oo,ooo.To find the total execution time, we take the total computation time,

$$
\left( \left\lceil \frac { \lceil 1 , 0 0 0 , 0 0 0 / p \rceil } { 2 } \right\rceil + \left\lceil \frac { \lceil 1 , 0 0 0 , 0 0 0 / p \rceil } { 3 } \right\rceil + \dots + \left\lceil \frac { \lceil 1 , 0 0 0 , 0 0 0 / p \rceil } { 9 9 7 } \right\rceil \right) x
$$

and add to it the total I/O time, $^ { 7 8 , 4 9 8 \beta }$

The solid curve in Fig. 1-14 ilustrates the expected speedup of this parallel algorithm for $1 , 2 , \ldots , 3 2$ processors, assuming that $\beta = \chi$ .Figure 1-15 illustrates the two components of the paralel execution time: computation time and output time. Because output to the I/O device must be performed sequentially, it puts a damper on the speedup achievable through parallelization. Amdahl's law is a way of expressing maximum speedup as a function of the amount of parallelism and the fraction of the computation that is inherently sequential.

![](images/31dd0b87f1658f255503100e928e4505d809d2da8a52edb592a31db4cea9facd.jpg)

![](images/0524e66e84c39510e74f89ecabd2e830296a9a1cfa7277195ccaa9a560947f03.jpg)  
FIGURE 1-14 Expected speedup of data-parallel Sieve of Eratosthenes algorithm that outputs primes to an $1 / \sigma$ device. Solid curve is speedup predicted from analysis.Dashed curve ismaximum speedupasdetermined by Amdahl's law. This graph is for the case when $\eta = 1 , 0 0 0 , 0 0 0$ and $\beta { = } \chi$

![](images/76e476a435a3b990a298f24886947f98ae81cbc3e878f597cf75a9829c2ef5d8.jpg)  
Total execution time of data-parallel outputproducing Sieve of Eratosthenesalgorithm asa function of its two components, computation time and $1 / 0$ time. This graph is for the case when $n = 1 , 0 0 0 , 0 0 0$ and $\beta = \chi$

Amdahl’s law (Amdahl 1967). Let $f$ be the fraction of operations in a computation that must be performed sequentially,where $0 ~ \leq ~ f ~ \leq ~ 1$ .The maximum speedup $s$ achievable by a parallel computer with $p$ processors performing the computation is

$$
S \leq { \frac { 1 } { f + ( 1 - f ) / p } }
$$

For example, consider the algorithm we have just explored. When $n =$ 1,000,000, the sequential algorithm marks 2,122,048 cells and outputs 78,498 primes. Assuming these two kinds of operations take the same amount of time, the total sequential time is 2,200,546, and $f = 7 8 { , } 4 9 8 / 2 { , } 2 0 0 { , } 5 4 6 = . 0 3 5 7$ An upper bound on the speedup achievable by a parallel computer with $p$ processors is

$$
\frac { 1 } { . 0 3 5 7 + . 9 6 4 3 / p }
$$

The dotted curve in Fig. 1-14 plots the upper bound on the speedup of the algorithm as predicted by Amdahl’s law.

Often，as the size of the problem increases,the fraction $f$ of inherently sequential operations decreases, making the problem more amenable to parallelization. This phenomenon--called the Amdahl effect—is true for the application we have been considering. Figure 1-16 plots $f$ as a function of $n$ for the data-parallel sieve algorithm with output, assuming $\beta = \chi$ ·

FIGURE 1-16 Fraction $f$ of inherently sequential operationsindata-parallel sievealgorithm with output,as a function of $n$ the size of the list of natural numbers,assuming $\beta = \chi$ ·

![](images/d7d7f3a6baf6d60c8840d1ced362da300238032e1edaeb9275bf997671d6d059.jpg)

# 1.5 SUMMARY

Solving many important scientific problems demands computation rates that far exceed the capabilities of today's supercomputers.Because the speed of the fastest single processors is increasing more slowly than the speed of microprocessors,constructing supercomputers out of collections of microprocessors appears to be the surest route to achieving the incredibly high performance demanded by these problems.

Parallel algorithms can be categorized as either data parallel or control parallel. Data parallelism is the use of multiple functional units to apply the same operation to different elements of a data set. Control parallelism is achieved through the simultaneous application of different operations to different data elements. The flow of data among control-parallel processes may be complex. If the flow graph forms a simple, directed path,then we say the algorithm is pipelined. Scalable algorithms are desirable, because they permit larger prob-Iems to be solved on more massively parallel machines.As a rule,data-parallel algorithms are more scalable than control-parallel algorithms, because the level of control parallelism is usually a constant, independent of the problem size, while the level of data parallelism is an increasing function of the problem size.

In our examination of parallel algorithms to implement the Sieve of Eratosthenes,we encountered some typical design problems. In the control-parallel algorithm targeted toa shared-memory model,we saw problems that can result from the uncontrolled parallel access to shared resources. In the data-parallel algorithm targeted to a private-memory model, we saw that by increasing processors we increase the communication overhead of the parallel algorithm. Eventually the increase in communication time exceeds the decrease in computation time brought about by adding processors. When this point is reached, adding more processors increases, rather than decreases, total execution time.

In our third parallel algorithm we saw how a sequential component-in this case the time needed to access an output device-can put a damper on the speedup achievable through parallelization. Amdahl's law expresses maximum speedup as a function of the inherently sequential component and the number of processors executing a parallel algorithm. However, an ameliorating factor is that as the size of the problem increases, inherently sequential operations constitute a smaller fraction of the total computation, making the problem more amenable to parallelization.

# 1.6 BIBLIOGRAPHIC NOTES

All the references in this book can be found in the Bibliography at the end of the text.

Since the first edition of this book appeared in 1987,several other textbooks devoted to parallel algorithms and/or parallel computing have entered the market. These texts include Akl (1989), Anderson (1989), JaJa (1992), Lakshmivarahan and Dhall(1990),Leighton (1992),and Lewis and El-Rewini (1992).Besides providing different perspectives on parallel computing,these texts can also serve as a source of additional exercises.

Other books that devote attntion to parallel algorithms include Evans (1982). Fox et al. (1988), and Jamieson et al. (1987).

The Turing lecture of Cocke (1988) discusses efforts to improve computer performance and includes his prediction that “the search for future scientific computing performance has to concentrate on gross parallelism.” Another look into the future of high performance computers has been written by Bell (1989).

Hillis and Steele (1986, 1987) discuss data-parallel algorithms.

Several authors have described parallel implementations of the Sieve of Eratosthenes. Bokhari (1987) describes a control-parallel implementation that achieves modest speedup.Lansdowne et al. (1987) point out the weaknesses in Bokhari'salgorithm and describe the implementation of a data-parallel version. Beck and Olien (1989) have implemented the algorithm of Lansdowne et al. (1987) on the Sequent Balance. Carriero and Gelernter (1989a) have compared several C-Linda implementations of the Sieve of Eratosthenes.

In the past, a number of arguments have been proposed against the merits of high-level parallelism. For instance,Grosch's law states that the speed of computers is proportional to the square of their cost (Grosch 1953, 1975). Modern studies of the price and performance of computer systems seem to indicate that Grosch's law no longer holds (Kang et al. 1986; Mendelson 1987).

Another argument against massive parallelism is Minsky's conjecture, which states that the speedup achievable by a parallel computer increases as the logarithm of the number of processing elements, thus making large-scale parallelism unproductive (Minksy and Papert 1971). In this book we will provide many examples to disprove Minsky's conjecture.

Developments in parallel computer architectures and parallel algorithms continue at an increasing pace. Journals and magazines regularly containing articles on parallel computing include Communications of the ACM; Computer; Concurrency:Practice and Experience;Future Generations Computer Systems; IEEE Transactions on Computers; IEEE Parallel and Distributed Technology: Systems and Applications;IEEE Transactions on Parallel and Distributed Systems; IEEE Transactions on Software Engineering; International Journal of Parallel Programming;Journal of Parallel Algorithms and Applications;Journal of Parallel and Distributed Computing;New Generation Computing; and Parallel Computing.

Conferences encompassing theoretical and/or practical aspects of parallel computing include the Annual Symposium on Foundations of Computer Science,the Annual Symposium on Computer Architecture, the Annual Symposium on Theory of Computing, Frontiers of Massively Parallel Computation, the International Conference on Parallel Processing, the International Parallel Processing Symposium, the SIAM Conference on Parallel Processing for Scientific Computing, Supercomputing ${ \mathfrak { s } } _ { X }$ ,and the Symposium on Principles and Practice of Parallel Programming.

1-1 Try this experiment with a few friends. Shuffle a deck of cards,then determine how long it takes one person to sort the cards into the order Ad, $2 \spadesuit$ ,...,K., A, $2 \heartsuit$ ...,K,A&, $^ { 2 \clubsuit }$ ....,K&, $_ { \mathrm { A } \diamondsuit }$ $2 \diamond$ $\mathrm { K } \diamond$ .(Is it faster to sort the cards initially by suit or by value?) How long does it take $p$ people to sort $p$ decks of shuffled cards? How long does it take $p$ people to sort one deck of cards? Try this experiment for $p = 1 , 2 , \ldots , 6$

1-2 You have been assigned the task of computing the sum of one thousand 4-digit numbers as rapidly as possible. You hold in your hands a stack of 1,ooo index cards,each containing a single number,and you are in charge of 1,ooo expert accountants,each siting at a desk in a cavernous room. Each accountant has a calculator.

a Describe a fast method of distributing cards to accountants.   
b Describe a fast method of accumulating the subtotals generated by the active accountants into a grand total.   
c Draw a graph that plots your best estimate of the time needed to compute the grand total as a function of the number of accountants you choose to use.   
d Add another curve to the graph you drew in part c,estimating the time needed to compute the grand total of 10.000 numbers, given 1,.,1000 accountants.   
e Draw a speedup chart that plots speedup achieved on the two addition problems in parts c and d as a function of number of accountants.   
f Explain why speedup does not reach 1,0oo in either case.

1-3Given a task that can be divided into $m$ subtasks,each requiring 1 unit of time how much time is required for an $m$ stage pipeline to process $n$ tasks?

1-4 How many widgets must the pipelined widget-assembly machine of Fig. 1-4b assemble inorder toachieve a speedup of 3 over the sequential machine? Justify youranswer.

1-5 How many widgets must the parallel widget-assembly machine of Fig. 1-4c assemble in order to achieve a speedup of 3 over the sequential machine? Justify your answer.

1-6 Consider a parallel pipelined widget-assembly machine with three pipelines, each pipeline having three segments. Draw the speedup curve for this machine for $1 , \ldots , 1 0$ widgetsassembled.

1-7A copy machine's feeder tray holds pages to be copied. Assume it takes 5 seconds to load a group of pages into the feeder before copying and 10 seconds to unload the originals and the copies after copying. If the copier takes 4 seconds to print a page and 1 second to print every subsequent page, what is the minimum capacity of the feeder tray necessary to ensure that the effective throughput of the copier asymptotically approaches 40 pages per minute as the length of the original document increases?

1-8 The task graph shown in Fig. 1-17 represents an image processing application. Each bubble represents an inherently sequential task. There are 12 tasks: an input task, 10 computation tasks, and an output task. Each of the 12 tasks can be accomplished in 1 unit of time on one processor. The input task must complete before any computational tasks begin. Likewise, all 10 computational tasks must complete before the output task begins. The input task consumes the entire bandwidth of the input device. The output task consumes the entire bandwidth of the output device.

a What is the maximum speedup that can be achieved if this problem is solved on two processors? (Hint: Processors do not have to receive the message elements in order.)   
b What is an upper bound on the speedup that can be achieved if this problem is solved with parallel processors?   
c What is the smallest number of processors sufficient to achieve the speedup given in part b?   
d What is the maximum speedup that can be achieved solving five instances of this problem on two processors? Continue to assume that there is one input device and one output device.   
e What is an upper bound on the speedup that can be achieved solving 100 instances of this problem with parallel processors? Continue to assume that there is one input device and one output device.   
f What is the smallest number of processors suficient to achieve the speedup given in part e?

![](images/01e6709744a9cb73a08e83e5e24ff336e34174341ae889d28ad6b53a96712db1.jpg)

1-9 Imagine a computer with p processors,each connected with every other processor by two unidirectional communication channels. (A four-processor system is shown in Fig.1-18.) Suppose for any two processors i and j,it takes k units of time for processor i to send a k-element message to processor j, for all k ≥ 0. In addition, suppose every processor has the ability to sendand receive different messages concurrently on all its communication channels without slowing the communication rate on any channel. Determine how long it takes for an n-element message to be communicated from a single processor to every other processor in the network. In other words, how long does it take for one processor to broadcast an $n$ -element message to the other $p - 1$ processors? (Hint: Processors do not have to receive the message elements in order.)

![](images/229519bf41288284ae60db46a2c5c1da375459722c46e65f07ae0383b17d01d7.jpg)

1-10 A sequential implementation of the Sieve of Eratosthenes marks about $2 . 2 \ \mathrm { m i l }$ lion cells in order to compute all primes less than 1 million. Estimate the maximum speedup achievable by the control-parallel version of the Sieve of Eratosthenes as it finds all primes less than 1 million.

1-11 Figure 1-11 illustrates the estimated speedup of the data-parallel Sieve of Eratosthenes algorithm,assuming that $n = 1 , 0 0 0 , 0 0 0$ and $\lambda = 1 0 0 \chi$ . Augment this figure with two additional speedup curves, one for the case where $\lambda = 1 0 \chi$ and one for the case where $\lambda = 1 , 0 0 0 \chi$ .Assume $n$ is unchanged.

1-12 Estimate the speedup achievable by $1 , 2 , \ldots , 1 6$ processors executing the dataparallel Sieve of Eratosthenes program a for $n = 1 , 0 0 0$ ,assuming the parallel model of Fig.1-10 and $\lambda = 1 0 0 \chi$ $\mathbf { b }$ for $n = 1 , 0 0 0$ , assuming the parallel model of Fig. 1-8.

1-13 Assume the communication network connecting the processors in Fig. 1-10b supports concurrent message passing. Propose a method faster than that described in this book for processor 1 to broadcast prime numbers to all other processors. Analyze the execution time and speedup on $1 , 2 , \ldots , 1 6$ processors of the new parallel algorithm,assuming $n = 1 , 0 0 0 , 0 0 0$ and $\lambda = 1 0 0 \chi$ ·

1-14 The series of broadcast operations performed by the data-parallel Sieve of Eratosthenes algorithm on the model of Figure 1-1Ob can be reduced to a single broadcast operation. Processor 1 can compute all primes less than or equal to $\sqrt { n }$ and broadcast the entire list of values at once. Then every processor uses this list of primes to sieve its own set of,at most, $\lceil n / p \rceil$ values. No further communication is required. Assume it takes $\lambda + i \beta$ time units for a processor to send a message containing $i$ prime numbers to another processor. Assume that $\lambda = 1 0 0 \beta$ .For $n = 1 , 0 0 0 , 0 0 0$ and $p = 1 6$ ,what is the smallest value of $\lambda$ for which this single broadcast parallel algorithm is superior to the multiple broadcast algorithm?

1-15 Since 2 is the only even prime,one way to save memory and improve the speed of the sequential Sieve of Eratosthenes algorithm is to have the elements of the boolean array represent only odd numbers.In this scheme the first sieve step would mark multiples of the prime number 3.

a Estimate the reduction in execution time of the sequential algorithm resulting from this improvement for $n = 1 , 0 0 0$ and $n = 1 , 0 0 0 , 0 0 0$   
b The improved sequential algorithm can be used as the basis for an improved data-paralel algorithm. Using the machine model of Fig.1-10b and assuming $\lambda = 1 0 0 \chi$ ,estimate the execution time of the improved data-parallel algorithm for $1 , 2 , \ldots , 1 6$ processors. Compute the speedup of the improved data-parallel algorithm over the improved sequential algorithm. Compare this speedup with the speedup estimated for the original data-parallel algorithm.   
d Why does the improved data-parallel algorithm achieve lower speedup than the original data-parallel algorithm?   
e Now that a better sequential algorithm exists, should the speedup figures in this chapter be modified?

1-16 In the control-parallel Sieve of Eratosthenes algorithm, a single processor is responsible for sieving all multiples of 2. For $n = 1 , 0 0 0$ ，sieving all multiples of 2 represents $35 \%$ of the total number of operations performed. By Amdahl's law the maximum speedup that can be achieved with $f = . 3 5$ and $p = 2$ is $1 / ( . 3 5 + . 6 5 / 2 ) = 1 . 4 8$ ,yet our analysis showed a speedup of 2 with 2 processors.Where is the flaw in our reasoning?

1-17 Prove that if $( 1 / k ) \mathrm { t h }$ of the time spent executing an algorithm involves operations that must be performed sequentially, then an upper limit on the speedup achievable by executing the algorithm on parallel processors is $k$

1-18 Name an algorithm (other than the Sieve of Eratosthenes) where the computationa requirements grow faster than the IO requirements. Name an algorithm where the computational requirements grow slower than the I/O requirements.

1-19.Define the following: microsecond $( \mu \mathbf { s } )$ ,millisecond (ms)，nanosecond (ns), picosecond (ps), gigabyte (Gbyte), megabyte (Mbyte), and terabyte (Tbyte). A nanosecond istoa second asa second is to how many years?

1-20 If manufacturers of massively parallel computers are increasing the top perfor mance of their systems by a factor of 10O every 5 years,how long does it take forperformance to double?

1-21 Assume an implementation of the numerical ocean model described in Sec. 1.1 performs 30 billion floating-point operations to simulate 10 minutes of global ocean circulation.

a How many floating-point operations are needed to simulate 10 years of global ocean circulation?   
b At what rate must the 1O-year simulation execute, if it is to complete in 15 hours, e.g.,between $5 \ \mathbf { p . M }$ and 8 A.M.?   
c Assume that this application currently executes on a microprocessor-based parallel computer at the rate of 10 billion floating-point operations per second. If such architectures keep increasing in speed one-hundredfold every 5 years, when will a massively parallel supercomputer be capable of the execution rate computed in part b?

# 2

Perhaps some day students of algorithms and programming will see sequential computers as the exception,rather than the rule. Today,however,most students carry preconceived notions about algorithms and data structures from their experiences on sequential machines. New problem-solving techniques are needed in order to take full advantage of the power of parallel hardware.

This chapter provides a mental break from the von Neumann model and sequential algorithms. Our vehicle is the PRAM (parallel random access machine, pronounced “pea ram") model of parallel computation. The PRAM model allows parallel-algorithm designers to treat processing power as an unlimited resource,much as programmers of computers with virtual memory are allowed to treat memory as an unlimited resource. The PRAM model is unrealistically simple; it ignores the complexity of interprocessor communication. Because communication complexity is not an issue, the designer of PRAM algorithms can focus on the parallelism inherent in a particular computation.

For some important algorithms, such as reduction, cost-optimal PRAM solutions exist, meaning that the total number of operations performed by the PRAM algorithm is of the same complexity class as an optimal-sequential algorithm. In Chap. 6 we demonstrate how cost-optimal PRAM algorithms can serve as a foundation for efcient algorithms on real parallel computers.

This chapter begins with a review of the standard RAM model of sequential computation. Section 2.2 describes the PRAM model of parallel computation. In Sec.2.3 we present five PRAM algorithms and analyze their complexity. We discuss Brent's theorem, used to determine when the number of processors used in a PRAM algorithm can be reduced without increasing the time complexity in Sec 2.4. In Sec. 2.5,we relate the PRAM model to complexity theory.

# 2.1 A MODEL OF SERIAL COMPUTATION

The random access machine (RAM) is a model of a one-address computer. A RAM consists of a memory, a read-only input tape, a write-only output tape, and a program (Fig. 2-1). The program is not stored in memory and cannot be modified. The input tape contains a sequence of integers. Every time an input value is read, the input head advances one square. Likewise, the output head advances after every write. Memory consists of an unbounded sequence of registers, designated $r _ { 0 } , r _ { 1 } , r _ { 2 } , \ldots$ Each register can hold a single integer. Register $r _ { 0 }$ is the accumulator, where computations are performed.

The exact instructions are not important, as long as they resemble the instructions found on an actual computer. Hence a RAM should have instructions along the linesof load, store,read,write,dd, subract,multiplydivide,tet, jump, and halt.

The worst-case time complexity of a RAM program is the function $f ( n )$ ， the maximum time taken by the program to execute over all inputs of size $n$ . The expected time complexity of a RAM program is the average, overall inputs of size $n$ , of the execution times. Analogous definitions hold for worstcase space complexity and expected space complexity by substituting the word “space" for “time”in the above definitions.

![](images/1057d65cbf3260f468f1ae1cce997d98905abec8aa92a7703d6bc145a4b26ad7.jpg)  
FIGURE 2-1The randomaccessmachine (RAM) model of serial computation.(Aho,Hopcroft,and UIIman 1974.)

There are two ways of measuring time and space on the RAM model. The uniform cost criterion says each RAM instruction requires one time unit to execute and every register requires one unit of space. The logarithmic cost criterion takes intoaccount that anactual word of memory hasa limited storage capacity.The uniform cost criterion is appropriate if the values manipulated by the program always fit into one computer word. That is always the case in this text; hence we always use the uniform cost criterion when computing time and space complexity.

# 2.2 THE PRAM MODEL OF PARALLEL COMPUTATION

A PRAM consists of a control unit, global memory,and an unbounded set of processors, each with its own private memory (Fortune and Wyllie 1978) (see Fig. 2-2). Although active processors execute identical instructions,every processor has a unique index, and the value of a processor's index can be used to enable or disable the processor or influence which memory location it accesses.

A PRAM computation begins with the input stored in global memory and a single active processing element. During each step of the computation an active,enabled processor may read a value from a single private or global memory location, perform a single RAM operation,and write into one local or global memory location. Alternatively, during a computation step a processor may activate another processor. All active, enabled processors must execute the same instruction,albeit on different memory locations. The computation terminates when the last processor halts.

Definition 2.1. The cost of a PRAM computation is the product of the parallel time complexity and the number of processors used. For example,a PRAM algorithm that has time complexity $\Theta ( \log p )$ using $p$ processors has cost $\Theta ( p \log p )$ ·

![](images/529d5a63f257656a3185304a4ad8e480200118efc68b9097c77d939ad04f689e.jpg)  
FIGURE 2-2 The PRAM model of parallel computation.

Various PRAM models differ in how they handle read or write conflicts; i.e.,when two or more processors attempt to read from, or write to, the same global memory location. Most of the results in the research literature have been based upon one of the following models (Li and Yesha 1989):

1 EREW (Exclusive Read Exclusive Write): Read or write conflicts are not allowed.

2 CREW (Concurrent Read Exclusive Write): Concurrent reading allowed; i.e., multiple processors may read from the same global memory location during the same instruction step. Write conflicts are not allowed. (This is the default PRAM model.)

3 CRCW (Concurrent Read Concurrent Write): Concurrent reading and concurrent writing allowed. A variety of CRCW models exist with different policies for handling concurrent writes to the same global address. We list three different models:

a. COMMON. All processors concurrently writing into the same global address must be writing the same value.   
b. ARBITRARY. If multiple processors concurrently write to the same global address,one of the competing processors is arbitrarily chosen as the “winner,"” and its value is written into the register.   
c. PRIORITY. If multiple processors concurrently write to the same global address,the processor with the lowest index succeeds in writing its value into the memory location.

Let us examine the relative strengths of these models. The EREW PRAM model is the weakest. Clearly a CREW PRAM can execute any EREW PRAM algorithm in the same amount of time; the concurrent read facility is simply not used. Similarly,a CRCW PRAM can execute any EREW PRAM algorithm in the same amount of time.

The PRIORITY PRAM model is the strongest. Any algorithm designed for the COMMON PRAM model will execute with the same complexity on the ARBITRARY PRAM and PRIORITY PRAM models as well, for if all processors writing to the same location write the same value, choosing an arbitrary processor would cause the same result. Likewise, if an algorithm executes correctly when an arbitrary processor is chosen as the “winner,” the processor with the lowest index is as reasonable an alternative as any other. Henceany algorithm designed for the ARBITRARY PRAM model willexecute with the same time complexity on the PRIORITY PRAM model.

Because the PRIORITY PRAM model is stronger than the EREW PRAM model,analgorithm tosolvea problem on the EREW PRAMcanhave higher time complexity than an algorithm solving the same problem on the PRIORITY PRAM model. Theorem 2.1 quantifies the increase in parallel time complexity that can occur when moving from the PRIORITY PRAM model to the EREW PRAM model. First, we state a lemma proven by R. Cole.

Lemma 2.1. (Se Cole [1988].) A $p$ -processor EREW PRAM can sort a $p$ -element array stored in global memory in $\Theta ( \log p )$ time.

Theorem 2.1. (See Eckstein [1979], Vishkin [1983].）A $p$ -processor PRIORITY PRAM can be simulated by a $p$ -processor EREWPRAMwith thetimecomplexity increased by a factor of $\Theta ( \log p )$ ·

Proof. Assume the PRIORITY PRAM algorithm uses processors $P _ { 1 } , P _ { 2 } , \ldots , P _ { p }$ and global memory locations $M _ { 1 } , M _ { 2 } , \ldots , M _ { m }$ The EREW PRAM usesauxiliary global memory locations $T _ { 1 } , T _ { 2 } , \ldots , T _ { p }$ and $S _ { 1 } , S _ { 2 } , \ldots , S _ { p }$ to simulate each read or write step of the PRIORITY PRAM. See Fig. 2-3.When processor $P _ { i }$ in the PRIORITY PRAM algorithm accesses memory location $M _ { j }$ ,processor $P _ { i }$ in the EREW PRAM algorithm writes the ordered pair $( j , i )$ in memory location $T _ { i }$ . Then the EREW PRAM sorts the elements of $T$ . This step takes time $\Theta ( \log p )$ (Lemma 2.1). By reading adjacent entries in the sorted array, the highest priority processor accessing any particular location can be found in constant time. Processor $P _ { 1 }$ readsmemory location $T _ { 1 }$ ,retrieves the ordered pair $( i _ { 1 } , j _ { 1 } )$ ,and writes a 1 into global memory location $S _ { j _ { 1 } }$ . The remaining processors $P _ { k }$ ,where $2 \le k \le p$ ，first read memory location $T _ { k }$ and then read memory location $T _ { k - 1 }$ . If $i _ { k } \neq i _ { k - 1 }$ ， then processor $P _ { k }$ writes a 1 into $S _ { j _ { k } }$ .Otherwise, processor $P _ { k }$ writes a O into $S _ { j _ { k } }$ . At this point the elements of S with value1 correspond to the highest priority processors accessing each memory location.

# FIGURE 2-3

A concurrent write operation, which takes constant time on a $p$ -processOr PRIORITY PRAM,canbe simutd in $\Theta ( \log { p } )$ time ona $p$ -processorEREWPRAM.(a) Concurrent writeon the PRIORITY PRAM model.Processors $P _ { 1 }$ ， $P _ { 2 }$ ,and $P _ { 4 }$ attempt to write values tomemory location $M _ { 3 }$ .Processor $P _ { 1 }$ wins.Processors $P _ { 3 }$ and $P _ { 5 }$ attempt to write values to memory location $M _ { 7 }$ .Processor $P _ { 3 }$ wins. (b) To simulate concurrent write on the EREWPRAMmodel，each processor writesan (address,processor number) pair toa unique element of $\tau$ .The processors sort $\tau$ intime $\Theta ( \log { p } )$ .Inconstant time processors can set to 1 those elements of $s$ corresponding to the winning processors. (c) Winning processors write their values.

![](images/0f9258045a2d1f4c625875b40b16fe7d542f8166a9f932a4502abfa98a5b91a2.jpg)

Fora write instruction, the highest priority processor accessing each memory location writes its value. For a read instruction, the highest priority processor accessing each memory location reads that location's value, then duplicates the value in $O ( \log p )$ time so there is a copy in a unique memory location for every processor to access the value.

# 2.3 PRAM ALGORITHMS

If a PRAM algorithm has lower time complexity than an optimal RAM algorithm, it is because parallelism has been used. Because a PRAM algorithm begins with only a single processor active, PRAM algorithms have two phases. In the first phase a sufficient number of processors are activated,and in the second phase these activated processors perform the computation in parallel.

Given a single active processor, it is easy to see that $\lceil \log p \rceil$ activation steps are both necessary and sufficient for $p$ processors to become active, since the number of active processors can double by excuting a single instruction (Fig. 2-4). Unless otherwise noted, all logarithms in this book are to base 2. In our presentation of PRAM algorithms we use the meta-instruction

spawn (<processor names>)

to denote this logarithmic time generation of processors from a single active processor.

To make the second phase PRAM algorithm computations easier to read, we allow references to global registers to be array references.We assume there is a mapping from these array references to the appropriate global registers.

# FIGURE 2-4

Exactly $\lceil \mathsf { I o g } p \rceil$ processor activation steps are necessary and suffcient tochange from 1 active processor to $p$ active processors.

![](images/5109cdfea6e363c7a8f3e02788d58048ff7f4b23f7e2e8aac0d50c5c58b28e51.jpg)  
Active processors

The construct

# for all <processor list> do $<$ {statement list>endfor

denotes a code segment to be executed in parallel by allthe specified processors.

Besides the special constructs already described,we express PRAMalgorithms using the familiar control structures if ...then ...else ...endif, for ...endfor， while ...endwhile, and repeat ...until. The symbol denotes assignment.

In the remainder of this section we present problems and solutions using the PRAM model.

# 2.3.1 Parallel Reduction

The binary tree is one of the most important paradigms of parallel computing (Fig. 2-5). In some algorithms data flows top-down from the root of the tree to the leaves.Broadcast and divide-and-conquer algorithms both fit this model. In broadcast algorithms the root sends the same data to every leaf. In divide-andconquer algorithms the tree represents the recursive subdivision of problems into subproblems.

In other algorithms data flows bottom-up from the leaves of the tree to the root. These are called fan-in or reduction operations.

More formally, given a set of $n$ values $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ and an associative binary operator $\oplus$ ,reduction is the process of computing $a _ { 1 } \oplus a _ { 2 } \oplus \cdots \oplus a _ { n }$

Parallel summation is an example of a reduction operation.

The processors in a PRAM manipulate data stored in global registers. To implement the summation algorithm illustrated in Figure 2-5,we represent each tree node with an element in an array. The mapping from the tree to the array is straightforward. Figure 2-6 illustrates how an array-based PRAM algorithm finds the sum of $n$ values. Pseudocode for this algorithm appears in Fig. 2-7.

Let us analyze the complexity of this algorithm. The spawn routine requires $\lceil \log \lfloor n / 2 \rfloor \rceil$ doubling steps. The sequential for loop executes $\lceil \log n \rceil$ times,and each iteration has constant time complexity. Hence the overall time complexity of the algorithm is $\Theta ( \log n )$ ,given $\lfloor n / 2 \rfloor$ processors.

![](images/2bbe7f3799fd4fcd88f5a78630470b4a39df5f76b5a455b364c367fa7e9a3829.jpg)  
FIGURE 2-5 Parallel summation is an example of a reduction operation. Parallel reduction can be representedbya binary tree. A group of n valuescan be added in 「log n] parallel addition steps.

![](images/6e86cbb0a9cc76b31a04b5f63041cee584bbbc6156b9f9e2f3e136aac8b5208b.jpg)  
FIGURE 2-6 Example of operation of PRAM algorithmtofind sumof10 values.

# 2.3.2 Prefix Sums

Given a set of $_ n$ values $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ and an associative operation $\oplus$ ,the prefix sums problem is to compute the $n$ quantities:

$a _ { 1 }$   
a1a   
a1田aa3   
$a _ { 1 } \oplus a _ { 2 } \oplus a _ { 3 } \oplus \cdot \cdot \cdot \oplus a _ { n }$

For example, given the operation $+$ and the array of integers {3,1,0,4,2), the prefix sums of the array are {3,4,4,8,10).

FIGURE 2-7 EREW PRAM algorithm to sum n elements using $\lfloor n / 2 \rfloor$ processors.

SUM (EREW PRAM)   
Initial condition: List of n ≥ 1 elements stored in A[0. (n-1)]   
Final condition:Sum of elements stored in A[0]   
Global variables: $n$ ， $A [ 0 \cdots ( n - 1 ) ]$ ， $j$   
begin spawn $\left( P _ { 0 } , \ P _ { 1 } , \ P _ { 2 } , \ \cdot \ \cdot \ , \ P _ { \mid \ n / 2 \ \mid - 1 } \right)$ for all $P _ { i }$ where $0 ~ \le ~ i ~ \le ~ \lfloor ~ n / 2 \rfloor ~ - ~ 1$ do for $j  0$ to $\lceil \log \ n \rceil \ - \ 1$ do if $i$ modulo $2 ^ { j } \ = \ 0$ and $2 i + 2 ^ { j } < n$ then $A [ 2 i ] \  \ A [ 2 i ] \ + \ A [ 2 i \ + \ 2 ^ { j } ]$ endif endfor endfor   
end、

![](images/f06658a669ace9326fdc4cbec6e8402f20a0595dcbaa76e74fec411cbabdeebb.jpg)  
Packing elements is one application of prefixsums. (a) Array A contains both uppercase and lowercase letters.We wanttopack uppercase letters into beginning of A.(b) Array $\tau$ containsa1 for everyuppercase letteranda o for every lowercase letter. (c) Array $T$ afterprefix sums have been computed.For each elementof Acontaining anuppercase letter, thecorresponding element of $\tau$ is thatelement's index in the packed array. (d) Array $A$ afterpacking.

Prefix sums are also called parallel prefixes and scans. Prefix sums have many uses. For instance, suppose we are given an array $A$ of $n$ letters. We want to pack the uppercase letters in the initial portion of $A$ while maintaining their order. See Fig.2-8.First we initialize the elements of an auxiliary array $T$ of size $n$ . An element of $T$ is O if the corresponding element of $A$ isa lowercase letter, and an element of $T$ is 1 if the corresponding element of $A$ is an uppercase letter. Second, we compute the prefix sums of $T$ using the addition operation. Now for every uppercase letter $L$ located at $A [ i ]$ ,the value of $T [ i ]$ is the index of $L$ in the packed array.

Figure 2-9 is a PRAM algorithm that computes prefix sums. The complexity of the algorithm is identical to the complexity of the parallel sum-finding algorithm. The spawn routine requires $\lceil \log ( n - 1 ) \rceil$ instructions. The sequential for loop executes $\lceil \log n \rceil$ times,and each iteration has constant time complexity. Hence the overall time complexity of the algorithm is $\Theta ( \log n )$ ，given $n - 1$ processors.

Figure 2-10 illustrates the prefix sums algorithm on a list of 10 values.

FIGURE 2-9 PRAM algorithm to find prefix sums of an $n$ -element list using $n - 1$ processors

PREFIX.SUMS (CREW PRAM):   
Initial condition: List of $n \geq 1$ elements stored in $A [ 0 \cdots ( n - 1 ) ]$   
Final condition:Each element $A [ i ]$ contains $A [ 0 ] \oplus A [ 1 ] \oplus \cdots \oplus A [ i ]$   
Global variables: $n$ ， $A [ 0 \ldots ( n - 1 ) ]$ ， $j$   
begin   
spawn $( P _ { 1 } , P _ { 2 } , . . . , P _ { n - 1 } )$ forall $P _ { i }$ where $1 \leq \ i \leq \ n - 1$ do for $j  0$ to $\lceil \log { \ n } \rceil - 1$ do if $i - 2 ^ { j } \ge 0$ then $A [ i ]  A [ i ] + A [ i - 2 ^ { j } ]$ endif endfor   
endfor   
end

![](images/ff2d34360b3e1b1b83a5932d4b5ce33ce64af4dde63fb8f7a18c673d406fdb01.jpg)  
FIGURE 2-10 All prefix sums of a list of n valuescan be computed in「log n] addition steps on an EREW PRAM.

Consider the problem of finding, for each of $n$ elements on a linked list, the suffix sums of the last $i$ elements on the list,where $1 \leq i \leq n$ (Fig. 2-11). The suffix sums problem is a variant of the prefix sums problem,where anarray is replaced by a linked list,and the sums are computed from the end, rather than from the beginning (Karp and Ramachandran 199O). (If the elements on the list are either Oor 1,and the associative operation $\oplus$ is addition, the problem is usually called the listranking problem. However,the algorithm in this section also works in the more general case.)

One way to determine list position is to count the number of links traversed between the list element and the end of the list. Only a single pointer can be followed in one step,and there are n-1 pointers between the first list element and the end of the list. How can any algorithm traverse such a list in less than $\Theta ( n )$ time?

If we associate a processor with every list element and jump pointers in parallel,thedistance totheendof the list iscut inhalf throughtheinstruction $n e x t [ i ]  n e x t [ n e x t [ i ] ]$

Hence a logarithmic number of pointer-jumping steps are sufficient to collapse the list so that every list element points to the last list element. If a processor adds to its own link-traversal count, position[i], the current linktraversal count of the successors it encounters, the list position will be corectly determined.

![](images/05f077ce441203a651f3a689ddb8def6214e35de27444385559e3892005d038b.jpg)  
2-11 The position of each item on an $n$ -element linked listcan be determined in $\lceil \log n \rceil$ pointer-jumping steps.

The PRAM algorithm to determine the position of each element on a singly linked list appears in Fig. 2-12.

We have seen that spawning $n$ processors has time complexity $\Theta ( \log n )$ .Because the constant time for loop executes at most $\lceil \log n \rceil$ times,thecoleity of the parallel algorithm is $\Theta ( \log n )$ using $n$ processors.

FIGURE 2-12PRAM algorithm tocompute,for each element of a singly-linked list,its distance from the end of the list.

# LIST.RANKING (CREW PRAM):

Initial condition: Values in array next represent a linked list   
Final condition: Values in array position contain original distance of each element from end of list   
Global variables:noition $[ 0 \ldots ( n - 1 ) ] , n e x t [ 0 \ldots ( n - 1 ) ] , j$   
begin spawn $( P _ { 0 } , P _ { 1 } , P _ { 2 } , . . . , P _ { n - 1 } )$ for all $P _ { i }$ where $0 ~ \leq ~ i ~ \leq ~ n ~ - ~ 1$ do if $n e x t [ i ] \ = \ i$ then position[i] $ 0$ else position[i] $ 1$ endif for $j \gets 1$ to [log $n ^ { - }$ do position[i] position[i] $^ +$ position[next[i]] next[i] next[next[i]] endfor endfor   
end

# 2.3.4 Preorder Tree Traversal

Sometimes it is appropriate to attempt to reduce a complicated-looking problem into a simpler one for which a fast parallel algorithm is already known. The problem of numbering the vertices of a rooted tree in preorder (depth-first search order) is a case in point. At first glance the problem of preorder traversal may seem inherently sequential. Consider its common recursive description:

PREORDER.TRAVERSAL (nOdeptr) :

begin if nodept $\neq$ null then nodecount nodecount $+ 1$ nodeptr.label nodecount PREORDER.TRAVERSAL (nOdeptr.left) PREORDER.TRAVERSAL (nodeptr.right) endif   
end

Where is the parallelism? The fundamental operation assigns a label to a node. We cannot assign labels to the vertices in the right subtree until we know how many vertices are in the left subtree. We cannot assign labels to the vertices in the right subtree of the left subtree until we know how many vertices are in the left subtree of the left subtree,and so on. Viewed this way, the algorithm seems inherently sequential.

So let's take another view of the problem. Instead of focusing on the tree's vertices,let's think about the tree's edges.When we perform a preorder traversal,we systematically work our way through all the edges of the tree. In fact, we pass along every edge twice--once heading down from parent vertex to child vertex and once going back up. If we divide each tree edge into two edges,one corresponding to the downward traversal and one corresponding to the upward traversal, then the problem of traversing a tree turns into the problem of traversing a singly-linked list, which we have just seen in parallel.

This edge-oriented view of tree traversal leads to a fast parallel algorithm, first published by Tarjan and Vishkin (1984). Let us consider the algorithm in detail. The algorithm has four phases (Fig. 2-13). In step one the algorithm constructsasingly-linked list.Each vertex of the singly-linked listcorresponds to a downward or upward edge traversal of the tree.

In step two the algorithm assigns weights to the vertices of the newly created singly-linked list.In the preorder traversal algorithm,a vertex is labeled as soon as it is encountered via a downward edge traversal. (The root vertex is an exception and must be handled differently.) For this reason every vertex in the singly-linked list corresponding to a downward edge gets the weight 1, meaning that the node count is incremented when this edge is traversed. List elements corresponding to upward edges have the weight O, because the node count does not increase when the preorder traversal works its way back up the tree through previously labeled nodes.

![](images/2b9198983061920567f68e74e6bbc6338578d502c209650f378051fe3152dcc3.jpg)  
FIGURE 2-13 Preorder traversal of a rooted tree. (a) Tree. (b) Double tree edges,distinguishing downward edges fromupward edges.(c) Build linked list out of directed tree edges. Associate1withdownward edgesandO withupward edges.(d) Usepointer jumping tocomputetotal weight from eachvertex toend of list.Bold elements of linked list correspond to downward edges.Processors managing these elementsassign preorder values.Forexample,element (E,G) hasweight4,meaning treenodeGis fourth node fromend of preorder traversal list.The tree has8 nodes,so we can compute that tree node G has label 5 in preorder traversal. (e) Preorder traversal values.

In the third phase of the parallel algorithm we compute, for each element of the singly-linked list, the rank of that list element.

In step four the processors associated with downward edges use the ranks they have computed to assign a preorder traversal number to their associated tree nodes (the node at the end of the downward edge).

Our implementation of the parallel preorder traversal algorithm uses an unusual data structure to represent the tree (see Fig 2-14). For every tree node, the data structure stores, the node's parent, immediate sibling to the right, and leftmost child. Representing the tree this way keeps the amount of data stored at a constant for each tree node and simplifies tree traversal.

Figure 2-15 contains the PRAM algorithm for preorder tree traversal. The algorithm associates a processor with each traversed edge.A tree with $n$ nodes has $n - 1$ edges. Since we are dividing each edge into a downward edge and an upward edge, the algorithm needs $2 ( n - 1 )$ processors to manipulate the $2 ( n - 1 )$ elements of the singly-linked list of elements corresponding to the edge traversals.

Once all the processors have been activated, they construct a linked list of elements corresponding to edges in the preorder traversal. Given edge $( i , j )$ ， each processor must compute the successor to that edge in the traversal. If parent $[ i ] = j$ , the edge is moving upward in the tree, from a child node to its parent. Upward edges have three kinds of successors.If the child has a sibling, the successor edge goes from the parent node to the sibling. Otherwise, if the child has a grandparent, the successor edge goes from the parent node to the grandparent. If both of these conditions fail, the edge is at the end of the tree traversal, so we put a loop at the end of the element list. In this case we also know the identity of the root node, and we set its preorder number to 1.

Next we consider the case where $p a r e n t [ i ] \neq j$ ； that is,where the edge is moving downward in the tree, from a parent node to one of its children. There are only two kinds of successor edges. If the child node itself has children, the successor is the edge from the child to the grandchild. Otherwise, the child node is a leaf,and the successor is the edge from the child back to the parent.

After the processors construct the linked list, they assign a position value of 1 to those elements corresponding to downward edges and O to those elements corresponding to upward edges.

The pointer-jumping loop follows. The final position values indicate the number of preorder traversal nodes between the list element and the end of the list. Tocompute each node's preorder traversal label,each processor assocated

![](images/26d14801124741400fab21f9b31884adb3c2cbb7e80ab8fc1d897e17487a649a.jpg)  
FIGURE 2-14 We can represent a rooted tree withadata structure that stores,for every tree node, the node'sparent,immediatesing totheright,andleftmostchild

Global,n {Number of vertices in tree} parent[1... n] {Vertex number of parent node] child[1... n] {Vertexnumberof first child) sibling $\left[ 1 \ldots n \right]$ {Vertexnumberof sibling] $s u c c [ 1 \ldots ( n - 1 ) ]$ {Index of successor edge] position $[ 1 \dots ( n - 1 ) ]$ {Edge rank} preorder $[ 1 \dots n ]$ {Preorder traversal number)   
begin   
spawn (set of all $P ( i , j )$ where $( i , j )$ is an edge)   
for all $P ( i , j )$ where $( i , j )$ is an edge do {Put the edges into a linked list} if parent[i] $\mathit { \Pi } = \mathit { \Pi } \mathit { j }$ then if sibling[i] $\neq$ null then $s u c c [ ( i , j ) ] ~ \gets ~ ( j , s i b l i n g [ i ] )$ else if parent $[ j ] \neq$ null then $s u c c [ ( i , j ) ] ~ \gets ~ ( j , p a r e n t [ j ] )$ else $s u c c [ ( i , j ) ] ~ \gets ~ ( i , j )$ preorder $\mathbf { \sigma } \cdot [ j ] \  \ 1 \ \{ j$ is root of tree } endif else if chil $d [ j ] \neq$ null then $s u c c [ ( i , j ) ] ~ \gets ~ ( j , c h i l d [ j ] )$ else succ $[ ( i , j ) ] ~  ~ ( j , i )$ endif endif {Number of edges of the successor list} if parent[i] $= \ j$ then position $[ ( i , j ) ] ~  ~ 0$ elseposition $[ ( i , j ) ] \ \gets \ 1$ endif {Perform suffix sum on successor list} for $k \gets 1$ to $\lceil \log ( 2 ( n - 1 ) ) \rceil$ do positior $\iota [ ( i , j ) ] ~  ~ p o s i t i o n [ ( i , j ) ] ~ + ~ p o s i t i o n [ s u c c [ ( i , j ) ] ]$ $s u c c [ ( i , j ) ] ~  ~ s u c c [ s u c c [ ( i , j ) ] ]$ endfor {Assign preorder values] if $i ~ = ~ p a r e n t [ j ]$ thenpreorder ${ \it \Delta \cdot } [ j ] ~  ~ n ~ + ~ 1 ~ - ~ p o s i t i o n [ ( i , j ) ]$ endif   
endfor   
end

FIGURE 2-15 PRAM algorithm to label the nodes of a tree according to their position in a preorder traversal.

with a downward edge subtracts its value of position from n +1. The added 1 causes the preorder traversal numbering to begin at 1, not 0.

We leave the complexity analysis of this algorithm as a simple exercise for the reader.

# 2.3.5 Merging Two Sorted Lists

Many PRAM algorithms achieve low time complexity by performing more operations than an optimal RAM algorithm. The problem of merging two sorted lists is another example.

One optimal RAM algorithm creates the merged list one element at a time. It requires at most $n - 1$ comparisons to merge two sorted lists of $n / 2$ elements. Its time complexity is $\Theta ( n )$ . A PRAM algorithm can perform the task in $\Theta ( \log n )$ time by assigning each list element its own processor. Every processor finds the position of its own element on the other list using binary search.Because an element's index on its own list is known, its place on the merged list can be computed when its index on the other list has been found and the two indices added. All $n$ elements can be inserted into the merged list by their processors in constant time (see Fig. 2-16).

The pseudocode for the PRAM algorithm to merge two sorted lists appears in Fig. 2-17. In this version of the algorithm the two lists and their unions have disjoint values. Let’s examine the algorithm in detail. As usual, the first step is to spawn the maximum number of processors needed at any point in the algorithm's execution. In this case we need $n$ processors, one for each element of the two lists to be merged. After the processors are spawned,we immediately activate them. In parallel, the processors determine the range of indices they are going to search. The processors associated with elements in the lower half of the array will perform binary search on the elements in the upper half of the array,and vice versa.

![](images/9692dea06bbfcfae9e93eab74394c23dfa6c5b019a438ed70cbb67f5887b0121.jpg)  
FIGURE 2-16 Two lists having $n / 2$ elements each can be merged in $\Theta ( \log { n } )$ time.

Given: Two sorted lists of $n / 2$ elements each, stored in $A [ 1 ] \cdots \ A [ n / 2 ]$ and $A [ ( n / 2 ) + 1 ] \cdots \ A [ n ]$ The two lists and their unions have disjoint values   
Final condition: Merged list in locations A[1]·.. A[n]   
Global $A [ 1 \cdots \ n ]$   
Local $x$ low,high,index   
begin spawn $( P _ { 1 } , \ P _ { 2 } , \ \ldots , \ P _ { n } )$ for all $P _ { i }$ where $1 \ \leq \ i \ \leq \ n$ do { Each processor sets bounds for binary search} if $\textit { i } \leq \textit { n } / 2$ then low $ \ ( n / 2 ) + 1$ $h i g h  n$ else $\begin{array} { l } { l o w \ \gets \ 1 } \\ { h i g h \ \gets \ n / 2 } \end{array}$ endif { Each processor performs binary search } $\begin{array} { r } { x  A [ i ] } \end{array}$ repeat index $ \lfloor ( l o w + h i g h ) / 2 \rfloor$ if $x ~ < ~ A [ i n d e x ]$ then high index - 1 else low ← index +1 endif until low $>$ high { Put value in correct position on merged list } $A [ h i g h + i - n / 2 ] \  \ x$ endfor   
end

Every processor has a unique value of $x$ ， an element to be merged. The repeat...until loop implements binary search. When a processor exits the loop,its private value of highwillbeset to the index of thelargest element on the list that is smaller than $x$ 。

Consider a processor $P _ { i }$ associated with value $A [ i ]$ in the lower half of the list. The processor's final value of high must be between $( n / 2 )$ and $n$ .Element $A [ i ]$ is larger than $i - 1$ elements on the lower half of the list. It isalso larger than $h i g h - ( n / 2 )$ elements on the upper half of the list. Therefore,we should put $A [ i ]$ on the merged list after $i + h i g h - n / 2 - 1$ other elements,at index $i + h i g h - n / 2$

Now consider a processor P: associated with value A[i] in the upper half of the list. The processor's final value of high must be between O and n/2. Element A[i] is larger than i - (n/2 + 1) other elements on the upper half of the list. It is also larger than high elements on the lower half of the list. Therefore, we should put A[i] on the merged list after i+high-n/2-1 other elements,at index $i + h i g h - n / 2$

Since all processors use the same expression to place elements in their proper places on the merged list, every processor relocates its element using the same assignment statement at the end of the algorithm.

The total number of operations performed to merge the lists has increased from O(n) in the sequential algorithm to ?(n log n) in the parallel algorithm. This tactic is sensible only when the number of processors is unbounded.When we begin to develop algorithms for real parallel computers, with processors a limited resource, we must consider the cost of the parallel algorithm.

# 2.3.6 Graph Coloring

Determining if the vertices of a graph can be colored with $c$ colors so that no two adjacent vertices are assigned the same color is called the graph coloring problem. To solve the problem quickly,we can create a processor for every possible coloring of the graph, then have each processor check to see if the coloring it represents is valid.

Assume the graph has $n$ vertices. Given an $n \times n$ adjacency matrix and a positive constant $c$ ,aprocessor is created for every possible coloring of the graph.For example, processor $P ( i _ { 0 } , i _ { 1 } , \ldots , i _ { n - 1 } )$ corresponds to a coloring of vertex O with color $i _ { 0 }$ ,a coloring of vertex 1 with color $i _ { 1 } , . . . ,$ and a coloring of vertex $n - 1$ with color $i _ { n - 1 }$

Each processor initially sets its value in the $n$ -dimensional candidate array to 1. It then spends $\Theta ( n ^ { 2 } )$ time determining whether,for the particular assignment of colors to vertices it represents, two adjacent vertices have been given the same color. If $A [ j , k ] = 1$ and $i _ { j } = i _ { k }$ , then the coloring is not valid, because $A [ j , k ] = 1$ means that vertices $j$ and $k$ are adjacent, and $i _ { j } = i _ { k }$ means that vertices $j$ and $k$ have the same color. If a processor detects an invalid coloring, it sets its value in the candidate array to O.After the $n ^ { 2 }$ comparisons, if any element in the candidate array is still 1,then the coloring is valid.By summing over all $c ^ { n }$ elements in the candidate array,it can be determined whether there exists a valid coloring (see Fig. 2-18). The CREW PRAM algorithm for graph coloring appears in Fig. 2-19.

Let us evaluate the time complexity of this algorithm. It takes $\Theta ( \log c ^ { n } )$ time to spawn the $c ^ { n }$ processors.Every processor executes the doubly-nested for loops in time $\Theta ( n ^ { 2 } )$ . Summing the $c ^ { n }$ elements of answer requires time $\Theta ( \log c ^ { n } )$ with the $c ^ { n }$ processors we have available. The overall complexity of the algorithm,then,is $\Theta ( \log c ^ { n } + n ^ { 2 } ) = \Theta ( n ^ { 2 } + n \log c )$ .Because $c < n$ ,the complexity expression reduces to $\Theta ( n ^ { 2 } )$ ·

Graph:

00②

FIGURE 2-18 Example of CREW PRAM graphcoloringalgorithm In this case thealgorithm attemptstocolora3-vertex graph with2 colors.

Colorings: Initial values: After checking:

0,0,0 0,0,1 Number of   
0,1,0 legal colorings:   
0,1,1 1,0,0 1 X   
1,0,1 1   
1,1,0   
1,1,1 1 0

# GRAPH.COLORING (CREW PRAM):

Global n {Number of vertices] C {Number of colors] $A [ 1 . . . n ] [ 1 . . . n ]$ {Adjacency matrix) candidate[1...][1..].·.[...] $n$ -dimensionalboolean matrix) valid {Number of valid colorings] $j , \ k$ begin spawn $\big ( P ( i _ { 0 } , i _ { 1 } , \dots , i _ { n - 1 } ) \big )$ where $0 ~ \le ~ i _ { \upsilon } ~ < ~ c$ for $0 ~ \leq ~ v ~ < ~ n$ for all $P ( i _ { 0 } , i _ { 1 } , \ldots , i _ { n - 1 } )$ where $0 ~ \leq ~ i _ { v } ~ < ~ c$ for $0 ~ \leq ~ v ~ < ~ n$ do candidate $[ i _ { 0 } , i _ { 1 } , \dotsc , i _ { n - 1 } ] \  \ 1$ for $j  0$ to $n - 1$ do for $k \gets 0$ to $n - 1$ do if $A [ j ] [ k ]$ and $i _ { j } ~ = ~ i _ { k }$ then candidate[i $\mathrm { i } _ { 0 } , i _ { 1 } , \ldots , i _ { n } ] ~  ~ 0$ endif endfor endfor valid $ \Sigma$ candidate {Sum of all elements of candidate} endfor if valid $> ~ 0$ then print "Valid coloring exists” else printif “Valid coloring does not exist” endif end

FIGURE 2-19 CREW PRAM algorithm to determine if a graph with $n$ vertices can be colored with c colors.

# 2.4 REDUCING THE NUMBER OF PROCESSORS

Definition 2.2. A cost optimal parallel algorithm is an algorithm for which the cost is in the same complexity class as an optimal sequential algorithm.

None of the algorithms we presented in the previous section are cost optimal. For example, the parallel reduction algorithm has complexity ?(log n) given ?(n) processors. This algorithm is not cost optimal because the product of its complexity and the number of processors is @(n log n), which is greater than the complexity of an optimal sequential algorithm, $\Theta ( n )$

If, however, the total number of operations performed by the parallel algorithm is of the same complexity class as an optimal sequential algorithm, then a cost-optimal parallel algorithm does exist. Returning to our example, the parallel reduction algorithm performs about n/2 additions the first step,n/4 additions the second step, $n / 8$ additions the third step, and so on, executing a total of n - 1 additions over the [log n] iterations. Since both the sequential and the parallel algorithms perform n -1 additions, a cost-optimal variant of the parallel reduction algorithm exists.

Is there a cost-optimal parallel reduction algorithm that also has time complexity O(log n)? We can compute the minimum number of processors needed to perform the $n - 1$ operations in logarithmic time:

$$
p = { \frac { n - 1 } { \Theta ( \log n ) } } \Rightarrow p = \Theta ( n / \log n )
$$

Once we have determined the appropriate number of processors, we need to verify that there is indeed a cost-optimal parallel-reduction algorithm with logarithmic time complexity. Theorem 2.2 lets us do that.

Theorem 2.2. (Brent's Theorem) (Brent 1974).Given $A$ , a parallel algorithm with computation time $t$ ,if parallel algorithm A performs $m$ computational operations, then $p$ processors can execute algorithm $A$ in time $t + ( m - t ) / p$

Proof. Let $s _ { i }$ denote the number of computational operations performed by parallel algorithm $A$ at step $i$ ，where $1 \ \leq \ i \ \leq \ t$ .By_definition $\textstyle \sum _ { i = 1 } ^ { n } s _ { i } \ = \ m$ .Using $p$ processors we can simulate step $i$ in time $\lceil s _ { i } / p \rceil$ . The entire computation $A$ can be performed with $p$ processors in time

$$
\begin{array} { r l } & { \displaystyle \sum _ { i = 1 } ^ { t } \Biggl \lceil \frac { s _ { i } } { p } \Biggr \rceil \leq \sum _ { i = 1 } ^ { t } \frac { s _ { i } + p - 1 } { p } } \\ & { \qquad = \displaystyle \sum _ { i = 1 } ^ { t } \frac { p } { p } + \sum _ { i = 1 } ^ { t } \frac { s _ { i } - 1 } { p } } \\ & { \qquad = t + ( m - t ) / p } \end{array}
$$

Applying Brent's theorem to our parallel reduction algorithm, the execution time with $\big \lfloor { \frac { n } { \log n } } \big \rfloor$ processors is

$$
\lceil \log n \rceil + \frac { n - 1 - \lceil \log n \rceil } { \lfloor \frac { n } { \log n } \rfloor } = \Theta \biggl ( \log n + \log n - \frac { \log n } { n } - \frac { \log ^ { 2 } n } { n } \biggr ) = \Theta ( \log n )
$$

In this case reducing the number of processors from $_ n$ to $\lfloor n / \log n \rfloor$ does not change the complexity of the parallel algorithm. Figure 2-2O illustrates how $n$ values can be summed in $O ( \log n )$ time using $\lfloor n / \log n \rfloor$ processors by associating no more than $\lceil \log n \rceil$ values per processor.

Let's consider another example. The prefix sums algorithm appearing in Sec. 2.3 executes in $\lceil \log n \rceil$ iterations. The number of operations performed in iteration $_ i$ is $n - 2 ^ { i }$ . The total number of operations performed, then, is

$$
\sum _ { i = 0 } ^ { \lceil \log n \rceil - 1 } n - 2 ^ { i } = n \log n - ( 2 ^ { \lceil \log n \rceil } - 1 ) = \Theta ( n \log n )
$$

This parallel algorithm is not cost optimal, because an optimal sequential algorithm can find all $_ n$ prefix sums in $n - 1$ operations.

To reduce the cost, we must reduce the number of processors. However, if the processors simply emulate the current parallel algorithm-as they did in the modified parallel-sum algorithm-and do not change the the total number of operations performed, then the decrease in the number of processors will be offset by an increase in the execution time,and the cost will remain the same. If we are going to reduce the number of processors, we must make them work more efficiently.

When we reduce the number of processors, a single processor must manipulate a larger data set than in the original parallel algorithm. In many problems, including the computation of prefix sums, applying an optimal sequential algorithm will improve the efficiency of this portion of the parallel algorithm.

Figure 2-21 illustrates how we can use this idea to compute the prefix sums of $n$ values given $p$ processors, where $p < n - 1$ .We divide the $n$ values into $p$ sets, each containing no more than $\lceil n / p \rceil$ values. The first $p - 1$ processors use the best sequential algorithm to find the sum of their $\lceil n / p \rceil$ values. This takes $\lceil n / p \rceil - 1$ steps. The processors compute the prefix sums of these subtotals in $\lceil \log ( p - 1 ) \rceil$ time using the parallel algorithm described in Sec. 2.3. Finally,

FIGURE 2-20 A PRAM can add $n$ values in $\Theta ( \mathsf { l o g } \mathsf { n } )$ time using $\lfloor n / \log n \rfloor$ processors. During the first few iterations of the algorithm,each processor emulates a set of processors, adding to the execution time of the algorithm, but not increasing the overall complexity of the parallel algorithm beyond $\Theta ( \log { n } )$ .During later iterations,when no more than $\lfloor n / \log n \rfloor$ processors are needed, the algorithm is identical to the original PRAM algorithm.

UNUUU 15 24 11 17 39 28 67

![](images/7296f4da717169c2404e8669195578d58b7c5d974511500ff054c7e31c9535ad.jpg)  
Illustration of a cost-optimal parallel algorithm to find prefix sums. (a) Set of 14 values is divided into 4 subsets,1 per processor.First3 processors find sum of their values using best sequential algorithm. (b) First 3 processors compute prefix sums in parallel using algorithmof Sec.2.3. (c) Each processor uses the sum of valuesin lower processors' blocks as base for computing prefix sums in its own block, using best sequential algorithm

each processor uses the sum of the values in the lower blocks to compute the prefix sums of its block of values. This step requires $\lceil n / p \rceil$ additions. The execution time of the parallel algorithm is

$$
\left\lceil { \frac { n } { p } } \right\rceil - 1 + \left\lceil \log ( p - 1 ) \right\rceil + \left\lceil { \frac { n } { p } } \right\rceil = \Theta \left( { \frac { n } { p } } + \log p \right)
$$

The total number of addition steps performed is $\Theta ( n + p \log p )$ , meaning if $p$ is small enough, the parallel algorithm will be cost-optimal.

Let's use Brent’s theorem to explore the trade-off between processors and execution time. Executing this algorithm with $p$ processors results in an execution time of

$$
\Theta \left( \left( { \frac { n } { p } } + \log p \right) + { \frac { n + p \log p - ( { \frac { n } { p } } + \log p ) } { p } } \right) = \Theta \left( { \frac { n } { p } } + \log p \right)
$$

Execution time is minimized when $p = \Omega ( n / \log n )$ . The parallel algorithm has optimal cost when $p = { O \left( n / \log n \right) }$ For this reason the value of $p$ that ensures both optimal cost and minimum execution time is $p = \Theta ( n / \log n )$

# 2.5 PROBLEMS DEFYING FAST SOLUTIONS ON PRAMS

This section relates the PRAM model to the rest of complexity theory; it presumes the reader has a knowledge of standard complexity terms, such as $\mathcal { P }$ ， $\mathcal { N P }$ ,and $\mathcal { N P }$ -complete.

Definition 2.3. The expression $T ( n ) ^ { o ( 1 ) }$ denotes polynomial functions of $T ( n )$

For example, the functions $l o g ^ { 2 } n$ and $l o g ^ { 3 } n$ are in the set $\log n ^ { O ( 1 ) }$ ,the functions $n ^ { 2 }$ and $n ^ { 3 }$ are in the set $n ^ { O ( 1 ) }$ ,and the functions $e ^ { 2 x }$ and $e ^ { 3 x }$ are in the set $( e ^ { x } ) ^ { O ( 1 ) }$ 。

Definition 2.4. The set $( \log n ) ^ { o ( 1 ) }$ is called the set of polylogarithmic functions.

Theorem 2.3. (Parallel Computation Thesis). The class of problems solvable in time $T ( n ) ^ { O ( 1 ) }$ by a PRAM isequal to theclassof problems solvable in work space $T ( n ) ^ { o ( 1 ) }$ by a RAM, if $T ( n ) \geq \log n$

The parallel computation thesis has been proven for those cases where $T ( n )$ is a polynomial function of the problem size (von zur Gathen 1986).

Restating the case where the parallel computation thesis has been proven, a PRAM can recognize in polynomial time all ianguages recognized by a RAM in polynomial space. A consequence of this theorem is that a PRAM can solve $\mathcal { N P }$ -complete problems in polynomial time. For example, the graph coloring problem considered in the previous section is $\mathcal { N P }$ -complete,yet we gave an $O ( n ^ { 2 } )$ algorithm to solve it.To do this,we used anumber of processors exponential in the problem size.

Theorem 2.4. If the number of processors in a PRAM is restricted to some polynomial function of the size of the input, then the problems solvable in parallel polynomial time is $\mathcal { P }$ ,the set of problems solvable in sequential polynomial time.

Proof. This is left to the reader.

Definition 2.5. A parallel algorithm has polylogarithmic time complexity if its time complexity is a polylogarithmic function of the problem size.

Definition 2.6. $\mathcal { N C }$ is the class of problems solvable on a PRAM in polylogarithmic time using a number of processors that are a polynomial function of the problem size.

Many problems in $\mathcal { P }$ can be solved in parallel in polylogarithmic time. For example,hardware circuits perform many operations in time logarithmic in the number of bits in the operands. Other examples of problems in class $\mathcal { N C }$ include computing the transitive closure of a relation, boolean matrix multiplication, matrix inversion, and constructing the maximal independent set of vertices in a graph (Karp and Ramachandran 1990).

It is an open problem whether $\mathcal { N C } = \mathcal { P }$ ,but it seems unlikely that every problem in $\mathcal { P }$ is in $\mathcal { N C }$ .In other words, there appear to be some problems in $\mathcal { P }$ that cannot be solved in polylogarithmic time on a PRAM using a polynomial number of processors.

Definition 2.7. (Gibbons and Ryter 1988) A problem $L \in \mathcal { P }$ is $\mathcal { P }$ -completeif every other problem in $\mathcal { P }$ can be transformed to $L$ in polylogarithmic parallel time using PRAM with a polynomial number of processors.

![](images/9c0e1442344155f70cf57623e9f28402d0ebc65ff3e63cc35513a6ad528b4494.jpg)  
FIGURE 2-22 Conjectured relationship between the complexity classes NC, $\mathcal { P }$ ， $\mathcal { N P }$ ， $\mathcal { P }$ -complete,and $\mathcal { N P }$ -complete.

The $\mathcal { P }$ -complete problems are those that seem to defy a fast (i.e., polylogarithmic time) parallel solution. Problems in this class include depth-frst search of an arbitrary graph, the maximum-flow problem,and the circuit value problem.

Figure 2-22 uses a Venn diagram to display the conjectured relationship between the sets $\mathcal { N C } , \mathcal { P } , \mathcal { N P } ,$ $\mathcal { P }$ complete, and $\mathcal { N P }$ -complete.Remember that the questions $\mathcal { N C } = \mathcal { P }$ and $\mathcal { P } = \mathcal { N P }$ remain open.

# 2.6 SUMMARY

The PRAM is a parallel extension of the RAM model of serial computation. A PRAM allows algorithmic steps to be performed simultaneously on a large data set. PRAM models may or may not allow multiple processors to read from or write to the same memory location simultaneously, resulting in three model categories: EREW (exclusive read,exclusive write), CREW (conct read, exclusive write),and CRCW (concurrent read, concurrent write). CCW PRAM models can be distinguished by how concurrent writes to the same memory location are resolved. In the COMMON PRAM model, concurrent writes to the same location are allowed only if all the values are identical. In the ARBITRARY PRAM model concurrent writes are resolved by letting the value of an arbitrary processor succeed. In the PRIORITY PRAM model the processor with highest priority wins a concurrent write to the same location.

Despite their popularity as bases for parallel algorithm design, no actual processor arrays have been built based on PRAM models because it is not feasible to allow $p$ processors to access any $p$ -memory locations simultaneously. Nevertheless,ifa PRAM algorithm is cost optimal, it may be a suitable basis for the design of a parallel program targeted to a real machine. Brent’s theorem can help identify those cases where cost-optimal parallel algorithms exist.

# 2.7 BIBLIOGRAPHIC NOTES

The primary sources for this chapter are Gibbons and Rytter (1988) and Karp and Ramachandran (1990).