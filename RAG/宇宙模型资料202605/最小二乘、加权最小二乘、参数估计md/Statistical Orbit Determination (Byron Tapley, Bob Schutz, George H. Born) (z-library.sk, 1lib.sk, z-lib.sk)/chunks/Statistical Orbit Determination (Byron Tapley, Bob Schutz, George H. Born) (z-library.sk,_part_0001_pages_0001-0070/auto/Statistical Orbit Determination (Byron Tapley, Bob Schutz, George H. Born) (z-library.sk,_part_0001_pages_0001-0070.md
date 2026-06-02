# Statistical Orbit Determination

![](images/5d2ce0898c63dc1e83769a3f2b96f44a90e774f96648e6c1ca0b9934c9e13dec.jpg)

Byron D. Tapley · Bob E.Schutz · George H. Born

# Statistical Orbit Determination

Byron D. Tapley

Center for Space Research The University of Texas at Austin

Bob E. Schutz Center for Space Research The University of Texas at Austin

George H. Born Colorado Center for Astrodynamics Research University of Colorado, Boulder

Senior Publishing Editor   
Project Manager   
Editorial Coordinator   
Marketing Manager   
Composition   
Printer   
Frank Cynar   
Simon Crump   
Jennifer Hele´   
Linda Beattie   
Author   
Maple-Vail Book Manufacturing Group   
Elsevier Academic Press   
200 Wheeler Road, Burlington, MA 01803, USA   
525 B Street, Suite 1900, San Diego, California 92101-4495, USA   
84 Theobald’s Road, London WC1X 8RR, UK

This book is printed on acid-free paper.

Copyright $\circledcirc$ 2004, Elsevier Inc. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or by any means, electronic or mechanical, including photocopy, recording, or any information storage and retrieval system, without permission in writing from the publisher.

Permissions may be sought directly from Elsevier’s Science & Technology Rights Department in Oxford, UK: phone: $( + 4 4 )$ 1865 843830, fax: $( + 4 4 )$ 1865 853333, e-mail: permissions@elsevier.com.uk. You may also complete your request on-line via the Elsevier homepage (http://elsevier.com), by selecting “Customer Support” and then “Obtaining Permissions.”

Library of Congress Cataloging-in-Publication Data Application submitted.

# British Library Cataloguing in Publication Data

A catalogue record for this book is available from the British Library.

ISBN: 0-12-683630-2

For all information on all Academic Press publications, visit our Web site at www.academicpressbooks.com.

Printed in the United States of America

04 05 06 07 08 09 9 8 7 6 5 4 3 2 1

# Contents

# Preface

# 1 Orbit Determination Concepts 1

1.1 Introduction .   
1.2 Uniform Gravity Field Model . 3 1.2.1 Formulation of the Problem 4 1.2.2 The Equation of the Orbit 1.2.3 The Role of the Observation 1.2.4 Linearization Procedure 9 1.2.5 State Transition Matrix . 11   
1.3 Background and Overview 13   
1.4 Summary 14   
1.5 References . 1 5   
1.6 Exercises 16

# 2 The Orbit Problem 17

# 2.1 Historical Background 17

2.2 Problem of Two Bodies: General Properties 19   
2.2.1 Motion in the Plane . 21   
2.2.2 Motion in Space 2 8   
2.2.3 Basic Coordinate Systems 29   
2.2.4 Orbit Elements and Position/Velocity 32   
2.2.5 Position/Velocity Prediction 35   
2.2.6 State Transition Matrix and Error Propagation . . 40

# 2.3 Perturbed Motion 44

2.3.1 Classical Example: Lunar Problem 45   
2.3.2 Variation of Parameters . 48   
2.3.3 Gravitational Perturbations: Mass Distribution 50   
2.3.4 Gravitational Perturbations: Oblateness and Other Effects 56   
2.3.5 Gravitational Perturbations: Third-Body Effects . . . 61   
2.3.6 Gravitational Perturbations: Temporal Changes in Gravity 64   
2.3.7 Gravitational Perturbations: General Relativity 65   
2.3.8 Nongravitational Perturbations: Atmospheric Resistance . 66   
2.3.9 Nongravitational Perturbations: Radiation Pressure 68   
2.3.10 Nongravitational Perturbations: Other . . 68   
2.3.11 Perturbed Equations of Motion: Summary . . 69   
2.4 Coordinate Systems and Time: Introduction 71   
2.4.1 Precession and Nutation 71   
2.4.2 Earth Rotation and Time 74   
2.4.3 Earth-Fixed and Topocentric Systems 77   
2.4.4 Transformation between ECF and ECI 82   
2.5 Orbit Accuracy 82   
2.6 References . . 84   
2.7 Exercises 87

# 3 Observations 93

3.1 Introduction 93   
3.2 Observations 9 4   
3.2.1 Ideal Range . 94   
3.2.2 Ideal Range-Rate 95   
3.2.3 Ideal Azimuth and Elevation Angles . 95   
3.2.4 Examples: Ideal Observations 95   
3.3 Conceptual Measurement Systems 99   
3.3.1 Range . 9 9   
3.3.2 Range-Rate . . 107   
3.4 Realization of Measurements 110   
3.4.1 Considerations 110   
3.4.2 Atmospheric Effects 110   
3.4.3 General Relativity 115   
3.5 Measurement Systems 116   
3.5.1 One-Way Range 116   
3.5.2 Two-Way Range 125   
3.5.3 Doppler Systems 132   
3.5.4 Examples 134   
3.6 Differenced Measurements 139   
3.6.1 Differenced GPS Measurements 140   
3.6.2 Differenced Altimeter Data . 145   
3.7 Satellite Positions 147   
3.8 Angles . . 148   
3.9 References . . 149   
3.10 Exercises 151   
4 Fundamentals of Orbit Determination 159   
4.1 Introduction . 159   
4.2 Linearization of the Orbit Determination Process 160   
4.2.1 The State Transition Matrix 164   
4.2.2 Solution for the State Transition Matrix 167   
4.2.3 Relating the Observations to an Epoch State . 172   
4.3 The Least Squares Solution . 173   
4.3.1 The Minimum Norm Solution 174   
4.3.2 Shortcomings of the Least Squares Solution 176   
4.3.3 Weighted Least Squares Solution 176   
4.3.4 An Alternate Least Squares Approach 178   
4.4 The Minimum Variance Estimate . 183   
4.4.1 Propagation of the Estimate and Covariance Matrix . 188   
4.4.2 Minimum Variance Estimate with A Priori Information . . 188   
4.5 Maximum Likelihood and Bayesian Estimation 190   
4.6 Computational Algorithm for the Batch Processor 194   
4.7 The Sequential Estimation Algorithm 199   
4.7.1 The Sequential Computational Algorithm 201   
4.7.2 The Extended Sequential Estimation Algorithm 209   
4.7.3 The Extended Sequential Computational Algorithm . 210   
4.7.4 The Prediction Residual 210   
4.8 Example Problems 211   
4.8.1 Linear System 211   
4.8.2 Spring-Mass Problem 216   
4.9 State Noise Compensation Algorithm 220   
4.9.1 The Gauss-Markov Process 230   
4.10 Information Filter 233   
4.11 Batch and Sequential Estimation 237   
4.12 Observability 237   
4.13 Error Sources 241   
4.14 Orbit Accuracy 244   
4.15 Smoothing . . 246   
4.15.1 Computational Algorithm for Smoother 250   
4.16 The Probability Ellipsoid 251   
4.16.1 Transformation of the Covariance Matrix between   
Coordinate Systems 257   
4.17 Combining Estimates 258   
4.18 References . 261   
4.19 Exercises 264

# 5 Square Root Solution Methods 285

5.1 Introduction 285   
5.2 Cholesky Decomposition 286   
5.2.1 The Cholesky Algorithm 287   
5.2.2 The Square Root Free Cholesky Algorithm 288   
5.3 Least Squares Solution via Orthogonal Transformation 290   
5.4 Givens Transformations . 291   
5.4.1 A Priori Information and Initialization 294   
5.4.2 Givens Computational Algorithm 298   
5.4.3 Square Root Free Givens Transformation . 301   
5.4.4 Square Root Free Givens Computational Algorithm . . . . 305   
5.4.5 A Simplified Square Root Free Givens Transformation . . 307   
5.4.6 Implementation Considerations . 309   
5.5 The Householder Transformation . 310   
5.5.1 Application to the Solution of the Least Squares Problem . 315   
5.5.2 Householder Computational Algorithm . 316   
5.6 Numerical Examples 318   
5.6.1 Cholesky Decomposition . 318   
5.6.2 Givens Transformation 320   
5.6.3 Householder Transformation 322   
5.6.4 A More Illustrative Example 324   
5.6.5 Cholesky Decomposition . 325   
5.6.6 Square Root Free Givens Transformation 326   
5.6.7 The Householder Transformation 329   
5.7 Square Root Filter Algorithms 330   
5.7.1 The Square Root Measurement Update Algorithms 332   
5.7.2 Square Root Free Measurement Update Algorithms 340   
5.8 Time Update of the Estimation Error Covariance Matrix . 343   
5.9 Continuous State Error Covariance Propagation 346   
5.9.1 Triangular Square Root Algorithm 349   
5.10 The Square Root Information Filter 351   
5.10.1 The Square Root Information Filter with Time-Dependent   
Effects . 353   
5.10.2 The Dynamic Case with Process Noise 358   
5.10.3 SRIF Computational Algorithm 363   
5.10.4 Smoothing with the SRIF 364   
5.11 Process Noise Parameter Filtering/Smoothing Using a SRIF 369   
5.11.1 Exponentially Correlated Process Noise SRIF 371   
5.11.2 Smoothing with a SRIF 377   
5.12 References . 380   
5.13 Exercises 381

# 6 Consider Covariance Analysis 387

6.1 Introduction . . 387   
6.2 Bias in Linear Estimation Problems 388   
6.3 Formulation of the Consider Covariance Matrix 389   
6.4 The Sensitivity and Perturbation Matrices . 397   
6.4.1 Example Application of a Sensitivity and Perturbation   
Matrix . . 398   
6.5 Inclusion of Time-Dependent Effects . 400   
6.6 Propagation of the Error Covariance 405   
6.7 Sequential Consider Covariance Analysis 407   
6.8 Example: Freely Falling Point Mass 410   
6.8.1 Propagation with Time 415   
6.8.2 The Sequential Consider Algorithm 416   
6.8.3 Perturbation in the State Estimate 419   
6.9 Example: Spring-Mass Problem 420   
6.10 Errors in the Observation Noise and A Priori State Covariances . . 425   
6.11 Errors in Process Noise, Observation Noise, and State Covariance 427   
6.12 Covariance Analysis and Orthogonal Transformations . . . 430   
6.13 References . . . 434   
6.14 Exercises 435

# A Probability and Statistics 439

A.1 Introduction . 439   
A.2 Axioms of Probability . 440   
A.3 Conditional Probability 443   
A.4 Probability Density and Distribution Functions 443   
A.5 Expected Values . . 445   
A.6 Examples and Discussion of Expectation . 446   
A.7 Moment Generating Functions 448   
A.8 Some Important Continuous Distributions 449   
A.8.1 Uniform or Rectangular Distribution . 449   
A.8.2 The Gaussian or Normal Distribution 450   
A.9 Two Random Variables 452   
A.10 Marginal Distributions 453   
A.11 Independence of Random Variables 454   
A.12 Conditional Probability 454   
A.13 Expected Values of Bivariate Functions 455   
A.14 The Variance-Covariance Matrix 456   
A.15 Properties of the Correlation Coefficient 458   
A.16 Properties of Covariance and Correlation 460   
A.17 Bivariate Normal Distribution 460   
A.18 Marginal Distributions . 461   
A.19 The Multivariate Normal Distribution . . . 462   
A.19.1 The Conditional Distribution for Multivariate Normal   
Variables 464   
A.20 The Central Limit Theorem 465   
A.21 Bayes Theorem 465   
A.22 Stochastic Processes 467   
A.22.1 Definitions for Stochastic Processes . 469   
A.23 References . 471

# B Review of Matrix Concepts 473

B.1 Introduction . 473   
B.2 Rank . . 475   
B.3 Quadratic Forms . 475   
B.4 Determinants 476   
B.5 Matrix Trace 477   
B.6 Eigenvalues and Eigenvectors . 478   
B.7 The Derivatives of Matrices and Vectors 478   
B.8 Maxima and Minima . 480   
B.9 Useful Matrix Inversion Theorems . 481   
B.10 Reference . 483

# C Equations of Motion 485

C.1 Lagrange Planetary Equations . 485   
C.2 Gaussian Form . 485   
C.3 References . . 486

# D Constants 487

D.1 Physical Constants . 487   
D.2 Earth Constants . 487   
D.3 Lunar, Solar, and Planetary Masses . . 488   
D.4 References . . 490

# E Analytical Theory for Near-Circular Orbits 493

E.1 Description . 493   
E.2 Example . . 497   
E.3 References . . 497

# F Example of State Noise and Dynamic Model Compensation 499

F.1 Introduction . . 499   
F.2 State Noise Compensation . 501   
F.3 Dynamic Model Compensation . 505   
F.4 Reference . 509

# G Solution of the Linearized Equations of Motion 511

G.1 Introduction . . 511   
G.2 The State Transition Matrix . . 513

# H Transformation between ECI and ECF Coordinates 517

H.1 Introduction . 517   
H.2 Matrix $P$ 518   
H.3 Matrix $N$ 519   
H.4 Matrix $S ^ { \prime }$ 519   
H.5 Matrix $W$ . 521   
H.6 References . 521

Bibliography Abbreviations 523

Bibliography 525

Author Index 537

Index 541

# Preface

The modern field of orbit determination (OD) originated with Kepler’s interpretations of the observations made by Tycho Brahe of the planetary motions. Based on the work of Kepler, Newton was able to establish the mathematical foundation of celestial mechanics. During the ensuing centuries, the efforts to improve the understanding of the motion of celestial bodies and artificial satellites in the modern era have been a major stimulus in areas of mathematics, astronomy, computational methodology and physics. Based on Newton’s foundations, early efforts to determine the orbit were focused on a deterministic approach in which a few observations, distributed across the sky during a single arc, were used to find the position and velocity vector of a celestial body at some epoch. This uniquely categorized the orbit. Such problems are deterministic in the sense that they use the same number of independent observations as there are unknowns.

With the advent of daily observing programs and the realization that the orbits evolve continuously, the foundation of modern precision orbit determination evolved from the attempts to use a large number of observations to determine the orbit. Such problems are over-determined in that they utilize far more observations than the number required by the deterministic approach. The development of the digital computer in the decade of the 1960s allowed numerical approaches to supplement the essentially analytical basis for describing the satellite motion and allowed a far more rigorous representation of the force models that affect the motion.

This book is based on four decades of classroom instruction and graduatelevel research. The material has been derived from and shared with numerous colleagues and students. In addition to the contributions of these individuals, the material has been influenced by the approaches used at the NASA Jet Propulsion Laboratory (JPL) to fulfill Earth and planetary navigation requirements and at the NASA Goddard Space Flight Center (GSFC) and the Department of Defense Naval Surface Weapons Center in applications of satellite tracking to problems in geodesy, geodynamics, and oceanography. Various implementations of the techniques described have been accomplished over the years to meet the requirements to determine the orbit of specific spacecraft.

This book is focused on developing data processing techniques for estimating the state of a non-linear dynamic system. The book contains six chapters and eight appendices, each covering a unique aspect of the OD problem. Although the concepts will be discussed primarily in the context of Earth-orbiting satellites or planetary transfers, the methods are applicable to any non-linear system and have been applied to such widely diverse problems as describing the state of economic systems, chemical processes, spacecraft attitude, and aircraft and missile guidance and navigation.

In Chapter 1, the inherent characteristics of the OD problem are introduced in the context of a very simple dynamic problem. The concepts of the dynamic system and its associated state are introduced. The fact that essentially all observations are non-linear functions of the state variables and the complexities associated with this are discussed. The classical or well-determined problem and the over-determined problem are described as examples of the approaches used in the following chapters.

Chapter 2 lays the background for the OD problem by introducing the relevant elements of orbital mechanics. The concept of perturbed two body motion and its role in the description of orbital motion is discussed. The fundamental forces acting on the satellite are described, especially within the context of an accurate description of the orbit. Finally, the definitions of the coordinate systems used to describe the motion and the time conventions used to index the observations and describe the satellite position are given.

Chapter 3 describes the various types of observations that are used to measure the satellites motion. This includes ground-based systems such as laser and radiometric, as well as space-based measurements from the Global Positioning System. Error sources and media corrections needed for these observation types also are described. In the problem of orbit determination, the observations described in this chapter will be the input to the estimation methodologies in the following chapters.

In Chapter 4, the orbit problem is formulated in state space notation and the non-linear orbit determination problem is reduced to an approximating linear state estimation problem by expanding the system dynamics about an a priori reference orbit. This concept allows application of an extensive array of mathematical tools from linear system theory that clarify the overall problem and aid in transferring the final algorithms to the computational environment. Chapter 4 also introduces the important concept of sequential processing of the observations, and the relation to the Kalman Filter, and relates the algorithm to the observation and control of real time processes.

Chapter 5 addresses issues related to the numerical accuracy and stability of the computational process, and formulates the square root computational algorithms. These algorithms are based on using a series of orthogonal transformations to operate on the information arrays in such a way that the requirement for formation of the normal equations is eliminated. The approach is used to develop both batch and sequential data processing algorithms.

Chapter 6 explores the very important problem of assessing the effect of error in unestimated measurement and force model parameters. The effects of incorrect statistical information on the a priori state and observation noise are examined and the overall process is known as consider covariance analysis.

The eight appendices provide background and supplemental information. This includes topics such as probability and statistics, matrix algebra, and coordinate transformations.

The material can be used in several ways to support graduate or senior level courses. Chapters 1, 3, and 4, along with Appendices A, B, F, and G provide the basis for a one-semester OD class. Chapters 5 and 6, along with Appendix A, provide the basis for a one-semester advanced OD class. Chapter 2 could serve as supplemental information for the first semester class as well as an introductory orbit mechanics class. Each chapter has a set of problems selected to emphasize the concepts described in the chapter.

# Acknowledgements

The authors gratefully acknowledge the assistance of Karen Burns and Melody Lambert for performing the word processing for the manuscript. We are especially indebted to Melody for her patience and expertise in dealing with countless additions and corrections. We thank the hundreds of students and colleagues who, over the past decade, contributed by providing suggestions and reviews of the manuscript. We are deeply grateful for your help and encouragement. We apologize for not mentioning you by name but our attempts to do so would surely result in our omission of some who made significant contributions.

Byron Tapley, Bob Schutz, and George Born April, 2004

# Web Sites

Relevant information can be found on the World Wide Web (www). However, the www does not provide a stable source of information comparable to a published document archived in a library. The following list of www sites was valid just prior to the publication date of this book, but some may no longer be functional. Use of readily available search engines on the www may be useful in locating replacement or new sites.

• Ancillary Information for Statistical Orbit Determination

Academic Press http://www.academicpress.com/companions/0126836302

Center for Space Research (CSR, University of Texas at Austin) http://www.csr.utexas.edu/publications/statod

Colorado Center for Astrodynamics Research (CCAR, University of Colorado at Boulder) http://www-ccar.colorado.edu/statod

Online Dissertation Services

UMI (also known as University Microfilms) http://www.umi.com/hp/Products/Dissertations.html • Satellite Two Line Elements (TLE)

NASA Goddard Space Flight Center http://oig1.gsfc.nasa.gov (registration required)

Dr. T. S. Kelso http://celestrak.com

Jonathan McDowell’s Home Page http://www.planet4589.org/space/ • Earth Orientation, Reference Frames, Time

International Earth Rotation and Reference Frames Service (IERS) http://www.iers.org

Observatoire de Paris Earth Orientation Center http://hpiers.obspm.fr/eop-pc/

IERS Conventions 2003 http://maia.usno.navy.mil/conv2003.html

National Earth Orientation Service (NEOS) http://maia.usno.navy.mil

International Celestial Reference Frame (ICRF) http://hpiers.obspm.fr/webiers/results/icrf/README.html

International Terrestrial Reference Frame (ITRF)http://lareg.ensg.ign.fr/ITRF/solutions.html

U. S. Naval Observatory Time Service http://tycho.usno.navy.mil/

• Space Geodesy Tracking Systems International GPS Service (IGS) http://igscb.jpl.nasa.gov International Laser Ranging Service (ILRS) http://ilrs.gsfc.nasa.gov International VLBI Service for Geodesy and Astrometry (IVS) http://ivscc.gsfc.nasa.gov International DORIS Service (IDS) http://ids.cls.fr/   
• Global Navigation Satellite Systems GPS http://gps.losangeles.af.mil/ GLONASS http://www.glonass-center.ru/ GALILEO http://www.europa.eu.int/comm/dgs/energy transport/galileo/

Web pages for particular satellite missions are maintained by the national space agencies.

# Chapter 1

# Orbit Determination Concepts

# 1.1 INTRODUCTION

The treatment presented here will cover the fundamentals of satellite orbit determination and its evolution over the past four decades. By satellite orbit determination we mean the process by which we obtain knowledge of the satellite’s motion relative to the center of mass of the Earth in a specified coordinate system. Orbit determination for celestial bodies has been a general concern of astronomers and mathematicians since the beginning of civilization and indeed has attracted some of the best analytical minds to develop the basis for much of the fundamental mathematics in use today.

The classical orbit determination problem is characterized by the assumption that the bodies move under the influence of a central (or point mass) force. In this treatise, we focus on the problem of determining the orbits of noncelestial satellites. That is, we focus on the orbits of objects placed into orbit by humans. These objects differ from most natural objects in that, due to their size, mass, and orbit charateristics, the nongravitational forces are of significant importance. Further, most satellites orbit near to the surface and for objects close to a central body, the gravitational forces depart from a central force in a significant way.

By the state of a dynamical system, we mean the set of parameters required to predict the future motion of the system. For the satellite orbit determination problem the minimal set of parameters will be the position and velocity vectors at some given epoch. In subsequent discussions, this minimal set will be expanded to include dynamic and measurement model parameters, which may be needed to improve the prediction accuracy. This general state vector at a time, $t$ , will be denoted as $\mathbf X ( t )$ t. The general orbit determination problem can then be posed as follows.

If at some initial time, $t _ { 0 }$ , the state $\mathbf { X } _ { 0 }$ of a vehicle following a ballistic trajecttory is given and if the differential equations that govern the motion of the vehicle are known, then the equations of motion can be integrated to determine the state of the vehicle at any time. However, during an actual flight, the initial state is never known exactly. Moreover, certain physical constants as well as the mathematical specification of the forces required to define the differential equations of motion are known only approximately. Such errors will cause the actual motion to deviate from the predicted motion. Consequently, in order to determine the position of the spacecraft at some time $t > t _ { 0 }$ , it must be tracked or observed from t > ttracking stations whose positions are known precisely. With the observations of the spacecraft motion, a better estimate of the trajectory can be determined. The term “better estimate” is used since the observations will be subject to both random and systematic errors and, consequently, the estimate of the trajectory will not be exact.

The observational data will usually consist of such measurements as range, range-rate, azimuth, elevation, or other observable quantities. That is, the state variables (position, velocity, unknown model parameters, etc.) will not be observed, but rather the observable will usually be some nonlinear function of the state variables.

The problem of determining the best estimate of the state of a spacecraft, whose initial state is unknown, from observations influenced by random and systematic errors, using a mathematical model that is not exact, is referred to as the problem of state estimation. In this presentation, such a procedure will be referred to as the process of orbit determination. The word “best” is used to imply that the estimate is optimal in some as yet undefined statistical sense.

When an estimate of the trajectory has been made, the subsequent motion and values for the observations can be predicted. In the orbit determination procedure, the process of predicting the state of a vehicle is referred to as “generating an ephemeris.” An ephemeris for a space vehicle is a table of its position and velocity components as a function of time. The predicted values will differ from the true values due to the following effects:

1. Inaccuracies in the estimated state vector (i.e., position and velocity vector) caused by errors in the orbit determination process, such as:

a. Approximations involved in the method of orbit improvement and in the mathematical model,   
b. Errors in the observations,   
c. Errors in the computational procedure used in the solution process.

2. Errors in the numerical integration procedure caused by errors in the dynamical model and computer truncation and roundoff errors.

![](images/b1132a7e23762a8db80a9a80b21240907329f03b06cadb2a8ce6a7f1967e7641.jpg)  
Figure 1.2.1: Uniform gravity field trajectory.

Consequently, the process of observation and estimation must be repeated continually as the vehicle’s motion evolves. Furthermore, the orbit determination procedure may be used to obtain better estimates of the location of tracking stations, adjust the station clocks, calibrate radar biases, obtain a better estimate of geophysical constants, and so on. In fact, any observable quantity directly affecting either the motion of the vehicle or the observation-state relationship can be determined by appropriately using the observational data.

To formulate the orbit determination problem, we will use elements of probability and statistics as well as matrix theory. Appendixes A and B contain introductory material on these topics.

# 1.2 UNIFORM GRAVITY FIELD MODEL

To illustrate some of the basic ideas involved in the orbit determination process, consider the flight of a vehicle moving under the influence of a uniform gravitational field, as shown in Fig. 1.2.1. In the preliminary design of the trajectory, an initial state $\mathbf { X } _ { 0 } ^ { * }$ (i.e., the initial position and the initial velocity vectors), is selected in such a way that the vehicle will follow a desired nominal (or design) trajectory. In practice, however, the design conditions are never realized. Hence, the true initial state, $\mathbf { X } _ { 0 }$ , will differ from the nominal initial state, $\mathbf { X } _ { 0 } ^ { * }$ , and consequently, the true trajectory followed by the vehicle will differ from the nominal trajectory. An indication of these two trajectories is given in Fig. 1.2.1. Here the true trajectory is denoted as $\mathbf { X }$ , the nominal trajectory as $\mathbf { X } ^ { * }$ , and the best estimate of the true trajectory is indicated by $\hat { \bf X }$ . To determine an estimate, $\hat { \bf X }$ , of the true trajectory of the vehicle, tracking information must be used.

Figure 1.2.1 shows a tracking station at a point whose coordinates are $( X _ { s } , Y _ { s } )$ Assume that the range (linear distance along the line of sight), $\rho$ X , Y, and the elevation, $\theta$ ρ, of the line of sight to the satellite can be measured. The tracking information, or θobservations, $\rho$ and $\theta$ , at any time depend on the true state of the satellite and the ρ θposition of the tracking station. Since the true position of the satellite is unknown, the calculated or modeled values of the observations will depend on the nominal position of the satellite and the location of the tracking station at the time the observation is made. The difference between observed and calculated observations at the observation time provides the information used to obtain an improved estimate of the satellite’s motion. Other observations such as range rate, $\dot { \rho }$ , and elevation rate, $\dot { \theta }$ ρ, which depend on both the velocity and position of the satellite θand tracking station, could also be used to determine $\hat { \mathbf X }$ . Note that range rate is the line of sight velocity that is, the projection of the spacecraft’s velocity vector on to the range vector

$$
{ \dot { \rho } } = { \frac { { \dot { \rho } } \cdot \rho } { \rho } } .
$$

# 1.2.1 FORMULATION OF THE PROBLEM

For the uniform gravity field model, the differential equations of motion can be expressed as

$$
\begin{array} { l c l } { \ddot { X } ( t ) } & { = } & { 0 } \\ { \ddot { Y } ( t ) } & { = } & { - g , } \end{array}
$$

where $g$ is the gravitational acceleration and is assumed to be constant. Integration gof Eq. (1.2.1) leads to

$$
\begin{array} { l c l } { { X ( t ) } } & { { = } } & { { X _ { 0 } + \dot { X } _ { 0 } t } } \\ { { Y ( t ) } } & { { = } } & { { Y _ { 0 } + \dot { Y } _ { 0 } t - g \frac { t ^ { 2 } } { 2 } , } } \\ { { \dot { X } ( t ) } } & { { = } } & { { \dot { X } _ { 0 } } } \\ { { \dot { Y } ( t ) } } & { { = } } & { { \dot { Y } _ { 0 } - g t } } \end{array}
$$

where $t$ represents the time, and the reference time, $t _ { 0 }$ , is chosen to be zero. The subscript 0 indicates values of the quantities at $t _ { 0 }$ . Now, providing the values of

$X _ { 0 } , Y _ { 0 } , \dot { X } _ { 0 } , \dot { Y } _ { 0 }$ , and $g$ are given, Eq. (1.2.2) can be used to predict the position X Y X Y gand velocity of the vehicle at any time. However, as previously indicated, the values of these quantities are never known exactly in practice, and it is the task of the orbit determination procedure to estimate their values.

# 1.2.2 THE EQUATION OF THE ORBIT

The parameter $t$ can be eliminated in the last two of Eq. (1.2.2) to obtain the tcurve followed by the vehicle in the $( X , Y )$ plane; that is,

$$
t = \frac { X - X _ { 0 } } { \dot { X } _ { 0 } } .
$$

Hence,

$$
{ \cal { Y } } ( t ) = { \cal { Y } } _ { 0 } + \frac { \dot { Y } _ { 0 } } { \dot { X } _ { 0 } } ( X - X _ { 0 } ) - { \frac { 1 } { 2 } } \frac { g } { \dot { X } _ { 0 } ^ { 2 } } ( X - X _ { 0 } ) ^ { 2 } .
$$

Equation (1.2.4) can be recognized readily as the equation of a parabola. This equation is analogous to the conic curve obtained as the solution to motion in an inverse square force field (see Chapter 2). It should be noted that Eqs. (1.2.3) and (1.2.4) still involve the values of the four initial conditions. The relation indicates that if the vehicle was at $X ^ { \prime }$ , then it must also have been at $Y ^ { \prime }$ obtained from Eq. X(1.2.4). It is also obvious that any real value of $X$ Yis possible, and it has associated with it a unique $Y$ X. However, the converse is not true. For each possible value of $Y$ Y, there are usually two values of $X$ possible. The time epoch, $t ^ { \prime }$ , corresponding Yto the point $( X ^ { \prime } , Y ^ { \prime } )$ Xcan be determined from the relation $t ^ { \prime } = ( X ^ { \prime } - \bar { X } _ { 0 } ) / \dot { X } _ { 0 }$ . X , Y t X X /XThis relation is analogous to Kepler’s equation for the motion in an inverse square force field. Since the epoch of time must be associated with the determination of the state of the vehicle if an ephemeris is to be generated and since the time is an integral part of all observations, the solution in the form of Eqs. (1.2.3) and (1.2.4) is usually not convenient for most orbit determination procedures.

In the subsequent discussions, either the differential equations, Eq. (1.2.1), or their solution in the form of Eq. (1.2.2) will be used.

# 1.2.3 THE ROLE OF THE OBSERVATION

As an example of the orbit determination procedure, consider the situation in which the state is observed at some time epoch, $t _ { j }$ . Then if $X _ { j } , Y _ { j } , \dot { X } _ { j }$ and $\dot { Y } _ { j }$ are given at $t _ { j }$ t X Y X, Eq. (1.2.2) can be used to form four equations in terms of Y tfour unknowns. This system of equations can be used to determine the unknown components of the initial state. For example, from Eq. (1.2.2) it follows that

$$
\begin{array} { r l r } { \left[ \begin{array} { l } { X _ { j } } \\ { Y _ { j } + g t _ { j } ^ { 2 } / 2 } \\ { \dot { X } _ { j } } \\ { \dot { Y } _ { j } + g t _ { j } } \end{array} \right] } & { = } & { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { t _ { j } } & { 0 } \\ { 0 } & { 1 } & { 0 } & { t _ { j } } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { l } { X _ { 0 } } \\ { Y _ { 0 } } \\ { \dot { X } _ { 0 } } \\ { \dot { Y } _ { 0 } } \end{array} \right] . } \end{array}
$$

Then, the initial state can be determined as follows:

$$
\begin{array} { r l r } { \left[ \begin{array} { l } { X _ { 0 } } \\ { Y _ { 0 } } \\ { \dot { X } _ { 0 } } \\ { \dot { Y } _ { 0 } } \end{array} \right] } & { { } = } & { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { t _ { j } } & { 0 } \\ { 0 } & { 1 } & { 0 } & { t _ { j } } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] ^ { - 1 } \left[ \begin{array} { l } { X _ { j } } \\ { Y _ { j } + g t _ { j } ^ { 2 } / 2 } \\ { \dot { X } _ { j } } \\ { \dot { Y } _ { j } + g t _ { j } } \end{array} \right] . } \end{array}
$$

Providing that the matrix inverse in Eq. (1.2.5) exists, the true initial state ${ \bf X } _ { 0 } ^ { T } = { }$ $[ X _ { 0 } , Y _ { 0 } , \overset { \cdot } { X } _ { 0 } , \overset { \cdot } { Y _ { 0 } } ]$ can be determined.

, Y , X , YUnfortunately, in an actual trajectory or orbit determination process, the individual components of the state generally cannot be observed directly. Rather, the observations consist of nonlinear functions of the state; for example, range, elevation, range rate, and so on. In this case, the nonlinear observation-state relationship is

$$
\begin{array} { r c l } { \rho } & { = } & { \sqrt { ( X - X _ { s } ) ^ { 2 } + ( Y - Y _ { s } ) ^ { 2 } } } \\ { \tan \theta } & { = } & { ( Y - Y _ { s } ) / ( X - X _ { s } ) } \\ { \dot { \rho } } & { = } & { \displaystyle \frac { 1 } { \rho } [ ( X - X _ { s } ) ( \dot { X } - \dot { X } _ { s } ) + ( Y - Y _ { s } ) ( \dot { Y } - \dot { Y } _ { s } ) ] } \\ { \dot { \theta } } & { = } & { \displaystyle \frac { 1 } { \rho ^ { 2 } } [ ( X - X _ { s } ) ( \dot { Y } - \dot { Y } _ { s } ) - ( \dot { X } - \dot { X } _ { s } ) ( Y - Y _ { s } ) ] , } \end{array}
$$

where $X _ { s } , Y _ { s } , \dot { X } _ { s }$ , and $\dot { Y } _ { s }$ are the position and velocity components, respectively, X Y X Yof the tracking station. Generally the station velocity components $\dot { X } _ { s }$ and $\dot { Y } _ { s }$ will X Ybe zero relative to an Earth-fixed frame unless we are accounting for tectonic plate motion. Now, if $\rho , \theta , \dot { \rho }$ and $\dot { \theta }$ are given at $t _ { j }$ , then Eq. (1.2.2) can be substituted ρ θ ρinto Eq. (1.2.6) to obtain

$$
\begin{array} { r c l } { \rho _ { j } } & { = } & { \sqrt { ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { j } ) ^ { 2 } + ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { j } - g t _ { j } ^ { 2 } / 2 ) ^ { 2 } } } \\ { \theta _ { j } } & { = } & { \tan ^ { - 1 } [ ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { j } - g \frac { t _ { j } ^ { 2 } } { 2 } ) / ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { j } ) ] } \\ { \dot { \rho } _ { j } } & { = } & { \cfrac { 1 } { \rho _ { j } } [ ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { j } ) ( \dot { X } _ { 0 } - \dot { X } _ { s } ) } \\ & & { + ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { j } - g \frac { t _ { j } ^ { 2 } } { 2 } ) ( \dot { Y } _ { 0 } - g t _ { j } - \dot { Y } _ { s } ) ] } \end{array}
$$

$$
\begin{array} { r c l } { { \dot { \theta } _ { j } } } & { { = } } & { { \displaystyle \frac { 1 } { \rho _ { j } ^ { 2 } } [ ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { j } ) ( \dot { Y } _ { 0 } - g t _ { j } - \dot { Y } _ { s } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - ( \dot { X } _ { 0 } - \dot { X } _ { s } ) ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { j } - g \frac { t _ { j } ^ { 2 } } { 2 } ) ] . } } \end{array}
$$

Symbolically Eq. (1.2.7) represents four nonlinear algebraic equations in terms of the unknown components of the initial state. If $\mathbf { Y } ^ { T }$ represents the vector whose components are the observations $[ \rho _ { j } , \theta _ { j } , \dot { \rho } _ { j } , \dot { \theta } _ { j } ]$ , then Eq. (1.2.7) can be expressed as

$$
J ( \mathbf { X } _ { 0 } ) \equiv \mathbf { Y } - G ( \mathbf { X } _ { 0 } , t ) = 0 ,
$$

where $G ( \mathbf { X } _ { 0 } , t )$ is a $4 \times 1$ vector of nonlinear functions consisting of the right-hand G , tside of Eq. (1.2.7). Eq. (1.2.8) can be solved iteratively by the Newton–Raphson iteration procedure. If $\mathbf { X } _ { 0 } ^ { n }$ represents the $n$ th approximation to the solution, then

$$
J ( \mathbf { X } _ { 0 } ^ { n + 1 } ) \cong J ( \mathbf { X } _ { 0 } ^ { n } ) + \left[ \frac { \partial J } { \partial \mathbf { X } _ { 0 } ^ { n } } \right] [ \mathbf { X } _ { 0 } ^ { n + 1 } - \mathbf { X } _ { 0 } ^ { n } ] ,
$$

according to a 2-term Taylor series approximation. Now, setting ${ \cal J } ( { \bf X } _ { 0 } ^ { n + 1 } ) = 0$ to comply with Eq. (1.2.8) and solving for $\mathbf { X } _ { 0 } ^ { n + 1 }$ leads to

$$
\mathbf { X } _ { 0 } ^ { n + 1 } = \mathbf { X } _ { 0 } ^ { n } - \left[ \frac { \partial J } { \partial \mathbf { X } _ { 0 } ^ { n } } \right] ^ { - 1 } J ( \mathbf { X } _ { 0 } ^ { n } ) ,
$$

where

$$
\frac { \partial J } { \partial \mathbf { X } _ { 0 } ^ { n } } = - \frac { \partial G ( \mathbf { X } _ { 0 } ^ { n } , t ) } { \partial \mathbf { X } _ { 0 } ^ { n } } .
$$

The process can be repeated until $| | \mathbf { X } _ { 0 } ^ { n + 1 } - \mathbf { X } _ { 0 } ^ { n } | | \leq \epsilon$ , where $\epsilon$ is a small positive number.

Several facts are obvious from this example:

1. The linear dependence of the state at time $t$ on the initial conditions, as tobtained in Eq. (1.2.2), usually does not occur.   
2. In general, the equations that define the solution to the orbit determination problem are nonlinear, and the solution must be obtained by a numerical iteration procedure. Note that this iteration procedure requires an initial guess for $\mathbf { X } _ { 0 }$ . This initial guess must be close enough to the true solution for convergence to occur.   
3. Since the equations are nonlinear, multiple solutions may exist; only one will correspond to the minimizing or correct solution. Generally the initial guess for $\mathbf { X } _ { 0 }$ will be close to the truth so convergence to an incorrect solution is not a problem.

This situation represents a special case of the usual orbit determination problem; that is, the case where there are as many independent observations at one epoch of time as there are unknown components of the state vector. Usually, the number of observations available at any time will be smaller than the number of components in the state vector. For example, the radar may have the capability of measuring only range, $\rho$ , and range rate, $\dot { \rho }$ , or range and elevation, $\theta$ , at any ρone point in time. The observation set $( \rho , \theta )$ ρ θis not adequate to determine the state $( \bar { X _ { 0 } , Y _ { 0 } , \dot { X } _ { 0 } , \dot { Y _ { 0 } } } )$ ρ, θ, since using Eq. (1.2.6) will lead to a set of two nonlinear equa-X , Y , X , Ytions in terms of four unknowns. However, if observations are available at any two time points $t _ { 1 }$ and $t _ { 2 }$ , then the set $( \rho _ { 1 } , \theta _ { 1 } , \rho _ { 2 } , \theta _ { 2 } )$ can be used to determine t t ρ , θ , ρ , θthe trajectory. From Eq. (1.2.7), the following equations can be obtained:

$$
\begin{array} { r c l } { \rho _ { 1 } } & { = } & { \sqrt { ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { 1 } ) ^ { 2 } + ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { 1 } - g t _ { 1 } ^ { 2 } / 2 ) ^ { 2 } } } \\ { \theta _ { 1 } } & { = } & { \tan ^ { - 1 } [ ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { 1 } - g t _ { 1 } ^ { 2 } / 2 ) / ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { 1 } ) ] } \\ { \rho _ { 2 } } & { = } & { \sqrt { ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { 2 } ) ^ { 2 } + ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { 2 } - g t _ { 2 } ^ { 2 } / 2 ) ^ { 2 } } } \\ { \theta _ { 2 } } & { = } & { \tan ^ { - 1 } [ ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { 2 } - g t _ { 2 } ^ { 2 } / 2 ) / ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { 2 } ) ] . } \end{array}
$$

Equation (1.2.10) represents four nonlinear equations in terms of four unknowns from which the unknowns can be determined as indicated by Eq. (1.2.9).

The approaches just outlined have two fundamental assumptions that cannot be realized in practice. These assumptions are:

1. Perfect knowledge of the differential equations that describe the motion.

2. Perfect observations.

The assumption of perfect knowledge of the differential equations implies that all the forces are modeled perfectly and that the values for the constant parameters used in the force model are exact. Usually, the true values for all of the parameters are not defined with complete numerical accuracy. But what is even more relevant, simplifying assumptions usually are made to reduce the computational requirements. Under such assumptions, certain unimportant or “negligible” components of the forces acting on the vehicle are omitted. As a consequence, the mathematical model used to describe the dynamical process will differ from the true process.

In general, the observations will be corrupted by random and systematic observation errors that are inherent in the measurement process. Hence, the observed value of the range, $\rho$ , or elevation, $\theta$ , will differ from the true value because of ρ θthese errors. In addition, the true and observed values for the range and the elevation will differ because of imperfect knowledge of the tracking station location, $( X _ { s } , Y _ { s } )$ .

Because of these factors, four observations will not be sufficient to determine the planar motion trajectory exactly. In the usual operational situation, many observations are made, and the trajectory is selected to give the best agreement with the observations obtained. In general the mechanism for obtaining the best estimate is to linearize the problem by expanding the equations of motion and the observation-state relationship about a reference trajectory. Deviations from the reference trajectory (e.g., position and velocity) are then determined to yield the “best” agreement with the observations. As we will see, the “best” agreement generally is based on the least squares criterion.

# 1.2.4 LINEARIZATION PROCEDURE

To illustrate the linearization procedure, return to the flat Earth example discussed previously. Assuming that there are errors in each of the initial position and velocity values and in $g$ , the state vector is $X ^ { T } = [ X , Y , \dot { X } , \dot { Y } , g ]$ . It is a gstraightforward procedure to replace $X$ by $X ^ { * } + \delta X$ , $Y$ X,by $Y ^ { * } + \delta Y , \ldots$ and $g$ by $g ^ { * } + \delta g$ in Eq. (1.2.2) to obtain the equation for perturbation, or deviation, from the reference trajectory. The $( ) ^ { * }$ values represent assumed or specified values. If the equations for the reference trajectory, designated by the $( ) ^ { * }$ values, are subtracted from the result obtained by this substitution, the equations for the state deviations are obtained as

$$
\begin{array} { l c l } { \delta X } & { = } & { \delta X _ { 0 } + \delta \dot { X } _ { 0 } t } \\ { \delta Y } & { = } & { \delta Y _ { 0 } + \delta \dot { Y } _ { 0 } t - \delta g \frac { t ^ { 2 } } { 2 } } \\ { \delta \dot { X } } & { = } & { \delta \dot { X } _ { 0 } } \\ { \delta \dot { Y } } & { = } & { \delta \dot { Y } _ { 0 } - \delta g t } \\ { \delta g } & { = } & { \delta g . } \end{array}
$$

Equation (1.2.11) can be expressed in matrix form in the following manner:

$$
\begin{array} { r l r } { \left[ \begin{array} { c } { \delta X } \\ { \delta Y } \\ { \delta \dot { X } } \\ { \delta \dot { Y } } \\ { \delta g } \end{array} \right] } & { = } & { \left[ \begin{array} { c c c c c } { 1 } & { 0 } & { t } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { t } & { - t ^ { 2 } / 2 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { - t } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c } { \delta X _ { 0 } } \\ { \delta Y _ { 0 } } \\ { \delta \dot { X } _ { 0 } } \\ { \delta \dot { Y } _ { 0 } } \\ { \delta g } \end{array} \right] . } \end{array}
$$

Equation (1.2.12) can be used to predict the deviation of the vehicle from the reference trajectory, $\mathbf { X } ^ { * } ( t )$ , at any time $t > 0$ . Note that the deviations from the true state, $\delta \mathbf { X } ( t ) \equiv \mathbf { x } ( t )$ t t >, will be caused by deviations in the original state or deviations δ t tin the gravitational acceleration, $\delta g$ . However, the quantities $\delta X _ { 0 } , \delta Y _ { 0 } , \ldots$ are δg δX , δY , . . . ,not known, and it is the problem of the orbit determination procedure to estimate their values.

In this example, both Eqs. (1.2.2) and (1.2.12) are linear. In the case of central force field motion, the equations analogous to Eq. (1.2.2) are not linear, however, and the orbit determination process is simplified considerably by the linearization procedure. Care must be taken so that deviations from the reference conditions remain in the linear range.

As mentioned earlier, the observations $\rho$ and $\theta$ , which are taken as the satellite ρ θfollows the true trajectory, are nonlinear functions of $X$ , $Y$ , $X _ { s }$ , and $Y _ { s }$ . Further-X Y Xmore, they contain random and systematic errors represented by $\epsilon _ { \rho }$ Yand $\epsilon _ { \theta }$ ; hence,

$$
\begin{array} { r c l } { \rho } & { = } & { \sqrt { ( X - X _ { s } ) ^ { 2 } + ( Y - Y _ { s } ) ^ { 2 } } + \epsilon _ { \rho } } \\ { \theta } & { = } & { \tan ^ { - 1 } \left( \frac { Y - Y _ { s } } { X - X _ { s } } \right) + \epsilon _ { \theta } . } \end{array}
$$

Our objective is to linearize the observations with respect to the reference trajectory. This can be accomplished by expanding Eq. (1.2.13) in a Taylor series about the reference or nominal trajectory as follows:

$$
\begin{array} { r l r } { \rho } & { \cong } & { \rho ^ { * } \quad + \left[ \frac { \partial \rho } { \partial X } \right] ^ { * } \left( X - X ^ { * } \right) + \left[ \frac { \partial \rho } { \partial Y } \right] ^ { * } \left( Y - Y ^ { * } \right) + \epsilon _ { \rho } } \\ { \theta } & { \cong } & { \theta ^ { * } \quad + \left[ \frac { \partial \theta } { \partial X } \right] ^ { * } \left( X - X ^ { * } \right) + \left[ \frac { \partial \theta } { \partial Y } \right] ^ { * } \left( Y - Y ^ { * } \right) + \epsilon _ { \theta } . } \end{array}
$$

Note that the partials with respect to $\dot { X } , \dot { Y }$ , and $g$ are zero since they do not appear Xexplicitly in Eq. (1.2.13). By defining

$$
\begin{array} { r c l } { { \delta \rho } } & { { = } } & { { \rho - \rho ^ { * } } } \\ { { \delta \theta } } & { { = } } & { { \theta - \theta ^ { * } } } \\ { { \delta X } } & { { = } } & { { X - X ^ { * } } } \\ { { \delta Y } } & { { = } } & { { Y - Y ^ { * } , } } \end{array}
$$

we can write Eq. (1.2.14) as

$$
\begin{array} { r l r } { \delta \rho } & { = } & { \left[ \frac { \partial \rho } { \partial X } \right] ^ { * } \delta X + \left[ \frac { \partial \rho } { \partial Y } \right] ^ { * } \delta Y + \epsilon _ { \rho } } \\ { \delta \theta } & { = } & { \left[ \frac { \partial \theta } { \partial X } \right] ^ { * } \delta X + \left[ \frac { \partial \theta } { \partial Y } \right] ^ { * } \delta Y + \epsilon _ { \theta } . } \end{array}
$$

The symbol $[ ] ^ { * }$ indicates that the value in brackets is evaluated along the nominal trajectory. In Eq. (1.2.16), terms of order higher than the first in the state deviation values have been neglected assuming that these deviations are small. This requires that the reference trajectory and the true trajectory be close at all times in the interval of interest. Now, if the following definitions are used,

$$
\begin{array} { l c l } { { { \bf y } ^ { T } } } & { { \equiv } } & { { \left[ \delta \rho \delta \theta \right] } } \\ { { } } & { { } } & { { } } \\ { { { \widetilde { H } } } } & { { { \equiv } } } &  { { \left[ \begin{array} { c } { { { \left[ \frac { \partial \rho } { \partial X } \right] } ^ { * } } } \\ { { \left[ \frac { \partial \theta } { \partial X } \right] } ^ { * } } \end{array} \begin{array} { c c c c } { { \left[ \frac { \partial \rho } { \partial Y } \right] } ^ { * } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { \left[ \frac { \partial \theta } { \partial Y } \right] } ^ { * } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right] } } \\ { { { \bf x } ^ { T } } } & { { \equiv } } & { { \left[ \delta X \delta Y \delta { \dot { X } } \delta { \dot { Y } } \delta { g } \right] } } \\ { { } } & { { } } & { { } } \\ { { \epsilon ^ { T } } } & { { \equiv } } & { { \left[ \epsilon _ { \rho } \epsilon _ { \theta } \right] , } } \end{array}
$$

then Eq. (1.2.16) can be expressed as the matrix equation,

$$
\begin{array} { r } { \mathbf { y } = \widetilde { H } \mathbf { x } + \boldsymbol { \epsilon } . } \end{array}
$$

In Eq. (1.2.18), y is called the observation deviation vector, $\mathbf { x }$ is the state deviation vector, $\bar { H }$ is a mapping matrix that relates the observation deviation vector Hto the state deviation vector, and $\epsilon$ is a random vector that represents the noise or error in the observations. It is common practice to refer to $\mathbf { x }$ and $\mathbf { y }$ as the state and observation vectors, respectively, even though they really represent deviations from nominal values.

# 1.2.5 STATE TRANSITION MATRIX

The matrix multiplying the initial state vector in Eq. (1.2.12) is referred to as the state transition matrix, $\Phi ( t , t _ { 0 } )$ . For the state deviation vector, $\mathbf { x }$ , defined in Eq. (1.2.17), this matrix is given by

$$
\begin{array} { r l r } { \Phi ( t , t _ { 0 } ) } & { = } & { \left[ \begin{array} { c c c c c } { 1 } & { 0 } & { t } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { t } & { - t ^ { 2 } / 2 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { - t } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] . } \end{array}
$$

The state transition matrix maps deviations in the state vector from one time to another. In this case, deviations in the state are mapped from $t _ { 0 }$ to $t$ . Note that we have arbitrarily set $t _ { 0 } = 0$ t t. For this linear example, the mapping is exact, but tin the general orbit determination case, the state equations will be nonlinear, and the state transition matrix is the linear term in a Taylor series expansion of the state vector at time $t$ about the state vector at a reference time $t _ { 0 }$ . Hence, the state t tdeviation vector and observation deviation vector at any time can be written in

terms of $\mathbf { x } _ { \mathrm { 0 } }$ , as follows:

$$
\begin{array} { r } { \mathbf { x } ( t ) = \Phi ( t , t _ { 0 } ) \mathbf { x } _ { 0 } } \\ { \mathbf { y } ( t ) = \widetilde { H } ( t ) \mathbf { x } ( t ) + \pmb { \epsilon } ( t ) . } \end{array}
$$

$\mathbf { y } ( t )$ can be written in terms of $\mathbf { x } _ { \mathrm { 0 } }$ as

$$
\mathbf { y } ( t ) = H ( t ) \mathbf { x } _ { 0 } + \epsilon ( t ) ,
$$

where

$$
H ( t ) = \widetilde { H } ( t ) \Phi ( t , t _ { 0 } ) .
$$

The problem that remains now is to determine the best estimate of $\mathbf { x } _ { \mathrm { 0 } }$ given the linearized system represented by Eqs. (1.2.20) and (1.2.21). Our problem can now be summarized as follows. Given an arbitrary epoch, $t _ { k }$ , and the state propagation equation and observation-state relationship

$$
\begin{array} { r } { { \mathbf { x } } ( t ) = \Phi ( t , t _ { k } ) { \mathbf { x } } _ { k } } \\ { { \mathbf { y } } = H { \mathbf { x } } _ { k } + \epsilon , } \end{array}
$$

find the “best” estimate of $\mathbf { x } _ { k }$ . In Eq. (1.2.23), y is an $m \times 1$ vector, $\mathbf { x }$ is an $n \times 1$ vector, $\epsilon$ is an $m \times 1$ vector, and $H$ is an $m \times n$ m nmapping matrix, where $n$ is mthe number of state variables and $m$ m nis the total number of observations. If $m$ is msufficiently large, the essential condition $m \geq n$ is satisfied.

m nIn contrast to the algebraic solutions described earlier in this chapter, the system represented by the second of Eq. (1.2.23) is always underdetermined. That is, there are $m$ -knowns (e.g., the observation deviations, y) and $m + n$ unknowns (e.g., the $m$ -observation errors, $\epsilon$ , and the $n$ -unknown components of the state mdeviation vector, $\mathbf { x } _ { k }$ n). In Chapter 4, several approaches for resolving this problem are discussed. The most straightforward is based on the method of least squares as proposed by Gauss (1809). In this approach, the best estimate for the unknown state vector, $\mathbf { x } _ { k }$ , is selected as the value $\hat { \mathbf { x } } _ { k }$ , which minimizes the sum of the squares of the calculated values of the observations errors. That is, if $\mathbf { x } _ { k } ^ { 0 }$ is any value of $\mathbf { x } _ { k }$ , then $\boldsymbol { \epsilon } ^ { 0 } = \mathbf { y } - H \mathbf { x } _ { k } ^ { 0 }$ will be the $m$ -calculated values of the observa-Htion residuals corresponding to the value $\mathbf { x } _ { k } ^ { 0 }$ m. Then, the best estimate of $\mathbf { x } _ { k }$ will be the value that leads to a minimal value of the performance index, $J ( \mathbf { x } _ { k } ^ { 0 } )$ , where

$$
J ( \mathbf { x } _ { k } ^ { 0 } ) = 1 / 2 ( \epsilon ^ { 0 T } \epsilon ^ { 0 } ) = 1 / 2 ( \mathbf { y } - H \mathbf { x } _ { k } ^ { 0 } ) ^ { T } ( \mathbf { y } - H \mathbf { x } _ { k } ^ { 0 } ) .
$$

For a minimum of this quantity, it is necessary and sufficient that

$$
 \frac { \partial J } { \partial \mathbf { x } _ { k } ^ { 0 } } | _ { \hat { \mathbf { x } } _ { k } } = 0 ; ~ \delta \mathbf { x } _ { k } ^ { 0 ^ { T } } \frac { \partial ^ { 2 } J } { \partial \mathbf { x } _ { k } ^ { 0 } \partial \mathbf { x } _ { k } ^ { 0 } } | _ { \hat { \mathbf { x } } _ { x } } \delta \mathbf { x } _ { k } ^ { 0 } > 0 .
$$

From the first of the conditions given by Eq. (1.2.25), it follows that

$$
( \mathbf { y } - H \hat { \mathbf { x } } _ { k } ) ^ { T } H = 0
$$

or by rearranging that

$$
H ^ { T } H \hat { \mathbf { x } } _ { k } = H ^ { T } \mathbf { y } .
$$

If the $n \times n$ matrix $( H ^ { T } H )$ has an inverse, the solution can be expressed as

$$
\begin{array} { r } { \hat { \mathbf x } _ { k } = ( H ^ { T } H ) ^ { - 1 } H ^ { T } \mathbf y . } \end{array}
$$

Chapter 4 expands and clarifies the procedure and techniques for determining, and assessing the accuracy of, the estimate $\hat { \mathbf { x } } _ { k }$ . Further details are given on computational methods for determining $\hat { \mathbf { x } } _ { k }$ in Chapter 5.

# 1.3 BACKGROUND AND OVERVIEW

As noted in this introductory chapter, orbit determination methodology can be separated into two general classes, for example, classical (or deterministic) orbit determination and modern (or statistical based) orbit determination. In the classical approach, observational errors are not considered and the problem is reduced to making the necessary number of measurements to determine the orbit. There is an equivalence between the number of observations and the number of unknowns. The modern orbit determination problem recognizes the influence of observation errors and, to minimize the effects of the observational error, more observations are used than the number of parameters to be estimated. Modern orbit determination methodology dates back to the beginning of the 19th century, when Legendre (1806), in attempting to determine the orbits of the planets, recognized the importance of observational errors and proposed the least squares solution as a method for minimizing the effect of such errors. Gauss (1809) presented a probabilistic basis for the method of least squares, which was closely akin to the maximum likelihood method proposed by Fisher (1912). Gauss (1809) stated that he had used the method since 1795 and historians (Cajori, 1919) generally agree that Gauss originated the method. The notation of Gauss is still in use. Laplace (1812) added refinements to the computational approach and to the statistical foundations. Markov (1898), in his work on the mathematical foundations of probability theory, clarified many of the concepts associated with the method of least squares. Helmert (1900) extended the application to astronomy and geodesy. In the 20th century, Kolmogorov (1941) and Wiener (1949) linked the problem to modern systems theory and set the stage for the sequential filter formulation for processing tracking data. In 1959, Swerling gave the first conceptual approach to the sequential orbit determination problem. Kalman (1960) presented a mathematically rigorous approach for the sequential processing of observations of a linear dynamic system. In a later work, Kalman and Bucy (1961)

gave an approach for the extended Kalman filter, which is the sequential approach for the general nonlinear orbit determination problem. Following the publication of Kalman’s paper in 1960, there was an extensive series of publications related to this topic during the next three decades. Many of these investigations will be referenced in the subsequent chapters. A summary of the historical development of the least squares approach is given by Sorenson (1970).

The main thrust of this book will be aimed at developing computational data processing techniques for estimating the state of orbiting satellites. As noted in the previous discussion, the problem formulation will lead to a nonlinear relation between the observations and the epoch state of the satellite. Therefore, in modern system theory terms, we will be concerned with estimating the state of a nonlinear dynamic system, using observations of nonlinear functions of the system state, where the observations are corrupted by random and systematic observational errors. Although the main focus for the physical models will be the orbit determination problem, the problem will be cast in the state space notation defined by modern system theory. As such, the computational approaches presented in the treatment will be applicable to a wide range of problems, including missile guidance, attitude control, economic system analysis, chemical process control, and a wide variety of manufacturing processes. Once the defining equations from these processes have been reduced to the state space formulation, the computational techniques developed here will be applicable.

# 1.4 SUMMARY

Following the introduction of the basic concepts of nonlinear parameter estimation in Chapter 1, Chapter 2 provides a detailed discussion of the characteristics of the orbit for Earth-orbiting satellites. This is the primary dynamical system of interest in this treatment. Chapter 3 describes the various observations used in the Earth-orbiting satellite orbit determination problem. Chapter 4 describes the properties of the Weighted Least Squares and Minimum Variance Estimation algorithms as they are expressed in a batch estimation form and describes the transformation to the sequential estimation algorithm. The relation to the Kalman filter is noted. In Chapter 5, the computation algorithms for solving the linear system based on both the Cholesky Decomposition and the Orthogonal Transformation approach are presented. In addition, square root sequential estimation algorithms are given. Chapter 6 describes the error analysis approaches that evolve from the Consider covariance analysis. The algorithms developed here account for the effects of uncertainties on unestimated parameters that appear in either the dynamic or measurement equations.

As noted previously, a primary emphasis of this treatment will be devoted to developing computationally robust and efficient algorithms for processing the

observations of Earth-orbiting satellites.

# 1.5 REFERENCES

Cajori, F., A History of Mathematics, MacMillan Co., New York, 1919.

Fisher, R. A., “On an absolute criteria for fitting frequency curves,” Mess. Math., Vol. 41, pp. 155–160, 1912.

Gauss, K. F., Theoria Motus Corporum Coelestium, 1809 (Translated into English: Davis, C. H., Theory of the Motion of the Heavenly Bodies Moving about the Sun in Conic Sections, Dover, New York, 1963).

Helmert, F. R., “Zur Bestimmung kleiner Flachenst ¨ ucke des Geoids aus Lothab- ¨ weichungen mit Rucksicht auf Lothkr ¨ ummung”, Sitzungsberichte Preuss. ¨ Akad. Wiss., Berlin, Germany, 1900.

Kalman, R. E., “A New Approach to Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 82, Series E, No. 1, pp. 35–45, March 1960.

Kalman, R. E. and R. S. Bucy, “New Results in Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 83, Series D, No. 1, pp. 95–108, March 1961.

Kolmogorov, A. N., “Interpolation and Extrapolation of Stationary Random Sequences,” Bulletin of the Academy of Sciences of the USSR Math. Series, Vol. 5, pp. 3–14, 1941.

Laplace, P. S., Theorie Analytique de Probabilit ´ es´ , Paris, 1812 (The 1814 edition included an introduction, Essai Philosophique sur les Probabilites´ , which has been translated into English: Dale, A. I., Philosophical Essay on Probabilities, Springer-Verlag, New York, 1995).

Legendre, A. M., Nouvelles methodes pour la d ´ etermination des orbites des ´ cometes \` , Paris, 1806.

Markov, A. A., “The law of large numbers and the method of Least Squares,” (1898), Izbr. Trudi., Izd. Akod. Nauk, USSR, pp. 233–251, 1951.

Sorenson, H. W., “Least squares estimation: from Gauss to Kalman,” IEEE Spectrum, Vol. 7, No. 7, pp. 63–68, July 1970.

Swerling, P., “First order error propagation in a stagewise differential smoothing procedure for satellite observations,” J. Astronaut. Sci., Vol. 6, pp. 46–52, 1959.

Wiener, N., The Extrapolation, Interpolation and Smoothing of Stationary Time Series, John Wiley & Sons, Inc., New York, 1949.

# 1.6 EXERCISES

1. Write a computer program that computes $\rho ( t _ { i } )$ for a uniform gravity field ρ tusing Eq. (1.2.10). A set of initial conditions, $X _ { 0 }$ , $\dot { X } _ { 0 }$ , $Y _ { 0 }$ , $\dot { Y } _ { 0 }$ , $g$ , $X _ { s }$ , $Y _ { s }$ , and observations, $\rho$ X X Y Y g X, follow. With the exception of the station coordi-Y ρnates, the initial conditions have been perturbed so that they will not produce exactly the observations given. Use the Newton iteration scheme of Eq. (1.2.9) to recover the exact initial conditions for these quantities; that is, the values used to generate the observations. Assume that $X _ { s }$ and $Y _ { s }$ are known exactly. Hence, they are not solved for.

# Unitless Initial Conditions

$$
\begin{array} { c } { { X _ { 0 } = 1 . 5 } } \\ { { Y _ { 0 } = 1 0 . 0 } } \\ { { \dot { X } _ { 0 } = 2 . 2 } } \\ { { \dot { Y } _ { 0 } = 0 . 5 } } \\ { { g = 0 . 3 } } \\ { { X _ { s } = Y _ { s } = 1 . 0 } } \end{array}
$$

Answer

$$
\begin{array} { r } { X _ { 0 } = 1 . 0 } \\ { Y _ { 0 } = 8 . 0 } \\ { \dot { X } _ { 0 } = 2 . 0 } \\ { \dot { Y } _ { 0 } = 1 . 0 } \\ { g = 0 . 5 } \end{array}
$$

2. In addition to the five state variables of Exercise 1, could $X _ { s }$ and $Y _ { s }$ be solved for given seven independent observations of $\rho$ X Y? Why or why not? Hint: Notice the relationship between $X _ { 0 }$ and $X _ { s }$ ρand between $Y _ { 0 }$ and $Y _ { s }$ in Eq. (1.2.7) for $\rho _ { j }$ X X. See also Section 4.12 on observability.

# The Orbit Problem

# 2.1 HISTORICAL BACKGROUND

Johannes Kepler, based on a study of planetary position data acquired by Tycho Brahe, formulated three laws of planetary motion (Plummer, 1918):

1. The orbit of each planet is an ellipse with the Sun at one focus;   
2. The heliocentric radius vector of each planet sweeps over equal area in equal time;   
3. The square of the orbital period is proportional to the cube of the ellipse semimajor axis.

But it was Isaac Newton who established the mathematical foundation from which Kepler’s Laws can be derived. Newton’s insightful analysis of the work of Kepler led to the formulation of the basic concepts of mechanics and gravitation at an early stage in his career. Not until he was in his forties, however, did Newton publish these concepts in the Principia (1687), as described in the extensive biography by Westfall (1980) .

The Principia presented the Three Laws of Motion, quoted from p. 13 of Motte’s 1729 English translation of Newton’s Latin publication (with modern terminology in brackets):

Law I: Every body continues in its state of rest, or of uniform motion in a right line [straight line] unless it is compelled to change that state by forces impressed upon it.

Law II: The change of motion is proportional to the motive force impressed; and is made in the direction of the right line in which that force is impressed. $\mathbf { \dot { F } } = m \mathbf { a }$ , where $\mathbf { F }$ is force, $m$ is mass, and a is acceleration, which is equal to the time derivative of velocity, V.]

Law III: To every action there is always opposed an equal reaction: or, the mutual actions of two bodies upon each other are always equal, and directed to contrary parts.

Newton deduced the Law of Gravitation as well, which states: the mutual force of gravitational attraction between two point masses is

$$
F = { \frac { G M _ { 1 } M _ { 2 } } { d ^ { 2 } } }
$$

where $G$ is the Universal Constant of Gravitation and $d$ is the distance between the two point masses or particles, $M _ { 1 }$ and $M _ { 2 }$ .

The Laws of Newton contain some important concepts. The concept of a point mass is embodied in these laws, which presumes that the body has no physical dimensions and all its mass is concentrated at a point. The concept of an inertial reference frame is crucial to Newton’s Second Law; that is, the existence of a coordinate system that has zero acceleration. The concept of force $( \mathbf { F } )$ i s introduced as the cause of the acceleration experienced by a point mass, and the mass $( m )$ is the constant of proportionality implied by Newton’s statement of the Second Law. Finally, the concept of a uniformly changing time is fundamental to Newton’s Laws of Motion.

These laws are the foundation of the mathematical description of orbital dynamics. To this day, the laws enable a remarkably accurate description of the motion of both natural and arti cial bodies. The work of Albert Einstein [1905] provided even greater insight into this description and allowed the explanation of small discrepancies between observation and Newtonian dynamics.

The description of orbital dynamics in this book is Newtonian in nature. Inclusion of relativistic corrections is important for those applications that require high accuracy, and the relevant terms are described in this chapter.

Subtle differences in terminology exist in the literature concerning the distinction between reference frames and reference systems, for example. A careful and precise set of de nitions is discussed by Kovalevsky et al. (1989). For purposes of this book, the terminology reference frame will be used within a context that describes some speci c characteristic (e.g., inertial reference frame). The terminology coordinate system generally will apply to a set of axes that is used to describe the motion of a body. In some instances, reference frame and coordinate system are used interchangeably where there is no ambiguity.

In the following sections, the description of satellite motion is developed, beginning with the two-body gravitational model of satellite motion. The fundamental description from the problem of two bodies serves as a useful reference, but it is inadequate for the accurate representation of the actual satellite motion. The more complete and realistic representation will be developed from the twobody case. It is not the intent of the development in this chapter to provide an exhaustive treatise on orbital mechanics, since excellent books already exist (e.g., Szebehely and Mark, 1998; Vallado, 2001; Bond and Allman, 1996; Chobotov, 1996; Prussing and Conway, 1993; Danby, 1988; Roy, 1988; Battin, 1999; and Schaub and Junkins, 2003). The philosophy in this chapter is to provide the key steps in the development and its interpretation, especially within the context of the main purpose related to the determination of the orbit. With this philosophy, many details are left to you, although the preceding list of references provides most of the details.

![](images/cdc4393127e0b1aba02629735a963310af074bcf713b3cfae45c7d1ef98c313d.jpg)  
Figure 2.2.1: The problem of two bodies: $M _ { 1 }$ and $M _ { 2 }$ are spheres of constant, uniform density. The position vectors of the spheres refer to their respective geometrical center, which also coincide with the center of mass of the sphere.

# 2.2 PROBLEM OF TWO BODIES: GENERALPROPERTIES

The classic problem of two bodies was solved by Newton, which is repeated in a modern form by all treatises on celestial mechanics. The classic treatment describes the motion of two point masses. However, human experience demonstrates that the Earth has physical dimensions, and a point mass Earth is a serious stretch of the imagination. Nevertheless, a spherical body with constant, uniform mass distribution can be shown to be gravitationally equivalent to a point mass. Thus, as a more realistic approximation to the physical characteristics of a planet, a spherical body will be used in the following development.

Consider the motion of two spheres of mass $M _ { 1 }$ and $M _ { 2 }$ , as illustrated in Fig. 2.2.1. No restrictions are placed on the magnitude of these masses, so for illustrative purposes, assume $M _ { 1 }$ represents the Earth and $M _ { 2 }$ represents a satellite, including the Moon. The coordinate system $( X , \ Y , \ Z )$ is inertial and nonrotating; that is, it has no acceleration, and there is no preferred orientation of the axes at this stage. The position vectors of the geometrical centers of the respective spheres are ${ \bf R } _ { 1 }$ and ${ \bf R } _ { 2 }$ . The position of $M _ { 2 }$ with respect to $M _ { 1 }$ is described by $\mathbf { r }$ . The equations of motion derived from Newton’s Laws of Motion and Law of Gravitation are

$$
\begin{array} { l c l } { { { \cal M } _ { 1 } { \ddot { \bf R } } _ { 1 } } } & { { = } } & { { \displaystyle \frac { G M _ { 1 } M _ { 2 } { \bf r } } { r ^ { 3 } } } } \\ { { { \cal M } _ { 2 } { \ddot { \bf R } } _ { 2 } } } & { { = } } & { { \displaystyle - \frac { G M _ { 1 } M _ { 2 } { \bf r } } { r ^ { 3 } } } } \end{array}
$$

where $\ddot { \bf R } _ { 1 } = d ^ { 2 } { \bf R } _ { 1 } / d t ^ { 2 }$ and $t$ represents time. It can readily be shown that the equations of relative motion are

$$
{ \ddot { \mathbf { r } } } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } }
$$

where $\mu = G ( M _ { 1 } + M _ { 2 } )$ . In the case of an arti ci al satellite of the Earth, let $M _ { 1 }$ represent the Earth and $M _ { 2 }$ the satellite. Since the Earth is so massive, even a large satellite like a fully loaded space station results in

$$
\mu = G ( M _ { 1 } + M _ { 2 } ) \cong G M _ { 1 }
$$

to very high accuracy (better than one part in $1 0 ^ { 1 5 }$ ).

The general characteristics of the motion follow from manipulation of Eqs. (2.2.1) and (2.2.2):

1. Motion of Two-Body Center of Mass. The de nition of the position of the center of mass of the two spheres, $\mathbf { R } _ { \mathrm { c m } }$ , is

$$
{ \bf R } _ { \mathrm { c m } } = \frac { M _ { 1 } { \bf R } _ { 1 } + M _ { 2 } { \bf R } _ { 2 } } { \left( M _ { 1 } + M _ { 2 } \right) } .
$$

By adding Eqs. (2.2.1) and (2.2.2) it follows that

$$
\ddot { \mathbf { R } } _ { \mathrm { c m } } = 0 \quad \mathrm { a n d } \quad \mathbf { R } _ { \mathrm { c m } } = \mathbf { C } _ { 1 } ( t - t _ { o } ) + \mathbf { C } _ { 2 }
$$

where $\mathbf { C } _ { 1 }$ and $\mathbf { C } _ { 2 }$ are constants of the motion. Equation (2.2.5) states that the center of mass of the two spheres moves in a straight line with constant velocity. Note that the straight line motion of the center of mass is de ned in an inertial coordinate system.

2. Angular Momentum. Taking the vector cross product of $\mathbf { r }$ with both sides of Eq. (2.2.3) gives

$$
\mathbf { r } \times { \ddot { \mathbf { r } } } = 0 \quad { \mathrm { o r } } \quad { \frac { d } { d t } } ( \mathbf { r } \times { \dot { \mathbf { r } } } ) = 0 .
$$

Defining $\textbf { h } = \textbf { r } \times \dot { \textbf { r } }$ , the angular momentum per unit mass (or specific angular momentum), it follows that $\mathbf { h }$ is a vector constant:

$$
\mathbf { h } = \mathbf { r } \times { \dot { \mathbf { r } } } = \mathbf { c o n s t a n t } .
$$

An important interpretation of $\textbf { h } =$ constant is that the orbital motion is planar, since $\mathbf { r }$ and $\dot { \mathbf { r } }$ must always be perpendicular to $\mathbf { h }$ . The plane of the motion is referred to as the orbit plane, which is a plane that is perpendicular to the angular momentum vector. Note that the angular momentum in Eq. (2.2.6) is defined for the motion of $M _ { 2 }$ with respect to $M _ { 1 }$ .

3. Energy. Taking the vector dot product of $\dot { \mathbf { r } }$ with Eq. (2.2.3), it can be shown that

$$
\xi = { \frac { { \dot { \mathbf { r } } } \cdot { \dot { \mathbf { r } } } } { 2 } } - { \frac { \mu } { r } } = \mathrm { c o n s t a n t }
$$

where $\xi$ is the scalar energy per unit mass (also known as specific energy or vis viva) and $\dot { \mathbf { r } }$ is the velocity of $M _ { 2 }$ with respect to $M _ { 1 }$ . Thus, the energy per unit mass is constant; that is, the sum of the kinetic and potential energies is constant. Note that this expression describes the energy in terms of the motion of $M _ { 2 }$ with respect to $M _ { 1 }$ .

In summary, there are ten constants of the motion: $\mathbf { C } _ { 1 }$ $\mathbf { \Sigma } _ { 1 , 1 , 2 , \mathbf { h } , \xi } ^ { \bullet }$ . The following general properties of the orbital motion can be stated:

a. The motion of $M _ { 2 }$ with respect to $M _ { 1 }$ takes place in a plane, the orbit plane, defined as the plane that is perpendicular to the constant angular momentum vector $( \mathbf { h } = \mathbf { r } \times { \dot { \mathbf { r } } } ,$ );   
b. The center of mass of the two bodies moves in a straight line with constant velocity with respect to an inertial coordinate system;   
c. The scalar energy per unit mass is constant, as given by Eq. (2.2.7).

# 2.2.1 MOTION IN THE PLANE

The previous section summarized some general characteristics of the twobody motion, but the differential equations of motion, Eq. (2.2.3), were not solved. The detailed characteristics of the orbital motion are still to be determined, as described in this section.

The previous section showed that the orbital motion of $M _ { 2 }$ with respect to $M _ { 1 }$ takes place in a plane perpendicular to the angular momentum vector. This fact of planar motion can be used to facilitate the solution of Eq. (2.2.3). The planar motion is illustrated in Fig. 2.2.2, described with respect to a nonrotating $( X , Y , Z )$ coordinate system. The $\hat { X }$ axis is shown at the intersection of the orbit plane and the $( X , Y )$ plane, where the intersection between the planes is referred to as the line of nodes. The angles $i$ and $\Omega$ are discussed in Section 2.2.2. The $\hat { Y }$ axis is perpendicular to $\hat { X }$ , but it lies in the orbit plane, whereas $\hat { Z }$ is coincident with $\mathbf { h }$ . Since the angular momentum vector, $\mathbf { h }$ , is constant, the orientation of the orbit plane in space does not change with time, and the $( \hat { X } , \hat { Y } , \hat { Z } )$ axes are, therefore, nonrotating. From the introduction of a unit vector, $\mathbf { u } _ { r }$ , defined by $\mathbf { r } = r \ \mathbf { u } _ { r }$ and the unit vector, $\mathbf { u } _ { \theta }$ , as illustrated in Fig. 2.2.3, it follows that Eq. (2.2.3) can be written in polar coordinates as

![](images/a67bf4ce0d81ec3e5e0fdc8a9b02d70601f4695f443760e9b2a726aefba01426.jpg)  
Figure 2.2.2: The orbit plane in space. Since the angular momentum is constant, the motion of $M _ { 2 }$ with repect to $M _ { 1 }$ takes place in a plane, known as the orbit plane. This plane is perpendicular to the angular momentum vector and the orientation is defined by the angles $i$ and $\Omega$ .

$$
\begin{array} { c c } { { \bf u } _ { r } \mathrm { c o m p o n e n t : } } & { { \ddot { r } - r \dot { \theta } ^ { 2 } = - \frac { \mu } { r ^ { 2 } } } } \\ { { \bf u } _ { \theta } \mathrm { c o m p o n e n t : } } & { { 2 \dot { r } \dot { \theta } + r \ddot { \theta } = 0 . } } \end{array}
$$

Two cases exist: $\dot { \theta } = 0$ and $\dot { \theta } \neq 0$ . The $\dot { \theta } = 0$ case is rectilinear motion, which is a special case of no interest in this discussion. For the orbital motion case, $\dot { \theta } \neq 0$ , and it can be shown from Eq. (2.2.9) that

$$
{ \frac { d } { d t } } ( r ^ { 2 } { \dot { \theta } } ) = 0 .
$$

![](images/b8669705dbf7a6094502bcc4cf856c5e0202c6813938488f09020e8c54a84552.jpg)  
Figure 2.2.3: The planar motion described with polar coordinates.

Note that since ${ \dot { \mathbf { r } } } = { \dot { r } } \mathbf { u } _ { r } + r { \dot { \theta } } \mathbf { u } _ { \theta }$ , it follows from $\mathbf { h } = \mathbf { r } \times { \dot { \mathbf { r } } }$ that $\mathbf { h } = r ^ { 2 } { \dot { \theta } } { \mathbf { u } } _ { h }$ , where $\mathbf { u } _ { h }$ is the unit vector in the $\mathbf { h }$ direction. It is evident that $\textit { h } = r ^ { 2 } \Dot { \theta }$ is constant. Furthermore, a change in both the dependent and independent variables in Eq. (2.2.8)

$$
r \to 1 / u , \quad t \to \theta
$$

gives the differential equation of motion

$$
{ \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } + u = { \frac { \mu } { h ^ { 2 } } }
$$

which has the solution

$$
u = \frac { \mu } { h ^ { 2 } } + A \cos ( \theta - \omega )
$$

where $A$ and $\omega$ are constants of integration.

From Eq. (2.2.7) for the energy, it can be shown that

$$
A = { \frac { \mu } { h ^ { 2 } } } e
$$

where

$$
e = \left[ 1 + 2 \frac { \xi h ^ { 2 } } { \mu ^ { 2 } } \right] ^ { \frac { 1 } { 2 } } ,
$$

a positive quantity.

Table 2.2.1: Classes of Orbital Motion   

<table><tr><td>Orbit Type</td><td>Eccentricity</td><td>Energy</td><td>Orbital Speed</td></tr><tr><td>Circle</td><td>e=0</td><td>=- 品</td><td>V=√u/r</td></tr><tr><td>Ellipse</td><td>e&lt;1</td><td>m&lt;0</td><td>√μ/r &lt;V&lt;√2μ/r</td></tr><tr><td>Parabola</td><td>e=1</td><td>m=0</td><td>V = √2μ/r</td></tr><tr><td>Hyperbola</td><td>e&gt;1</td><td>m&gt;0</td><td>V &gt;√2μ/r</td></tr></table>

It follows from Eq. (2.2.13) that

$$
r = \frac { h ^ { 2 } / \mu } { 1 + e \cos ( \theta - \omega ) } .
$$

It can be readily shown that

$$
\frac { d r } { d \theta } = \frac { \mu e \sin ( \theta - \omega ) } { h ^ { 2 } ( 1 + \cos ( \theta - \omega ) ) ^ { 2 } }
$$

from which it follows that

$$
\frac { d r } { d \theta } = 0
$$

when $\theta = \omega$ or $\theta - \omega = \pi$ . Furthermore, since

$$
\frac { d ^ { 2 } r } { d \theta ^ { 2 } } > 0
$$

at $\theta = \omega$ , it is evident that $r$ is a minimum. This location with minimum $r$ is referred to as the perifocus, or perigee in the case of a satellite of the Earth. As a consequence, the constant of integration $\omega$ is known as the argument of perigee.

Introducing the true anomaly, $f$ defined by $f = \theta - \omega$ , then the expression for $r$ becomes

$$
r = { \frac { p } { 1 + e \cos f } }
$$

where $p = h ^ { 2 } / \mu$

The form of Eq. (2.2.15) is identical to the geometrical equation for a conic section (for example, see Danby [1988]). The geometrical quantities $p$ and $e$ are the semilatus rectum and eccentricity of the conic section, respectively. As shown in the preceding equations, these geometrical parameters are determined by dynamical parameters $h , \xi$ , and $\mu$ .

The two-body orbit can be described as a conic section: circle, ellipse, parabola, or hyperbola. The specific conic section is determined by the eccentricity, e. Each conic section has a specific energy and velocity for a given $r$ , as shown in Table 2.2.1.

![](images/34766eeedf52c00237142982948ba8dbc33f9852a0ef5e0917dbdc4442d091ea.jpg)  
Figure 2.2.4: Characteristics of the elliptic orbit. The circle has radius equal to $a$ and is used to illustrate the eccentric anomaly, $E$ . The dashed line is perpendicular to the major axis of the ellipse.

Only the conic sections with $e < 1$ are closed paths. The parabola and hyperbola are often referred to as escape trajectories.

Equation (2.2.15) describes the position of $M _ { 2 }$ with respect to $M _ { 1 }$ , where $M _ { 1 }$ is located at a focus of the conic section, and the position of $M _ { 2 }$ is described in terms of $r$ and $f$ . The ellipse conic section, as illustrated in Fig. 2.2.4, has two foci, where $M _ { 1 }$ is located at one focus and the other is an empty focus. The ellipse is defined by $p$ and $e$ , but other parameters are commonly used, such as semimajor axis $( a )$ and semiminor axis $( b )$ . Some useful geometrical relations are

$$
\begin{array} { r c l } { { p } } & { { = } } & { { a ( 1 - e ^ { 2 } ) } } \\ { { b } } & { { = } } & { { a \sqrt { 1 - e ^ { 2 } } . } } \end{array}
$$

Note that $p = r$ when $f = \pm \pi / 2$ .

The minimum distance between $M _ { 1 }$ and $M _ { 2 }$ is the perifocus (or perigee if $M _ { 1 }$ is the Earth), given by

$$
r _ { p } = a ( 1 - e )
$$

and the maximum distance, apfocus (or apogee for an Earth satellite) is

$$
r _ { a } = a ( 1 + e ) .
$$

Other relations between geometrical and dynamical parameters for the elliptical orbit can be shown to be

$$
\begin{array} { r } { h ^ { 2 } = \mu a ( 1 - e ^ { 2 } ) = \mu p } \\ { \xi = - \displaystyle \frac { \mu } { 2 a } . } \end{array}
$$

The $M _ { 2 }$ velocity, $\mathbf { V }$ , with respect to $M _ { 1 }$ can be written as

$$
{ \bf V } = \dot { r } { \bf u } _ { r } + r \dot { f } { \bf u } _ { \theta } .
$$

The magnitude of the $M _ { 2 }$ velocity (with respect to $M _ { 1 }$ ), or speed, is

$$
V = \sqrt { \mu ( 2 / r - 1 / a ) }
$$

and it can be shown that the radial component of the velocity, $\dot { r }$ , is

$$
\dot { r } = \frac { h e \sin f } { p }
$$

from which it is evident that the radial velocity is positive (away from $M _ { 1 }$ ) while traveling from perifocus to apfocus, and it is negative (toward $M _ { 1 }$ ) from apfocus to perifocus. Furthermore, from $h = r ^ { 2 } { \dot { f } }$ (since ${ \dot { f } } = { \dot { \theta } }$ ), the velocity component perpendicular to the position vector is

$$
r { \dot { f } } = { \frac { h } { r } } .
$$

As demonstrated by Vallado (2001), for example, the area (A) swept out by $r$ as a function of time is

$$
{ \frac { d A } { d t } } = { \frac { h } { 2 } }
$$

which is constant, thereby demonstrating Kepler’s Second Law. If this equation is integrated over one orbital period, $T$ , the time required for $M _ { 2 }$ to complete one revolution of $M _ { 1 }$ (for example, from perifocus and back to perifocus) is

$$
T = \frac { 2 \pi a ^ { 3 / 2 } } { \mu ^ { 1 / 2 } } .
$$

This equation verifies Kepler’s Third law.

From the conic section equation, Eq. (2.2.14), if the angle $f$ is known, the distance $r$ can be determined. However, for most applications, the time of a particular event is the known quantity, rather than the true anomaly, $f$ . A simple relation between time and true anomaly does not exist. The transformation between time and true anomaly uses an alternate angle, $E$ , the eccentric anomaly, and is expressed by Kepler’s Equation, which relates time and $E$ as

$$
E - e \sin E = n ( t - t _ { p } )
$$

where $n$ is the mean motion $( \sqrt { \mu / a ^ { 3 } } )$ , $t$ is time, and $t _ { p }$ is the time when $M _ { 2 }$ is located at perifocus. The time $t _ { p }$ is a constant of integration. Since Kepler’s Equation is a transcendental equation, its solution can be obtained by an iterative method, such as the Newton–Raphson method. If

$$
g = E - e \sin E - M ,
$$

where $M = n ( t - t _ { p } )$ , the mean anomaly, then the iterative solution gives

$$
E _ { k + 1 } = E _ { k } - \left( \frac { g } { g ^ { \prime } } \right) _ { k } ,
$$

where $k$ represents the iteration number and

$$
g ^ { \prime } = \frac { d g } { d E } = 1 - e \cos E .
$$

From known values of $a$ and $e$ and a specifie $\textrm { d } t$ , the preceding iterative method will provide the eccentric anomaly, $E$ . A typical value of $E$ to start the iteration is $E _ { 0 } = M$ . Some useful relations between the true anomaly and the eccentric anomaly are

$$
\begin{array} { c c } { { \sin f = \displaystyle \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \sin E } { 1 - e \cos E } \quad } } & { { \sin E = \displaystyle \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \sin f } { 1 + e \cos f } } } \\ { { \cos f = \displaystyle \frac { \cos E - e } { 1 - e \cos E } \quad } } & { { \cos E = \displaystyle \frac { e + \cos f } { 1 + e \cos f } } } \\ { { \tan \displaystyle \frac { f } { 2 } = \displaystyle \left( \frac { 1 + e } { 1 - e } \right) ^ { 1 / 2 } \tan \displaystyle \frac { E } { 2 } \quad } } & { { \tan \displaystyle \frac { E } { 2 } = \displaystyle \left( \frac { 1 - e } { 1 + e } \right) ^ { 1 / 2 } \tan \displaystyle \frac { f } { 2 } } } \end{array}
$$

$$
{ \begin{array} { r c l } { M } & { = } & { E - e \sin E { \mathrm { ( K e p l e r ' s ~ E q u a t i o n ) } } } \\ { { \frac { d f } { d E } } } & { = } & { { \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { 1 - e \cos E } } = { \frac { 1 + e \cos f } { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } } } \\ { { \frac { d M } { d E } } } & { = } & { 1 - e \cos E = { \frac { 1 - e ^ { 2 } } { 1 + e \cos f } } } \\ { { \frac { d M } { d f } } } & { = } & { { \frac { ( 1 - e \cos E ) ^ { 2 } } { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } } = { \frac { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } { ( 1 + e \cos f ) ^ { 2 } } } . } \end{array} }
$$

It can be shown that

$$
r = a ( 1 - e \cos E )
$$

but in some cases it is useful to express $r$ as a function of time, or mean anomaly. This relation for elliptic orbits, however, involves an infinite series because of the

transcendental nature of Kepler’s Equation; namely,

$$
\frac { a } { r } = 1 + 2 \sum _ { m = 1 } ^ { \infty } \hat { J } _ { m } ( m e ) \cos m M
$$

where ${ \hat { J } } _ { m } $ is the Bessel Function of the first kind of order $m$ , with argument me (see Smart, 1961; Brouwer and Clemence, 1961). If the eccentricity is small, the following approximate equations may be useful:

$$
{ \begin{array} { r c l } { { \frac { a } { r } } } & { \simeq } & { 1 + e \cos M + \mathrm { h i g h e r ~ o r d e r ~ t e r m s } } \\ { } & { \simeq } & { \cos M + e ( \cos 2 M - 1 ) + \dots } \\ { } & { \sin f } & { \cong } & { \sin M + e \sin 2 M + \dots } \\ { f } & { \cong } & { M + 2 e \sin M + \dots } \\ { } & { \cos E } & { \cong } & { \cos M + { \frac { e } { 2 } } ( \cos 2 M - 1 ) + \dots } \\ { } & { \sin E } & { \cong } & { \sin M + { \frac { e } { 2 } } \sin 2 M + \dots } \\ { } & { \cong } & { M + e \sin M + \dots ~ . } \end{array} }
$$

# 2.2.2 MOTION IN SPACE

The preceding section has described the two-body orbital motion in the plane. The description of the complete three-dimensional motion requires two additional parameters. The angular momentum per unit mass, $\mathbf { h }$ , is

$$
\mathbf { h } = h _ { X } \mathbf { u } _ { X } + h _ { Y } \mathbf { u } _ { Y } + h _ { Z } \mathbf { u } _ { Z }
$$

where $\mathbf { u } _ { X } , \mathbf { u } _ { Y }$ , and $\mathbf { u } _ { Z }$ are unit vectors associated with the $( X , Y , Z )$ axes. Two angles, $i$ and $\Omega$ (see Fig. 2.2.2), can be used to describe the three-dimensional orientation of the orbit plane.

The orbital inclination, $i$ , is the angle between the $Z$ axis and $\mathbf { h }$ . This angle can be determined from

$$
\cos i = { \frac { h _ { Z } } { h } } ,
$$

where $0 \leq i \leq 1 8 0 ^ { \circ }$ and $h = | \mathbf { h } |$ . If the $( X , \ Y )$ axes are in the equator of the planet, then the orbit can be categorized by the inclination, as summarized in Table 2.2.2.

The orbit plane shown in Fig. 2.2.2 intersects the plane containing the $( X , Y )$ axes at the line of nodes. Since the motion is planar, the satellite will move through the line of nodes at the ascending node (AN) where it moves from $- Z$ to $+ Z$ . With the $( X , Y )$ axes in the equatorial plane, the satellite moves from the southern hemisphere to the northern hemisphere when it crosses the ascending node.

Table 2.2.2: Inclination Terminology   

<table><tr><td>i</td><td>Orbit Type</td></tr><tr><td>90°</td><td>Polar</td></tr><tr><td>0≤i&lt;90°</td><td>Posigrade</td></tr><tr><td>90°&lt;i≤180°</td><td>Retrograde</td></tr><tr><td>i=0°</td><td>Posigrade equatorial</td></tr><tr><td>i= 180°</td><td>Retrograde equatorial</td></tr></table>

Similarly, the point where the satellite crosses the line of nodes from $+ Z$ to $- Z$ is referred to as the descending node (DN). The angle, $\Omega$ , that defines the ascending node location is

$$
\begin{array} { l c l } { \sin \Omega } & { = } & { \displaystyle \frac { h _ { X } } { h _ { X Y } } } \\ { \cos \Omega } & { = } & { \displaystyle - \frac { h _ { Y } } { h _ { X Y } } } \end{array}
$$

where $h _ { X Y } = [ h _ { X } ^ { 2 } + h _ { Y } ^ { 2 } ] ^ { 1 / 2 }$ and $0 \leq \Omega \leq 3 6 0 ^ { \circ }$ . Note that both $\sin \Omega$ and $\cos \Omega$ are required to determine the quadrant of $\Omega$ . The specific terminology used for $\Omega$ depends on the $( X , \ Y , \ Z )$ coordinate system. The term right ascension of the ascending node is used in cases where $( X , \ Y , \ Z )$ is a celestial system, but longitude of the ascending node is used in the case of an Earth-fix ed coordinate system.

# 2.2.3 BASIC COORDINATE SYSTEMS

The $( X , Y , Z )$ coordinate system used in the preceding sections has no preferred orientation for the simple description of the two-body motion. Nevertheless, a specific, well-defined orientation of the $( X , \ Y , \ Z )$ axes is required in practice.

Consider the motion of the Earth about the Sun. Since the mass of the Sun is 328,000 times the mass of the Earth, it is quite natural to describe the motion of this system as the motion of the Earth relative to the Sun. But from the description of the two-body motion, there is no requirement that $M _ { 1 }$ be greater than $M _ { 2 }$ or vice versa. The two-body motion of the Earth-Sun system is illustrated in Fig. 2.2.5 from a geocentric point of view. The sphere representing the Earth includes a body-fix ed (Earth-fixed) coordinate system, with the $( x , y )$ axes in the equatorial plane and with the $x$ axis coincident with the intersection of the Greenwich meridian and the equator. The $z$ axis of the Earth-fix ed system coincides with the angular velocity vector of the Earth, $\omega _ { e }$ . The nonrotating $( X ^ { \prime } , Y ^ { \prime } )$ axes lie in the Earth’s equator, but there is no preferred direction for these axes, except the $Z ^ { \prime }$ axis coincides with the angular velocity of the Earth in this model. The Earth-Sun orbit plane intersects the equator at the line of nodes. The point where the Sun moves from the southern hemisphere into the northern hemisphere is the ascending node, denoted by AN in Fig. 2.2.5 from a geocentric viewpoint. Similarly, the descending node is identified by DN.

![](images/32ff5e19abe63f22d299e174ad6ef53e327c7c8a7d4c9fa3392dcc5a9162818e.jpg)  
Figure 2.2.5: The Earth-Sun two-body motion. For convenience the motion can be described from the geocentric perspective to illustrate the relations between twobody parameters and astronomical conventions. The orbit plane defined by the angular momentum of the two-body system is the ecliptic, the ascending node is the vernal equinox, and the inclination is the obliquity of the ecliptic. The bodies are not drawn to scale since the diameter of the Sun is 100 times the diameter of the Earth. The $( \mathrm { X } ^ { \prime } , \mathrm { Y } ^ { \prime } )$ axes have no preferred orientation, but the $\mathbf { X }$ axis is chosen to coincide with the vernal equinox.

The description given in the preceding paragraph and illustrated in Fig. 2.2.5 contains the essential descriptions of a well-defined and consistent celestial coordinate system. Since the two celestial bodies are modeled as rigid spheres with constant density, the node locations are fix ed in space and the angular velocity vector, $\omega _ { e }$ , of the rotating Earth is constant in magnitude and direction.

Special terms are assigned to the orbit parameters illustrated in Fig. 2.2.5. The orbit plane of the Sun about the Earth (or the Earth about the Sun) is referred to as the ecliptic and the inclination is the obliquity of the ecliptic, usually denoted by $\epsilon \ : ( \simeq 2 3 . 5 ^ { \circ }$ ). The ascending node corresponds to the point known as the vernal equinox and the descending node is the autumnal equinox. The vernal equinox occurs about March 21 and the autumnal equinox occurs about September 21. The location of the Sun when it is $9 0 ^ { \circ }$ from the vernal equinox is the summer solstice and the location at $2 7 0 ^ { \circ }$ is the winter solstice, which occur about June 21 and December 21, respectively. It is somewhat prejudicial that these astronomical locations are identified with northern hemisphere seasons, since association with seasons is reversed in the southern hemisphere. Finally, the angle $\alpha _ { G }$ defines the orientation of the Earth-fix ed coordinate system $( x , y , z )$ with respect to the vernal equinox (i.e., the $x$ axis shown in Fig. 2.2.5). The angle $\alpha _ { G }$ is known as the Greenwich mean sidereal time (GMST), defined by $\alpha _ { G } = \omega _ { e } ( t - t _ { 0 } ) + \alpha _ { G 0 }$ . The period of Earth rotation with respect to a fix ed direction in space is about 86,164 sec $( 2 3 \mathrm { h r } 5 6 \mathrm { m i n } 4 \mathrm { s e c } )$ (i.e., $\omega _ { e } = 2 \pi / 8 6 1 6 4 ~ \mathrm { r a d / s e c } )$ .

With the $X$ axis directed toward the vernal equinox and with both the $z$ and $Z$ axes coincident with the angular velocity vector, $\omega _ { e }$ , it follows that the relations between the nonrotating $( X , Y , Z )$ axes and the Earth-fix ed, rotating $( x , y , z )$ axes as illustrated in Fig. 2.2.5 are

$$
\begin{array} { l c l } { x } & { = } & { X \cos \alpha _ { G } + Y \sin \alpha _ { G } } \\ { y } & { = } & { - X \sin \alpha _ { G } + Y \cos \alpha _ { G } } \\ { z } & { = } & { Z . } \end{array}
$$

For the two-body problem that has been described up to this point, the orientation of the ecliptic defined in a consistent manner with the two-body dynamics will be fix ed in space. Hence, the vernal equinox would be a fix ed direction in space and the obliquity of the ecliptic would also be fix ed. However, as described in Section 2.4, temporal variations exist in the location of the vernal equinox and in $\epsilon$ . With such variations, it is necessary to designate a specific epoch to be assigned to the equinox and obliquity. A commonly used reference is the mean equator and equinox of 2000.0 (the vernal equinox on January 1, 2000, 12 hrs). The system defined for this date is referred to as the J2000 system. In some applications, the M50 system is used, which is defined by the mean equator and equinox of

1950.0. The nonrotating J2000 or M50 systems are sometimes referred to as Earth-centered inertial (ECI) and the Earth-fix ed system $( x , y , z )$ is referred to as Earth-centered, Earth-fix ed (ECF or ECEF or ECF (Earth-centered, fix ed)). We will use the notation J2000 to refer to the system and J2000.0 to refer to the date.

# 2.2.4 ORBIT ELEMENTS AND POSITION/VELOCITY

Assume that an artificial satellite orbits a planet whose mass, $M _ { 1 }$ , is known (i.e., $\mu = G M _ { 1 }$ is known). Assume further that a technique and/or procedure has been utilized to determine the position and velocity of the satellite at a time, $t _ { 0 }$ , in a nonrotating coordinate system. The position and velocity at $t _ { 0 }$ are

$$
\begin{array} { r c l } { \mathbf { r } _ { 0 } } & { = } & { X _ { 0 } \mathbf { u } _ { X } + Y _ { 0 } \mathbf { u } _ { Y } + Z _ { 0 } \mathbf { u } _ { Z } } \\ { \mathbf { V } _ { 0 } } & { = } & { \dot { X } _ { 0 } \mathbf { u } _ { X } + \dot { Y } _ { 0 } \mathbf { u } _ { Y } + \dot { Z } _ { 0 } \mathbf { u } _ { Z } . } \end{array}
$$

The angular momentum, $\mathbf { h }$ , is

$$
\mathbf { h } = h _ { X } \mathbf { u } _ { X } + h _ { Y } \mathbf { u } _ { Y } + h _ { Z } \mathbf { u } _ { Z }
$$

where

$$
\begin{array} { r c l } { { h _ { X } } } & { { = } } & { { Y _ { 0 } \dot { Z } _ { 0 } - \dot { Y } _ { 0 } Z _ { 0 } } } \\ { { h _ { Y } } } & { { = } } & { { Z _ { 0 } \dot { X } _ { 0 } - \dot { Z } _ { 0 } X _ { 0 } } } \\ { { h _ { Z } } } & { { = } } & { { X _ { 0 } \dot { Y } _ { 0 } - \dot { X } _ { 0 } Y _ { 0 } . } } \end{array}
$$

Also,

$$
h ^ { 2 } = \mathbf { h } \cdot \mathbf { h } .
$$

It follows that the inclination $( i )$ and node location $( \Omega )$ can be determined from Eqs. (2.2.28), (2.2.29), (2.2.30), and (2.2.33).

The energy per unit mass can be determined from Eq. (2.2.7),

$$
\xi = \frac { V _ { 0 } ^ { 2 } } { 2 } - \frac { \mu } { r _ { 0 } }
$$

where

$$
V _ { 0 } ^ { 2 } = \mathbf { V } _ { 0 } \cdot \mathbf { V } _ { 0 }
$$

and

$$
r _ { 0 } = \left[ \mathbf { r } _ { 0 } \cdot \mathbf { r } _ { 0 } \right] ^ { 1 / 2 } .
$$

From $\xi$ , the semimajor axis is

$$
a = - \frac { \mu } { 2 \xi } .
$$

The eccentricity of the orbit is determined from Eq. (2.2.14),

$$
e = \left[ 1 + \frac { 2 \xi h ^ { 2 } } { \mu ^ { 2 } } \right] ^ { 1 / 2 } .
$$

The semilatus rectum is given by $p = h ^ { 2 } / \mu$ and the true anomaly is

$$
\begin{array} { l } { \displaystyle \cos f = \frac { 1 } { r _ { 0 } e } [ p - r _ { 0 } ] } \\ { \displaystyle \sin f = \frac { p } { h e } \frac { { \bf r } _ { 0 } \cdot \dot { \bf r _ { 0 } } } { r _ { 0 } } . } \end{array}
$$

The angle $( \omega + f )$ i s

$$
\cos ( \omega + f ) = \frac { X _ { 0 } } { r _ { 0 } } \cos \Omega + \frac { Y _ { 0 } } { r _ { 0 } } \sin \Omega
$$

$$
\sin ( \omega + f ) = \frac { Z _ { 0 } } { r _ { 0 } \sin i }
$$

where both cosine and sine expressions are required to properly determine the quadrant. The argument of perifocus, $\omega$ , can be determined from

$$
\omega = ( \omega + f ) - f .
$$

An alternate determination of the argument of perifocus can be obtained from the eccentricity vector, $\mathbf { e }$ , a vector directed toward perifocus with magnitude equal to the orbit eccentricity. The vector $\mathbf { e }$ is given by

$$
\mathbf { e } = \mathbf { V } _ { 0 } \times { \frac { \mathbf { h } } { \mu } } - { \frac { \mathbf { r } _ { 0 } } { r _ { 0 } } } = e _ { X } \mathbf { u } _ { X } + e _ { Y } \mathbf { u } _ { Y } + e _ { Z } \mathbf { u } _ { Z } .
$$

It can be shown that

$$
\cos \omega = \frac { e _ { X } \cos \Omega + e _ { Y } \sin \Omega } { e }
$$

$$
\sin \omega = \frac { - \cos i \sin \Omega e _ { X } + \cos i \cos \Omega e _ { Y } + \sin i e _ { Z } } { e } .
$$

The eccentric anomaly, $E _ { 0 }$ , can be obtained from

$$
\begin{array} { r } { \cos E _ { 0 } = \frac { r _ { 0 } } { a } \cos f + e } \\ { \sin E _ { 0 } = \frac { r _ { 0 } } { b } \sin f . } \end{array}
$$

Furthermore, the mean anomaly, $M _ { 0 }$ , is given by

$$
M _ { 0 } = E _ { 0 } - e \sin E _ { 0 }
$$

and the time of perifocus passage is

$$
t _ { p } = t _ { 0 } - { \frac { M _ { 0 } } { n } } .
$$

In summary, the position and velocity vectors at $t _ { 0 }$ completely describe the two-body orbit, since they can be converted to an independent set of six orbit elements:

$$
\begin{array} { r } { a } \\ { e } \\ { i } \\ { \Omega } \\ { \omega } \\ { t _ { p } \mathrm { o r } M _ { 0 } . } \end{array}
$$

In other words, the position and velocity completely determine the nature of the two-body orbit, assuming that $\mu$ is known. Similarly, if the orbit elements are given, there are corresponding position and velocity vectors at a specified time.

# Example 2.2.4.1

The ECI position and velocity of a Space Shuttle has been determined to be the following:

$$
{ \begin{array} { l c c c } { X } & { = } & { 5 4 9 2 0 0 0 . 3 4 } & { { \mathrm { m } } } \\ { Y } & { = } & { 3 9 8 4 0 0 1 . 4 0 } & { { \mathrm { m } } } \\ { Z } & { = } & { 2 9 5 5 . 8 1 } & { { \mathrm { m } } } \\ { { \dot { X } } } & { = } & { - 3 9 3 1 . 0 4 6 4 9 1 } & { { \mathrm { m / s e c } } } \\ { { \dot { Y } } } & { = } & { 5 4 9 8 . 6 7 6 9 2 1 } & { { \mathrm { m / s e c } } } \\ { { \dot { Z } } } & { = } & { 3 6 6 5 . 9 8 0 6 9 7 } & { { \mathrm { m / s e c } } } \end{array} }
$$

With $\mu = 3 . 9 8 6 0 0 4 4 \times 1 0 ^ { 1 4 } \mathrm { m ^ { 3 } / s ^ { 2 } }$ and the preceding equations, it follows that the corresponding orbit elements are

Also,

# Example 2.2.4.2

A two-line element (TLE) format is commonly used by NORAD and NASA. An example for NOAA 14 is

NOAA 14

1 23455U 94089A 97229.90474114 .00000115 00000-0 88111-4 0 1530   
2 23455 98.9964 181.3428 0010013 113.9737 246.2483 14.11685823135657

The interpretation of the TLE format is given in Table 2.2.3. Some components of the TLE pertain to the perturbing effects of additional forces, described in Section 2.3. Updated TLE sets can be found on the World Wide Web.

Convert the TLE for NOAA 14 into position and velocity at the epoch contained in the format. From the TLE set, the orbit elements on Day 229.90474114 of 1997 are

It follows that

# 2.2.5 POSITION/VELOCITY PREDICTION

With a specified set of orbit elements, the position and velocity at time $t$ can be determined by solving Kepler’s Equation for eccentric anomaly and determining true anomaly. From the orbit elements and the true anomaly at time $t$ , the position and velocity are

$$
\begin{array} { l c l } { { X } } & { { = } } & { { r \cos f Q _ { 1 1 } + r \sin f Q _ { 1 2 } } } \\ { { Y } } & { { = } } & { { r \cos f Q _ { 2 1 } + r \sin f Q _ { 2 2 } } } \\ { { Z } } & { { = } } & { { r \cos f Q _ { 3 1 } + r \sin f Q _ { 3 2 } } } \\ { { \dot { X } } } & { { = } } & { { \dot { X } ^ { \ast } Q _ { 1 1 } + \dot { Y } ^ { \ast } Q _ { 1 2 } } } \\ { { \dot { Y } } } & { { = } } & { { \dot { X } ^ { \ast } Q _ { 2 1 } + \dot { Y } ^ { \ast } Q _ { 2 2 } } } \\ { { \dot { Z } } } & { { = } } & { { \dot { X } ^ { \ast } Q _ { 3 1 } + \dot { Y } ^ { \ast } Q _ { 3 2 } } } \end{array}
$$

Table 2.2.3: NORAD/NASA TWO-LINE ELEMENTS (TLE)   

<table><tr><td rowspan=1 colspan=2>Line 1</td></tr><tr><td rowspan=1 colspan=1>Column</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>01-01</td><td rowspan=1 colspan=1>Line Number of Element Data</td></tr><tr><td rowspan=1 colspan=1>03-07</td><td rowspan=1 colspan=1>Satellite Number</td></tr><tr><td rowspan=1 colspan=1>10-11</td><td rowspan=1 colspan=1>International Designator (Last two digits of launch year)</td></tr><tr><td rowspan=1 colspan=1>12-14</td><td rowspan=1 colspan=1>International Designator (Launch number of the year)</td></tr><tr><td rowspan=1 colspan=1>15-17</td><td rowspan=1 colspan=1>International Designator (Component of launch)</td></tr><tr><td rowspan=1 colspan=1>19-20</td><td rowspan=1 colspan=1>Epoch Year (Last two digits of year)</td></tr><tr><td rowspan=1 colspan=1>21-32</td><td rowspan=1 colspan=1>Epoch (Day of year and fractional portion of the day)</td></tr><tr><td rowspan=1 colspan=1>34-43</td><td rowspan=1 colspan=1>First Time Derivative of the Mean Motion or Ballistic Coeffcient</td></tr><tr><td rowspan=1 colspan=1>45-52</td><td rowspan=1 colspan=1>Second Time Derivative of Mean Motion (decimal point assumed)</td></tr><tr><td rowspan=1 colspan=1>54-61</td><td rowspan=1 colspan=1>Drag term or radiation pressure coeffcient (decimal point assumed)</td></tr><tr><td rowspan=1 colspan=1>63-63</td><td rowspan=1 colspan=1>Ephemeris type</td></tr><tr><td rowspan=1 colspan=1>65-68</td><td rowspan=1 colspan=1>Element number</td></tr><tr><td rowspan=1 colspan=1>69-69</td><td rowspan=1 colspan=1>Check sum (Modulo 10)</td></tr><tr><td rowspan=1 colspan=2>Line 2</td></tr><tr><td rowspan=1 colspan=1>Column</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>01-01</td><td rowspan=1 colspan=1>Line Number of Element Data</td></tr><tr><td rowspan=1 colspan=1>03-07</td><td rowspan=1 colspan=1>Satellite Number</td></tr><tr><td rowspan=1 colspan=1>09-16</td><td rowspan=1 colspan=1>Inclination [Degrees]</td></tr><tr><td rowspan=1 colspan=1>18-25</td><td rowspan=1 colspan=1>Right Ascension of the Ascending Node [Degrees]</td></tr><tr><td rowspan=1 colspan=1>27-33</td><td rowspan=1 colspan=1>Eccentricity (decimal point assumed)</td></tr><tr><td rowspan=1 colspan=1>35-42</td><td rowspan=1 colspan=1>Argument of Perigee [Degrees]</td></tr><tr><td rowspan=1 colspan=1>44-51</td><td rowspan=1 colspan=1>Mean Anomaly [Degrees]</td></tr><tr><td rowspan=1 colspan=1>53-63</td><td rowspan=1 colspan=1>Mean Motion [Revs per day]</td></tr><tr><td rowspan=1 colspan=1>64-68</td><td rowspan=1 colspan=1>Revolution number at epoch [Revs]</td></tr><tr><td rowspan=1 colspan=1>69-69</td><td rowspan=1 colspan=1>Check Sum (Modulo 10)</td></tr></table>

where

$$
\begin{array} { r c l } { \dot { X } ^ { * } } & { = } & { V _ { \mathrm { r } } \cos f - V _ { \mathrm { r } } \sin f } \\ { \dot { Y } ^ { * } } & { = } & { V _ { \mathrm { r } } \sin f + V _ { \mathrm { t } } \cos f } \\ { V _ { \mathrm { r } } } & { = } & { \dot { r } - \frac { \hbar c } { 9 } \sin f } \\ { V _ { \mathrm { \theta } } } & { = } & { \frac { \hbar } { r } } \\ { Q _ { 1 1 } } & { = } & { \cos \omega \cos \Omega - \sin \omega \sin \Omega \cos i } \\ { Q _ { 2 1 } } & { = } & { - \sin \omega \cos \Omega - \cos \omega \sin \Omega \cos i } \\ { Q _ { 2 1 } } & { = } & { \cos \omega \sin \Omega + \sin \omega \cos \Omega \cos i } \\ { Q _ { 2 2 } } & { = } & { - \sin \omega \sin \Omega + \cos \omega \cos \Omega \cos i } \\ { Q _ { 3 1 } } & { = } & { \sin \omega \sin i } \\ { Q _ { 2 3 } } & { = } & { \cos \omega \cos \sin i . } \end{array}
$$

# Example 2.2.5

The position and velocity of the Space Shuttle at a later time can be determined from the state given in Example 2.2.4.1. For example, at 30 minutes after the epoch used in Example 2.2.4.1, the eccentric anomaly is $1 5 9 . 6 2 8 1 3 8 ^ { \circ }$ . It follows that the position and velocity at 30 minutes is

An example of an ephemeris of positions, or table of positions, for the interval $3 0 \mathrm { { m i n } }$ to $3 4 \mathrm { m i n }$ is

<table><tr><td>t (min)</td><td>X (m)</td><td>Y (m)</td><td>Z (m)</td></tr><tr><td>30</td><td>-5579681.52</td><td>2729244.60</td><td>2973901.72</td></tr><tr><td>32</td><td>-5999982.83</td><td>1951421.98</td><td>2765929.81</td></tr><tr><td>34</td><td>-6315097.41</td><td>1139386.52</td><td>2509466.97</td></tr></table>

![](images/fc0f4897c47db6de47254e55f2eb62724f69d62afe8c8cfee1bbd49c9bdd44f4.jpg)  
Figure 2.2.6: Shuttle ground track: the latitude-longitude ephemeris of Example 2.2.4.1. The latitude-longitude ephemeris is overlaid on a global map to illustrate the ground track of the satellite.

In some applications, the ephemeris is expressed in the body-fix ed coordinate system. The transformation is given by Eq. (2.2.31), in which

$$
\alpha _ { G } = \omega _ { e } ( t - t _ { 0 } ) + \alpha _ { G 0 } .
$$

Assuming $t _ { 0 } = 0$ and $\alpha _ { G 0 } = 0$ , it follows that the preceding ephemeris expressed in ECF coordinates is:

<table><tr><td>t (min)</td><td>x (m)</td><td>y(m)</td><td>z (m)</td></tr><tr><td>30</td><td>-5174477.07</td><td>3436045.54</td><td>2973901.72</td></tr><tr><td>32</td><td>-5668947.18</td><td>2769635.28</td><td>2765929.81</td></tr><tr><td>34</td><td>-6076481.79</td><td>2062771.41</td><td>2509466.97</td></tr></table>

![](images/5e026e00fddadc3c96caab525dbd0d02f009a1f8b71cdbce65a404cc5dbbf682.jpg)  
Figure 2.2.7: Definition of geocentric latitude $( \phi )$ and longitude $( \lambda )$ .

For other applications, these coordinates are further transformed into geocentric latitude $( \phi )$ and longitude $( \lambda )$ , illustrated in Fig. 2.2.7 and defined by

$$
\begin{array} { l c l } { x } & { = } & { r \cos \phi \cos \lambda } \\ { y } & { = } & { r \cos \phi \sin \lambda } \\ { z } & { = } & { r \sin \phi } \end{array}
$$

or

$$
\begin{array} { l l } { \sin \phi = \displaystyle \frac { z } { r } } & { - 9 0 ^ { \circ } \leq \phi \leq 9 0 ^ { \circ } } \\ { \cos \lambda = \displaystyle \frac { x } { r \cos \phi } } & \\ { \sin \lambda = \displaystyle \frac { y } { r \cos \phi } } & { 0 \leq \lambda \leq 3 6 0 ^ { \circ } . } \end{array}
$$

The altitude, $h$ , is obtained from $h = r - r _ { e }$ , where $r _ { e }$ is the Earth radius. The geocentric latitude, longitude, and height ephemeris derived from the preceding ECF ephemeris for the interval is:

<table><tr><td>t(min)</td><td>(deg)</td><td>入(deg)</td><td>h(m)</td></tr><tr><td>30</td><td>25.584</td><td>146.414</td><td>508495.95</td></tr><tr><td>32</td><td>23.672</td><td>153.962</td><td>510854.90</td></tr><tr><td>34</td><td>21.359</td><td>161.249</td><td>512151.92</td></tr></table>

Here, it has been assumed that the Earth is spherical with radius $6 3 7 8 1 3 7 \mathrm { m }$ . The latitude/longitude ephemeris can be plotted on a global or regional map to illustrate the path of the subsatellite point; that is, the point where the position vector of the satellite pierces the Earth’s surface. The subsatellite locus of points produces a ground track. The ephemeris generated by the position and velocity in Example 2.2.4.1 for two orbital revolutions is illustrated in Fig. 2.2.6.

It is evident from Fig. 2.2.6 that, although $\Omega$ is constant, the longitude of the point where the satellite crosses the equator in a northward direction is not constant. The change in the longitude of the ascending node is caused solely by the rotation of the Earth in the two-body problem, but other factors contribute as well to the actual motion, as described in Section 2.3.

# 2.2.6 STATE TRANSITION MATRIX AND ERROR PROPAGA-TION

The initial state for a particular problem, such as the example state vectors in the Section 2.2.4 examples, can be expected to be in error at some level. If the error in position, for example, is $\Delta \mathbf { r } ( t _ { 0 } )$ , this error will produce an error $\Delta \mathbf { r } ( t )$ at a later time $t$ , as well as an error in velocity, $\Delta \dot { \mathbf { r } } ( t )$ . The propagation of the error at $t _ { 0 }$ to an error at $t$ can be approximately expressed by

$$
[ \begin{array} { c } { \Delta X } \\ { \Delta Y } \\ { \Delta Z } \\ { \Delta \dot { X } } \\ { \Delta \dot { X } } \\ { \Delta \dot { Y } } \\ { \Delta \dot { X } } \\ { \Delta \dot { Z } } \end{array} ] = [ \begin{array} { c c c c c c c } { \frac { \partial X } { \partial X _ { 0 } } } & { \frac { \partial X } { \partial Y _ { 0 } } } & { \frac { \partial X } { \partial Z _ { 0 } } } & { \frac { \partial X } { \partial X _ { 0 } } } & { \frac { \partial X } { \partial Y _ { 0 } } } & { \frac { \partial X } { \partial Z _ { 0 } } } \\ { \frac { \partial Y } { \partial X _ { 0 } } } & { \frac { \partial Y } { \partial Y _ { 0 } } } & { \frac { \partial Y } { \partial Z _ { 0 } } } & { \frac { \partial Y } { \partial X _ { 0 } } } & { \frac { \partial Y } { \partial Y _ { 0 } } } & { \frac { \partial Y } { \partial Z _ { 0 } } } \\ { \frac { \partial Z } { \partial X _ { 0 } } } & { \frac { \partial Z } { \partial Y _ { 0 } } } & { \frac { \partial Z } { \partial Z _ { 0 } } } & { \frac { \partial Z } { \partial X _ { 0 } } } & { \frac { \partial Z } { \partial Y _ { 0 } } } & { \frac { \partial Z } { \partial Z _ { 0 } } } \\ { \frac { \partial \dot { X } } { \partial X _ { 0 } } } & { \frac { \partial \dot { X } } { \partial Y _ { 0 } } } & { \frac { \partial \dot { X } } { \partial Z _ { 0 } } } & { \frac { \partial \dot { X } } { \partial X _ { 0 } } } & { \frac { \partial \dot { X } } { \partial Y _ { 0 } } } & { \frac { \partial \dot { X } } { \partial Z _ { 0 } } } \\ { \frac { \partial \dot { Y } } { \partial X _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial Y _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial Z _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial X _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial Y _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial Z _ { 0 } } } \\ { \frac { \partial \dot { Z } } { \partial X _ { 0 } } } & { \frac { \partial \dot { Z } } { \partial Y _ { 0 } } } &  \frac { \partial \dot { Z } }  \partial Z _  \end{array}
$$

where the matrix of partial derivatives is referred to as the state transition matrix, also known as the matrizant. Although they are complicated, expressions for the partial derivatives, such as $\frac { \partial X } { \partial X _ { 0 } }$ , can be formed for the problem of two bodies (e.g., Goodyear, 1965). A general approach to the generation of the state transition matrix is given in Chapter 4. The origin of Eq. (2.2.38) can readily be seen by noting that a differential change in $X$ at time $t$ is related to differential changes in position and velocity at $t _ { 0 }$ by

$$
\begin{array} { r } { d X = \cfrac { \partial X } { \partial X _ { 0 } } d X _ { 0 } + \cfrac { \partial X } { \partial Y _ { 0 } } d Y _ { 0 } + \cfrac { \partial X } { \partial Z _ { 0 } } d Z _ { 0 } + \cfrac { \partial X } { \partial \dot { X } _ { 0 } } d \dot { X } _ { 0 } } \\ { + \cfrac { \partial X } { \partial \dot { Y } _ { 0 } } d \dot { Y } _ { 0 } + \cfrac { \partial X } { \partial \dot { Z } _ { 0 } } d \dot { Z } _ { 0 } . } \end{array}
$$

For fini te changes, let $\Delta X$ replace $d X$ , $\Delta X _ { 0 }$ replace $d X _ { 0 }$ , and so on; then Eq.   
(2.2.38) becomes the equation produced by Eq. (2.2.39) for $\Delta X$ .

# Example 2.2.6.1

Assuming an initial error in Example 2.2.4.1 given by

$$
\begin{array} { r l } { \Delta X _ { 0 } = } & { { } ~ 1 \mathrm { m } } \\ { \Delta Y _ { 0 } = } & { { } ~ 2 \mathrm { m } } \\ { \Delta Z _ { 0 } = } & { { } ~ 3 \mathrm { m } } \\ { \Delta \dot { X } _ { 0 } = } & { { } ~ 0 } \\ { \Delta \dot { Y } _ { 0 } = } & { { } ~ 0 } \\ { \Delta \dot { Z } _ { 0 } = } & { { } ~ 0 , } \end{array}
$$

the Goodyear (1965) formulation of the state transition matrix can be used to map this error to $3 0 \mathrm { { m i n } }$ , which produces

$$
\begin{array} { r l } { \Delta X = } & { { } \quad 0 . 6 5 \mathrm { m } } \\ { \Delta Y = } & { { } \quad 1 3 . 7 7 \mathrm { m } } \\ { \Delta Z = } & { { } \quad 4 . 7 8 \mathrm { m } } \\ { \Delta \dot { X } = } & { { } \quad - 0 . 0 0 9 9 5 3 \mathrm { m } / \mathrm { s } } \\ { \Delta \dot { Y } = } & { { } \quad 0 . 0 1 1 4 2 1 \mathrm { m } / \mathrm { s } } \\ { \Delta \dot { Z } = } & { { } \quad 0 . 0 0 5 7 1 8 \mathrm { m } / \mathrm { s } } \end{array}
$$

Note that the error at $t _ { 0 }$ propagated to $3 0 \mathrm { { m i n } }$ can also be obtained by adding the above initial error to the state, which results in

$$
\begin{array} { r l r } { X } & { = } & { 5 4 9 2 0 0 1 . 3 4 \mathrm { m } } \\ { Y } & { = } & { 3 9 8 4 0 0 3 . 4 0 \mathrm { m } } \\ { Z } & { = } & { 2 9 5 8 . 8 1 \mathrm { m } } \end{array}
$$

and no change in velocity. Following the procedure in Section 2.2.5, the predicted state at 1800 sec is

![](images/3b03b614718a527e4050fcc84c6f6777e96e54ce625155141d39de78af68d3c8.jpg)  
Figure 2.2.8: The RTN system: Radial (R), Transverse (T), and Normal (N).

Differencing this state with the predicted state in Section 2.2.5 produces the same error components obtained with the state transition matrix mapping. Since the differences are small in comparison to the total position magnitudes, the differential displacements in Eq. (2.2.38) are accurately approximated by the actual displacements. This aspect is discussed in Chapter 4 within the context of linear approximations.

For most applications, use of the $( X Y Z )$ coordinates to express the error is less revealing than other coordinate systems. An alternate system is shown in Fig. 2.2.8, in which unit vectors are defined in the radial (R) direction, transverse (T) direction, and normal $( \mathrm { N } )$ direction, referred to as the RTN system. To avoid ambiguity, these directions are specified by unit vectors $\mathbf { u } _ { r } , \mathbf { u } _ { t }$ , and $\mathbf { u } _ { n }$ , which are defined by

$$
\begin{array} { r } { \mathbf { r } = r \mathbf { u } _ { r } } \\ { \mathbf { h } = h \mathbf { u } _ { n } } \end{array}
$$

and $\mathbf { u } _ { t }$ completes the right-handed, orthogonal system.

A commonly used terminology for the RTN directions is: $\mathbf { u } _ { t }$ may be referred to as the along-track direction and $\mathbf { u } _ { n }$ may be referred to as the cross-track direc-

![](images/62346d359fa6e105541bee0b296314d1fd65b43c4f4a3b2d1d3eba449da1428d.jpg)  
Figure 2.2.9: Orbit error evolution in RTN directions. A radial perturbation of 1 meter at $t = 0$ was applied to the state vector in Example 2.2.4.1. The plot illustrates the $1 { - } \mathrm { m }$ radially perturbed orbit minus the unperturbed orbit (Example 2.2.4.1).

tion. In some definitions, the along-track direction may refer to the direction of the velocity vector, which coincides with the $\mathbf { u } _ { t }$ direction at every point only on a circular orbit. The ECI to RTN transformation is given by Eq. (4.16.21).

# Example 2.2.6.2

To illustrate the nature of the orbit error, Fig. 2.2.9 shows the evolution of orbit error for two orbital revolutions resulting from a 1-meter error in the radial direction for the Shuttle described in Example 2.2.4.1. The 1-meter error in the radial component (increase in radial component) at the initial time produces the perturbed position of

$$
\begin{array} { r l r } { X = } & { { } } & { 5 4 9 2 0 0 1 . 1 4 9 4 5 \mathrm { m } } \\ { Y = } & { { } } & { 3 9 8 4 0 0 1 . 9 8 7 1 9 \mathrm { m } } \\ { Z = } & { { } } & { 2 9 5 5 . 8 1 0 4 4 \mathrm { m } } \end{array}
$$

and no change in velocity. Figure 2.2.9 shows the evolution of this 1-meter radial error in (RTN)-components, where the components are defined as the perturbed orbit position minus the reference orbit defined by the state vector in Example 2.2.4.1. With $\mathbf { u } _ { t }$ defined by the reference orbit, the position on the perturbed orbit is about $- 4 0 \mathrm { ~ m ~ } \mathbf { u } _ { t }$ at $1 1 , 0 0 0 ~ \mathrm { s e c }$ ; that is, it “trails” the reference orbit by about $4 0 \mathrm { m }$ at this time. Since there is no out-of-plane perturbation of either position or velocity, the normal component is zero. Two significant characteristics are evident in the radial and transverse components. The transverse component exhibits a somewhat linear growth with time, or secular change. Furthermore, the existence of a periodic variation coinciding with the orbit period is evident in the radial and transverse components. This periodic variation is usually identified as a once per revolution variation. A more complete discussion is given by El´Yasberg (1967).

Further consideration of Fig. 2.2.9 explains the sign and periodicity in this figure. The increase in $r$ with no change in initial velocity results in an increase in semimajor axis and an increase in orbital period. With the difference in orbital period, a satellite in the unperturbed orbit must move ahead of a satellite in the perturbed orbit. Since the transverse component is defined as perturbed minus unperturbed, the component will be negative. It appears linear because of the linear dependence in time exhibited by Kepler’s Equation. The explanation of the periodic variation in this characteristic results from the difference in semimajor axis and eccentricity of the two orbits, which produces terms that are dependent on eccentric anomaly.

# 2.3 PERTURBED MOTION

The description of motion given in Section 2.2 is idealized. It has been obtained by assuming that only gravitational forces exist between two bodies, both of which have been further idealized by assuming them to be spheres that are gravitationally equivalent to point masses. The idealizations enable an analytical solution to the equations of motion and the motion can be interpreted as a simple geometrical figure (circle, ellipse, parabola, hyperbola). Because of the simple geometrical interpretation of the orbit, the idealized problem of two bodies provides a starting point for the interpretation of more realistic representations of the orbital motion.

Newton was well aware of the complexities surrounding the equations of motion that better represent the real world. He considered the gravitational problem of three bodies representing the Earth, Moon, and Sun, but he reportedly told his friend, the Royal Astronomer Halley, that the motion of the Moon “ma de his head ache and kept him awake so often that he would think of it no more” (Moulton, p. 363, 1914). The lunar problem (or the three-body problem) has no general, closed-form solution analogous to the conic section solution for the problem of two bodies (except for equilibrium solutions), but there are various ways of forming approximate solutions. Approximate analytical solutions use the problem of two bodies as a reference solution and expressions can be derived for the deviation, or perturbation, resulting from additional forces. These additional forces, that is, forces in addition to the point mass gravitation between two bodies, are referred to as perturbing forces. The analytical techniques used to obtain the approximate solutions are known as general perturbations.

With the advent of increasingly powerful digital computers, techniques that provide a numerical solution to the perturbed equations of motion have received increased attention as well. In these techniques, the equations of perturbed motion, represented by a set of ordinary differential equations, are solved numerically with specified initial conditions. These techniques are known as special perturbations. The procedures applied to the numerical integration of the equations of motion are described in most books on numerical analysis, but references such as Press et al. (1986) and Shampine and Gordon (1975) are good sources of applied information.

In the following sections, the contributions of various perturbing forces are summarized. These forces are separated into two categories: gravitational and nongravitational. The influenc e of these perturbing forces on the orbit is described in these sections.

# 2.3.1 CLASSICAL EXAMPLE: LUNAR PROBLEM

In spite of the notorious difficulty in solving the equations that describe the motion of the Moon, the problem can readily be solved by numerical integration. The results of the integration are instructive in describing the nature of perturbed motion and, additionally, the results are applicable to a further discussion of astronomical coordinate systems.

Following the approach used in the derivation of the equations of motion of two spheres given in Section 2.2, the equations of motion for three bodies that attract each other in accordance with Newtonian gravity can be derived in a similar manner. Let $M _ { 1 }$ , $M _ { 2 }$ , and $M _ { 3 }$ represent the masses of three spheres, each with constant and uniform density. The equations of motion for each body can be expressed using an inertial coordinate system. But it is useful (and instructive) to describe the motion of two of the bodies with respect to the third body, say $M _ { 1 }$ . The resulting equations of motion for $M _ { 2 }$ and $M _ { 3 }$ are as follows, where the

![](images/00f0ea176bb7b469d32d038725b0196b0854439649d4ed9ee0400eb911d7dd06.jpg)  
Figure 2.3.1: Vector definition for three bodies.

vectors are illustrated in Fig. 2.3.1:

$$
\begin{array} { r c l } { \displaystyle \ddot { \mathbf { r } } } & { = } & { \displaystyle - \frac { \mu \mathbf { r } } { r ^ { 3 } } + G M _ { 3 } \left( \frac { \Delta } { \Delta ^ { 3 } } - \frac { \mathbf { r } _ { p } } { r _ { p } ^ { 3 } } \right) } \\ { \displaystyle \ddot { \mathbf { r } } _ { p } } & { = } & { \displaystyle - \frac { \mu ^ { \prime } \mathbf { r } _ { p } } { r _ { p } ^ { 3 } } - G M _ { 2 } \left( \frac { \mathbf { r } } { r ^ { 3 } } + \frac { \Delta } { \Delta ^ { 3 } } \right) } \end{array}
$$

where $\mu = G ( M _ { 1 } + M _ { 2 } )$ and $\mu ^ { \prime } = G ( M _ { 1 } + M _ { 3 } )$ .

Let the bodies represent the Earth, Moon, and Sun, so that $M _ { 1 }$ is the Earth’s mass, $M _ { 2 }$ is the mass of the Moon, and $M _ { 3 }$ represents the Sun. This description is known as the problem of three bodies in celestial mechanics. The vector $\mathbf { r }$ represents the position vector of the Moon with respect to the Earth, $\pmb { \Delta }$ is the position vector of the Sun with respect to the Moon, and $\mathbf { r } _ { p }$ is the position vector of the Sun with respect to the Earth. Examination of the gravitational parameters of the Earth, Moon, and Sun as given in Appendix D shows that the mass of the Sun is more than 300,000 times greater than the Earth and the mass of the Moon is 81 times smaller than the Earth. An accurate approximation can be made in Eq. (2.3.2) by ignoring both the term with $G M _ { 2 }$ and $M _ { 1 }$ in $\mu ^ { \prime }$ . With these approximations, the motion of the Sun about the Earth (or vice versa) is described by two-body dynamics. This approximation is known as the restricted problem of three bodies, described in more detail by Szebehely (1967).

Equations (2.3.1) and (2.3.2) can be integrated using a numerical method (e.g., see Shampine and Gordon, 1975) with specified initial conditions. Since the Sun is a dominant perturbation of the lunar motion, it is more appropriate to use a different orientation of the $( X , Y , Z )$ axes. In this orientation, the $Z$ axis is perpendicular to the ecliptic instead of the equator (as defined in Section 2.2.3), but the $X$ axis is still directed to the vernal equinox. If the initial conditions in Table 2.3.1 are adopted, along with the mass parameters from Appendix D, the numerical integration of the equations for the Moon will produce an ephemeris, a table of time, position, and velocity. If the position and velocity vectors at each time are converted into orbit elements, referred to as osculating elements, using the equations in Section 2.2.4, the lunar inclination is illustrated in Fig. 2.3.2. The variation in the lunar ascending node is shown in Fig. 2.3.3 with respect to the vernal equinox over a period of one year. It is clearly evident from these figures that the orbit elements are not constant, which is the result of the influence of the gravitational perturbation of the Sun on the two bodies: Earth and Moon.

Table 2.3.1: Ecliptic Position and Velocity of Sun and Moon on January 1, 2000, 12 Hours   

<table><tr><td colspan="3">MOON</td></tr><tr><td>X=</td><td>-291608 km</td><td>X= 0.643531 km/sec</td></tr><tr><td>Y=</td><td>-274979 km</td><td>Y= -0.730984 km/sec</td></tr><tr><td>Z=</td><td>36271 km</td><td>2= -0.011506 km/sec</td></tr><tr><td colspan="3">SUN</td></tr><tr><td>X=</td><td>26499000 km</td><td>X= 29.794 km/sec</td></tr><tr><td>Y=</td><td>Y= -144697300 km</td><td>5.469 km/sec</td></tr><tr><td>Z=</td><td>0 km Z=</td><td>0 km/sec</td></tr></table>

Figures 2.3.2 and 2.3.3 exhibit some important features of perturbed motion. The ascending node location in Fig. 2.3.3 exhibits a linear variation with time, referred to as a secular variation, as well as periodic variations. The inclination also shows periodic variations, but no apparent secular variation. Close examination of the periodic variations show the existence of approximately 180-day and 14-day periods, half the orbital period of the Sun about the Earth, and half the orbital period of the Moon, respectively. These periods appear in the plot for the node as well, but the 14-day periods are less evident. The secular node rate is negative, thus the change is referred to as a regression of the node, with a rate of about 19.4 degrees per year. The line of nodes of the Moon’s orbit completes one revolution in 18.6 years, a fundamental period in the lunar motion that has been known since antiquity. Although less evident, other periodicities exist in the orbit element variations, including 28 days and 365 days, but the amplitudes of these terms are smaller and their effects are less evident in Figs. 2.3.2 and 2.3.3.

This example illustrates the influence that a perturbing force may have. An orbit element may exhibit secular variations, but it will also show periodic variations. The orbit elements that exhibit secular variations depend on the nature of the perturbing force, as do the specific periods associated with the periodic variations. The periodic variations are often loosely categorized as short-period perturbations or long-period perturbations. Depending on the nature of the perturbing forces, other periodicities may exist that do not fit these two categories, so other categories may be introduced to accommodate them. Furthermore, the period of a perturbation is not a definit ive statement regarding how a perturbation should be categorized. For example, “short period” usually refers to perturbations in the frequency spectrum that are integer or near-integer multiples of the mean orbital angular rate. There are usually several specific frequencies that are categorized as short-period, but all are near the mean orbital angular rate.

# 2.3.2 VARIATION OF PARAMETERS

As illustrated in the previous section, the influence of a perturbing force on an orbit can be illustrated through time variations of the elements. The temporal variations illustrated for the Moon suggest the development of differential equations for the elements, analogous to the process known as variation of parameters in the solution of ordinary differential equations. The differential equations of motion for the perturbed satellite problem can be expressed as

$$
{ \ddot { \mathbf { r } } } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } } + \mathbf { f } ,
$$

where $\mathbf { r }$ is the position vector of the satellite center of mass expressed in an appropriate reference frame and $\mathbf { f }$ is the perturbing force. The perturbing force f , or more correctly, the force per unit mass since f has acceleration units, can be further resolved into components in the RTN system (see Section 2.2.6),

$$
\mathbf { f } = { \hat { R } } \mathbf { u } _ { r } + { \hat { T } } \mathbf { u } _ { t } + { \hat { N } } \mathbf { u } _ { n }
$$

where the unit vectors are defined by the RTN directions and $\hat { R } , \hat { T } , \hat { N }$ represent the force components. Note in Eq. (2.3.3) that if $\mathbf { f } = 0$ , the resulting motion is two-body. Thus, f perturbs the two-body motion.

It can be shown that the equations of motion given by Eq. (2.3.3) can be equivalently expressed by a set of differential equations that describes the time rate of change of the orbit elements (Appendix D). For example, the rates of change of the node and inclination are

$$
\frac { d \Omega } { d t } = \frac { r \sin ( \omega + f ) \hat { N } } { h \sin i }
$$

![](images/b874e4de784ca82d5bce8918cd49cafdeeef5f3cf33948cd386ef3c3c53b9ed5.jpg)  
Figure 2.3.2: Time variation of the lunar inclination with respect to the ecliptic. Epoch: January 1, 2000, 12 hours.

$$
\frac { d i } { d t } = \frac { r \cos ( \omega + f ) { \hat { N } } } { h } .
$$

The solutions to the full set of equations give the six orbit elements as a function of time, from which position and velocity can be obtained from the equations in Section 2.2.4.

In some cases, the perturbing force, f , is derivable from a potential or disturbing function, $D$ . The equations for time variation of the orbit elements can be also expressed as a function of $D$ , as given in Appendix C. For example, the node and inclination are

$$
\begin{array} { r c l } { { \displaystyle \frac { d \Omega } { d t } } } & { { = } } & { { \displaystyle \frac { 1 } { h \sin i } \frac { \partial D } { \partial i } } } \\ { { \displaystyle \frac { d i } { d t } } } & { { = } } & { { \displaystyle \frac { 1 } { h \sin i } \left[ \cos i \frac { \partial D } { \partial \omega } - \frac { \partial D } { \partial \Omega } \right] . } } \end{array}
$$

The equations given by Eqs. (2.3.3), (2.3.5), and (2.3.6) are equivalent. That is, aside from errors introduced by the respective technique used to solve these equations, the solutions of the equations are identical for the same perturbing forces. Equation (2.3.6) is particularly useful in gaining insight into the nature of perturbed motion, whereas Eq. (2.3.3) is most often used for applications requiring high accuracy in the representation of f.

![](images/2745a615caf879975fbd164112807f7f170357748b956f9277b93ec7bf313c18.jpg)  
Figure 2.3.3: Time variation of the lunar node measured in the ecliptic. Epoch: January 1, 2000, 12 hours.

The perturbing force f in Eq. (2.3.3) can be categorized into two types of forces: gravitational and nongravitational. In the following sections, various sources that contribute to f are described.

# 2.3.3 GRAVITATIONAL PERTURBATIONS: MASS DISTRIBUTION

Consider the gravitational attraction between two point masses, $M _ { 1 }$ and $M _ { 2 }$ , separated by a distance $r$ . The gravitational potential between these two bodies, $U$ , can be expressed as

$$
U = { \frac { G M _ { 1 } M _ { 2 } } { r } } .
$$

The gravitational force on $M _ { 2 }$ resulting from the interaction with $M _ { 1 }$ can be derived from the potential as the gradient of $U$ ; that is,

$$
\mathbf { F } = \boldsymbol { \nabla } U = - { \frac { G M _ { 1 } M _ { 2 } \mathbf { r } } { r ^ { 3 } } }
$$

where $\mathbf { r }$ is the position vector of $M _ { 2 }$ with respect to $M _ { 1 }$ given by

$$
\mathbf { r } = x \mathbf { u } _ { x } + y \mathbf { u } _ { y } + z \mathbf { u } _ { z }
$$

![](images/7939f2a788285f2ed9c366d731c208facd4dcadc12d57cc82b33cc55b749acea.jpg)  
Figure 2.3.4: Definit ion of position vectors and differential mass for a body with arbitrary mass distribution.

and

$$
\nabla = \frac { \partial } { \partial x } { \mathbf u } _ { x } + \frac { \partial } { \partial y } { \mathbf u } _ { y } + \frac { \partial } { \partial z } { \mathbf u } _ { z } .
$$

If a body of total mass $M$ has an arbitrary distribution of mass, it can be modeled as the collection of a large number of point masses. The gravitational potential sensed by a point mass, $m ^ { \prime }$ , at an external location is

$$
U = m ^ { \prime } \int \int \int { \frac { G \gamma d x d y d z } { \rho } }
$$

where $\gamma$ is the mass density associated with an element of mass dm, dx dy $d z$ is the differential volume, and $\rho$ is the distance between the differential mass dm and the external mass $m ^ { \prime }$ (see Fig. 2.3.4). For convenience, the external mass is usually taken to be unity $( m ^ { \prime } = 1 \mathrm { ~ \AA ~ }$ ), and the integral expression is written in a more compact notation

$$
U = \int _ { M } { \frac { G d m } { \rho } }
$$

where the integral notation represents integration over the entire mass of the body. Equation (2.3.10) can be directly integrated for some bodies, such as a sphere of constant density $\gamma$ . This integration (see Danby, 1988) shows that the constant density sphere is gravitationally equivalent to a point mass.

The position vector of $m ^ { \prime }$ with respect to the coordinate system $( x , y , z )$ is $\mathbf { r }$ . The location of the origin, $O$ , and the orientation of $( x , y , z )$ is arbitrary; however, for convenience, the $( x , y , z )$ system is assumed to be body-fixed. Hence, the $( x , y , z )$ axes are fix ed in the body and rotate with it. For the Earth, as an example, the $( x , y )$ plane would coincide with the equator, with the $x$ axis also coinciding with the Greenwich meridian.

Equation (2.3.10) can be expanded into the infinite series

$$
U = \frac { G } { r } \int _ { M } \sum _ { \ell = 0 } ^ { \infty } \left( \frac { R } { r } \right) ^ { \ell } P _ { \ell } ( \cos S ) d m
$$

where $R$ is the distance between the origin $O$ and the differential mass $d m$ , and $P _ { \ell }$ is the Legendre polynomial of degree $\ell$ , with argument equal to the cosine of the angle between the two vectors, $\mathbf { R }$ and $\mathbf { r }$ . Using the decomposition formula (Heiskanen and Moritz, 1967, p. 33), the Legendre polynomial can be expanded into spherical harmonics and terms that are dependent on the mass distribution collected into coefficients to yield

$$
\begin{array} { r c l } { { U } } & { { = } } & { { \displaystyle { \frac { \mu } { r } } + U ^ { \prime } } } \\ { { U ^ { \prime } } } & { { = } } & { { \displaystyle - { \frac { \mu ^ { * } } { r } } \sum _ { \ell = 1 } ^ { \infty } \left( { \frac { a _ { e } } { r } } \right) ^ { \ell } P _ { \ell } ( \sin \phi ) J _ { \ell } } } \\ { { } } & { { } } & { { \displaystyle + { \frac { \mu ^ { * } } { r } } \sum _ { \ell = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \ell } \left( { \frac { a _ { e } } { r } } \right) ^ { \ell } P _ { \ell m } ( \sin \phi ) [ C _ { \ell m } \cos m \lambda + S _ { \ell m } \sin m \lambda ] } } \end{array}
$$

where the coordinates of $m ^ { \prime }$ are now expressed with spherical coordinates $( r _ { \cdot }$ , $\phi , \lambda )$ . Scale factors involving a reference mass $( \mu ^ { * } = G M ^ { * } )$ ) and a reference distance $( a _ { e } )$ have been introduced to nondimensionalize the mass property coefficients , $C _ { \ell m }$ and $S _ { \ell m }$ . The decomposition formula has introduced Legendre’s Associated Functions, $P _ { \ell m }$ , of degree $\ell$ and order m. The spherical coordinate $\phi$ represents a geocentric latitude and $\lambda$ represents a longitude angle. The relations between the spherical coordinates and $( x , y , z )$ are given by Eq. (2.2.37).

The coeffici ents $J _ { \ell } , C _ { \ell m }$ , and $S _ { \ell m }$ are referred to as spherical harmonic coefficients , or Stokes coefficients , representing mass properties of the body. For example, $J _ { \ell }$ is given by

$$
J _ { \ell } = - \left( \frac { 1 } { M ^ { * } a _ { e } ^ { \ell } } \right) \int _ { M } R ^ { \ell } P _ { \ell } ( \sin \phi ^ { \prime } ) d m
$$

where $\phi ^ { \prime }$ is the geocentric latitude of the differential mass $d m$ , $M ^ { * }$ is usually taken to be the mass of the body, and $a _ { e }$ is its mean equatorial radius. The Legendre polynomial $P _ { \ell }$ equals $P _ { \ell , 0 }$ . The similar expressions for $C _ { \ell m }$ and $S _ { \ell m }$ are dependent on the longitude of the differential mass. Note that if the body is rigid and the $( x , y , z )$ system is fix ed in the body, then the $J _ { \ell }$ , $C _ { \ell m }$ , and $S _ { \ell m }$ coeffic ients will be constant. On the other hand, if $( x , y , z )$ is not body-fix ed or if temporal redistribution of mass takes place, the coefficients will be time-dependent.

The $J _ { \ell }$ coefficient s are referred to as zonal harmonics, which are related to $C _ { \ell m }$ by the relation $J _ { \ell } = - C _ { \ell , 0 }$ . The $C _ { \ell m }$ and $S _ { \ell m }$ terms are named according to the values of $\ell$ and $m$ . If $\ell \neq m$ , the $C _ { \ell m }$ and $S _ { \ell m }$ coefficients are referred to as tesseral harmonics and if $\ell = m$ , they are referred to as sectoral harmonics. The terminology is derived from the fact that the $J _ { \ell }$ terms are independent of longitude and the zeroes of $P _ { \ell }$ can be visualized as dividing the body into zones of latitude. Similarly, when $\ell = m$ , the coefficients divide the body into sectors defined by longitude. The number of sectors is determined by $m$ . Additional descriptions are given by Heiskanen and Moritz (1967).

An alternate formulation for the gravitational potential uses normalized Legendre functions and coefficients. The Legendre functions for high degree acquire large numerical values and the mass coefficients are very small. The normalization process results in a set of mass coefficients, usually identified as $\overline { { C } } _ { \ell m }$ and $\overline { { S } } _ { \ell m }$ , with the same order of magnitude over a wide range of $\ell$ and $m$ . For the Earth, a set of mass coefficients is given in Appendix D along with the relations between normalized coefficients and conventional coefficients. Note that if normalized coefficients are used, a normalized set of Legendre functions must be used also.

Recursive expressions for the generation of both conventional and normalized expressions are given by Lundberg and Schutz (1988). The recursive expression for the conventional Legendre polynomial, $P _ { \ell } ( \sin \phi )$ , is

$$
P _ { \ell } ( \sin \phi ) = \bigl [ ( 2 \ell - 1 ) \sin \phi P _ { \ell - 1 } ( \sin \phi ) - ( \ell - 1 ) P _ { \ell - 2 } ( \sin \phi ) \bigr ] / \ell
$$

where $P _ { 0 } ( \sin \phi ) = 1$ and $P _ { 1 } ( \sin \phi ) = \sin \phi$ . The recursions for the conventional Legendre Associated Functions are

$$
P _ { \ell , \ell } ( \sin \phi ) = ( 2 \ell - 1 ) \cos \phi P _ { \ell - 1 , \ell - 1 } ( \sin \phi )
$$

where $P _ { 1 , 1 } ( \sin \phi ) = \cos \phi$ . Furthermore, for $l \neq m$

$$
P _ { \ell , m } ( \sin \phi ) = \left[ ( 2 \ell - 1 ) \sin \phi P _ { \ell - 1 , m } ( \sin \phi ) - ( \ell + m - 1 ) P _ { \ell - 2 , m } \right] / ( \ell - m )
$$

where $P _ { i , j } = 0$ if $j > i$ . In addition, note the following recursions:

$$
\begin{array} { r c l } { { \sin m \lambda } } & { { = } } & { { 2 \cos \lambda \sin ( m - 1 ) \lambda - \sin ( m - 2 ) \lambda } } \\ { { \cos m \lambda } } & { { = } } & { { 2 \cos \lambda \cos ( m - 1 ) \lambda - \cos ( m - 2 ) \lambda . } } \end{array}
$$

It can be shown that the degree one terms $( J _ { 1 } , C _ { 1 , 1 }$ , and $S _ { 1 , 1 }$ ) are proportional to the distance that the origin $O$ is offset from the center of mass of the body. If the origin $O$ coincides with the center of mass, the degree one terms will be zero.

In the case of the Earth, the center of mass origin usually is referred to as the geocenter. Furthermore, it can be shown that the degree two terms are proportional to the moments and products of inertia of the body and their combinations:

$$
\begin{array} { c } { { J _ { 2 } = \displaystyle \frac { 2 C - B - A } { 2 M a _ { e } ^ { 2 } } } } \\ { { { } } } \\ { { C _ { 2 , 1 } = \displaystyle \frac { I _ { x z } } { M a _ { e } ^ { 2 } } { \quad } S _ { 2 , 1 } = \displaystyle \frac { I _ { y z } } { M a _ { e } ^ { 2 } } { } } } \\ { { { } } } \\ { { C _ { 2 , 2 } = \displaystyle \frac { B - A } { 4 M a _ { e } ^ { 2 } } { \quad } S _ { 2 , 2 } = \displaystyle \frac { I _ { x y } } { 2 M a _ { e } ^ { 2 } } } } \end{array}
$$

where $A$ and $B$ are equatorial moments of inertia $\scriptstyle \cdot$ and $y$ axes); $C$ is the polar moment of inertia $z$ axis); $I _ { x y } , I _ { x z }$ , and $I _ { y z }$ are the products of inertia; $M$ is the mass of the body; and $a _ { e }$ is the mean radius.

$\mathbf { F } ^ { * }$ , experienced by $m ^ { \prime }$ , can be expressed as

$$
\mathbf { F } ^ { * } = m ^ { \prime } \nabla U
$$

and the equations of motion for $m ^ { \prime }$ can be shown to be

$$
\ddot { \bf r } = \left( 1 + \frac { m ^ { \prime } } { M } \right) \nabla U .
$$

However, if $m ^ { \prime }$ represents an artific ial satellite of the Earth, $m ^ { \prime } / M$ is very small, and this equation becomes

$$
\ddot { \mathbf { r } } = \nabla U = - \frac { \mu \mathbf { r } } { r ^ { 3 } } + \mathbf { f } _ { N S }
$$

where $\mathbf { f } _ { N S }$ denotes the contribution from the nonspherical $U ^ { \prime }$ terms; that is, $\boldsymbol { \nabla } U ^ { \prime }$ . Integration of these equations, even with a numerical method, requires some careful consideration. The acceleration term, $\ddot { \mathbf { r } }$ , can be expressed in either a bodyfix ed, rotating system $( x , y , z )$ or a nonrotating system $( X , Y , Z )$ . However, the gravitational potential is expressed using spherical coordinates, presumed to be defined using a body-fix ed coordinate system so that the mass property coefficients are constant (at least for a rigid body). Thus,

$$
\pmb { \nabla } U = \frac { \partial U } { \partial r } \mathbf { u } _ { r } + \frac { 1 } { r } \frac { \partial U } { \partial \phi } \mathbf { u } _ { \phi } + \frac { 1 } { r \cos \phi } \frac { \partial U } { \partial \lambda } \mathbf { u } _ { \lambda } .
$$

Although Eq. (2.3.18) contains a singularity at the poles, which poses a problem for exactly polar orbits, alternate formulations exist that remove this singularity (e.g., Pines, 1973). If the body-fix ed system is chosen to represent $\mathbf { r }$ , then $\ddot { \mathbf { r } }$ will