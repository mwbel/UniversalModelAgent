#

Symplectic Geometric Algorithms for Hamiltonian Systems

# Symplectic Geometric Algorithms Symplectic Geometric Al

# Kang Feng Mengzhao Qin

# Symplectic Geometric Symplectic Geo Algorithms for

With 62 Figures

Authors Kang Feng (1920-1993) Institute of Computational Mathematics and Scientific/ Engineering Computing Beijing 100190, China

Mengzhao Qin Institute of Computational Mathematics and Scientific/ Engineering Computing Beijing 100190, China Email: qmz@lsec.cc.ac.cn

ISBN 978-3-642-01776-6 e-ISBN 978-3-642-01777-3

Springer Heidelberg Dordrecht London New York

Library of Congress Control Number: 2009930026 $\circledcirc$ Zhejiang Publishing United Group, Zhejiang Science and Technology Publishing House, Hangzhou and Springer-Verlag Berlin Heidelberg 2010

This work is subject to copyright. All rights are reserved, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilm or in any other way, and storage in data banks. Duplication of this publication or parts thereof is permitted only under the provisions of the German Copyright Law of September 9, 1965, in its current version, and permission for use must always be obtained from Springer. Violations are liable to prosecution under the German Copyright Law.

The use of general descriptive names, registered names, trademarks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.

Cover design: Frido Steinen-Broo, EStudio Calamar, Spain

Printed on acid-free paper

“. . . In the late 1980s Feng Kang proposed and developed so-called symplectic algorithms for solving equations in Hamiltonian form. Combining theoretical analysis and computer experimentation, he showed that such methods, over long times, are much superior to standard methods. At the time of his death, he was at work on extensions of this idea to other structures . . . ，

# Peter Lax

# Cited from SIAM News November 1993

![](images/55ae8f8093ec88929397959d761c959d077f662949b705cd13fd87608dac1a81.jpg)  
Kang Feng giving a talk at an international conference

“ A basic idea behind the design of numerical schemes is that they can preserve the properties of the original problems as much as possible . . . Different representations for the same physical law can lead to different computational techniques in solving the same problem, which can produce different numerical results . . .”

Kang Feng (1920 – 1993)

Cited from a paper entitled “How to compute property Newton’s equation of motion”

# 自然科学奖

# 证书

为表彰在自然科学研完中做出重大贡献者，特颁发国家自然科学奖证书，以资鼓励。

![](images/1047552b104040af583888c0c13eb3c3a3b62132f430054291a00565557e6a8c.jpg)

# Prize certificate

![](images/26c15327aab34513173551f7ab7bdc3cacc1aaf5507990a16fb83182669658e7.jpg)  
Author’s photograph taken in Xi’an in 1989

# Foreword

Kang Feng (1920–1993), Member of the Chinese Academy of Sciences, Professor and Honorary Director of the Computing Center of the Chinese Academy of Sciences, famous applied mathematician, founder and pioneer of computational mathematics and scientific computing in China.

It has been 16 years since my brother Kang Feng passed away. His scientific achievements have been recognized more and more clearly over time, and his contributions to various fields have become increasingly outstanding. In the spring of 1997, Professor Shing-Tung Yau, a winner of the Fields Medal and a foreign member of the Chinese Academy of Sciences, mentioned in a presentation at Tsinghua University, entitled “The development of mathematics in China in my view”, that “there are three main reasons for Chinese modern mathematics to go beyond or hand in hand with the West. Of course, I am not saying that there are no other works, but I mainly talk about the mathematics that is well known historically: Professor Shiingshen Chern’s work on characteristic class, Luogeng Hua’s work on the theory of functions of several complex variables, and Kang Feng’s work on finite elements.” This high evaluation of Kang Feng as a mathematician (not just a computational mathematician) sounds so refreshing that many people talked about it and strongly agreed with it. At the end of 1997, the Chinese National Natural Science Foundation presented Kang Feng et al. with the first class prize for his other work on a symplectic algorithm for Hamiltonian systems, which is a further recognition of his scientific achievements (see the certificate on the previous page). As his brother, I am very pleased.

Achieving a major scientific breakthrough is a rare event. It requires vision, ability and opportunity, all of which are indispensable. Kang Feng has achieved two major scientific breakthroughs in his life, both of which are very valuable and worthy of mention. Firstly, from 1964 to 1965, he proposed independently the finite element method and laid the foundation for the mathematical theory. Secondly, in 1984, he proposed a symplectic algorithm for Hamiltonian systems. At present, scientific innovation has become the focus of discussion. Kang Feng’s two scientific breakthroughs may be treated as case studies in scientific innovation. It is worth emphasizing that these breakthroughs were achieved in China by Chinese scientists. Careful study of these has yet to be carried out by experts. Here I just describe some of my personal feelings.

It should be noted that these breakthroughs resulted not only from the profound mathematical knowledge of Kang Feng, but also from his expertise in classical physics and engineering technology that were closely related to the projects. Scientific breakthroughs are often cross-disciplinary. In addition, there is often a long period of time before a breakthrough is made-not unlike a long time it takes for a baby to be born, which requires the accumulation of results in small steps.

The opportunity for inventing the finite element method came from a national research project, a computational problem in the design of the Liu Jia Xia dam. For such a concrete problem, Kang Feng found a basis for solving of the problem using his sharp insight. In his view, a discrete computing method for a mathematical and physical problem is usually carried out in four steps. Firstly, one needs to know and define the physical mechanism. Secondly, one writes the appropriate differential equations accordingly. In the third step, design a discrete model. Finally, one develops the numerical algorithm. However, due to the complexity of the geometry and physical conditions, conventional methods cannot always be effective. Nonetheless, starting from the physical law of conservation or variational principle of the matter, we can directly relate to the appropriate discrete model. Combining the variational principle with the spline approximation leads to the finite element method, which has a wide range of adaptability and is particularly suited to deal with the complex geometry of the physical conditions of computational engineering problems. In 1965, Kang Feng published his paper entitled “Difference schemes based on the variational principle”, which solved the basic theoretical issues of the finite element method, such as convergence, error estimation, and stability. It laid the mathematical foundation for the finite element method. This paper is the main evidence for recognition by the international academic community of our independent development of the finite element method.

After the Chinese Cultural Revolution, he continued his research in finite element and related areas. During this period, he made several great achievements. I remember that he talked with me about other issues, such as Thom’s catastrophe theory, Prigogine’s theory of dissipative structures, solitons in water waves, the Radon transform, and so on. These problems are related to physics and engineering technology. Clearly he was exploring for new areas and seeking a breakthrough. In the 1970s, Arnold’s “Mathematical Method of Classical Mechanics” came out. It described the symplectic structure for Hamiltonian equations, which proved to be a great inspiration to him and led to a breakthrough. Through his long-term experience in mathematical computation, he fully realized that different mathematical expressions for the same physical law, which are physically equivalent, can perform different functions in scientific computing (his students later called this the “Feng’s major theorem”). In this way, for classical mechanics, Newton’s equations, Lagrangian equations and Hamiltonian equations will show a different pattern of calculations after discretization. Because the Hamiltonian formulation has a symplectic structure, he was keenly aware that, if the algorithm can maintain the geometric symmetry of symplecticity, it will be possible to avoid the flaw of artificial dissipation of this type of algorithm and design a high-fidelity algorithm. Thus, he opened up a broad way for the computational method of the Hamiltonian system. He called this way the “Hamiltonian way”. This computational method has been used in the calculation of the orbit in celestial mechanics, in calculations for the particle path in accelerator, as well as in molecular dynamics. Later, the scope of its application was expanded. For example, it has also been widely used in studies of the atmosphere and earth sciences and elsewhere. It has been effectively applied in solving the GPS observation operator, indicating that Global Positioning System data can be dealt with in a timely manner. This algorithm is 400 times more efficient than the traditional method. In addition, a symplectic algorithm has been successfully used in the oil and gas exploration fields. Under the influence of Kang Feng, international research on symplectic algorithm has become popular and flourishing, nearly 300 papers have been published in this field to date.

Kang Feng’s research work on the symplectic algorithm has been well-known and recognized internationally for its unique, innovative, systematic and widespread properties, for its theoretical integrity and fruitful results.

J. Lions, the former President of the International Mathematics Union, spoke at a workshop when celebrating his 60th birthday: “This is another major innovation made by Kang Feng, independent of the West, after the finite element method.” In 1993 one of the world’s leading mathematicians, P.D. Lax, a member of the American Academy of Sciences, wrote a memorial article dedicated to Kang Feng in SIAM News, stating that “In the late 1980s, Kang Feng proposed and developed so-called symplectic algorithms for solving evolution equations . . .. Such methods, over a long period, are much superior to standard methods.” E. J. Marsden, an internationlly wellknown applied mathematician, visited the computing institute in the late 1980s and had a long conversation with Kang Feng. Soon after the death of Kang Feng, he proposed the multi-symplectic algorithm and extended the characteristics of stability of the symplectic algorithm for long time calculation of Hamiltonian systems with infinite dimensions.

On the occasion of the commemoration of the 16th anniversary of Kang Feng’s death and the 89th anniversary of his birth, I think it is especially worthwhile to praise and promote what was embodied in the lifetime’s work of Kang Feng — “ independence in spirit, freedom in thinking”. 1 Now everyone is talking about scientific innovation, which needs a talented person to accomplish. What type of person is needed most? A person who is just a parrot or who has an “independent spirit, freely thinking”? The conclusion is self-evident. Scientific innovation requires strong academic atmosphere. Is it determined by only one person or by all of the team members? This is also self-evident. From Kang Feng’s scientific career, we can easily find that the key to the problem of scientific innovation is “independence in spirit, freedom in thinking”, and that needs to be allowed to develop and expand.

Kang Feng had planned to write a monograph about a symplectic algorithm for Hamiltonian systems. He had accumulated some manuscripts, but failed to complete it because he died too early due to sickness. Fortunately, his students and Professor Mengzhao Qin (see the photo on the previous page), one of the early collaborators, spent 15 years and finally completed this book based on Kang Feng’s plan, realizing his wish. It is not only an authoritative exposition of this research field, but also an exposure of the academic thought of a master of science, which gives an example of how an original and innovative scientific discovery is initiated and developed from beginning to end in China.

We would also like to thank Zhejiang Science and Technology Publishing House, which made a great contribution to the Chinese scientific cause through the publication of this manuscript.

Although Kang Feng died 16 years ago, his scientific legacy has been inherited and developed by the younger generation of scientists. His scientific spirit and thought still elicit care, thinking and resonance in us. He is still living in the hearts of us.

Duan, Feng   
Member of Chinese Academy of Sciences Nanjing University   
Nanjing   
September 20, 2009

# Preface

It has been 16 years since Kang Feng passed away. It is our honor to publish the English version of Symplectic Algorithm for Hamiltonian Systems, so that more readers can see the history of the development of symplectic algorithms. In particular, after the death of Kang Feng, the development of symplectic algorithms became more sophisticated and there have been a series of monographs published in this area, e.g., Sanz-Serna & M.P. Calvo’s Numerical Hamiltonian Problems published in 1994 by Chapman and Hall Publishing House; E. Hairer, C. Lubich and G. Wanner’s Geometrical Numerical Integration published in 2001 by Springer Verlag; B. Leimkuhler and S. Reich’s Simulating Hamiltonian Dynamics published in 2004 by Cambridge University Press. The symplectic algorithm has been developed from ordinary differential equations to partial differential equations, from a symplectic structure to a multi-symplectic structure. This is largely due to the promotion of this work by J. Marsden of the USA and T. Bridge and others in Britain. Starting with a symplectic structure, J. Marsden first developed the Lagrange symplectic structure, and then to the multi-symplectic structure. He finally proposed a symplectic structure that meets the requirement of the Lagrangian form from the variational principle by giving up the boundary conditions. On the other hand, T. Bridge and others used the multisymplectic structure to derive directly the multi-symplectic Hamilton equations, and then constructed the difference schemes that preserve the symplectic structure in both time and space. Both methods can be regarded as equivalent in the algorithmic sense.

Now, in this monograph, most of the content refers only to ordinary differential equations. Kang Feng and his algorithms research group working on the symplectic algorithm did some foundation work. In particular, I would like to point out three negative theorems: “ non-existence of energy preserving scheme”, “ non-existence of multistep linear symplectic scheme”, and “ non-existence of volume-preserving scheme form rational fraction expression”. In addition, generating function theory is not only rich in analytical mechanics and Hamilton–Jacobi equations. At the same time, the construction of symplectic schemes provides a tool for any order accuracy difference scheme. The formal power series proposed by Kang Feng had a profound impact on the later developed “ backward error series” work ,“ modified equation” and “ modified integrator”.

The symplectic algorithm developed very quickly, soon to be extended to the geometric method. The structure preserving algorithm (not only preserving the geometrical structure, but also the physical structure, etc.) preserves the algebraic structure to present the Lie group algorithm, and preserves the differential complex algorithm. Many other prominent people have contributed to the symplectic method in addition to those mentioned above. There are various methods related to structure preserving algorithms and for important contributions the readers are referred to R. McLachlan & GRW Quispel “ Geometric integration for ODEs” and T. Bridges & S. Reich “ Numerical methods for Hamiltonian PDEs”.

The book describes the symplectic geometric algorithms and theoretical basis for a number of related algorithms. Most of the contents are a collection of lectures given by Kang Feng at Beijing University. Most of other sections are a collection of papers which were written by group members.

Compared to the previous Chinese version, the present English one has been improved in the following respects. First of all, to correct a number of errors and mistakes contained in the Chinese version. Besides, parts of Chapter 1 and Chapter 2 were removed, while some new content was added to Chapter 4, Chapter 7, Chapter 8, Chapter 9 and Chapter 10. More importantly, four new chapters — Chapter 13 to Chapter 16 were added. Chapter 13 is devoted to the KAM theorem for the symplectic algorithm. We invited Professor Zaijiu Shang , a former PhD student of Kang Feng to compose this chapter. Chapter 14 is called Variational Integrator. This chapter reflects the work of the Nobel Prize winner Professor Zhengdao Li who proposed in the 1980s to preserve the energy variational integrator, but had not explained at that time that it had a Lagrange symplectic type, which satisfied the Lagrange symplectic structure. Together with J. Marsden he proposed the variational integrator trail connection, which leads from the variational integrator. Just like J. Marsden, he hoped this can link up with the finite element method. Chapter 15 is about Birkhoffian Systems, describing a class of dissipative structures for Birkohoffian systems to preserve the dissipation of the Birkhoff structure. Chapter 16 is devoted to Multisymplectic and Variational Integrators, providing a summary of the widespread applications of multisymplectic integrators in the infinitely dimensional Hamiltonian systems.

We would also like to thank every member of the Kang Feng’s research group for symplectic algorithms: Huamo Wu, Daoliu Wang, Zaijiu Shang, Yifa Tang, Jialin Hong, Wangyao Li, Min Chen, Shuanghu Wang, Pingfu Zhao, Jingbo Chen, Yushun Wang, Yajuan Sun, Hongwei Li, Jianqiang Sun, Tingting Liu, Hongling Su, Yimin Tian; and those who have been to the USA: Zhong Ge, Chunwang Li, Yuhua Wu, Meiqing Zhang, Wenjie Zhu, Shengtai Li, Lixin Jiang, and Haibin Shu. They made contributions to the symplectic algorithm over different periods of time.

The authors would also like to thank the National Natural Science Foundation, the National Climbing Program projects, and the State’s Key Basic Research Projects for their financial support. Finally, the authors would also like to thank the Mathematics and Systems Science Research Institute of the Chinese Academy of Sciences, the Computational Mathematics and Computational Science and Engineering Institute, and the State Key Laboratory of Computational Science and Engineering for their support.

The editors of this book have received help from E. Hairer, who provided a template from Springer publishing house. I would also like to thank F. Holzwarth at Springer publishing house and Linbo Zhang of our institute, and others who helped me successfully publish this book.

For the English translation, I thank Dr. Shengtai Li for comprehensive proofreading and polishing, and the editing of Miss Yi Jin. For the English version of the publication I would also like to thank the help of the Chinese Academy of Sciences Institute of Mathematics. Because Kang Feng has passed away, it may not be possible to provide a comprehensive representation of his academic thought, and the book will inevitably contain some errors. I accept the responsibility for any errors and welcome criticism and corrections.

We would also like to thank Springer Beijing Representation Office and Zhejiang Science and Technology Publishing House, which made a great contribution to the Chinese scientific cause through the publication of this manuscript. We are especially grateful to thank Lisa Fan, W. Y. Zhou, L. L. Liu and X. M. Lu for carefully reading and finding some misprints, wrong signs and other mistakes.

This book is supported by National Natural Science Foundation of China under grant No.G10871099 ; supported by the Project of National 863 Plan of China (grant No.2006AA09A102-08); and supported by the National Basic Research Program of China (973 Program) (Grant No. 2007CB209603).

Mengzhao Qin   
Institute of Computational Mathematics and Scientific Engineering Computing   
Beijing   
September 20, 2009

# Contents

Introduction . . . 1   
Bibliography 35

# 1. Preliminaries of Differentiable Manifolds . . 39

1.1 Differentiable Manifolds . . 40

1.1.1 Differentiable Manifolds and Differentiable Mapping . . . . 40   
1.1.2 Tangent Space and Differentials . 4 3   
1.1.3 Submanifolds . 46   
1.1.4 Submersion and Transversal . 5 1

Tangent Bundle . . 56

1.2.1 Tangent Bundle and Orientation . 56   
1.2.2 Vector Field and Flow 62

Exterior Product . . 64

1.3.1 Exterior Form . . 6 6   
1.3.2 Exterior Algebra . . 6 8

1.4 Foundation of Differential Form 7 5

1.4.1 Differential Form . 7 6   
1.4.2 The Behavior of Differential Forms under Maps 8 0   
1.4.3 Exterior Differential . . 8 2   
1.4.4 Poincare Lemma and Its Inverse Lemma ´ . 8 4   
1.4.5 Differential Form in $\mathbf { R } ^ { 3 }$ 8 6   
1.4.6 Hodge Duality and Star Operators 88   
1.4.7 Codifferential Operator $\delta$ 8 9   
1.4.8 Laplace–Beltrami Operator . 9 0

1.5 Integration on a Manifold . 91

1.5.1 Geometrical Preliminary . 9 1   
1.5.2 Integration and Stokes Theorem . 9 3   
1.5.3 Some Classical Theories on Vector Analysis 9 6

1.6 Cohomology and Homology 98

1.7 Lie Derivative . 99

1.7.1 Vector Fields as Differential Operator . 99   
1.7.2 Flows of Vector Fields . 101   
1.7.3 Lie Derivative and Contraction . . 103

Bibliography

# Symplectic Algebra and Geometry Preliminaries 113

2.1 Symplectic Algebra and Orthogonal Algebra . . . . 113

2.1.1 Bilinear Form . 113   
2.1.2 Sesquilinear Form . 116   
2.1.3 Scalar Product, Hermitian Product . . 117   
2.1.4 Invariant Groups for Scalar Products . . 119   
2.1.5 Real Representation of Complex Vector Space . 121   
2.1.6 Complexification of Real Vector Space and Real Linear   
Transformation . . 123   
2.1.7 Lie Algebra for $G L ( n , \mathbf { F } )$ . . 124   
2.2 Canonical Reductions of Bilinear Forms . 128   
2.2.1 Congruent Reductions . . 129   
2.2.2 Congruence Canonical Forms of Conformally Symmet  
ric and Hermitian Matrices . . . 130   
2.2.3 Similar Reduction to Canonical Forms under Orthogo  
nal Transformation . . 134   
2.3 Symplectic Space . . . . 137   
2.3.1 Symplectic Space and Its Subspace . . 137   
2.3.2 Symplectic Group . 144   
2.3.3 Lagrangian Subspaces . 147   
2.3.4 Special Types of $S p ( 2 n )$ . . 148   
2.3.5 Generators of $S p ( 2 n )$ . 155   
2.3.6 Eigenvalues of Symplectic and Infinitesimal Matrices . . . 158   
2.3.7 Generating Functions for Lagrangian Subspaces . . . 160   
2.3.8 Generalized Lagrangian Subspaces . 162   
Bibliography . 164

# Hamiltonian Mechanics and Symplectic Geometry . . 165

3.1 Symplectic Manifold . . 165

3.1.1 Symplectic Structure on Manifolds 165   
3.1.2 Standard Symplectic Structure on Cotangent Bundles . . . . 166   
3.1.3 Hamiltonian Vector Fields . . 167   
3.1.4 Darboux Theorem . 168   
3.2 Hamiltonian Mechanics on $\mathbf { R } ^ { 2 n }$ . 168   
3.2.1 Phase Space on $\mathbf { R } ^ { 2 n }$ and Canonical Systems . 169   
3.2.2 Canonical Transformation . 172   
3.2.3 Poisson Bracket . . 177   
3.2.4 Generating Functions . . . 180   
3.2.5 Hamilton–Jacobi Equations . 182   
Bibliography . 185

# 4. Symplectic Difference Schemes for Hamiltonian Systems . . . . . 187

4.1 Background . . 187   
4.1.1 Element and Notation for Hamiltonian Mechanics . . . . . . 187

4.1.2 Geometrical Meaning of Preserving Symplectic Structure $\omega$ . 189

4.1.3 Some Properties of a Symplectic Matrix . . . . . 190

Symplectic Schemes for Linear Hamiltonian Systems . . . . . . . . . . . 192

4.2.1 Some Symplectic Schemes for Linear Hamiltonian Systems . . 192 4.2.2 Symplectic Schemes Based on Pade Approximation ´ . . . . . 193 4.2.3 Generalized Cayley Transformation and Its Application . . 197 em . 200

Explicit Symplectic Scheme for Hamiltonian System . . . . . . . . 203

4.4.1 Systems with Nilpotent of Degree 2 . 204   
4.4.2 Symplectically Separable Hamiltonian Systems . . 205   
4.4.3 Separability of All Polynomials in $\mathbf { R } ^ { 2 n }$ . 207   
4.5 Energy-conservative Schemes by Hamiltonian Difference . 209   
Bibliography . 211

# 5. The Generating Function Method . . 213

5.1 Linear Fractional Transformation . 213   
5.2 Symplectic, Gradient Mapping and Generating Function . 215   
5.3 Generating Functions for the Phase Flow . 221   
5.4 Construction of Canonical Difference Schemes . . 226   
5.5 Further Remarks on Generating Function . . 231   
5.6 Conservation Laws . 234   
5.7 Convergence of Symplectic Difference Schemes . . 239   
5.8 Symplectic Schemes for Nonautonomous System . 242   
Bibliography . 247

# 6. The Calculus of Generating Functions and Formal Energy . . . . . 249

6.1 Darboux Transformation . . . 249   
6.2 Normalization of Darboux Transformation . . . 251   
6.3 Transform Properties of Generator Maps and Generating Functions 255   
6.4 Invariance of Generating Functions and Commutativity of Gener  
ator Maps . . . 261   
6.5 Formal Energy for Hamiltonian Algorithm . 264   
6.6 Ge–Marsden Theorem . . 273   
Bibliography . 275

# 7. Symplectic Runge–Kutta Methods . 277

7.1 Multistage Symplectic Runge–Kutta Method . . . 277

7.1.1 Definition and Properties of Symplectic R–K Method . . . . 277   
7.1.2 Symplectic Conditions for R–K Method . . 281   
7.1.3 Diagonally Implicit Symplectic R–K Method . 284   
7.1.4 Rooted Tree Theory . . . 288   
7.1.5 Simplified Conditions for Symplectic R–K Method . . . . . 297

#

7.2 Symplectic P–R–K Method . 302   
7.2.1 P–R–K Method . 302   
7.2.2 Symplified Order Conditions of Explicit Symplectic R–K   
Method . 307   
7.3 Symplectic R–K–N Method . . 319   
7.3.1 Order Conditions for Symplectic R–K–N Method . . 319   
7.3.2 The 3-Stage and 4-th order Symplectic R–K–N Method . 323   
7.3.3 Symplified Order Conditions for Symplectic R–K–N   
Method . . 327   
7.4 Formal Energy for Symplectic R–K Method . 333   
7.4.1 Modified Equation . 334   
7.4.2 Formal Energy for Symplectic R–K Method . 339   
7.5 Definition of $a ( t )$ and $b ( t )$ . 345   
7.5.1 Centered Euler Scheme . . 345   
7.5.2 Gauss–Legendre Method . 346   
7.5.3 Diagonal Implicit R–K Method . 347   
7.6 Multistep Symplectic Method . 347   
7.6.1 Linear Multistep Method . . 347   
7.6.2 Symplectic LMM for Linear Hamiltonian Systems . . . . . . 348   
7.6.3 Rational Approximations to Exp and Log Function . . . . . . 352   
Bibliography 357

# 8. Composition Scheme . . . 365

8.1 Construction of Fourth Order with 3-Stage Scheme . . 365   
8.1.1 For Single Equation . . . 365   
8.1.2 For System of Equations . . 370   
8.2 Adjoint Method and Self-Adjoint Method . . 372   
8.3 Construction of Higher Order Schemes . 377   
8.4 Stability Analysis for Composition Scheme . . 388   
8.5 Application of Composition Schemes to PDE . 396   
8.6 H-Stability of Hamiltonian System . 401   
Bibliography . 405

# 9. Formal Power Series and B-Series . . . . . 407

9.1 Notation . . . 407   
9.2 Near-0 and Near-1 Formal Power Series . . 409   
9.3 Algorithmic Approximations to Phase Flows . . 414   
9.3.1 Approximations of Phase Flows and Numerical Method . 414   
9.3.2 Typical Algorithm and Step Transition Map . . 415   
9.4 Related B-Series Works . . 417   
9.4.1 The Composition Laws . . 418   
9.4.2 Substitution Law . 432   
9.4.3 The Logarithmic Map . 434

Bibliography . 441

# 10. Volume-Preserving Methods for Source-Free Systems . . . . 443

10.1 Liouville’s Theorem . 443   
10.2 Volume-Preserving Schemes . 444   
10.2.1 Conditions for Centered Euler Method to be Volume   
Preserving . . 444   
10.2.2 Separable Systems and Volume-Preserving Explicit Meth  
ods . . 447   
10.3 Source-Free System . . 449   
10.4 Obstruction to Analytic Methods . . 450   
10.5 Decompositions of Source-Free Vector Fields 452   
10.6 Construction of Volume-Preserving Schemes . . 454   
10.7 Some Special Discussions for Separable Source-Free Systems . . . . 458   
10.8 Construction of Volume-Preserving Scheme via Generating Func  
tion . 460   
10.8.1 Fundamental Theorem . . 460   
10.8.2 Construction of Volume-Preserving Schemes . . . 464   
10.9 Some Volume-Preserving Algorithms . . . 467   
10.9.1 Volume-Preserving R–K Methods . 467   
10.9.2 Volume-Preserving 2-Stage P–R–K Methods . 471   
10.9.3 Some Generalizations . 473   
10.9.4 Some Explanations . 474   
Bibliography . 476

# 11. Contact Algorithms for Contact Dynamical Systems . . 477

11.1 Contact Structure . . . . 477   
11.1.1 Basic Concepts of Contact Geometry . 477   
11.1.2 Contact Structure . . 480   
11.2 Contactization and Symplectization . . 484   
11.3 Contact Generating Functions for Contact Maps . 488   
11.4 Contact Algorithms for Contact Systems . 492   
11.4.1 $\overline { { Q } }$ Contact Algorithm . . 493   
11.4.2 $\overline { { P } }$ Contact Algorithm . . 493   
11.4.3 $\overline { C }$ Contact Algorithm . . 493   
11.5 Hamilton–Jacobi Equations for Contact Systems . 494   
. 497

Bibliography

# 12. Poisson Bracket and Lie–Poisson Schemes . . . 499

12.1 Poisson Bracket and Lie–Poisson Systems . . 499   
12.1.1 Poisson Bracket . . 499   
12.1.2 Lie–Poisson Systems . 501   
12.1.3 Introduction of the Generalized Rigid Body Motion . . . . . 505   
12.2 Constructing Difference Schemes for Linear Poisson Systems . . . . 507   
12.2.1 Constructing Difference Schemes for Linear Poisson   
Systems . . . 508

12.2.2 Construction of Difference Schemes for General Poisson Manifold . 509

12.2.3 Answers of Some Questions . . . 511

Generating Function and Lie–Poisson Scheme . . . 514

12.3.1 Lie–Poisson–Hamilton–Jacobi (LPHJ) Equation and Generating Function . . 514   
12.3.2 Construction of Lie–Poisson Schemes via Generating Function . 519

12.4 Construction of Structure Preserving Schemes for Rigid Body . . . . 523

12.4.1 Rigid Body in Euclidean Space . 523   
12.4.2 Energy-Preserving and Angular Momentum-Preserving   
Schemes for Rigid Body . . 525   
12.4.3 Orbit-Preserving and Angular-Momentum-Preserving Ex  
plicit Scheme . . 527   
12.4.4 Lie–Poisson Schemes for Free Rigid Body . 530   
12.4.5 Lie–Poisson Scheme on Heavy Top . . 535   
12.4.6 Other Lie–Poisson Algorithm . . 538   
12.5 Relation Among Some Special Group and Its Lie Algebra . . 543   
12.5.1 Relation Among $S O ( 3 ) , s o ( 3 )$ and $S H _ { 1 } , S U ( 2 )$ . 543   
12.5.2 Representations of Some Functions in $S O ( 3 )$ . 545   
Bibliography . 547

# 13. KAM Theorem of Symplectic Algorithms . 549

13.1 Brief Introduction to Stability of Geometric Numerical Algorithms 549   
13.2 Mapping Version of the KAM Theorem . 551   
13.2.1 Formulation of the Theorem . . 551   
13.2.2 Outline of the Proof of the Theorems . 554   
13.2.3 Application to Small Twist Mappings . 558   
13.3 KAM Theorem of Symplectic Algorithms for Hamiltonian Systems559   
13.3.1 Symplectic Algorithms as Small Twist Mappings . 560   
13.3.2 Numerical Version of KAM Theorem . 564   
13.4 Resonant and Diophantine Step Sizes . . 568   
13.4.1 Step Size Resonance . 568   
13.4.2 Diophantine Step Sizes . 569   
13.4.3 Invariant Tori and Further Remarks . 574   
Bibliography . 578

# 14. Lee-Variational Integrator . 581

14.1 Total Variation in Lagrangian Formalism . . 581   
14.1.1 Variational Principle in Lagrangian Mechanics . 581   
14.1.2 Total Variation for Lagrangian Mechanics . 583   
14.1.3 Discrete Mechanics and Variational Integrators . 586   
14.1.4 Concluding Remarks . . 591   
14.2 Total Variation in Hamiltonian Formalism . 591   
14.2.1 Variational Principle in Hamiltonian Mechanics . 591   
14.2.2 Total Variation in Hamiltonian Mechanics . 593   
14.2.3 Symplectic-Energy Integrators . . 596   
14.2.4 High Order Symplectic-Energy Integrator . 600   
14.2.5 An Example and an Optimization Method . 603   
14.2.6 Concluding Remarks . . 605   
14.3 Discrete Mechanics Based on Finite Element Methods . . 606   
14.3.1 Discrete Mechanics Based on Linear Finite Element . . . . . 606   
14.3.2 Discrete Mechanics with Lagrangian of High Order . . . . . 608   
14.3.3 Time Steps as Variables . . 613   
14.3.4 Conclusions . 614   
Bibliography . 615

# 15. Structure Preserving Schemes for Birkhoff Systems . . . . . 617

15.1 Introduction . 617   
15.2 Birkhoffian Systems . 618   
15.3 Generating Functions for $K ( z , t )$ -Symplectic Mappings . 621   
15.4 Symplectic Difference Schemes for Birkhoffian Systems . . 625   
15.5 Example . 629   
15.6 Numerical Experiments . 634   
Bibliography . 639

# 16. Multisymplectic and Variational Integrators . . . . 641

16.1 Introduction . 641   
16.2 Multisymplectic Geometry and Multisymplectic Hamiltonian Sys  
tems . . 642   
16.3 Multisymplectic Integrators and Composition Methods . 646   
16.4 Variational Integrators . . 652   
16.5 Some Generalizations . 654   
Bibliography . 658

Symbol . . . 663

Index . . 669

# Introduction

The main theme of modern scientific computing is the numerical solution of various differential equations of mathematical physics bearing the names, such as Newton, Euler, Lagrange, Laplace, Navier–Stokes, Maxwell, Boltzmann, Einstein, Schrodinger, ¨ Yang-Mills, etc. At the top of the list is the most celebrated Newton’s equation of motion. The historical, theoretical and practical importance of Newton’s equation hardly needs any comment, so is the importance of the numerical solution of such equations. On the other hand, starting from Euler, right down to the present computer age, a great wealth of scientific literature on numerical methods for differential equations has been accumulated, and a great variety of algorithms, software packages and even expert systems has been developed. With the development of the modern mechanics, physics, chemistry, and biology, it is undisputed that almost all physical processes, whether they are classical, quantum, or relativistic, can be represented by an Hamiltonian system. Thus, it is important to solve the Hamiltonian system correctly.

# 1. Numerical Method for the Newton Equation of Motion

In the spring of 1991, the first author $[ \mathrm { F e n 9 2 b } ]$ presented a plenary talk on how to compute the numerical solution of Newton classical equation accurately at the Annual Physics Conference of China in Beijing.

It is well known that numerically solving so-called mathematics-physics equations has become a main topic in modern scientific computation. The Newton equation of motion is one of the most popular equations among various mathematics-physics equations. It can be formulated as a group of second-order ordinary differential equations, $f = m a = m { \ddot { x } }$ . The computational methods of the differential equations advanced slowly in the past due to the restriction of the historical conditions. However, a great progress was made since Euler, due to contributions from Adams, Runge, Kutta, and Stomer, etc.. This is especially true since the introduction of the modern com- ¨ puter for which many algorithms and software packages have been developed. It is said that the three-body problem is no longer a challenging problem and can be easily computed. Nevertheless, we propose the following two questions:

$1 ^ { \circ }$ Are the current numerical algorithms suitable for solving the Newton equation of motion?

$2 ^ { \circ }$ How can one calculate the Newton equation of motion more accurately?

It seems that nobody has ever thought about the first issue seriously, which may be the reason why the second issue has never been studied systematically. In this book, we will study mainly the fundamental but more difficult Newton equation of motion that is in conservative form. First, the conservative Newton equation has two equivalent mathematical representations: a Lagrange variation form and a Hamiltonian form. The latter transforms the second-order differential equations in physical space into a group of the first-order canonical equations in phase space. Different representations for the same physical law can lead to different computational techniques in solving the same problem, which can produce different numerical results. Thus making a wise and reasonable choice among various equivalent mathematical representations is extremely important in solving the problem correctly.

We choose the Hamiltonian formulation as our basic form in practice based on the fact that the Hamiltonian equations have symmetric and clean form, where the physical laws of the motion can be easily represented. Secondly, the Hamiltonian formulation is more general and universal than the Newton formulation. It can cover the classical, relativistic, quantum, finite or infinite dimensional real physical processes where dissipation effect can be neglected. Therefore, the success of the numerical methods for Hamiltonian equations has broader development and application perspectives. Thus, it is very surprising that the numerical algorithms for Hamiltonian equations are almost nonexistent after we have searched various publications. This motivates us to study the problem carefully to seek the answers to the previous two questions.

Our approach is to use the symplectic geometry, which is the geometry in phase space. It is based on the anti-symmetric area metric, which is in contrast to the symmetric length metrics of Euclid and Riemann geometry. The basic theorem of the classic mechanics can be described as “the dynamic evolution of all Hamiltonian systems preserves the symplectic metrics, which means it is a symplectic (canonical) transformation”. Hence the correct discretization algorithms to all the Hamiltonian systems should be symplectic transformation. Such algorithms are called symplectic (canonical) algorithms or Hamiltonian algorithms. We have intentionally analyzed and evaluated the derivation of the Hamiltonian algorithm within the symplectic structures. The fact proved that this approach is correct and fruitful. We have derived a series of symplectic algorithms, found out their properties, laid out their theoretical foundation, and tested them with extremely difficult numerical experiments.

In order to compare the symplectic and non-symplectic algorithm, we proposed eight numerical experiments: harmonic oscillator, nonlinear Duffing oscillator, Huygens oscillator, Cassini oscillator, two dimensional multi-crystal and semi-crystal lattice steady flow, Lissajous image, geodesic flow on ellipsoidal surface, and Kepler motion. The numerical experiments demonstrate the superiority of the symplectic algorithm. All traditional non-symplectic algorithms fail without exception, especially in preserving global property and structural property, and long-term tracking capability, regardless of their accuracy. However, all the symplectic algorithms passed the tests with long-term stable tracking capability. These tests clearly demonstrate the superiority of the symplectic algorithms.

Almost all of the traditional algorithms are non-symplectic with few exceptions. They are designed for the asymptotic stable system which has dissipation mechanism to maintain stability, whereas the Hamiltonian system does not have the asymptotic stability. Hence all these algorithms inevitably contain artificial numerical dissipation, fake attractors, and other parasitics effects of non-Hamiltonian system. All these effects lead to seriously twist and serious distortion in numerical results. They can be used in short-term transient simulation, but are not suitable and can lead to wrong conclusions for long-term tracking and global structural property research. Since the Newton equation is equivalent to Hamiltonian equation, the answer to the first question is “No”, which is quite beyond expectation.

The symplectic algorithm does not have any artificial dissipation so that it can congenitally avoid all non-symplectic pollution and become a “clean” algorithm. Hamiltonian system has two types of conservation laws: one is the area invariance in phase space, i.e., Liouville–Poincare conservation law; the other is the motion invariance ´ which includes energy conservation, momentum and angular momentum conservation, etc. We have proved that all symplectic algorithms have their own invariance, which has the same convergence to the original theoretical invariance as the convergence order of the numerical algorithm. We have also proved that the majority of invariant tori of the near integrable system can be preserved, which is a new formulation of the famous KAM (Kolmogorov–Arnorld–Moser) theorem[Kol54b,Kol54a,Arn63,Mos62] . All of these results demonstrate that the structure of the discrete Hamiltonian algorithm is completely parallel to the conservation law, and is very close to the original form of the Hamiltonian system. Moreover, theoretically speaking, it has infinite longterm tracking capability. Hence, a correct numerical method to solve the Newton equation is to Hamiltonize the equation first and then use the Hamiltonian algorithm. This is the answer to the second question. We will describe in more detail the KAM theory of symplectic algorithms for Hamiltonian systems in Chapter 13. In the following we present some examples to compare the symplectic algorithm and other non-symplectic algorithms in solving Newton equation of motion.

# (1) Calculation of the Harmonic oscillator’s elliptic orbit

Calculation of the Harmonic oscillator’s elliptic orbit (Fig. 0.1(a)) uses Runge–Kutta method (R–K) with a step size 0.4. The output is at 3,000 steps. It shows artificial dissipation, shrinking of the orbit. Fig. 0.1(b) shows the results using Adams method with a step size 0.2. It is anti-dissipative and the orbit is scattered out. Fig. 0.1(c) shows the results of two-step central difference (leap-frog scheme). This scheme is symplectic to linear equations. The results are obtained with a step size 0.1. It shows that the results of three stages for 10,000,000 steps: the initial 1,000 steps, the middle 1,000 steps, and the final 1,000 steps. They are completely in agreement.

# (2) The elliptic orbit for the nonlinear oscillator

Fig. 0.2(a) shows the results of two-step central-difference. This scheme is nonsymplectic for nonlinear equations. The output is for step size 0.2 and 10,000 steps. Fig. 0.2(a) shows the initial 1,000 steps and Fig. 0.2(b) shows the results between 9,000 to 10,000 steps. Both of them show the distortion of the orbit. Fig. 0.2(c) is for the second-order symplectic algorithm with 0.1 step size, 1,000 steps.

![](images/f7dec0b3011d3402e9f2c5d66c129fa198bfb4f8ffe169fa8ae0430a5f2635c5.jpg)  
Fig. 0.1. Calculation of the Harmonic oscillator’s elliptic orbit

![](images/aff197bf021693098cb4cec47d2bd19737b17a9e77deb0fb1e5b968a6d73fd1b.jpg)  
Fig. 0.2. Calculation of the nonlinear oscillator’s elliptic orbit

![](images/c219f61303a61ad2f3714468c5dffc59dda1fce1e35d43596490f1c7391ac3f2.jpg)  
Fig. 0.3. Calculation of the nonlinear Huygens oscillator

# (3) The oval orbit of the Huygens oscillator

Using the R–K method, the two fixed points on the horizontal axes become two fake attractors. The probability of the phase point close to the two attractors is the same. The same initial point outside the separatrix is attracted randomly either to the left or to the right. Fig. 0.3(a) shows the results with a step size 0.10000005 and 900,000 steps, which approach the left attractor. Fig. 0.3(b) shows the results with a step size 0.10000004 and 900,000 steps, which approach the right attractor. Fig. 0.3(c) shows the results of the second-order symplectic algorithm with a step size 0.1. Four typical orbits are plotted and each contains 100,000,000 steps: for every orbit first 500 steps, the middle 500 steps, and the final 500 steps. They are in complete agreement.

# (4) The dense orbit of the geodesic for the ellipsoidal surface

The dense orbit of the geodesic for the ellipsoidal surface with irrational frequency ratio. The square of frequency ratio is 5/16, step size is 0.05658, 10,000 steps. Fig.0.4(a) is for the R–K method which does not tend to dense. Fig. 0.4(b) is for the symplectic algorithm which tends to dense.

![](images/a38938a214c1d36308994416dd9974c88b449f9d9d683a2079e4c341c710762b.jpg)  
Fig. 0.4. Geodesics on ellipsoid, frequency ratio ${ \sqrt { 5 } } : 4$ , non dense (a), dense orbit (b)

# (5) The close orbit of the geodesic for the ellipsoidal surface

The close orbit of the geodesic for the ellipsoidal surface with rational frequency ratio. The frequency ratio is 11/16, step size is 0.033427, 100,000 steps and 25 cycles. Fig.0.5(a) is for the R–K method which does not lead to the close orbit. Fig. 0.5(b) is for the symplectic algorithm which leads to the close orbit.

![](images/07b11a56bfc605fe3f3a371cc2d3b3d0607964318dd3c2b88df4b67e0ed9a222.jpg)  
Fig. 0.5. Geodesics on ellipsoid, frequency ratio 11:16, non closed (a), closed orbit (b)

# (6) The close orbit of the Keplerian motion

The close orbit of the Keplerian motion with rational frequency ratio. The frequency ratio is 11/20, step size is 0.01605, 240,000 steps and 60 cycles. Fig. 0.6(a) is for the R–K method which does not lead to the close orbit. Fig. 0.6(b)is for the symplectic method which leads to the close orbit.

![](images/d036eebee4ed2f1dca84b641a7fffe09b2cf2acfbc18914056869498f8cea682.jpg)  
Fig. 0.6. Geodesics on ellipsoid, frequency ratio 11:20, non closed (a), closed orbit (b)

# 2. History of the Hamiltonian Mechanics

We first consider the three formulations of the classical mechanics. Assume a motion has $n$ degrees of freedom. The position is denoted as $q = ( q _ { 1 } , \cdots , q _ { n } )$ . The potential function is $V = V ( q )$ . Then we have

$$
m { \frac { \mathrm { d } ^ { 2 } q } { \mathrm { d } t ^ { 2 } } } = - { \frac { \partial } { \partial q } } V ,
$$

which is the standard formulation of the motion. It is a group of second-order differential equations in space $\mathbf { R } ^ { n }$ . It is usually called the standard formulation of the classical mechanics, or Newton formulation.

Euler and Lagrange introduced an action on the difference between the kinetic energy and potential energy

$$
L ( q , \dot { q } ) = T ( \dot { q } ) - V ( q ) = \frac { 1 } { 2 } ( \dot { q } , M \dot { q } ) - V ( q ) .
$$

Using the variational principle the above equation can be written as

$$
\frac { \mathrm { d } } { \mathrm { d } t } \frac { \partial L } { \partial \dot { q } } - \frac { \partial L } { \partial q } = 0 ,
$$

which is called the variational form of the classical mechanics, i.e., the Lagrange form.

In the 19th century, Hamilton proposed another formulation. He used the momentum $p = M { \dot { q } }$ and the total energy $H = T + V$ to formulate the equation of motion as

$$
\dot { p } = - \frac { \partial H } { \partial q } , \quad \dot { q } = \frac { \partial H } { \partial p } ,
$$

which is called Hamiltonian canonical equations. This is a group of the first-order differential equations in $2 n$ phase space $\left( p _ { 1 } , \cdots , p _ { n } , q _ { 1 } , \cdots , q _ { n } \right)$ . It has simple and symmetric form.

The three basic formulations of the classical mechanics have been described in almost all text-books on theoretical physics or theoretical mechanics. These different mathematical formulations describe the same physics law but provide different approaches in problem solving. Thus equivalent mathematical formulation can have different effectiveness in computational methods. We have verified this in our own simulations.

The first author did extensive research on Finite Element Method (FEM) in the 1960s [Fen65] which represents a systematic algorithm for solving equilibrium problem. Physical problems of this type have two equivalent formulations: Newtonian, i.e., solving the second-order elliptic equations, and variational formulation, i.e., minimization principle in energy functional. The key to the success of FEM in both theoretical and computational methods lies in using a reasonable variational formulation as the basic principle. After that, he had attempted to apply the FEM idea to the dynamic problem of continuum media mechanics, but not yet achieved the corresponding success, which appears to be difficult to accomplish even today. Therefore, the reasonable choice for computational method of dynamic problem might be the Hamiltonian formulation. Initially it is a conjecture and requires verification from the computational experiments. We have investigated how others evaluated the Hamiltonian system in history. First we should point out that Hamilton himself proposed his theory based on the geometric optics and then extended it to mechanics that appears to be a very different field. In 1834 Hamilton said, “This set of idea and method has been applied to optics and mechanics. It seems it can be applied to other areas and developed into an independent knowledge by the mathematicians” $\scriptstyle \left[ \mathrm { H a m } 3 4 \right]$ . This is just his expectation, and other peers in the same generation seemed indifferent to this set of theory, which was “beautiful but useless”[Syn44] to them. Klein, a famous mathematician, while giving a high appreciation to the mathematical elegance of the theory, suspected its applicability, and said: “. . . a physicist, for his problems, can extract from these theories only very little, and an engineer nothing”[Kle26] . This claim has been proved wrong at least in physics aspect in the later history. The quantum mechanics developed in the 1920s under the framework of the Hamiltonian formulation. One of the founders of the quantum mechanics, Schrodinger said, “Hamiltonian principle has been the foundation for ¨ modern physics . . . If you want to solve any physics problem using the modern theory, you must represent it using the Hamiltonian formulation”[Sch44] .

# 3. The Importance of the Hamiltonian System

The Hamiltonian system is one of the most important systems among all the dynamics systems. All real physical processes where the dissipation can be neglected can be formulated as Hamiltonian system. Hamiltonian system has broad applications, which include but are not limited to the structural biology, pharmacology, semiconductivity, superconductivity, plasma physics, celestial mechanics, material mechanics, and partial differential equations. The first five topics have been listed as “Grand Challenges” in Research Project of American government.

The development of the physics verifies the importance of the Hamiltonian systems. Up to date, it is undisputed that all real physical processes where the dissipation can be neglected can be written as Hamiltonian formulation, whether they have finite or infinite degrees of freedom.

The problem with finite degrees of freedom includes celestial and man-made satellite mechanics, rigid body, and multi-body (including the robots), geometric optics, and geometric asymptotic method (including ray-tracing approximation method in wave-equation, and WKB equation of quantum mechanics), confinement of the plasma, the design of the high speed accelerator, automatic control, etc.

The problem with infinite degrees of freedom includes ideal fluid dynamics, elastic mechanics, electrical mechanics, quantum mechanics and field theory, general relativistic theory, solitons and nonlinear waves, etc.

All the above examples show the ubiquitous and nature of the Hamiltonian systems. It has the advantage that different physics laws can be represented by the same mathematical formulation. Thus we have confidence to say that successful development of the numerical methods for Hamiltonian system will have extremely broad applications.

We now discuss the status of the numerical method for Hamiltonian systems. Hamiltonian systems, including finite and infinite dimensions, are Ordinary Differential Equations (ODE) or Partial Differential Equations (PDE) with special form. The research on the numerical method of the differential equations started in the 18th century and produced abundant publications. However, we find that few of them discuss the numerical method specifically for Hamiltonian systems. This status is in sharp contrast with the importance of the Hamiltonian system. Therefore, it is appealing and worthy to investigate and develop numerical methods for this virgin field.

# 4. Technical Approach — Symplectic Geometry Method

The foundation for the Hamiltonian system is symplectic geometry, which is increasingly flourishing in both theory and practice. The history of symplectic geometry can be traced back to Astronomer Hamilton in the 19th century. In order to study the Newton mechanics, he introduced generalized coordinates and generalized momentums to represent the energy of the system, which is now called Hamiltonian function now. For a system with $n$ degrees of freedom, the $n$ generalized coordinates and momentums are spanned into a $2 n$ phase space. Thus the Newton mechanics becomes the geometry in phase space. In terms of the modern concept, this is a kind of symplectic geometry. Later, Jacobi, Darboux, Poincare, Cartan, and Weyl did a lot of research on this topic ´ from different points of view (algebra and geometry). However, the major development of the modern symplectic geometry started with the discovery of KAM theorem (1950s to the beginning of 1960s). In the 1970s, in order to research Fourier integral operator, quantum representation of the geometry, group representation theory, classification of the critical points, Lie Algebra, etc., people did a lot of work on symplectic geometry (e.g., Arnold[Arn89] , Guillemin[GS84] , Weinstein[Wei77] , Marsden[AM78] , etc.), which promoted the development in these areas. In the 1980s, the research on total symplectic geometry emerged subsequently, such as the research on “coarse” symplectic (e.g., Gromov et al.), fix point for symplectic map (e.g., Conley, Zehnder’s Arnold conjecture), the convexity of the matrix mapping (e.g., Atiyah, Guillemin, Sternberg et al.). The research on symplectic geometry is not only extremely enriched and vital, but its application is also widely applied to different areas, such as celestial mechanics, geometric optics, plasma, the design of high speed accelerators, fluid dynamics, elastic mechanics, optimal control, etc.

Weyl[Wey39] said the following in his monograph on the history of the symplectic group: “I called it complex group initially. Because this name can be confused with the complex number, I suggest using symplectic, a Greek word with the same meaning.”

An undocumented law for the modern numerical method is that the discretized problem should preserve the properties of the original problem as much as possible. To achieve this goal, the discretization should be performed in the same framework as the original problem. For example, the finite element method treats the discretized and original problem in the same framework of the Sobolev space so that the basic properties of the original problem, such as symmetry, positivity, and conservativity, etc., are all preserved. This not only ensures the effectiveness and reliability in practice, but also provides a theoretical foundation.

Based on the above principle, the constructed numerical methods for the Hamiltonian system should preserve the Hamiltonian structure, which we call “Hamiltonian algorithm”. The Hamiltonian algorithm must be constructed in the same framework as the Hamiltonian system. In the following, we will describe the basic mathematical framework of the Hamiltonian system and derive the Hamiltonian algorithm from the same framework. This is our approach.

We will use the Euclid geometry as an analogy to describe the symplectic geometry. The structure of an Euclid space $\mathbf { R } ^ { n }$ lies in the bilinear, symmetric, non-degenerate inner product,

$$
( x , y ) = \langle x , I y \rangle , \quad I = I _ { n } .
$$

Since it is non-degenerate, $( x , x )$ is always positive when $x \neq 0$ . Therefore we can define the length of the vector $x$ as $\lvert | x \rvert | = \hat { \sqrt { ( x , x ) } } > 0$ . All the linear operators that preserve the inner product, i.e., satisfy $A ^ { \mathrm { T } } I A = I$ , form a group $O ( n )$ , called the orthogonal group, which is a typical Lie group. The corresponding Lie algebra $o ( n )$ consists of all the transformation that satisfies $A ^ { \mathrm { T } } + A = A I + I A = 0$ , which is infinitesimal orthogonal transformation.

The symplectic geometry is the geometry on the phase space. The symplectic space, i.e, the symplectic structure in phase space, lies in a bilinear, anti-symmetric, and non-degenerate inner product,

$$
[ x , y ] = \langle x , J y \rangle , \quad J = J _ { 2 n } = { \left[ \begin{array} { l l } { O } & { I _ { n } } \\ { - I _ { n } } & { O } \end{array} \right] } ,
$$

which is called the symplectic inner product. When $n = 1$ ,

$$
[ x , y ] = { \left| \begin{array} { l l } { x _ { 1 } } & { y _ { 1 } } \\ { x _ { 2 } } & { y _ { 2 } } \end{array} \right| } ,
$$

which is the area of the parallel quadrilateral with vectors $x$ and $y$ as edges. Generally speaking, the symplectic inner product is an area metric. Due to the anti-symmetry of the inner product, $[ x , x ] = 0$ always holds for any vector $x$ . Thus it is impossible to derive the concept of length of a vector from the symplectic inner product. This is the fundamental difference between the symplectic geometry and Euclid geometry. All transformations that preserve the symplectic inner product form a group, called a symplectic group, $S p ( 2 n )$ , which is also a typical Lie group. Its corresponding Lie algebra consists of all infinitesimal symplectic transformations $B$ , which satisfy $B ^ { \mathrm { T } } J + J B = 0$ . We denote it as $s p ( 2 n )$ . Since the non-degenerate anti-symmetric matrix exists only for even dimensions, the symplectic space must be of even dimensions. The phase space exactly satisfies this condition.

Overall the Euclid geometry is a geometry for studying the length, while the symplectic geometry is for studying the area.

The one-to-one nonlinear transformation in the symplectic geometry is called symplectic transformation, or canonical transformation. The transformation whose Jacobian is always a symplectic matrix plays a major role in the symplectic geometry. For the Hamiltonian system, if we represent a pair of $n$ -dim vectors with a $2 n$ -dim vector ${ z } = ( p , q )$ , the Hamiltonian equation becomes

$$
{ \frac { \mathrm { d } z } { \mathrm { d } t } } = J ^ { - 1 } { \frac { \partial H } { \partial z } } .
$$

Under the symplectic transformation, the canonical form of the Hamiltonian equation is invariant. The basic principle of the Hamiltonian mechanics is for any Hamiltonian system. There exists a group of symplectic transformation (i.e., the phase flow) $G _ { H } ^ { t _ { 1 } , t _ { 0 } }$ that depends on and time $t _ { 0 } , t _ { 1 }$ , so that

$$
\boldsymbol { z } ( t _ { 1 } ) = \boldsymbol { G } _ { H } ^ { t _ { 1 } , t _ { 0 } } \boldsymbol { z } ( t _ { 0 } ) ,
$$

which means that $G _ { H } ^ { t _ { 1 } , t _ { 0 } }$ transforms the state at $t = t _ { 0 }$ to the state at $t = t _ { 1 }$ . Therefore, formation. This is a general mathematical principle for classical mechanics. When $H$ is independent of $t$ , $G _ { H } ^ { t _ { 1 } , - t _ { 2 } } = G _ { H } ^ { t _ { 1 } , - t _ { 0 } }$ , i.e., the phase flow depends only on the difference in parameters $t _ { 1 } - t _ { 0 }$ H . We can let $G _ { H } ^ { t } = G _ { H } ^ { t , 0 }$ .

One of the most important issues for the Hamiltonian system is stability. The feature of this type of problems in geometry perspective is that its solution preserves the metrics. Thus the eigenvalue is always a purely imaginary number. Therefore, we cannot use the asymptotic stability theory of Poincare and Liapunov. The KAM theorem ´ must be used. This is a theory about the total stability and is the most important breakthrough for Newton mechanics. The application of the symplectic geometry to the numerical analysis was first proposed by K. Feng [Fen85] in 1984 at the international conference on differential geometry and equations held in Beijing. It is based on a basic principle of the analytical mechanics: the solution of the system is a volume-preserved transformation (i.e., symplectic transformation) with one-parameter2 on symplectic integration. Since then, new computational methods for the Hamiltonian system have been developed and we have studied the numerical method of the Hamiltonian system from this perspective. The new methods make the discretized equations preserve the symplectic structure of the original system, i.e., to restore the original principle of the discretized Hamiltonian mechanics. Its discretized phase flow can be regarded as a series of discrete symplectic transformations, which preserve a series of phase area and phase volume. In 1988, K. Feng described his research work on the symplectic algorithm during his visit to Western Europe and gained the recognition from many prominent mathematicians. His presentation on “Symplectic Geometry and Computational Hamiltonian Mechanics” has obtained consistent high praise at the workshop to celebrate the 60th birthday of famous French mathematician Lions. Lions thought that K. Feng founded the symplectic algorithm for Hamiltonian system after he developed the finite element methods independent of the efforts in the West. The prominent German numerical mathematician Stoer said, “This is a new method that has been overlooked for a long time but should not be overlooked.”

We know that we can not study the Hamiltonian mechanics without the symplectic geometry. In the meantime, the computational method of the Hamiltonian mechanics doesn’t work without the symplectic difference scheme. The classical R–K method is not suitable to solve this type of problems, because it cannot preserve the long-term stability. For example, the fourth-order R–K method obtains a completely distorted result after 200,000 steps with a step size 0.1, because it is not a symplectic algorithm, but a dissipative algorithm.

We will describe in more detail the theory of symplectic geometry and symplectic algebra in Chapters 1, 2 and 3.

# 5. The Symplectic Schemes

Every scheme, whether it is explicit or implicit, can be treated as a mapping from this time to the next time. If this mapping is symplectic, we call it a symplectic geometric scheme, or in short, symplectic scheme.

We first search the classical difference schemes. The well-known Euler midpoint scheme is a symplectic scheme

$$
z ^ { n + 1 } = z ^ { n } + J ^ { - 1 } H _ { z } \Big ( \frac { z ^ { n + 1 } + z ^ { n } } { 2 } \Big ) .
$$

The symplectic scheme is usually implicit. Only for a split Hamiltonian system, we can obtain an explicit scheme in practice by alternating the explicit and implicit stages. Its accuracy is only of first order. Symmetrizing this first-order scheme yields a second-order scheme (or so-called reversible scheme). There exist multi-stage $\mathbf { R - K }$ symplectic schemes among the series of $\mathbf { R - K }$ schemes. It is proved that the $2 s$ -order Gauss multi-stage $\mathbf { R - K }$ scheme is symplectic. We will give more details on these topics in Chapters 4 , 7 and 8. The theoretical analysis and a priori error analysis will be described in Chapter 6 and 9.

In addition, the first author and his group constructed various symplectic schemes with arbitrary order of accuracy using the generating function theory from the analytical mechanics perspective. In the meantime, he extended the generating function theory and Hamilton–Jacobi equations by constructing all types of generating function and the corresponding Hamilton–Jacobi equations. The generating function theory and the construction of the symplectic schemes will be introduced in Chapter 5.

# 6. The Volume-Preserving Scheme for Source-free System

Among the various dynamical systems, one of them is called source-free dynamical system, where the divergence of the vector field is zero:

$$
{ \frac { \mathrm { d } x } { \mathrm { d } t } } = f ( x ) , \quad \mathrm { d i v } f ( x ) = 0 .
$$

The phase flow to this system is volume-preserved, i.e., $\operatorname* { d e t } \Bigl ( \frac { \partial x _ { n + 1 } } { \partial x _ { n } } \Bigr ) = 1 .$ . Therefore, the numerical solution should also be volume-preserved.

We know that Hamiltonian system is of even dimensions. However, the source-free system can be of either even or odd dimensions. For the system of odd dimensions, the Euler midpoint scheme may not be volume-preserved. ABC (Arnold–Beltrami– Childress) flow is one of the examples. Its vector field has the following form:

$$
\begin{array} { r } { \dot { x } = A \sin x + C \cos y , } \\ { \dot { y } = B \sin x + A \cos z , } \\ { \dot { z } = C \sin y + B \cos x , } \end{array}
$$

which is a source-free system and the phase flow is volume-preserved. This is a split system and constructing the volume-preserving scheme is easy. Numerical experiments show that the volume-preserving scheme can calculate the topological structure accurately, whereas the traditional schemes can not[FS95,QZ93] . We will give more details in Chapter 10.

# 7. The Contact Schemes for Contact System

There exists a special type of dynamical systems with odd dimensions. They have similar symplectic structure as the systems of even dimensions. We call them contact systems. The reader can find more details in Chapter 11.

Consider the contact system in $\mathbf { R } ^ { 2 n + 1 }$ space

$$
\begin{array} { r l } & { ( 2 n + 1 ) - \dim \mathrm { \ v e c t o r : } \left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] , \mathrm { \ w h e r e } x = \left[ \begin{array} { l } { x _ { 1 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right] , y = \left[ \begin{array} { l } { y _ { 1 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] , z = ( z ) ; } \\ & { 2 n + 1 ) - \dim \mathrm { \ v e c t : } \left[ \begin{array} { l } { a ( x , y , z ) } \\ { b ( x , y , z ) } \\ { c ( x , y , z ) } \end{array} \right] , \mathrm { \ w h e r e } a = \left[ \begin{array} { l } { a _ { 1 } } \\ { \vdots } \\ { a _ { n } } \end{array} \right] , b = \left[ \begin{array} { l } { b _ { 1 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right] , c = ( c ) . } \end{array}
$$

A contact system can be generated from a contact Hamiltonian function $K ( x , y , z )$

$$
\begin{array} { r l } & { \frac { \mathrm { d } x } { \mathrm { d } t } = - K _ { y } + K _ { z } x = a , } \\ & { \frac { \mathrm { d } y } { \mathrm { d } t } = K _ { x } = b , } \\ & { \frac { \mathrm { d } z } { \mathrm { d } t } = K _ { e } = c , } \\ & { K _ { e } ( x , y , z ) = K ( x , y , z ) - ( x , K _ { y } ( x , y , z ) ) . } \end{array}
$$

The contact structure in $\mathbf { R } ^ { 2 n + 1 }$ space is defined as

$$
\alpha = x \mathbf { d } y + \mathbf { d } z = [ 0 , x , 1 ] \left[ \begin{array} { l } { \mathbf { d } x } \\ { \mathbf { d } y } \\ { \mathbf { d } z } \end{array} \right] .
$$

A transformation $f$ is called the contact transformation if it could preserve the contact structure with a pre-factor $\mu _ { f }$ . A scheme which can preserve the contact structure is called contact scheme[FW94,Shu93] .

The contact schemes have potential applications in the propagation of the wave front[MF81,QC00] , the applications in thermal dynamics[MNSS91,EMvdS07] , and the characteristic method for the first-order differential equations[Arn88] .

The symplectic algorithm, the volume-preserving algorithm, the contact algorithm, and the Lie–Poisson algorithm are all schemes that preserve the geometry structure of the phase space. We call these methods “geometric integration for dynamic system” $\mathbf { \cdot } [ \mathbf { F W 9 4 } , \mathbf { L Q 9 5 a } ]$ . The geometric integration was first introduced by the first author[FW94] and has been widely accepted and used by the international scientists. The 1996 workshop on the advance of the numerical method, held in England, mentioned the importance of the structure-preserving schemes for the dynamics system. In that workshop, a series of high-order structure preserving schemes has been proposed via the multiplicative extrapolation method[QZ92,QZ94] . We have extended the explicit schemes of Yoshida[Yos90] to all self-adjoint schemes. By using the product of the schemes and their adjoint, we have constructed very high order self-adjoint schemes. The details are described in Chapter 8. Concerning the Lie–Poisson algorithm we will describe more details in Chapter 12.

# 8. Applications of the Symplectic Algorithms for Dynamics System

# (1) Applications of symplectic algorithms to large time scale system

Nearly all systems of celestial mechanics and dynamic astrophysics are Hamiltonian or approximately Hamiltonian with few dissipations. Such systems can be described by canonical forms of Hamiltonian systems, which has now become one of the most important research areas of dynamical system. However, due to the complicated nonlinearity of those canonical Hamiltonian systems, few analytic solutions are available. Although sometimes approximate analytic solutions in form of power series can be obtained by the perturbation method, the long time dynamics, the quantity property, and the intrinsic nonlinearity are overlooked by such solutions. Thus, the numerical methods are required to study those problems to get more accurate and quantitative numerical solutions, which not only provide the information and images on the whole phase space of the given mechanical system for further qualitative analysis, but also lead to some important results for the system. There are two ways to analyze Hamiltonian system qualitatively. One way is to get the numerical solution of the canonical Hamiltonian system directly by the numerical methods, and the other is simpler discretization process to the equation of motion, which becomes a simple mapping question which making computing easier. The later method reduces the computational effort so that it can be performed by normal computers to study the large time scale evolution of dynamical systems.

Traditional numerical methods for dynamics system can be categorized into singlestep methods, e.g. the R–K method, and multi-step methods, e.g. the widely used Adams method for the first order differential equations, and Cowell methods for the second order differential equations. However, all the methods have the artificial numerical dissipations so that the corresponding total energy of the Hamiltonian system will change linearly. This will distort basic property of Hamiltonian system and lead to wrong results for a long time computation. By quantitative analysis, we know that the dissipation of the total energy will accumulate errors of the numerical trajectories of the celestial bodies. The errors will increase at least squarely with respect to the integration time step.

In the 1980s, the first author and his group established the theory of the symplectic algorithms for Hamiltonian system. The significance of this theory is not only to present a new kind of algorithms, but also to elucidate the reason for the false dissipation of the traditional methods, i.e.,that the main truncation error terms of those non-symplectic methods are dissipative terms, whereas the main truncation error terms of symplectic algorithms are not dissipative terms. Thus the numerical energy of the system will not decrease linearly, but change periodically. Due to the conservation of the symplectic structure of the system, which is the basic property, the symplectic algorithms have the long time capacity to simulate the evolution of the celestial bodies. As the energy is a very important parameter of such a system, the numerical results of symplectic algorithms, which can preserve the energy approximatively, are more reasonable. Furthermore, because the errors of the energy are controlled, the errors of numerical trajectories of celestial bodies are no longer along the track by $( t - t _ { 0 } ) ^ { 2 }$ laws of the fast-growing, and with only a $t - t _ { 0 }$ linear growth, this to the long arc computation is extremely advantageous.

For the advantages of the symplectic algorithms, nowadays they have been widely used in the study of dynamical astronomy, especially in the qualitative analysis of the evolution of solar system, e.g. to analyze the stable motion area, space distributions and trajectory resonance of little planets, long time evolution of large planets and extra-planets, and other hot topics in the dynamical astronomy.

# (2) Applications of symplectic algorithms to qualitative analysis

We first use two simple examples to illustrate the special affects of symplectic schemes on the qualitative analysis in dynamics astronomy[LZL93,JLL02,LL95,LL94,Lia97,LLZW94] .

Example I. The Keplerian motions. It is the elliptical motions of two-body problem. The corresponding Hamiltonian function is:

$$
H ( p , q ) = T ( p ) + V ( q ) ,
$$

where $p$ and $q$ are the generalized coordinates and generalize momentum, $T$ and $V$ are the kinetic and potential energies. The analytic solution is a fixed ellipse. When we simulate this problem by the R–K methods and symplectic algorithms, the former ones shrink the ellipse gradually, whereas the later ones preserve the shape and size of the ellipse (see the numerical trajectories after 150 and 1000 steps respectively in Fig. 0.7(a), $e { = } 0 . 7$ and Fig. 0.7(b), $e { = } 0 . 9$ where $e$ is the eccentricity of the ellipse). This means the non-symplectic $\mathbf { R - K }$ methods have the false energy dissipation and the symplectic algorithms preserve the main character of the Kepler problem because of the conservation of the symplectic structure.

Example II. The axial symmetry galaxy’s stellar motion question. Its simplified dynamic model corresponding to the Hamiltonian function is:

$$
H ( p , q ) = { \frac { 1 } { 2 } } ( p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } ) + { \frac { 1 } { 2 } } ( q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } ) + ( 2 q _ { 1 } ^ { 2 } q _ { 2 } - { \frac { 2 } { 3 } } p _ { 2 } ^ { 3 } ) .
$$

To obtain the basic character of the dynamics of this system, we compute it with order 7 and order 8 Runge–Kutta–Fehlberg methods (denoted as RKF(7) and RKF(8) resp.), as well as the order 6 explicit symplectic algorithm (SY6). The numerical results are listed in Fig. 0.8 to Fig. 0.10. In these figures (Fig. 0.8 to Fig. 0.9), we see that the symplectic algorithm preserves the energy $H$ very well in both of the two cases (ordered $\mathrm { L C N } { = } \ 0$ and disorder region $\mathrm { L C N } > 0$ ), while the RKF methods increase the energy with the evolution of time $\Delta H$ . In Fig. 0.10 (a) and Fig. 0.10 (b), the symplectic algorithms present numerically the basic characters of the system: the fixed curve in case of $\mathrm { L C N } { = } 0$ and the chaos property in case of $\mathrm { L C N } > 0$ .

![](images/28a4b803374908f5ea9bc227a97c739d4a771763e5b88cd2899e666e1f0f4b8d.jpg)  
Fig. 0.7. Comparison of calculation of Keplerian motion by $\mathbf { R - K }$ and symplectic methods.

![](images/20ca43b0728d4bfbcfb481f287e84e0c6665e729708ee3270dfbcd62d8df560a.jpg)  
Fig. 0.8. Curves of $\Delta H$ obtained by RKF(8)[left] and SY6 [right] both with $H _ { 0 } = 0 . 5 5 3$ , $\mathrm { L C N } { = } 0$ .

![](images/403f26accc3ad641c171bb90b63cb844f2aca335bb80ca9767bd00cfba835e8d.jpg)  
Fig. 0.9. Curves of $\Delta H$ obtained by RKF(8)[left] and SY6 [right] both with $\begin{array} { r l } { H _ { 0 } } & { { } = } \end{array}$ $0 . 0 1 4 8 , \mathrm { L C N } > 0$

The symplectic algorithms can preserve the symplectic structure of Hamiltonian systems and the basic evolutionary property of such dynamical systems. Therefore, the symplectic algorithms were widely used to study the dynamical astronomy. Currently, it is a hot topic to study the dynamical evolution of the solar system, such as the long-term trajectory evolution of large planet and extra-planet, the space distribution of little planets in main zone (Kirkwood interstice phenomenon), trajectory resonance, the evolution of satellite system of a large planet, the birth and evolution of planet loops and the trajectory evolution of a little planet near Earth. All these problems require numerical simulation for a very long time, e.g. $1 0 ^ { 9 }$ years or more for the solar system. Thus, the time steps for the numerical methods shall be large enough due to limitations of our computers, while the basic property of the system should be preserved. This excludes all the non-symplectic methods, whilst just lower order symplectic algorithms are valid for the task. In recent years, many astronomers in Japan and America, e.g. Kinoshita[KYN91] , Bretit[GDC91] and Wisdom[WHT96,WH91] , have done a large amount of research on the evolution of the solar system. The following contribution of Wisdom has been widely cited. He derived the Hamiltonian function in Jacobin coordinates of the solar system as

![](images/2391b3b3d474b4a20334bf3b821efa513f13ec0a116ea9cf1eb8e486bcb9a853.jpg)  
Fig. 0.10. Poincare section obtained by RKF(8)[left] with ´ $H _ { 0 } ~ = ~ 0 . 5 5 3 , \mathrm { L C N } { = } 0$ and SY6 [right] with $H _ { 0 } = 0 . 0 1 4 8 , \mathrm { L C N } { > } 0$

$$
H ( p , q ) = \sum _ { i = 1 } ^ { n - 1 } H _ { i } ( p , q ) + \varepsilon \Delta H ( p , q ) ,
$$

where $H _ { i } ( p , q )$ is corresponding Hamiltonian function for a two-body system, $\varepsilon \ll 1$ is a small parameter. By splitting the Hamiltonian function, explicit symplectic algorithms with different orders can be constructed. The advantage of those symplectic algorithms is that the truncation errors are as small as order of $\varepsilon$ than those of algorithms constructed by the ordinary splitting for the Hamiltonian function (i.e., $H ( p , q ) = T ( p ) + V ( q ) )$ . Even the lower order symplectic algorithms obtained by this splitting method are very effective in a study of the evolution of the solar system. Since the 1980s , Chinese astronomers have also made some progress in the applications of symplectic algorithms to the research of dynamical astronomy, such as[WH91]

$1 ^ { \circ }$ For the restrictive three-body system constituted by solar, the major planet and the planetoid, some new results have been obtained after studying its corresponding resonance of 1:1 orbit and the triangle libration point. These results can successfully explain the distribution of stability region [ZL94,ZLL92] of Trojan planetoid, as well the actual size of the stable region of distributed triangle libration points corresponding to several relate major planet.

$2 ^ { \circ }$ Adopting the splitting method of Wisdom for the Hamiltonian function to study the long-term trajectories evolution of some little planets.

$$
H ( p , q ) = H _ { 0 } ( p , q ) + \varepsilon H _ { 1 } ( q ) ,
$$

where $H _ { 0 } ( p , q )$ is the Hamiltonian function for an integrable system, $\varepsilon \ll 1$ is a little parameter. The numerical results obtained by using this splitting method are very reasonable because the energy is preserved in a controlled range and no false dissipation occurs.

$3 ^ { \circ }$ Application of symplectic algorithms to galaxy system. The bar phenomenon and the evolution of stars in NGC4736 Galaxy were simulated successfully by the symplectic algorithms.

$4 ^ { \circ }$ Some useful results on how to describe the evolutionary features of celestial dynamical system were obtained by further study on the symplectic integrators and the existence of their formal integrations, as well as the changes of all kinds of conservation laws.

Besides the research on Hamilton systems in dynamics astronomy mentioned above, the small diffusion situation were also discussed and applied. In view of the fact that the diffusion factor is relatively weak, a mixed symplectic algorithm constituted by the explicit scheme and the centered Euler scheme is applied for the conservative part (the main part corresponding to mechanic system) and the dissipative part, which is remarkably effective, because it could maintain the features of Hamilton system in the main part of this system.

# (3) Applications of symplectic algorithms to quantitative computations

Because the structure could be preserved by the symplectic algorithms, the errors of their numerical energy don’t accumulate linearly. When the celestial systems are integrated by symplectic algorithms, errors of trajectories will increase linearly as $t - t _ { 0 }$ , whereas errors of the non-symplectic methods increase rapidly as $( t - t _ { 0 } ) ^ { 2 }$ . We show some examples next.

Taking the trajectory of Lageos satellite as background, we consider two mechanics system of the Earth perturbation problems. The first one just takes into account the nonspherical perturbation of the Earth and the second one takes into account the nonspherical perturbation of the Earth and the perturbation of atmospheric resistance. The former problem corresponds to a Hamiltonian system, while the later one corresponds to a quasi-Hamiltonian system because of very small dissipation. We use the RKF7(8) methods and revised order 6 symplectic algorithm (denoted as SY6) to compute the two problems, respectively. The numerical results of the errors $\Delta ( M + \omega )$ of main 1000 cycles trajectory are listed in Table 0.1 and Table 0.2. From the two tables, we can clearly see that the errors of the non-symplectic methods, though very small at the beginning, increase rapidly as $( t - t _ { 0 } ) ^ { 2 }$ ; whereas the errors of symplectic algorithm increase linearly as $t - t _ { 0 }$ . The results of symplectic algorithms are much better. This indicates that though the accuracy order of symplectic algorithms is the same as for other methods, they have more application value in the quantitative computations. We also improve the RKF7(8) for energy conserving methods by compensating the energy at every time step. We denote such method as the RKH method whose numerical results are also listed in the two tables. From the results, we can see that we have made much improvement of the schemes. The results of the energy error by the RKH are almost same with those by the symplectic algorithm. Thus the RKH methods not only have high order accuracy, but also can preserve the energy approximately as the symplectic algorithms.

Table 0.1. Errors of trajectories with nonspherical perturbation of the Earth $\Delta ( M + \omega )$   

<table><tr><td>method</td><td>N of steps / circle</td><td>100 circles</td><td>1000 circles</td><td>10000 circles</td></tr><tr><td>FKF7(8)</td><td>100</td><td>1.5E-10</td><td>1.4E-08</td><td>1.3E-06</td></tr><tr><td>SY6</td><td>50</td><td>0.5E-09</td><td>0.6E-08</td><td>1.0E-07</td></tr><tr><td>RKH</td><td>100</td><td>0.9E-11</td><td>0.9E-10</td><td>0.9E-09</td></tr></table>

Table 0.2. Errors of trajectories with perturbation of atmospheric resistance $\Delta ( M + \omega )$   

<table><tr><td>method</td><td>N of steps / circle</td><td>100 circles</td><td>1000 circles</td><td>10000 circles</td></tr><tr><td>FKF7(8)</td><td>100</td><td>1.4E- 410</td><td>1.3E-08</td><td>1.3E-06</td></tr><tr><td>SY6</td><td>50</td><td>0.6E-09</td><td>0.7E-08</td><td>1.0E-07</td></tr><tr><td>RKH</td><td>100</td><td>2.1E-11</td><td>3.5E-10</td><td>6.2E-09</td></tr></table>

# (4) Applications of symplectic algorithms to quantum systems

The governing equation of the time evolution of quantum system is the Schrodinger ¨ equation

$$
\mathrm { i } \frac { \partial \psi } { \partial t } = \hat { H } \psi , \quad \hat { H } = \hat { H } _ { 0 } ( r ) + \hat { V } ( t , r ) ,
$$

where the operator $\hat { H }$ is Hermitian.

According to the basic theory of quantum mechanics, the initial state of a quantum system uniquely determines all the states after initial moment of time. That is to say, if the state function $\psi ( t _ { 1 } , r )$ is given at time $t _ { 1 }$ , then the solution (so-called wave function) of Equation (0.1) is determined as

$$
\psi ( t , r ) = a ( t , r ) + i b ( t , r ) ,
$$

where functions $a$ and $b$ are real.

Such a solution can be generated by a group of time evolutionary operators $\{ U _ { \hat { H } } ^ { t _ { 1 } , t _ { 2 } } \}$ , i.e.,

$$
\psi ( t _ { 2 } , r ) = U _ { \hat { H } } ^ { t _ { 1 } , t _ { 2 } } \psi ( t _ { 1 } , r ) .
$$

Every operator is unitary and depends on $t _ { 1 } , t _ { 2 }$ and $\hat { H }$ . They are independent of the state $\psi ( t _ { 1 } , \boldsymbol { r } )$ at time $t _ { 1 }$ . Therefore, the time evolutions of the quantum system are evolutions of unit transformation in this sense. Every operator can induce an operator, which acts on the real function vector. The two components of the real functions vector are the real part and the image part of the wave function, i.e.,

$$
\left[ \begin{array} { l } { b ( t _ { 2 } , r ) } \\ { a ( t _ { 2 } , r ) } \end{array} \right] = S _ { \hat { H } } ^ { t _ { 1 } , t _ { 2 } } \left[ \begin{array} { l } { b ( t _ { 1 } , r ) } \\ { a ( t _ { 1 } , r ) } \end{array} \right] .
$$

The operator $S _ { \hat { H } } ^ { t _ { 1 } , t _ { 2 } }$ preserves the inner product and symplectic wedge product for any two real function vectors. It is simply called norm-preserving symplectic evolution. The quantum system is a Hamiltonian system (with infinite dimensions) and the time evolution of the Schrodinger equation can be rewritten as a canonical Hamilto- ¨ nian system for the two real functions of the wave function as the generalized momentum and generalized coordinates. The norm of wave function is the conservation law of the canonical system. Thus it is reasonable to integrate such a system by the norm-preserving symplectic numerical methods. To apply such a method to the infinite dimensional system, we should first space discretize the system into a finite dimensional canonical Hamiltonian system, which also preserves the norm of wave function. Suppose the characteristic functions of the operator $\hat { H } _ { 0 } ( r )$ for the evolutionary Schrodinger equation with some given boundary conditions contain the discrete ¨ states and continuous states.

When the Hamiltonian $\hat { H }$ is independent on time explicitly, the energy of the quantum system $\langle \psi | , \hat { H } | \psi \rangle = Z ^ { \mathrm { T } } H Z$ is a conservation law both for the canonical system and norm-preserving symplectic algorithm. Such a norm-preserving symplectic algorithm with the fourth order accuracy can be constructed by the order 4 diagonal Pade´ approximations to the exponential function $e ^ { \lambda }$ .

In the following, we take an example to introduce the method to discretize the time involved Schrodinger equation to a canonical system ¨ [LQHD07,QZ90a] .

Consider the time evolution of an atom moving in one dimensional space by the action of some strong field $V ( t , x )$ is

$$
\begin{array} { c } { { \displaystyle { \mathrm { i } \frac { \partial \psi } { \partial t } = \hat { H } \psi , \quad \hat { H } = \hat { H } _ { 0 } ( { \boldsymbol { r } } ) + \hat { V } ( t , { \boldsymbol { r } } ) , } } } \\ { { \hat { H } _ { 0 } = - \displaystyle { \frac { 1 } { 2 } \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } + V _ { 0 } ( x ) } , } } \\ { { V _ { 0 } ( x ) = \left\{ \begin{array} { l l } { { 0 , \quad 0 < x < 1 , } } \\ { { \infty , \quad x \leq 0 \quad \mathrm { o r } \quad x \geq 1 . } } \end{array} \right. } } \end{array}
$$

In contrast to the characteristic function expanding method, we don’t make any truncation for the wave function when discretizing the Schrodinger equation. Therefore, ¨ the resulting canonical system contains all the characteristic states of $\hat { H } _ { 0 }$ .

The numerical conservation laws of explicit symplectic algorithms will converge to the corresponding conservation laws of the system as the time step tends to zero. Thus, although numerical energy and norm of the wave function presented by explicit symplectic algorithms will not be preserved exactly, they will converge to the true energy and norm of the wave function of the system as the time step reduces.

The time dependent Schrodinger equation (TDSE) in one dimensional space by ¨ the action of some strong field $V ( t , x )$ is

$$
\begin{array} { r l } & { \mathrm { i } \frac { \partial \hat { \psi } } { \partial t } = \hat { H } \psi , \quad \hat { H } = \hat { H } _ { 0 } ( x ) + \varepsilon \hat { V } ( t , x ) , } \\ & { \qquad \hat { H } _ { 0 } = - \frac { 1 } { 2 } \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } + V _ { 0 } ( x ) , } \\ & { V _ { 0 } ( x ) = \left\{ \begin{array} { l l l } { 0 , } & { 0 < x < 1 , } \\ { \infty , } & { x \leq 0 \quad \mathrm { o r } \quad x \geq 1 . } \\ { 0 < x < 0 . 5 , } \\ { 2 x - 2 x , } & { 0 . 5 \leq x \leq 1 , } \\ { 0 , } & { x \leq 0 \quad \mathrm { o r } \quad x \geq 1 . } \end{array} \right. } \end{array}
$$

Using the similar method as before, we expand the wave function as the characteristic functions $\{ X _ { n } ( x ) = { \sqrt { 2 } } \sin n \pi x , n = \bar { 1 , } 2 , \cdot \cdot \cdot \}$ of $\hat { H } _ { 0 }$ to discretize the TDSE. Because the Hamiltonian operator is real, the discrete TDSE is a separable linear canonical Hamiltonian system with the parameters as follows.

$$
\begin{array} { c } { { S = ( S _ { m n } ) , \quad S _ { m n } = \displaystyle { \frac { n ^ { 2 } \pi ^ { 2 } } { 2 } } \delta _ { m n } + \varepsilon v _ { m n } , } } \\ { { { } } } \\ { { v _ { m n } = \left\{ \begin{array} { l l } { { \displaystyle { \frac { 1 } { 2 } } + \frac { 1 - ( - 1 ) ^ { n } } { n ^ { 2 } \pi ^ { 2 } } , } } & { { m = n , } } \\ { { 0 , } } & { { | m - n | = 1 , 3 , 5 , \cdots , } } \\ { { \displaystyle { \frac { - 1 6 m n ( 1 - ( - 1 ) ^ { \frac { m - n } { 2 } } ) } { ( m ^ { 2 } - n ^ { 2 } ) ^ { 2 } \pi ^ { 2 } } } , } } & { { | m - n | = 2 , 4 , 6 , \cdots , n = 2 , 4 , 6 , \cdots , } } \\ { { \displaystyle { \frac { - 8 | 2 m n - ( - 1 ) ^ { \frac { m - n } { 2 } } ( m ^ { 2 } - n ^ { 2 } ) | } { ( m ^ { 2 } - n ^ { 2 } ) ^ { 2 } \pi ^ { 2 } } } , | m - n | = 2 , 4 , 6 , \cdots , n = 1 , 3 , 5 , \cdots . } } \end{array} \right. } } \end{array}
$$

The initial state is taken as

$$
\psi ( 0 , x ) = \frac { 1 + \mathrm { i } } { 2 } \vert X _ { 1 } ( x ) + X _ { 2 } ( x ) \vert , \quad \varepsilon = 5 \pi ^ { 2 } .
$$

The energy of the system is conserved because the Hamiltonian does not depend on the time explicitly. $E ( b , a ) = e ^ { 0 } = 4 2 . 0 1 1 0 1 6 5 .$ . The norm of wave function keeps unitary, i.e., $N ( b , a ) = n ^ { 0 } = 1$ . We take the Euler midpoint rule, order 2 explicit symplectic algorithm and the order $2 \ \mathrm { R - K }$ method to compute the problem with the same time step $h = 1 0 ^ { - 3 }$ . The numerical results are as follows:

$1 ^ { \circ }$ The $\mathbf { R - K }$ method can not preserve the energy and the norm of wave function, as evident by $E _ { \mathrm { R - K } }$ in Fig. 0.11(left) and $N _ { \mathrm { R - K } }$ in Fig. 0.11(right).

$2 ^ { \circ }$ The Euler midpoint rule can preserve the energy and norm, as evident by $E _ { \mathrm { E } }$ in Fig. 0.11(left) and $N _ { \mathrm { E } }$ in Fig. 0.11(right). Note that for $E _ { \mathrm { E } }$ in Fig. 0.11(left), there is a very small increase at some time because of the implicity of the Euler scheme.

![](images/f358e04bb36063904b940ebc3b3a6b59ade90ad48ee7e75cfb04d62797e6a064.jpg)  
Fig. 0.11. Energy [left] and norm [right] comparison among the 3 difference schemes

$3 ^ { \circ }$ The explicit symplectic algorithms can preserve exactly the energy ${ \tilde { E } } ( b ^ { k } , a ^ { k } ; h )$ and norm $\tilde { N } ( b ^ { k } , a ^ { k } ; h )$ , as evident by $E _ { \mathrm { S } } ^ { \prime }$ in Fig. 0.11(left) and $N _ { \mathrm { S } } ^ { \prime }$ in Fig. 0.11(right). If we want to get further insight into these conservation laws within smaller scales, we find that as the time steps get smaller, the numerical energy of symplectic algorithm converges to the true energy of the system $e ^ { 0 } = 4 2 . 0 1 1 0 1 6 5$ and the numerical norm converges to unit $n ^ { 0 } = 1$ . See Table 0.3 showing the numerical energy and norm as well as their errors. The errors are defined as

$$
C _ { E } ( h ) = \operatorname* { m a x } _ { k } | E _ { \mathrm { S } } ^ { k } - e ^ { 0 } | , \quad C _ { N } ( h ) = \operatorname* { m a x } _ { k } | N _ { \mathrm { S } } ^ { k } - n ^ { 0 } | .
$$

Actually, the numerical energy and norm obtained by symplectic algorithm oscillate slightly, as shown by $E _ { \mathrm { { S } } }$ and $N _ { S }$ in Fig. 0.12. However, the amplitude of their oscillations will converge to zero, if the time step tends to zero. As the time step tends to zero, we have

$$
\begin{array} { l l l } { { e ( h ) \longrightarrow e ^ { 0 } , } } & { { \quad C _ { E } ( h ) = \operatorname* { m a x } _ { k } | E _ { S } ^ { k } - e ^ { 0 } | \longrightarrow 0 , } } \\ { { } } & { { } } & { { } } \\ { { n ( h ) \longrightarrow n ^ { 0 } , } } & { { \quad C _ { N } ( h ) = \operatorname* { m a x } _ { k } | N _ { S } ^ { k } - n ^ { 0 } | \longrightarrow 0 . } } \end{array}
$$

Table 0.3. The change of energy and norm of the wave function with the step size   

<table><tr><td rowspan=1 colspan=1>h</td><td rowspan=1 colspan=1>e(h)</td><td rowspan=1 colspan=1>Cs(h)</td><td rowspan=1 colspan=1>n(h)</td><td rowspan=1 colspan=1>CN(h)</td></tr><tr><td rowspan=1 colspan=1>10-3</td><td rowspan=1 colspan=1>42.0169964</td><td rowspan=1 colspan=1>0.0445060</td><td rowspan=1 colspan=1>0.9996509</td><td rowspan=1 colspan=1>0.0003106</td></tr><tr><td rowspan=1 colspan=1>10-4</td><td rowspan=1 colspan=1>42.0110763</td><td rowspan=1 colspan=1>0.0004195</td><td rowspan=1 colspan=1>0.9999965</td><td rowspan=1 colspan=1>0.0000030</td></tr><tr><td rowspan=1 colspan=1>10-5</td><td rowspan=1 colspan=1>42.0110171</td><td rowspan=1 colspan=1>0.0000018</td><td rowspan=1 colspan=1>0.9999990</td><td rowspan=1 colspan=1>0.0000000</td></tr><tr><td rowspan=1 colspan=1>10-6</td><td rowspan=1 colspan=1>42.0110165</td><td rowspan=1 colspan=1>0.0000000</td><td rowspan=1 colspan=1>1.0000000</td><td rowspan=1 colspan=1>0.0000000</td></tr><tr><td rowspan=1 colspan=1>10-7</td><td rowspan=1 colspan=1>42.0110165</td><td rowspan=1 colspan=1>0.0000000</td><td rowspan=1 colspan=1>1.0000000</td><td rowspan=1 colspan=1>0.0000000</td></tr><tr><td rowspan=1 colspan=1>exact value</td><td rowspan=1 colspan=1>42.0110165</td><td rowspan=1 colspan=1>0.0000000</td><td rowspan=1 colspan=1>1.0000000</td><td rowspan=1 colspan=1>0.0000000</td></tr></table>

![](images/016b770ceeb53c5d96f5cc39161455c31b6ef890ba73d4471afbf10f926faee1.jpg)  
Fig. 0.12. Energy $E$ and norm $N$ obtained from explicit symplectic scheme

In all, for a quantum system with real Hamiltonian function independent of time explicitly, the explicit symplectic algorithms can preserve the energy and norm of the wave function to any given accuracy. They overcome the main disadvantages of the traditional numerical methods.

Next, we look at the quantum system with real Hamiltonian function, which is dependent on time explicitly. In this case, the resulting system after semi-discretization is an $m$ -dimensional, separable, linear, Hamiltonian canonical system. The energy of the system is not conserved any more, but the norm of the wave function is still a quadratic conservation law.

The TDSE for an atom in one dimensional space with the action of some strong field $V ( t , x ) = \varepsilon x \sin ( \omega t )$ is

$$
\begin{array} { c } { { { \displaystyle { \bf i } \frac { \partial \psi } { \partial t } = \hat { H } \psi , \quad \hat { H } = \hat { H } _ { 0 } ( x ) + \varepsilon \hat { V } ( t , x ) , } } } \\ { { \hat { H } _ { 0 } = - \displaystyle { \frac { 1 } { 2 } \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } + V _ { 0 } ( x ) } . } } \end{array}
$$

By the similar method as before, we expand the wave function as the characteristic functions $X _ { n } x = { \sqrt { 2 } } \sin n \pi x ( n = 1 , 2 , \cdots )$ of $\hat { H } _ { 0 }$ to discretize the TDSE. Because

![](images/c78a3fa1ab82f21caea91a68147b8066e65ad6da9bf220661fcc6332b35ce121.jpg)  
Fig. 0.13. $\omega = 3 \pi ^ { 2 } / 2 , \varepsilon = \pi ^ { 2 } / 2$ : Graph of norm[left]; graph of probability[right]

the Hamiltonian operator is real, the discrete TDSE is a separable linear canonical Hamiltonian system with the parameters as follows.

$$
\begin{array} { l } { { S ( t ) = ( s ( t ) _ { m n } ) , \quad s ( t ) _ { m n } = \frac { { n ^ { 2 } \pi ^ { 2 } } } { 2 } \delta _ { m , n } + \varepsilon v ( t ) _ { m n } ; } } \\ { { \quad \begin{array} { l } { { \begin{array} { l } { { m = n , } } \\ { { 0 , } } \end{array} } } \end{array} } } \\ { { v ( t ) _ { m n } = \left\{ \begin{array} { l l } { { 8 \pi ( \omega t ) _ { m n } = \frac { n ^ { 2 } \pi ^ { 2 } } { 2 } \delta _ { m , n } = 1 , 3 , 5 , \cdots , } } \\ { { \frac { 8 m n \sin { ( \omega t ) } } { ( m ^ { 2 } - n ^ { 2 } ) ^ { 2 } \pi ^ { 2 } } , } } \end{array} \right. } } \end{array}
$$

The initial state is taken as $\psi ( 0 , x ) = X _ { 1 } ( x ) = \sqrt { 2 } \sin ( \pi x ) $ . The energy of the system is not conserved in this case because the Hamiltonian depends on the time explicitly. The norm of wave function remains unitary, i.e., $N ( b , a ) = n ^ { 0 } = 1$ . We take the Euler midpoint rule scheme, order 2 explicit symplectic algorithm and the order $2 \ \mathrm { R - K }$ method to compute the problem with the same time step $h = 4 \times 1 0 ^ { - 3 }$ . The numerical results are as follows:

$1 ^ { \circ }$ The $\mathbf { R - K }$ method increases the norm of wave function rapidly, see $N _ { \mathrm { R - K } }$ in Fig. 0.13(left). It leads to unreasonable results, see in Fig. 0.13(right).

$2 ^ { \circ }$ The Euler midpoint rule scheme can preserve the norm, see $N _ { \mathrm { E } }$ in Fig.0.13(left). These results are in good agreement with the theoretical results. See Fig. 0.13(right) for the results for weak fields $\varepsilon = \frac { \pi } { 2 }$ When $\omega = \Delta E _ { 1 n }$ , i.e., resonance occurs, the basic state and the first inspired state will intermix and the variation period of the energy is identical to the period of intermixing. See the corresponding results in Fig. 0.14(left) and Fig. 0.14(right). When $\omega \neq \Delta E _ { 1 n }$ there will not be intermixing. See the corresponding numerical results in Fig. 0.15(left) and Fig. 0.15(right), where $O$ is the basic state. When the field is strong, the selection rule is untenable, and no resonance occurs, but the basic state will intermix with the first, second, . . . inspired states. See the results for $\omega = { \frac { 5 \pi ^ { 2 } } { 4 } }$ in Fig. 0.16(left) and Fig. 0.16(right) and $\omega \stackrel { . } { = } \frac { 3 \pi ^ { 2 } } { 2 } = \Delta E _ { 1 2 }$ in Fig. 0.17(left) and Fig. 0.17(right).

![](images/2ebf51d201cd1c29819f87be5aba5823933ca9d327653da8e9107028f9268a8a.jpg)  
Fig. 0.14. $\omega = 3 \pi ^ { 2 } / 2 , \varepsilon = \pi ^ { 2 } / 2$ : Graph of probability[left]; graph of norm[right]

![](images/5690150453e7cd3b97afd853def55e835a39338f9421d1c46606913c0f1cd676.jpg)  
Fig. 0.15. $\omega = 5 \pi ^ { 2 } / 4 , \varepsilon = 3 \pi ^ { 2 } / 2$ : Graph of probability[left]; graph of norm[right]

$3 ^ { \circ }$ The order 2 explicit symplectic algorithms can not preserve the norm exactly. The numerical norms oscillate near the unit. See $N _ { S }$ in Fig. 0.13, where changes of numerical energy and states of intermixing obtained by symplectic algorithms are similar to the results of Euler midpoint rule scheme.

We can conclude that for this system the $\mathbf { R - K }$ method can not preserve the norm of wave function and its results are unreasonable; the Euler scheme can preserve the norm and its results are in agreement with the theoretical results; the second order scheme obtains the numerical norm which oscillates near the unit and its energy and states of intermixing are the same as for the results of Euler scheme. Thus, the Euler scheme (an implicit symplectic scheme) and the second order explicit symplectic algorithm are good choices for studying the quantum system with the Hamiltonian dependent on time explicitly. They overcome the drawbacks of the traditional R–K methods.

# (5) Applications to computation of classical trajectories

Applications of symplectic algorithms to computation of classical trajectories of $A _ { 2 } B$ molecular reacting system [LDJW00] .

To study the classical or semi-classical trajectories of the dynamical system, microscopic chemistry is an effective theory method.

![](images/41edf3657c1dc04d32d876eb8d18207eafec3e9c6c69642a900e79f6534a92a4.jpg)  
Fig. 0.16. $\omega = 5 \pi ^ { 2 } / 4 , \varepsilon = 5 0 \pi ^ { 2 }$ : Graph of probability[left]; graph of norm[right]

![](images/e3121e484258dcb2fe982b488e4b4b2ca6651960c337a461fec52e5b6d59e1dd.jpg)  
Fig. 0.17. $\omega = 3 \pi ^ { 2 } / 2 , \varepsilon = 5 0 \pi ^ { 2 }$ : Graph of probability[left]; graph of norm[right]

The classical trajectory method regards the atom approximatively as a point and the system as a system of some points, and advances the process of action as the classical motions of point system in potential energy plane of the electrons. It was Bunker who first applied the $\mathbf { R - K }$ method to computations of classical trajectory of molecular reacting system. Karplus et al. did a large number of computations by all kinds of numerical methods and screened out the R–K–G (Runge–Kutta–Gear) method to prolong the computation time from $1 0 ^ { - 1 5 } \mathrm { s }$ to $1 0 ^ { - 1 2 } \mathrm { s }$ . The R–K–G method made rapid progress in the theoretical study of reacting dynamics of microscopic chemistry and was widely used for computation of classical trajectory. However, its valid computation time is much less than $1 0 ^ { - 8 } \mathrm { s }$ which is necessary time for study of chemical reactions. Moreover, there were many differences between the numerical quantities and theoretical quantities of some parameters. The classical trajectory method describes the microscopic reaction system approximately as a Hamiltonian system which naturally has symplectic structure. Thus, it is expected that the symplectic algorithms will overcome the shortages of the R–K–G method and improve the numerical results.

Here we take the mass of the proton as the unit mass and $4 . 4 5 \times 1 0 ^ { - 1 4 } \mathrm { s }$ as unit time.

Consider the classical motions of the $A _ { 2 } B$ type molecules like $_ \mathrm { H _ { 2 } O }$ and $\mathrm { S O _ { 2 } }$ moving in the electron potential energy plane of the reaction system and preserving the symmetry of $C _ { 2 v }$ . Set the masses of $A$ and $B$ to be $m _ { A } = 1$ and $m _ { B } = 2$ resp., the center of mass of the molecule be the origin of some coordinate, the $C _ { 2 }$ axes be $z$ axes, and the coordinates of two atoms $A$ and the atom $B$ be $( y _ { 1 } , z _ { 1 } )$ , $( y _ { 2 } , z _ { 2 } )$ and $( y _ { 3 } , z _ { 3 } )$ reps. in the fixed coordinate system. By Banerjee’s coordinates separating method, we can get the generalized coordinates of the $A _ { 2 } B$ molecule as

$$
q _ { 1 } = z _ { 1 } + z _ { 2 } - 2 z _ { 3 } , \quad q _ { 2 } = y _ { 2 } - y _ { 1 } ,
$$

and the generalized mass as $M _ { 1 } = 0 . 2 5$ , $M _ { 2 } = 0 . 5$ , further the generalized momentum as

$$
p _ { 1 } = 0 . 2 5 \frac { \mathrm { d } q _ { 1 } } { \mathrm { d } t } , \quad p _ { 2 } = 0 . 5 \frac { \mathrm { d } q _ { 2 } } { \mathrm { d } t } ,
$$

and the kinetic energy of system as

$$
K ( p ) = 2 p _ { 1 } ^ { 2 } + p _ { 2 } ^ { 2 } .
$$

The potential energy suggested by Banerjee, who introduced the symmetry $C _ { 2 v }$ and notation $D = \sqrt { q _ { 1 } ^ { 2 } + q _ { 2 } ^ { 2 } }$ , was

$$
\begin{array} { r l r } { V ( q ) } & { = } & { 5 \pi ^ { 2 } ( D ^ { 2 } - 5 D + 6 . 5 ) + 4 D ^ { - 1 } } \\ & { } & \\ & { } & { + 0 . 5 \pi ^ { 2 } ( | q _ { 2 } | - 1 . 5 ) ^ { 2 } + | q _ { 2 } | ^ { - 1 } . } \end{array}
$$

The Hamiltonian function for the $A _ { 2 } B$ molecular system is

$$
H ( p , q ) = K ( p ) + V ( q ) ,
$$

and the canonical equations for the classical trajectories are

$$
\begin{array} { c c } { \displaystyle \frac { \mathrm { d } p _ { 1 } } { \mathrm { d } t } = - \frac { \partial V } { \partial t } = - f _ { 1 } ( q ) , } & { \displaystyle \frac { \mathrm { d } q _ { 1 } } { \mathrm { d } t } = \frac { \partial K } { \partial p _ { 1 } } = g _ { 1 } ( p ) , } \\ { \displaystyle \frac { \mathrm { d } p _ { 2 } } { \mathrm { d } t } = - \frac { \partial V } { \partial q _ { 2 } } = - f _ { 2 } ( q ) , } & { \displaystyle \frac { \mathrm { d } q _ { 2 } } { \mathrm { d } t } = \frac { \partial K } { \partial p _ { 2 } } = g _ { 2 } ( p ) . } \end{array}
$$

It is a separated Hamiltonian system, which can be integrated by explicit symplectic algorithms. We can obtain its numerical solutions of some initial values as

$$
t ^ { k } = k h , \quad p _ { 1 } ^ { k } = p _ { 1 } ( t ^ { k } ) , \quad q _ { 1 } ^ { k } = q _ { 1 } ( t ^ { k } ) , \quad p _ { 2 } ^ { k } = p _ { 2 } ( t ^ { k } ) , \quad q _ { 2 } ^ { k } = q _ { 2 } ( t ^ { k } ) ,
$$

and further its classical trajectories of $A _ { 2 } B$ system and the changes of kinetic energy, potential energy and total energy with time by following relations:

$$
y _ { 3 } = 0 , \quad z _ { 3 } = - { \frac { q _ { 1 } } { 4 } } ; \quad y _ { 2 } = - y _ { 1 } = { \frac { q _ { 2 } } { 2 } } , \quad z _ { 2 } = z _ { 1 } = { \frac { q _ { 1 } } { 4 } } .
$$

The initial values are taken as

$$
q _ { 1 } ( 0 ) = 3 , \quad q _ { 2 } ( 0 ) = { \frac { 3 } { 2 } } ; \quad p _ { 1 } = 0 , \quad p _ { 2 } = 0 .
$$

![](images/c8555b4dc843d1bc7de352aac5c938f17766ab969d82ae573a82a6eb996eec4a.jpg)  
Fig. 0.18. The potential energy curve of the electronic potential function in phase space

We compute this system with order 4 explicit symplectic algorithm and R–K method. The time step is taken as $h = 0 . 0 1$ for both. The numerical classical trajectories, kinetic energy, potential energy and total energy are recorded. Fig. 0.18 shows the potential energy curve of the electronic potential function in phase space. If $| q _ { 1 } | \to + \infty$ , then $V ( q ) \to + \infty$ ; if $| q _ { 2 } | \to 0$ or $| q _ { 2 } | \to + \infty$ , then $V ( q ) \to + \infty$ . By the theoretical analysis, we know that the total energy of the system will be conserved all the time, the three atoms will oscillate nearly periodically, and the whole geometry structure of the system may be reversed but kept periodic. The changes of the total energy with time are shown in Fig.0.19, where we can see that the total energy obtained by symplectic algorithms are preserved up to $6 . 2 3 \times 1 0 ^ { - 9 } \mathrm { s }$ , whereas the $\mathbf { R - K }$ method reduces them rapidly with time. The motion trajectories of the system in the plane by the symplectic algorithms and $\mathbf { R - K }$ method are shown in Fig. 0.20 (a), (c), (e) and (b), (d), (f) resp., where we can see that the numerical results of symplectic algorithms are coincident with the theoretical results but the results of $\mathbf { R - K }$ method are not. We also applied the order 1 and 2 symplectic algorithms, the Euler method and the revised Euler method to compute the same problem. The conclusions are almost the same. Because all the traditional methods such as $\mathbf { R - K }$ methods, Adams methods and Euler methods can not preserve the symplectic structure of this microscopic system, they will bring false dissipations inevitably, which will make their numerical results meaningless after long-term computations. On the contrary, symplectic algorithms can preserve the structure and do not bring any false dissipations. Therefore, they are suitable for long-term computations and greatly improve the classical trajectory methods for studying the microscopic dynamical reactions of chemical systems.

![](images/953cb4a7a3ec5a2f452800b23fe856e21b66951cddfb83f563a50dcda93fe83d.jpg)  
Fig. 0.19. The changes of the total energy with the time

# (6) Applications to computation of classical trajectories of diatomic system [Dea94,DLea96]

Consider the classical motion of $A B$ diatomic molecule system in electron potential energy plane. Set the masses of $A$ and $B$ to be $m _ { 1 }$ and $m _ { 2 }$ resp., the center of mass to be the origin of some coordinate with fixed axes $O x$ , the coordinates of two atoms $A$ and $B$ to be $- { x } _ { 1 }$ and $x _ { 2 }$ resp. Then the generalized coordinate is $q = x _ { 2 } + x _ { 1 }$ and the generalize mass is $M = { \frac { m _ { 1 } m _ { 2 } } { m _ { 1 } + m _ { 2 } } }$ . Further, the generalized momentum is $p = M { \frac { \mathrm { d } q } { \mathrm { d } t } } $ m1 + m2and the generalized kinetic energy is $U ( p ) = { \frac { p ^ { 2 } } { 2 M } }$ d tTake the potential function as the Morse potential

$$
V ( q ) = D \{ { \bf e } ^ { - 2 a \left( q - q _ { e } \right) } - 2 { \bf e } ^ { - a \left( q - q _ { e } \right) } \} ,
$$

where the parameters $D , a , q _ { e }$ were derived by E. Ley and Koo recently. Thus, the total energy for such system is $H ( p , q ) = U ( p ) + V ( q )$ , and the canonical Hamiltonian system for the classical trajectory is

$$
\begin{array} { l } { \displaystyle \frac { \mathrm { d } p } { \mathrm { d } t } = - \frac { \mathrm { d } V ( q ) } { \mathrm { d } t } = - f ( q ) , } \\ { \displaystyle \frac { \mathrm { d } q } { \mathrm { d } t } = \frac { \mathrm { d } U ( p ) } { \mathrm { d } t } = g ( p ) . } \end{array}
$$

It is a separable system. By explicit symplectic algorithms, we can get its numerical solutions as

$$
t ^ { k } = k h , \quad p ^ { k } = p ( t ^ { k } ) , \quad q ^ { k } = q ( t ^ { k } ) ,
$$

and advance its classical trajectories of $A B$ two-atom system as

$$
x _ { 1 } = \frac { m _ { 2 } q } { m _ { 1 } + m _ { 2 } } , ~ x _ { 2 } = \frac { m _ { 1 } q } { m _ { 1 } + m _ { 2 } } ,
$$

![](images/d15b9aa52d1106e7d9e4c5f69ee4b9834ccf56025769becca97ecac6dae48b88.jpg)  
Fig. 0.20. The motion trajectories of the system in the plane,(a) and (b) period range from $4 . { \overset { \vartriangle } { 4 } } 5 \times 1 0 ^ { - 1 0 } \mathrm { s }$ to $( 4 . 4 5 \times 1 0 ^ { - 1 0 } + 4 . 4 5 \times 1 0 ^ { - 1 3 } ) \mathrm { s }$ . (c) and (d) period range from $6 . 2 3 \times 1 0 ^ { - 9 } \mathrm { s }$ to $( 6 . 2 3 \times 1 0 ^ { - 9 } + 4 . 4 5 \times 1 0 ^ { - 1 3 } ) \mathrm { s }$ . (e) and (f) period range from $6 . 2 \mathrm { { 3 } \times 1 0 ^ { - 9 } \mathrm { { s } } }$ to $( 6 . 2 3 \times$ $1 0 ^ { \overset { . } { - } 9 } + 4 . 4 5 \times 1 0 ^ { - 1 3 } )$ s. (a), (c), (e) is the symplectic algorithm path, (b), (d), (f) is the $\mathbf { R - K }$ method path

as well as the changes of kinetic energy, potential energy and total energy with the variation of time.

We compute some states of two homonuclear molecules $\mathrm { L i _ { 2 } }$ and $\Nu _ { 2 }$ and two heteronuclear molecules CO and CN by using the order 1, 2 and 4 explicit symplectic algorithms and compare the numerical results of total energy and classical trajectories with the Euler method and order 2 and 4 order $\mathbf { R - K }$ methods. In Fig. 0.21, Fig. 0.22 and Fig. 0.23, we show the numerical results of the classical trajectories, total energy and the trajectories in $p - q$ phase space obtained by order 4 explicit symplectic algorithm and order $4 ~ \mathrm { R - K }$ method respectively. The parameters in those computations are taken as the time step $h \ : = \ : 0 . 0 0 5$ , the initial values $q ( 0 ) = q _ { e }$ , $p ( 0 ) \stackrel { \textstyle - } { = } \sqrt { 2 M D } - 0 . 0 0 0 1$ , and $D = 8 5 4 1 \mathrm { { c m } ^ { - 1 } }$ , $q _ { e } = 2 . 6 7 3 2 8 \mathring \mathrm { A }$ , $a =$ $0 . 8 6 7 \mathring \mathrm { A } ^ { - 1 }$ , $\mathring { \mathbf { A } } = 0 . 1 \mathrm { n m }$ . The results show that the symplectic algorithms can preserve the energy after $1 0 ^ { 6 }$ time steps and the facts that the two Li atoms oscillate periodically and their trajectories in phase remain invariant are simulated by the symplectic algorithm. The results are opposite for the $\mathbf { R - K }$ method. The numerical total energy, and the oscillation period and amplitude of the two atoms were reduced, after 3000 time steps. Furthermore, the trajectories in the phase space became flat to $q$ axis after 50000 time steps and lost entirely their shape as manifested in the theory analysis and experiments (Fig. 0.21, Fig. 0.22, Fig. 0.23). The results of the other molecules $\Nu _ { 2 }$ , CO and CN are similar. Thus, we can draw the conclusion that the symplectic algorithms can preserve the symplectic structure and the basic properties of the microscopic system. Therefore they are capable of long time computations for such systems.

![](images/7cb1359a84bddcd37862ab9d65c8a59c02d88636d3366bfd0fa948969eb09f6b.jpg)  
Fig. 0.21. Classical orbit of two homonuclear molecules $\mathrm { L i _ { 2 } }$

![](images/3c38d1ed89e6776182b4dd1c3a1f96769f56205d4e7cbd972541a45e015a590d.jpg)  
Fig. 0.22. Comparison of energy of two homonuclear molecules $\mathrm { L i _ { 2 } }$

![](images/7ed0e34fa54dcaa7664d6902dfb9e710b22cbdfcf1796ac98c761a4cae19dba9.jpg)  
Fig. 0.23. The trajectories in $p - q$ phase space

# (7) Applications to atmospheric and geophysical science

Recently, the symplectic algorithms have been applied to study the observation operator of the global positioning system (GPS) by Institute of Atmospheric Physics of the Chinese Academy of Science[WZJ95,WJX01] . Numerical weather forecasting needs very large amount of atmospheric information from GPS. One of the key problems in this field is how to reduce largely the computational costs and to compute it accurately for a long time. The symplectic algorithms provide rapid and accurate numerical algorithms for them to deal with the information of GPS efficiently. The computational costs of the symplectic algorithms are one four hundredth of the costs of traditional algorithms. For the complicated nonlinear system of atmosphere and ocean, symplectic algorithms can preserve its total energy, total mass, total potential so well that the relative errors of potential height is below 0.0006 (see Fig. 0.24).

Another application of symplectic algorithms to geophysics is carried out by Institute of Geophysics to prospect for the oil and natural gas[GLCY00,LLL01a,LLL01b,LLL99] , which has obtained several great achievements. For example, the spread waves of earthquake under the framework of Hamiltonian system and the corresponding symplectic algorithms have been investigated. Moreover, “the information of oil reserves and geophysics and its process system ” has been produced, and the task of prospecting for $1 0 ^ { 1 0 } \mathrm { m ^ { 3 } }$ of natural gas, which has obtained. Fig. 0.25 shows the numerical results of prestack depth migration in the area of Daqing Xujiaweizi by applying symplectic algorithms to Marmousi model. Recently, Liuhong et.al. proposed a new method[LYC06] to calculate the depth extrapolation operator via exponential of pseudo-differential operator in lateral varied medium. The method offers the phase of depth extrapolation operator by introducing lateral differential to velocity, which in fact is an application of Lie group method.

![](images/4c8f44d3bc1a3f9d07ad5d6d84dbae1cba9601f467b31d5f44550e7364629aff.jpg)  
Fig. 0.24. The relative errors of potential height is below 0.0006 after 66.5 days

![](images/95e4ff8b0a6c04f5d6de70ea7bd481b1eb296139c6537716178c72393190a61c.jpg)  
Fig. 0.25. Numerical results of prestack depth migration in the area of Daqing Xujiaweizi obtained by applying symplectic algorithms to Marmousi model

# Bibliography

[AM78] R. Abraham and J. E. Marsden: Foundations of Mechanics. Addison-Wesley, Reading, MA, Second edition, (1978).   
[Arn63] V. I. Arnold: Small denominators and problems of stability of motion in classical and celestial mechanics. Russian Math. Surveys, 18:85–191, (1963).   
[Arn88] V. I. Arnold: Geometrical Methods In The Theory Of Ordinary Differential Equations. Springer-Verlag, Berlin , (1988).   
[Arn89] V. I. Arnold: Mathematical Methods of Classical Mechanics. Springer-Verlag, GTM 60, Berlin Heidelberg, Second edition, (1989).   
[Dea94] P. Z. Ding and et al: Symplectic method of time evolution problem for atomic system. Atomic and Molecular Physics (in Chinese), 6:440, (1994).   
[DLea96] P. Z. Ding, Y. Li and et al: Symplectic method of caculation classical trojectory for microscopic chemical reaction. Chinese Academic Journals Science and Technology Abstracts (Express), 2(2):111, (1996).   
[DLM97a] A. Dullweber, B. Leimkuhler, and R. McLachlan: Symplectic splitting methods for rigid body molecular dynamics. J. Chem. Phys., 107:5840–5851, (1997).   
[DLM97b] A. Dullweber, B. Leimkuhler, and R. I. McLachlan: Split-Hamiltonian Methods for Rigid Body Molecular Dynamics. Technical Report 1997/NA11, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, (1997).   
[EMvdS07] D. Eberard, B.M. Maschkea, and A.J. van der Schaftb: An extension of Hamiltonian systems to the thermodynamic phase space: Towards a geometry of nonreversible processes. Reports on Mathematical Physics, 60(2):175–198, (2007).   
[Fen65] K. Feng: Difference schemes based on variational principle. J. of Appl. and Comput. Math.in Chinese, 2(4):238–262, (1965).   
[Fen85] K. Feng: On difference schemes and symplectic geometry. In K. Feng, editor, Proceedings of the 1984 Beijing Symposium on Differential Geometry and Differential Equations, pages 42–58. Science Press, Beijing, (1985).   
[Fen92] K. Feng: How to compute property Newton’s equation of motion. In L. A. Ying, B.Y. Guo, and I. Gladwell, editors, Proc of 2nd conf. on numerical method for $P D E { } _ { s }$ , pages $1 5 -$ 22. World Scientific, Singapore. (1992). Also see Collected Works of Feng Kang. Volume I, II. National Defence Industry Press, Beijing, (1995).   
[FQ87] K. Feng and M.Z. Qin: The symplectic methods for the computation of Hamiltonian equations. In Y. L. Zhu and B. Y. Guo, editors, Numerical Methods for Partial Differential Equations, Lecture Notes in Mathematics 1297, pages 1–37. Springer, Berlin, (1987).   
[FQ91a] K. Feng and M.Z. Qin: Hamiltonian Algorithms for Hamiltonian Dynamical Systems. Progr. Natur. Sci., 1(2):105–116, (1991).   
[FQ91b] K. Feng and M.Z. Qin: Hamiltonian algorithms for Hamiltonian systems and a comparative numerical study. Comput. Phys. Comm., 65:173–187, (1991).   
[FQ03] K. Feng and M. Q. Qin: Symplectic Algorithms for Hamiltonian Systems. Zhejiang Press for Science and Technology, Hangzhou, in Chinese, First edition, (2003).   
[FS95] K. Feng and Z. J. Shang: Volume-preserving algorithms for source-free dynamical systems. Numer. Math., 71:451–463, (1995). rithms. In Z. C. Shi and C. C. Yang, editors, Computational Mathematics in China, Contemporary Mathematics of AMS Vol 163, pages 1–32. AMS, (1994).   
[GDC91] B. Gladman, M. Duncan, and J. Candy: Symplectic integrators for long-term integration in celestial mechanics. Celest. Mech., 52:221–240, (1991).   
[GLCY00] L. Gao, Y. Li, X. Chen, and H. Yang: An attempt to seismic ray tracing with symplectic algorithm. Chinese Journal Geophys., 43(3):402–409, (2000).   
[Gol80] H. Goldstein: Classical Mechanics. Addison-Wesley Reading, Massachusetts, (1980).   
[GS84] V. Guillemin and S. Sternberg: Symplectic Techniques in Physics. Cambridge University Press, Cambridge, (1984).   
[GS94a] Z. Ge and C. Scovel: Hamiltonian truncation of shallow water equations. Letters in Mathematical Physics, 31:1–13, (1994).   
[Ham34] Sir W. R. Hamilton: On a general method in dynamics; by which the study of the motions of all free systems of attracting or repelling points is reduced to the search and differentiation of one central relation, or characteristic function. Phil. Trans. Roy. Soc. Part II for 1834, 247–308; Math. Papers, Vol. II, 103–161, Second edition, (1834).   
[Ham40] W.R. Hamilton: General methods in dynamics, volume I,II. Cambridge Univ. Press, (1940).   
[HIWZ95] T. Y. Huang, K. A. Innanen, C. B. Wang, and Z. Y. Zhao: Symplectic methods and their application to the motion of small bodies in the solar system. Earth, Moon, and Planets,, 71(3):179–183, (1995).   
[HKRS97] M. Hankel, B. Karasozen, P. Rentrop, and U. Schmitt: A Molecular Dynamics ¨ Model for Symplectic Integrators. Mathematical Modelling of Systems, 3(4):282–296, (1997).   
[HL97a] E. Hairer and P. Leone: Order barriers for symplectic multi-value methods. In D.F. Grifysis, D.F.Higham, and G.A. Watson, editors, Numerical analysis 1997 Proc. of the 17th Dundee Biennial Conference, June 24-27, 1997, Pitman Reserch Notes in math. series 380, pages 133–149, (1997).   
[IMKNZ00] A. Iserles, H. Z. Munthe-Kaas, S. P. Nørsett, and A. Zanna: Lie-group methods. Acta Numerica, 9:215–365, (2000).   
[JLL02] J. Ji, G. Li, and L. Liu: The dynamical simulations of the planets orbiting gj 876. Astrophys. J., 572: 1041C-1047, (2002).   
[Kle26] F. Klein: Vorlesungen uber ¨ die Entwicklung der Mathematik in 19 Jahrhundert. Teubner, (1926).   
[Kol54a] A. N. Kolmogorov: General theory of dynamical systems and classical mechanics. In Proc. Inter. Congr. Math., volume 1, pages 315–333, (1954).   
[Kol54b] A. N. Kolmogorov: On conservation of conditionally periodic motions under small perturbations of the Hamiltonian. Dokl. Akad. Nauk SSSR, 98:527–530, (1954).   
[KYN91] H. Kinoshita, H. Yoshida, and H. Nakai: Symplectic integrators and their application to dynamical astronomy. Celest. Mech. and Dyn. Astro., 50:59–71, (1991).   
[LDJW00] Y. X. Li, P. Z. Ding, M. X. Jin, and C. X. Wu: Computing classical trajectories of model molecule $A _ { 2 } B$ by symplectic algorithm. Chemical Journal of Chinese Universities, 15(8):1181–1186, (2000).   
[Lia97] X. Liao: Symplectic integrator for general near-integrable Hamiltonian systems. Celest. Mech. and Dyn. Astro., 66:243–253, (1997).   
[LL94] L. Liu and X. H. Liao: Numerical calculations in the orbital determination of an artificial satellite for a long arc. Celest. Mech., 59:221–235, (1994).   
[LL95] L. Liu and X. H. Liao: Existence of formal integrals of symplectic integrators. Celest. Mech., 63(1):113–123, (1995).   
[LL99] L. D. Landau and E. M. Lifshitz: Mechanics, Volume I of Course of Theoretical Physics. Corp. Butterworth, Heinemann, New York, Third edition, (1999).   
[LLL99] M. Luo, Y. Li, and H. Lin: The symplectic geometric description and algorithm of seismic wave propagation. In The 69-th Ann. Seg mecting, volume 199, pages 1825–1828, method based on spectral factorization on helix. Chinese Journal Geophys., 44(3):379–388, (2001).   
[LLL01b] M. Q. Luo, H. Liu, and Y. M. Li: Hamiltonian description and symplectic method of seismic wave propagation. Chinese Journal Geophys., 44(1):120–128, (2001).   
[LLZD01] X. S. Liu, X. M. Liu, Z. Y. Zhao, and P. Z. Ding: Numerical solution of 2-D timeindependent schrodings. ¨ Int. J. Quant. Chem., 83:303–309, (2001).   
[LLZW94] L. Liu, X. Liao, Z. Zhao, and C. Wang: Application of symplectic integrators to dynamical astronomy(3). Acta Astronomica Sinica, 35:1, (1994).   
[LQ88] C.W. Li and M.Z. Qin: A symplectic difference scheme for the infinite dimensional Hamiltonian system. J. Comput. Appl. Math., 6:164–174, (1988).   
[LQ95a] S. T. Li and M. Qin: Lie–Poisson integration for rigid body dynamics. Computers Math. Applic., 30:105–118, (1995).   
[LQ95b] S. T. Li and M. Qin: A note for Lie–Poisson Hamilton-Jacobi equation and Lie-Poisson integrator. Computers Math. Applic., 30:67–74, (1995).   
[LQHD07] X.S. Liu, Y.Y. Qi, J. F. He, and P. Z. Ding: Recent progress in symplectic algorithms for use in quantum systems. Communications in Computational Physics, 2(1):1–53, (2007).   
[LSD02a] X. S. Liu, L. W. Su, and P. Z. Ding: Symplectic algorithm for use in computing the time independent Schrodinger equation. Int. J. Quant. Chem., 87:1–11, (2002).   
[LSD02b] X.S. Liu, L.W. Su, and P. Z. Ding: Symplectic algorithm for use in computing the time independent schrodinger equation. ¨ Int. J. Quant. Chem., 87(1):1–11, (2002).   
[LYC06] H. Liu, J.H. Yuan, J.B. Chen, H. Shou, and Y.M. Li: Theory of large-step depth extrapolation. Chinese Journal Geophys., 49(6):1779–1793, (2006).   
[LZL93] X. Liao, Z. Zhao, and L. Liu: Application of symplectic algorithms in computation of LCN. Acta Astronomica Sinica, 34(2):201–207, (1993).   
[Men84] C.R. Menyuk: Some properties of the discrete Hamiltonian method. Physica $D$ , 11:109–129, (1984).   
[MF81] V.P. Maslov and M. V. Fedoriuk: Semi-classical approximation in quantum mechanics. D. Reidel Publishing Company, Dordrecht Holland, First edition, (1981).   
[MK95] H. Munthe-Kaas. Lie–Butcher theory for Runge–Kutta methods. BIT, 35(4):572–587, (1995).   
[MK98] H. Munthe-Kaas: Runge–Kutta methods on Lie groups. BIT, 38(1):92–111, (1998).   
[MK99] H. Munthe-Kaas: High order Runge–Kutta methods on manifolds. Appl. Numer. Math., 29:115–127, (1999).   
[MKO99] H. Munthe-Kaas and B. Owren: Computations in a free Lie algebra. Phil. Trans. Royal Soc. A, 357:957–981, (1999).   
[MKQZ01] H. Munthe-Kaas, G. R. W. Quispel, and A. Zanna: Generalized polar decompositions on Lie groups with involutive automorphisms. Foundations of Computational Mathematics, 1(3):297–324, (2001).   
[MKZ97] H. Munthe-Kaas and A. Zanna: Numerical integration of differential equations on homogeneous manifolds. In F. Cucker and M. Shub, editors, Foundations of Computational Mathematics, pages 305–315. Springer Verlag, (1997).   
[MM05] K.W. Morton and D.F. Mayers: Numerical Solution of Partial Differential Equations: an introduction. Cambridge University Press, Cambridge, Second edition, (2005).   
[MR99] J. E. Marsden and T. S. Ratiu: Introduction to Mechanics and Symmetry. Number 17 in Texts in Applied Mathematics. Springer-Verlag, second edition, (1999).   
[MNSS91] R. Mrugała, J.D. Nulton, J.C. Schon, and P. Salamon: Contact structure in thermodynamic theory. Reports on Mathematical Physics, 29:109C121, (1991).   
[Mos62] J. Moser: On invariant curves of area-preserving mappings of an annulus. Nachr. Akad. Wiss. Gottingen, II. Math.-Phys., pages 1–20, (1962).   
[QC00] M. Z. Qin and J.B. Chen: Maslov asymptotic theory and symplectic algorithm. Chinese Journal Geophys., 43(4):522–533, (2000).   
[Qin89] M. Z. Qin: Cononical difference scheme for the Hamiltonian equation. Mathematical Methodsand in the Applied Sciences, 11:543–557, (1989).   
[Qin97a] M. Z. Qin: A symplectic schemes for the pde’s. AMS/IP studies in Advanced Mathemateics, 5:349–354, (1997).   
[QT90] G. D. Quinlan and S. Tremaine: Symmetric multistep methods for the numerical integration of planetary orbits. Astron. J., 100:1694–1700, (1990).   
[QZ90] M. Z. Qin and M. Q. Zhang: Explicit Runge–Kutta–like Schemes to Solve Certain Quantum Operator Equations of Motion. J. Stat. Phys., 60(5/6):839–843, (1990).   
[QZ92] M. Z. Qin and W.J. Zhu: Construction of Higher Order Symplectic Schemes by Composition. Computing, 47:309–321, (1992).   
[QZ93a] M. Z. Qin and W. J. Zhu: Volume-preserving schemes and numerical experiments. Computers Math. Applic., 26:33–42, (1993).   
[QZ93b] M. Z. Qin and W. J. Zhu: Volume-preserving schemes and applications. Chaos, Soliton & Fractals, 3(6):637–649, (1993).   
[QZ94] M. Z. Qin and W. J. Zhu: Multiplicative extrapolation method for constructing higher order schemes for ode’s. J. Comput. Math., 12:352–356, (1994).   
[Rut83] R. Ruth: A canonical integration technique. IEEE Trans. Nucl. Sci., 30:26–69, (1983).   
[Sch44] E. Schrodinger: ¨ Scripta mathematica, 10:92–94, (1944).   
[Shu93] H.B. Shu: A new approach to generating functions for contact systems. Computers Math. Applic., 25:101–106, (1993).   
[ST92a] P. Saha and S. Tremaine: Symplectic integrators for solar system dynamics. Astron. J., 104:1633–1640, (1992).   
[Syn44] J.L. Synge: Scripta mathematica, 10:13–24, (1944).   
[Vog56] R. de Vogelaere: Methods of integration which preserve the contact transformation property of the Hamiltonian equations. Report No. 4, Dept. Math., Univ. of Notre Dame, Notre Dame, Ind., Second edition, (1956).   
[War83] F. W. Warner: Foundations of Differentiable Manifolds and Lie Groups. GTM 94. Springer-Verlag, Berlin, (1983).   
[Wei77] A. Weinstein: Lectures on symplectic manifolds. In CBMS Regional Conference, 29. American Mathematical Society,Providence,RI, (1977).   
[wey39] H. weyl: The Classical Groups. Princeton Univ. Press, Princeton, Second edition, (1939).   
[WH91] J. Wisdom and M. Holman: Symplectic maps for the $N$ -body problem. Astron. J., 102:1528–1538, (1991).   
[WHT96] J. Wisdom, M. Holman, and J. Touma: Symplectic Correctors. In Jerrold E. Marsden, George W. Patrick, and William F. Shadwick, editors, Integration Algorithms and Classical Mechanics, volume 10 of Fields Institute Communications, pages 217–244. Fields Institute, American Mathematical Society, July (1996).   
[WJX01] B. Wang, Z. Ji, and Q. Xiao: the atmospheric dynamics of the equation Hamiltonian algorithm. Chinese Journal Computational Physics, 18(1):289–297, (2001).   
[WZJ95] B. Wang, Q. Zhen, and Z. Ji: The system of square conservation and Hamiltonian systems. Science in China (series A), 25(7):765–770, (19950.   
[Yos90] H. Yoshida: Construction of higher order symplectic integrators. Physics Letters A, 150:262–268, (1990).   
[ZL93] Z. Zhao and L. Liu: The stable regions of triangular libration points of the planets . Acta Astronomica Sinica, 34(1):56–65, (1993).   
[ZL94] Z. Zhao and L. Liu: The stable regions of triangular libration points of the planets II. Acta Astronomica Sinica, 35(1):76–83, (1994).   
[ZLL92] Z. Zhao, X. Liao, and L. Liu: Application of symplectic integrators to dynamical astronomy. Acta Astronomica Sinica, 33(1):33–41, (1992).

# Chapter 1. Preliminaries of Differentiable Manifolds

Before introducing the concept of differentiable manifold, we first explain what mapping is. Given two sets $X$ , $Y .$ , and a corresponding principle, if for any $x \in X$ , there exists $y = f ( x ) \in Y$ to be its correspondence, then $f$ is a mapping of the set $X$ into the set $Y$ , which is denoted as $f : X \to Y . X$ is said to be the domain of definition of $f$ , and $f ( x ) = \{ f ( x ) \mid x \in X \} \subset Y$ is said to be the image of $f$ . If $f ( X ) = Y$ , then $f$ is said to be surjective or onto; if $f ( x ) = f ( x ^ { \prime } ) \Rightarrow x = x ^ { \prime }$ , then $f$ is said to be injective (one-to-one); if $f$ is both surjective and injective (i.e., $X$ and $Y$ have a one-to-one correspondence under $f$ ), $f$ is said to be bijective. For a bijective mapping $f$ , if we define $x = f ^ { - 1 } ( y )$ , then $f ^ { - 1 } : Y \to X$ is said to be the inverse mapping of $f$ . In abstract algebra, a homomorphism is a structure-preserving map between two algebraic structures (such as groups, rings, or vector spaces). For example, for two groups $G$ and $G ^ { \prime }$ and a mapping $f : G \to G ^ { \prime }$ , $a  f ( a )$ , if $f ( a , b ) = f ( a ) \cdot f ( b ) , \forall a , b \in G$ , then $f$ is said to be a homomorphism from $G$ to $G ^ { \prime }$ . A homomorphism is a map from one algebraic structure to another of the same type that preserves all the relevant structures, i.e., properties such as identity element, inverse element, and binary operations. An isomorphism is a bijective homomorphism. If $f$ is a $G  G ^ { \prime }$ homomorphic mapping, and also a one-to-one mapping from $G$ to $G ^ { \prime }$ , then $f$ is said to be a $G  G ^ { \prime }$ isomorphic mapping. An epimorphism is a surjective homomorphism. Given two topological spaces $( x , \tau )$ and $( y , \tau )$ , if the mapping $f : X \to Y$ is one-to-one, and both $f$ and its inverse mapping $f ^ { - 1 } : Y \to X$ are continuous, then $f$ is said to be a homeomorphism. If $f$ and $f ^ { - 1 }$ are also differentiable, then the mapping is said to be diffeomorphism. A monomorphism (sometimes called an extension) is an injective homomorphism. A homomorphism from an object to itself is said to be an endomorphism. An endomorphism that is also an isomorphism is said to be an automorphism. Given two manifolds $M$ and $N$ , a bijective mapping $f$ from $M$ to $N$ is called a diffeomorphism if both $f : M \to N$ and its inverse $f ^ { - 1 } : N \to M$ are differentiable (if these functions are $r$ times continuously differentiable, $f$ is said to be a $C ^ { r }$ -diffeomorphism).

Many differential mathematical methods and concepts are used in classical mechanics and modern physics: differential equations, phase flow, smooth mapping, manifold, Lie group and Lie algebra, and symplectic geometry. If one would like to construct a new numerical method, one needs to understand these basic theories and concepts. In this book, we briefly explain manifold, symplectic algebra, and symplectic geometry. In a series of books[AM78,Che53,Arn89,LM87,Ber00,Wes81] can be found these materials.

# 1.1 Differentiable Manifolds

The concept of manifold is an extension of Euclidean space. Roughly speaking, a manifold is an abstract mathematical space where every point has a neighborhood that resembles Euclidean space (homeomorphism). Differentiable manifold is one of the manifolds that can have differentiable structures.

# 1.1.1 Differentiable Manifolds and Differentiable Mapping

Definition 1.1. A Hausdorff space $M$ with countable bases is called an $n$ -dimensional topological manifold, if for any point in $M$ there exists an open neighborhood homeomorphic to an open subset of $\mathbf { R } ^ { n }$ .

Remark 1.2. Let $( U , \varphi ) , ( V , \psi )$ be two local coordinate systems (usually called chart) on the topological manifold $M . \ ( U , \varphi ) , ( V , \psi )$ are said to be compatible, if $U \cap V = \emptyset$ , or the change of coordinates $\varphi \circ \psi ^ { - 1 }$ and $\psi \circ \varphi ^ { - 1 }$ are smooth when $U \cap V \neq \emptyset$ .

Definition 1.3. A chart is a domain $U \subset \mathbf { R } ^ { n }$ together with a 1 to 1 mapping $\varphi : W \to$ $U$ of a subset $W$ of the manifold $M$ onto $U$ . $\varphi ( x )$ is said to be the image of the point $x \in W \subset M$ on the chart $U$ .

Definition 1.4. A collection of charts $\varphi _ { i } : W _ { i } \to U _ { i }$ is an atlas on $M$ if $1 ^ { \circ }$ Any two charts are compatible. $2 ^ { \circ }$ Any point $x \in M$ has an image on at least one chart.

Remark 1.5. If a smooth atlas on a topological manifold $M$ possesses with its all compatible local coordinate systems (chart), then this smooth atlas is called the maximum atlas.

Definition 1.6. If an $n$ -dimensional topological manifold $M$ is equipped with the maximal smooth atlas $\mathcal { A }$ , then $( M , A )$ is called the $n$ -dimensional differentiable manifold, and $\mathcal { A }$ is called the differentiable structure on $M$ .

Definition 1.7. Two atlases on $M$ are equivalent if their union is also an atlas (i.e., if any chart of the first atlas is compatible with any chart of the second).

Remark 1.8. Suppose $M$ is the $n$ -dimensional topological manifold, $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \}$ is a smooth atlas on $M$ . Then there exists a unique differentiable structure $\ b { A } ^ { * }$ , which contains $\mathcal { A }$ . Hence, a smooth atlas determines a unique differentiable structure on $M$ . The local coordinate system will be called (coordinate) chart subsequently.

Definition 1.9. A differentiable manifold structure on $M$ is a class of equivalent atlases.

Definition 1.10. A differentiable manifold $M$ is a set $M$ together with a differentiable manifold structure on it. A differentiable manifold structure is induced on set $M$ if an atlas consisting of compatible charts is prescribed.

Below are examples of differentiable manifold.

Example 1.11. $\mathbf { R } ^ { n }$ is an $n$ -dimensional differentiable manifold. Let $\mathcal { A } = \{ ( \mathbf { R } ^ { n } , I ) \}$ , where $I$ is the identity mapping.

Example 1.12. $S ^ { n }$ is an $n$ -dimensional differentiable manifold. We only discuss the $n = 1$ case. Let

$$
\begin{array} { r l } & { U _ { 1 } = \{ ( u ^ { 1 } , u ^ { 2 } ) \in S ^ { 1 } | u ^ { 1 } > 0 \} , \quad U _ { 2 } = \{ ( u ^ { 1 } , u ^ { 2 } ) \in S ^ { 1 } | u ^ { 1 } < 0 \} , } \\ & { } \\ & { U _ { 3 } = \{ ( u ^ { 1 } , u ^ { 2 } ) \in S ^ { 1 } | u ^ { 2 } > 0 \} , \quad U _ { 4 } = \{ ( u ^ { 1 } , u ^ { 2 } ) \in S ^ { 1 } | u ^ { 2 } < 0 \} . } \end{array}
$$

Define $\varphi _ { i } : U _ { i } \to ( - 1 , 1 )$ , such that (s.t.)

$$
\varphi _ { i } ( u ^ { 1 } , u ^ { 2 } ) = u ^ { 2 } , \quad i = 1 , 2 ; \quad \varphi _ { i } ( u ^ { 1 } , u ^ { 2 } ) = u ^ { 1 } , \quad i = 3 , 4 .
$$

Note that on $\varphi _ { 1 } ( U _ { 1 } \cap U _ { 3 } )$

$$
\varphi _ { 3 } \circ \varphi _ { 1 } ^ { - 1 } : u ^ { 2 } \longrightarrow ( \sqrt { 1 - ( u ^ { 2 } ) ^ { 2 } } , u ^ { 2 } ) \longrightarrow \sqrt { 1 - ( u ^ { 2 } ) ^ { 2 } }
$$

is smooth, then $\scriptstyle { \mathcal { A } } = \{ ( U _ { k } , \varphi _ { k } ) \}$ is a smooth atlas on $S ^ { 1 }$ .

Example 1.13. $R P ^ { n }$ is an $n$ -dimensional differentiable manifold.

Let

$$
U _ { k } = \{ [ ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) ] \mid ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) \in S ^ { n } , u ^ { k } \neq 0 \} , \quad k = 1 , \cdots , n + 1
$$

defines $\varphi _ { k } : U _ { k } \to \operatorname { I n t } B ^ { n } ( 1 )$ , s.t.

$$
\varphi _ { k } ( [ ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) ] ) = u ^ { k } | u ^ { k } | ^ { - 1 } ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { k - 1 } , u ^ { k + 1 } , \cdot \cdot \cdot , u ^ { n + 1 } ) ,
$$

where $B ^ { n } ( 1 ) = \left\{ ( u ^ { 1 } , \cdot \cdot \cdot , u ^ { n } ) \in { \bf \delta R } ^ { n } \Big | \sum _ { i = 1 } ^ { n } ( u ^ { i } ) ^ { 2 } \le 1 \right\}$ . It is easy to prove that $\mathcal { A }$ $\mathbf { \Omega } = \{ ( U _ { k } , \varphi _ { k } ) \}$ is a smooth atlas on $R P ^ { n }$ .

Example 1.14. Let $M , N$ be $m$ - and $n$ -dimensional differentiable manifolds, respectively, then $M \times N$ is a $m + n$ dimensional differentiable manifold (product manifold).

Suppose ${ \mathcal { A } } = \{ ( U _ { \alpha } , \varphi _ { \alpha } ) \} , B = \{ ( V _ { \alpha } , \psi _ { \alpha } ) \}$ are smooth atlases on $M , N$ respectively. Denote $\mathcal { A } \times \mathcal { B } { = } \{ ( U _ { \alpha } \times V _ { \lambda } , \varphi _ { \alpha } \times \psi _ { \lambda } ) \}$ , where $\varphi _ { \alpha } \times \psi _ { \lambda } \colon U _ { \alpha } \times V _ { \lambda } \to$ $\varphi _ { \alpha } ( U _ { \alpha } ) \times \psi _ { \lambda } ( V _ { \lambda } ) , ( \varphi _ { \alpha } \times \psi _ { \lambda } ) ( p , q ) = { \big ( } \varphi _ { \alpha } ( p ) , \psi _ { \lambda } ( q ) { \big ) } , ( p , q ) \in U _ { \alpha } \times V _ { \lambda }$ , then $\mathcal { A } \times \mathcal { B }$ is a smooth atlas on $M \times N$ .

Definition 1.15. Let $M , N$ be $m$ - and $n$ -dimensional differentiable manifolds, respectively. A continuous mapping $f : M \to N$ is called $C ^ { k }$ differentiable at $p \in M$ , if the local representation $\widehat { f } = \psi \circ f \circ \varphi ^ { - 1 } : \varphi ( U ) \to \psi ( V )$ is $C ^ { k }$ differentiable for the charts $( U , \varphi ) , ( V , \psi )$ corresponding to points $p$ and $f ( \boldsymbol p )$ , and $f ( U ) \subset V$ . If $f$ is $C ^ { k }$ differentiable in each $p \in M$ , then $f$ is called $C ^ { k }$ differentiable, or called $C ^ { k }$ mapping. See Fig. 1.1.

![](images/39508fc6254819a70f06e2da49b1e6b8112a613660f261ed35290dbf5e95258e.jpg)  
Fig. 1.1. A differentiable mapping

Example 1.16. Let $M _ { 1 }$ , $M _ { 2 }$ be $m$ - and $n$ -dimensional differentiable manifolds, respectively. Define $\theta _ { 1 } : M _ { 1 } \times M _ { 2 } \to M _ { 1 }$ , $\theta _ { 2 } : M _ { 1 } \times M _ { 2 } \to M _ { 2 }$ , such that

$$
\theta _ { 1 } ( p , q ) = p , \quad \theta _ { 2 } ( p , q ) = q , \quad \forall ( p , q ) \in M _ { 1 } \times M _ { 2 } ,
$$

then $\theta _ { 1 } , \theta _ { 2 }$ are all smooth mappings.

If the charts on $M _ { 1 } , M _ { 2 }$ are denoted by $( U , \varphi ) , ( V , \psi )$ , then it is easy to show that $( U \times V , \varphi \times \psi )$ is the chart on $\mathbf { M } _ { 1 } \times M _ { 2 }$ . Thus, the local coordinate expression of $\theta _ { 1 }$ ,

$$
\widehat { \theta } _ { 1 } = \varphi \circ \theta _ { 1 } \circ ( \varphi \times \psi ) ^ { - 1 } : ( \varphi \times \psi ) ( U \times V ) \longrightarrow \varphi ( U ) , \quad \widehat { \theta } _ { 1 } ( u , v ) = u
$$

is a smooth mapping. Therefore, $\theta _ { 1 }$ is a smooth mapping. Likewise, $\theta _ { 2 }$ is also a smooth mapping.

Example 1.17. Let $M , N _ { 1 } , N _ { 2 }$ be differentiable manifolds.

$$
f _ { 1 } : M \longrightarrow N _ { 1 } , \quad f _ { 2 } : M \longrightarrow N _ { 2 }
$$

are $C ^ { k }$ -mapping. Define

$$
f : M \longrightarrow N _ { 1 } \times N _ { 2 } , \quad f ( p ) = ( f _ { 1 } ( p ) , f _ { 2 } ( p ) ) , \quad \forall p \in M ,
$$

then $f$ is a $C ^ { k }$ -mapping.

$\forall p _ { 0 } \in M$ , let $N _ { 1 }$ contain the chart $( V , \psi )$ of $f _ { 1 } ( p _ { 0 } )$ , and let $N _ { 2 }$ contain the chart $( W , \chi )$ of $f _ { 2 } ( \boldsymbol { p } _ { 0 } )$ , and $M$ contain the chart $( U , \varphi )$ of $p _ { 0 }$ . Assume $f _ { 1 } ( U ) \subset V , f _ { 2 } ( U ) \subset$ $W$ , and

$$
\begin{array} { r l } & { \widehat { f } _ { 1 } : \psi \circ f _ { 1 } \circ \varphi ^ { - 1 } : \varphi ( U ) \longrightarrow \psi ( V ) , } \\ & { } \\ & { \widehat { f } _ { 2 } : \chi \circ f _ { 2 } \circ \varphi ^ { - 1 } : \varphi ( U ) \longrightarrow \chi ( W ) } \end{array}
$$

are all $C ^ { k }$ -mapping, and $( V \times W , \varphi \times \chi )$ is a chart that contains $( f _ { 1 } ( p _ { 0 } ) , f _ { 2 } ( p _ { 0 } ) ) =$ $f ( p _ { 0 } )$ on the product manifold $N _ { 1 } \times N _ { 2 }$ , which satisfies $f ( U ) \subset V \times W$ . Then we have

$$
\widehat { f } = ( \psi \times \chi ) \circ f \circ \varphi ^ { - 1 } : \varphi ( U ) \longrightarrow ( \psi \times \chi ) ( U \times W ) , \quad \widehat { f } = ( \widehat { f } _ { 1 } , \widehat { f } _ { 2 } ) ,
$$

i.e., $f$ is $C ^ { k }$ -mapping.

Remark 1.18. According to the definition, if $f : { \cal M }  { \cal N } , g : { \cal N }  { \cal L }$ are $C ^ { k }$ - mappings, then $g \circ f : M \to L$ is also a $C ^ { k }$ -mapping.

Definition 1.19. Let $M , N$ be differentiable manifolds, $f : M \to N$ is a homeomorphism. If $f , f ^ { - 1 }$ are smooth, then $f$ is called diffeomorphism from $M$ to $N$ . If there exists a diffeomorphism between differentiable manifolds $M$ and $N$ , then $M$ and $N$ are called differentiable manifolds under diffeomorphism, denoted by $M \simeq N$ .

If we define two smooth atlases $( { \bf R } , I ) , ( { \bf R } , \varphi )$ on $\mathbf { R }$ , and $\varphi : \mathbf { R }  \mathbf { R } , \varphi ( u ) = u ^ { 3 }$ , because the change of coordinates $I \circ \varphi ^ { - 1 } ( u ) = \sqrt [ 3 ] { u }$ in $u = 0$ is not differentiable, then $( \mathbf { R } , I )$ and $( \mathbf { R } , \varphi )$ determine two different differentiable structures $\mathcal { A }$ , $\mathcal { A } ^ { \prime }$ on $\mathbf { R }$ . However, if we define $f : ( \mathbf { R } , { \mathcal { A } } )  ( \mathbf { R } , { \mathcal { A } } ^ { \prime } )$ , $\{ f ( u ) \} = u ^ { 3 }$ , then $( \mathbf { R } , { \mathcal { A } } ) \simeq ( \mathbf { R } , { \mathcal { A } } ^ { \prime } )$ .

In fact, there exist examples that are not homeomorphism in a differentiable manifold, like the famous Milnor exotic sphere.

# 1.1.2 Tangent Space and Differentials

In order to establish the differential concept for differentiable mapping on a differentiable manifold, we first need to extend the concept of tangent of curve and tangent plane of surface in Euclidean space. If we take the tangent vector in Euclidean space not simply as a vector with size and direction, but as a linear mapping, which satisfies the Leibniz rule, from the differentiable functional space to $\mathbf { R }$ , then the definition of tangent vector can be given similarly for a manifold.

Let $M$ be the $m$ -dimensional differentiable manifold, $p \in M$ be a fixed point. Let $C ^ { \infty } ( p )$ be the set of all smooth functions that are defined in some neighborhood of $p$ . Define operations on $M$ that have the following properties:

$$
\begin{array} { l } { { ( f + g ) ( p ) = f ( p ) + g ( p ) , } } \\ { { \mathit { \Omega } } } \\ { { ( \alpha f ) ( p ) = \alpha f ( p ) , } } \\ { { \mathit { \Omega } } } \\ { { ( f g ) ( p ) = f ( p ) g ( p ) . } } \end{array}
$$

Definition 1.20. A tangent vector $X _ { p }$ at the point $p \in M$ is a mapping

$$
X _ { p } : C ^ { \infty } \longrightarrow \mathbf { R } ,
$$

that has the following properties:

$1 ^ { \circ }$ $X _ { p } ( f ) = X _ { p } ( g )$ , if $f$ , $g \in C ^ { \infty } ( p )$ are consistent in some neighborhood of the point $p$ .

$2 ^ { \circ }$ $X _ { p } ( \alpha f + \beta g ) = \alpha X _ { p } ( f ) + \beta X _ { p } ( g ) , \forall \ : f$ , $g \in C ^ { \infty } ( p )$ , $\forall \alpha$ , β ∈ R.

$3 ^ { \circ }$ $X _ { p } ( f g ) = f ( p ) X _ { p } ( g ) + g ( p ) X _ { p } ( f ) , \forall f , g \in C ^ { \infty } ( p )$ (which is equivalent to the derivative operation in Leibniz rule).

Denote $T _ { p } M = \{ { \mathrm { A l l } } $ tangent vectors at the point $p \in M \}$ and define operation:

$$
\begin{array} { r l } & { ( X _ { p } + Y _ { p } ) ( f ) = X _ { p } ( f ) + Y _ { p } ( f ) , } \\ & { ( k X _ { p } ) ( f ) = k X _ { p } ( f ) , \quad \forall f \in C ^ { \infty } ( p ) . } \end{array}
$$

It is easy to verify that $T _ { p } M$ becomes the vector space that contains the above operation, which is called the tangent space at the point $p$ of the differential manifold $M$ .

Remark 1.21. By definition of the tangent vector, it is easy to know that if $f$ is the constant function, $X _ { p } ( f ) = 0$ for $X _ { p } \in T _ { p } M$ .

Lemma 1.22. Let $( U , \varphi )$ be the chart that contains $p \in M$ , and let $x ^ { 1 } , \cdots , x ^ { m }$ , $\varphi ( p )$ $\mathbf { \Sigma } = ( a ^ { 1 } , \cdots , a ^ { m } )$ be the coordinate functions. If $f \in C ^ { \infty } ( p )$ , then there exists a function $g _ { i }$ in some neighborhood $W$ of $p \in M$ , such that

$$
f ( \boldsymbol { q } ) = f ( \boldsymbol { p } ) + \sum _ { i = 1 } ^ { m } ( x ^ { i } ( \boldsymbol { q } ) - a ^ { i } ) g _ { i } ( \boldsymbol { q } ) , \quad \forall \boldsymbol { q } \in W ,
$$

$$
g _ { i } ( p ) = \frac { \partial f } { \partial x ^ { i } } \Big | _ { p } \Big ( w h e r e \frac { \partial f } { \partial x ^ { i } } \Big | _ { p } = \frac { \partial } { \partial x ^ { i } } \Big | _ { p } ( f ) = \frac { \partial f \circ \varphi ^ { - 1 } } { \partial u ^ { i } } \Big | _ { \varphi ( p ) } \Big ) .
$$

Proof. Assume $\varphi ( p ) = O \in \mathbf { R } ^ { m }$ , and $f$ is well defined in some neighborhood of $p$ . Let $W = \varphi ^ { - 1 } ( B ^ { m } )$ . Then $\forall q \in W$ and we have

$$
f ( q ) - f ( p ) = f \circ \varphi ^ { - 1 } ( u ) - f \circ \varphi ^ { - 1 } ( O ) .
$$

After calculation, we obtain

$$
f ( q ) - f ( p ) = \sum _ { i = 1 } ^ { m } u ^ { i } \overline { { { g } } } _ { i } ( u ) ,
$$

where gi(u) =  10 ∂f ◦ ϕ−1∂ui ( $\begin{array} { r } { \overline { { g } } _ { i } ( u ) \ = \ \int _ { 0 } ^ { 1 } \frac { \partial f \circ \varphi ^ { - 1 } } { \partial u ^ { i } } ( s u ^ { 1 } , \cdots , s u ^ { m } ) \mathrm { d } s \ ( i \ = \ 1 , \cdots , m ) } \end{array}$ . Let $\overline { { { g } } } _ { i } ( \varphi ( q ) ) \ =$ $g _ { i } ( q )$ , then $g _ { i }$ is smooth on $W$ , and satisfies

$$
\begin{array} { l } { f ( q ) = f ( p ) + \displaystyle \sum _ { i = 1 } ^ { m } x ^ { i } ( q ) g _ { i } ( q ) , } \\ { g _ { i } ( p ) = \overline { { g } } _ { i } ( O ) = \frac { \partial f \circ \varphi ^ { - 1 } } { \partial u ^ { i } } \Big | _ { O } = \frac { \partial f } { \partial x ^ { i } } \Big | _ { p } . } \end{array}
$$

Hence lemma is proved.

Theorem 1.23. Define $\frac { \partial } { \partial x ^ { i } } \Big | _ { p } : C ^ { \infty } ( p )  { \bf R } , \frac { \partial } { \partial x ^ { i } } \Big | _ { p } ( f ) = \frac { \partial f \circ \varphi ^ { - 1 } } { \partial u ^ { i } } \Big | _ { \varphi ( p ) } , \forall f \in$ $C ^ { \infty } ( p )$ , then ${ \frac { \partial } { \partial x ^ { i } } } \bigg | _ { p } \left( i = 1 , \cdot \cdot \cdot , m \right)$ is a group of bases for $T _ { p } M$ . Therefore, $\mathrm { d i m } T _ { p } M$ $= m$ , and for $X _ { p } \in T _ { p } M$ , we have

$$
X _ { p } = \sum _ { i = 1 } ^ { m } X _ { p } ( x ^ { i } ) { \frac { \partial } { \partial x ^ { i } } } { \bigg | } _ { p } .
$$

Proof. $\forall X _ { p } \in T _ { p } M$ , as $f \in C ^ { \infty } ( p )$ . By Lemma 1.22, we know

$$
f = f ( \boldsymbol { p } ) + \sum _ { i = 1 } ^ { m } ( x ^ { i } - a ^ { i } ) g _ { i } ,
$$

then

$$
X _ { p } ( f ) = \sum _ { i = 1 } ^ { m } X _ { p } [ ( x ^ { i } - a ^ { i } ) g _ { i } ] = \sum _ { i = 1 } ^ { m } X _ { p } ( x ^ { i } ) { \frac { \partial f } { \partial x ^ { i } } } { \Big | } _ { p } = \sum _ { i = 1 } ^ { m } X _ { p } ( x ^ { i } ) { \frac { \partial } { \partial x ^ { i } } } { \Big | } _ { p } ( f ) .
$$

The decomposed coefficients, $\{ X _ { p } ( x ^ { i } ) \}$ , of $X _ { p }$ with respect to (w.r.t.) the bases $\frac { \partial } { \partial x ^ { i } } \Big | _ { p } \ ( i \ = \ 1 , \cdot \cdot \cdot , m )$ are called coordinates of the tangent vector $X _ { p }$ w.r.t. the char $( U , \varphi )$ . -

Remark 1.24. By Theorem 1.23 we know: if the coordinates of $X _ { p }$ w.r.t. chart $( U , \varphi )$ are defined as $( X _ { p } ( x ^ { 1 } ) , \cdot \cdot \cdot , X _ { p } ( x ^ { m } ) )$ , then $T _ { p } M$ and $\mathbf { R } ^ { m }$ are isomorphisms, and the basis for $T _ { p } M$ corresponds exactly to the standard basis for $\mathbf { R } ^ { m }$ , i.e., $\left. { \frac { \partial } { \partial x ^ { i } } } \right| _ { p } \mapsto e _ { i } =$ $( 0 , \cdots , 1 , 0 , \cdots , 0 )$ .

# 1. Definition and properties of differentials of mappings

The definition of differentials of a mapping is as follows:

Definition 1.25. Let $f : M \to N$ be a smooth mapping. $\forall p \in M$ , $X _ { p } \in T _ { p } M$ , we define $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ that satisfies:

$$
f _ { * p } ( X _ { p } ) ( g ) = X _ { p } ( g \circ f ) , \quad \forall g \in C ^ { \infty } ( f ( p ) ) .
$$

This linear mapping $f _ { \ast p }$ is called the differential of $f$ at the $p \in M$ .

Definition 1.26. The differential of the identity mapping $I$ is an identity mapping, i.e., $I _ { \ast p } : T _ { p } M \to T _ { p } M$ .

Remark 1.27. Let $M , N , L$ be differentiable manifolds, $p \in M$ , and $f : M \to N ,$ g : $N  L$ are smooth mappings, then $( g \circ f ) _ { \ast p } = g _ { \ast f ( p ) } \circ f _ { \ast p }$ .

Remark 1.28. If $f : M \to N$ is a diffeomorphism, then $f _ { \ast p } : T _ { p } M \to T _ { f ( p ) } N$ is a isomorphism.

Proposition 1.29. Let $x ^ { 1 } , \cdots , x ^ { m }$ , $y ^ { 1 } , \cdots , y ^ { n }$ be the coordinate functions of $( U , \varphi )$ , $( V , \psi )$ respectively, then

$$
f _ { \ast p } \bigg ( \frac { \partial } { \partial x ^ { i } } \Big | _ { p } \bigg ) = \sum _ { j = 1 } ^ { n } \frac { \partial f _ { j } } { \partial x ^ { i } } \Big | _ { p } \frac { \partial } { \partial y ^ { j } } \Big | _ { f ( p ) } ,
$$

where $f _ { j } = y ^ { j } \circ f$ .