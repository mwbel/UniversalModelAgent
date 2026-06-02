# RichardL.Burden J. Douglas Faires

# Numerical Analysis

# Solution Manual

Ninth Edition

# Instructor’s Solutions Manual

# for Numerical Analysis 9th EDITION

Richard L. Burden Youngstown State University

J. Douglas Faires Youngstown State University

Prepared by

Richard L. Burden Youngstown State University

J. Douglas Faires Youngstown State University $\circledcirc$ 2011 Brooks/Cole, Cengage Learning

ALL RIGHTS RESERVED. No part of this work covered by the copyright herein may be reproduced, transmitted, stored, or used in any form or by any means graphic, electronic, or mechanical, including but not limited to photocopying, recording, scanning, digitizing, taping, Web distribution, information networks, or information storage and retrieval systems, except as permitted under Section 107 or 108 of the 1976 United States Copyright Act, without the prior written permission of the publisher except as may be permitted by the license terms below.

For product information and technology assistance, contact us at Cengage Learning Customer & Sales Support, 1-800-354-9706

For permission to use material from this text or product, submit all requests online at www.cengage.com/permissions Further permissions questions can be emailed to permissionrequest@cengage.com

ISBN-13: 978-0-538-73596-4   
ISBN-10: 0-538-73596-1

Brooks/Cole   
20 Channel Center Street   
Boston, MA 02210   
USA

Cengage Learning is a leading provider of customized learning solutions with office locations around the globe, including Singapore, the United Kingdom, Australia, Mexico, Brazil, and Japan. Locate your local office at: international.cengage.com/region

Cengage Learning products are represented in Canada by Nelson Education, Ltd.

For your course and learning solutions, visit academic.cengage.com

Purchase any of our products at your local college store or at our preferred online store www.ichapters.com

NOTE: UNDER NO CIRCUMSTANCES MAY THIS MATERIAL OR ANY PORTION THEREOF BE SOLD, LICENSED, AUCTIONED, OR OTHERWISE REDISTRIBUTED EXCEPT AS MAY BE PERMITTED BY THE LICENSE TERMS HEREIN.

# READ IMPORTANT LICENSE INFORMATION

Dear Professor or Other Supplement Recipient:

Cengage Learning has provided you with this product (the “Supplement”) for your review and, to the extent that you adopt the associated textbook for use in connection with your course (the “Course”), you and your students who purchase the textbook may use the Supplement as described below. Cengage Learning has established these use limitations in response to concerns raised by authors, professors, and other users regarding the pedagogical problems stemming from unlimited distribution of Supplements.

Cengage Learning hereby grants you a nontransferable license to use the Supplement in connection with the Course, subject to the following conditions. The Supplement is for your personal, noncommercial use only and may not be reproduced, posted electronically or distributed, except that portions of the Supplement may be provided to your students IN PRINT FORM ONLY in connection with your instruction of the Course, so long as such students are advised that they

may not copy or distribute any portion of the Supplement to any third party. You may not sell, license, auction, or otherwise redistribute the Supplement in any form. We ask that you take reasonable steps to protect the Supplement from unauthorized use, reproduction, or distribution. Your use of the Supplement indicates your acceptance of the conditions set forth in this Agreement. If you do not accept these conditions, you must return the Supplement unused within 30 days of receipt.

All rights (including without limitation, copyrights, patents, and trade secrets) in the Supplement are and will remain the sole and exclusive property of Cengage Learning and/or its licensors. The Supplement is furnished by Cengage Learning on an “as is” basis without any warranties, express or implied. This Agreement will be governed by and construed pursuant to the laws of the State of New York, without regard to such State’s conflict of law rules.

Thank you for your assistance in helping to safeguard the integrity of the content contained in this Supplement. We trust you find the Supplement a useful teaching tool.

# Table of Contents

# Preface vii

# Mathematical Preliminaries 1

Exercise Set 1.1 . 1   
Exercise Set 1.2 . 6   
Exercise Set 1.3 . 12

# Solutions of Equations of One Variable 19

# Exercise Set 2.1 19

Exercise Set 2.2 . 22   
Exercise Set 2.3 . 26   
Exercise Set 2.4 . 31   
Exercise Set 2.5 . 34   
Exercise Set 2.6 . 36

# Interpolation and Polynomial Approximation 41

# Exercise Set 3.1 . 41

Exercise Set 3.2 . 47   
Exercise Set 3.3 . 49   
Exercise Set 3.4 . 52   
Exercise Set 3.5 . 56   
Exercise Set 3.6 . 68

# Numerical Differentiation and Integration 71

# Exercise Set 4.1 71

Exercise Set 4.2 . 78   
Exercise Set 4.3 . 82   
Exercise Set 4.4 . 87   
Exercise Set 4.5 . 91   
Exercise Set 4.6 . 94   
Exercise Set 4.7 . 96   
Exercise Set 4.8 . 99   
Exercise Set 4.9 . 101

# Initial-Value Problems for Ordinary Differential Equations 105

# Exercise Set 5.1 . 105

Exercise Set 5.2 . 108   
Exercise Set 5.3 . 113   
Exercise Set 5.4 . 119   
Exercise Set 5.5 . 129   
Exercise Set 5.6 . 133   
Exercise Set 5.7 . 144   
Exercise Set 5.8 . 149   
Exercise Set 5.9 . 152   
Exercise Set 5.10 159

# Direct Methods for Solving Linear Systems 169

Exercise Set 6.1 . 169   
Exercise Set 6.2 . 174   
Exercise Set 6.3 . 180   
Exercise Set 6.4 . 188   
Exercise Set 6.1 . 190   
Exercise Set 6.6 . 194

# Iterative Techniques in Matrix Algebra 201

# Exercise Set 7.1 . 201

Exercise Set 7.2 . 206   
Exercise Set 7.3 . 209   
Exercise Set 7.4 . 215   
Exercise Set 7.5 . 219   
Exercise Set 7.6 . 221

# Approximation Theory 231

# Exercise Set 8.1 231

Exercise Set 8.2 . 232   
Exercise Set 8.3 . 236   
Exercise Set 8.4 . 238   
Exercise Set 8.5 . 244   
Exercise Set 8.6 . 247

# Approximating Eigenvalues 251

# Exercise Set 9.1 251

Exercise Set 9.2 . 257   
Exercise Set 9.3 . 262   
Exercise Set 9.4 . 266   
Exercise Set 9.5 . 267   
Exercise Set 9.6 . 273

# Numerical Solutions of Nonlinear Systems of Equations 281

Exercise Set 10.1 281   
Exercise Set 10.2 284   
Exercise Set 10.3 287   
Exercise Set 10.4 290   
Exercise Set 10.5 291

# Boundary-Value Problems for Ordinary Differential Equations 295

Exercise Set 11.1 295   
Exercise Set 11.2 299   
Exercise Set 11.3 303   
Exercise Set 11.4 308   
Exercise Set 11.5 313

# Numerical Solutions to Partial Differential Equations 319

Exercise Set 12.1 319   
Exercise Set 12.2 323   
Exercise Set 12.3 333   
Exercise Set 12.4 336

# Preface

This Instructor’s Manual for the Ninth Edition of Numerical Analysis by Burden and Faires contains solutions to all the exercises in the book. Although the answers to the odd exercises are also in the back of the text, we have found that users of the book appreciate having all the solutions in one source. In addition, the results listed in this Instructor’s Manual often go beyond those given in the back of the book. For example, we do not place the long solutions to theoretical and applied exercises in the book. You will find them here.

A Student Study Guide for the Ninth Edition of Numerical Analysis is also available and the solutions given in the Guide are generally more detailed than those in the Instructor’s Manual. In order to make it convenient for instructors, we have placed an asterisk ( $^ *$ ) in this Manual in front of each exercise whose solution is given in the Student Study Guide. Hopefully this will help with your homework assignments and test problems.

We have added a number of exercises to the text that involve the use of a Computer Algebra System. We have chosen Maple as our standard, because their Numerical-Analysis package parallels the algorithms in this book, but any of these systems can be used. In our recent teaching of the course we found that students understood the concepts better when they worked through the algorithms step-by-step, but let the computer algebra system do the tedious computation.

It has been our practice to include structured algorithms in our Numerical Analysis book for all the techniques discussed in the text. The algorithms are given in a form that can be coded in any appropriate programming language, by students with even a minimal amount of programming expertise.

At our website for the book, http://www.math.ysu.edu/ $\sim$ faires/Numerical-Analysis/ you will find all the algorithms written in the programming languages FORTRAN, Pascal, C, Java, as well as in the Computer Algebra Systems, Maple, MATLAB, and Mathematica. For the Ninth Edition, we have added new Maple programs to reflect the changes in their system and to include portions of their NumericalAnalysis package.

The website also contains additional information about the book and will be updated regularly to reflect any modifications that might be made. For example, we will place there any responses to questions from users of the book concerning interpretations of the exercises and appropriate applications of the techniques.

We will have a set of presentation material ready soon for many of the methods in the book. These are being constructed by Professor John Carroll of Dublin City University using the Beamer package of LATEX, and will be placed on the website. The Beamer package creates PDF files that are similar to Power Point presentations but incorporates mathematical elements easily and correctly. We are quite excited about this material and expect to have many of the presentations ready before they would normally be covered in the Fall term of 2010. If you send us an e-mail we will keep you posted on our progress.

We hope our supplement package provides flexibility for instructors teaching Numerical Analysis. If you have any suggestions for improvements that can be incorporated into future editions of the book or the supplements, we would be most grateful to receive your comments. We can be most easily contacted by electronic mail at the addresses listed below.

Youngstown State University

Richard L. Burden burden@math.ysu.edu

# Mathematical Preliminaries

Note: An asterisk ( $^ *$ ) before an exercise indicates that there is a solution in the Student Study Guide.

# Exercise Set 1.1, page 14

$^ * 1$ . For each part, $f \in C [ a , b ]$ on the given interval. Since $f ( a )$ and $f ( b )$ are of opposite sign, the Intermediate Value Theorem implies that a number $c$ exists with $f ( c ) = 0$ .

2. (a) $[ 0 , 1 ]$ (b) [0, 1], [4, 5], $[ - 1 , 0 ]$ \*(c) $[ - 2 , - 2 / 3 ]$ , [0, 1], [2, 4] (d) $[ - 3 , - 2 ]$ , [−1, −0.5], and [−0.5, 0]

3. For each part, $f \in C [ a , b ]$ , $f ^ { \prime }$ exists on $( a , b )$ and $f ( a ) = f ( b ) = 0$ . Rolle’s Theorem implies that a number $c$ exists in $( a , b )$ with $f ^ { \prime } ( c ) = 0$ . For part (d), we can use $[ a , b ] = [ - 1 , 0 ]$ or $[ a , b ] = [ 0 , 2 ]$ .

4. The maximum value for $| f ( x ) |$ is given below.

\*(a) $( 2 \ln 2 ) / 3 \approx 0 . 4 6 2 0 9 8 1$   
(b) 0.8   
(c) 5.164000   
(d) 1.582572

$^ { * } 5$ . For $x < 0$ , $f ( x ) < 2 x + k < 0$ , provided that $x < - { \textstyle { \frac { 1 } { 2 } } } k$ . Similarly, for $x > 0$ , $f ( x ) > 2 x + k > 0$ , provided that $x > - { \textstyle { \frac { 1 } { 2 } } } k$ . By Theorem 1.11, there exists a number $c$ with $f ( c ) = 0$ . If $f ( c ) = 0$ and $f ( c ^ { \prime } ) = 0$ for some $c ^ { \prime } \neq c$ , then by Theorem 1.7, there exists a number $p$ between $c$ and $c ^ { \prime }$ with $f ^ { \prime } ( p ) = 0$ . However, $f ^ { \prime } ( x ) = 3 x ^ { 2 } + 2 > 0$ for all $x$ .

6. Suppose $p$ and $q$ are in $[ a , b ]$ with $p \neq q$ and $f ( p ) = f ( q ) = 0$ . By the Mean Value Theorem, there exists $\xi \in ( a , b )$ with

$$
f ( p ) - f ( q ) = f ^ { \prime } ( \xi ) ( p - q ) .
$$

But, $f ( p ) - f ( q ) = 0$ and $p \neq q$ . So $f ^ { \prime } ( \xi ) = 0$ , contradicting the hypothesis.

7. (a) $P _ { 2 } ( x ) = 0$ (b) $R _ { 2 } ( 0 . 5 ) = 0 . 1 2 5$ ; actual error = 0.125

8. $\begin{array} { r } { P _ { 3 } ( x ) = 1 + \frac { 1 } { 2 } x - \frac { 1 } { 8 } x ^ { 2 } + \frac { 1 } { 1 6 } x ^ { 3 } } \end{array}$

<table><tr><td>C</td><td>0.5</td><td>0.75</td><td>1.25</td><td>1.5</td></tr><tr><td>P(x)</td><td>1.2265625</td><td>1.3310547</td><td>1.5517578</td><td>1.6796875</td></tr><tr><td>Vx+1</td><td>1.2247449</td><td>1.3228757</td><td>1.5</td><td>1.5811388</td></tr><tr><td>|vx+1-P3(x)l</td><td>0.0018176</td><td>0.0081790</td><td>0.0517578</td><td>0.0985487</td></tr></table>

$^ { * } 9$ . Since

$$
P _ { 2 } ( x ) = 1 + x \quad { \mathrm { a n d } } \quad R _ { 2 } ( x ) = { \frac { - 2 e ^ { \xi } ( \sin \xi + \cos \xi ) } { 6 } } x ^ { 3 }
$$

for some $\xi$ between $x$ and $0$ , we have the following:

(a) $P _ { 2 } ( 0 . 5 ) = 1 . 5$ and $| f ( 0 . 5 ) - P _ { 2 } ( 0 . 5 ) | \le 0 . 0 9 3 2$ ;   
(b) $| f ( x ) - P _ { 2 } ( x ) | \le 1 . 2 5 2$ ;   
(c) $\textstyle \int _ { 0 } ^ { 1 } f ( x ) \ d x \approx 1 . 5$ ;   
(d) $\begin{array} { r } { \mid \int _ { 0 } ^ { 1 } f ( x ) \ d x - \int _ { 0 } ^ { 1 } P _ { 2 } ( x ) \ d x \mid \leq \int _ { 0 } ^ { 1 } | R _ { 2 } ( x ) | d x \leq 0 . 3 1 3 } \end{array}$ , and the actual error is 0.122.

10. $\begin{array} { r } { P _ { 2 } ( x ) = 1 . 4 6 1 9 3 0 + 0 . 6 1 7 8 8 4 \left( x - \frac { \pi } { 6 } \right) - 0 . 8 4 4 0 4 6 \left( x - \frac { \pi } { 6 } \right) ^ { 2 } } \end{array}$ and R2(x) = − 13 eξ(sin ξ+cos ξ)  x − π6 3 for some $\xi$ between $x$ and $\textstyle { \frac { n } { 6 } }$ .

(a) $P _ { 2 } ( 0 . 5 ) = 1 . 4 4 6 8 7 9$ and $f ( 0 . 5 ) = 1 . 4 4 6 8 8 9$ . An error bound is $1 . 0 1 \times 1 0 ^ { - 5 }$ , and the actual error is $1 . 0 \times 1 0 ^ { - 5 }$ .   
(b) $| f ( x ) - P _ { 2 } ( x ) | \leq 0 . 1 3 5 3 7 2$ on $[ 0 , 1 ]$   
(c) $\textstyle \int _ { 0 } ^ { 1 } P _ { 2 } ( x ) \ d x = 1 . 3 7 6 5 4 2$ and $\textstyle \int _ { 0 } ^ { 1 } f ( x ) \ d x = 1 . 3 7 8 0 2 5$   
(d) An error bound is $7 . 4 0 3 \times 1 0 ^ { - 3 }$ , and the actual error is $1 . 4 8 3 \times 1 0 ^ { - 3 }$ .

11. $P _ { 3 } ( x ) = ( x - 1 ) ^ { 2 } - { \textstyle { \frac { 1 } { 2 } } } ( x - 1 ) ^ { 3 }$

(a) $P _ { 3 } ( 0 . 5 ) = 0 . 3 1 2 5 0 0$ , $f ( 0 . 5 ) = 0 . 3 4 6 5 7 4$ . An error bound is $\phantom { - } 0 . 2 9 1 \overline { { 6 } }$ , and the actual error is 0.034074.   
(b) $| f ( x ) - P _ { 3 } ( x ) | \leq 0 . 2 9 1 6$ on [0.5, 1.5]   
(c) $\begin{array} { r } { \int _ { 0 . 5 } ^ { 1 . 5 } P _ { 3 } ( x ) \ d x = 0 . 0 8 \overline { { 3 } } . } \end{array}$ $\textstyle \int _ { 0 . 5 } ^ { 1 . 5 } ( x - 1 ) \ln x \ d x = 0 . 0 8 8 0 2 0$   
(d) An error bound is $0 . 0 5 8 { \overline { { 3 } } }$ , and the actual error is $4 . 6 8 7 \times 1 0 ^ { - 3 }$ .

12. (a) $P _ { 3 } ( x ) = - 4 + 6 x - x ^ { 2 } - 4 x ^ { 3 }$ ; $P _ { 3 } ( 0 . 4 ) = - 2 . 0 1 6$ (b) $| R _ { 3 } ( 0 . 4 ) | \leq 0 . 0 5 8 4 9$ ; $| f ( 0 . 4 ) - P _ { 3 } ( 0 . 4 ) | = 0 . 0 1 3 3 6 5 3 6 7$ (c) $P _ { 4 } ( x ) = - 4 + 6 x - x ^ { 2 } - 4 x ^ { 3 }$ ; $P _ { 4 } ( 0 . 4 ) = - 2 . 0 1 6$ (d) $| R _ { 4 } ( 0 . 4 ) | \leq 0 . 0 1 3 6 6$ ; $| f ( 0 . 4 ) - P _ { 4 } ( 0 . 4 ) | = 0 . 0 1 3 3 6 5 3 6 7$

13. $P _ { 4 } ( x ) = x + x ^ { 3 }$

(a) $| f ( x ) - P _ { 4 } ( x ) | \leq 0 . 0 1 2 4 0 5$   
(b) $\textstyle \int _ { 0 } ^ { 0 . 4 } P _ { 4 } ( x ) \ d x = 0 . 0 8 6 4$ , $\textstyle \int _ { 0 } ^ { 0 . 4 } x e ^ { x ^ { 2 } } \ d x = 0 . 0 8 6 7 5 5$   
(c) $8 . 2 7 \times 1 0 ^ { - 4 }$   
(d) $P _ { 4 } ^ { \prime } ( 0 . 2 ) = 1 . 1 2$ , $f ^ { \prime } ( 0 . 2 ) = 1 . 1 2 4 0 7 6$ . The actual error is $4 . 0 7 6 \times 1 0 ^ { - 3 }$ .

$^ *$ 14. First we need to convert the degree measure for the sine function to radians. We have $1 8 0 ^ { \circ } = \pi$ radians, so $1 ^ { \circ } = \frac { \pi } { 1 8 0 }$ radians. Since,

$$
f ( x ) = \sin x , \quad f ^ { \prime } ( x ) = \cos x , \quad f ^ { \prime \prime } ( x ) = - \sin x , \quad { \mathrm { a n d } } \quad f ^ { \prime \prime \prime } ( x ) = - \cos x ,
$$

we have $f ( 0 ) = 0$ , $f ^ { \prime } ( 0 ) = 1$ , and $f ^ { \prime \prime } ( 0 ) = 0$ .

The approximation $\sin x \approx x$ is given by

$$
f ( x ) \approx P _ { 2 } ( x ) = x , \quad \mathrm { a n d } \quad R _ { 2 } ( x ) = - \frac { \cos \xi } { 3 ! } x ^ { 3 } .
$$

If we use the bound $| \cos \xi | \le 1$ , then

$$
\left| \sin { \frac { \pi } { 1 8 0 } } - { \frac { \pi } { 1 8 0 } } \right| = \left| R _ { 2 } \left( { \frac { \pi } { 1 8 0 } } \right) \right| = \left| { \frac { - \cos \xi } { 3 ! } } \left( { \frac { \pi } { 1 8 0 } } \right) ^ { 3 } \right| \leq 8 . 8 6 \times 1 0 ^ { - 7 } .
$$

15. Since $4 2 ^ { \circ } = 7 \pi / 3 0$ radians, use $x _ { 0 } = \pi / 4$ . Then

$$
\left| R _ { n } \left( { \frac { 7 \pi } { 3 0 } } \right) \right| \leq { \frac { \left( { \frac { \pi } { 4 } } - { \frac { 7 \pi } { 3 0 } } \right) ^ { n + 1 } } { ( n + 1 ) ! } } < { \frac { ( 0 . 0 5 3 ) ^ { n + 1 } } { ( n + 1 ) ! } } .
$$

For $| R _ { n } ( \frac { 7 \pi } { 3 0 } ) | < 1 0 ^ { - 6 }$ , it suffices to take $n = 3$ . To 7 digits,

$$
\cos 4 2 ^ { \circ } = 0 . 7 4 3 1 4 4 8 \quad { \mathrm { a n d } } \quad P _ { 3 } ( 4 2 ^ { \circ } ) = P _ { 3 } ( { \frac { 7 \pi } { 3 0 } } ) = 0 . 7 4 3 1 4 4 6 ,
$$

so the actual error is $2 \times 1 0 ^ { - 7 }$ .

$^ { * } 1 6$ . (a) $P _ { 3 } ( x ) = \frac { 1 } { 3 } x + \frac { 1 } { 6 } x ^ { 2 } + \frac { 2 3 } { 6 4 8 } x ^ { 3 }$ (b) We have

$$
f ^ { ( 4 ) } ( x ) = \frac { - 1 1 9 } { 1 2 9 6 } e ^ { x / 2 } \sin \frac { x } { 3 } + \frac { 5 } { 5 4 } e ^ { x / 2 } \cos \frac { x } { 3 } ,
$$

so

$$
{ \biggl | } f ^ { ( 4 ) } ( x ) { \biggr | } \leq { \Bigl | } f ^ { ( 4 ) } ( 0 . 6 0 4 7 3 8 9 1 ) { \Bigr | } \leq 0 . 0 9 7 8 7 1 7 6 , \quad { \mathrm { f o r ~ } } 0 \leq x \leq 1 ,
$$

and

$$
| f ( x ) - P _ { 3 } ( x ) | \leq \frac { \left| f ^ { ( 4 ) } ( \xi ) \right| } { 4 ! } | x | ^ { 4 } \leq \frac { 0 . 0 9 7 8 7 1 7 6 } { 2 4 } ( 1 ) ^ { 4 } = 0 . 0 0 4 0 7 7 9 9 0 .
$$

17. (a) $\begin{array} { r } { P _ { 3 } ( x ) = \ln ( 3 ) + \frac { 2 } { 3 } ( x - 1 ) + \frac { 1 } { 9 } ( x - 1 ) ^ { 2 } - \frac { 1 0 } { 8 1 } ( x - 1 ) ^ { 3 } } \end{array}$ (b) $\begin{array} { r } { \operatorname* { m a x } _ { 0 \leq x \leq 1 } | f ( x ) - P _ { 3 } ( x ) | = | f ( 0 ) - P _ { 3 } ( 0 ) | = 0 . 0 2 6 6 3 3 6 6 } \end{array}$ (c) $\begin{array} { r } { \tilde { P } _ { 3 } ( x ) = \ln ( 2 ) + \frac { 1 } { 2 } x ^ { 2 } } \end{array}$ (d) $\begin{array} { r } { \operatorname* { m a x } _ { 0 \leq x \leq 1 } | f ( x ) - \tilde { P } _ { 3 } ( x ) | = | f ( 1 ) - \tilde { P } _ { 3 } ( 1 ) | = 0 . 0 9 4 5 3 4 8 9 } \end{array}$ (e) $P _ { 3 } ( 0 )$ approximates $f ( 0 )$ better than $\bar { P } _ { 3 } ( 1 )$ approximates $f ( 1 )$ .

18. $\textstyle P _ { n } ( x ) = \sum _ { k = 0 } ^ { n } x ^ { k } , \ n \geq 1 9$

19. $P _ { n } ( x ) = \sum _ { k = 0 } ^ { n } { \frac { 1 } { k ! } } x ^ { k } , \ n \geq 7$

20. For $n$ odd, $P _ { n } ( x ) = x - { \textstyle { \frac { 1 } { 3 } } } x ^ { 3 } + { \textstyle { \frac { 1 } { 5 } } } x ^ { 5 } + \cdot \cdot \cdot + { \textstyle { \frac { 1 } { n } } } ( - 1 ) ^ { ( n - 1 ) / 2 } x ^ { n }$ . For $n$ even, $P _ { n } ( x ) = P _ { n - 1 } ( x )$ .

21. A bound for the maximum error is 0.0026.

22. (a) $P _ { n } ^ { ( k ) } ( x _ { 0 } ) = f ^ { ( k ) } ( x _ { 0 } )$ for $k = 0 , 1 , \ldots , n$ . The shapes of $P _ { n }$ and $f$ are the same at $x _ { 0 }$ . (b) $P _ { 2 } ( x ) = 3 + 4 ( x - 1 ) + 3 ( x - 1 ) ^ { 2 }$ .   
23. (a) The assumption is that $f ( x _ { i } ) = 0$ for each $i = 0 , 1 , \ldots , n$ . Applying Rolle’s Theorem on each on the intervals $[ x _ { i } , x _ { i + 1 } ]$ implies that for each $i = 0 , 1 , \ldots , n - 1$ there exists a number $z _ { i }$ with $f ^ { \prime } ( z _ { i } ) = 0$ . In addition, we have $a \leq x _ { 0 } < z _ { 0 } < x _ { 1 } < z _ { 1 } < \cdot \cdot \cdot < z _ { n - 1 } < x _ { n } \leq b .$ (b) Apply the logic in part (a) to the function $g ( x ) = f ^ { \prime } ( x )$ with the number of zeros of $g$ in $[ a , b ]$ reduced by $^ { 1 }$ . This implies that numbers $w _ { i }$ , for $i = 0 , 1 , \ldots , n - 2$ exist with g′(wi) = f′′(wi) = 0, and a < z0 < w0 < z1 < w1 < · · · wn 2 < zn 1 < b. (c) Continuing by induction following the logic in parts (a) and (b) provides $n + 1 - j$ distinct zeros of $f ^ { ( j ) }$ in $[ a , b ]$ . (d) The conclusion of the theorem follows from part (c) when $j = n$ , for in this case there will be (at least) $( n + 1 ) - n = 1$ zero in $[ a , b ]$ .

\*24. First observe that for $f ( x ) = x - \sin x$ we have $f ^ { \prime } ( x ) = 1 - \cos x \geq 0$ , because $- 1 \leq \cos x \leq 1$ for all values of $x$ . Also, the statement clearly holds when $| x | \geq \pi$ , because $| \sin x | \le 1$ .

(a) The observation implies that $f ( x )$ is non-decreasing for all values of $x$ , and in particular that $f ( x ) > f ( 0 ) = 0$ when $x > 0$ . Hence for $x \ge 0$ , we have $x \geq \sin x$ , and when $0 \leq x \leq \pi$ , $| \sin x | = \sin x \leq x = | x |$ .   
(b) When $- \pi < x < 0$ , we have $\pi \geq - x > 0$ . Since $\sin x$ is an odd function, the fact (from part (a)) that $\sin ( - x ) \leq ( - x )$ implies that $| \sin x | = - \sin x \leq - x = | x |$ . As a consequence, for all real numbers $x$ we have $| \sin x | \leq | x |$ .

25. Since $\begin{array} { r } { R _ { 2 } ( 1 ) = \frac { 1 } { 6 } e ^ { \xi } } \end{array}$ , for some $\xi$ in $( 0 , 1 )$ , we have $\begin{array} { r } { | E - R _ { 2 } ( 1 ) | = \frac 1 6 | 1 - e ^ { \xi } | \le \frac 1 6 ( e - 1 ) } \end{array}$ .

26. (a) Use the series

$$
e ^ { - t ^ { 2 } } = \sum _ { k = 0 } ^ { \infty } { \frac { ( - 1 ) ^ { k } t ^ { 2 k } } { k ! } } \quad { \mathrm { t o ~ i n t e g r a t e } } \quad { \frac { 2 } { \sqrt { \pi } } } \int _ { 0 } ^ { x } e ^ { - t ^ { 2 } } ~ d t ,
$$

and obtain the result.

(b) We have

$$
{ \begin{array} { c } { { \frac { 2 } { \sqrt { \pi } } } e ^ { - x ^ { 2 } } \displaystyle \sum _ { k = 0 } ^ { \infty } { \frac { 2 ^ { k } x ^ { 2 k + 1 } } { 1 \cdot 3 \cdot \cdot \cdot ( 2 k + 1 ) } } = { \frac { 2 } { \sqrt { \pi } } } \left[ 1 - x ^ { 2 } + { \frac { 1 } { 2 } } x ^ { 4 } - { \frac { 1 } { 6 } } x ^ { 7 } + { \frac { 1 } { 2 4 } } x ^ { 8 } + \cdots \right] } \\ { \cdot \left[ x + { \frac { 2 } { 3 } } x ^ { 3 } + { \frac { 4 } { 1 5 } } x ^ { 5 } + { \frac { 8 } { 1 0 5 } } x ^ { 7 } + { \frac { 1 6 } { 9 4 5 } } x ^ { 9 } + \cdots \right] } \\ { = { \frac { 2 } { \sqrt { \pi } } } \left[ x - { \frac { 1 } { 3 } } x ^ { 3 } + { \frac { 1 } { 1 0 } } x ^ { 5 } - { \frac { 1 } { 4 2 } } x ^ { 7 } + { \frac { 1 } { 2 1 6 } } x ^ { 9 } + \cdots \right] = { \mathrm { e r f ~ } } \left( x \right) } \end{array} }
$$

(c) 0.8427008

(d) 0.8427069

(e) The series in part (a) is alternating, so for any positive integer $n$ and positive $x$ we have the bound

$$
\left| \operatorname { e r f } ( x ) - { \frac { 2 } { \sqrt { \pi } } } \sum _ { k = 0 } ^ { n } { \frac { ( - 1 ) ^ { k } x ^ { 2 k + 1 } } { ( 2 k + 1 ) k ! } } \right| < { \frac { x ^ { 2 n + 3 } } { ( 2 n + 3 ) ( n + 1 ) ! } } ~ .
$$

We have no such bound for the positive term series in part (b).

27. (a) Let $x _ { 0 }$ be any number in $[ a , b ]$ . Given $\epsilon > 0$ , let $\delta = \epsilon / L$ . If $| x - x _ { 0 } | < \delta$ and $a \leq x \leq b$ then $| f ( x ) - f ( x _ { 0 } ) | \leq L | x - x _ { 0 } | < \epsilon$ .

(b) Using the Mean Value Theorem, we have

$$
| f ( x _ { 2 } ) - f ( x _ { 1 } ) | = | f ^ { \prime } ( \xi ) | | x _ { 2 } - x _ { 1 } | ,
$$

for some $\xi$ between $x _ { 1 }$ and $x _ { 2 }$ , so

$$
| f ( x _ { 2 } ) - f ( x _ { 1 } ) | \leq L | x _ { 2 } - x _ { 1 } | .
$$

(c) One example is $f ( x ) = x ^ { 1 / 3 }$ on $[ 0 , 1 ]$ .

$^ *$ 28. (a) The number ${ \textstyle \frac { 1 } { 2 } } ( f ( x _ { 1 } ) + f ( x _ { 2 } ) )$ is the average of $f ( x _ { 1 } )$ and $f ( x _ { 2 } )$ , so it lies between these two values of $f$ . By the Intermediate Value Theorem 1.11 there exist a number $\xi$ between $x _ { 1 }$ and $x _ { 2 }$ with

$$
f ( \xi ) = { \frac { 1 } { 2 } } ( f ( x _ { 1 } ) + f ( x _ { 2 } ) ) = { \frac { 1 } { 2 } } f ( x _ { 1 } ) + { \frac { 1 } { 2 } } f ( x _ { 2 } ) .
$$

(b) Let $m = \operatorname* { m i n } \{ f ( x _ { 1 } ) , f ( x _ { 2 } ) \}$ and $M = \operatorname* { m a x } \{ f ( x _ { 1 } ) , f ( x _ { 2 } ) \}$ . Then $m \le f ( x _ { 1 } ) \le M$ and $m \leq f ( x _ { 2 } ) \leq M$ , so

$$
\leq c _ { 1 } f ( x _ { 1 } ) \leq c _ { 1 } M \quad { \mathrm { a n d } } \quad c _ { 2 } m \leq c _ { 2 } f ( x _ { 2 } ) \leq c _ { 2 } l
$$

Thus

$$
( c _ { 1 } + c _ { 2 } ) m \leq c _ { 1 } f ( x _ { 1 } ) + c _ { 2 } f ( x _ { 2 } ) \leq ( c _ { 1 } + c _ { 2 } ) M
$$

and

$$
m \leq { \frac { c _ { 1 } f ( x _ { 1 } ) + c _ { 2 } f ( x _ { 2 } ) } { c _ { 1 } + c _ { 2 } } } \leq M .
$$

By the Intermediate Value Theorem 1.11 applied to the interval with endpoints $x _ { 1 }$ and $x _ { 2 }$ , there exists a number $\xi$ between $x _ { 1 }$ and $x _ { 2 }$ for which

$$
f ( \xi ) = \frac { c _ { 1 } f ( x _ { 1 } ) + c _ { 2 } f ( x _ { 2 } ) } { c _ { 1 } + c _ { 2 } } .
$$

(c) Let $f ( x ) = x ^ { 2 } + 1$ , $x _ { 1 } = 0$ , $x _ { 2 } = 1$ , $c _ { 1 } = 2$ , and $c _ { 2 } = - 1$ . Then for all values of $x$ ,

$$
f ( x ) > 0 \quad \mathrm { b u t } \quad { \frac { c _ { 1 } f ( x _ { 1 } ) + c _ { 2 } f ( x _ { 2 } ) } { c _ { 1 } + c _ { 2 } } } = { \frac { 2 ( 1 ) - 1 ( 2 ) } { 2 - 1 } } = 0 .
$$

29. (a) Since $f$ is continuous at $p$ and $f ( p ) \neq 0$ , there exists a $\delta > 0$ with

$$
| f ( x ) - f ( p ) | < { \frac { | f ( p ) | } { 2 } } ,
$$

for $| x - p | < \delta$ and $a < x < b$ . We restrict $\delta$ so that $[ p - \delta , p + \delta ]$ is a subset of $[ a , b ]$ . Thus, for $x \in [ p - \delta , p + \delta ]$ , we have $x \in [ a , b ]$ . So

$$
- { \frac { | f ( p ) | } { 2 } } < f ( x ) - f ( p ) < { \frac { | f ( p ) | } { 2 } } { \mathrm { a n d } } f ( p ) - { \frac { | f ( p ) | } { 2 } } < f ( x ) < f ( p ) + { \frac { | f ( p ) | } { 2 } } .
$$

If $f ( p ) > 0$ , then

$$
f ( p ) - \frac { | f ( p ) | } { 2 } = \frac { f ( p ) } { 2 } > 0 , \quad \mathrm { s o } \quad f ( x ) > f ( p ) - \frac { | f ( p ) | } { 2 } > 0 .
$$

If $f ( p ) < 0$ , then $| f ( p ) | = - f ( p )$ , and

$$
f ( x ) < f ( p ) + \frac { | f ( p ) | } { 2 } = f ( p ) - \frac { f ( p ) } { 2 } = \frac { f ( p ) } { 2 } < 0 .
$$

In either case, $f ( x ) \neq 0$ , for $x \in [ p - \delta , p + \delta ]$ .

(b) Since $f$ is continuous at $p$ and $f ( p ) = 0$ , there exists a $\delta > 0$ with

$$
| f ( x ) - f ( p ) | < k , \quad { \mathrm { f o r } } \quad | x - p | < \delta \quad { \mathrm { a n d } } \quad a < x < b .
$$

We restrict $\delta$ so that $[ p - \delta , p + \delta ]$ is a subset of $\lfloor a , b \rfloor$ . Thus, for $x \in [ p - \delta , p + \delta ]$ , we have

$$
| f ( x ) | = | f ( x ) - f ( p ) | < k .
$$

# Exercise Set 1.2, page 28

1. We have

<table><tr><td colspan="2">Absolute error Relative error</td></tr><tr><td>(a) 0.001264</td><td>4.025 × 10-4</td></tr><tr><td>(b) 7.346 × 10-6</td><td>2.338 × 10-6</td></tr><tr><td>(c) 2.818× 10-4</td><td>1.037 × 10-4</td></tr><tr><td>(d) 2.136 × 10-4</td><td>1.510 × 10-4</td></tr><tr><td>(e) 2.647 ×101</td><td>1.202 × 10-3</td></tr><tr><td>(f) 1.454×101</td><td>1.050 × 10-2</td></tr><tr><td>420</td><td>1.042 × 10-2</td></tr><tr><td>(g)</td><td></td></tr><tr><td>(h) 3.343 × 103</td><td>9.213 × 10-3</td></tr></table>

2. The largest intervals are:

(a) (3.1412784, 3.1419068) (b) (2.7180100, 2.7185536) \*(c) (1.4140721, 1.4143549) (d) (1.9127398, 1.9131224)

3. The largest intervals are (a) (149.85,150.15) (b) (899.1, 900.9 ) (c) (1498.5, 1501.5) (d) (89.91,90.09)

4. The calculations and their errors are:

(a) (i) 17/15 (ii) 1.13 (iii) 1.13 (iv) both $3 \times 1 0 ^ { - 3 }$ (b) (i) 4/15 (ii) 0.266 (iii) 0.266 (iv) both $2 . 5 \times 1 0 ^ { - 3 }$ (c) (i) 139/660 (ii) 0.211 (iii) 0.210 (iv) $2 \times 1 0 ^ { - 3 }$ , $3 \times 1 0 ^ { - 3 }$ (d) (i) 301/660 (ii) 0.455 (iii) 0.456 (iv) $2 \times 1 0 ^ { - 3 }$ , $1 \times 1 0 ^ { - 4 }$

5. We have

<table><tr><td>Approximation</td><td></td><td>Absolute error</td><td>Relative error</td></tr><tr><td>8</td><td>134</td><td>0.079</td><td>5.90 ×10-4</td></tr><tr><td></td><td>133</td><td>0.499</td><td>3.77 × 10-3</td></tr><tr><td>C</td><td>2.00</td><td>0.327</td><td>0.195</td></tr><tr><td>(d)</td><td>1.67</td><td>0.003</td><td>1.79 × 10-3</td></tr><tr><td>*（e）</td><td>1.80</td><td>0.154</td><td>0.0786</td></tr><tr><td>(f）</td><td>-15.1</td><td>0.0546</td><td>3.60 × 10-3</td></tr><tr><td>（g）</td><td>0.286</td><td>2.86 × 10-4</td><td>10-3</td></tr><tr><td>(h)</td><td>0.00</td><td>0.0215</td><td>1.00</td></tr></table>

6. We have

<table><tr><td>Approximation</td><td>Absolute error</td><td>Relative error</td></tr><tr><td>(a) 133.9</td><td>0.021</td><td>1.568 × 10-4</td></tr><tr><td>(b) 132.5</td><td>0.001</td><td>7.55 × 10-6</td></tr><tr><td>(c) 1.700</td><td>0.027</td><td>0.01614</td></tr><tr><td>(d) 1.673</td><td>0</td><td>0</td></tr><tr><td>(e) 1.986</td><td>0.03246</td><td>0.01662</td></tr><tr><td>(f） -15.16</td><td>0.005377</td><td>3.548 × 10-4</td></tr><tr><td>(g） 0.2857</td><td>1.429 × 10-5</td><td>5×10-5</td></tr><tr><td>(h) -0.01700</td><td>0.0045</td><td>0.2092</td></tr></table>

<table><tr><td>Approximation</td><td></td><td>Absolute error</td><td>Relative error</td></tr><tr><td>(a)</td><td>133</td><td>0.921</td><td>6.88 × 10-3</td></tr><tr><td>b</td><td>132</td><td>0.501</td><td>3.78 × 10-3</td></tr><tr><td>C</td><td>1.00</td><td>0.673</td><td>0.402</td></tr><tr><td>(d)</td><td>1.67</td><td>0.003</td><td>1.79 × 10-3</td></tr><tr><td>*（e)</td><td>3.55</td><td>1.60</td><td>0.817</td></tr><tr><td>国</td><td>-15.2</td><td>0.0454</td><td>0.00299</td></tr><tr><td></td><td>0.284</td><td>0.00171</td><td>0.00600</td></tr><tr><td>(h)</td><td>0</td><td>0.02150</td><td>1</td></tr></table>

8. We have

<table><tr><td>Approximation</td><td>Absolute error</td><td>Relative error</td></tr><tr><td>(a)</td><td>133.9 0.021</td><td>1.568 × 10-4</td></tr><tr><td>(b)</td><td>0.001</td><td>7.55 × 10-6</td></tr><tr><td>（c）</td><td>0.073</td><td>0.04363</td></tr><tr><td>(d)</td><td>0</td><td>0</td></tr><tr><td>(e)</td><td>0.02945</td><td>0.01508</td></tr><tr><td>(f)</td><td>0.004622</td><td>3.050 × 10-4</td></tr><tr><td>(g）</td><td>2.143 × 10-4</td><td>7.5 ×10-4</td></tr><tr><td>(h)</td><td>0.0045</td><td>0.2092</td></tr></table>

9. We have

<table><tr><td></td><td>Approximation</td><td>Absolute error</td><td>Relative error</td></tr><tr><td>*（a)</td><td>3.14557613</td><td>3.983 × 10-3</td><td>1.268 × 10-3</td></tr><tr><td>(b)</td><td>3.14162103</td><td>2.838×10-5</td><td>9.032 × 10-6</td></tr></table>

10. We have

<table><tr><td></td><td>Approximation</td><td>Absolute error</td><td>Relative error</td></tr><tr><td>(a)</td><td>2.7166667</td><td>0.0016152</td><td>5.9418 × 10-4</td></tr><tr><td>(b)</td><td>2.718281801</td><td>2.73 ×10-8</td><td>1.00 × 10-8</td></tr></table>

11. (a) We have

$$
\operatorname* { l i m } _ { x \to 0 } { \frac { x \cos x - \sin x } { x - \sin x } } = \operatorname* { l i m } _ { x \to 0 } { \frac { - x \sin x } { 1 - \cos x } } = \operatorname* { l i m } _ { x \to 0 } { \frac { - \sin x - x \cos x } { \sin x } } = \operatorname* { l i m } _ { x \to 0 } { \frac { - 2 \cos x + x \sin x } { \cos x } } = - 2
$$

(b) $f ( 0 . 1 ) \approx - 1 . 9 4 1$   
(c) $\frac { x ( 1 - \frac { 1 } { 2 } x ^ { 2 } ) - ( x - \frac { 1 } { 6 } x ^ { 3 } ) } { x - ( x - \frac { 1 } { 6 } x ^ { 3 } ) } = - 2$   
(d) The relative error in part (b) is 0.029. The relative error in part (c) is 0.00050.

12. (a) $\operatorname* { l i m } _ { x \to 0 } { \frac { e ^ { x } - e ^ { - x } } { x } } = \operatorname* { l i m } _ { x \to 0 } { \frac { e ^ { x } + e ^ { - x } } { 1 } } = 2$ (b) $f ( 0 . 1 ) \approx 2 . 0 5$ (c) ${ \frac { 1 } { x } } \left( \left( 1 + x + { \frac { 1 } { 2 } } x ^ { 2 } + { \frac { 1 } { 6 } } x ^ { 3 } \right) - \left( 1 - x + { \frac { 1 } { 2 } } x ^ { 2 } - { \frac { 1 } { 6 } } x ^ { 3 } \right) \right) = { \frac { 1 } { x } } \left( 2 x + { \frac { 1 } { 3 } } x ^ { 3 } \right) = 2 + { \frac { 1 } { 3 } } x ^ { 2 } .$ ; using three-digit rounding arithmetic and $x = 0 . 1$ , we obtain 2.00. (d) The relative error in part (b) is $= 0 . 0 2 3 3$ . The relative error in part (c) is $= 0 . 0 0 1 6 6$

13. We have

<table><tr><td></td><td>X1</td><td>Absolute error</td><td>Relative error</td><td>2</td><td>Absolute error</td><td>Relative error</td></tr><tr><td>(a）</td><td>92.26</td><td>0.01542</td><td>1.672 × 10-4</td><td>0.005419</td><td>6.273 × 10-7</td><td>1.157 × 10-4</td></tr><tr><td>(b）</td><td>0.005421</td><td>1.264 × 10-6</td><td>2.333×10-4</td><td>-92.26</td><td>4.580 ×10-3</td><td>4.965 × 10-5</td></tr><tr><td>（c）</td><td>10.98</td><td>6.875×10-3</td><td>6.257 ×10-4</td><td>0.001149</td><td>7.566 × 10-8</td><td>6.584 ×10-5</td></tr><tr><td>d)</td><td>-0.001149</td><td>7.566 × 10-8</td><td>6.584 × 10-5</td><td>-10.98</td><td>6.875 × 10-3</td><td>6.257× 10-4</td></tr></table>

14. We have

<table><tr><td></td><td>Approximation for x1</td><td>Absolute error</td><td>Relative error</td></tr><tr><td>(a)</td><td>92.24</td><td>0.004580</td><td>4.965 × 10-5</td></tr><tr><td>(b)</td><td>0.005417</td><td>2.736 ×10-6</td><td>5.048 × 10-4</td></tr><tr><td>(c）</td><td>10.98</td><td>6.875 × 10-3</td><td>6.257× 10-4</td></tr><tr><td>(d)</td><td>-0.001149</td><td>7.566 × 10-8</td><td>6.584 × 10-5</td></tr></table>

<table><tr><td>Approximation for</td><td>x2</td><td>Absolute error</td><td>Relative error</td></tr><tr><td>(a)</td><td>0.005418</td><td>2.373 × 10-6</td><td>4.377 × 10-4</td></tr><tr><td>(6)</td><td>-92.25</td><td>5.420 × 10-3</td><td>5.875 × 10-5</td></tr><tr><td>（c）</td><td>0.001149</td><td>7.566 × 10-8</td><td>6.584 × 10-5</td></tr><tr><td>(d）</td><td>-10.98</td><td>6.875 × 10-3</td><td>6.257 × 10-4</td></tr></table>

15. The machine numbers are equivalent to

(a) 3224 (b) −3224 \*(c) 1.32421875 (d) 1.3242187500000002220446049250313080847263336181640625

16. (a) Next Largest: 3224.00000000000045474735088646411895751953125; Next Smallest: 3223.99999999999954525264911353588104248046875 (b) Next Largest: −3224.00000000000045474735088646411895751953125; Next Smallest: −3223.99999999999954525264911353588104248046875 \*(c) Next Largest: 1.3242187500000002220446049250313080847263336181640625; Next Smallest: 1.3242187499999997779553950749686919152736663818359375 (d) Next Largest: 1.324218750000000444089209850062616169452667236328125; Next Smallest: 1.32421875

17. (b) The first formula gives $- 0 . 0 0 6 5 8$ , and the second formula gives $- 0 . 0 1 0 0$ . The true threedigit value is $- 0 . 0 1 1 6$ .

18. (a) $- 1 . 8 2$ (b) $7 . 0 9 \times 1 0 ^ { - 3 }$ (c) The formula in (b) is more accurate since subtraction is not involved.

19. The approximate solutions to the systems are (a) $x = 2 . 4 5 1$ , $y = - 1 . 6 3 5$ (b) $x = 5 0 7 . 7$ , $y = 8 2 . 0 0$

20. (a) $x = 2 . 4 6 0$ $y = - 1 . 6 3 4$ (b) $x = 4 7 7 . 0$ $y = 7 6 . 9 3$

\*21. (a) In nested form, we have $f ( x ) = ( ( ( 1 . 0 1 e ^ { x } - 4 . 6 2 ) e ^ { x } - 3 . 1 1 ) e ^ { x } + 1 2 . 2 ) e ^ { x } - 1 . 9 9 .$

(b) $- 6 . 7 9$   
(c) $- 7 . 0 7$   
(d) The absolute errors are

$$
- 7 . 6 1 - ( - 6 . 7 1 ) | = 0 . 8 2 \quad \mathrm { a n d } \quad | - 7 . 6 1 - ( -
$$

Nesting is significantly better since the relative errors are

$$
\left| { \frac { 0 . 8 2 } { - 7 . 6 1 } } \right| = 0 . 1 0 8 \quad { \mathrm { a n d } } \quad \left| { \frac { 0 . 5 4 } { - 7 . 6 1 } } \right| = 0 . 0 7 1 ,
$$

22. We have $3 9 . 3 7 5 \leq$ Volume $\leq 8 6 . 6 2 5$ and 71.5 ≤ Surface Area ≤ 119.5.

23. (a) $n = 7 7$

(b) $n = 3 5$

$^ { * } 2 4$ . When $d _ { k + 1 } < 5$ ,

$$
\left| \frac { y - f l ( y ) } { y } \right| = \frac { 0 . d _ { k + 1 } \ldots \times 1 0 ^ { n - k } } { 0 . d _ { 1 } \ldots \times 1 0 ^ { n } } \leq \frac { 0 . 5 \times 1 0 ^ { - k } } { 0 . 1 } = 0 . 5 \times 1 0 ^ { - k + 1 } .
$$

When $d _ { k + 1 } > 5$ ,

$$
\left| \frac { y - f l ( y ) } { y } \right| = \frac { ( 1 - 0 . d _ { k + 1 } \ldots ) \times 1 0 ^ { n - k } } { 0 . d _ { 1 } \ldots \times 1 0 ^ { n } } < \frac { ( 1 - 0 . 5 ) \times 1 0 ^ { - k } } { 0 . 1 } = 0 . 5 \times 1 0 ^ { - k + 1 } .
$$

25. (a) $m = 1 7$ (b) We have ${ \binom { m } { k } } = { \frac { m ! } { k ! ( m - k ) ! } } = { \frac { m ( m - 1 ) \cdot \cdot \cdot ( m - k - 1 ) ( m - k ) ! } { k ! ( m - k ) ! } } = \left( { \frac { m } { k } } \right) \left( { \frac { m - 1 } { k - 1 } } \right) \cdot \cdot \cdot \left( { \frac { m - k - 1 } { 1 } } \right)$ (c) $m = 1 8 1 7 0 7$ (d) 2,597,000; actual error 1960; relative error $7 . 5 4 1 \times 1 0 ^ { - 4 }$

26. (a) The actual error is $| f ^ { \prime } ( \xi ) \epsilon |$ , and the relative error is $| f ^ { \prime } ( \xi ) \boldsymbol { \epsilon } | \cdot | f ( x _ { 0 } ) | ^ { - 1 }$ , where the number $\xi$ is between $x _ { 0 }$ and $x _ { 0 } + \epsilon$ . (b) (i) $1 . 4 \times 1 0 ^ { - 5 }$ ; $5 . 1 \times 1 0 ^ { - 6 }$ (ii) $2 . 7 \times 1 0 ^ { - 6 }$ ; $3 . 2 \times 1 0 ^ { - 6 }$ (c) (i) 1.2; $5 . 1 \times 1 0 ^ { - 5 }$ (ii) $4 . 2 \times 1 0 ^ { - 5 }$ ; $7 . 8 \times 1 0 ^ { - 5 }$

27. (a) 124.03  
(b) 124.03  
(c) −124.03  
(d) −124.03  
(e) 0.0065  
(f) 0.0065  
(g) −0.0065  
(h) −0.0065

\*28. Since $0 . 9 9 5 \le P \le 1 . 0 0 5$ , $0 . 0 9 9 5 \le V \le 0 . 1 0 0 5$ , $0 . 0 8 2 0 5 5 \le R \le 0 . 0 8 2 0 6 5$ , and $0 . 0 0 4 1 9 5 \le$ $N \leq 0 . 0 0 4 2 0 5$ , we have $2 8 7 . 6 1 ^ { \circ } \leq T \leq 2 9 3 . 4 2 ^ { \circ }$ . Note that $1 5 ^ { \circ } \mathrm { C } = 2 8 8 . 1 6 \mathrm { K }$ .

When $P$ is doubled and $V$ is halved, $1 . 9 9 \leq P \leq 2 . 0 1$ and $0 . 0 4 9 7 \le V \le 0 . 0 5 0 3$ so that $2 8 6 . 6 1 ^ { \circ } \leq T \leq 2 9 3 . 7 2 ^ { \circ }$ . Note that $1 9 ^ { \circ } \mathrm { C } \ = \ 2 9 2 . 1 6 \mathrm { K }$ . The laboratory figures are within an acceptable range.

# Exercise Set 1.3, page 39

1. (a) ${ \frac { 1 } { 1 } } + { \frac { 1 } { 4 } } \ldots + { \frac { 1 } { 1 0 0 } } = 1 . 5 3 ; \quad { \frac { 1 } { 1 0 0 } } + { \frac { 1 } { 8 1 } } + \ldots + { \frac { 1 } { 1 } } = 1 . 5 4 .$ The actual value is 1.549. Significant round-off error occurs much earlier in the first method. (b) The following algorithm will sum the series $\textstyle \sum _ { i = 1 } ^ { N } x _ { i }$ in the reverse order. INPUT N; x1, x2, . . . , xN OUTPUT SUM STEP 1 Set $S U M = 0$ STEP 2 For $j = 1 , \ldots , N$ set $i = N - j + 1$ $S U M = S U M + x _ { i }$ STEP 3 $\operatorname { O U T P U T } ( S U M )$ ; STOP.

2. We have

<table><tr><td></td><td>Approximation</td><td>Absolute Error</td><td>Relative Error</td></tr><tr><td>(a)</td><td>2.715</td><td>3.282 × 10-3</td><td>1.207 × 10-3</td></tr><tr><td>(b)</td><td>2.716</td><td>2.282 × 10-3</td><td>8.394 × 10-4</td></tr><tr><td>（c）</td><td>2.716</td><td>2.282 ×10-3</td><td>8.394 × 10-4</td></tr><tr><td>(d)</td><td>2.718</td><td>2.818 × 10-4</td><td>1.037 × 10-4</td></tr></table>

\*3. (a) 2000 terms (b) 20,000,000,000 terms

4. 4 terms \*5. 3 terms

6. (a) $\textstyle O \left( { \frac { 1 } { n } } \right)$ (b) $\textstyle O \left( { \frac { 1 } { n ^ { 2 } } } \right)$ (c) $\textstyle O \left( { \frac { 1 } { n ^ { 2 } } } \right)$ (d) $\textstyle O \left( { \frac { 1 } { n } } \right)$

7. The rates of convergence are:

(a) $O ( h ^ { 2 } )$ (b) $O ( h )$ (c) $O ( h ^ { 2 } )$ (d) $O ( h )$

$^ { * } 8$ . (a) $n ( n + 1 ) / 2$ multiplications; $( n + 2 ) ( n - 1 ) / 2$ additions.

(b) $\sum _ { i = 1 } ^ { n } a _ { i } \left( \sum _ { j = 1 } ^ { i } b _ { j } \right)$ requires $n$ multiplications; $( n + 2 ) ( n - 1 ) / 2$ additions.

9. The following algorithm computes $P ( x _ { 0 } )$ using nested arithmetic.

INPUT n, a0, a1, . . . , an, x0   
OUTPUT $y = P ( x _ { 0 } )$   
STEP 1 Set $y = a _ { n }$ .   
STEP 2 For $i = n - 1 , n - 2 , \dots , 0$ set $y = x _ { 0 } y + a _ { i }$ . STEP 3 OUTPUT (y);   
STOP.

\*10. The following algorithm uses the most effective formula for computing the roots of a quadratic equation.

INPUT A, $B$ , $C$ .   
OUTPUT $x _ { 1 }$ , $x _ { 2 }$ .

STEP 1 If $A = 0$ then

STEP 2 Set $D = B ^ { 2 } - 4 A C$ .

STEP 3 If $D = 0$ then set $x _ { 1 } = - B / ( 2 A )$ ; OUTPUT (‘MULTIPLE ROOTS’, $x _ { 1 }$ ); STOP.

STEP 4 If $D < 0$ then set

STEP 5 If $B \geq 0$ then set

else set

$$
\begin{array} { l } { d = - B + \sqrt { D } ; } \\ { x _ { 1 } = d / ( 2 A ) ; } \\ { x _ { 2 } = 2 C / d . } \end{array}
$$

STEP 6 OUTPUT $( x _ { 1 } , x _ { 2 } )$ ;

STOP.

11. The following algorithm produces the product $P = ( x - x _ { 0 } ) , \ldots , ( x - x _ { n } )$ .

INPUT n, x0, x1, · · · , xn, x OUTPUT $P$ .

STEP 1 Set P = x − x0; i = 1.

STEP 2 While $P \neq 0$ and $i \leq n$ set

$$
{ \begin{array} { l } { P = P \cdot ( x - x _ { i } ) ; } \\ { i = i + 1 } \end{array} }
$$

STEP 3 OUTPUT $( P )$ ; STOP.

12. The following algorithm determines the number of terms needed to satisfy a given tolerance.

INPUT number $x$ , tolerance $T O L$ , maximum number of iterations $M$ .   
OUTPUT number $N$ of terms or a message of failure.

STEP 1 Set SUM = (1 − 2x)/  1 − x + x2; S = (1 + 2x)/  1 + x + x2; N = 2.

STEP 2 While $N \leq M$ do Steps 3–5.

$$
\begin{array} { l l l } { { S T E P 3 } } & { { \mathrm { S e t } } } & { { j = 2 ^ { N - 1 } ; } } \\ { { } } & { { y = x ^ { j } } } \\ { { } } & { { } } & { { t _ { 1 } = { \displaystyle \frac { j y } { x } } ( 1 - 2 y ) ; } } \\ { { } } & { { } } & { { t _ { 2 } = y ( y - 1 ) + 1 ; } } \\ { { } } & { { } } & { { S U M = S U M + { \displaystyle \frac { t _ { 1 } } { t _ { 2 } } } . } } \\ { { } } & { { } } & { { S U M - S | < T O L } } \end{array}
$$

OUTPUT ( $N$ );

STOP.

STEP 6 OUTPUT(’Method failed’); STOP.

When $T O L = 1 0 ^ { - 6 }$ , we need to have $N \geq 4$ .

13. (a) If $| \alpha _ { n } - \alpha | / ( 1 / n ^ { p } ) \leq K$ , then

$$
| \alpha _ { n } - \alpha | \leq K ( 1 / n ^ { p } ) \leq K ( 1 / n ^ { q } ) \quad { \mathrm { s i n c e } } \quad 0 < q < p .
$$

Thus

$$
| \alpha _ { n } - \alpha | / ( 1 / n ^ { p } ) \leq K \quad { \mathrm { a n d } } \quad \{ \alpha _ { n } \} _ { n = 1 } ^ { \infty } \to \alpha
$$

with rate of convergence $O ( 1 / n ^ { p } )$ .

<table><tr><td>n</td><td>1/n</td><td>1/n²</td><td>1/n</td><td>1/n5</td></tr><tr><td>5</td><td>0.2</td><td>0.04</td><td>0.008</td><td>0.0016</td></tr><tr><td>10</td><td>0.1</td><td>0.01</td><td>0.001</td><td>0.0001</td></tr><tr><td>50</td><td>0.02</td><td>0.0004</td><td>8×10-6</td><td>1.6 ×10-7</td></tr><tr><td>100</td><td>0.01</td><td>10-4</td><td>10-6</td><td>10-8</td></tr></table>

The most rapid convergence rate is $O ( 1 / n ^ { 4 } )$ .

14. (a) If $F ( h ) = L + O \left( h ^ { p } \right)$ , there is a constant $k > 0$ such that

$$
| F ( h ) - L | \leq k h ^ { p } ,
$$

for sufficiently small $h > 0$ . If $0 < q < p$ and $0 < h < 1$ , then $h ^ { q } > h ^ { p }$ . Thus, $k h ^ { p } < k h ^ { q }$ , so

$$
\vert F ( h ) - L \vert \leq k h ^ { q } \quad { \mathrm { a n d } } \quad F ( h ) = L + O \left( h ^ { q } \right) .
$$

(b) For various powers of $h$ we have the entries in the following table.

<table><tr><td>h</td><td>h2</td><td>h</td><td>h4</td></tr><tr><td>0.5</td><td>0.25</td><td>0.125</td><td>0.0625</td></tr><tr><td>0.1</td><td>0.01</td><td>0.001</td><td>0.0001</td></tr><tr><td>0.01</td><td>0.0001</td><td>0.00001</td><td>10-8</td></tr><tr><td>0.001</td><td>10-6</td><td>10-9</td><td>10-12</td></tr></table>

The most rapid convergence rate is $O \left( h ^ { 4 } \right)$ .

$^ *$ 15. Suppose that for sufficiently small $| x |$ we have positive constants $k _ { 1 }$ and $k _ { 2 }$ independent of $x$ , for which

$$
| F _ { 1 } ( x ) - L _ { 1 } | \leq K _ { 1 } | x | ^ { \alpha } \mathrm { ~ a n d ~ } | F _ { 2 } ( x ) - L _ { 2 } | \leq K _ { 2 } | x | ^ { \beta } .
$$

Let $c = \operatorname* { m a x } ( | c _ { 1 } | , | c _ { 2 } | , 1 )$ , $K = \operatorname* { m a x } ( K _ { 1 } , K _ { 2 } )$ , and $\delta = \operatorname* { m a x } ( \alpha , \beta )$ .

(a) We have

$$
\begin{array} { r l r } {  { | F ( x ) - c _ { 1 } L _ { 1 } - c _ { 2 } L _ { 2 } | = | c _ { 1 } ( F _ { 1 } ( x ) - L _ { 1 } ) + c _ { 2 } ( F _ { 2 } ( x ) - L _ { 2 } ) | } } \\ & { } & { \leq | c _ { 1 } | K _ { 1 } | x | ^ { \alpha } + | c _ { 2 } | K _ { 2 } | x | ^ { \beta } \leq c K [ | x | ^ { \alpha } + | x | ^ { \beta } ] } \\ & { } & { \leq c K | x | ^ { \gamma } [ 1 + | x | ^ { \delta - \gamma } ] \leq \tilde { K } | x | ^ { \gamma } , } \end{array}
$$

for sufficiently small $| x |$ and some constant $\ddot { K }$ . Thus, $F ( x ) = c _ { 1 } L _ { 1 } + c _ { 2 } L _ { 2 } + O ( x ^ { \gamma } )$ .

(b) We have

$$
\begin{array} { r l } & { | G ( x ) - L _ { 1 } - L _ { 2 } | = | F _ { 1 } ( c _ { 1 } x ) + F _ { 2 } ( c _ { 2 } x ) - L _ { 1 } - L _ { 2 } | } \\ & { \qquad \leq K _ { 1 } | c _ { 1 } x | ^ { \alpha } + K _ { 2 } | c _ { 2 } x | ^ { \beta } \leq K c ^ { \delta } [ | x | ^ { \alpha } + | x | ^ { \beta } ] } \\ & { \qquad \leq K c ^ { \delta } | x | ^ { \gamma } [ 1 + | x | ^ { \delta - \gamma } ] \leq \tilde { K } | x | ^ { \gamma } , } \end{array}
$$

for sufficiently small $| x |$ and some constant $\ddot { K }$ . Thus, $G ( x ) = L _ { 1 } + L _ { 2 } + O ( x ^ { \gamma } )$ .

$^ *$ 16. Since

$$
\operatorname* { l i m } _ { n \to \infty } x _ { n } = \operatorname* { l i m } _ { n \to \infty } x _ { n + 1 } = x \quad { \mathrm { a n d } } \quad x _ { n + 1 } = 1 + { \frac { 1 } { x _ { n } } } ,
$$

we have

$$
x = 1 + { \frac { 1 } { x } } , \quad \mathrm { s o } \quad x ^ { 2 } - x - 1 = 0 .
$$

The quadratic formula implies that

$$
x = { \frac { 1 } { 2 } } \left( 1 + { \sqrt { 5 } } \right) .
$$

This number is called the golden ratio. It appears frequently in mathematics and the sciences.

$^ *$ 17. (a) To save space we will show the Maple output for each step in one line. Maple would produce this output on separate lines. $n : = 9 8 ; f : = 1 ; s : = 1$ $n : = 9 8 \quad f : = 1 \quad s : = 1$ for $i$ from 1 to $n$ do $l : = f + s ; f : = s ; s : = l ; o d$ : $l : = 2$ $f : = 1$ $s : = 2$ $\mathit { l } : = 3$ $f : = 2$ $s : = 3$ .. l :=218922995834555169026 f := 135301852344706746049 s := 218922995834555169026 l :=354224848179261915075

$$
\begin{array} { c } { { F 1 0 0 : = \displaystyle \frac { 1 } { s q r t ( 5 ) } \left( \left( \displaystyle \frac { \left( 1 + s q r t ( 5 ) \right) } { 2 } \right) ^ { 1 0 0 } - \left( \displaystyle \frac { 1 - s q r t ( 5 ) } { 2 } \right) ^ { 1 0 0 } \right) } } \\ { { F 1 0 0 : = \displaystyle \frac { 1 } { \sqrt { 5 } } \left( \left( \displaystyle \frac { 1 } { 2 } + \displaystyle \frac { 1 } { 2 } \sqrt { 5 } \right) ^ { 1 0 0 } - \left( \displaystyle \frac { 1 } { 2 } - \displaystyle \frac { 1 } { 2 } \sqrt { 5 } \right) ^ { 1 0 0 } \right) } } \end{array}
$$

$$
0 . 3 5 4 2 2 4 8 5 3 8 \times 1 0 ^ { 2 1 }
$$

(c) The result in part (a) is computed using exact integer arithmetic, and the result in part (b) is computed using ten-digit rounding arithmetic.   
(d) The result in part (a) required traversing a loop 98 times.   
(e) The result is the same as the result in part (a).

18. (a) $n = 5 0$ (b) $n = 5 0 0$

# Solutions of Equations of One Variable

Exercise Set 2.1, page 54

$^ * 1$ . $p _ { 3 } = 0 . 6 2 5$

2. \*(a) $p _ { 3 } = - 0 . 6 8 7 5$ (b) $p _ { 3 } = 1 . 0 9 3 7 5$

3. The Bisection method gives:

(a) $p _ { 7 } = 0 . 5 8 5 9$ (b) $p _ { 8 } = 3 . 0 0 2$ (c) $p _ { 7 } = 3 . 4 1 9$

4. The Bisection method gives:

(a) $p _ { 7 } = - 1 . 4 1 4$ (b) $p _ { 8 } = 1 . 4 1 4$ (c) $p _ { 7 } = 2 . 7 2 7$ (d) $p _ { 7 } = - 0 . 7 2 6 5$

5. The Bisection method gives:

(a) $p _ { 1 7 } = 0 . 6 4 1 1 8 ^ { \cdot }$   
(b) $p _ { 1 7 } = 0 . 2 5 7 5 3 0$   
(c) For the interval $[ - 3 , - 2 ]$ , we have $p _ { 1 7 } = - 2 . 1 9 1 3 0 7$ , and for the interval $[ - 1 , 0 ]$ , we have $p _ { 1 7 } = - 0 . 7 9 8 1 6 4$ .   
(d) For the interval [0.2, 0.3], we have $p _ { 1 4 } = 0 . 2 9 7 5 2 8$ , and for the interval [1.2, 1.3], we have $p _ { 1 4 } = 1 . 2 5 6 6 2 2$ .

6. (a) $p _ { 1 7 } = 1 . 5 1 2 1 3 8 3 7$ (b) $p _ { 1 7 } = 0 . 9 7 6 7 6 8 4 9$ (c) For the interval [1, 2], we have $p _ { 1 7 } = 1 . 4 1 2 3 9 1 6 6$ , and for the interval [2, 4], we have $p _ { 1 8 } = 3 . 0 5 7 1 0 6 0 ^ { \cdot }$ .

(d) For the interval $[ 0 , 0 . 5 ]$ , we have $p _ { 1 6 } = 0 . 2 0 6 0 3 1 8 0$ , and for the interval [0.5, 1], we have $p _ { 1 6 } = 0 . 6 8 1 9 6 8 6 9$ .

7. (a)

![](images/67a2ad8f28a7e910d51b526b768de92f46863cf2ea105012ab53059bd3625dcd.jpg)

(b) Using [1.5, 2] from part (a) gives $p _ { 1 6 } = 1 . 8 9 5 5 0 0 1 8$ .

\*8. (a)

![](images/92528321b69f954db8b42100c8f809cbdfb2c48f6041ba14c2c95f5cf90f1fa0.jpg)

(b) Using [4.2, 4.6] from part (a) gives $p _ { 1 6 } = 4 . 4 9 3 4 1 4 3$ .

9. (a)

![](images/0de3a09adbdf34de07b5f8812d19f0c99199aee31dc49ca0343c02c49cf19678.jpg)

(b) $p _ { 1 7 } = 1 . 0 0 7 6 2 1 7 7$

10. (a) 0   
(b) 0   
(c) 2   
(d) −2

11. \*(a) 2 (b) −2 \*(c) $^ { - 1 }$ (d) 1

$^ *$ 12. We have $\sqrt { 3 } \approx p _ { 1 4 } = 1 . 7 3 2 0$ , using [1, 2].

13. The third root of 25 is approximately $p _ { 1 4 } = 2 . 9 2 4 0 1$ , using [2, 3].

$^ *$ 14. A bound for the number of iterations is $n \geq 1 2$ and $p _ { 1 2 } = 1 . 3 7 8 7$ .

15. A bound is $n \geq 1 4$ , and $p _ { 1 4 } = 1 . 3 2 4 7 7$

16. For $n > 1$ ,

$$
| f ( p _ { n } ) | = \left( { \frac { 1 } { n } } \right) ^ { 1 0 } \leq \left( { \frac { 1 } { 2 } } \right) ^ { 1 0 } = { \frac { 1 } { 1 0 2 4 } } < 1 0 ^ { - 3 } ,
$$

so

$$
\left| p - p _ { n } \right| = \frac { 1 } { n } < 1 0 ^ { - 3 } \Leftrightarrow 1 0 0 0 < n .
$$

$^ *$ 17. Since $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } ( p _ { n } - p _ { n - 1 } ) = \operatorname* { l i m } _ { n \to \infty } 1 / n = 0 } \end{array}$ , the difference in the terms goes to zero. However, $p _ { n }$ is the $_ { n }$ th term of the divergent harmonic series, so $\scriptstyle \operatorname* { l i m } _ { n \to \infty } p _ { n } = \infty$ .

18. Since $- 1 < a < 0$ and $2 < b < 3$ , we have $1 < a + b < 3$ or $1 / 2 < 1 / 2 ( a + b ) < 3 / 2$ in all cases. Further,

$$
\begin{array} { l } { { f ( x ) < 0 , \quad \mathrm { f o r } - 1 < x < 0 \quad \mathrm { a n d } \quad 1 < x < 2 ; } } \\ { { f ( x ) > 0 , \quad \mathrm { f o r } 0 < x < 1 \quad \mathrm { a n d } \quad 2 < x < 3 . } } \end{array}
$$

Thus, $a _ { 1 } = a$ , $f ( a _ { 1 } ) < 0$ , $b _ { 1 } = b$ , and $f ( b _ { 1 } ) > 0$ .

(a) Since $a + b < 2$ , we have $\textstyle p _ { 1 } ~ = ~ { \frac { a + b } { 2 } } $ and $1 / 2 \ < \ p _ { 1 } \ < \ 1$ . Thus, $f ( p _ { 1 } ) > 0$ . Hence, $a _ { 2 } = a _ { 1 } = a$ and $b _ { 2 } = p _ { 1 }$ . The only zero of $f$ in $[ a _ { 2 } , b _ { 2 } ]$ is $p = 0$ , so the convergence will be to $0$ .   
(b) Since $a + b > 2$ , we have $\textstyle p _ { 1 } = { \frac { a + b } { 2 } }$ and $1 < p _ { 1 } < 3 / 2$ . Thus, $f ( p _ { 1 } ) < 0$ . Hence, $a _ { 2 } = p _ { 1 }$ and $b _ { 2 } = b _ { 1 } = b$ . The only zero of $f$ in $[ a _ { 2 } , b _ { 2 } ]$ is $p = 2$ , so the convergence will be to 2.   
(c) Since $a + b = 2$ , we have $\textstyle p _ { 1 } = { \frac { a + b } { 2 } } = 1$ and $f ( p _ { 1 } ) = 0$ . Thus, a zero of $f$ has been found on the first iteration. The convergence is to $p = 1$ .

$^ { * } 1 9$ . The depth of the water is 0.838 ft.

20. The angle $\theta$ changes at the approximate rate $w = - 0 . 3 1 7 0 5 9$ .

# Exercise Set 2.2, page 64

1. For the value of $x$ under consideration we have

$$
x = ( 3 + x - 2 x ^ { 2 } ) ^ { 1 / 4 } \Leftrightarrow x ^ { 4 } = 3 + x - 2 x ^ { 2 } \Leftrightarrow f ( x ) = 0
$$

$$
x = \left( { \frac { x + 3 - x ^ { 4 } } { 2 } } \right) ^ { 1 / 2 } \Leftrightarrow 2 x ^ { 2 } = x + 3 - x ^ { 4 } \Leftrightarrow f ( x ) = 0
$$

$$
x = \left( { \frac { x + 3 } { x ^ { 2 } + 2 } } \right) ^ { 1 / 2 } \Leftrightarrow x ^ { 2 } ( x ^ { 2 } + 2 ) = x + 3 \Leftrightarrow f ( x ) = 0
$$

$$
x = { \frac { 3 x ^ { 4 } + 2 x ^ { 2 } + 3 } { 4 x ^ { 3 } + 4 x - 1 } } \Leftrightarrow 4 x ^ { 4 } + 4 x ^ { 2 } - x = 3 x ^ { 4 } + 2 x ^ { 2 } + 3 \Leftrightarrow f ( x ) = 0
$$

2. (a) p4 = 1.10782; (b) p4 = 0.987506; (c) $p _ { 4 } = 1 . 1 2 3 6 4$ ; (d) $p _ { 4 } = 1 . 1 2 4 1 \dot { 2 }$ ; (b) Part (d) gives the best answer since $| p _ { 4 } - p _ { 3 } |$ is the smallest for (d).

$^ * 3$ . The order in descending speed of convergence is (b), (d), and (a). The sequence in (c) does not converge.

4. The sequence in (c) converges faster than in (d). The sequences in (a) and (b) diverge.

5. With $g ( x ) = ( 3 x ^ { 2 } + 3 ) ^ { 1 / 4 }$ and $p _ { 0 } = 1$ , $p _ { 6 } = 1 . 9 4 3 3 2$ is accurate to within 0.01.

6. With $g ( x ) = \textstyle { \sqrt { 1 + { \frac { 1 } { x } } } }$ and $p _ { 0 } = 1$ , we have $p _ { 4 } = 1 . 3 2 4$ .

7. Since $\begin{array} { r } { g ^ { \prime } ( x ) = \frac { 1 } { 4 } \cos \frac { x } { 2 } } \end{array}$ , $_ { g }$ is continuous and $g ^ { \prime }$ exists on $[ 0 , 2 \pi ]$ . Further, $g ^ { \prime } ( x ) = 0$ only when $x = \pi$ , so that $\begin{array} { r } { g ( 0 ) = g ( 2 \pi ) = \pi \leq g ( x ) = \leq g ( \pi ) = \pi + \frac { 1 } { 2 } } \end{array}$ and $\begin{array} { r } { | g ^ { \prime } ( x ) | \le \frac { 1 } { 4 } } \end{array}$ , for $0 \leq x \leq 2 \pi$ . Theorem 2.3 implies that a unique fixed point $p$ exists in $[ 0 , 2 \pi ]$ . With $\textstyle k = { \frac { 1 } { 4 } }$ and $p _ { 0 } = \pi$ , we have $\begin{array} { r } { p _ { 1 } = \pi + \frac { 1 } { 2 } } \end{array}$ . Corollary 2.5 implies that

$$
| p _ { n } - p | \leq { \frac { k ^ { n } } { 1 - k } } | p _ { 1 } - p _ { 0 } | = { \frac { 2 } { 3 } } \left( { \frac { 1 } { 4 } } \right) ^ { n } .
$$

For the bound to be less than 0.1, we need $n \geq 4$ . However, $p _ { 3 } = 3 . 6 2 6 9 9 6$ is accurate to within 0.01.

8. Using $p _ { 0 } = 1$ gives $p _ { 1 2 } = 0 . 6 4 1 2 0 5 3$ . Since $| g ^ { \prime } ( x ) | = 2 ^ { - x } \ln 2 \leq 0 . 5 5 1$ on $\left\lfloor { \frac { 1 } { 3 } } , 1 \right\rfloor$ with $k = 0 . 5 5 1$ , Corollary 2.5 gives a bound of 16 iterations.

$^ { * } 9$ . For $p _ { 0 } = 1 . 0$ and $\textstyle g ( x ) = 0 . 5 ( x + { \frac { 3 } { x } } )$ , we have $\sqrt { 3 } \approx p _ { 4 } = 1 . 7 3 2 0 5$ .

10. For $g ( x ) = 5 / \sqrt { x }$ and $p _ { 0 } = 2 . 5$ , we have $p _ { 1 4 } = 2 . 9 2 3 9 9$ .

11. (a) With $[ 0 , 1 ]$ and $p _ { 0 } = 0$ , we have $p _ { 9 } = 0 . 2 5 7 5 3 1$ . (b) With [2.5, 3.0] and $p _ { 0 } = 2 . 5$ , we have $p _ { 1 7 } = 2 . 6 9 0 6 5 0$ . (c) With [0.25, 1] and $p _ { 0 } = 0 . 2 5$ , we have $p _ { 1 4 } = 0 . 9 0 9 9 9 9$ . (d) With [0.3, 0.7] and $p _ { 0 } = 0 . 3$ , we have $p _ { 3 9 } = 0 . 4 6 9 6 2 5$ . (e) With [0.3, 0.6] and $p _ { 0 } = 0 . 3$ , we have $p _ { 4 8 } = 0 . 4 4 8 0 5 9$ .

(f) With $[ 0 , 1 ]$ and $p _ { 0 } = 0$ , we have $p _ { 6 } = 0 . 7 0 4 8 1 2$ .

12. The inequalities in Corollary 2.4 give $| p _ { n } - p | < k ^ { n } \operatorname* { m a x } ( p _ { 0 } - a , b - p _ { 0 } )$ . We want

$$
k ^ { n } \operatorname* { m a x } ( p _ { 0 } - a , b - p _ { 0 } ) < 1 0 ^ { - 5 } \quad \mathrm { s o ~ w e ~ n e e d } \quad n > \frac { \ln ( 1 0 ^ { - 5 } ) - \ln ( \operatorname* { m a x } ( p _ { 0 } - a , b - p _ { 0 } ) ) } { \ln k } .
$$

(a) Using $g ( x ) = 2 + \sin { x }$ we have $k = 0 . 9 8 9 9 2 4 9 6 6$ so that with $p _ { 0 } = 2$ we have $n \_ \textgreater$ $\ln ( 0 . 0 0 0 0 1 ) / \ln k = 1 1 4 4 . 6 6 3 2 2 1$ . However, our tolerance is met with $p _ { 6 3 } = 2 . 5 5 4 1 9 9 8$ .   
(b) Using $g ( x ) \ = \ \sqrt [ 3 ] { 2 x + 5 }$ we have $k = 0 . 1 5 4 0 8 0 2 8 3 2$ so that with $p _ { 0 } = 2$ we have $n \_ \textgreater$ $\ln ( 0 . 0 0 0 0 1 ) / \ln k = 6 . 1 5 5 7 1 8 0 0 5$ . However, our tolerance is met with $p _ { 6 } = 2 . 0 9 4 5 5 0 3$ .   
\*(c) Using $g ( x ) = \sqrt { e ^ { x } / 3 }$ and the interval $[ 0 , 1 ]$ we have $k = \ 0 . 4 7 5 9 4 4 8 3 4 7$ so that with $p _ { 0 } = 1$ we have $n > \ln ( 0 . 0 0 0 0 1 ) / \ln k = 1 5 . 5 0 6 5 9 8 2 9$ . However, our tolerance is met with $p _ { 1 2 } = 0 . 9 1 0 0 1 4 9 6$ .   
(d) Using $g ( x ) = \cos x$ and the interval $[ 0 , 1 ]$ we have $k = 0 . 8 4 1 4 7 0 9 8 4 8$ so that with $p _ { 0 } = 0$ we have $n > \ln ( 0 . 0 0 0 0 1 ) / \ln k > 6 6 . 7 0 1 4 8 0 7 4 .$ . However, our tolerance is met with $p _ { 3 0 } =$ 0.73908230.

13. For $g ( x ) = ( 2 x ^ { 2 } - 1 0 \cos x ) / ( 3 x )$ , we have the following:

$$
p _ { 0 } = 3 \Rightarrow p _ { 8 } = 3 . 1 6 1 9 3 ; \quad p _ { 0 } = - 3 \Rightarrow p _ { 8 } = - 3 . 1 6 1 9 3 .
$$

For $g ( x ) = \operatorname { a r c c o s } ( - 0 . 1 x ^ { 2 } )$ , we have the following:

$$
p _ { 0 } = 1 \Rightarrow p _ { 1 1 } = 1 . 9 6 8 8 2 ; \quad p _ { 0 } = - 1 \Rightarrow p _ { 1 1 } = - 1 . 9 6 8 8 2 .
$$

$^ { * } 1 4$ . For $g ( x ) = { \frac { 1 } { \tan x } } - { \frac { 1 } { x } } + x$ and $p _ { 0 } = 4$ , we have $p _ { 4 } = 4 . 4 9 3 4 0 9$ .

15. With $g ( x ) = { \frac { 1 } { \pi } } \arcsin \left( - { \frac { x } { 2 } } \right) + 2$ , we have $p _ { 5 } = 1 . 6 8 3 8 5 5$

16. (a) If fixed-point iteration converges to the limit $p$ , then

$$
p = \operatorname * { l i m } _ { n  \infty } p _ { n } = \operatorname * { l i m } _ { n  \infty } 2 p _ { n - 1 } - A p _ { n - 1 } ^ { 2 } = 2 p - A p ^ { 2 } .
$$

Solving for p gives p = 1 .

(b) Any subinterval $[ c , d ]$ of $\left( { \frac { 1 } { 2 A } } , { \frac { 3 } { 2 A } } \right)$ containing $\frac { 1 } { A }$ suffices.

Since

$$
g ( x ) = 2 x - A x ^ { 2 } , \quad g ^ { \prime } ( x ) = 2 - 2 A x ,
$$

so $g ( x )$ is continuous, and $g ^ { \prime } ( x )$ exists. Further, $g ^ { \prime } ( x ) = 0$ only if $x = { \frac { 1 } { A } }$ .

Since

$$
g \left( { \frac { 1 } { A } } \right) = { \frac { 1 } { A } } , \quad g \left( { \frac { 1 } { 2 A } } \right) = g \left( { \frac { 3 } { 2 A } } \right) = { \frac { 3 } { 4 A } } , { \mathrm { a n d ~ w e ~ h a v e } } { \frac { 3 } { 4 A } } \leq g ( x ) \leq { \frac { 1 } { A } } .
$$

For $x$ in $\textstyle \left( { \frac { 1 } { 2 A } } , { \frac { 3 } { 2 A } } \right)$ , we have

$$
\left| x - { \frac { 1 } { A } } \right| < { \frac { 1 } { 2 A } } \quad { \mathrm { s o } } \quad | g ^ { \prime } ( x ) | = 2 A \left| x - { \frac { 1 } { A } } \right| < 2 A \left( { \frac { 1 } { 2 A } } \right) = 1 .
$$

17. One of many examples is $g ( x ) = \sqrt { 2 x - 1 }$ on $\left[ { \frac { 1 } { 2 } } , 1 \right]$ .

$^ *$ 18. (a) The proof of existence is unchanged. For uniqueness, suppose $p$ and $q$ are fixed points in $[ a , b ]$ with $p \neq q$ . By the Mean Value Theorem, a number $\xi$ in $( a , b )$ exists with

$$
\begin{array} { r } { = g ( p ) - g ( q ) = g ^ { \prime } ( \xi ) ( p - q ) \le k ( p - q ) < p - q } \end{array}
$$

giving the same contradiction as in Theorem 2.3.

(b) Consider $g ( x ) = 1 - x ^ { 2 }$ on $[ 0 , 1 ]$ . The function $g$ has the unique fixed point

$$
p = { \frac { 1 } { 2 } } \left( - 1 + { \sqrt { 5 } } \right) .
$$

With $p _ { 0 } = 0 . 7$ , the sequence eventually alternates between $0$ and $1$ .

\*19. (a) Suppose that $x _ { 0 } > { \sqrt { 2 } }$ . Then

$$
x _ { 1 } - { \sqrt { 2 } } = g ( x _ { 0 } ) - g \left( { \sqrt { 2 } } \right) = g ^ { \prime } ( \xi ) \left( x _ { 0 } - { \sqrt { 2 } } \right) ,
$$

where $\sqrt { 2 } < \xi < x _ { 0 }$ . Thus, $x _ { 1 } - { \sqrt { 2 } } > 0$ and $x _ { 1 } > \sqrt { 2 }$ . Further,

$$
x _ { 1 } = { \frac { x _ { 0 } } { 2 } } + { \frac { 1 } { x _ { 0 } } } < { \frac { x _ { 0 } } { 2 } } + { \frac { 1 } { \sqrt { 2 } } } = { \frac { x _ { 0 } + { \sqrt { 2 } } } { 2 } }
$$

and ${ \sqrt { 2 } } < x _ { 1 } < x _ { 0 }$ . By an inductive argument,

$$
\sqrt { 2 } < x _ { m + 1 } < x _ { m } < . ~ . ~ . < x _ { 0 } .
$$

Thus, $\{ x _ { m } \}$ is a decreasing sequence which has a lower bound and must converge.

Suppose $p = \mathrm { l i m } _ { m  \infty } x _ { m }$ . Then

$$
p = \operatorname* { l i m } _ { m \to \infty } \left( { \frac { x _ { m - 1 } } { 2 } } + { \frac { 1 } { x _ { m - 1 } } } \right) = { \frac { p } { 2 } } + { \frac { 1 } { p } } . \quad { \mathrm { T h u s } } \quad p = { \frac { p } { 2 } } + { \frac { 1 } { p } } ,
$$

which implies that $p = \pm { \sqrt { 2 } }$ . Since $x _ { m } > \sqrt { 2 }$ for all $m$ , we have $\begin{array} { r } { \operatorname* { l i m } _ { m \to \infty } x _ { m } = \sqrt { 2 } } \end{array}$

(b) We have

$$
0 < \Big ( x _ { 0 } - \sqrt { 2 } \Big ) ^ { 2 } = x _ { 0 } ^ { 2 } - 2 x _ { 0 } \sqrt { 2 } + 2 ,
$$

$2 x _ { 0 } \sqrt { 2 } < x _ { 0 } ^ { 2 } + 2$ and $\begin{array} { r } { \sqrt { 2 } < \frac { x _ { 0 } } { 2 } + \frac { 1 } { x _ { 0 } } = x _ { 1 } } \end{array}$

(c) Case 1: $0 < x _ { 0 } < { \sqrt { 2 } }$ , which implies that ${ \sqrt { 2 } } < x _ { 1 }$ by part (b). Thus,

$$
0 < x _ { 0 } < \sqrt { 2 } < x _ { m + 1 } < x _ { m } < \ldots < x _ { 1 } \quad \mathrm { a n d } \quad \operatorname * { l i m } _ { m \to \infty } x _ { m } = \sqrt { 2 } .
$$

Case 2: $x _ { 0 } = { \sqrt { 2 } }$ , which implies that $x _ { m } = { \sqrt { 2 } }$ for all $m$ and $\begin{array} { r } { \operatorname* { l i m } _ { m \to \infty } x _ { m } = \sqrt { 2 } } \end{array}$

Case 3: $x _ { 0 } > { \sqrt { 2 } }$ , which by part (a) implies that $\begin{array} { r } { \operatorname* { l i m } _ { m  \infty } x _ { m } = \sqrt { 2 } } \end{array}$

20. (a) Let

$$
g ( x ) = \frac { x } { 2 } + \frac { A } { 2 x } .
$$

Note that $g \left( { \sqrt { A } } \right) = { \sqrt { A } }$ . Also,

$$
\begin{array} { r } { g ^ { \prime } ( x ) = 1 / 2 - A / \left( 2 x ^ { 2 } \right) \mathrm { ~ i f ~ } x \neq 0 \quad \mathrm { a n d } \quad g ^ { \prime } ( x ) > 0 \mathrm { ~ i f ~ } x > \sqrt { A } . } \end{array}
$$

If $x _ { 0 } = { \sqrt { A } }$ , then $x _ { m } = { \sqrt { A } }$ for all $m$ and $\begin{array} { r } { \operatorname* { l i m } _ { m  \infty } x _ { m } = \sqrt { A } } \end{array}$

If $x _ { 0 } > A$ , then

$$
x _ { 1 } - { \sqrt { A } } = g ( x _ { 0 } ) - g \left( { \sqrt { A } } \right) = g ^ { \prime } ( \xi ) \left( x _ { 0 } - { \sqrt { A } } \right) > 0 .
$$

Further,

$$
x _ { 1 } = { \frac { x _ { 0 } } { 2 } } + { \frac { A } { 2 x _ { 0 } } } < { \frac { x _ { 0 } } { 2 } } + { \frac { A } { 2 { \sqrt { A } } } } = { \frac { 1 } { 2 } } \left( x _ { 0 } + { \sqrt { A } } \right) .
$$

Thus, ${ \sqrt { A } } < x _ { 1 } < x _ { 0 }$ . Inductively,

$$
\sqrt { A } < x _ { m + 1 } < x _ { m } < . ~ . ~ . < x _ { 0 }
$$

and $\begin{array} { r } { \operatorname* { l i m } _ { m  \infty } x _ { m } = \sqrt { A } } \end{array}$ by an argument similar to that in Exercise 19(a). If $0 < x _ { 0 } < { \sqrt { A } }$ , then

$$
0 < \left( x _ { 0 } - \sqrt { A } \right) ^ { 2 } = x _ { 0 } ^ { 2 } - 2 x _ { 0 } \sqrt { A } + A \quad \mathrm { a n d } \quad 2 x _ { 0 } \sqrt { A } < x _ { 0 } ^ { 2 } + A ,
$$

which leads to

$$
\sqrt { A } < \frac { x _ { 0 } } { 2 } + \frac { A } { 2 x _ { 0 } } = x _ { 1 } .
$$

Thus

$$
0 < x _ { 0 } < \sqrt { A } < x _ { m + 1 } < x _ { m } < . . . < x _ { 1 } ,
$$

and by the preceding argument, $\begin{array} { r } { \operatorname* { l i m } _ { m  \infty } x _ { m } = \sqrt { A } } \end{array}$

(b) If $x _ { 0 } < 0$ , then $\begin{array} { r } { \operatorname* { l i m } _ { m  \infty } x _ { m } = - \sqrt { A } } \end{array}$ .

21. Replace the second sentence in the proof with: “Since $g$ satisfies a Lipschitz condition on $[ a , b ]$ with a Lipschitz constant $L < 1$ , we have, for each $n$ ,

$$
| p _ { n } - p | = | g ( p _ { n - 1 } ) - g ( p ) | \leq L | p _ { n - 1 } - p | .
$$

The rest of the proof is the same, with $k$ replaced by $L$ .

22. Let $\varepsilon = ( 1 - | g ^ { \prime } ( p ) | ) / 2$ . Since $g ^ { \prime }$ is continuous at $p$ , there exists a number $\delta > 0$ such that for $x \in [ p - \delta , p + \delta ]$ , we have $| g ^ { \prime } ( x ) - g ^ { \prime } ( p ) | < \varepsilon$ . Thus, $| g ^ { \prime } ( x ) | < | g ^ { \prime } ( p ) | + \varepsilon < 1$ for $x \in \lfloor p - \delta , p + \delta \rfloor$ . By the Mean Value Theorem

$$
| g ( x ) - g ( p ) | = | g ^ { \prime } ( c ) | | x - p | < | x - p | .
$$

for $x \in [ p - \delta , p + \delta ]$ . Applying the Fixed-Point Theorem completes the problem.

23. With $g ( t ) = 5 0 1 . 0 6 2 5 - 2 0 1 . 0 6 2 5 e ^ { - 0 . 4 t }$ and $p _ { 0 } = 5 . 0 , \ p _ { 3 } = 6 . 0 0 2 8$ is within 0.01 s of the actual time.

$^ { * } 2 4$ . Since $g ^ { \prime }$ is continuous at $p$ and $| g ^ { \prime } ( p ) | > 1$ , by letting $\epsilon = | g ^ { \prime } ( p ) | - 1$ there exists a number $\delta > 0$ such that $| g ^ { \prime } ( x ) - g ^ { \prime } ( p ) | < | g ^ { \prime } ( p ) | - 1$ whenever $0 < | x - p | < \delta$ . Hence, for any $x$ satisfying $0 < | x - p | < \delta$ , we have

$$
| g ^ { \prime } ( x ) | \geq | g ^ { \prime } ( p ) | - | g ^ { \prime } ( x ) - g ^ { \prime } ( p ) | > | g ^ { \prime } ( p ) | - ( | g ^ { \prime } ( p ) | - 1 ) = 1 .
$$

If $p _ { 0 }$ is chosen so that $0 < | p - p _ { 0 } | < \delta$ , we have by the Mean Value Theorem that

$$
| p _ { 1 } - p | = | g ( p _ { 0 } ) - g ( p ) | = | g ^ { \prime } ( \xi ) | | p _ { 0 } - p | ,
$$

for some $\xi$ between $p _ { 0 }$ and $p$ . Thus, $0 < | p - \xi | < \delta$ so $| p _ { 1 } - p | = | g ^ { \prime } ( \xi ) | | p _ { 0 } - p | > | p _ { 0 } - p |$

# Exercise Set 2.3, page 75

\*1. $p _ { 2 } = 2 . 6 0 7 1 4$

2. $p _ { 2 } = - 0 . 8 6 5 6 8 4$ ; If $p _ { 0 } = 0$ , $f ^ { \prime } ( p _ { 0 } ) = 0$ and $p _ { 1 }$ cannot be computed.

\*3. (a) 2.45454 (b) 2.44444 (c) Part (a) is better.

4. (a) −1.25208   
(b) −0.841355

5. (a) For $p _ { 0 } = 2$ , we have $p _ { 5 } = 2 . 6 9 0 6 5$ . (b) For $p _ { 0 } = - 3$ , we have $p _ { 3 } = - 2 . 8 7 9 3 9$ . \*(c) For $p _ { 0 } = 0$ , we have $p _ { 4 } = 0 . 7 3 9 0 9$ . (d) For $p _ { 0 } = 0$ , we have $p _ { 3 } = 0 . 9 6 4 3 4$ .

6. (a) For $p _ { 0 } = 1$ , we have $p _ { 8 } = 1 . 8 2 9 3 8 4$ . (b) For $p _ { 0 } = 1 . 5$ , we have $p _ { 4 } = 1 . 3 9 7 7 4 8$ . (c) For $p _ { 0 } = 2$ , we have $p _ { 4 } = 2 . 3 7 0 6 8 7$ ; and for $p _ { 0 } = 4$ , we have $p _ { 4 } =  { \mathrm { 3 . 7 2 2 1 1 3 } }$ . (d) For $p _ { 0 } = 1$ , we have $p _ { 4 } = 1 . 4 1 2 3 9 1$ ; and for $p _ { 0 } = 4$ , we have $p _ { 5 } = 3 . 0 5 7 1 0 4$ . (e) For $p _ { 0 } = 1$ , we have $p _ { 4 } = 0 . 9 1 0 0 0 8$ ; and for $p _ { 0 } = 3$ , we have $p _ { 9 } = 3 . 7 3 3 0 7 9$ . (f) For $p _ { 0 } = 0$ , we have $p _ { 4 } = 0 . 5 8 8 5 3 3$ ; for $p _ { 0 } = 3$ , we have $p _ { 3 } = 3 . 0 9 6 3 6 4$ ; and for $p _ { 0 } = 6$ , we have $p _ { 3 } = 6 . 2 8 5 0 4 9$ .

7. Using the endpoints of the intervals as $p _ { 0 }$ and $p _ { 1 }$ , we have:

(a) $p _ { 1 1 } = 2 . 6 9 0 6 5$ (b) $p _ { 7 } = - 2 . 8 7 9 3 9$ \*(c) $p _ { 6 } = 0 . 7 3 9 0 9$ (d) $p _ { 5 } = 0 . 9 6 4 3 3$

8. Using the endpoints of the intervals as $p _ { 0 }$ and $p _ { 1 }$ , we have:

(a) $p _ { 7 } = 1 . 8 2 9 3 8 4$   
(b) $p _ { 9 } = 1 . 3 9 7 7 4 9$   
(c) $p _ { 6 } = 2 . 3 7 0 6 8 7 ; p _ { 7 } = 3 . 7 2 2 1 1 3$   
(d) $p _ { 8 } = 1 . 4 1 2 3 9 1 ; p _ { 7 } = 3 . 0 5 7 1 0 4$   
(e) $p _ { 6 } = 0 . 9 1 0 0 0 8 ; p _ { 1 0 } = 3 . 7 3 3 0 7 9$   
(f) $p _ { 6 } = 0 . 5 8 8 5 3 3 ; p _ { 5 } = 3 . 0 9 6 3 6 4 ; p _ { 5 } = 6 . 2 8 5 0 4 9$

9. Using the endpoints of the intervals as $p _ { 0 }$ and $p _ { 1 }$ , we have:

(a) $p _ { 1 6 } = 2 . 6 9 0 6 0$ (b) $p _ { 6 } = - 2 . 8 7 9 3 8$ \*(c) $p _ { 7 } = 0 . 7 3 9 0 8$ (d) $p _ { 6 } = 0 . 9 6 4 3 3$

10. Using the endpoints of the intervals as $p _ { 0 }$ and $p _ { 1 }$ , we have:

(a) $p _ { 8 } = 1 . 8 2 9 3 8 3$   
(b) $p _ { 9 } = 1 . 3 9 7 7 4 9$   
(c) $p _ { 6 } = 2 . 3 7 0 6 8 7 ; p _ { 8 } = 3 . 7 2 2 1 1 2$   
(d) $p _ { 1 0 } = 1 . 4 1 \dot { 2 } \dot { 3 } 9 \dot { 2 } ; p _ { 1 2 } = \dot { 3 } . 0 5 7 0 9 9$   
(e) $p _ { 7 } = 0 . 9 1 0 0 0 8 ; p _ { 2 9 } = 3 . 7 3 3 0 6 5$   
(f) $p _ { 9 } = 0 . 5 8 8 5 3 3 ; p _ { 5 } = 3 . 0 9 6 3 6 4 ; p _ { 5 } = 6 . 2 8 5 0 4 9$

11. (a) Newton’s method with $p _ { 0 } = 1 . 5$ gives $p _ { 3 } = 1 . 5 1 2 1 3 4 5 5$ . The Secant method with $p _ { 0 } = 1$ and $p _ { 1 } = 2$ gives $p _ { 1 0 } = 1 . 5 1 2 1 3 4 5 5$ . The Method of False Position with $p _ { 0 } = 1$ and $p _ { 1 } = 2$ gives $p _ { 1 7 } = 1 . 5 1 2 1 2 9 5 4$ . (b) Newton’s method with $p _ { 0 } = 0 . 5$ gives $p _ { 5 } = 0 . 9 7 6 7 7 3 0 1 7$ . The Secant method with $p _ { 0 } = 0$ and $p _ { 1 } = 1$ gives $p _ { 5 } = 1 0 . 9 7 6 7 7 3 0 1 7 $ . The Method of False Position with $p _ { 0 } = 0$ and $p _ { 1 } = 1$ gives $p _ { 5 } = 0 . 9 7 6 7 7 2 9 7 6$ .

12. (a) We have

<table><tr><td></td><td>Initial Approximation</td><td>Result</td><td>Initial Approximation</td><td>Result</td></tr><tr><td>Newton's</td><td>po = 1.5</td><td>P4 = 1.41239117</td><td>po = 3.0</td><td>P4 = 3.05710355</td></tr><tr><td>Secant</td><td>po= 1,p1 = 2</td><td>P8 = 1.41239117</td><td>po = 2,p1= 4</td><td>P10 = 3.05710355</td></tr><tr><td>False Position</td><td>p0 = 1,p1 = 2</td><td>P13 = 1.41239119</td><td>po = 2,p1= 4</td><td>P19 = 3.05710353</td></tr><tr><td>Newton's</td><td>po = 0.25</td><td>P4 = 0.206035120</td><td>po = 0.75</td><td>P4 = 0.681974809</td></tr><tr><td>Secant</td><td>po = 0,p1 = 0.5</td><td>Pg = 0.206035120</td><td>Po = 0.5,p1 = 1</td><td>P8 = 0.681974809</td></tr><tr><td>False Position</td><td>Po = 0,p1 = 0.5</td><td>P12 = 0.206035125</td><td>po = 0.5,p1 = 1</td><td>P15 = 0.681974791</td></tr></table>

\*13. For $p _ { 0 } = 1$ , we have $p _ { 5 } = 0 . 5 8 9 7 5 5$ . The point has the coordinates (0.589755, 0.347811).

14. For $p _ { 0 } = 2$ , we have $p _ { 2 } = 1 . 8 6 6 7 6 0$ . The point is (1.866760, 0.535687).

15. The equation of the tangent line is

$$
y - f ( p _ { n - 1 } ) = f ^ { \prime } ( p _ { n - 1 } ) ( x - p _ { n - 1 } ) .
$$

To complete this problem, set $y = 0$ and solve for $x = p _ { n }$ $^ *$ 16. Newton’s method gives $p _ { 1 5 } = 1 . 8 9 5 4 8 8$ , for $\begin{array} { r } { p _ { 0 } = \frac { \pi } { 2 } } \end{array}$ ; and $p _ { 1 9 } = 1 . 8 9 5 4 8 9$ , for $p _ { 0 } = 5 \pi$ . The sequence does not converge in 200 iterations for $p _ { 0 } = 1 0 \pi$ . The results do not indicate the fast convergence usually associated with Newton’s method.

17. (a) For $p _ { 0 } = - 1$ and $p _ { 1 } = 0$ , we have $p _ { 1 7 } = - 0 . 0 4 0 6 5 8 5 0$ , and for $p _ { 0 } = 0$ and $p _ { 1 } = 1$ , we have $p _ { 9 } = 0 . 9 6 2 3 9 8 4$ . (b) For $p _ { 0 } = - 1$ and $p _ { 1 } = 0$ , we have $p _ { 5 } = - 0 . 0 4 0 6 5 9 2 9$ , and for $p _ { 0 } = 0$ and $p _ { 1 } = 1$ , we have $p _ { 1 2 } = - 0 . 0 4 0 6 5 9 2 9$ . (c) For $p _ { 0 } = - 0 . 5$ , we have $p _ { 5 } = - 0 . 0 4 0 6 5 9 2 9$ , and for $p _ { 0 } = 0 . 5$ , we have $p _ { 2 1 } = 0 . 9 6 2 3 9 8 9$ .

18. (a) The Bisection method yields $p _ { 1 0 } = 0 . 4 4 7 6 5 6 3$ . (b) The method of False Position yields $p _ { 1 0 } = 0 . 4 4 2 0 6 7$ . (c) The Secant method yields $p _ { 1 0 } = - 1 9 5 . 8 9 5 0$ .

$^ { * } 1 9$ . This formula involves the subtraction of nearly equal numbers in both the numerator and denominator if $p _ { n - 1 }$ and $p _ { n - 2 }$ are nearly equal.

20. Newton’s method for the various values of $p _ { 0 }$ gives the following results.

(a) $p _ { 8 } = - 1 . 3 7 9 3 6 5$ (b) $p _ { 7 } = - 1 . 3 7 9 3 6 5$ (c) $p _ { 7 } = 1 . 3 7 9 3 6 5$ (d) $p _ { 7 } = - 1 . 3 7 9 3 6 5$ (e) $p _ { 7 } = 1 . 3 7 9 3 6 5$ (f) $p _ { 8 } = 1 . 3 7 9 3 6 5$

21. Newton’s method for the various values of $p _ { 0 }$ gives the following results.

(a) $p _ { 0 } = - 1 0 , p _ { 1 1 } = - 4 . 3 0 6 2 4 5 2 7$   
(b) $p _ { 0 } = - 5 , p _ { 5 } = - 4 . 3 0 6 2 4 5 2 7$   
(c) $p _ { 0 } = - 3 , p _ { 5 } = 0 . 8 2 4 4 9 8 5 8 5$   
(d) $p _ { 0 } = - 1 , p _ { 4 } = - 0 . 8 2 4 4 9 8 5 8 5$   
(e) $p _ { 0 } = 0$ , $p _ { 1 }$ cannot be computed because $f ^ { \prime } ( 0 ) = 0$   
(f) $p _ { 0 } = 1 , p _ { 4 } = 0 . 8 2 4 4 9 8 5 8 5$   
(g) $p _ { 0 } = 3 , p _ { 5 } = - 0 . 8 2 4 4 9 8 5 8 5$   
(h) $p _ { 0 } = 5 , p _ { 5 } = 4 . 3 0 6 2 4 5 2 7$   
(i) $p _ { 0 } = 1 0 , p _ { 1 1 } = 4 . 3 0 6 2 4 5 2 7$

$^ { * } 2 2$ . The required accuracy is met in 7 iterations of Newton’s method.

$^ { * } 2 3$ . For $f ( x ) = \ln ( x ^ { 2 } + 1 ) - e ^ { 0 . 4 x } \cos \pi x$ , we have the following roots.

(a) For $p _ { 0 } = - 0 . 5$ , we have $p _ { 3 } = - 0 . 4 3 4 1 4 3 1$ .   
(b) For $p _ { 0 } = 0 . 5$ , we have $p _ { 3 } = 0 . 4 5 0 6 5 6 7$ . For $p _ { 0 } = 1 . 5$ , we have $p _ { 3 } = 1 . 7 4 4 7 3 8 1$ . For $p _ { 0 } = 2 . 5$ , we have $p _ { 5 } = 2 . 2 3 8 3 1 9 8$ . For $p _ { 0 } = 3 . 5$ , we have $p _ { 4 } = 3 . 7 0 9 0 4 1 \mathrm { : }$ .   
(c) The initial approximation $n - 0 . 5$ is quite reasonable.   
(d) For $p _ { 0 } = 2 4 . 5$ , we have $p _ { 2 } = 2 4 . 4 9 9 8 8 7 0$ .

24. We have $\lambda \approx 0 . 1 0 0 9 9 8$ and ${ \cal N } ( 2 ) \approx 2 , 1 8 7 , 9 5 0$ .

25. The two numbers are approximately 6.512849 and 13.487151.

$^ { * } 2 6$ . The minimal annual interest rate is 6.67%.

27. The borrower can afford to pay at most $8 . 1 0 \%$ .

$^ *$ 28. (a) $\textstyle { \frac { 1 } { 3 } } e , t = 3$ hours (b) 11 hours and 5 minutes (c) 21 hours and 14 minutes $^ { * } 2 9$ . (a) First define the function by

$$
f : = x  3 ^ { ( 3 x + 1 ) } - 7 ~ 5 ^ { 2 x }
$$

$$
- { \frac { \ln \left( 3 / 7 \right) } { \ln \left( 2 7 / 2 5 \right) } }
$$

$$
\mathrm { f s o l v e } ( 3 ^ { ( 3 x + 1 ) } - 7 5 ^ { ( 2 x ) } = 0 , x )
$$

The procedure solve gives the exact solution, and fsolve fails because the negative $x$ -axis is an asymptote for the graph of $f ( x )$ .

(b) Using the Maple command $p l o t ( \{ f ( x ) \} , x = 1 0 . 5 . 1 1 . 5 )$ produces the following graph.

![](images/30d70941eaeee1bf5d1b8c3f05f0cf9d98635e34d49665fd5a62f71b653b4d97.jpg)

(c) Define $f ^ { \prime } ( x )$ using

$f p : = x - > ( D ) ( f ) ( x )$

$$
f p : = x \to 3 \ 3 ^ { ( 3 x + 1 ) } \ln ( 3 ) - 1 4 \ 5 ^ { ( 2 x ) } \ln ( 5 )
$$

$$
p 0 : = 1 1
$$

for $i$ from $^ { 1 }$ to 5 do   
$p 1 : = e v a l f ( p 0 - f ( p 0 ) / f p ( p 0 ) )$   
$e r r : = a b s ( p 1 - p 0 )$   
$p 0 : = p 1$   
od   
The results are given in the following table.

<table><tr><td>i</td><td>Pi</td><td>|Pi-Pi-1l</td></tr><tr><td>1</td><td>11.0097380401552503</td><td>.0097380401552503</td></tr><tr><td>2</td><td>11.0094389359662827</td><td>.0002991041889676</td></tr><tr><td>3</td><td>11.0094386442684488</td><td>.2916978339 10-6</td></tr><tr><td>4</td><td>11.0094386442681716</td><td>.2772 10-2</td></tr><tr><td>5</td><td>11.0094386442681716</td><td>0</td></tr></table>

(d) We have $3 ^ { 3 x + 1 } = 7 \cdot 5 ^ { 2 x }$ . Taking the natural logarithm of both sides gives

$$
( 3 x + 1 ) \ln 3 = \ln 7 + 2 x \ln 5 .
$$

Thus

$$
3 x \ln 3 - 2 x \ln 5 = \ln 7 - \ln 3 , \quad x ( 3 \ln 3 - 2 \ln 5 ) = \ln { \frac { 7 } { 3 } } ,
$$

and

$$
x = { \frac { \ln 7 / 3 } { \ln 2 7 - \ln 2 5 } } = { \frac { \ln 7 / 3 } { \ln 2 7 / 2 5 } } = - { \frac { \ln 3 / 7 } { \ln 2 7 / 2 5 } } .
$$

This agrees with part (a).

30. (a) $s o l v e ( 2 ^ { x ^ { 2 } } - 3 \cdot 7 ^ { ( x + 1 ) } , x )$ fails and $f s o l v e ( 2 ^ { x ^ { 2 } } - 3 \cdot 7 ^ { ( x + 1 ) } , x )$ returns −1.118747530. (b) $p l o t ( 2 ^ { x ^ { 2 } } - 3 \cdot 7 ^ { ( x + 1 ) } , x = - 2 . 4 )$ shows there is also a root near $x = 4$ . (c) With $p _ { 0 } ~ = ~ 1$ , $p _ { 4 } \ = \ - 1 . 1 1 8 7 4 7 5 3 0 3 9 8 8 9 6 3$ is accurate to $1 0 ^ { - 1 6 }$ ; with $p _ { 0 } ~ = ~ 4$ , $p _ { 6 } ~ =$ 3.9261024524565005 is accurate to $1 0 ^ { - 1 6 }$ (d) The roots are

$$
\frac { \ln ( 7 ) \pm { \sqrt { [ \ln ( 7 ) ] ^ { 2 } + 4 \ln ( 2 ) \ln ( 4 ) } } } { 2 \ln ( 2 ) } .
$$

31. We have $P _ { L } = 2 6 5 8 1 6$ , $c = - 0 . 7 5 6 5 8 1 2 5$ , and $k = 0 . 0 4 5 0 1 7 5 0 2$ . The 1980 population is $P ( 3 0 ) = 2 2 2 , 2 4 8 , 3 2 0$ , and the 2010 population is $P ( 6 0 ) = 2 5 2 , 9 6 7 , 0 3 0$ .

32. $P _ { L } = 2 9 0 2 2 8$ , $c = 0 . 6 5 1 2 2 9 9$ , and $k = 0 . 0 3 0 2 0 0 2 8$ ; The 1980 population is $P ( 3 0 ) = 2 2 3 , 0 6 9 , 2 1 0$ , and the 2010 population is $P ( 6 0 ) = 2 6 0 , 9 4 3 , 8 0 6$ .

33. Using $p _ { 0 } = 0 . 5$ and $p _ { 1 } = 0 . 9$ , the Secant method gives $p _ { 5 } = 0 . 8 4 2$ .

34. (a) We have, approximately,

$$
A = 1 7 . 7 4 , \quad B = 8 7 . 2 1 , \quad C = 9 . 6 6 , \quad \mathrm { a n d } \quad E = 4 7 . 4 7
$$

With these values we have

$$
\displaystyle \mathrm { i n } \alpha \cos \alpha + B \sin ^ { 2 } \alpha - C \cos \alpha - E \sin \alpha = 0 . 0 2
$$

(b) Newton’s method gives $\alpha \approx 3 3 . 2 ^ { \circ }$ .

# Exercise Set 2.4, page 85

1. \*(a) For $p _ { 0 } = 0 . 5$ , we have $p _ { 1 3 } = 0 . 5 6 7 1 3 5$ . (b) For $p _ { 0 } = - 1 . 5$ , we have $p _ { 2 3 } = - 1 . 4 1 4 3 2 5$ . (c) For $p _ { 0 } = 0 . 5$ , we have $p _ { 2 2 } = 0 . 6 4 1 1 6 6$ . (d) For $p _ { 0 } = - 0 . 5$ , we have $p _ { 2 3 } = - 0 . 1 8 3 2 7 4$ .

2. (a) For $p _ { 0 } = 0 . 5$ , we have $p _ { 1 5 } = 0 . 7 3 9 0 7 6 5 8 9$ . (b) For $p _ { 0 } = - 2 . 5$ , we have $p _ { 9 } = - 1 . 3 3 4 3 4 5 9 4$ . (c) For $p _ { 0 } = 3 . 5$ , we have $p _ { 5 } = 3 . 1 4 1 5 6 7 9 3$ . (d) For $p _ { 0 } = 4 . 0$ , we have $p _ { 4 4 } = 3 . 3 7 3 5 4 1 9 0$ .

3. Modified Newton’s method in Eq. (2.11) gives the following:

\*(a) For $p _ { 0 } = 0 . 5$ , we have $p _ { 3 } = 0 . 5 6 7 1 4 3$ .   
(b) For $p _ { 0 } = - 1 . 5$ , we have $p _ { 2 } = - 1 . 4 1 4 1 5 8$ .   
(c) For $p _ { 0 } = 0 . 5$ , we have $p _ { 3 } = 0 . 6 4 1 2 7 4$ .   
(d) For $p _ { 0 } = - 0 . 5$ , we have $p _ { 5 } = - 0 . 1 8 3 3 1 9$ .

4. (a) For $p _ { 0 } = 0 . 5$ , we have $p _ { 4 } = 0 . 7 3 9 0 8 7 4 3 9$ . (b) For $p _ { 0 } = - 2 . 5$ , we have $p _ { 5 3 } = - 1 . 3 3 4 3 4 5 9 4$ . (c) For $p _ { 0 } = 3 . 5$ , we have $p _ { 5 } = 3 . 1 4 1 5 6 7 9 3$ . (d) For $p _ { 0 } = 4 . 0$ , we have $p _ { 3 } = - 3 . 7 2 9 5 7 6 3 9$ .

5. Newton’s method with $p _ { 0 } ~ = ~ - 0 . 5$ gives $p _ { 1 3 } = - 0 . 1 6 9 6 0 7$ . Modified Newton’s method in Eq. (2.11) with $p _ { 0 } = - 0 . 5$ gives $p _ { 1 1 } = - 0 . 1 6 9 6 0 7$ .

6. $^ { * } ( \mathrm { a } )$ Since

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p | } { | p _ { n } - p | } } = \operatorname* { l i m } _ { n \to \infty } { \frac { \frac { 1 } { n + 1 } } { \frac { 1 } { n } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { n } { n + 1 } } = 1 ,
$$

we have linear convergence. To have $| p _ { n } - p | < 5 \times 1 0 ^ { - 2 }$ , we need $n \geq 2 0$ .

(b) Since

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p | } { | p _ { n } - p | } } = \operatorname* { l i m } _ { n \to \infty } { \frac { \frac { 1 } { ( n + 1 ) ^ { 2 } } } { \frac { 1 } { n ^ { 2 } } } } = \operatorname* { l i m } _ { n \to \infty } \left( { \frac { n } { n + 1 } } \right) ^ { 2 } = 1 ,
$$

we have linear convergence. To have $| p _ { n } - p | < 5 \times 1 0 ^ { - 2 }$ , we need $n \geq 5$

7. (a) For $k > 0$ ,

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - 0 | } { | p _ { n } - 0 | } } = \operatorname* { l i m } _ { n \to \infty } { \frac { \frac { 1 } { ( n + 1 ) ^ { k } } } { \frac { 1 } { n ^ { k } } } } = \operatorname* { l i m } _ { n \to \infty } \left( { \frac { n } { n + 1 } } \right) ^ { k } = 1 ,
$$

so the convergence is linear.

(b) We need to have $N > 1 0 ^ { m / k }$ .

$^ { * } 8$ . (a) Since

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - 0 | } { | p _ { n } - 0 | ^ { 2 } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { 1 0 ^ { - 2 ^ { n + 1 } } } { \left( 1 0 ^ { - 2 ^ { n } } \right) ^ { 2 } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { 1 0 ^ { - 2 ^ { n + 1 } } } { 1 0 ^ { - 2 ^ { n + 1 } } } } = 1 ,
$$

the sequence is quadratically convergent.

(b) We have

$$
\begin{array} { r l r } {  { \operatorname* { l i m } _ { n \to \infty } \frac { | p _ { n + 1 } - 0 | } { | p _ { n } - 0 | ^ { 2 } } = \operatorname* { l i m } _ { n \to \infty } \frac { 1 0 ^ { - ( n + 1 ) ^ { k } } } { ( 1 0 ^ { - n ^ { k } } ) ^ { 2 } } = \operatorname* { l i m } _ { n \to \infty } \frac { 1 0 ^ { - ( n + 1 ) ^ { k } } } { 1 0 ^ { - 2 n ^ { k } } } } } \\ & { } & { = \operatorname* { l i m } _ { n \to \infty } 1 0 ^ { 2 n ^ { k } - ( n + 1 ) ^ { k } } = \operatorname* { l i m } _ { n \to \infty } 1 0 ^ { n ^ { k } ( 2 - ( \frac { n + 1 } { n } ) ^ { k } ) } = \infty , } \end{array}
$$

so the sequence $p _ { n } = 1 0 ^ { - n ^ { k } }$ does not converge quadratically.

9. Typical examples are

(a) pn = 10−3n $\begin{array} { c } { p _ { n } = 1 0 ^ { - 3 ^ { n } } } \\ { p _ { n } = 1 0 ^ { - \alpha ^ { n } } } \end{array}$

$^ { * } 1 0$ . Suppose $f ( x ) = ( x - p ) ^ { m } q ( x )$ . Since

$$
g ( x ) = x - \frac { m ( x - p ) q ( x ) } { m q ( x ) + ( x - p ) q ^ { \prime } ( x ) } ,
$$

we have $g ^ { \prime } ( p ) = 0$

11. This follows from the fact that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { \left| { \frac { b - a } { 2 ^ { n + 1 } } } \right| } { \left| { \frac { b - a } { 2 ^ { n } } } \right| } } = { \frac { 1 } { 2 } } .
$$

$^ { \ast } 1 2$ . If $f$ has a zero of multiplicity $m$ at $p$ , then $f$ can be written as

$$
f ( x ) = ( x - p ) ^ { m } q ( x ) ,
$$

for $x \neq p$ , where

$$
\operatorname* { l i m } _ { x \to p } q ( x ) \neq 0 .
$$

Thus,

$$
f ^ { \prime } ( x ) = m ( x - p ) ^ { m - 1 } q ( x ) + ( x - p ) ^ { m } q ^ { \prime } ( x )
$$

and $f ^ { \prime } ( p ) = 0$ . Also,

$$
f ^ { \prime \prime } ( x ) = m ( m - 1 ) ( x - p ) ^ { m - 2 } q ( x ) + 2 m ( x - p ) ^ { m - 1 } q ^ { \prime } ( x ) + ( x - p ) ^ { m } q ^ { \prime \prime } ( x )
$$

and $f ^ { \prime \prime } ( p ) = 0$ . In general, for $k \leq m$ ,

$$
f ^ { ( k ) } ( x ) = \sum _ { j = 0 } ^ { k } { \binom { k } { j } } { \frac { d ^ { j } ( x - p ) ^ { m } } { d x ^ { j } } } q ^ { ( k - j ) } ( x ) = \sum _ { j = 0 } ^ { k } { \binom { k } { j } } m ( m - 1 ) \cdot \cdot ( m - j + 1 ) ( x - p ) ^ { m - j } q ^ { ( k - j ) } ( x ) .
$$

Thus, for $0 \leq k \leq m - 1$ , we have $f ^ { ( k ) } ( p ) = 0$ , but $f ^ { ( m ) } ( p ) = m ! \operatorname* { l i m } _ { x \to p } q ( x ) \neq 0$ .

Conversely, suppose that

$$
f ( p ) = f ^ { \prime } ( p ) = \ldots = f ^ { ( m - 1 ) } ( p ) = 0 \quad { \mathrm { a n d } } \quad f ^ { ( m ) } ( p ) \neq 0 .
$$

Consider the $( m - 1 )$ th Taylor polynomial of $f$ expanded about $p$ :

$$
\begin{array} { l } { { f ( x ) = f ( p ) + f ^ { \prime } ( p ) ( x - p ) + . . . + \frac { f ^ { ( m - 1 ) } ( p ) ( x - p ) ^ { m - 1 } } { ( m - 1 ) ! } + \frac { f ^ { ( m ) } ( \xi ( x ) ) ( x - p ) ^ { m } } { m ! } } } \\ { { { } } } \\ { { = ( x - p ) ^ { m } \displaystyle \frac { f ^ { ( m ) } ( \xi ( x ) ) } { m ! } , } } \end{array}
$$

where $\xi ( x )$ is between $x$ and $p$ .

Since $f ^ { ( m ) }$ is continuous, let

$$
q ( x ) = \frac { f ^ { ( m ) } ( \xi ( x ) ) } { m ! } .
$$

Then $f ( x ) = ( x - p ) ^ { m } q ( x )$ and

$$
\operatorname* { l i m } _ { x \to p } q ( x ) = { \frac { f ^ { ( m ) } ( p ) } { m ! } } \neq 0 .
$$

Hence $f$ has a zero of multiplicity $m$ at $p$

13. If

$$
\frac { \left| p _ { n + 1 } - p \right| } { \left| p _ { n } - p \right| ^ { 3 } } = 0 . 7 5 \mathrm { a n d } \left. p _ { 0 } - p \right. = 0 . 5 , \mathrm { t h e n } \left. p _ { n } - p \right. = \left( 0 . 7 5 \right) ^ { ( 3 ^ { n } - 1 ) / 2 } \left| p _ { 0 } - p \right| ^ { 3 ^ { n } } .
$$

To have $| p _ { n } - p | \leq 1 0 ^ { - 8 }$ requires that $n \geq 3$ .

$^ *$ 14. Let $e _ { n } = p _ { n } - p$ . If

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | e _ { n + 1 } | } { | e _ { n } | ^ { \alpha } } } = \lambda > 0 ,
$$

then for sufficiently large values of $n$ , $| e _ { n + 1 } | \approx \lambda | e _ { n } | ^ { \alpha }$ . Thus,

$$
| e _ { n } | \approx \lambda | e _ { n - 1 } | ^ { \alpha } \quad \mathrm { a n d } \quad | e _ { n - 1 } | \approx \lambda ^ { - 1 / \alpha } | e _ { n } | ^ { 1 / \alpha } .
$$

Using the hypothesis gives

$$
\lambda | e _ { n } | ^ { \alpha } \approx | e _ { n + 1 } | \approx C | e _ { n } | \lambda ^ { - 1 / \alpha } | e _ { n } | ^ { 1 / \alpha } , \quad \mathrm { s o } \quad | e _ { n } | ^ { \alpha } \approx C \lambda ^ { - 1 / \alpha - 1 } | e _ { n } | ^ { 1 + 1 / \alpha } .
$$

Since the powers of $\left| e _ { n } \right|$ must agree,

$$
\alpha = 1 + 1 / \alpha \mathrm { a n d } \alpha = { \frac { 1 + \sqrt { 5 } } { 2 } } \approx 1 . 6 2 .
$$

The number $\alpha$ is the golden ratio that appeared in Exercise 16 of section 1.3.

# Exercise Set 2.5, page 90

1. The results are listed in the following table.

<table><tr><td></td><td>(a)</td><td>(b)</td><td>(c）</td><td>(d)</td></tr><tr><td>p0</td><td>0.258684</td><td>0.907859</td><td>0.548101</td><td>0.731385</td></tr><tr><td>p1</td><td>0.257613</td><td>0.909568</td><td>0.547915</td><td>0.736087</td></tr><tr><td>p2</td><td>0.257536</td><td>0.909917</td><td>0.547847</td><td>0.737653</td></tr><tr><td>p3</td><td>0.257531</td><td>0.909989</td><td>0.547823</td><td>0.738469</td></tr><tr><td>p4</td><td>0.257530</td><td>0.910004</td><td>0.547814</td><td>0.738798</td></tr><tr><td>p5</td><td>0.257530</td><td>0.910007</td><td>0.547810</td><td>0.738958</td></tr></table>

\*2. Newton’s Method gives $p _ { 6 } = - 0 . 1 8 2 8 8 7 6$ and $\hat { p } _ { 6 } = - 0 . 1 8 3 3 8 7$ $^ * 3$ . Steffensen’s method gives $p _ { 0 } ^ { ( 1 ) } = 0 . 8 2 6 4 2 7$

4. Steffensen’s method gives p(1)0 = 2.152905 and p(2)0 $p _ { 0 } ^ { ( 2 ) } = 1 . 8 7 3 4 6 4$ .

$^ { * } 5$ . Steffensen’s method gives $p _ { 1 } ^ { ( 0 ) } = 1 . 5$ .

6. Steffensen’s method gives $p _ { 2 } ^ { ( 0 ) } = 1 . 7 3 2 0 5$ .

7. For $g ( x ) = \sqrt { 1 + \textstyle { \frac { 1 } { x } } }$ and $p _ { 0 } ^ { ( 0 ) } = 1$ , we have $p _ { 0 } ^ { ( 3 ) } = 1 . 3 2 4 7 2$ .

8. For $g ( x ) = 2 ^ { - x }$ and $p _ { 0 } ^ { ( 0 ) } = 1$ = 1, we have p(3)0 $p _ { 0 } ^ { ( 3 ) } = 0 . 6 4 1 1 9$ .

9. For $\textstyle g ( x ) = 0 . 5 ( x + { \frac { 3 } { x } } )$ and $p _ { 0 } ^ { ( 0 ) } = 0 . 5$ , we have $p _ { 0 } ^ { ( 4 ) } = 1 . 7 3 2 0 5$

10. For $\textstyle g ( x ) = { \frac { 5 } { \sqrt { x } } }$ and $p _ { 0 } ^ { ( 0 ) } = 2 . 5$ = 2.5, we have p(3)0 $p _ { 0 } ^ { ( 3 ) } = 2 . 9 2 4 0 1 7 7 4$ .

11. (a) For $g ( x ) = \left( 2 - e ^ { x } + x ^ { 2 } \right) / 3$ and $p _ { 0 } ^ { ( 0 ) } = 0$ , we have $p _ { 0 } ^ { ( 3 ) } = 0 . 2 5 7 5 3 0$ . \*(b) For $g ( x ) = 0 . 5 ( \sin x + \cos x )$ and $p _ { 0 } ^ { ( 0 ) } = 0$ , we have $p _ { 0 } ^ { ( 4 ) } = 0 . 7 0 4 8 1 2$ . (c) With $p _ { 0 } ^ { ( 0 ) } = 0 . 2 5$ , $p _ { 0 } ^ { ( 4 ) } = 0 . 9 1 0 0 0 7 5 7 2$ . (d) With $p _ { 0 } ^ { ( 0 ) } = 0 . 3$ , $p _ { 0 } ^ { ( 4 ) } = 0 . 4 6 9 6 2 1 9 2 3$ .

12. (a) For $g ( x ) = 2 + \sin x$ and $p _ { 0 } ^ { ( 0 ) } = 2$ , we have p(4)0 = 2.55419595. (b) For $g ( x ) = \sqrt [ 3 ] { 2 x + 5 }$ and $p _ { 0 } ^ { ( 0 ) } = 2$ , we have p(2)0 = 2.09455148. (c) With $g ( x ) = \textstyle { \sqrt { \frac { e ^ { x } } { 3 } } }$ and p(0) $p _ { 0 } ^ { ( 0 ) } = 1$ , we have $p _ { 0 } ^ { ( 3 ) } = 0 . 9 1 0 0 0 7 5 7 4$ . (d) With $g ( x ) = \cos x$ , and $p _ { 0 } ^ { ( 0 ) } = 0$ , we have p(4)0 = 0.739085133.

13. Aitken’s $\Delta ^ { 2 }$ method gives:

(a) $\begin{array} { r } { \hat { p } _ { 1 0 } = 0 . 0 \overline { { 4 5 } } } \\ { \hat { p } _ { 2 } = 0 . 0 3 6 3 } \end{array}$ (b)

$^ { * } 1 4$ . (a) A positive constant $\lambda$ exists with

$$
\lambda = \operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p | } { | p _ { n } - p | ^ { \alpha } } } .
$$

Hence

$$
\operatorname* { l i m } _ { n \to \infty } \left| { \frac { p _ { n + 1 } - p } { p _ { n } - p } } \right| = \operatorname* { l i m } _ { n \to \infty } { \frac { \left| p _ { n + 1 } - p \right| } { \left| p _ { n } - p \right| ^ { \alpha } } } \cdot \left| p _ { n } - p \right| ^ { \alpha - 1 } = \lambda \cdot 0 = 0 { \pmod { } } \quad \operatorname* { l i m } _ { n \to \infty } { \frac { p _ { n + 1 } - p } { p _ { n } - p } } = 0 .
$$

(b) One example is $\textstyle p _ { n } = { \frac { 1 } { n ^ { n } } }$ .

15. We have

$$
{ \frac { \left| p _ { n + 1 } - p _ { n } \right| } { \left| p _ { n } - p \right| } } = { \frac { \left| p _ { n + 1 } - p + p - p _ { n } \right| } { \left| p _ { n } - p \right| } } = \left| { \frac { p _ { n + 1 } - p } { p _ { n } - p } } - 1 \right| ,
$$

so

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p _ { n } | } { | p _ { n } - p | } } = \operatorname* { l i m } _ { n \to \infty } \left| { \frac { p _ { n + 1 } - p } { p _ { n } - p } } - 1 \right| = 1 .
$$

16.

$$
\frac { \hat { p } _ { n } - p } { p _ { n } - p } = \frac { \lambda \left( \delta _ { n } + \delta _ { n + 1 } \right) - 2 \delta _ { n } + \delta _ { n } \delta _ { n + 1 } - 2 \delta _ { n } ( \lambda - 1 ) - \delta _ { n } ^ { 2 } } { ( \lambda - 1 ) ^ { 2 } + \lambda \left( \delta _ { n } + \delta _ { n + 1 } \right) - 2 \delta _ { n } + \delta _ { n } \delta _ { n + 1 } }
$$

\*17. (a) Since $p _ { n } = P _ { n } ( x ) = \sum _ { k = 0 } ^ { n } { \frac { 1 } { k ! } } x ^ { k }$ , we have

$$
p _ { n } - p = P _ { n } ( x ) - e ^ { x } = \frac { - e ^ { \xi } } { ( n + 1 ) ! } x ^ { n + 1 } ,
$$

where $\xi$ is between $0$ and $x$ . Thus, $p _ { n } - p \neq 0$ , for all $n \geq 0$ . Further,

$$
{ \frac { p _ { n + 1 } - p } { p _ { n } - p } } = { \frac { { \frac { - e ^ { \xi _ { 1 } } } { ( n + 2 ) ! } } x ^ { n + 2 } } { { \frac { - e ^ { \xi } } { ( n + 1 ) ! } } x ^ { n + 1 } } } = { \frac { e ^ { ( \xi _ { 1 } - \xi ) } x } { n + 2 } } ,
$$

where $\xi _ { 1 }$ is between 0 and $1$ . Thus, $\begin{array} { r } { \lambda = \operatorname* { l i m } _ { n  \infty } \frac { e ^ { ( \xi _ { 1 } - \xi ) } x } { n + 2 } = 0 < 1 } \end{array}$

<table><tr><td>n</td><td>pn</td></tr><tr><td>0</td><td>3</td></tr><tr><td>1</td><td>2.75</td></tr><tr><td>2</td><td>2.72</td></tr><tr><td>2.5 3 2.6</td><td>2.71875</td></tr><tr><td>4 2.7083</td><td>2.7183</td></tr><tr><td>5 2.716</td><td>2.7182870</td></tr><tr><td>6</td><td>2.7182823</td></tr><tr><td>7</td><td>2.7182539 2.7182818</td></tr><tr><td>8</td><td>2.7182787 2.7182818</td></tr><tr><td>9</td><td>2.7182815</td></tr><tr><td>10</td><td>2.7182818</td></tr></table>

(c) Aitken’s $\Delta ^ { 2 }$ method gives quite an improvement for this problem. For example, $\hat { p } _ { 6 }$ is accurate to within $5 \times 1 0 ^ { - 7 }$ . We need $p _ { 1 0 }$ to have this accuracy.

# Exercise Set 2.6, page 100

1. (a) For $p _ { 0 } = 1$ , we have $p _ { 2 2 } = 2 . 6 9 0 6 5$ . (b) For $p _ { 0 } = 1$ , we have $p _ { 5 } = 0 . 5 3 2 0 9$ ; for $p _ { 0 } = - 1$ , we have $p _ { 3 } = - 0 . 6 5 2 7 0$ ; and for $p _ { 0 } = - 3$ , we have $p _ { 3 } = - 2 . 8 7 9 3 9$ . (c) For $p _ { 0 } = 1$ , we have $p _ { 5 } = 1 . 3 2 4 7 2$ . (d) For $p _ { 0 } = 1$ , we have $p _ { 4 } = 1 . 1 2 4 1 \dot { 2 }$ ; and for $p _ { 0 } = 0$ , we have $p _ { 8 } = - 0 . 8 7 6 0 5$ . (e) For $p _ { 0 } = 0$ , we have $p _ { 6 } ~ = ~ - 0 . 4 7 0 0 6$ ; for $p _ { 0 } ~ = ~ - 1$ , we have $p _ { 4 } = - 0 . 8 8 5 3 3$ ; and for $p _ { 0 } = - 3$ , we have $p _ { 4 } = - 2 . 6 4 5 6 1$ . (f) For $p _ { 0 } = 0$ , we have $p _ { 1 0 } = 1 . 4 9 8 1 9$ .   
2. (a) For $p _ { 0 } = 0$ , we have $p _ { 9 } = - 4 . 1 2 3 1 0 6$ ; and for $p _ { 0 } = 3$ , we have $p _ { 6 } = 4 . 1 2 3 1 0 6$ . The complex roots are $- 2 . 5 \pm 1 . 3 2 2 8 7 9 i$ .   
\*(b) For $p _ { 0 } = 1$ , we have $p _ { 7 } = - 3 . 5 4 8 2 3 3$ ; and for $p _ { 0 } = 4$ , we have $p _ { 5 } = 4 . 3 8 1 1 1$ . The complex roots are $0 . 5 8 3 5 5 9 7 \pm 1 . 4 9 4 1 8 8 i$ .   
(c) The only roots are complex, and they are $\pm \sqrt { 2 } i$ and $- 0 . 5 \pm 0 . 5 { \sqrt { 3 } } i$ .   
(d) For $p _ { 0 } ~ = ~ 1$ , we have $p _ { 5 } = - 0 . 2 5 0 2 3 7$ ; for $p _ { 0 } ~ = ~ 2$ , we have $p _ { 5 } ~ = ~ 2 . 2 6 0 0 8 6$ ; and for $p _ { 0 } = - 1 1$ , we have $p _ { 6 } = - 1 2 . 6 1 2 4 3 0$ . The complex roots are $- 0 . 1 9 8 7 0 9 4 \pm 0 . 8 1 3 3 1 2 5 i$ .   
(e) For $p _ { 0 } = 0$ , we have $p _ { 8 } = 0 . 8 4 6 7 4 3$ ; and for $p _ { 0 } = - 1$ , we have $p _ { 9 } = - 3 . 3 5 8 0 4 4$ . The complex roots are $- 1 . 4 9 4 3 5 0 \pm 1 . 7 4 4 2 1 9 i$ .   
(f) For $p _ { 0 } = 0$ , we have $p _ { 8 } = 2 . 0 6 9 3 2 3$ ; and for $p _ { 0 } = 1$ , we have $p _ { 3 } = 0 . 8 6 1 1 7 4$ . The complex roots are $- 1 . 4 6 5 2 4 8 \pm 0 . 8 1 1 6 7 2 2 i$ .   
(g) For $p _ { 0 } = 0$ , we have $p _ { 6 } = - 0 . 7 3 2 0 5 1$ ; for $p _ { 0 } = 1$ , we have $p _ { 4 } = 1 . 4 1 4 2 1 4$ ; for $p _ { 0 } = 3$ , we have $p _ { 5 } = 2 . 7 3 2 0 5 1$ ; and for $p _ { 0 } = - 2$ , we have $p _ { 6 } = - 1 . 4 1 4 2 1 4$ .   
(h) For $p _ { 0 } = 0$ , we have $p _ { 5 } = 0 . 5 8 5 7 8 6$ ; for $p _ { 0 } = 2$ , we have $p _ { 2 } = 3$ ; and for $p _ { 0 } = 4$ , we have $p _ { 6 } = 3 . 4 1 4 2 1 4$ .

3. The following table lists the initial approximation and the roots.   

<table><tr><td></td><td>P0</td><td>P1</td><td>p2</td><td>Approximate roots</td><td>Complex Conjugate roots</td></tr><tr><td rowspan="2">(a)</td><td>-1</td><td>0</td><td>1</td><td>P7 = -0.34532 - 1.31873i</td><td>-0.34532 + 1.31873i</td></tr><tr><td>0</td><td>1</td><td>2</td><td>P6 = 2.69065</td><td></td></tr><tr><td rowspan="3">(b)</td><td>0</td><td>1</td><td>2</td><td>P6 = 0.53209</td><td></td></tr><tr><td>1</td><td>2</td><td>3</td><td>P9 = -0.65270</td><td></td></tr><tr><td>-2</td><td>-3</td><td>-2.5</td><td>P4 = -2.87939</td><td></td></tr><tr><td rowspan="2">（c）</td><td>0</td><td>1</td><td>2</td><td>P5 = 1.32472</td><td></td></tr><tr><td>-2</td><td>-1</td><td>0</td><td>P7 = -0.66236- 0.56228i</td><td>-0.66236 + 0.56228i</td></tr><tr><td rowspan="3">(d)</td><td>0</td><td>1</td><td>2</td><td>P5 = 1.12412</td><td></td></tr><tr><td>2</td><td>3</td><td>4</td><td>P12 = -0.12403 + 1.74096i</td><td>-0.12403- 1.74096i</td></tr><tr><td>-2</td><td>0</td><td>-1</td><td>P5 = -0.87605</td><td></td></tr><tr><td rowspan="3">(e）</td><td>0</td><td>1</td><td>2</td><td>P10 = -0.88533</td><td></td></tr><tr><td>1</td><td>0</td><td>-0.5</td><td>P5 = -0.47006</td><td></td></tr><tr><td>-1</td><td>-2</td><td>-3</td><td>P5 = -2.64561</td><td></td></tr><tr><td rowspan="3">(f)</td><td>0</td><td>1</td><td>2</td><td>P6 = 1.49819</td><td></td></tr><tr><td>-1</td><td>-2</td><td>-3</td><td>P10 = -0.51363- 1.09156i</td><td>-0.51363 + 1.09156i</td></tr><tr><td>1</td><td>0</td><td>-1</td><td>P8 = 0.26454- 1.32837i</td><td>0.26454 + 1.32837i</td></tr></table>

4. The following table lists the initial approximation and the roots.

<table><tr><td></td><td>P0</td><td>P1</td><td>p2</td><td>Approximate roots</td><td>Complex Conjugate roots</td></tr><tr><td rowspan="3">(a)</td><td>0</td><td>1</td><td>2</td><td>P11 = -2.5 - 1.322876i</td><td>-2.5 + 1.322876i</td></tr><tr><td>1</td><td>2</td><td>3</td><td>P6 = 4.123106</td><td></td></tr><tr><td>-3</td><td>-4</td><td>-5</td><td>P5 = -4.123106</td><td></td></tr><tr><td rowspan="3">*（(b)</td><td>0</td><td>1</td><td>2</td><td>P7 = 0.583560 - 1.494188i</td><td>0.583560 + 1.494188i</td></tr><tr><td>2</td><td>3</td><td>4</td><td>P6 = 4.381113</td><td></td></tr><tr><td>-2</td><td>-3</td><td>-4</td><td>P5 = -3.548233</td><td></td></tr><tr><td rowspan="2">(c）</td><td>0</td><td>1</td><td>2</td><td>P11 = 1.414214i</td><td>−1.414214i</td></tr><tr><td>-1</td><td>-2</td><td>-3</td><td>P10 = -0.5 + 0.866025i</td><td>-0.5 - 0.866025i</td></tr><tr><td rowspan="4">(d）</td><td>0</td><td>1</td><td>2</td><td>p7 = 2.260086</td><td></td></tr><tr><td>3</td><td>4</td><td>5</td><td>P14 = -0.198710 + 0.813313i</td><td>-0.198710 + 0.813313i</td></tr><tr><td>11</td><td>12</td><td>13</td><td>P22 = -0.250237</td><td></td></tr><tr><td>-9</td><td>-10</td><td>-11</td><td>P6 = -12.612430</td><td></td></tr><tr><td rowspan="3">(e)</td><td>0</td><td>1</td><td>2</td><td>P6 = 0.846743</td><td></td></tr><tr><td>3</td><td>4</td><td>5</td><td>P12 = -1.494349 + 1.744218i</td><td>−1.494349 - 1.744218i</td></tr><tr><td>-1</td><td>-2</td><td>-3</td><td>P7 = -3.358044</td><td></td></tr><tr><td rowspan="3">(f)</td><td>0</td><td>1</td><td>2</td><td>P6 = 2.069323</td><td></td></tr><tr><td>-1</td><td>0</td><td>1</td><td>P5 = 0.861174</td><td></td></tr><tr><td>-1</td><td>-2</td><td>-3</td><td>P8 = -1.465248+ 0.811672i</td><td>-1.465248 - 0.811672i</td></tr><tr><td rowspan="4">(g）</td><td>0</td><td>1</td><td>2</td><td>P6 = 1.414214</td><td></td></tr><tr><td>-2</td><td>-1</td><td>0</td><td>P7 = -0.732051</td><td></td></tr><tr><td>0</td><td>-2</td><td>-1</td><td>P7 = -1.414214</td><td></td></tr><tr><td>2</td><td>3</td><td>4</td><td>P6 = 2.732051</td><td></td></tr><tr><td rowspan="3">(h)</td><td>0</td><td>1</td><td>2</td><td>P8=3</td><td></td></tr><tr><td>-1</td><td>0</td><td>1</td><td>P5 = 0.585786</td><td></td></tr><tr><td>2.5</td><td>3.5</td><td>4</td><td>P6 = 3.414214</td><td></td></tr></table>

5. (a) The roots are 1.244, 8.847, and $- 1 . 0 9 1$ , and the critical points are 0 and 6. \*(b) The roots are 0.5798, 1.521, 2.332, and $- 2 . 4 3 2$ , and the critical points are 1, 2.001, and −1.5.

6. We get convergence to the root 0.27 with $p _ { 0 } = 0 . 2 8$ . We need $p _ { 0 }$ closer to 0.29 since $f ^ { \prime } ( 0 . 2 8 { \overline { { 3 } } } ) =$ 0.

7. Maple gives the only real zero as

$$
\frac { ( 5 4 + 6 { \sqrt { 1 2 9 } } ) ^ { 2 / 3 } - 1 2 } { 3 ( 5 4 + 6 { \sqrt { 1 2 9 } } ) ^ { 1 / 3 } } \approx 0 . 8 4 7 7 0 7 5 9 7 9 .
$$

8. Maple gives the only real zero as

$$
\frac { ( 5 4 0 + 1 2 { \sqrt { 1 9 2 9 } } ) ^ { 2 / 3 } + 2 4 } { 6 ( 5 4 0 + 1 2 { \sqrt { 1 9 2 9 } } ) ^ { 1 / 3 } } \approx 2 . 0 9 4 5 5 1 4 8 2 .
$$

$^ { * } 9$ . The methods all find the solution 0.23235.

10. The width is approximately $W = 1 6 . 2 1 2 1$ ft.

$^ { * } 1 1$ . The minimal material is approximately 573.64895 cm2.

$^ { * } 1 2$ . Fibonacci’s answer was 1.3688081078532, and Newton’s Method gives 1.36880810782137 with a tolerance of $1 0 ^ { - 1 6 }$ , so Fibonacci’s answer is within $4 \times 1 0 ^ { - 1 1 }$ . This accuracy is amazing for the time.

# Interpolation and Polynomial Approximation

# Exercise Set 3.1, page 114

1. The interpolation polynomials are as follows.

(a) $P _ { 1 } ( x ) = - 0 . 1 4 8 8 7 8 x + 1$ ; $P _ { 1 } ( 0 . 4 5 ) = 0 . 9 3 3 0 0 5$ ; $| f ( 0 . 4 5 ) - P _ { 1 } ( 0 . 4 5 ) | = 0 . 0 3 2 5 5 8$ ; $P _ { 2 } ( x ) = - 0 . 4 5 2 5 9 2 x ^ { 2 } - 0 . 0 1 3 1 0 0 9 x + 1$ ; $P _ { 2 } ( 0 . 4 5 ) = 0 . 9 0 2 4 5 5$ ; $| f ( 0 . 4 5 ) - P _ { 2 } ( 0 . 4 5 ) | = 0 . 0 0 2 0 0 8$   
(b) $P _ { 1 } ( x ) = 0 . 4 6 7 2 5 1 x + 1$ ; $P _ { 1 } ( 0 . 4 5 ) = 1 . 2 1 0 2 6 3$ ; $| f ( 0 . 4 5 ) - P _ { 1 } ( 0 . 4 5 ) | = 0 . 0 0 6 1 0 4$ ; $P _ { 2 } ( x ) = - 0 . 0 7 8 0 0 2 6 x ^ { 2 } + 0 . 4 9 0 6 5 2 x + 1$ ; $P _ { 2 } ( 0 . 4 5 ) = 1 . 2 0 4 9 9 8$ ; $| f ( 0 . 4 5 ) - P _ { 2 } ( 0 . 4 5 ) | = 0 . 0 0 0 8 3 9$   
(c) $P _ { 1 } ( x ) = 0 . 8 7 4 5 4 8 x$ ; $P _ { 1 } ( 0 . 4 5 ) = 0 . 3 9 3 5 4 6$ ; $| f ( 0 . 4 5 ) - P _ { 1 } ( 0 . 4 5 ) | = 0 . 0 2 1 2 9 8 3$ ; $P _ { 2 } ( x ) = - 0 . 2 6 8 9 6 1 x ^ { 2 } + 0 . 9 5 5 2 3 6 x$ ; $P _ { 2 } ( 0 . 4 5 ) = 0 . 3 7 5 3 9 2$ ; $| f ( 0 . 4 5 ) - P _ { 2 } ( 0 . 4 5 ) | = 0 . 0 0 3 8 2 8$   
(d) $P _ { 1 } ( x ) = 1 . 0 3 1 1 2 1 x$ ; $P _ { 1 } ( 0 . 4 5 ) = 0 . 4 6 4 0 0 4$ ; $| f ( 0 . 4 5 ) - P _ { 1 } ( 0 . 4 5 ) | = 0 . 0 1 9 0 5 1$ ; $P _ { 2 } ( x ) = 0 . 6 1 5 0 9 2 x ^ { 2 } + 0 . 8 4 6 5 9 3 x$ ; $P _ { 2 } ( 0 . 4 5 ) = 0 . 5 0 5 5 2 3$ ; $| f ( 0 . 4 5 ) - P _ { 2 } ( 0 . 4 5 ) | = 0 . 0 2 2 4 6 8$

2. The interpolation polynomials are as follows.

\*(a) $P _ { 1 } ( x ) = - 0 . 6 9 6 9 9 9 2 4 0 8 x + 0 . 1 6 4 1 4 2 2 6 9 1$ ; $P _ { 1 } ( 1 . 4 ) = - 0 . 8 1 1 6 5 6 6 6 8 0$ ; $| f ( 1 . 4 ) - P _ { 1 } ( 1 . 4 ) | = 0 . 1 3 9 3 9 9 8 4 8 6$ ; $P _ { 2 } ( x ) = 3 . 5 5 2 3 7 9 8 0 9 x ^ { 2 } - 1 0 . 8 2 1 2 8 1 7 0 x + 7 . 2 6 8 9 0 1 8 8 7 ;$ ; $P _ { 2 } ( 1 . 4 ) = - 0 . 9 1 8 2 2 8 0 6 7$ ; $| f ( 1 . 4 ) - P _ { 2 } ( 1 . 4 ) | = 0 . 0 3 2 8 2 8 4 4 9 6$   
(b) $P _ { 1 } ( x ) = 0 . 6 0 9 9 2 0 4 0 0 8 x - 0 . 1 3 2 4 3 9 9 7 6 0$ ; $P _ { 1 } ( 1 . 4 ) = 0 . 7 2 1 4 4 8 5 8 5 1$ ; $| f ( 1 . 4 ) - P _ { 1 } ( 1 . 4 ) | = 0 . 0 1 5 3 5 7 7 1 4 7$ ; $P _ { 2 } ( x ) = - 3 . 1 8 3 2 0 2 8 3 2 x ^ { 2 } + 9 . 6 8 2 0 4 8 4 7 2 x - 6 . 4 9 8 8 4 5 6 4 0$ ; $P _ { 2 } ( 1 . 4 ) = 0 . 8 1 6 9 4 4 6 6 9$ ; $| f ( 1 . 4 ) - P _ { 2 } ( 1 . 4 ) | = 0 . 0 8 0 1 3 8 3 6 9 2$   
(c) $P _ { 1 } ( x ) = 0 . 4 0 1 2 8 8 2 9 3 7 x - 0 . 0 6 2 2 7 7 6 7 3 3$ ; $P _ { 1 } ( 1 . 4 ) = 0 . 4 9 9 5 2 5 9 3 7 9$ ; $| f ( 1 . 4 ) - P _ { 1 } ( 1 . 4 ) | = 0 . 0 0 5 6 2 4 0 4 0 4$ ; $P _ { 2 } ( x ) = - 0 . 2 5 3 2 0 4 1 6 4 3 x ^ { 2 } + 1 . 1 2 2 9 2 0 1 6 2 x - 0 . 5 6 8 6 8 6 0 0 2 1$ ; $P _ { 2 } ( 1 . 4 ) = 0 . 5 0 7 1 2 2 0 6 2 9$ ; $| f ( 1 . 4 ) - P _ { 2 } ( 1 . 4 ) | = 0 . 0 0 1 9 7 2 0 8 4 6$   
(d) $P _ { 1 } ( x ) = 3 4 . 2 8 5 8 1 7 8 3 x - 3 1 . 9 2 4 7 7 8 3 3$ ; $P _ { 1 } ( 1 . 4 ) = 1 6 . 0 7 5 3 6 6 6 3$ ; $| f ( 1 . 4 ) - P _ { 1 } ( 1 . 4 ) | = 1 . 0 3 0 7 1 9 8 6$ ; $^ { D } _ { 2 } ( x ) = 2 6 . 8 5 3 4 4 4 0 0 x ^ { 2 } - 4 2 . 2 4 6 4 9 7 5 6 x + 2 1 . 7 8$ 8210966; $P _ { 2 } ( 1 . 4 ) = 1 5 . 2 6 9 7 6 3 3 2$ ; $| f ( 1 . 4 ) - P _ { 2 } ( 1 . 4 ) | = 0 . 2 2 5 1 1 6 5 5$

3. Error bounds for the polynomials in Exercise 1 are as follows.

$$
\begin{array} { r l } & { \mathrm { ~ F o r ~ } P r _ { 1 } ( x ) : | \begin{array} { l } { \frac { j ^ { \prime \prime } ( \xi ) } { 2 } ( 0 . 4 5 - 0 ) ( 0 . 4 5 - 0 . 6 ) \big | \leq 0 . 1 3 3 ; } \\ { \frac { \xi } { 2 } ( \xi ) } \\ { \mathrm { ~ F o r ~ } 2 ( x ) : | \frac { j ^ { \prime \prime } ( \xi ) } { 2 } ( 0 . 4 5 - 0 ) ( 0 . 4 5 - 0 . 6 ) ( 0 . 4 5 - 0 . 9 ) | \leq 0 . 0 0 3 9 7 } \end{array}  } \\ & { \mathrm { ~ F o r ~ } P r _ { 1 } ( x ) : | \begin{array} { l } { \frac { j ^ { \prime \prime } ( \xi ) } { 2 } ( 0 . 4 5 - 0 ) ( 0 . 4 5 - 0 . 6 ) \Big | \leq 0 . 0 3 3 7 5 ; } \\ { \frac { j ^ { \prime \prime } ( \xi ) } { 2 } ( 0 . 4 5 - 0 ) ( 0 . 4 5 - 0 . 6 ) \Big | \leq 0 . 0 3 3 7 5 ; } \end{array}  } \\ & { \mathrm { ~ F o r ~ } P r _ { 2 } ( x ) : | \begin{array} { l } { \frac { j ^ { \prime \prime } ( \xi ) } { 2 } ( 0 . 4 5 - 0 ) ( 0 . 4 5 - 0 . 6 ) ( 0 . 4 5 - 0 . 9 ) \Big | \leq 0 . 0 0 1 8 9 8 } \\ { \frac { j ^ { \prime \prime } ( \xi ) } { 2 } ( 0 . 4 5 - 0 ) ( 0 . 4 5 - 0 . 6 ) \Big | \leq 0 . 1 3 5 ; } \end{array}  } \\ &  \mathrm { ~ F o r ~ } P r _ { 1 } ( x ) : | \begin{array} { l } { \frac { j ^ { \prime \prime } ( \xi ) } { 2 } ( 0 . 4 5 - 0 ) ( 0 . 4 5 - 0 . 6 ) \Big | \leq 0 . 1 3 5 ; } \\ { \frac { j ^ { \prime \prime } ( \xi ) } { 2 } ( 0 . 4 5 - 0 ) ( 0 . 4 5 - 0 . 6 ) ( 0 . 4 5 - 0 . 9 ) \Big | \leq 0 . 0 1 0 1 2 5 ; } \end{array} \end{array}
$$

4. Error bounds for the polynomials in Exercise 2 are as follows.

\*(a) For $P _ { 1 } ( x )$ : 0.1480440661; For $P _ { 2 } ( x )$ : 0.062012553   
(b) For $P _ { 1 } ( x )$ : 0.03359789466; There is no bound since the derivative goes to $\infty$ . (c) For $P _ { 1 } ( x )$ : 0.004169227026; For $P _ { 2 } ( x )$ : 0.006080122747   
(d) For $P _ { 1 } ( x )$ : 1.471951812; For $P _ { 2 } ( x )$ : 1.373821691

5. Interpolation polynomials give the following results.

<table><tr><td colspan="3"></td></tr><tr><td>n</td><td>xo,x1,...,xn</td><td>Pn(8.4)</td></tr><tr><td>1</td><td>8.3, 8.6</td><td>17.87833</td></tr><tr><td>2</td><td>8.3, 8.6, 8.7</td><td>17.87716</td></tr><tr><td>3</td><td>8.3, 8.6, 8.7, 8.1</td><td>17.87714</td></tr></table>

<table><tr><td colspan="2">C</td><td></td></tr><tr><td rowspan="3">n</td><td>xo,x1,...,xn</td><td>Pn(0.25)</td></tr><tr><td>1 0.2, 0.3</td><td>-0.13869287</td></tr><tr><td>0.2, 0.3, 0.4</td><td>-0.13259734</td></tr><tr><td>2 3</td><td>0.2, 0.3, 0.4, 0.1</td><td>-0.13277477</td></tr></table>

<table><tr><td colspan="2">xo,x1,...,Xn n</td><td>Pn(-1/3)</td></tr><tr><td>1</td><td>-0.5,-0.25</td><td>0.21504167</td></tr><tr><td>2</td><td>-0.5,-0.25, 0.0</td><td>0.16988889</td></tr><tr><td>3</td><td>−0.5,-0.25, 0.0, -0.75</td><td>0.17451852</td></tr></table>

<table><tr><td colspan="2">(d)</td><td></td></tr><tr><td>n</td><td>xo,x1,...,xn</td><td>Pn(0.9)</td></tr><tr><td>1</td><td>0.8,1.0</td><td>0.44086280</td></tr><tr><td>2</td><td>0.8, 1.0, 0.7</td><td>0.43841352</td></tr><tr><td>3</td><td>0.8, 1.0, 0.7, 0.6</td><td>0.44198500</td></tr></table>

6. Interpolation polynomials give the following results.

(a) $P _ { 1 } ( x ) = 4 . 2 7 8 2 4 0 0 0 0 x + 0 . 5 7 9 1 6 0 0 0 0 ; P _ { 1 } ( 0 . 4 3 ) = 2 . 4 1 8 8 0 3 2 0 0$ $| f ( 0 . 4 3 ) - P _ { 1 } ( 0 . 4 3 ) | = 0 . 0 5 5 6 4 2 5 0 6$ ; $P _ { 2 } ( x ) = 5 . 5 5 0 8 0 0 0 0 0 x ^ { 2 } + 0 . 1 1 5 1 4 0 0 0 0 x + 1 . 2 7 3 0 1 0 0 0 0$ ; $P _ { 2 } ( 0 . 4 3 ) = 2 . 3 4 8 8 6 3 1 2 0$ ; $| f ( 0 . 4 3 ) - P _ { 2 } ( 0 . 4 3 ) | = 0 . 0 1 4 2 9 7 5 7 4$ $P _ { 3 } ( x ) = 2 . 9 1 2 1 0 6 6 6 8 x ^ { 3 } + 1 . 1 8 2 6 3 9 9 9 9 x ^ { 2 } + 2 . 1 1 7 2 1 3 3 3 4 x + 1 . 0$ ; $P _ { 3 } ( 0 . 4 3 ) = 2 . 3 6 0 6 0 4 7 3 4$ ; $| f ( 0 . 4 3 ) - P _ { 3 } ( 0 . 4 3 ) | = 0 . 0 0 2 5 5 5 9 6 0 e$   
(b) $P _ { 1 } ( x ) = - 1 . 0 6 2 4 9 8 0 0 0 x + 1 . 0 6 6 4 0 5 5 0 0 ; P _ { 1 } ( 0 . 0 ) = 1 . 0 6 6 4 0 5 5 0 0$ $| f ( 0 . 0 ) - P _ { 1 } ( 0 . 0 ) | = 0 . 0 6 6 4 0 5 5 0 0$ ; $P _ { 2 } ( x ) = 1 . 8 1 2 5 0 9 3 3 4 x ^ { 2 } - 1 . 0 6 2 4 9 7 9 9 9 x + 0 . 9 5 3 1 2 3 6 6 7 0$ ; $P _ { 2 } ( 0 . 0 ) = 0 . 9 5 3 1 2 3 6 6 7 0$ ; $| f ( 0 . 0 ) - P _ { 2 } ( 0 . 0 ) | = 0 . 0 4 6 8 7 6 3 3 3 0$ $P _ { 3 } ( x ) = - 1 . 0 0 0 1 0 6 6 7 x ^ { 3 } + 1 . 3 1 2 5 0 4 0 0 0 x ^ { 2 } - 0 . 9 9 9 9 9 7 3 3 3 0 x + 0 . 9 8 4 3 7 4 0 0 0 0$ ; $P _ { 3 } ( 0 . 0 ) =$ 0.9843740000; $| f ( 0 . 0 ) - P _ { 3 } ( 0 . 0 ) | = 0 . 0 1 5 6 2 6 0 0 0 0$   
(c) $P _ { 1 } ( x ) = - 2 . 7 0 7 4 7 4 8 x - 0 . 0 1 9 3 0 2 3 8 ; P _ { 1 } ( 0 . 1 8 ) = - 0 . 5 0 6 6 4 7 8 4 4$ $| f ( 0 . 1 8 ) - P _ { 1 } ( 0 . 1 8 ) | = 0 . 0 0 1 4 7 5 6 2 0 4$ ; $P _ { 2 } ( x ) = 0 . 8 7 6 2 5 5 0 0 0 0 x ^ { 2 } - 2 . 9 7 0 3 5 1 3 0 0 x - 0 . 0 0 1 7 7 7 2 8 0 0 ;$ $P _ { 2 } ( 0 . 1 8 ) = - 0 . 5 0 8 0 4 9 8 5 2 0$ ; $| f ( 0 . 1 8 ) - P _ { 2 } ( 0 . 1 8 ) | = 0 . 0 0 0 0 7 3 6 1 2 4$ $^ { D } _ { 3 } ( x ) = - 0 . 4 8 5 5 3 3 3 3 3 4 x ^ { 3 } + 1 . 1 6 7 5 7 5 0 0 0 x ^ { 2 } - \frac { 3 } { 4 }$ $3 3 3 4 x ^ { 3 } + 1 . 1 6 7 5 7 5 0 0 0 x ^ { 2 } - 3 . 0 2 3 7 5 9 9 6 7 x + 0 . 0$ 011359200; $P _ { 3 } ( 0 . 1 8 ) =$ $- 0 . 5 0 8 1 4 3 0 7 4 5$ ; $| f ( 0 . 1 8 ) - P _ { 3 } ( 0 . 1 8 ) | = 0 . 0 0 0 0 1 9 6 1 0 1$   
(d) $P _ { 1 } ( x ) = 0 . 3 9 1 5 2 8 8 0 0 0 x + 1 . 0 9 8 6 1 2 3 ; P _ { 1 } ( 0 . 2 5 ) = 1 . 1 9 6 4 9 4 5 0 0$ $| f ( 0 . 2 5 ) - P _ { 1 } ( 0 . 2 5 ) | = 0 . 0 0 7 4 2 4 5 6 9$ ; $P _ { 2 } ( x ) = 0 . 1 1 0 3 4 4 3 8 0 0 x ^ { 2 } + 0 . 3 3 6 3 5 6 6 1 0 0 x + 1 . 0$ 098612300; $P _ { 2 } ( 0 . 2 5 ) = 1 . 1 8 9 5 9 7 9 7 6$ ; $| f ( 0 . 2 5 ) - P _ { 2 } ( 0 . 2 5 ) | = 0 . 0 0 0 5 2 8 0 4 5$ $P _ { 3 } ( x ) = 0 . 0 1 4 1 4 0 3 6 0 0 0 x ^ { 3 } + 0 . 1 1 0 3 4 4 3 8 0 0 x ^ { 2 } + 0 . 3 3 2 8 2 1 5 2 0 0 x + 1 . 0 9 8 6 1 2 3 0 0$ ; $P _ { 3 } ( 0 . 2 5 ) =$ 1.188935147; $| f ( 0 . 2 5 ) - P _ { 3 } ( 0 . 2 5 ) | = 0 . 0 0 0 1 3 4 7 8 4$

7. Interpolation polynomials give the following results.

<table><tr><td>n</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>1</td><td>0.00118</td><td>0.00120</td></tr><tr><td>2</td><td>1.367 × 10-5</td><td>1.452 × 10-5</td></tr></table>

<table><tr><td colspan="2">(b)</td><td>Error Bound</td></tr><tr><td>n 1</td><td>Actual Error 4.0523 × 10-2</td><td>4.5153 × 10-2</td></tr><tr><td></td><td>4.6296 × 10-3</td><td>4.6296× 10-3</td></tr><tr><td>2</td><td></td><td></td></tr></table>

<table><tr><td rowspan="3">(c) n</td><td></td></tr><tr><td>Actual Error</td><td>Error Bound</td></tr><tr><td></td><td>6.0971 × 10-3</td></tr><tr><td>1 2</td><td>5.9210 ×10-3 1.7455 × 10-4</td><td>1.8128 × 10-4</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td rowspan="3">(d) n</td><td></td><td>Error Bound</td></tr><tr><td>Actual Error</td><td></td></tr><tr><td>1 2.7296× 10-3 2 5.1789 × 10-3</td><td>1.4080 × 10-2 9.2215×10-3</td></tr></table>

8. Error bounds when $n = 1$ and $n = 2$ are as follows.

(a) 0.06850070205 and 0.02409356045   
(b) 0.2656250000 and 0.09375000000   
(c) 0.001552099938 and 0.0001109161632   
(d) 0.007740087700 and 0.0007457301283

\*9. We have $y = 4 . 2 5$ .

10. The largest value is $x _ { 1 } = 0 . 8 7 2 6 7 7 9 9 6$ .

11. We have $P _ { 3 } ( 1 . 0 9 ) \approx 0 . 2 8 2 6$ . The actual error is $4 . 3 \times 1 0 ^ { - 5 }$ , and an error bound is $7 . 4 \times 1 0 ^ { - 6 }$ . The discrepancy is due to the fact that the data are given to only four decimal places, and only four-digit arithmetic is used.

$^ { * } 1 2$ . The approximation is $\cos { 0 . 7 5 } \approx 0 . 7 3 1 3$ . The actual error is 0.0004, and an error bound is $2 . 7 \times 1 0 ^ { - 8 }$ . The discrepancy is due to the fact that the data are given only to four decimal places and four digit arithmetic is used.

13. (a) $P _ { 2 } ( x ) = - 1 1 . 2 2 3 8 8 8 8 9 x ^ { 2 } + 3 . 8 1 0 5 0 0 0 0 0 x + 1$ . An error bound is 0.11371294. (b) $P _ { 2 } ( x ) = - 0 . 1 3 0 6 3 4 4 1 6 7 x ^ { 2 } + 0 . 8 9 6 9 9 7 9 3 3 5 x - 0 . 6 3 2 4 9 6 9 3 .$ An error bound is $9 . 4 5 7 6 2 \times 1 0 ^ { - 4 }$ . (c) $^ { D } _ { 3 } ( x ) = 0 . 1 9 7 0 0 5 6 6 6 7 x ^ { 3 } - 1 . 0 6 2 5 9 0 5 5 x ^ { 2 } + 2 . 5 3 ^ { 2 }$ $- 1 . 0 6 2 5 9 0 5 5 x ^ { 2 } + 2 . 5 3 2 4 5 3 1 8 9 x - 1 . 6 6 6 8 6 8 3 0 5$ . An error bound is $1 0 ^ { - 4 }$ . (d) $P _ { 3 } ( x ) = - 0 . 0 7 9 3 2 x ^ { 3 } - 0 . 5 4 5 5 0 6 x ^ { 2 } + 1 . 0 0 6 5 9 9 2 x + 1$ . An error bound is $1 . 5 9 1 3 7 6 \times 1 0 ^ { - 3 }$ .

14. (a) 1.32436 (b) 2.18350 (c) 1.15277, 2.01191 (d) Parts (a) and (b) are better due to the spacing of the nodes.

$^ *$ 15. Using 10 digits gives $P _ { 3 } ( x ) = 1 . 3 0 2 6 3 7 0 6 6 x ^ { 3 } - 3 . 5 1 1 3 3 3 1 1 8 x ^ { 2 } + 4 . 0 7 1 1 4 1 9 3 6 x - 1 . 6 7 0 0 4 3 5 6 0 , P _ { 3 } ( 1 . 0 9 ) = 6 . 0 9 7 1 1 8 x ^ { 5 }$ 0.282639050, and $| f ( 1 . 0 9 ) - P _ { 3 } ( 1 . 0 9 ) | = 3 . 8 6 4 6 \times 1 0 ^ { - 6 }$ .

16. 0.7317039560

$^ *$ 17. The largest possible step size is 0.004291932, so 0.004 would be a reasonable choice.

18. (a) We have

which gives $P ( 1 9 4 0 ) = 6 4 2 3 9 7$ , $P ( 1 9 7 5 ) = 2 3 0 8 6 3$ , and $P ( 2 0 2 0 ) = - 1 7 5 4 5 5 7$ .

(b) The actual population in 1940 was approximately 132,165,000 as compared to the approximation of 642,397,000, does not lend confidence to the other approximations. Further, the 1975 estimate is also too large and the estimate for 2020 is negative. This is a very poor approximating polynomial.

19. (a) Sample 1: P $\mathsf { \Pi } _ { 6 } ^ { \circ } ( x ) = 6 . 6 7 - 4 2 . 6 4 3 4 x + 1 6 . 1 4 2 7 x ^ { 2 } - 2 . 0 9 4 6 4 x ^ { 3 }$ +0.126902x4−0.00367168x5+ $0 . 0 0 0 0 4 0 9 4 5 8 x ^ { 6 }$ ; Sample 2: P $\geqslant _ { 6 } ( x ) = 6 . 6 7 - 5 . 6 7 8 2 1 x + 2 . 9 1 2 8 1 x ^ { 2 } - 0 . 4 1 3 7 9 9 x ^ { 3 }$ 3+0.0258413x4 0.000752546x5+ 0.00000836160x6 (b) Sample 1: 42.71 mg; Sample 2: 19.42 mg

20. (a) We have

<table><tr><td>x</td><td>erf(x)</td></tr><tr><td>0.0</td><td>0</td></tr><tr><td>0.2</td><td>0.2227</td></tr><tr><td>0.4</td><td>0.4284</td></tr><tr><td>0.6</td><td>0.6039</td></tr><tr><td>0.8 1.0</td><td>0.7421 0.8427</td></tr></table>

(b) Linear interpolation with $x _ { 0 } = 0 . 2$ and $x _ { 1 } = 0 . 4$ gives $\mathrm { e r f } ( { \scriptstyle { \frac { 1 } { 3 } } } ) \ \approx \ 0 . 3 5 9 8$ , and quadratic interpolation with $x _ { 0 } = 0 . 2 , x _ { 1 } = 0 . 4$ , and $x _ { 2 } = 0 . 6$ gives $\mathrm { e r f } ( { \scriptstyle { \frac { 1 } { 3 } } } ) \approx 0 . 3 6 3 2$ . Since $\operatorname { e r f } \left( { \frac { 1 } { 3 } } \right) \approx$ 0.3626, quadratic interpolation is more accurate.

21. Since $g ( x ) = g ( x _ { 0 } ) = 0$ , there exists a number $\xi _ { 1 }$ between $x$ and $x _ { 0 }$ , for which $g ^ { \prime } ( \xi _ { 1 } ) = 0$ . Also, $g ^ { \prime } ( x _ { 0 } ) = 0$ , so there exists a number $\xi _ { 2 }$ between $x _ { 0 }$ and $\xi _ { 1 }$ , for which $g ^ { \prime \prime } ( \xi _ { 2 } ) = 0$ . The process is continued by induction to show that a number $\xi _ { n + 1 }$ between $x _ { 0 }$ and $\xi _ { n }$ exists with $g ^ { ( n + 1 ) } ( \xi _ { n + 1 } ) = 0$ . The error formula for Taylor polynomials follows.

\*22. Since

$$
\begin{array} { l } { { \displaystyle ( ( j + \frac 1 2 ) h ) = 0 , } } \\ { { \displaystyle  \operatorname* { m a x } | g ( x ) | = \operatorname* { m a x } \{ | g ( j h ) | , | g ( ( j + \frac 1 2 ) h ) | , | g ( ( j + 1 ) h ) | \} = \operatorname* { m a x } ( 0 , \frac { h ^ { 2 } } 4 ) , } } \end{array}
$$

so $| g ( x ) | \le h ^ { 2 } / 4$

23. (a) For (i) we have

$$
{ \begin{array} { r l r } { \displaystyle { \mathfrak { z } } _ { 3 } ( x ) = \sum _ { k = 0 } ^ { 3 } { \binom { 3 } { k } } \left( { \frac { k } { 3 } } \right) x ^ { k } ( 1 - x ) ^ { 3 - k } = 0 + { \binom { 3 } { 1 } } \left( { \frac { 1 } { 3 } } \right) x ( 1 - x ) ^ { 2 } + { \binom { 3 } { 2 } } \left( { \frac { 2 } { 3 } } \right) x ^ { 2 } ( 1 - x ) + { \binom { 3 } { 3 } } } & \\ & { } & { = 3 \cdot \left( { \frac { 1 } { 3 } } \right) x ( 1 - 2 x + x ^ { 2 } ) + 3 \cdot \left( { \frac { 2 } { 3 } } \right) ( x ^ { 2 } - x ^ { 3 } ) + x ^ { 3 } = x - 2 x ^ { 2 } + x ^ { 3 } + 2 x ^ { 2 } - 2 x ^ { 3 } + x ^ { 3 } = 0 } \end{array} }
$$

For (ii) we have

$$
{ \begin{array} { r l } & { B _ { 3 } ( x ) = \displaystyle \sum _ { k = 0 } ^ { 3 } { \binom { 3 } { k } } x ^ { k } ( 1 - x ) ^ { 3 - k } = { \binom { 3 } { 0 } } ( 1 - x ) ^ { 3 } + { \binom { 3 } { 1 } } x ( 1 - x ) ^ { 2 } + { \binom { 3 } { 2 } } x ^ { 2 } ( 1 - x ) + { \binom { 3 } { 3 } } x ^ { 3 } } \\ & { \qquad = ( 1 - x ) ^ { 3 } + 3 \cdot x ( 1 - 2 x + x ^ { 2 } ) + 3 \cdot ( x ^ { 2 } - x ^ { 3 } ) + x ^ { 3 } } \\ & { \qquad = ( 1 - 3 x + 3 x ^ { 2 } - x ^ { 3 } ) + ( 3 x - 6 x ^ { 2 } + 3 x ^ { 3 } ) + ( 3 x ^ { 2 } - 3 x ^ { 3 } ) + x ^ { 3 } = 1 } \end{array} }
$$

(b) We have

$$
{ \frac { k } { n } } \cdot { \binom { n } { k } } = { \frac { k } { n } } \cdot { \frac { n ! } { k ! ( n - k ) ! } } = { \frac { ( n - 1 ) ! } { ( k - 1 ) ! ( n - k ) ! } } = { \frac { ( n - 1 ) ! } { ( k - 1 ) ! ( ( n - 1 ) - ( k - 1 ) ) ! } } = { \binom { n - 1 } { k - 1 } } .
$$

(c) First we need to show that when $f ( x ) = 1$ and $n \geq 0$ we have $B _ { n } ( x ) = 1$ , and when $f ( x ) = x$ and $n \geq 1$ we have $B _ { n } ( x ) = x$ . The first of these follows directly from the Binomial Theorem. For the second we will use mathematical induction on $n$ .

When $f ( x ) = x$ and $n = 1$ we have

$$
B _ { 1 } ( x ) = \sum _ { k = 0 } ^ { 1 } { \binom { 1 } { k } } \left( { \frac { k } { 1 } } \right) x ^ { k } ( 1 - x ) ^ { 1 - k } = 0 + 1 \cdot 1 \cdot x = x .
$$

Now assume that for an arbitrary positive integer $n$ we have $B _ { n } ( x ) = x$ . From part (b) we have

Let $j = k - 1$ .

$$
\begin{array} { l } { \displaystyle B _ { n + 1 } ( x ) = \sum _ { k = 0 } ^ { n + 1 } \binom { n + 1 } { k } \left( \frac { k } { n + 1 } \right) x ^ { k } ( 1 - x ) ^ { n + 1 - k } } \\ { \displaystyle = \sum _ { k = 1 } ^ { n + 1 } \binom { n + 1 } { k } \left( \frac { k } { n + 1 } \right) x ^ { k } ( 1 - x ) ^ { n + 1 - k } } \\ { \displaystyle = \sum _ { k = 1 } ^ { n + 1 } \binom { n } { k } x ^ { k } ( 1 - x ) ^ { n + 1 - k } } \\ { \displaystyle = \sum _ { k = 1 } ^ { n + 1 } \binom { n } { k - 1 } x ^ { k } ( 1 - x ) ^ { n + 1 - k } } \\ { \displaystyle = x \sum _ { j = 0 } ^ { n } \binom { n } { j } x ^ { j } ( 1 - x ) ^ { n - j } = x \cdot 1 = x . } \end{array}
$$

This establishes the fact that when $f ( x ) = x$ , $B _ { n } ( x ) = x$ for all $n \geq 1$ .

Now consider the case of $f ( x ) = x ^ { 2 }$ . For this function the $n$ th Bernstein polynomial is

$$
\begin{array} { l } { \displaystyle B _ { n } ( x ) = \sum _ { k = 0 } ^ { n } \binom { n } { k } \left( \frac k n \right) ^ { 2 } x ^ { k } ( 1 - x ) ^ { n - k } } \\ { = \sum _ { k = 1 } ^ { n } \left( \binom n k \frac { k } { n } \right) \left( \frac k n \right) x ^ { k } ( 1 - x ) ^ { n - k } } \\ { = \sum _ { k = 1 } ^ { n } \binom n k \left( { k - 1 } \left( \frac k n \right) x ^ { k } ( 1 - x ) ^ { n - k } \right. } \end{array}
$$

Let $j = k - 1$ . Then

$$
\begin{array} { l } { \displaystyle B _ { n } ( x ) = \sum _ { j = 0 } ^ { n - 1 } \binom { n - 1 } { j } \left( \frac { j + 1 } { n } \right) x ^ { j + 1 } ( 1 - x ) ^ { n - ( j + 1 ) } } \\ { \displaystyle = \sum _ { j = 0 } ^ { n - 1 } \binom { n - 1 } { j } \left( \frac { j } { n } \right) x ^ { j + 1 } ( 1 - x ) ^ { n - ( j + 1 ) } + \sum _ { j = 0 } ^ { n - 1 } \binom { n - 1 } { j } \left( \frac { 1 } { n } \right) x ^ { j + 1 } ( 1 - x ) ^ { n - ( j + 1 ) } } \\ { \displaystyle = \left( \frac { n - 1 } { n } \right) x \sum _ { j = 0 } ^ { n - 1 } \binom { n - 1 } { j } \left( \frac { j } { n - 1 } \right) x ^ { j } ( 1 - x ) ^ { n - 1 - j } + \left( \frac { 1 } { n } \right) x \sum _ { j = 0 } ^ { n - 1 } \binom { n - 1 } { j } x ^ { j } ( 1 - x ) } \\ { \displaystyle = \left( \frac { n - 1 } { n } \right) x \cdot x + \left( \frac { 1 } { n } \right) x \cdot 1 = \frac { n - 1 } { n } x ^ { 2 } + \frac { 1 } { n } x . } \end{array}
$$

(d) $n \geq 2 5 0 { , } 0 0 0$

# Exercise Set 3.2, page 123

1. Interpolation polynomials give the following results.

<table><tr><td colspan="2"></td><td></td><td></td></tr><tr><td rowspan="3">(a)</td><td>n</td><td>xo,x1,..., xn</td><td>Pn(8.4)</td></tr><tr><td>1</td><td>8.3, 8.6</td><td>17.87833</td></tr><tr><td>2</td><td>8.3, 8.6, 8.7</td><td>17.87716</td></tr><tr><td></td><td>3</td><td>8.3, 8.6, 8.7, 8.1</td><td>17.87714</td></tr></table>

<table><tr><td colspan="2">(b)</td><td>Pn(-1/3)</td></tr><tr><td>n</td><td>xo,x1,...,xn</td><td></td></tr><tr><td>1</td><td>-0.5,-0.25</td><td>0.21504167</td></tr><tr><td>2</td><td>-0.5, -0.25, 0.0</td><td>0.16988889</td></tr><tr><td>3</td><td>-0.5,-0.25, 0.0, -0.75</td><td>0.17451852</td></tr></table>

<table><tr><td colspan="3">(c)</td></tr><tr><td colspan="3"></td></tr><tr><td>n</td><td>xo,x1,...,xn</td><td>Pn(0.25) -0.13869287</td></tr><tr><td>1</td><td>0.2, 0.3</td><td>-0.13259734</td></tr><tr><td>2</td><td>0.2, 0.3, 0.4</td><td></td></tr><tr><td>3</td><td>0.2, 0.3, 0.4, 0.1</td><td>-0.13277477</td></tr></table>

<table><tr><td colspan="2">(d)</td><td></td></tr><tr><td>n</td><td>xo,x1,...,xn</td><td>Pn(0.9)</td></tr><tr><td>1</td><td>0.8, 1.0</td><td>0.44086280</td></tr><tr><td>2</td><td>0.8, 1.0, 0.7</td><td>0.43841352</td></tr><tr><td>3</td><td>0.8, 1.0, 0.7, 0.6</td><td>0.44198500</td></tr></table>

2. Interpolation polynomials give the following results.

(a) $P _ { 1 , 2 } = 2 . 4 1 8 8 0 3 2 0 0$ $| f ( 0 . 4 3 ) - P _ { 1 , 2 } | = 0 . 0 5 5 6 4 2 5 0 6$ ; $P _ { 1 , 2 , 3 } = 2 . 3 4 8 8 6 3 1 2 0$ ; $| f ( 0 . 4 3 ) - P _ { 1 , 2 , 3 } | = 0 . 0 1 4 2 9 7 5 7 4$ $P _ { 0 , 1 , 2 , 3 } = 2 . 3 6 0 6 0 4 7 3 4$ ; $| f ( 0 . 4 3 ) - P _ { 0 , 1 , 2 , 3 } | = 0 . 0 0 2 5 5 5 9 6 0 e$

\*(b) $P _ { 1 , 2 } = 1 . 0 6 6 4 0 5 5 0 0$ $| f ( 0 . 0 ) - P _ { 1 , 2 } | = 0 . 0 6 6 4 0 5 5 0 0$ ; $P _ { 0 , 1 , 2 } = 0 . 9 5 3 1 2 3 6 6 7 0$ ; $| f ( 0 . 0 ) - P _ { 0 , 1 , 2 } | = 0 . 0 4 6 8 7 6 3 3 3 0$ $P _ { 0 , 1 , 2 , 3 } = 0 . 9 8 4 3 7 4 0 0 0 0$ ; $| f ( 0 . 0 ) - P _ { 0 , 1 , 2 , 3 } | = 0 . 0 1 5 6 2 6 0 0 0 0$   
(c) $P _ { 0 , 1 } = - 0 . 5 0 6 6 4 7 8 4 4$ $| f ( 0 . 1 8 ) - P _ { 0 , 1 } | = 0 . 0 0 1 4 7 5 6 2 0 4$ ; $P _ { 0 , 1 , 2 } = - 0 . 5 0 8 0 4 9 8 5 2 0$ ; $| f ( 0 . 1 8 ) - P _ { 0 , 1 , 2 } | = 0 . 0 0 0 0 7 3 6 1 2 4$ $P _ { 0 , 1 , 2 , 3 } = - 0 . 5 0 8 1 4 3 0 7 4 5$ ; $| f ( 0 . 1 8 ) - P _ { 0 , 1 , 2 , 3 } | = 0 . 0 0 0 0 1 9 6 1 0 1$   
(d) $P _ { 2 , 3 } = 1 . 1 9 6 4 9 4 5 0 0$ $| f ( 0 . 2 5 ) - P _ { 2 , 3 } | = 0 . 0 0 7 4 2 4 5 6 9$ ; $P _ { 1 , 2 , 3 } = 1 . 1 8 9 5 9 7 9 7 6$ ; $| f ( 0 . 2 5 ) - P _ { 1 , 2 , 3 } | = 0 . 0 0 0 5 2 8 0 4 5$ $P _ { 0 , 1 , 2 , 3 } = 1 . 1 8 8 9 3 5 1 4 7$ ; $| f ( 0 . 2 5 ) - P _ { 0 , 1 , 2 , 3 } | = 0 . 0 0 0 1 3 4 7 8 4$

\*3. (a) We have ${ \sqrt { 3 } } \approx P _ { 0 , 1 , 2 , 3 , 4 } = 1 . 7 0 8 { \overline { { 3 } } }$ . (b) We have ${ \sqrt { 3 } } \approx P _ { 0 , 1 , 2 , 3 , 4 } = 1 . 6 9 0 6 0 7$ . (c) Absolute error in part (a) is approximately 0.0237, and the absolute error in part (b) is 0.0414, so part (a) is more accurate.

4. The Neville table is

<table><tr><td>xo= 0.0 x1= 0.5</td><td</table>

Since the last difference is $0$ , $y = 5$ .

5. $P _ { 2 } = f ( 0 . 5 ) = 4$   
\*6. $P _ { 2 } = f ( 0 . 7 ) = 6 . 4$   
7. $P _ { 0 , 1 , 2 , 3 } ( 2 . 5 ) = 2 . 8 7 5$   
8. $P _ { 0 , 1 , 2 , 3 } ( 1 . 5 ) = 3 . 6 2 5$   
9. The approximation is

$$
- \frac { 1 } { 6 } f ( 2 ) + \frac { 2 } { 3 } f ( 1 ) + \frac { 2 } { 3 } + \frac { 2 } { 3 } f ( - 1 ) - \frac { 1 } { 6 } f ( - 2 ) ,
$$

and the correct values is

$$
- \frac { 1 } { 6 } f ( 2 ) + \frac { 2 } { 3 } f ( 1 ) + \frac { 2 } { 3 } f ( - 1 ) - \frac { 1 } { 6 } f ( - 2 ) ,
$$

so the approximation is too large by the amount $\frac { 2 } { 3 }$

$^ { * } 1 0$ . The approximation is

$$
- \frac { 1 } { 6 } f ( 2 ) + \frac { 2 } { 3 } f ( 1 ) - \frac { 2 } { 3 } + \frac { 2 } { 3 } f ( - 1 ) - \frac { 1 } { 6 } f ( - 2 ) ,
$$

and the correct values is

$$
- \frac { 1 } { 6 } f ( 2 ) + \frac { 2 } { 3 } f ( 1 ) + \frac { 2 } { 3 } f ( - 1 ) - \frac { 1 } { 6 } f ( - 2 ) ,
$$

so the approximation is too small by the amount $\frac { 2 } { 3 }$ .

11. The first ten terms of the sequence are 0.038462, 0.333671, 0.116605, −0.371760, −0.0548919, 0.605935, 0.190249, $-$ 0.513353, −0.0668173, and 0.448335. Since $f ( 1 + \sqrt { 1 0 } ) = 0 . 0 5 4 5 7 1 6$ , the sequence does not appear to converge.

12. The solution is approximately 0.567142.

$^ *$ 13. Change Algorithm 3.1 as follows:

INPUT numbers $y _ { 0 } , y _ { 1 } , . . . , y _ { n }$ ; values $x _ { 0 } , x _ { 1 } , . . . , x _ { n }$ as the first column $Q _ { 0 , 0 } , Q _ { 1 , 0 } , . . . , Q _ { n , 0 }$ of $Q$ .   
OUTPUT the table $Q$ with $Q _ { n , n }$ approximating $f ^ { - 1 } ( 0 )$ .

STEP 1 For i = 1, 2, ..., n for j = 1, 2, ..., i set

$$
Q _ { i , j } = \frac { y _ { i } Q _ { i - 1 , j - 1 } - y _ { i - j } Q _ { i , j - 1 } } { y _ { i } - y _ { i - j } } .
$$

# Exercise Set 3.3, page 133

1. The interpolating polynomials are as follows.

$^ *$ (a) $^ { D } _ { 1 } ( x ) = 1 6 . 9 4 4 1 + 3 . 1 0 4 1 ( x - 8 . 1 ) ; P _ { 1 } ( 8 . 4 ) = 1 ^ { \prime }$ 7.87533 ${ } _ { 2 } ^ { D } ( x ) = P _ { 1 } ( x ) + 0 . 0 6 ( x - 8 . 1 ) ( x - 8 . 3 ) ; P _ { 2 } ( 8 . 4 )$ = 17.87713 $P _ { 3 } ( x ) = P _ { 2 } ( x ) + - 0 . 0 0 2 0 8 3 3 3 ( x - 8 . 1 ) ( x - 8 . 3 ) ( x - 8 . 6 ) ; P _ { 3 } ( 8 . 4 $ ) = 17.87714   
(b) $P _ { 1 } ( x ) = - 0 . 1 7 6 9 4 4 6 + 1 . 9 0 6 9 6 8 7 ( x - 0 . 6 ) ; P _ { 1 } ( 0 . 9 ) = 0 . 3 9 5 1 4 6$ $P _ { 2 } ( x ) = P _ { 1 } ( x ) + 0 . 9 5 9 2 2 4 ( x - 0 . 6 ) ( x - 0 . 7 ) ; P _ { 2 } ( 0 . 9 ) = 0 . 4 5 2 6 9 9 5$ $P _ { 3 } ( x ) = P _ { 2 } ( x ) - 1 . 7 8 5 7 4 1 ( x - 0 . 6 ) ( x - 0 . 7 ) ( x - 0 . 8 ) ; P _ { 3 } ( 0 . 9 ) = 0 . 4 4 1 9 8 5 0$

2. The interpolating polynomials are as follows.

(a) $P _ { 1 } ( x ) = 1 . 0 + 2 . 5 9 4 8 8 0 0 0 0 x ; P _ { 1 } ( 0 . 4 3 ) = 2 . 1 1 5 7 $ 98400 $P _ { 2 } ( x ) = P _ { 1 } ( x ) + 3 . 3 6 6 7 2 0 0 0 0 x ( x - 0 . 2 5 ) ; P _ { 2 } ( 0 . 4 3 ) = 2 . 3 7 6 3 8 2 5 2 8$ $P _ { 3 } ( x ) = P _ { 2 } ( x ) + 2 . 9 1 2 1 0 6 6 6 7 x ( x - 0 . 2 5 ) ( x - 0 . 5 ) ; P _ { 3 } ( 0 . 4 3 ) = 2 . 3 6 0 6 0 4 7 3 4$   
(b) $P _ { 1 } ( x ) = 0 . 7 2 6 5 6 0 0 0 0 - 2 . 4 2 1 8 8 0 0 0 0 x ; P _ { 1 } ( 0 ) = 0 . 7 2 6 5 6 0 0 0 0$ $P _ { 2 } ( x ) = P _ { 1 } ( x ) + 1 . 8 1 2 5 0 9 3 3 3 ( x + 0 . 5 ) ( x + 0 . 2 5 ) ; P _ { 2 } ( 0 ) = 0 . 9 5 3 1 2 3 6 6 6 6$ $P _ { 3 } ( x ) = P _ { 2 } ( x ) - 1 . 0 0 0 0 1 0 6 6 6 ( x + 0 . 5 ) ( x + 0 . 2 5 ) ( x - 0 . 2 5 ) ; P _ { 3 } ( 0 ) = 0 . 9 8 4 3 7 3 9 9 9$

3. In the following equations, we have $s = \left( 1 / h \right) \left( x - x _ { 0 } \right)$ .

(a) $P _ { 1 } ( s ) = - 0 . 7 1 8 1 2 5 - 0 . 0 4 7 0 6 2 5 s ;$ ; $P _ { 1 } \left( - { \frac { 1 } { 3 } } \right) = - 0 . 0 0 6 6 2 5$ $P _ { 2 } ( s ) = P _ { 1 } ( s ) + 0 . 3 1 2 6 2 5 s ( s - 1 ) / 2$ ; $P _ { 2 } \left( - { \textstyle \frac { 1 } { 3 } } \right) = 0 . 1 8 0 3 0 5 6$ $P _ { 3 } ( s ) = P _ { 2 } ( s ) + 0 . 0 9 3 7 5 s ( s - 1 ) ( s - 2 ) / 6$ ; $P _ { 3 } \left( - { \textstyle { \frac { 1 } { 3 } } } \right) = 0 . 1 7 4 5 1 8 5$   
(b) $P _ { 1 } ( s ) = - 0 . 6 2 0 4 9 9 5 8 + 0 . 3 3 6 5 1 2 9 s$ ; $P _ { 1 } ( 0 . 2 5 ) = - 0 . 1 1 5 7 3 0 2$ $P _ { 2 } ( s ) = P _ { 1 } ( s ) - 0 . 0 4 5 9 2 5 2 7 s ( s - 1 ) / 2$ ; $P _ { 2 } ( 0 . 2 5 ) = - 0 . 1 3 2 9 5 2 2$ 2 $P _ { 3 } ( s ) = P _ { 2 } ( s ) - 0 . 0 0 2 8 3 8 9 1 s ( s - 1 ) ( s - 2 ) / 6$ ; $P _ { 3 } ( 0 . 2 5 ) = - 0 . 1 3 2 7 7 4 8$

4. In the following equations, we have $s = ( 1 / h ) ( x - x _ { 0 } )$ .

$^ *$ (a) $P _ { 1 } ( s ) = 1 . 0 + 0 . 6 4 8 7 2 0 0 0 0 0 s$ ; $P _ { 1 } ( 0 . 4 3 ) = 2 . 1 1 5 7 9 8 4 0 0$ $P _ { 2 } ( s ) = P _ { 1 } ( s ) + 0 . 2 1 0 4 2 0 0 0 0 0 s ( s - 1 )$ ; $P _ { 2 } ( 0 . 4 3 ) = 2 . 3 7 6 3 8 2 5 2 8$ $P _ { 3 } ( s ) = P _ { 2 } ( s ) + 0 . 0 4 5 5 0 1 6 6 6 6 7 s ( s - 1 ) ( s - 2 )$ ; $P _ { 3 } ( 0 . 4 3 ) = 2 . 3 6 0 6 0 4 7 3 4$   
(b) $P _ { 1 } ( s ) = - 0 . 2 9 0 0 4 9 8 6 - 0 . 2 7 0 7 4 7 4 8 0 0 s ; P$ $P _ { 1 } ( 0 . 1 8 ) = - 0 . 5 0 6 6 4 7 8 4 4 0$ $P _ { 2 } ( s ) = P _ { 1 } ( s ) + 0 . 0 0 8 7 6 2 5 5 0 0 0 0 s ( s - 1 )$ ; $P _ { 2 } ( 0 . 1 8 ) = - 0 . 5 0 8 0 4 9 8 5 2 0$ $P _ { 3 } ( s ) = P _ { 2 } ( s ) - 0 . 0 0 0 4 8 5 5 3 3 3 3 3 s ( s - 1 ) ( s - 2 )$ ; $P _ { 3 } ( 0 . 1 8 ) = - 0 . 5 0 8 1 4 3 0 7 4 4$

5. In the following equations, we have $s = ( 1 / h ) \left( x - x _ { n } \right)$ .

(a) $P _ { 1 } ( s ) = 1 . 1 0 1 + 0 . 7 6 6 0 6 2 5 s$ ; $f ( - { \textstyle { \frac { 1 } { 3 } } } ) \approx P _ { 1 } ( - { \textstyle { \frac { 4 } { 3 } } } ) = 0 . 0 7 9 5 8 3 3 3$ $P _ { 2 } ( s ) = P _ { 1 } ( s ) + 0 . 4 0 6 3 7 5 s ( s + 1 ) / 2$ ; $f ( - { \textstyle \frac { 1 } { 3 } } ) \approx P _ { 2 } ( - { \textstyle \frac { 4 } { 3 } } ) = 0 . 1 6 9 8 8 8 9$ $P _ { 3 } ( s ) = P _ { 2 } ( s ) + 0 . 0 9 3 7 5 s ( s + 1 ) ( s + 2 ) / 6$ ; $f ( - { \textstyle \frac { 1 } { 3 } } ) \approx P _ { 3 } ( - { \textstyle \frac { 4 } { 3 } } ) = 0 . 1 7 4 5 1 8 5$   
(b) $P _ { 1 } ( s ) = 0 . 2 4 8 4 2 4 4 + 0 . 2 4 1 8 2 3 5 s ;$ $f ( 0 . 2 5 ) \approx P _ { 1 } ( - 1 . 5 ) = - 0 . 1 1 4 3 1 0 8$ $P _ { 2 } ( s ) = P _ { 1 } ( s ) - 0 . 0 4 8 7 6 4 1 9 s ( s + 1 ) / 2$ ; $f ( 0 . 2 5 ) \approx P _ { 2 } ( - 1 . 5 ) = - 0 . 1 3 2 5 9 7 3$ $P _ { 3 } ( s ) = P _ { 2 } ( s ) - 0 . 0 0 2 8 3 8 9 1 s ( s + 1 ) ( s + 2 ) / 6$ ; $f ( 0 . 2 5 ) \approx P _ { 3 } ( - 1 . 5 ) = - 0 . 1 3 2 7 7 4 8$

6. In the following equations, we have $s = \left( 1 / h \right) \left( x - x _ { 0 } \right)$ .

$^ *$ (a) $P _ { 1 } ( s ) = 4 . 4 8 1 6 9 + 1 . 7 6 3 4 1 0 0 0 0 s$ ; $P _ { 1 } ( 0 . 4 3 ) = 2 . 2 2 4 5 2 5 2 0 0$ $P _ { 2 } ( s ) = P _ { 1 } ( s ) + 0 . 3 4 6 9 2 5 0 0 0 0 s ( s + 1 ) ;$ $P _ { 2 } ( 0 . 4 3 ) = 2 . 3 4 8 8 6 3 1 2 0$ $P _ { 3 } ( s ) = P _ { 2 } ( s ) + 0 . 0 4 5 5 0 1 6 6 6 7 s ( s + 1 ) ( s + 2 ) ; \quad P _ { 3 } ( 0 . 4 3 ) = 2$ $P _ { 3 } ( 0 . 4 3 ) = 2 . 3 6 0 6 0 4 7 3 4$ (b) $P _ { 1 } ( s ) = 1 . 2 9 4 3 7 6 7 + 0 . 1 9 5 7 6 4 4 0 0 0 s ;$ $P _ { 1 } ( 0 . 2 5 ) = 1 . 1 9 6 4 9 4 5 0 0$ $P _ { 2 } ( s ) = P _ { 1 } ( s ) + 0 . 0 2 7 5 8 6 0 9 5 0 0 s ( s + 1 )$ ; $P _ { 2 } ( 0 . 2 5 ) = 1 . 1 8 9 5 9 7 9 7 6$ $P _ { 3 } ( s ) = P _ { 2 } ( s ) + 0 . 0 0 1 7 6 7 5 4 5 0 0 0 s ( s + 1 ) ( s + 2 ) ; \quad P _ { 3 } ( 0 . 2 5 ) = 1 . 1 8 8 9 3 5 1 4 7$ $^ { * } 7$ . (a) $P _ { 3 } ( x ) = 5 . 3 - 3 3 ( x + 0 . 1 ) + 1 2 9 . 8 { \overline { { 3 } } } ( x + 0 . 1 ) x - 5 5 6 . { \overline { { 6 } } } ( x + 0 . 1 ) x ( x - 0 . 2 )$ (b) $P _ { 4 } ( x ) = P _ { 3 } ( c ) + 2 7 3 0 . 2 4 3 3 8 7 ( x + 0 . 1 ) x ( x - 0 . 2 ) ( x - 0 . 3 )$

8. (a) $P _ { 4 } ( x ) = - 6 + 1 . 0 5 1 7 0 x + 0 . 5 7 2 5 0 x ( x - 0 . 1 ) + 0 . 2 1 5 0 0 x ( x - 0 . 1 ) ( x - 0 . 3 ) + 0 . 0 6 3 0 1 6 x ( x - 0 . 3 )$ $0 . 1 ) ( x - 0 . 3 ) ( x - 0 . 6 )$ (b) Ad $\mathrm { ~ l d ~ } 0 . 0 1 4 1 5 9 x ( x - 0 . 1 ) ( x - 0 . 3 ) ( x - 0 . 6 ) ( x - 1 )$ to the answer in part (a).

9. (a) $f ( 0 . 0 5 ) \approx 1 . 0 5 1 2 6$ (b) $f ( 0 . 6 5 ) \approx 1 . 9 1 5 5 5$ (c) $f ( 0 . 4 3 ) \approx 1 . 5 3 7 2 5$

10. $\Delta ^ { 3 } f ( x _ { 0 } ) = - 6$ , $\Delta ^ { 4 } f ( x _ { 0 } ) = \Delta ^ { 5 } f ( x _ { 0 } ) = 0$ , so the interpolating polynomial has degree 3.

$^ { * } 1 1$ . (a) $P ( - 2 ) = Q ( - 2 ) = - 1 , P ( - 1 ) = Q ( - 1 ) = 3 , P$ $P ( 0 ) = Q ( 0 ) = 1$ , $P ( 1 ) = Q ( 1 ) = - 1$ , $P ( 2 ) = Q ( 2 ) = 3$ (b) The format of the polynomial is not unique. If $P ( x )$ and $Q ( x )$ are expanded, they are identical. There is only one interpolating polynomial if the degree is less than or equal to four for the given data. However, it can be expressed in various ways depending on the application.

$^ *$ 12. $\Delta ^ { 2 } P ( 1 0 ) = 1 1 4 0$ $^ \mathrm { * _ { 1 3 } }$ . The coefficient of $x ^ { 2 }$ is 3.5.

14. The coefficient of $x ^ { 3 }$ is $- 1 1 / 1 2$ .

$^ \mathrm { * _ { 1 5 } }$ . The approximation to $f ( 0 . 3 )$ should be increased by 5.9375.

16. $f ( 0 . 7 5 ) = 1 0$

$^ *$ 17. $f [ x _ { 0 } ] = f ( x _ { 0 } ) = 1$ , $f [ x _ { 1 } ] = f ( x _ { 1 } ) = 3$ , f [x0, x1] = 5

18. The results of this exercise are the same as those of Exercise 18 in Section 3.1, because the polynomial is the same.

19. Since $f [ x _ { 2 } ] = f [ x _ { 0 } ] + f [ x _ { 0 } , x _ { 1 } ] ( x _ { 2 } - x _ { 0 } ) + a _ { 2 } ( x _ { 2 } - x _ { 0 } ) ( x _ { 2 } - x _ { 1 } ) ,$

$$
a _ { 2 } = { \frac { f [ x _ { 2 } ] - f [ x _ { 0 } ] } { ( x _ { 2 } - x _ { 0 } ) ( x _ { 2 } - x _ { 1 } ) } } - { \frac { f [ x _ { 0 } , x _ { 1 } ] } { ( x _ { 2 } - x _ { 1 } ) } } .
$$

This simplifies to $f [ x _ { 0 } , x _ { 1 } , x _ { 2 } ]$ .

$^ *$ 20. Theorem 3.3 gives

$$
f ( x ) = P _ { n } ( x ) + { \frac { f ^ { n + 1 } ( \xi ( x ) ) } { ( n + 1 ) ! } } \left( x - x _ { 0 } \right) \ldots ( x - x _ { n } ) .
$$

Let $x _ { n + 1 } = x$ . The interpolation polynomial of degree $n + 1$ on $x _ { 0 } , x _ { 1 } , \ldots , x _ { n + 1 }$ is

$$
P _ { n + 1 } ( t ) = P _ { n } ( t ) + f \left[ x _ { 0 } , x _ { 1 } , . . . , x _ { n } , x _ { n + 1 } \right] ( t - x _ { 0 } ) ( t - x _ { 1 } ) . . . ( t - x _ { n } ) .
$$

Since $f ( x ) = P _ { n + 1 } ( x )$ , we have

$$
P _ { n } ( x ) + { \frac { f ^ { n + 1 } ( \xi ( x ) ) } { ( n + 1 ) ! } } \left( x - x _ { 0 } \right) \ldots ( x - x _ { n } ) = P _ { n } ( x ) + f \left[ x _ { 0 } , . . . , x _ { n } , x \right] \left( x - x _ { 0 } \right) \ldots \left( x - x _ { n } \right) .
$$

Thus

$$
f \left[ x _ { 0 } , . . . , x _ { n } , x \right] = \frac { f ^ { n + 1 } ( \xi ( x ) ) } { ( n + 1 ) ! } .
$$

21. Let

$$
{ \tilde { P } } ( x ) = f [ x _ { i _ { 0 } } ] + \sum _ { k = 1 } ^ { n } f [ x _ { i _ { 0 } } , \ldots , x _ { i _ { k } } ] ( x - x _ { i _ { 0 } } ) \cdot \cdot \cdot ( x - x _ { i _ { k } } )
$$

and

$$
{ \hat { P } } ( x ) = f [ x _ { 0 } ] + \sum _ { k = 1 } ^ { n } f [ x _ { 0 } , \ldots , x _ { k } ] ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { k } ) .
$$

The polynomial $\tilde { P } ( x )$ interpolates $f ( x )$ at the nodes $x _ { i _ { 0 } } , \ldots , x _ { i _ { n } }$ , and the polynomial $\hat { P } ( x )$ interpolates $f ( x )$ at the nodes $x _ { 0 } , \ldots , x _ { n }$ . Since both sets of nodes are the same and the interpolating polynomial is unique, we have $\tilde { P } ( x ) = \hat { P } ( x )$ . The coefficient of $x ^ { n }$ in $\mathring { P } ( x )$ is $f [ x _ { i _ { 0 } } , \ldots , x _ { i _ { n } } ]$ , and the coefficient of $x ^ { n }$ in $\hat { P } ( x )$ is $f [ x _ { 0 } , \ldots , x _ { n } ]$ . Thus

$$
f [ x _ { i _ { 0 } } , \dots , x _ { i _ { n } } ] = f [ x _ { 0 } , \dots , x _ { n } ] .
$$

# Exercise Set 3.4, page 142

1. The coefficients for the polynomials in divided-difference form are given in the following tables. For example, the polynomial in part (a) is

$$
H _ { 3 } ( x ) = 1 7 . 5 6 4 9 2 + 3 . 1 1 6 2 5 6 ( x - 8 . 3 ) + 0 . 0 5 9 4 8 ( x - 8 . 3 ) ^ { 2 } - 0 . 0 0 2 0 2 2 2 ( x - 8 . 3 ) ^ { 2 } ( x - 8 . 6 ) .
$$

<table><tr><td>(a)</td><td>(b)</td><td>(c)</td><td>(d）</td></tr><tr><td>17.56492</td><td>0.22363362</td><td>-0.02475</td><td>-0.62049958</td></tr><tr><td>3.116256</td><td>2.1691753</td><td>0.751</td><td>3.5850208</td></tr><tr><td>0.05948</td><td>0.01558225</td><td>2.751</td><td>-2.1989182</td></tr><tr><td>-0.00202222</td><td>-3.2177925</td><td>1</td><td>-0.490447</td></tr><tr><td></td><td></td><td>0</td><td>0.037205</td></tr><tr><td></td><td></td><td>0</td><td>0.040475</td></tr><tr><td></td><td></td><td></td><td>-0.0025277777</td></tr><tr><td></td><td></td><td></td><td>0.0029629628</td></tr></table>

2. The coefficients for the polynomials in divided-difference form are given in the following tables. For example, the polynomial in part (a) is $H _ { 3 } ( x ) = 1 + 2 x + 2 . 8 7 3 1 2 x ^ { 2 } + 2 . 2 5 3 7 6 x ^ { 2 } ( x - 0 . 5 )$   

<table><tr><td>(a)</td><td>(b)</td><td>*（c）</td><td>(d)</td></tr><tr><td>1.0</td><td>1.33203</td><td>-0.29004996</td><td>0.8619948</td></tr><tr><td>2.0</td><td>0.4375</td><td>-2.8019975</td><td>0.1553624</td></tr><tr><td>2.87312</td><td>-2.999996</td><td>0.945237</td><td>0.07337636</td></tr><tr><td>2.25376</td><td>7.749984</td><td>-0.297</td><td>0.01583112</td></tr><tr><td></td><td></td><td>-0.47935</td><td>-0.00014728</td></tr><tr><td></td><td></td><td>0.05</td><td>-0.00089244</td></tr><tr><td></td><td></td><td></td><td>-0.00007672</td></tr><tr><td></td><td></td><td></td><td>0.00005975111111</td></tr></table>

3. The following table shows the approximations.

<table><tr><td>X</td><td>Approximation to f(x)</td><td>Actual f(x）</td><td>Error</td></tr><tr><td>(@) 8.4</td><td>17.877144</td><td>17.877146</td><td>2.33 × 10-6</td></tr><tr><td>(b) 0.9</td><td>0.44392477</td><td>0.44359244</td><td>3.3323 × 10-4</td></tr><tr><td>（c) -</td><td>0.1745185</td><td>0.17451852</td><td>1.85 × 10-8</td></tr><tr><td>(d) 0.25</td><td>-0.1327719</td><td>-0.13277189</td><td>5.42 × 10-9</td></tr></table>

4. The following table shows the approximations.

<table><tr><td>X</td><td>Approximation to f(x)</td><td>Actual f(x)</td><td>Error</td></tr><tr><td>(a) 0.43</td><td>2.362069472</td><td>2.363160694</td><td>0.001091222</td></tr><tr><td>(b) 0.0</td><td>1.132811175</td><td>1.000000000</td><td>0.132811750</td></tr><tr><td>*（c） 0.18</td><td>-0.5081234697</td><td>-0.5081234644</td><td>0.53 × 10-8</td></tr><tr><td>(d) 0.25</td><td>1.189069883</td><td>1.189069931</td><td>0.48 ×10-7</td></tr></table>

5. (a) We have $\sin 0 . 3 4 \approx H _ { 5 } ( 0 . 3 4 ) = 0 . 3 3 3 4 9$ . (b) The formula gives an error bound of $3 . 0 5 \times 1 0 ^ { - 1 4 }$ , but the actual error is $2 . 9 1 \times 1 0 ^ { - 6 }$ . The discrepancy is due to the fact that the data are given to only five decimal places. (c) We have $\sin 0 . 3 4 \approx H _ { 7 } ( 0 . 3 4 ) = 0 . 3 3 3 5 0$ . Although the error bound is now $5 . 4 \times 1 0 ^ { - 2 0 }$ , the accuracy of the given data dominates the calculations. This result is actually less accurate than the approximation in part (b), since $\sin 0 . 3 4 = 0 . 3 3 3 4 8 7$ .

6. (a) $H ( 1 . 0 3 ) = 0 . 8 0 9 3 2 4 8 5$ . The actual error is $1 . 2 4 \times 1 0 ^ { - 6 }$ , and error bound is $1 . 3 1 \times 1 0 ^ { - 6 }$ . (b) $H ( 1 . 0 3 ) = 0 . 8 0 9 3 2 3 6 1 9 2 6 3$ . The actual error is $3 . 6 3 \times 1 0 ^ { - 1 0 }$ , and an error bound is 3.86 10−10.

7. For 3(a), we have an error bound of $5 . 9 \times 1 0 ^ { - 8 }$ . The error bound for $3 ( \mathrm { c } )$ is $0$ since $f ^ { ( n ) } ( x ) \equiv 0$ , for $n > 3$ .

8. For 4(a), we have an error bound of $1 . 6 \times 1 0 ^ { - 3 }$ . The error bound for $4 ( \mathrm { c } )$ is $1 . 5 \times 1 0 ^ { - 7 }$ .

$^ { * } 9$ . $H _ { 3 } ( 1 . 2 5 ) = 1 . 1 6 9 0 8 0 4 0 3$ with an error bound of $4 . 8 1 \times 1 0 ^ { - 5 }$ , and $H _ { 5 } ( 1 . 2 5 ) = 1 . 1 6 9 0 1 6 0 6 4$ with an error bound of $4 . 4 3 \times 1 0 ^ { - 4 }$ .

10. The Hermite polynomial generated from these data is

$$
\begin{array} { r l } & { 7 5 x + 0 . 2 2 2 2 2 x ^ { 2 } ( x - 3 ) - 0 . 0 3 1 1 1 1 1 x ^ { 2 } ( x - 3 ) ^ { 2 } } \\ & { - 0 . 0 0 6 4 4 4 4 4 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) + 0 . 0 0 2 2 6 3 8 9 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) ^ { 2 } } \\ & { - 0 . 0 0 0 9 1 3 1 9 4 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) ^ { 2 } ( x - 8 ) + 0 . 0 0 0 1 3 0 5 2 7 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) ^ { 2 } ( x - 8 ) ^ { 2 } } \\ & { - 0 . 0 0 0 0 2 0 2 2 3 6 x ^ { 2 } ( x - 3 ) ^ { 2 } ( x - 5 ) ^ { 2 } ( x - 8 ) ^ { 2 } ( x - 1 3 ) . } \end{array}
$$

(a) The Hermite polynomial predicts a position of $H _ { 9 } ( 1 0 ) = 7 4 3$ ft and a speed of $H _ { 9 } ^ { \prime } ( 1 0 ) =$ 48 ft/sec. Although the position approximation is reasonable, the low speed prediction is suspect.

(b) To find the first time the speed exceeds 55 mi/hr, which is equivalent to 80.¯6 ft/sec, we solve for the smallest value of $t$ in the equation $8 0 . 6 = H _ { 9 } ^ { \prime } ( x )$ . This gives $x \approx 5 . 6 4 8 8 0 9 2$ .

(c) The estimated maximum speed is $H _ { 9 } ^ { \prime } ( 1 2 . 3 7 1 8 7 ) = 1 1 9 . 4 2 3$ ft/sec ≈ 81.425 mi/hr.

$^ *$ 11. (a) Suppose $P ( x )$ is another polynomial with $P \left( x _ { k } \right) = f \left( x _ { k } \right)$ and $P ^ { \prime } \left( x _ { k } \right) = f ^ { \prime } \left( x _ { k } \right)$ , for $k = 0 , . . . , n$ , and the degree of $P ( x )$ is at most $2 n + 1$ . Let

$$
D ( x ) = H _ { 2 n + 1 } ( x ) - P ( x ) .
$$

Then $D ( x )$ is a polynomial of degree at most $2 n + 1$ with $D \left( x _ { k } \right) = 0$ , and $D ^ { \prime } \left( x _ { k } \right) = 0$ , for each $k = 0 , 1 , . . . , n$ . Thus, $D$ has zeros of multiplicity 2 at each $x _ { k }$ and

$$
D ( x ) = \left( x - x _ { 0 } \right) ^ { 2 } \ldots \left( x - x _ { n } \right) ^ { 2 } Q ( x ) .
$$

Hence, $D ( x )$ must be of degree $2 n$ or more, which would be a contradiction, or $Q ( x ) \equiv 0$ which implies that $D ( x ) \equiv 0$ . Thus, $P ( x ) \equiv H _ { 2 n + 1 } ( x )$ .

(b) First note that the error formula holds if $x = x _ { k }$ for any choice of $\xi$ .

Let $x \neq x _ { k }$ , for $k = 0 , . . . , n$ , and define

$$
g ( t ) = f ( t ) - H _ { 2 n + 1 } ( t ) - { \frac { { ( t - x _ { 0 } ) } ^ { 2 } \dots { ( t - x _ { n } ) } ^ { 2 } } { { ( x - x _ { 0 } ) } ^ { 2 } \dots { ( x - x _ { n } ) } ^ { 2 } } } \left[ f ( x ) - H _ { 2 n + 1 } ( x ) \right] .
$$

Note that $g ( x _ { k } ) = 0$ , for $k = 0 , . . . , n$ , and $g ( x ) = 0$ . Thus, $g$ has $n + 2$ distinct zeros in $[ a , b ]$ . By Rolle’s Theorem, $g ^ { \prime }$ has $n + 1$ distinct zeros $\xi _ { 0 } , . . . , \xi _ { n }$ , which are between the numbers $x _ { 0 } , . . . , x _ { n } , x$ .

In addition, $g ^ { \prime } ( x _ { k } ) = 0$ , for $k = 0 , . . . , n$ , so $g ^ { \prime }$ has $2 n + 2$ distinct zeros $\xi _ { 0 } , . . . , \xi _ { n } , x _ { 0 } , . . . , x _ { n }$ . Since $g ^ { \prime }$ is $2 n + 1$ times differentiable, the Generalized Rolle’s Theorem implies that a number $\xi \operatorname { i n } [ a , b ]$ exists with $g ^ { ( 2 n + 2 ) } ( \xi ) = 0$ . But,

$$
g ^ { ( 2 n + 2 ) } ( t ) = f ^ { ( 2 n + 2 ) } ( t ) - { \frac { d ^ { 2 n + 2 } } { d t ^ { 2 n + 2 } } } H _ { 2 n + 1 } ( t ) - { \frac { \left[ f ( x ) - H _ { 2 n + 1 } ( x ) \right] \cdot ( 2 n + 2 ) ! } { ( x - x _ { 0 } ) ^ { 2 } \cdot \cdot \cdot ( x - x _ { n } ) ^ { 2 } } }
$$

and

$$
0 = g ^ { ( 2 n + 2 ) } ( { \xi } ) = f ^ { ( 2 n + 2 ) } ( { \xi } ) - \frac { ( 2 n + 2 ) ! [ f ( x ) - H _ { 2 n + 1 } ( x ) ] } { ( x - x _ { 0 } ) ^ { 2 } \cdots ( x - x _ { n } ) ^ { 2 } } .
$$

The error formula follows.

12. Let

$$
H ( x ) = f [ z _ { 0 } ] + f [ z _ { 0 } , z _ { 1 } ] ( x - x _ { 0 } ) + f [ z _ { 0 } , z _ { 1 } , z _ { 2 } ] ( x - x _ { 0 } ) ^ { 2 } + f [ z _ { 0 } , z _ { 1 } , z _ { 2 } , z _ { 3 } ] ( x - x _ { 0 } ) ^ { 2 } ( x - x _ { 1 } ) .
$$

Substituting $f [ z _ { 0 } ] = f ( x _ { 0 } )$ , $f [ z _ { 0 } , z _ { 1 } ] = f ^ { \prime } ( x _ { 0 } )$ ,

$$
f [ z _ { 0 } , z _ { 1 } , z _ { 2 } ] = { \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } } ,
$$

and

$$
f [ z _ { 0 } , z _ { 1 } , z _ { 2 } , z _ { 3 } ] = { \frac { f ^ { \prime } ( x _ { 1 } ) ( x _ { 1 } - x _ { 0 } ) - 2 f ( x _ { 1 } ) + 2 f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 3 } } }
$$

into $H ( x )$ and simplifying gives

$$
\begin{array} { l } { { H ( x ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x - x _ { 0 } ) + \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 2 } } ( x - x _ { 0 } ) ^ { 2 } } } \\ { { + \frac { f ^ { \prime } ( x _ { 1 } ) ( x _ { 1 } - x _ { 0 } ) - 2 f ( x _ { 1 } ) + 2 f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 3 } } ( x - x _ { 0 } ) ^ { 2 } ( x - x _ { 1 } ) . } } \end{array}
$$

Thus, $H ( x _ { 0 } ) = f ( x _ { 0 } )$ and

$$
H ( x _ { 1 } ) = f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) + [ f ( x _ { 1 } ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) ] = f ( x _ { 1 } ) .
$$

Further,

$$
\begin{array} { l } { { H ^ { \prime } ( x ) = f ^ { \prime } ( x _ { 0 } ) + 2 { \frac { f ( x _ { 1 } ) - f ( x _ { 0 } ) - f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 2 } } } ( x - x _ { 0 } ) } } \\ { { \ \qquad + { \frac { f ^ { \prime } ( x _ { 1 } ) ( x _ { 1 } - x _ { 0 } ) - 2 f ( x _ { 1 } ) + 2 f ( x _ { 0 } ) + f ^ { \prime } ( x _ { 0 } ) ( x _ { 1 } - x _ { 0 } ) } { ( x _ { 1 } - x _ { 0 } ) ^ { 3 } } } [ 2 ( x - x _ { 0 } ) ( x - x _ { 1 } ) + ( x - x _ { 0 } ) ( x - x _ { 0 } ) + f ( x - x _ { 0 } ) ] } } \end{array}
$$

so

$$
H ^ { \prime } ( x _ { 0 } ) = f ^ { \prime } ( x _ { 0 } )
$$

$$
\begin{array} { l } { { H ^ { \prime } ( x _ { 1 } ) = f ^ { \prime } ( x _ { 0 } ) + \displaystyle \frac { 2 f ( x _ { 1 } ) } { x _ { 1 } - x _ { 0 } } - \displaystyle \frac { 2 f ( x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } - 2 f ^ { \prime } ( x _ { 0 } ) + f ^ { \prime } ( x _ { 1 } ) - \displaystyle \frac { 2 f ( x _ { 1 } ) } { x _ { 1 } - x _ { 0 } } + \displaystyle \frac { 2 f ( x _ { 0 } ) } { x _ { 1 } - x _ { 0 } } + f ^ { \prime } ( x _ { 0 } ) } } \\ { { \ = f ^ { \prime } ( x _ { 1 } ) . } } \end{array}
$$

Thus, $H$ satisfies the requirements of the cubic Hermite polynomial $H _ { 3 }$ , and the uniqueness of $H _ { 3 }$ implies $H _ { 3 } = H$ .

# Exercise Set 3.5, page 161

$^ * 1$ . We have $S ( x ) = x$ on $[ 0 , 2 ]$ .

and

2. We have $s ( x ) = x$ on $[ 0 , 2 ]$

3. The equations of the respective free cubic splines are

$$
S ( x ) = S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the coefficients are given in the following tables.

\*(a)

<table><tr><td>i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>17.564920</td><td>3.13410000</td><td>0.00000000</td><td>0.00000000</td></tr></table>

<table><tr><td>i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>0.22363362</td><td>2.17229175</td><td>0.00000000</td><td>0.00000000</td></tr></table>

<table><tr><td>i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>-0.02475000</td><td>1.03237500</td><td>0.00000000</td><td>6.50200000</td></tr><tr><td>1</td><td>0.33493750</td><td>2.25150000</td><td>4.87650000</td><td>-6.50200000</td></tr></table>

<table><tr><td>i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>-0.62049958</td><td>3.45508693</td><td>0.00000000</td><td>-8.9957933</td></tr><tr><td>1</td><td>-0.28398668</td><td>3.18521313</td><td>-2.69873800</td><td>-0.94630333</td></tr><tr><td>2</td><td>0.00660095</td><td>2.61707643</td><td>-2.98262900</td><td>9.9420966</td></tr></table>

4. The equations of the respective free cubic splines are

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 }
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the coefficients are given in the following table.

<table><tr><td>i</td><td></td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>(a)</td><td>0</td><td>1.00000000</td><td>3.43656000</td><td>0.00000000</td><td>0.00000000</td></tr><tr><td>(b)</td><td>0</td><td>1.33203000</td><td>-1.06249800</td><td>0.00000000</td><td>0.00000000</td></tr><tr><td>(c)</td><td>0</td><td>-0.29004996</td><td>-2.75128630</td><td>0.00000000</td><td>4.38125000</td></tr><tr><td></td><td>1</td><td>-0.56079734</td><td>-2.61984880</td><td>1.31437500</td><td>-4.38125000</td></tr><tr><td>(d)</td><td>0</td><td>0.86199480</td><td>0.17563785</td><td>0.00000000</td><td>0.06565093</td></tr><tr><td></td><td>1</td><td>0.95802009</td><td>0.22487604</td><td>0.09847639</td><td>0.02828072</td></tr><tr><td></td><td>2</td><td>1.09861230</td><td>0.34456298</td><td>0.14089747</td><td>-0.09393165</td></tr></table>

5. The following tables show the approximations.

<table><tr><td>X</td><td></td><td>Approximation to f(x)</td><td>Actual f(x）</td><td>Error</td></tr><tr><td>*（a)</td><td>8.4</td><td>17.87833</td><td>17.877146</td><td>1.1840 × 10-3</td></tr><tr><td>(b)</td><td>0.9</td><td>0.4408628</td><td>0.44359244</td><td>2.7296 × 10-3</td></tr><tr><td>（c）</td><td>一</td><td>0.1774144</td><td>0.17451852</td><td>2.8959 ×10-3</td></tr><tr><td>(d)</td><td>0.25</td><td>-0.1315912</td><td>-0.13277189</td><td>1.1807 × 10-3</td></tr></table>

<table><tr><td>X</td><td>Approximation to f&#x27;(x)</td><td>Actual f&#x27;(x)</td><td>Error</td></tr><tr><td>(@) 8.4</td><td>3.134100</td><td>3.128232</td><td>5.86829 × 10-3</td></tr><tr><td>(b) 0.9</td><td>2.172292</td><td>2.204367</td><td>0.0320747</td></tr><tr><td>（c） -</td><td>1.574208</td><td>1.668000</td><td>0.093792</td></tr><tr><td>(d) 0.25</td><td>2.908242</td><td>2.907061</td><td>1.18057 × 10-3</td></tr></table>

6. The following tables show the approximations.

<table><tr><td>x</td><td>f(x)</td><td>s(x)</td><td>Error</td></tr><tr><td>(a) 0.43</td><td>2.363160694</td><td>2.4777208</td><td>0.114560106</td></tr><tr><td>(b) 0.0</td><td>1.000000000</td><td>1.066405500</td><td>0.066405500</td></tr><tr><td>（C） 0.18</td><td>-0.5081234644</td><td>-0.5079096640</td><td>0.0002138004</td></tr><tr><td>(d) 0.25</td><td>1.189069931</td><td>1.192091455</td><td>0.003021524</td></tr></table>

<table><tr><td>x</td><td>f&#x27;(x)</td><td>s(x)</td><td>Error</td></tr><tr><td>(@) 0.43</td><td>4.726321388</td><td>3.436560000</td><td>1.289761388</td></tr><tr><td>(b) 0.0</td><td>-1.000000000</td><td>-1.06249800</td><td>0.06249800</td></tr><tr><td>（c） 0.18</td><td>-2.651616829</td><td>-2.66716630</td><td>0.015549471</td></tr><tr><td>(d) 0.25</td><td>0.3909913152</td><td>0.3973995306</td><td>0.0064082154</td></tr></table>

7. The equations of the respective clamped cubic splines are

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } .
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the coefficients are given in the following tables.

\*(a)

<table><tr><td>i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>17.564920</td><td>3.1162560</td><td>0.0600867</td><td>-0.00202222</td></tr></table>

<table><tr><td>i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>0.22363362</td><td>2.1691753</td><td>0.65914075</td><td>-3.2177925</td></tr><tr><td>0</td><td>-0.02475000</td><td>0.75100000</td><td>2.5010000</td><td>1.0000000</td></tr><tr><td>1</td><td>0.33493750</td><td>2.18900000</td><td>3.2510000</td><td>1.0000000</td></tr></table>

<table><tr><td>i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>-0.62049958</td><td>3.5850208</td><td>-2.1498407</td><td>-0.49077413</td></tr><tr><td>1</td><td>-0.28398668</td><td>3.1403294</td><td>-2.2970730</td><td>-0.47458360</td></tr><tr><td>2</td><td>0.006600950</td><td>2.6666773</td><td>-2.4394481</td><td>-0.44980146</td></tr></table>

8. The coefficients of the clamped cubic spline interpolation are given in the following table.   

<table><tr><td></td><td>i</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>(a)</td><td>0</td><td>1.00000000</td><td>2.00000000</td><td>1.74624000</td><td>2.25376000</td></tr><tr><td>(b)</td><td>0</td><td>1.33203000</td><td>0.43750000</td><td>-6.87498800</td><td>7.74998400</td></tr><tr><td>(c)</td><td>0</td><td>-0.29004996</td><td>-2.80199750</td><td>0.97498700</td><td>-0.29750000</td></tr><tr><td></td><td>1</td><td>-0.56079734</td><td>-2.61592510</td><td>0.88573700</td><td>-0.48724000</td></tr><tr><td>(d)</td><td>0</td><td>0.86199480</td><td>0.15536240</td><td>0.06537475</td><td>0.01600323</td></tr><tr><td></td><td>1</td><td>0.95802009</td><td>0.23273957</td><td>0.08937959</td><td>0.01502024</td></tr><tr><td></td><td>2</td><td>1.09861230</td><td>0.33338433</td><td>0.11190995</td><td>0.00875797</td></tr></table>

9. The following tables show the approximations.

<table><tr><td>X</td><td>Approximation to f(x)</td><td>Actual f(x)</td><td>Error</td></tr><tr><td>(a) 8.4</td><td>17.877144</td><td>17.877146</td><td>1.6 × 10-6</td></tr><tr><td>(b) 0.9</td><td>0.4439248</td><td>0.44359244</td><td>3.323 × 10-4</td></tr><tr><td>（c） </td><td>0.17451852</td><td>0.17451852</td><td>0</td></tr><tr><td>(d) 0.25</td><td>-0.13277221</td><td>-0.13277189</td><td>3.19 × 10-7</td></tr></table>

<table><tr><td colspan="3">Approximation</td><td rowspan="2">Actual f(x)</td><td rowspan="2">Error</td></tr><tr><td></td><td>X</td><td>to f&#x27;(x)</td></tr><tr><td>a</td><td>8.4</td><td>3.128126</td><td>3.128232</td><td>1.90 × 10-5</td></tr><tr><td>b</td><td>0.9</td><td>2.204470</td><td>2.204367</td><td>1.0296 × 10-4</td></tr><tr><td>C</td><td>-</td><td>1.668000</td><td>1.668000</td><td>0</td></tr><tr><td>d</td><td>0.25</td><td>2.908242</td><td>2.907061</td><td>1.18057 × 10-3</td></tr></table>

10. The following tables show the approximations.

<table><tr><td>X</td><td>f(x)</td><td>s(x)</td><td>Error</td></tr><tr><td>(a) 0.43</td><td>2.363160694</td><td>2.362069472</td><td>0.001091222</td></tr><tr><td>(b) 0.0</td><td>1.000000000</td><td>1.132811750</td><td>0.132811750</td></tr><tr><td>（c） 0.18</td><td>-0.5081234644</td><td>-0.4443014992</td><td>0.0638219652</td></tr><tr><td>(d) 0.25</td><td>1.189069931</td><td>1.189089597</td><td>0.000019666</td></tr></table>

<table><tr><td>x</td><td>f&#x27;(x）</td><td>s&#x27;(x）)</td><td>Error</td></tr><tr><td>(a) 0.43</td><td>4.726321388</td><td>4.751927072</td><td>0.025605684</td></tr><tr><td>(b) 0.0</td><td>-1.000000000</td><td>-1.546872000</td><td>0.546872000</td></tr><tr><td>（c） 0.18</td><td>-2.651616829</td><td>-2.325976780</td><td>0.325640049</td></tr><tr><td>(d)</td><td>0.25 0.3909913152</td><td>0.3909814244</td><td>0.98908 × 10-5</td></tr></table>

11. $b = - 1$ , $c = - 3$ , $d = 1$

$^ { \ast } 1 2$ . $a = 4$ , $b = 4$ , $c = - 1$ , $\begin{array} { r } { d = \frac { 1 } { 3 } } \end{array}$

$^ *$ 13. $\begin{array} { r } { B = \frac { 1 } { 4 } } \end{array}$ , $\begin{array} { r } { D = \frac { 1 } { 4 } } \end{array}$ , $b = - \textstyle { \frac { 1 } { 2 } }$ , $\begin{array} { r } { d = \frac { 1 } { 4 } } \end{array}$

14. $f ^ { \prime } ( 0 ) = 0$ , $f ^ { \prime } ( 2 ) = 1 1$

15. The equation of the spline is

$$
S ( x ) = S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the coefficients are given in the following table.

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1.0</td><td>-0.7573593</td><td>0.0</td><td>-6.627417</td></tr><tr><td>0.25</td><td>0.7071068</td><td>-2.0</td><td>-4.970563</td><td>6.627417</td></tr><tr><td>0.5</td><td>0.0</td><td>-3.242641</td><td>0.0</td><td>6.627417</td></tr><tr><td>0.75</td><td>-0.7071068</td><td>-2.0</td><td>4.970563</td><td>-6.627417</td></tr></table>

We have $\int _ { 0 } ^ { 1 } S ( x ) d x = 0 . 0 0 0 0 0$ and $\int _ { 0 } ^ { 1 } \cos \pi x d x = 0$

Also, $S ^ { \prime } ( 0 . 5 ) = - 3 . 2 4 2 6 4$ and $f ^ { \prime } ( 0 . 5 ) = - \pi \sin ( 0 . 5 \pi ) = - \pi$ .

Finally $S ^ { \prime \prime } ( 0 . 5 ) = 0 . 0$ and $f ^ { \prime \prime } ( 0 . 5 ) = - \pi \cos ( 0 . 5 \pi ) = 0$ .

$^ { * } 1 6$ . Assume that the equation of the spline is

$$
S ( x ) = S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ .

The results are given in the following table.

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1.00000</td><td>-0.923601</td><td>0</td><td>0.620865</td></tr><tr><td>0.25</td><td>0.778801</td><td>-0.807189</td><td>0.465649</td><td>-0.154017</td></tr><tr><td>0.75</td><td>0.472367</td><td>-0.457052</td><td>0.234624</td><td>-0.312832</td></tr></table>

We have

$$
\int _ { 0 } ^ { 1 } S ( x ) d x = 0 . 6 3 1 9 6 7 , \quad S ^ { \prime } ( 0 . 5 ) = - 0 . 6 0 3 2 4 3 \quad \mathrm { a n d } \quad S ^ { \prime \prime } ( 0 . 5 ) = 0 . 7 0 0 2 7 4 .
$$

Also,

$$
\int _ { 0 } ^ { 1 } e ^ { - x } d x = 0 . 6 3 2 1 2 0 5 6 , \quad f ^ { \prime } ( 0 . 5 ) = - 0 . 6 0 6 5 3 0 7 , \quad \mathrm { a n d } \quad f ^ { \prime \prime } ( 0 . 5 ) = 0 . 6 0 6 5 3 0 7 .
$$

17. Assume that the equation of the spline is

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ .