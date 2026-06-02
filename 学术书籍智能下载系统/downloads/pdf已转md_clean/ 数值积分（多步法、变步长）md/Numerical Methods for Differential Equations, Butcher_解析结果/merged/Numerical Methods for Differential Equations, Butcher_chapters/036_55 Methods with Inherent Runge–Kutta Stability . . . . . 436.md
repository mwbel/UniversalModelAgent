# 55 Methods with Inherent Runge–Kutta Stability . . . . . 436

550 Doubly companion matrices . . 436   
551 Inherent Runge–Kutta stability . 438   
552 Conditions for zero spectral radius 440   
553 Derivation of methods with IRK stability . 442   
554 Methods with property $F$ . 445   
555 Some non-stiff methods 446   
556 Some stiff methods . 447   
557 Scale and modify for stability 448   
558 Scale and modify for error estimation . 450

# References . 453

Index . 459

# Preface to the first edition

# Introductory remarks

This book represents an attempt to modernize and expand my previous volume, The Numerical Analysis of Ordinary Differential Equations: Runge– Kutta and General Linear Methods. It is more modern in that it considers several topics that had not yet emerged as important research areas when the former book was written. It is expanded in that it contains a comprehensive treatment of linear multistep methods. This achieves a better balance than the earlier volume which made a special feature of Runge–Kutta methods.

In order to accommodate the additional topics, some sacrifices have been made. The background work which introduced the earlier book is here reduced to an introductory chapter dealing only with differential and difference equations. Several topics that seem to be still necessary as background reading are now introduced in survey form where they are actually needed. Some of the theoretical ideas are now explained in a less formal manner. It is hoped that mathematical rigour has not been seriously jeopardized by the use of this more relaxed style; if so, then there should be a corresponding gain in accessibility. It is believed that no theoretical detail has been glossed over to the extent that an interested reader would have any serious difficulty in filling in the gaps.

It is hoped that lowering the level of difficulty in the exposition will widen the range of readers who might be able to find this book interesting and useful. With the same idea in mind, exercises have been introduced at the end of each section.

Following the chapter on differential and difference equations, Chapter 2 is presented as a study of the Euler method. However, it aims for much more than this in that it also reviews many other methods and classes of methods as generalizations of the Euler method. This chapter can be used as a broadranging introduction to the entire subject of numerical methods for ordinary differential equations.

Chapter 3 contains a detailed analysis of Runge–Kutta methods. It includes studies of the order, stability and convergence of Runge–Kutta methods and also considers in detail the design of efficient explicit methods for non-stiff problems. For implicit methods for stiff problems, inexpensive implementation costs must be added to accuracy and stability as a basic requirement. Recent work on each of these questions is surveyed and discussed.

Linear multistep methods, including the combination of two methods as predictor–corrector pairs, are considered in Chapter 4. The theory interrelating stability, consistency and convergence is presented together with an analysis of order conditions. This leads to a proof of the (first) ‘Dahliquist barrier’. The methods in this class which are generally considered to be the most important for the practical solution of non-stiff problems are the Adams– Bashforth and Adams–Moulton formulae. These are discussed in detail, including their combined use as predictor–corrector pairs. The application of linear multistep methods to stiff problems is also of great practical importance and the treatment will include an analysis of the backward difference formulae.

In Chapter 5 the wider class of general linear methods is introduced and analysed. Questions analogous to those arising in the classical Runge–Kutta and linear multistep methods – that is, questions of consistency, stability, convergence and order – are considered and explored. Several sub-families of methods, that have a potential practical usefulness, are examined in detail. This includes the so-called DIMSIM methods and a new type of method exhibiting what is known as inherent Runge–Kutta stability.

The remarks in the following paragraphs are intended to be read following Chapter 5.

# Concluding remarks

Any account of this rapidly evolving subject is bound to be incomplete. Complete books are all alike; every incomplete book is incomplete in its own way.

It has not been possible to deal adequately with implementation questions. Numerical software for evolutionary problems entered its modern phase with the DIFSUB code of Gear (1971a). ‘Modern’ in this sense means that most of the ingredients of subsequent codes were present. Both stiff and nonstiff problems are catered for, provision is made for Jacobian calculation either by subroutine call or by difference approximation; the choice is up to the user. Most importantly, automatic selection of stepsize and order is made dynamically as the solution develops. Compared with this early implementation of linear multistep methods, the Radau code (Hairer and Wanner, 1996) uses implicit Runge–Kutta methods for the solution of stiff problems.

In recent years, the emphasis in numerical methods for evolutionary problems has moved beyond the traditional areas of non-stiff and stiff problems. In particular, differential-algebraic equations have become the subject of intense analysis as well as the development of reliable and efficient algorithms for problems of variable difficulty, as measured for example by the indices of the problems. Some basic references in this vibrant area are Brenan, Campbell and Petzold (1989) and Hairer, Lubich and Roche (1989) In particular, many codes are now designed for applications to stiff ordinary differential equations in which algebraic constraints also play a role. On the Runge–Kutta side, Radau is an example of this multipurpose approach. On the linear multistep side, Petzold’s DASSL code is closely related to Gear’s DIFSUB but has the capability of solving differential-algebraic equations, at least of low index.

Many problems derived from mechanical systems can be cast in a Hamiltonian formulation. To faithfully model the behaviour of such problems it is necessary to respect the symplectic structure. Early work on this by the late Feng Kang has led to worldwide activity in the study of this type of question. A basic reference on Hamiltonian problems is Sanz-Serna and Calvo (1994).

The emphasis on the preservation of qualitative features of a numerical solution has now grown well beyond the Hamiltonian situation and has become a mathematical discipline in its own right. We mention just two key references in this emerging subject of ‘geometric integration’. They are Iserles, et al. (2000) and Hairer, Lubich and Wanner (2006).

# Internet commentary

Undoubtedly there will be comments and suggestions raised by readers of this volume. A web resource has been developed to form a commentary and information exchange for issues as they arise in the future. The entry point is http://www.math.auckland.ac.nz/\~butcher/book

# Acknowledgements

I acknowledge with gratitude the support and assistance of many people in the preparation of this volume. The editorial and production staff at Wiley have encouraged and guided me through the publishing process. My wife, children, grandchildren and stepchildren have treated me gently and sympathetically.

During part of the time I have been working on this book, I have received a grant from the Marsden Fund. I am very grateful for this assistance both as an expression of confidence from my scientific colleagues in New Zealand and as practical support.

The weekly workshop in numerical analysis at The University of Auckland has been an important activity in the lives of many students, colleagues and myself. We sometimes refer to this workshop as the ‘Runge–Kutta Club’. Over the past five or more years especially, my participation in this workshop has greatly added to my understanding of numerical analysis through collaboration and vigorous discussions. As this book started to take shape they have provided a sounding board for many ideas, some of which were worked on and improved and some of which were ultimately discarded. Many individual colleagues, both in Auckland and overseas, have read and worked through drafts of the book at various stages of its development. Their comments have been invaluable to me and I express my heartfelt thanks.

Amongst my many supportive colleagues, I particularly want to name Christian Brouder, Robert Chan, Tina Chan, David Chen, Allison Heard, Shirley Huang, Arieh Iserles, Zdzislaw Jackiewicz, Pierre Leone, Taketomo (Tom) Mitsui, Nicolette Moir, Steffen Schulz, Anjana Singh, Angela Tsai, Priscilla Tse and Will Wright.

# Preface to the second edition

# Reintroductory remarks

The incremental changes incorporated into this edition are an acknowledgement of progress in several directions. The emphasis of structure-preserving algorithms has driven much of this recent progress, but not all of it. The classical linear multistep and Runge–Kutta methods have always been special cases of the large family of general linear methods, but this observation is of no consequence unless some good comes of it. In my opinion, there are only two good things that might be worth achieving. The first is that exceptionally good methods might come to light which would not have been found in any other way. The second is that a clearer insight and perhaps new overarching theoretical results might be expressed in the general linear setting. I believe that both these aims have been achieved but other people might not agree. However, I hope it can be accepted that some of the new methods which arise naturally as general linear methods have at least some potential in practical computation. I hope also that looking at properties of traditional methods from within the general linear framework will provide additional insight into their computational properties.

# How to read this book

Of the five chapters of this book, the first two are the most introductory in nature. Chapter 1 is a review of differential and difference equations with a systematic study of their basic properties balanced against an emphasis on interesting and prototypical problems. Chapter 2 provides a broad introduction to numerical methods for ordinary differential equations. This is motivated by the simplicity of the Euler method and a view that other standard methods are systematic generalizations of this basic method. If Runge–Kutta and linear multistep methods are generalizations of Euler then so are general linear methods and it is natural to introduce a wide range of multivalue–multistage methods at this elementary level.

A reading of this book should start with these two introductory chapters. For a reader less experienced in this subject this is an obvious entry point but they also have a role for a reader who is ready to go straight into the later chapters. For such readers they will not take very long but they do set the scene for an entry into the most technical parts of the book.

Chapter 3 is intended as a comprehensive study of Runge–Kutta methods. A full theory of order and stability is presented and at least the early parts of this chapter are prerequisites for Chapter 5 and to a lesser extent for Chapter 4. The use of B-series, or the coefficients that appear in these series, is becoming more and more a standard tool for a full understanding of modern developments in this subject.

Chapter 4 is full study of linear multistep methods. It is based on Dahlquists’ classic work on consistency, stability and order and includes analysis of linear and nonlinear stability. In both Chapters 3 and 4 the use of order stars to resolve order and stability questions is complemented by the introduction of order arrows. It is probably a good idea to read through most of Chapter 4 before embarking on Chapter 5. This is not because general linear methods are intrinsically inaccessible, but because an appreciation of their overarching nature hinges on an appreciation of the special cases they include.

General linear methods, the subject of Chapter 5, treat well-known methods in a unified way, but it is hoped they do more than this. There really seem to be new and useful methods buried amongst them which cannot be easily motivated in any other way. Thus, while this chapter needs to be put aside to be read as a culmination, it should not be put off too long. There is so much nice mathematics already associated with these methods, and the promise of more to come provides attraction enough. It is general linear methods, and the stability functions associated with them that really put order arrows in their rightful place.

# Internet support pages

For additional information and supporting material see http://www.math.auckland.ac.nz/\~butcher/ODE-book-2008

# Reacknowledgements

I have many people to thank and to rethank in my efforts to produce an improved edition. My understanding of the stability and related properties of general linear methods has been sharpened by working with Adrian Hill and Laura Hewitt. Helmut Podhaisky has given me considerable help and advice especially on aspects of general linear method implementation. My special thanks to Jane HyoJin Lee for her assistance with the final form of the manuscript. A number of people have made comments and provided corrections on the first edition or made constructive suggestions on early drafts of this new version. In addition to people acknowledged in some other way, I would like to mention the names of Ian Gladwell, Dawoomi Kim, Yoshio Komori, Ren´e Lamour, Dione O’Neale, Christian Perret, Higinio Ramos, Dave Simpson, Steve Stalos, Caren Tischendorf, Daniel Weiß, Frank Wrona and Jinsen Zhuang.
