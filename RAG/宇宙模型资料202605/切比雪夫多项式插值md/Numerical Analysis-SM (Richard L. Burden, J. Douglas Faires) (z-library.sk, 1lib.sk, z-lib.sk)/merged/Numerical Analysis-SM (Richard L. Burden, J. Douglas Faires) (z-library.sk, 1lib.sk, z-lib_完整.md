<!-- source: Numerical Analysis-SM (Richard L. Burden, J. Douglas Faires) (z-library.sk, 1lib.sk, z-lib.sk).pdf -->

<!-- pdf_type: normal; pages: 347; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-70 -->
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


<!-- chunk 0002: pages 71-140 -->
The coefficients are given in the following table.

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1</td><td>0</td><td>-5.193321</td><td>2.028118</td></tr><tr><td>0.25</td><td>0.7071068</td><td>-2.216388</td><td>-3.672233</td><td>4.896310</td></tr><tr><td>0.5</td><td>0</td><td>-3.134447</td><td>0</td><td>4.896310</td></tr><tr><td>0.75</td><td>-0.7071068</td><td>-2.216388</td><td>3.672233</td><td>2.028118</td></tr></table>

We have

$$
\int _ { 0 } ^ { 1 } s ( x ) d x = 0 . 0 0 0 0 0 0 , \quad s ^ { \prime } ( 0 . 5 ) = - 3 . 1 3 4 4 5 \quad { \mathrm { a n d } } \quad s ^ { \prime \prime } ( 0 . 5 ) = 0 . 0 0 0 0 0 0 .
$$

Also,

$$
\int _ { 0 } ^ { 1 } \cos \pi x d x = 0 , \quad f ^ { \prime } ( 0 . 5 ) = - \pi , \quad \mathrm { a n d } \quad f ^ { \prime \prime } ( 0 . 5 ) = 0 .
$$

18. Assume that the equation of the spline is

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$

The coefficients are given in the following table.

<table><tr><td>xi</td><td>ai</td><td>b</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1.00000</td><td>-1.00000</td><td>0.499440</td><td>-0.154515</td></tr><tr><td>0.25</td><td>0.778801</td><td>-0.779251</td><td>0.383555</td><td>-0.101580</td></tr><tr><td>0.75</td><td>0.472367</td><td>-0.471881</td><td>0.231185</td><td>-0.0618174</td></tr></table>

We have

$$
\int _ { 0 } ^ { 1 } s ( x ) d x = 0 . 6 2 3 0 7 8 , \quad s ^ { \prime } ( 0 . 5 ) = - 0 . 6 0 6 5 2 0 , \quad \mathrm { a n d } \quad s ^ { \prime \prime } ( 0 . 5 ) = 0 . 6 1 4 7 4 0 .
$$

Also,

$$
\int _ { 0 } ^ { 1 } e ^ { - x } d x = 0 . 6 3 2 1 2 0 5 , \quad f ^ { \prime } ( 0 . 5 ) = - 0 . 6 0 6 5 3 0 7 \quad \mathrm { a n d } \quad f ^ { \prime \prime } ( 0 . 5 ) = 0 . 6 0 6 5 3 0 7 .
$$

19. Let $f ( x ) = a + b x + c x ^ { 2 } + d x ^ { 3 }$ . Clearly, $f$ satisfies properties (a), (c), (d), and (e) of Definition 3.10, and $f$ interpolates itself for any choice of $x _ { 0 } , \ldots , x _ { n }$ . Since (ii) of property (f) in Definition 3.10 holds, $f$ must be its own clamped cubic spline. However, $f ^ { \prime \prime } ( x ) = 2 c + 6 d x$ can be zero only at $x = - c / 3 d$ . Thus, part (i) of property (f) in Definition 3.10 cannot hold at two values $x _ { 0 }$ and $x _ { n }$ . Thus, $f$ cannot be a natural cubic spline.

20. The free cubic spline must be the linear function $L ( x )$ through all the data $\{ x _ { i } , f ( x _ { i } ) \} _ { i = 1 } ^ { n }$ since $L ^ { \prime \prime } ( x ) = 0$ for all $x$ . So properties (a), (b), (c), (d), (e), (f), (i) of Definition 3.10 would be satisfied.

If $f$ is linear, then $f$ is its own clamped cubic spline. If, for example, $f$ satisfies $f ( 0 ) = 0$ $f ( 1 ) = 1$ , $f ( 2 ) = 2$ , $f ^ { \prime } ( 0 ) = 1$ , and $f ^ { \prime } ( 2 ) = 0$ , then the data lie on a straight line but the function $f$ is not linear. In that case the spline is

$$
\begin{array} { r } { s ( x ) = \left\{ \begin{array} { l l } { x - \frac { 1 } { 4 } x ^ { 2 } + \frac { 1 } { 4 } x ^ { 3 } , \quad 0 \leq x \leq 1 } \\ { 1 + \frac { 5 } { 4 } ( x - 1 ) + \frac { 1 } { 2 } ( x - 1 ) ^ { 2 } - \frac { 3 } { 4 } ( x - 1 ) ^ { 3 } , \quad 1 \leq x \leq 2 , } \end{array} \right. } \end{array}
$$

which is not a linear function.

21. The piecewise linear approximation to $f$ is given by

$$
F ( x ) = { \left\{ \begin{array} { l l } { 2 0 ( e ^ { 0 . 1 } - 1 ) x + 1 , } & { { \mathrm { f o r ~ } } x { \mathrm { ~ i n ~ } } [ 0 , 0 . 0 5 ] } \\ { 2 0 ( e ^ { 0 . 2 } - e ^ { 0 . 1 } ) x + 2 e ^ { 0 . 1 } - e ^ { 0 . 2 } , } & { { \mathrm { f o r ~ } } x { \mathrm { ~ i n ~ } } ( 0 . 0 5 , 1 ] . } \end{array} \right. }
$$

We have

$$
\int _ { 0 } ^ { 0 . 1 } F ( x ) \ d x = 0 . 1 1 0 7 9 3 6 \quad { \mathrm { ~ a n d ~ } } \int _ { 0 } ^ { 0 . 1 } f ( x ) \ d x = 0 . 1 1 0 7 0 1 4 .
$$

22. We have

$$
| f ( x ) - F ( x ) | \leq \frac { M } { 8 } \operatorname* { m a x } _ { 0 \leq j \leq n - 1 } | x _ { j + 1 } - x _ { j } | ^ { 2 } ,
$$

where $M = \mathrm { m a x } _ { a \leq x \leq b } | f ^ { \prime \prime } ( x ) |$ .

Error bounds for Exercise 21 are on $[ 0 , 0 . 1 ]$ , $| f ( x ) - F ( x ) | \leq 1 . 5 3 \times 1 0 ^ { - 3 }$ and

$$
\left| \int _ { 0 } ^ { 0 . 1 } F ( x ) \ d x - \int _ { 0 } ^ { 0 . 1 } e ^ { 2 x } \ d x \right| \leq 1 . 5 3 \times 1 0 ^ { - 4 } .
$$

$^ { * } 2 3$ . Insert the following before Step 7 in Algorithm 3.4 and Step 8 in Algorithm 3.5: For $j = 0 , 1 , \ldots , n - 1$ set

Set

$^ { * } 2 4$ . Before STEP 7 in Algorithm 3.4 and STEP 8 in Algorithm 3.5 insert the following:

Set $I = 0$ ; For $j = 0 , \ldots , n - 1$ set

$$
I = a _ { j } h _ { j } + \frac { b _ { j } } { 2 } h _ { j } ^ { 2 } + \frac { c _ { j } } { 3 } h _ { j } ^ { 3 } + \frac { d _ { j } } { 4 } h _ { j } ^ { 4 } + I . \left( A c c u m u l a t e \int _ { x _ { j } } ^ { x _ { j + 1 } } S ( x ) d x . \right)
$$

OUTPUT (I).

25. (a) On $[ 0 , 0 . 0 5 ]$ , we have $s ( x ) ~ = ~ 1 . 0 0 0 0 0 0 + 1 . 9 9 9 9 9 9 x + 1 . 9 9 8 3 0 2 x ^ { 2 } + 1 . 4 0 1 3 1 0 x ^ { 3 }$ , and on $( 0 . 0 5 , 0 . 1 ]$ , we have $s ( x ) = 1 . 1 0 5 1 7 0 + 2 . 2 1 0 3 4 0 ( x - 0 . 0 5 ) + 2 . 2 0 8 4 9 8 ( x - 0 . 0 5 ) ^ { 2 } +$ $1 . 5 4 8 7 5 8 ( x - 0 . 0 5 ) ^ { 3 }$ . (b) $\begin{array} { r } { \int _ { 0 } ^ { 0 . 1 } s ( x ) \ d x = 0 . 1 1 0 7 0 1 } \end{array}$ (c) $1 . 6 \times 1 0 ^ { - 7 }$ (d) On $[ 0 , 0 . 0 5 ]$ , we have $S ( x ) = 1 + 2 . 0 4 8 1 1 x + 2 2 . 1 2 1 8 4 x ^ { 3 }$ , and on (0.05, 0.1], we have $S ( x ) = 1 . 1 0 5 1 7 1 + 2 . 2 1 4 0 2 8 ( x - 0 . 0 5 ) + 3 . 3 1 8 2 7 7 ( x - 0 . 0 5 ) ^ { 2 } - 2 2 . 1 2 1 8 4 ( x - 0 . 0 5 ) ^ { 3 }$ . $S ( 0 . 0 2 ) =$ 1.041139 and $S ( 0 . 0 2 ) = 1 . 0 4 0 8 1 1$ .

26. The five equations are

$$
a _ { 0 } = f ( x _ { 0 } ) , \quad a _ { 1 } = f ( x _ { 1 } ) , \quad a _ { 1 } + b _ { 1 } ( x _ { 2 } - x _ { 1 } ) + c _ { 1 } ( x _ { 2 } - x _ { 1 } ) ^ { 2 } = f ( x _ { 2 } ) .
$$

$$
a _ { 0 } + b _ { 0 } ( x _ { 1 } - x _ { 0 } ) + c _ { 0 } ( x _ { 1 } - x _ { 0 } ) ^ { 2 } = a _ { 1 } , \quad \mathrm { a n d } \quad b _ { 0 } + 2 c _ { 0 } ( x _ { 1 } - x _ { 0 } ) = b _ { 1 } .
$$

If $S \in C ^ { 2 }$ , then $S$ is a quadratic on $[ x _ { 0 } , x _ { 2 } ]$ and the solution may not be meaningful.

27. We have

$$
S ( x ) = \left\{ \begin{array} { l l } { 2 x - x ^ { 2 } , } & { 0 \leq x \leq 1 } \\ { 1 + ( x - 1 ) ^ { 2 } , } & { 1 \leq x \leq 2 } \end{array} \right.
$$

28. (a)

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>1950</td><td>151326</td><td>2906.50</td><td>0.00000</td><td>-1.06802</td></tr><tr><td>1960</td><td>179323</td><td>2586.10</td><td>-32.0407</td><td>1.32212</td></tr><tr><td>1970</td><td>203302</td><td>2341.92</td><td>7.62287</td><td>-0.94145</td></tr><tr><td>1980</td><td>226542</td><td>2211.94</td><td>-20.6208</td><td>3.03370</td></tr><tr><td>2000</td><td>249633</td><td>2709.63</td><td>70.3902</td><td>-2.34634</td></tr></table>

$S ( 1 9 4 0 ) = 1 2 3 , 3 2 9$ , $S ( 1 9 7 5 ) = 2 1 5 , 0 8 4$ , and $S ( 2 0 1 0 ) = 3 3 0 , 9 2 2$ .

(b) This is much better than using Lagrange interpolation, but still probably not very accurate.

29. The spline has the equation

$$
s ( x ) = s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the coefficients are given in the following table.

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>0</td><td>75</td><td>-0.659292</td><td>0.219764</td></tr><tr><td>3</td><td>225</td><td>76.9779</td><td>1.31858</td><td>-0.153761</td></tr><tr><td>5</td><td>383</td><td>80.4071</td><td>0.396018</td><td>-0.177237</td></tr><tr><td>8</td><td>623</td><td>77.9978</td><td>-1.19912</td><td>0.0799115</td></tr></table>

The spline predicts a position of $s ( 1 0 ) = 7 7 4 . 8 4$ ft and a speed of $s ^ { \prime } ( 1 0 ) \ = \ 7 4 . 1 6 \ \mathrm { f t / s }$ s. To maximize the speed, we find the single critical point of $s ^ { \prime } ( x )$ , and compare the values of $s ( x )$ at this point and the endpoints. We find that max $s ^ { \prime } ( x ) = s ^ { \prime } ( 5 . 7 4 4 8 ) = 8 0 . 7 ~ \mathrm { f t / s } = 5 5 $ mi/h. The speed 55 mi/h was first exceeded at approximately 5.5 s.

30. (a) We have

The coefficients of the spline are given in the following table.

<table><tr><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0.00000000</td><td>0.01100783</td><td>0.00000000</td><td>-0.00000024</td></tr><tr><td>0.25000000</td><td>0.01062142</td><td>-0.00001681</td><td>0.00000016</td></tr><tr><td>0.50000000</td><td>0.01009276</td><td>-0.00000499</td><td>0.00000004</td></tr><tr><td>1.00000000</td><td>0.00990986</td><td>0.00000135</td><td>-0.00000002</td></tr></table>

This gives

$s _ { 0 } ( t ) = 0 . 0 1 1 0 0 7 8 3 t - 0 . 0 0 0 0 0 0 2 4 t ^ { 3 }$ , $s _ { 1 } ( t ) = 0 . 5 0 + 0 . 0 1 0 6 2 1 4 2 ( t - 4 7 . 2 3 ) - 0 . 0 0 0 0 1 6 8 1 ( t - 4 7 . 2 3 ) ^ { 2 } + 0 . 0 0 0 0 0 0 1 6 ( t - 4 7 . 2 3 ) ^ { 3 }$ , $s _ { 2 } ( t ) = 1 . 0 0 + 0 . 0 0 9 9 0 9 8 6 ( t - 9 7 . 4 9 ) + 0 . 0 0 0 0 0$ $\mathrm { . 0 0 0 0 0 1 3 5 ( } t - 9 7 . 4 9 ) ^ { 2 } - 0 . 0 0 0 0 0 0 0 2 ( t - 9 7 . 4 9 ) ^ { 3 }$ .

(b) The predicted time at the three-quarter mile pole is $1 : 1 2 . 2 5$ , which compares well with the actual time of $1 : 1 2 : 0 9$ .

(c) The starting speed is predicted to be $3 9 . 6 3 \ \mathrm { m i / h }$ and the speed at the finish line is predicted to be $3 5 . 7 8 \ \mathrm { m i / h }$ .

31. The equation of the spline is

$$
S ( x ) = S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the coefficients are given in the following table.

Sample 1   
Sample 2   

<table><tr><td>Xi</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td><td>ai</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>6.67</td><td>-0.44687</td><td>0</td><td>0.06176</td><td>6.67</td><td>1.6629</td><td>0</td><td>-0.00249</td></tr><tr><td>6</td><td>17.33</td><td>6.2237</td><td>1.1118</td><td>-0.27099</td><td>16.11</td><td>1.3943</td><td>-0.04477</td><td>-0.03251</td></tr><tr><td>10</td><td>42.67</td><td>2.1104</td><td>-2.1401</td><td>0.28109</td><td>18.89</td><td>-0.52442</td><td>-0.43490</td><td>0.05916</td></tr><tr><td>13</td><td>37.33</td><td>-3.1406</td><td>0.38974</td><td>-0.01411</td><td>15.00</td><td>-1.5365</td><td>0.09756</td><td>0.00226</td></tr><tr><td>17</td><td>30.10</td><td>-0.70021</td><td>0.22036</td><td>-0.02491</td><td>10.56</td><td>-0.64732</td><td>0.12473</td><td>-0.01113</td></tr><tr><td>20</td><td>29.31</td><td>-0.05069</td><td>-0.00386</td><td>0.00016</td><td>9.44</td><td>-0.19955</td><td>0.02453</td><td>-0.00102</td></tr></table>

$^ { * } 3 2$ . The three clamped splines have equations of the form

$$
s _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the values of the coefficients are given in the following tables.

Spline 1   

<table><tr><td>i</td><td>Xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td><td>f&#x27;(xi)</td></tr><tr><td>0</td><td>1</td><td>3.0</td><td>1.0</td><td>-0.347</td><td>-0.049</td><td>1.0</td></tr><tr><td>1</td><td>2</td><td>3.7</td><td>0.447</td><td>-0.206</td><td>0.027</td><td></td></tr><tr><td>2</td><td>5</td><td>3.9</td><td>-0.074</td><td>0.033</td><td>0.342</td><td></td></tr><tr><td>3</td><td>6</td><td>4.2</td><td>1.016</td><td>1.058</td><td>-0.575</td><td></td></tr><tr><td>4</td><td>7</td><td>5.7</td><td>1.409</td><td>-0.665</td><td>0.156</td><td></td></tr><tr><td>5</td><td>8</td><td>6.6</td><td>0.547</td><td>-0.196</td><td>0.024</td><td></td></tr><tr><td>6</td><td>10</td><td>7.1</td><td>0.048</td><td>-0.053</td><td>-0.003</td><td></td></tr><tr><td>7</td><td>13</td><td>6.7</td><td>-0.339</td><td>-0.076</td><td>0.006</td><td></td></tr><tr><td>8</td><td>17</td><td>4.5</td><td></td><td></td><td></td><td>-0.67</td></tr></table>

Spline 2   

<table><tr><td>i</td><td>xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td><td>f&#x27;(xi)</td></tr><tr><td>0</td><td>17</td><td>4.5</td><td>3.0</td><td>-1.101</td><td>-0.126</td><td>3.0</td></tr><tr><td>1</td><td>20</td><td>7.0</td><td>-0.198</td><td>0.035</td><td>-0.023</td><td></td></tr><tr><td>2</td><td>23</td><td>6.1</td><td>-0.609</td><td>-0.172</td><td>0.280</td><td></td></tr><tr><td>3</td><td>24</td><td>5.6</td><td>-0.111</td><td>0.669</td><td>-0.357</td><td></td></tr><tr><td>4</td><td>25</td><td>5.8</td><td>0.154</td><td>-0.403</td><td>0.088</td><td></td></tr><tr><td>5</td><td>27</td><td>5.2</td><td>-0.401</td><td>0.126</td><td>-2.568</td><td></td></tr><tr><td>6</td><td>27.7</td><td>4.1</td><td></td><td></td><td></td><td>-4.0</td></tr></table>

Spline 3   

<table><tr><td>i</td><td>Xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td><td>f&#x27;(xi)</td></tr><tr><td>0</td><td>27.7</td><td>4.1</td><td>0.330</td><td>2.262</td><td>-3.800</td><td>0.33</td></tr><tr><td>1</td><td>28</td><td>4.3</td><td>0.661</td><td>-1.157</td><td>0.296</td><td></td></tr><tr><td>2</td><td>29</td><td>4.1</td><td>-0.765</td><td>-0.269</td><td>-0.065</td><td></td></tr><tr><td>3</td><td>30</td><td>3.0</td><td></td><td></td><td></td><td>-1.5</td></tr></table>

33. The three natural splines have equations of the form

$$
S _ { i } ( x ) = a _ { i } + b _ { i } ( x - x _ { i } ) + c _ { i } ( x - x _ { i } ) ^ { 2 } + d _ { i } ( x - x _ { i } ) ^ { 3 } ,
$$

for $x$ in $[ x _ { i } , x _ { i + 1 } ]$ , where the values of the coefficients are given in the following tables.

Spline 1   

<table><tr><td>i</td><td>xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>1</td><td>3.0</td><td>0.786</td><td>0.0</td><td>-0.086</td></tr><tr><td>1</td><td>2</td><td>3.7</td><td>0.529</td><td>-0.257</td><td>0.034</td></tr><tr><td>2</td><td>5</td><td>3.9</td><td>-0.086</td><td>0.052</td><td>0.334</td></tr><tr><td>3</td><td>6</td><td>4.2</td><td>1.019</td><td>1.053</td><td>-0.572</td></tr><tr><td>4</td><td>7</td><td>5.7</td><td>1.408</td><td>-0.664</td><td>0.156</td></tr><tr><td>5</td><td>8</td><td>6.6</td><td>0.547</td><td>-0.197</td><td>0.024</td></tr><tr><td>6</td><td>10</td><td>7.1</td><td>0.049</td><td>-0.052</td><td>-0.003</td></tr><tr><td>7</td><td>13</td><td>6.7</td><td>-0.342</td><td>-0.078</td><td>0.007</td></tr><tr><td>8</td><td>17</td><td>4.5</td><td></td><td></td><td></td></tr></table>

Spline 2   

<table><tr><td>i</td><td>xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>17</td><td>4.5</td><td>1.106</td><td>0.0</td><td>-0.030</td></tr><tr><td>1</td><td>20</td><td>7.0</td><td>0.289</td><td>-0.272</td><td>0.025</td></tr><tr><td>2</td><td>23</td><td>6.1</td><td>-0.660</td><td>-0.044</td><td>0.204</td></tr><tr><td>3</td><td>24</td><td>5.6</td><td>-0.137</td><td>0.567</td><td>-0.230</td></tr><tr><td>4</td><td>25</td><td>5.8</td><td>0.306</td><td>-0.124</td><td>-0.089</td></tr><tr><td>5</td><td>27</td><td>5.2</td><td>-1.263</td><td>-0.660</td><td>0.314</td></tr><tr><td>6</td><td>27.7</td><td>4.1</td><td></td><td></td><td></td></tr></table>

Spline 3   

<table><tr><td>i</td><td>Xi</td><td>ai=f(xi)</td><td>bi</td><td>Ci</td><td>di</td></tr><tr><td>0</td><td>27.7</td><td>4.1</td><td>0.749</td><td>0.0</td><td>-0.910</td></tr><tr><td>1</td><td>28</td><td>4.3</td><td>0.503</td><td>-0.819</td><td>0.116</td></tr><tr><td>2</td><td>29</td><td>4.1</td><td>-0.787</td><td>-0.470</td><td>0.157</td></tr><tr><td>3</td><td>30</td><td>3.0</td><td></td><td></td><td></td></tr></table>

# Exercise Set 3.6, page 170

1. The parametric cubic Hermite approximations are as follows.

$$
\begin{array} { l } { x ( t ) = - 1 0 t ^ { 3 } + 1 4 t ^ { 2 } + t , y ( t ) = - 2 t ^ { 3 } + 3 t ^ { 2 } + t } \\ { x ( t ) = - 1 0 t ^ { 3 } + 1 4 . 5 t ^ { 2 } + 0 . 5 t , y ( t ) = - 3 t ^ { 3 } + 4 . 5 t ^ { 2 } + 0 . 5 t } \\ { x ( t ) = - 1 0 t ^ { 3 } + 1 4 t ^ { 2 } + t , y ( t ) = - 4 t ^ { 3 } + 5 t ^ { 2 } + t } \\ { x ( t ) = - 1 0 t ^ { 3 } + 1 3 t ^ { 2 } + 2 t , y ( t ) = 2 t } \end{array}
$$

2. The parametric cubic B´ezier approximations are as follows.

$$
\begin{array} { r l } & { x ( t ) = - 1 0 t ^ { 3 } + 1 2 t ^ { 2 } + 3 t , \quad y ( t ) = 2 t ^ { 3 } - 3 t ^ { 2 } + 3 t } \\ & { x ( t ) = - 1 0 t ^ { 3 } + 1 3 . 5 t ^ { 2 } + 1 . 5 t , \quad y ( t ) = - t ^ { 3 } + 1 . 5 t ^ { 2 } + 1 . 5 t } \\ & { x ( t ) = - 1 0 t ^ { 3 } + 1 2 t ^ { 2 } + 3 t , \quad y ( t ) = - 4 t ^ { 3 } + 3 t ^ { 2 } + 3 t } \\ & { x ( t ) = - 1 0 t ^ { 3 } + 9 t ^ { 2 } + 6 t , \quad y ( t ) = 8 t ^ { 3 } - 1 2 t ^ { 2 } + 6 t } \end{array}
$$

3. The parametric cubic B´ezier approximations are as follows.

(a) $\begin{array} { l } { x ( t ) = - 1 1 . 5 t ^ { 3 } + 1 5 t ^ { 2 } + 1 . 5 t + 1 , y ( t ) = - 4 . 2 5 t ^ { 3 } + 4 . 5 t ^ { 2 } + 0 . 7 5 t + 1 } \\ { x ( t ) = - 6 . 2 5 t ^ { 3 } + 1 0 . 5 t ^ { 2 } + 0 . 7 5 t + 1 , y ( t ) = - 3 . 5 t ^ { 3 } + 3 t ^ { 2 } + 1 . 5 t + 1 } \end{array}$   
(b)   
(c) For $t$ between $( 0 , 0 )$ and $( 4 , 6 )$ , we have

$$
x ( t ) = - 5 t ^ { 3 } + 7 . 5 t ^ { 2 } + 1 . 5 t , y ( t ) = - 1 3 . 5 t ^ { 3 } + 1 8 t ^ { 2 } + 1 . 5 t ,
$$

and for $t$ between $( 4 , 6 )$ and $( 6 , 1 )$ , we have

$$
x ( t ) = - 5 . 5 t ^ { 3 } + 6 t ^ { 2 } + 1 . 5 t + 4 , y ( t ) = 4 t ^ { 3 } - 6 t ^ { 2 } - 3 t + 6 .
$$

(d) For $t$ between $( 0 , 0 )$ and $( 2 , 1 )$ , we have

$$
\begin{array} { r } { x ( t ) = - 5 . 5 t ^ { 3 } + 6 t ^ { 2 } + 1 . 5 t , y ( t ) = - 0 . 5 t ^ { 3 } + 1 . 5 t , } \end{array}
$$

for $t$ between $( 2 , 1 )$ and $( 4 , 0 )$ , we have

$$
x ( t ) = - 4 t ^ { 3 } + 3 t ^ { 2 } + 3 t + 2 , \quad y ( t ) = - t ^ { 3 } + 1 ,
$$

and for $t$ between $( 4 , 0 )$ and $( 6 , - 1 )$ , we have

$$
x ( t ) = - 8 . 5 t ^ { 3 } + 1 3 . 5 t ^ { 2 } - 3 t + 4 , y ( t ) = - 3 . 2 5 t ^ { 3 } + 5 . 2 5 t ^ { 2 } - 3 t .
$$

4. Between $( 3 , 6 )$ and $( 2 , 2 )$ , we have

$$
x ( t ) = 0 . 5 t ^ { 3 } - 2 . 4 t ^ { 2 } + 0 . 9 t + 3 , y ( t ) = 6 . 5 t ^ { 3 } - 1 2 t ^ { 2 } + 1 . 5 t + 6 ;
$$

between $( 2 , 2 )$ and $( 6 , 6 )$ , we have

$$
x ( t ) = - 5 . 9 t ^ { 3 } + 8 . 4 t ^ { 2 } + 1 . 5 t + 2 , y ( t ) = - 3 . 5 t ^ { 3 } + 6 t ^ { 2 } + 1 . 5 t + 2 ;
$$

between $( 6 , 6 )$ and $( 5 , 2 )$ , we have

$$
x ( t ) = - 2 . 5 t ^ { 3 } + 4 . 5 t ^ { 2 } - 3 t + 6 , y ( t ) = 6 . 8 t ^ { 3 } - 1 0 . 2 t ^ { 2 } - 0 . 6 t + 6 ;
$$

and between $( 5 , 2 )$ and $( 6 . 5 , 3 )$ , we have

$$
x ( t ) = - 4 . 2 t ^ { 3 } + 7 . 2 t ^ { 2 } - 1 . 5 t + 5 , y ( t ) = 0 . 1 t ^ { 3 } - 0 . 6 t ^ { 2 } + 1 . 5 t + 2 .
$$

\*5. (a) Using the forward divided difference gives the following table.

<table><tr><td>0</td><td>uo</td><td></td><td></td></tr><tr><td>0</td><td>uo</td><td>3(u1-uo)</td><td></td></tr><tr><td>1</td><td>u3</td><td>u3-uo</td><td>U3 -3u1+ 2uo</td></tr><tr><td>1</td><td>u3</td><td>3(u3-u2)</td><td>2u3-3u2+uo u3-3u2+3u1-uo</td></tr></table>

Therefore,

$$
\begin{array} { r l r } {  { u ( t ) = u _ { 0 } + 3 ( u _ { 1 } - u _ { 0 } ) t + ( u _ { 3 } - 3 u _ { 1 } + 2 u _ { 0 } ) t ^ { 2 } + ( u _ { 3 } - 3 u _ { 2 } + 3 u _ { 1 } - u _ { 0 } ) t ^ { 2 } ( t - 1 ) } } \\ & { } & \\ & { } & { \quad = u _ { 0 } + 3 ( u _ { 1 } - u _ { 0 } ) t + ( - 6 u _ { 1 } + 3 u _ { 0 } + 3 u _ { 2 } ) t ^ { 2 } + ( u _ { 3 } - 3 u _ { 2 } + 3 u _ { 1 } - u _ { 0 } ) t ^ { 3 } . \quad } \end{array}
$$

Similarly, $v ( t ) = v _ { 0 } + 3 ( v _ { 1 } - v _ { 0 } ) t + ( 3 v _ { 2 } - 6 v _ { 1 } + 3 v _ { 0 } ) t ^ { 2 } + ( v _ { 3 } - 3 v _ { 2 } + 3 v _ { 1 } - v _ { 0 } ) t ^ { 3 } .$

(b) Using the formula for Bernstein polynomials gives, for $f$ ,

$$
\begin{array} { c } { { \displaystyle \sum _ { k = 0 } ^ { 3 } \binom { 3 } { k } u _ { k } t ^ { k } ( 1 - t ) ^ { 3 - k } = u _ { 0 } ( 1 - t ) ^ { 3 } + 3 u _ { 1 } t ( 1 - t ) ^ { 2 } + 3 u _ { 2 } t ^ { 2 } ( 1 - t ) + u _ { 3 } t ^ { 3 } } } \\ { { { } } } \\ { { = u _ { 0 } + 3 ( u _ { 1 } - u _ { 0 } ) t + ( 3 u _ { 2 } - 6 u _ { 1 } + 3 u _ { 0 } ) t ^ { 2 } + ( u _ { 3 } - 3 u _ { 2 } + 3 u _ { 1 } - u _ { 0 } ) t ^ { 3 } } } \\ { { { } } } \\ { { = u ( t ) } } \end{array}
$$

and, for $g$

$$
\begin{array} { r l } { \displaystyle \sum _ { k = 0 } ^ { 3 } \binom { 3 } { k } v _ { k } t ^ { k } ( 1 - t ) ^ { 3 - k } = v _ { 0 } ( 1 - t ) ^ { 3 } + 3 v _ { 1 } t ( 1 - t ) ^ { 2 } + 3 v _ { 2 } t ^ { 2 } ( 1 - t ) + v _ { 3 } t ^ { 3 } } & { } \\ { = v _ { 0 } + 3 ( v _ { 1 } - v _ { 0 } ) t + ( 3 v _ { 2 } - 6 v _ { 1 } + 3 v _ { 0 } ) t ^ { 2 } + ( v _ { 3 } - 3 v _ { 2 } + 3 v _ { 1 } - v _ { 0 } ) t ^ { 3 } } & { } \\ { = v ( t ) . } \end{array}
$$

# Numerical Differentiation and Integration

Exercise Set 4.1, page 182

1. From the forward-backward difference formula (4.1), we have the following approximations:

(a) $f ^ { \prime } ( 0 . 5 ) \approx 0 . 8 5 2 0$ , $f ^ { \prime } ( 0 . 6 ) \approx 0 . 8 5 2 0$ , $f ^ { \prime } ( 0 . 7 ) \approx 0 . 7 9 6 0$ (b) $f ^ { \prime } ( 0 . 0 ) \approx 3 . 7 0 7 0$ , $f ^ { \prime } ( 0 . 2 ) \approx 3 . 1 5 2 0$ , $f ^ { \prime } ( 0 . 4 ) \approx 3 . 1 5 2 0$

2. The approximations are in the following tables

<table><tr><td colspan="2">*(a) x</td><td>f(x)</td><td>f&#x27;（x）</td></tr><tr><td colspan="2"></td><td></td><td></td></tr><tr><td colspan="2">1 0.3 -0.2</td><td>1.9507 2.0421</td><td>0.9140 0.1800</td></tr><tr><td colspan="2">-0.1</td><td>2.0601</td><td>0.1800</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td colspan="3"></td></tr><tr><td>X</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>1.0</td><td>1.0000</td><td>1.3125</td></tr><tr><td>1.2</td><td>1.2625</td><td>1.3125</td></tr><tr><td>1.4</td><td>1.6595</td><td>1.9850</td></tr></table>

3. The approximations are in the following tables.

<table><tr><td rowspan="7">(a)</td><td></td></tr><tr><td>x Actual Error</td><td>Error] Bound</td></tr><tr><td>0.5 0.0255</td><td>0.0282</td></tr><tr><td>0.6 0.0267</td><td>0.0282</td></tr><tr><td>0.7 0.0312</td><td>0.0322</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2"></td></tr><tr><td rowspan="2"></td><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>0.0</td><td>0.2930</td><td>0.3000</td></tr><tr><td></td><td>0.2</td><td>0.2694</td><td>0.2779</td></tr><tr><td></td><td>0.4</td><td>0.2602</td><td>0.2779</td></tr></table>

4. (a)

<table><tr><td>X Actual Error</td><td></td><td>Error Bound</td></tr><tr><td>-0.3</td><td>0.34457</td><td>0.36842</td></tr><tr><td>-0.2</td><td>0.35633</td><td>0.36842</td></tr><tr><td>-0.1</td><td>0.38533</td><td>0.39203</td></tr></table>

<table><tr><td>X</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>1.0</td><td>0.31250</td><td>0.33646</td></tr><tr><td>1.2</td><td>0.32507</td><td>0.33646</td></tr><tr><td>1.4</td><td>0.35712</td><td>0.36729</td></tr></table>

5. For the endpoints of the tables, we use Formula (4.4). The other approximations come from Formula (4.5).

\*(a) $f ^ { \prime } ( 1 . 1 ) \approx 1 7 . 7 6 9 7 0 5$ , $f ^ { \prime } ( 1 . 2 ) \approx 2 2 . 1 9 3 6 3 5$ , $f ^ { \prime } ( 1 . 3 ) \approx 2 7 . 1 0 7 3 5 0$ , $f ^ { \prime } ( 1 . 4 ) \approx 3 2 . 1 5 0 8 5 0$ (b) $f ^ { \prime } ( 8 . 1 ) \approx 3 . 0 9 2 0 5 0$ , $f ^ { \prime } ( 8 . 3 ) \approx 3 . 1 1 6 1 5 0$ , $f ^ { \prime } ( 8 . 5 ) \approx 3 . 1 3 9 9 7 5$ , $f ^ { \prime } ( 8 . 7 ) \approx 3 . 1 6 3 5 2 5$ (c) $f ^ { \prime } ( 2 . 9 ) \approx 5 . 1 0 1 3 7 5$ , $f ^ { \prime } ( 3 . 0 ) \approx 6 . 6 5 4 7 8 5$ , $f ^ { \prime } ( 3 . 1 ) \approx 8 . 2 1 6 3 3 0$ , $f ^ { \prime } ( 3 . 2 ) \approx 9 . 7 8 6 0 1 0$ (d) $f ^ { \prime } ( 2 . 0 ) \approx 0 . 1 3 5 3 3 1 5 0 , f ^ { \prime } ( 2 . 1 ) \approx - 0 . 0 9 9 8 9 5 5 0 , f ^ { \prime } ( 2 . 2 ) \approx - 0 . 3 2 9 8 9 6 0 , f ^ { \prime } ( 2 . 3 ) \approx - 0 . 5 5 4 6 7 0 0 9 6 0 , f ^ { \prime } ( 2 . 3 ) \approx - 0 . 1 9 5 3 6 7 0 2 4 , f ^ { \prime } ( 2 . 3 ) \approx - 0 . 3 2 5 3 3 8 9 6 0 0 , f ^ { \prime } ( 2 . 3 )$

6. For the endpoints of the tables, we use Formula (4.4). The other approximations come from Formula (4.5).

<table><tr><td rowspan="3">(a)</td><td colspan="3"></td></tr><tr><td>x</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>- 0.3</td><td>-0.27652</td><td>-0.06030</td></tr><tr><td rowspan="2">-0.2</td><td></td><td></td><td>0.57590</td></tr><tr><td>-0.1</td><td>-0.25074 -0.16134</td><td>1.25370</td></tr><tr><td rowspan="2"></td><td>0.0</td><td>0.0</td><td>1.97310</td></tr><tr><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td colspan="3"></td></tr><tr><td>x</td><td>f(x)</td><td>f&#x27;(xc)</td></tr><tr><td>7.4</td><td>-68.3193</td><td>-16.6933</td></tr><tr><td>7.6</td><td>-71.6982</td><td>-17.0958</td></tr><tr><td>7.8</td><td>-75.1576</td><td>-17.4980</td></tr><tr><td>8.0</td><td>-78.6974</td><td>-17.9000</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3"></td></tr><tr><td>C</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>1.1</td><td>1.52918</td><td>1.34360</td></tr><tr><td>1.2</td><td>1.64024</td><td>0.87760</td></tr><tr><td>1.3</td><td>1.70470</td><td>0.36265</td></tr><tr><td>1.4</td><td>1.71277</td><td>-0.20125</td></tr></table>

<table><tr><td colspan="2">(d)</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td>f(x)</td><td>f&#x27;(xc)</td></tr><tr><td colspan="2">-2.7</td><td>0.054797</td><td>-0.915178</td></tr><tr><td colspan="2">-2.5</td><td>0.11342</td><td>1.50141</td></tr><tr><td colspan="2">-2.3</td><td>0.65536</td><td>2.17825</td></tr><tr><td colspan="2">-2.1</td><td>0.98472</td><td>1.11535</td></tr></table>

7. The errors and error bounds are given in the following tables.

<table><tr><td colspan="2">*（a)</td><td colspan="2"></td></tr><tr><td colspan="2">x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td colspan="2">1.1</td><td>0.280322</td><td>0.359033</td></tr><tr><td colspan="2">1.2</td><td>0.147282</td><td>0.179517</td></tr><tr><td colspan="2">1.3</td><td>0.179874</td><td>0.219262</td></tr><tr><td colspan="2">1.4</td><td>0.378444</td><td>0.438524</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2"></td></tr><tr><td rowspan="2"></td><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>8.1</td><td>0.00018594</td><td>0.000020322</td></tr><tr><td></td><td>8.3</td><td>0.00010551</td><td>0.000010161</td></tr><tr><td></td><td>8.5</td><td>9.116 × 10-5</td><td>0.000009677</td></tr><tr><td></td><td>8.7</td><td>0.00020197</td><td>0.000019355</td></tr></table>

<table><tr><td colspan="2">(c) x</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td>Actual Error</td><td>Error Bound</td></tr><tr><td colspan="2">2.9</td><td>0.011956</td><td>0.0180988</td></tr><tr><td colspan="2">3.0</td><td>0.0049251</td><td>0.00904938</td></tr><tr><td colspan="2">3.1</td><td>0.0004765</td><td>0.00493920</td></tr><tr><td colspan="2">3.2</td><td>0.0013745</td><td>0.00987840</td></tr></table>

<table><tr><td colspan="2">(d)</td><td colspan="2"></td></tr><tr><td colspan="2">X</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td colspan="2">2.0</td><td>0.00252235</td><td>0.00410304</td></tr><tr><td colspan="2">2.1</td><td>0.00142882</td><td>0.00205152</td></tr><tr><td colspan="2">2.2</td><td>0.00204851</td><td>0.00260034</td></tr><tr><td colspan="2">2.3</td><td>0.00437954</td><td>0.00520068</td></tr></table>

8. The errors and error bounds are given in the following tables.

<table><tr><td colspan="3">(a) Error Bound</td></tr><tr><td colspan="3">x Actual Error</td></tr><tr><td></td><td></td><td></td></tr><tr><td>- 0.3</td><td>0.028638</td><td>0.029692</td></tr><tr><td>-0.2</td><td>0.014097</td><td>0.014846</td></tr><tr><td>-0.1</td><td>0.013577</td><td>0.014130</td></tr><tr><td>0.0</td><td>0.026900</td><td>0.028260</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>7.4</td><td></td><td>0.000032</td></tr><tr><td>7.6</td><td>0.000367 0.000083</td><td>0.000016</td></tr><tr><td>7.8</td><td>0.000041</td><td>0.000015</td></tr><tr><td></td><td></td><td></td></tr><tr><td>8.0</td><td>0.000000</td><td>0.000030</td></tr></table>

<table><tr><td rowspan="3">(c)</td><td colspan="3"></td></tr><tr><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>1.1</td><td>0.033886</td><td>0.034784</td></tr><tr><td>1.2</td><td></td><td>0.016791</td><td>0.017392</td></tr><tr><td></td><td>1.3</td><td>0.015740</td><td>0.016817</td></tr><tr><td></td><td>1.4</td><td>0.030920</td><td>0.033633</td></tr></table>

<table><tr><td colspan="4"></td></tr><tr><td></td><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td rowspan="5"></td><td>-2.7</td><td>0.511122</td><td>1.440958</td></tr><tr><td>-2.5</td><td>0.435980</td><td>0.720479</td></tr><tr><td>-2.3</td><td>0.632733</td><td>0.720479</td></tr><tr><td>-2.1</td><td>1.044472</td><td></td></tr><tr><td></td><td></td><td>1.440958</td></tr></table>

9. The approximations and the formulas used are:

(a) $f ^ { \prime } ( 2 . 1 ) \approx 3 . 8 9 9 3 4 4$ from (4.7) $f ^ { \prime } ( 2 . 2 ) \approx 2 . 8 7 6 8 7 6$ from (4.7) $f ^ { \prime } ( 2 . 3 ) \approx 2 . 2 4 9 7 0 4$ from (4.6) $f ^ { \prime } ( 2 . 4 ) \approx 1 . 8 3 7 7 5 6$ from (4.6) $f ^ { \prime } ( 2 . 5 ) \approx 1 . 5 4 4 2 1 0$ from (4.7) $f ^ { \prime } ( 2 . 6 ) \approx 1 . 3 5 5 4 9 6$ from (4.7)

(b) $f ^ { \prime } ( - 3 . 0 ) \approx - 5 . 8 7 7 3 5 8$ from (4.7) $f ^ { \prime } ( - 2 . 8 ) \approx - 5 . 4 6 8 9 3 3$ from (4.7) $f ^ { \prime } ( - 2 . 6 ) \approx - 5 . 0 5 9 8 8 4$ from (4.6) $f ^ { \prime } ( - 2 . 4 ) \approx - 4 . 6 5 0 2 2 3$ from (4.6) $f ^ { \prime } ( - 2 . 2 ) \approx - 4 . 2 3 9 9 1 1$ from (4.7) $f ^ { \prime } ( - 2 . 0 ) \approx - 3 . 8 2 8 8 5 3$ from (4.7)

10. The approximations are in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>x</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>1.05</td><td>-1.709847</td><td>7.798690</td></tr><tr><td>1.10</td><td>-1.373823</td><td>5.753747</td></tr><tr><td>1.15</td><td>-1.119214</td><td>4.499409</td></tr><tr><td>1.20</td><td>-0.9160143</td><td>3.675512</td></tr><tr><td>1.25</td><td>-0.7470223</td><td>3.088414</td></tr><tr><td>1.30</td><td>-0.6015966</td><td>2.710997</td></tr></table>

<table><tr><td rowspan="15"></td><td></td><td></td><td></td></tr><tr><td>x</td><td>f(x)</td><td>f&#x27;(x)</td></tr><tr><td>-3.0</td><td>16.08554</td><td>-19.08087</td></tr><tr><td>-2.8</td><td>12.64465</td><td>-15.44088</td></tr><tr><td>-2.6</td><td>9.863738</td><td>-12.46303</td></tr><tr><td>-2.4</td><td>7.623176</td><td>-10.02259</td></tr><tr><td>-2.2</td><td>5.825013</td><td>-8.02097</td></tr><tr><td>-2.0</td><td>4.389056</td><td>-6.38573</td></tr></table>

11. The approximations are in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>2.1</td><td>0.0242312</td><td>0.109271</td></tr><tr><td>2.2</td><td>0.0105138</td><td>0.0386885</td></tr><tr><td>2.3</td><td>0.0029352</td><td>0.0182120</td></tr><tr><td>2.4</td><td>0.0013262</td><td>0.00644808</td></tr><tr><td>2.5</td><td>0.0138323</td><td>0.109271</td></tr><tr><td>2.6</td><td>0.0064225</td><td>0.0386885</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2"></td></tr><tr><td></td><td>C</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td></td><td>-3.0</td><td>1.55 × 10-5</td><td>6.33 × 10-7</td></tr><tr><td></td><td>-2.8</td><td>1.32 × 10-5</td><td>6.76 × 10-7</td></tr><tr><td></td><td>-2.6</td><td>7.95 × 10-7</td><td>1.05 × 10-7</td></tr><tr><td></td><td>-2.4</td><td>6.79 × 10-7</td><td>1.13 × 10-7</td></tr><tr><td></td><td>-2.2</td><td>1.28 × 10-5</td><td>6.76 × 10-7</td></tr><tr><td></td><td>-2.0</td><td>7.96 × 10-6</td><td>6.76 ×10-7</td></tr></table>

<table><tr><td rowspan="7">12. (a)</td><td colspan="3"></td></tr><tr><td>x</td><td>Actual Error</td><td>Error Bound</td></tr><tr><td>1.05</td><td>0.0484600</td><td>0.2185438</td></tr><tr><td>1.10</td><td>0.0210325</td><td>0.0773769</td></tr><tr><td>1.15</td><td>0.0058693</td><td>0.0364240</td></tr><tr><td>1.20</td><td>0.0026524</td><td>0.0128962</td></tr><tr><td>1.25</td><td>0.0276704</td><td>0.2185438</td></tr><tr><td></td><td>1.30</td><td>0.0128401</td><td>0.0773769</td></tr></table>

<table><tr><td colspan="2">C</td><td>Actual Error Error</td><td>Bound</td></tr><tr><td rowspan="7"></td><td></td><td></td><td></td></tr><tr><td>-3.0 -2.8</td><td>0.004666 0.003763</td><td>0.006427 0.005262</td></tr><tr><td>-2.6</td><td>0.000711</td><td>0.001071</td></tr><tr><td>-2.4</td><td>0.000591</td><td>0.000877</td></tr><tr><td>-2.2</td><td>0.004041</td><td>0.006427</td></tr><tr><td>-2.0</td><td>0.003329</td><td>0.005262</td></tr><tr><td></td><td></td><td></td></tr></table>

\*13. $\begin{array} { r } { f ^ { \prime } ( 3 ) \approx \frac { 1 } { 1 2 } [ f ( 1 ) - 8 f ( 2 ) + 8 f ( 4 ) - f ( 5 ) ] = 0 . 2 1 0 6 2 } \end{array}$ , with an error bound given by

$$
\operatorname* { m a x } _ { 1 \leq x \leq 5 } { \frac { | f ^ { ( 5 ) } ( x ) | h ^ { 4 } } { 3 0 } } \leq { \frac { 2 3 } { 3 0 } } = 0 . 7 { \overline { { 6 } } } .
$$

14. $\begin{array} { r } { f ^ { \prime } ( 3 ) \approx \frac { 1 } { 2 } [ f ( 4 ) - f ( 2 ) ] = 0 . 2 1 2 1 0 } \end{array}$ , with an error bound given by

$$
\operatorname* { m a x } _ { 1 \leq x \leq 5 } { \frac { | f ^ { \prime \prime \prime } ( x ) | h ^ { 2 } } { 6 } } \leq { \frac { 4 } { 2 } } = 0 . 6 { \overline { { 6 } } } .
$$

15. From the forward-backward difference formula (4.1), we have the following approximations:

$$
\begin{array} { r l } & { { { \mathfrak { r } } } ^ { \prime } ( 0 . 5 ) \approx 0 . 8 5 2 , { \{ } ^ { \prime } } ( 0 . 6 ) \approx 0 . 8 5 2 , { \{ } ^ { \prime }  ( 0 . 7 ) \approx 0 . 7 9 6 0  \\ & { { { \mathfrak { r } } } ^ { \prime } ( 0 . 0 ) \approx 3 . 7 0 7 , { \{ } ^ { \prime } } ( 0 . 2 ) \approx 3 . 1 5 3 , { \ f } ^ { \prime } ( 0 . 4 ) \approx 3 . 1 5 3  \end{array}
$$

16. For the endpoints of the tables, we use Formula (4.7). The other approximations come from Formula (4.6).

$$
\begin{array} { r l } & { f ^ { \prime } ( 1 . 1 ) \approx 1 7 . 7 5 , f ^ { \prime } ( 1 . 2 ) \approx 2 2 . 1 7 , f ^ { \prime } ( 1 . 3 ) \approx 2 7 . 1 0 , f ^ { \prime } ( 1 . 4 ) \approx 3 2 . 5 0 , } \\ & { f ^ { \prime } ( 8 . 1 ) \approx 3 . 0 7 5 , f ^ { \prime } ( 8 . 3 ) \approx 3 . 1 2 5 , f ^ { \prime } ( 8 . 5 ) \approx 3 . 1 5 0 , f ^ { \prime } ( 8 . 7 ) \approx 3 . 1 5 0 , } \\ & { f ^ { \prime } ( 2 . 9 ) \approx 5 . 0 8 0 , f ^ { \prime } ( 3 . 0 ) \approx 6 . 6 5 5 , f ^ { \prime } ( 3 . 1 ) \approx 8 . 2 2 0 , f ^ { \prime } ( 3 . 2 ) \approx 9 . 7 6 0 , } \\ & { f ^ { \prime } ( 2 . 0 ) \approx 0 . 1 6 0 0 , f ^ { \prime } ( 2 . 1 ) \approx - 0 . 1 0 0 0 , f ^ { \prime } ( 2 . 2 ) \approx - 0 . 3 3 0 0 , f ^ { \prime } ( 2 . 3 ) \approx - 0 . 5 5 0 0 , } \end{array}
$$

17. For the endpoints of the tables, we use Formula (4.7). The other approximations come from Formula (4.6).

$$
\begin{array} { r l } & { f ^ { \prime } ( 2 . 1 ) \approx 3 . 8 8 4 \quad f ^ { \prime } ( 2 . 2 ) \approx 2 . 8 9 6 \quad f ^ { \prime } ( 2 . 3 ) \approx 2 . 2 4 9 \quad f ^ { \prime } ( 2 . 4 ) \approx 1 . 8 3 6 \quad f ^ { \prime } ( 2 . 5 ) \approx 1 . 5 5 0 } \\ & { f ^ { \prime } ( 2 . 6 ) \approx 1 . 3 4 8 } \\ & { f ^ { \prime } ( - 3 . 0 ) \approx - 5 . 8 8 3 \quad f ^ { \prime } ( - 2 . 8 ) \approx - 5 . 4 6 7 \quad f ^ { \prime } ( - 2 . 6 ) \approx - 5 . 0 5 9 \quad f ^ { \prime } ( - 2 . 4 ) \approx - 4 . 6 5 0 } \\ & { f ^ { \prime } ( - 2 . 2 ) \approx - 4 . 2 0 8 \quad f ^ { \prime } ( - 2 . 0 ) \approx - 3 . 8 7 5 } \end{array}
$$

18. (a)

<table><tr><td></td><td>f&#x27;(0.4)</td><td>f&quot;(0.4)</td></tr><tr><td>(4.1)</td><td>h =0.6</td><td>-0.8889958 (4.8) h= 0.2 -1.191050</td></tr><tr><td></td><td>h= 0.4</td><td>-0.6979043</td></tr><tr><td></td><td>h= 0.2</td><td>-0.5486810</td></tr><tr><td></td><td>h=-0.2</td><td>-0.3104710</td></tr><tr><td>(4.4)</td><td>h = 0.2</td><td>-0.3994578</td></tr><tr><td>(4.5)</td><td>h = 0.2</td><td>-0.4295760</td></tr></table>

<table><tr><td></td><td></td><td>f&#x27;(0.4)</td><td>f&quot;(0.4)</td></tr><tr><td>(4.1)</td><td>h= 0.4</td><td>-1.059153 (4.8)</td><td>h= 0.4 -1.573943</td></tr><tr><td></td><td>h= 0.2</td><td>-0.8471275</td><td>h= 0.2 -1.492233</td></tr><tr><td></td><td>h=-0.2</td><td>-0.5486810</td><td></td></tr><tr><td></td><td>h = -0.4</td><td>-0.4295760</td><td></td></tr><tr><td>(4.4)</td><td>h= 0.2</td><td>-0.6351018</td><td></td></tr><tr><td></td><td>h=-0.2</td><td>-0.6677860</td><td></td></tr><tr><td>(4.5)</td><td>h= 0.4</td><td>-0.7443646</td><td></td></tr><tr><td></td><td>h= 0.2</td><td>-0.6979043</td><td></td></tr><tr><td>(4.6)</td><td>h= 0.2</td><td>-0.6824175</td><td></td></tr></table>

19. The approximation is $- 4 . 8 \times 1 0 ^ { - 9 }$ . $f ^ { \prime \prime } ( 0 . 5 ) = 0$ . The error bound is 0.35874. The method is very accurate since the function is symmetric about $x = 0 . 5$ .

20. With $h = 0 . 1$ , we have 36.641, and with $h = 0 . 0 1$ , we have 36.5. The actual value is 36.5935.

21. (a) $f ^ { \prime } ( 0 . 2 ) \approx - 0 . 1 9 5 1 0 2 7 \qquad \mathrm { ( b ) } f ^ { \prime } ( 1 . 0 ) \approx - 1 . 5 4 1 4 1 5 \qquad \mathrm { ( c ) } f ^ { \prime } ( 0 . 6 ) \approx - 0 . 6 8 2 4 1 7 5 \qquad \mathrm { ( b ) }$

$^ { * } 2 2$ . We have the Taylor expansions:

$$
\begin{array} { c } { { \displaystyle f ( x _ { 0 } - h ) = f ( x _ { 0 } ) - h f ^ { \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 2 } h ^ { 2 } f ^ { \prime \prime } ( x _ { 0 } ) - \displaystyle \frac { 1 } { 6 } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 2 4 } h ^ { 4 } f ^ { ( 4 ) } ( x _ { 0 } ) + O \left( h ^ { 5 } \right) ; } } \\ { { \displaystyle f ( x _ { 0 } + h ) = f ( x _ { 0 } ) + h f ^ { \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 2 } h ^ { 2 } f ^ { \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 6 } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 1 } { 2 4 } h ^ { 4 } f ^ { ( 4 ) } ( x _ { 0 } ) + O \left( h ^ { 5 } \right) ; } } \\ { { \displaystyle f ( x _ { 0 } + 2 h ) = f ( x _ { 0 } ) + 2 h f ^ { \prime } ( x _ { 0 } ) + 2 h ^ { 2 } f ^ { \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 4 } { 3 } h ^ { 3 } f ^ { \prime \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 2 } { 3 } h ^ { 4 } f ^ { ( 4 ) } ( x _ { 0 } ) + O \left( h ^ { 5 } \right) ; } } \\ { { \displaystyle f ( x _ { 0 } + 3 h ) = f ( x _ { 0 } ) + 3 h f ^ { \prime } ( x _ { 0 } ) + \displaystyle \frac { 9 } { 2 } h ^ { 2 } f ^ { \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 9 } { 2 } h ^ { 3 } f ^ { \prime \prime } ( x _ { 0 } ) + \displaystyle \frac { 2 7 } { 8 } h ^ { 4 } f ^ { ( 4 ) } ( x _ { 0 } ) + O \left( h ^ { 5 } \right) . } } \end{array}
$$

Thus,

$$
\begin{array} { l } { { A f ( x _ { 0 } - h ) + B f ( x _ { 0 } + h ) + C f ( x _ { 0 } + 2 h ) + D f ( x _ { 0 } + 3 h ) = } } \\ { { \qquad f ( x _ { 0 } ) ( A + B + C + D ) + f ^ { \prime } ( x _ { 0 } ) h [ - A + B + 2 C + 3 D ] + f ^ { \prime \prime } ( x _ { 0 } ) h ^ { 2 } \left( \frac { 1 } { 2 } A + \frac { 1 } { 2 } B + 2 C + \frac { 1 } { 2 } B + 2 C \right) + } } \\ { { \qquad + f ^ { \prime \prime \prime } ( x _ { 0 } ) h ^ { 3 } \left( - \frac { 1 } { 6 } A + \frac { 1 } { 6 } B + \frac { 4 } { 3 } C + \frac { 9 } { 2 } D \right) + f ^ { ( 4 ) } ( x _ { 0 } ) h ^ { 4 } \left( \frac { 1 } { 2 4 } A + \frac { 1 } { 2 4 } B + \frac { 2 } { 3 } C + \frac { 2 7 } { 8 } D \right) . } } \end{array}
$$

We want to eliminate the terms involving $f ^ { \prime \prime } ( x _ { 0 } )$ , $f ^ { \prime \prime \prime } ( x _ { 0 } )$ , and $f ^ { ( 4 ) } ( x _ { 0 } )$ and have the coefficient

of $f ^ { \prime } ( x _ { 0 } )$ equal 1. Thus,

$$
\begin{array} { c } { - A + B + 2 C + 3 D = 1 } \\ { \displaystyle \frac { 1 } { 2 } A + \frac { 1 } { 2 } B + 2 C + \frac { 9 } { 2 } D = 0 } \\ { - \frac { 1 } { 6 } A + \frac { 1 } { 6 } B + \frac { 4 } { 3 } C + \frac { 9 } { 2 } D = 0 } \\ { \displaystyle \frac { 1 } { 2 4 } A + \frac { 1 } { 2 4 } B + \frac { 2 } { 3 } C + \frac { 2 7 } { 8 } D = 0 . } \end{array}
$$

The solution to this linear system is

$$
A = - { \frac { 1 } { 4 } } , \quad B = { \frac { 3 } { 2 } } , \quad C = - { \frac { 1 } { 2 } } , \quad \mathrm { a n d } \quad D = { \frac { 1 } { 1 2 } } .
$$

Thus

$$
- { \frac { 1 } { 4 } } f ( x _ { 0 } - h ) + { \frac { 3 } { 2 } } f ( x _ { 0 } + h ) - { \frac { 1 } { 2 } } f ( x _ { 0 } + 2 h ) + { \frac { 1 } { 1 2 } } f ( x _ { 0 } + 3 h ) = f ( x _ { 0 } ) \left( - { \frac { 1 } { 4 } } + { \frac { 3 } { 2 } } - { \frac { 1 } { 2 } } + { \frac { 1 } { 1 2 } } \right) + h f ^ { \prime } ( x _ { 0 } ) + { \frac { 3 } { 4 } } f ( x _ { 0 } - 2 h ) + h f ^ { \prime } ( x _ { 0 } )
$$

Solving for $f ^ { \prime } ( x _ { 0 } )$ gives

$$
f ^ { \prime } ( x _ { 0 } ) = - { \frac { 1 } { h } } \left[ f ( x _ { 0 } ) { \frac { 1 0 } { 1 2 } } + { \frac { 1 } { 4 } } f ( x _ { 0 } - h ) - { \frac { 3 } { 2 } } f ( x _ { 0 } + h ) + { \frac { 1 } { 2 } } f ( x _ { 0 } + 2 h ) - { \frac { 1 } { 1 2 } } f ( x _ { 0 } + 3 h ) \right] + O \left( h ^ { 4 } \right) .
$$

Finally,

$$
f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 1 2 h } \left[ - 3 f ( x _ { 0 } - h ) - 1 0 f ( x _ { 0 } ) + 1 8 f ( x _ { 0 } + h ) - 6 f ( x _ { 0 } + 2 h ) + f ( x _ { 0 } + 3 h ) \right] + O \left( h ^ { 4 } \right) .
$$

23. $f ^ { \prime } ( 0 . 4 ) \approx - 0 . 4 2 4 9 8 4 0$ and $f ^ { \prime } ( 0 . 8 ) \approx - 1 . 0 3 2 7 7 2$ .

$^ { * } 2 4$ . (a) Assume that the computed values ${ \ddot { f } } ( x _ { 0 } + h )$ and $\ddot { f } ( x _ { 0 } )$ are related to the true values $f ( x _ { 0 } + h )$ and $f ( x _ { 0 } )$ by the formulas $f ( x _ { 0 } + h ) = f ( x _ { 0 } + h ) + e ( x _ { 0 } + h )$ and $f ( x _ { 0 } ) =$ $f ( x _ { 0 } ) + e ( x _ { 0 } )$ . The total error in the approximation becomes

$$
f ^ { \prime } ( x _ { 0 } ) - { \frac { \tilde { f } ( x _ { 0 } + h ) - \tilde { f } ( x _ { 0 } ) } { h } } = { \frac { e ( x _ { 0 } + h ) - e ( x _ { 0 } ) } { h } } - { \frac { h } { 2 } } f ^ { \prime \prime } ( \xi _ { 0 } ) .
$$

If $| e ( x _ { 0 } + h ) | < \varepsilon$ , $| e ( x _ { 0 } ) | < \varepsilon$ , and $| f ^ { \prime \prime } ( \xi _ { 0 } ) | \le M$ , then

$$
\left| f ^ { \prime } ( x _ { 0 } ) - \frac { \tilde { f } ( x _ { 0 } + h ) - \tilde { f } ( x _ { 0 } ) } { h } \right| \leq \frac { 2 \varepsilon } { h } + \frac { h M } { 2 } .
$$

(b) The function in Example 2 is

$$
f ( x ) = x e ^ { x } , \quad { \mathrm { f o r } } \quad 1 . 8 \leq x \leq 2 . 2 .
$$

We have $f ^ { \prime } ( x ) = x e ^ { x } + e ^ { x }$ and $f ^ { \prime \prime } ( x ) = x e ^ { x } + 2 e ^ { x }$ . Thus,

$$
M = \operatorname* { m a x } _ { 1 . 8 \leq x \leq 2 . 2 } | f ^ { \prime \prime } ( x ) | = f ^ { \prime \prime } ( 2 . 2 ) = 3 7 . 9 0 5 0 5 6 7 .
$$

The numbers in the table are given to 6 decimal places, so it is reasonable to let $\varepsilon =$ 0.0000005. The optimal value of $h$ is

$$
h = 2 { \sqrt { \frac { \varepsilon } { M } } } = 2 { \sqrt { \frac { 0 . 0 0 0 0 0 0 5 } { 3 7 . 9 0 5 0 5 6 7 } } } = 0 . 0 0 0 2 2 9 7 0 3 .
$$

25. The three-point formulas give the results in the following table.

<table><tr><td>Time</td><td>0</td><td>3</td><td>5</td><td>8</td><td>10</td><td>13</td></tr><tr><td>Speed</td><td>79</td><td>82.4</td><td>74.2</td><td>76.8</td><td>69.4</td><td>71.2</td></tr></table>

26. The three-point formulas give the results in the following table.

<table><tr><td rowspan=1 colspan=1>t</td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1>1.01</td><td rowspan=1 colspan=1>1.02</td><td rowspan=1 colspan=1>1.03</td><td rowspan=1 colspan=1>1.04</td></tr><tr><td rowspan=1 colspan=1>(t）</td><td rowspan=1 colspan=1>2.400</td><td rowspan=1 colspan=1>2.403</td><td rowspan=1 colspan=1>3.386</td><td rowspan=1 colspan=1>5.352</td><td rowspan=1 colspan=1>7.320</td></tr></table>

$^ { * } 2 7$ . The approximations eventually become zero since the numerator becomes zero.

28. By averaging the Taylor polynomials we have

$$
f ^ { \prime \prime \prime } ( x _ { 0 } ) = { \frac { 1 } { h ^ { 3 } } } \bigg [ - { \frac { 1 } { 2 } } f ( x _ { 0 } - 2 h ) + f ( x _ { 0 } - h ) - f ( x _ { 0 } + h ) + { \frac { 1 } { 2 } } f ( x _ { 0 } + 2 h ) \bigg ] - { \frac { h ^ { 2 } } { 4 } } f ^ { ( 5 ) } ( \xi ) ,
$$

where $\xi$ is between $x _ { 0 } - 2 h$ and $x _ { 0 } + 2 h$ .

$^ { * } 2 9$ . Since $e ^ { \prime } ( h ) = - \varepsilon / h ^ { 2 } + h M / 3$ , we have $e ^ { \prime } ( h ) = 0$ if and only if $h = \sqrt [ 3 ] { 3 \varepsilon / M }$ . Also, $e ^ { \prime } ( h ) < 0$ if $h < \sqrt [ 3 ] { 3 \varepsilon / M }$ and $e ^ { \prime } ( h ) > 0$ if $h > \sqrt [ 3 ] { 3 \varepsilon / M }$ , so an absolute minimum for $e ( h )$ occurs at $h = \sqrt [ 3 ] { 3 \varepsilon / M }$ .

# Exercise Set 4.2, page 191

1. \*(a) $f ^ { \prime } ( 1 ) \approx 1 . 0 0 0 0 1 0 9$ (b) $f ^ { \prime } ( 0 ) \approx 2 . 0 0 0 0 0 0 0$ (c) $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 7 5 1 4 5 9$ (d) $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 4 6 7 9 9$

2. (a) $f ^ { \prime } ( 1 ) \approx 0 . 9 9 9 9 9 9 9 9 8$ (b) $f ^ { \prime } ( 0 ) \approx 1 . 9 9 9 9 9 9 9 9$ (c) $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 7 5 1 4 5 8$ (d) $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 4 6 7 9 6$

3. (a) $f ^ { \prime } ( 1 ) \approx 1 . 0 0 1$ (b) $f ^ { \prime } ( 0 ) \approx 1 . 9 9 9$ (c) $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 8 3$ (d) $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 1$

4. (a) $f ^ { \prime } ( 1 ) \approx 0 . 9 9 9 9$ (b) $f ^ { \prime } ( 0 ) \approx 1 . 9 9 7$ (c) $f ^ { \prime } ( 1 . 0 5 ) \approx 2 . 2 8 2$ (d) $f ^ { \prime } ( 2 . 3 ) \approx - 1 9 . 6 6$ $^ { * } 5$ . $\int _ { 0 } ^ { \pi } \sin x \ d x \approx 1 . 9 9 9 9 9 9$

6. $\int _ { 0 } ^ { 3 \pi / 2 } \cos { x } ~ d x \approx - 1 . 0 0 0 1 3 5$

7. With $h = 0 . 1$ , Formula (4.6) becomes

$$
f ^ { \prime } ( 2 ) \approx { \frac { 1 } { 1 . 2 } } \left[ 1 . 8 e ^ { 1 . 8 } - 8 \left( 1 . 9 e ^ { 1 . 9 } \right) + 8 ( 2 . 1 ) e ^ { 2 . 1 } - 2 . 2 e ^ { 2 \cdot 2 } \right] = 2 2 . 1 6 6 9 9 5 .
$$

With $h = 0 . 0 5$ , Formula (4.6) becomes

$$
f ^ { \prime } ( 2 ) \approx { \frac { 1 } { 0 . 6 } } \left[ 1 . 9 e ^ { 1 . 9 } - 8 \left( 1 . 9 5 e ^ { 1 . 9 5 } \right) + 8 ( 2 . 0 5 ) e ^ { 2 . 0 5 } - 2 . 1 e ^ { 2 . 1 } \right] = 2 2 . 1 6 7 1 5 7 .
$$

8. The formula $\begin{array} { r } { f ^ { \prime } ( x _ { 0 } ) = \frac { 1 } { 1 2 h } \left[ f ( x _ { 0 } + 4 h ) - 1 2 f ( x _ { 0 } + 2 h ) + 3 2 f ( x _ { 0 } + h ) - 2 1 f ( x _ { 0 } ) \right] } \end{array}$ is $O \left( h ^ { 3 } \right)$

9. Let

$$
N _ { 2 } ( h ) = N \left( \frac { h } { 3 } \right) + \left( \frac { N \left( \frac { h } { 3 } \right) - N ( h ) } { 2 } \right) \quad \mathrm { a n d } \quad N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 3 } \right) + \left( \frac { N _ { 2 } \left( \frac { h } { 3 } \right) - N _ { 2 } ( h ) } { 8 } \right) .
$$

Then $N _ { 3 } ( h )$ is an $O ( h ^ { 3 } )$ approximation to $M$ .

10. Let $\begin{array} { r } { N _ { 2 } ( h ) = N \left( \frac { h } { 3 } \right) + \frac { 1 } { 8 } \left( N \left( \frac { h } { 3 } \right) - N ( h ) \right) } \end{array}$ and $\begin{array} { r } { N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 3 } \right) + \frac { 1 } { 8 0 } \left( N _ { 2 } \left( \frac { h } { 3 } \right) - N _ { 2 } ( h ) \right) } \end{array}$ . Then $N _ { 3 } ( h )$ is an $O \left( h ^ { 6 } \right)$ approximation to $M$ .

11. Let $N ( h ) = ( 1 + h ) ^ { 1 / h }$ , $\begin{array} { r } { N _ { 2 } ( h ) = 2 N \left( \frac { h } { 2 } \right) - N ( h ) , N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 2 } \right) + \frac { 1 } { 3 } ( N _ { 2 } \left( \frac { h } { 2 } \right) - N _ { 2 } ( h ) ) . } \end{array}$

(a) $N ( 0 . 0 4 ) = 2 . 6 6 5 8 3 6 3 3 1$ , $N ( 0 . 0 2 ) = 2 . 6 9 1 5 8 8 0 2 9$ , $N ( 0 . 0 1 ) = 2 . 7 0 4 8 1 3 8 2 9$   
(b) N2(0.04) = 2.717339727, $N _ { 2 } ( 0 . 0 2 ) = 2 . 7 1 8 0 3 9 6 2 \Omega$ . The $O ( h ^ { 3 } )$ approximation is $N _ { 3 } ( 0 . 0 4 ) =$ 2.718272931.   
(c) Yes, since the errors seem proportioned to $h$ for $N ( h )$ , to $h ^ { 2 }$ for $N _ { 2 } ( h )$ , and to $h ^ { 3 }$ for $N _ { 3 } ( h )$ .

$^ { * } 1 2$ . (a) We have

$$
\operatorname* { l i m } _ { h \to 0 } { \frac { \ln ( 2 + h ) - \ln ( 2 - h ) } { h } } = \operatorname* { l i m } _ { h \to 0 } { \frac { 1 } { 2 + h } } + { \frac { 1 } { 2 - h } } = 1 ,
$$

so

$$
\operatorname* { l i m } _ { h \to 0 } \left( { \frac { 2 + h } { 2 - h } } \right) ^ { 1 / h } = \operatorname* { l i m } _ { h \to 0 } e ^ { { \frac { 1 } { h } } [ \ln ( 2 + h ) - \ln ( 2 - h ) ] } = e ^ { 1 } = e .
$$

(b) $N ( 0 . 0 4 ) = 2 . 7 1 8 6 4 4 3 7 7 2 2 1 2 1 9$ , $N ( 0 . 0 2 ) = 2 . 7 1 8 3 7 2 4 4 4 8 0 0 6 0 7$ , $N ( 0 . 0 1 ) = 2 . 7 1 8 3 0 4 4 8 1 2 4 1 6 8 5$   
(c) Let $\begin{array} { r } { N _ { 2 } ( h ) = 2 N \left( \frac { h } { 2 } \right) - N ( h ) } \end{array}$ and $\begin{array} { r } { N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 2 } \right) + \frac { 1 } { 3 } \left[ N _ { 2 } \left( \frac { h } { 2 } \right) - N _ { 2 } ( h ) \right] } \end{array}$ . Then $N _ { 2 } ( 0 . 0 4 ) =$ 2.718100512379995, $N _ { 2 } ( 0 . 0 2 ) = 2 . 7 1 8 2 3 6 5 1 7 6 8 2 7 6 3$ and $N _ { 3 } ( 0 . 0 4 ) = 2 . 7 1 8 2 8 1 8 5 2 7 8 3 6 8 5$ . $N _ { 3 } ( 0 . 0 4 )$ is an $O \left( h ^ { 3 } \right)$ approximation satisfying $| e - N _ { 3 } ( 0 . 0 4 ) | \le 0 . 5 \times 1 0 ^ { - 7 }$ .

$$
N ( - h ) = \left( { \frac { 2 - h } { 2 + h } } \right) ^ { 1 / - h } = \left( { \frac { 2 + h } { 2 - h } } \right) ^ { 1 / h } = N ( h )
$$

(e) Let

$$
e = N ( h ) + K _ { 1 } h + K _ { 2 } h ^ { 2 } + K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot .
$$

Replacing $h$ by $- h$ gives

$$
e = N ( - h ) - K _ { 1 } h + K _ { 2 } h ^ { 2 } - K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot ,
$$

but $N ( - h ) = N ( h )$ , so that

$$
e = N ( h ) - K _ { 1 } h + K _ { 2 } h ^ { 2 } - K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot .
$$

Thus,

$$
K _ { 1 } h + K _ { 3 } h ^ { 3 } + \cdot \cdot \cdot = - K _ { 1 } h - K _ { 3 } h ^ { 3 } \cdot \cdot \cdot ,
$$

and it follows that $K _ { 1 } = K _ { 3 } = K _ { 5 } = \cdot \cdot \cdot = 0$ and

$$
e = N ( h ) + K _ { 2 } h ^ { 2 } + K _ { 4 } h ^ { 4 } + \cdot \cdot \cdot .
$$

(f) Let

$$
N _ { 2 } ( h ) = N \left( { \frac { h } { 2 } } \right) + { \frac { 1 } { 3 } } \left( N \left( { \frac { h } { 2 } } \right) - N ( h ) \right)
$$

and

$$
N _ { 3 } ( h ) = N _ { 2 } \left( \frac { h } { 2 } \right) + \frac { 1 } { 1 5 } \left( N _ { 2 } \left( \frac { h } { 2 } \right) - N _ { 2 } ( h ) \right) .
$$

Then

$$
N _ { 2 } ( 0 . 0 4 ) = 2 . 7 1 8 2 8 1 8 0 0 6 6 0 4 0 2 , N _ { 2 } ( 0 . 0 2 ) = 2 . 7 1 8 2 8 1 8 2 6 7 2 2 0 4 3
$$

and

$$
N _ { 3 } ( 0 . 0 4 ) = 2 . 7 1 8 2 8 1 8 2 8 4 5 9 4 8 7 .
$$

$N _ { 3 } ( 0 . 0 4 )$ is an $O \left( h ^ { 6 } \right)$ approximation satisfying

$$
| e - N _ { 3 } ( 0 . 0 4 ) | \leq 0 . 5 \times 1 0 ^ { - 1 2 } .
$$

\*13. (a) We have

$$
P _ { 0 , 1 } ( x ) = { \frac { \left( x - h ^ { 2 } \right) N _ { 1 } \left( { \frac { h } { 2 } } \right) } { { \frac { h ^ { 2 } } { 4 } } - h ^ { 2 } } } + { \frac { \left( x - { \frac { h ^ { 2 } } { 4 } } \right) N _ { 1 } ( h ) } { h ^ { 2 } - { \frac { h ^ { 2 } } { 4 } } } } , \quad \mathrm { s o } \quad P _ { 0 , 1 } ( 0 ) = { \frac { 4 N _ { 1 } \left( { \frac { h } { 2 } } \right) - N _ { 1 } ( h ) } { 3 } } .
$$

Similarly,

$$
P _ { 1 , 2 } ( 0 ) = \frac { 4 N _ { 1 } \left( \frac { h } { 4 } \right) - N _ { 1 } \left( \frac { h } { 2 } \right) } { 3 } .
$$

(b) We have

$$
P _ { 0 , 2 } ( x ) = { \frac { \left( x - h ^ { 4 } \right) N _ { 2 } \left( { \frac { h } { 2 } } \right) } { { \frac { h ^ { 4 } } { 1 6 } } - h ^ { 4 } } } + { \frac { \left( x - { \frac { h ^ { 4 } } { 1 6 } } \right) N _ { 2 } ( h ) } { h ^ { 4 } - { \frac { h ^ { 4 } } { 1 6 } } } } , \quad { \mathrm { ~ s o ~ } } \quad P _ { 0 , 2 } ( 0 ) = { \frac { 1 6 N _ { 2 } \left( { \frac { h } { 2 } } \right) - N _ { 2 } ( h ) } { 1 5 } } .
$$

14. All the approximations of the form $N _ { 2 i } \left( h / 2 ^ { j } \right)$ , for $i = 1 , 2 , \dots$ and $j = 0 , 1 , 2 , . . .$ , will be upper bounds for $M$ , and all the approximations of the form $N _ { 2 i + 1 } \left( { \frac { h } { 2 ^ { j } } } \right)$ , for $i = 0 , 1 , 2 , \ldots$ and $j = 0 , 1 , 2 , \ldots$ , will be lower bounds for $M$ .

15. (a) We have

$$
p _ { 4 } = 4 \sin \left( { \frac { \pi } { 4 } } \right) = 4 { \frac { \sqrt { 2 } } { 2 } } = 2 { \sqrt { 2 } } \quad { \mathrm { a n d } } \quad P _ { 4 } = 4 \tan \left( { \frac { \pi } { 4 } } \right) = 4 \cdot 1 = 4 .
$$

(b) We have

$$
{ \frac { 2 p _ { k } P _ { k } } { p _ { k } + P _ { k } } } = { \frac { 2 k \sin \left( { \frac { \pi } { k } } \right) \cdot k \tan \left( { \frac { \pi } { k } } \right) } { k \sin \left( { \frac { \pi } { k } } \right) + \tan \left( { \frac { \pi } { k } } \right) } } = { \frac { 2 k ^ { 2 } \left( \sin \left( { \frac { \pi } { k } } \right) \right) ^ { 2 } } { k \sin \left( { \frac { \pi } { k } } \right) \left( 1 + \cos \left( { \frac { \pi } { k } } \right) \right) } } = { \frac { 2 k \sin \left( { \frac { \pi } { k } } \right) } { 1 + \cos \left( { \frac { \pi } { k } } \right) } }
$$

and

$$
\begin{array} { l } { P _ { 2 k } = 2 k \tan \left( \frac { \pi } { 2 k } \right) = 2 k \frac { \sin \left( \frac { \pi } { 2 k } \right) } { \cos \left( \frac { \pi } { 2 k } \right) } = 2 k \sqrt { \frac { 1 - \cos \left( \frac { \pi } { k } \right) } { 1 + \cos \left( \frac { \pi } { k } \right) } } } \\ { = 2 k \sqrt { \displaystyle \frac { 1 - \cos \left( \frac { \pi } { k } \right) } { 1 + \cos \left( \frac { \pi } { k } \right) } } \cdot \sqrt { \frac { 1 + \cos \left( \frac { \pi } { k } \right) } { 1 + \cos \left( \frac { \pi } { k } \right) } } = 2 k \frac { \sqrt { 1 - \left( \cos \left( \frac { \pi } { k } \right) \right) ^ { 2 } } } { 1 + \cos \left( \frac { \pi } { k } \right) } = \frac { 2 k \sin \left( \frac { \pi } { k } \right) } { 1 + \cos \left( \frac { \pi } { k } \right) } . } \end{array}
$$

In addition,

$$
\begin{array} { c } { { \sqrt { p _ { k } P _ { 2 k } } = \sqrt { k \sin \left( \displaystyle \frac { \pi } { k } \right) \cdot 2 k \tan \left( \displaystyle \frac { \pi } { 2 k } \right) } = k \sqrt { \left( 2 \sin \left( \displaystyle \frac { \pi } { 2 k } \right) \cos \left( \displaystyle \frac { \pi } { 2 k } \right) \right) \cdot 2 \left( \displaystyle \frac { \sin \left( \displaystyle \frac { \pi } { 2 k } \right) } { \cos \left( \displaystyle \frac { \pi } { 2 k } \right) } \right) } } } \\ { { = 2 k \sqrt { \left( \sin \left( \displaystyle \frac { \pi } { 2 k } \right) \right) ^ { 2 } } = 2 k \sin \left( \displaystyle \frac { \pi } { 2 k } \right) = p _ { 2 k } . } } \end{array}
$$

\*(c) The polygonal approximations are in the following table.

<table><tr><td>k</td><td>4</td><td>8</td><td>16</td><td>32</td><td>64</td><td>128</td><td>256</td><td>512</td></tr><tr><td>Pk</td><td>2√2</td><td>3.0614675</td><td>3.1214452</td><td>3.1365485</td><td>3.1403312</td><td>3.1412723</td><td>3.1415138</td><td>3.1415729</td></tr><tr><td>Pk</td><td>4</td><td>3.3137085</td><td>3.1825979</td><td>3.1517249</td><td>3.144184</td><td>3.1422236</td><td>3.1417504</td><td>3.1416321</td></tr></table>

\*(d) Values of $p _ { k }$ and $P _ { k }$ are given in the following tables, together with the extrapolation results: For $p _ { k }$ we have :

<table><tr><td>2.8284271</td><td></td><td></td><td></td><td></td></tr><tr><td>3.0614675</td><td>3.1391476</td><td></td><td></td><td></td></tr><tr><td>3.1214452</td><td>3.1414377</td><td>3.1415904</td><td></td><td></td></tr><tr><td>3.1365485</td><td>3.1415829</td><td>3.1415926</td><td>3.1415927</td><td></td></tr><tr><td>3.1403312</td><td>3.1415921</td><td>3.1415927</td><td>3.1415927</td><td>3.1415927</td></tr></table>

For $P _ { k }$ we have :

<table><tr><td>4</td><td></td><td></td><td></td><td></td></tr><tr><td>3.3137085</td><td>3.0849447</td><td></td><td></td><td></td></tr><tr><td>3.1825979</td><td>3.1388943</td><td>3.1424910</td><td></td><td></td></tr><tr><td>3.1517249</td><td>3.1414339</td><td>3.1416032</td><td>3.1415891</td><td></td></tr><tr><td>3.1441184</td><td>3.1415829</td><td>3.1415928</td><td>3.1415926</td><td>3.1415927</td></tr></table>

# Exercise Set 4.3, page 202

1. The Trapezoidal rule gives the following approximations.

(a) 0.265625  
(b) −0.2678571  
\*(c) 0.228074  
(d) 0.1839397  
(e) −0.8666667  
(f) −0.1777643  
(g) 0.2180895  
(h) 4.1432597

2. The Trapezoidal rule gives the following approximations.

(a) 0.4693956405  
(b) 0.08664339760  
(c) −0.03702425262  
(d) 0.2863341726

3. For the approximations in Exercise 1 we have the following.   

<table><tr><td></td><td>Actual error</td><td>Error bound</td></tr><tr><td>(a)</td><td>0.071875</td><td>0.125</td></tr><tr><td>(b)</td><td>7.943 × 10-4</td><td>9.718 × 10-4</td></tr><tr><td>*（c）</td><td>0.0358146</td><td>0.0396972</td></tr><tr><td>(d)</td><td>0.0233369</td><td>0.1666667</td></tr><tr><td>(e)</td><td>0.1326975</td><td>0.5617284</td></tr><tr><td>(f)</td><td>9.443 × 10-4</td><td>1.0707 × 10-3</td></tr><tr><td>(g)</td><td>0.0663431</td><td>0.0807455</td></tr><tr><td>(h)</td><td>1.554631</td><td>2.298827</td></tr></table>

4. For the approximations in Exercise 2 we have the following.

<table><tr><td>Actual error</td><td>Error bound</td></tr><tr><td>(a) 0.0203171288</td><td>0.02083333333</td></tr><tr><td>(b） 0.03407359031</td><td>0.0625</td></tr><tr><td>0.01664745664 (d) 0.0138202920</td><td>0.02444080544 0.02904245657</td></tr></table>

5. Simpson’s rule gives the following approximations.

(a) 0.1940104  
(b) −0.2670635  
\*(c) 0.1922453  
(d) 0.16240168  
(e) −0.7391053  
(f) −0.1768216  
(g) 0.1513826  
(h) 2.5836964

6. Simpson’s rule gives the following approximations.

(a) 0.4897985467  
(b) 0.05285463857  
(c) −0.02027158961  
(d) 0.2762704525

7. Simpson’s rule gives the following approximations.

<table><tr><td></td><td>Actual error</td><td>Error bound</td></tr><tr><td>(a)</td><td>2.604 ×10-4</td><td>2.6042 × 10-4</td></tr><tr><td>(b)</td><td>7.14 × 10-7</td><td>9.92 ×10-7</td></tr><tr><td>*（c）</td><td>1.406 × 10-5</td><td>2.170 × 10-5</td></tr><tr><td>(d)</td><td>1.7989 × 10-3</td><td>4.1667 × 10-4</td></tr><tr><td>(e)</td><td>5.1361 × 10-3</td><td>0.063280</td></tr><tr><td>(f)</td><td>1.549 × 10-6</td><td>2.095 × 10-6</td></tr><tr><td>(g)</td><td>3.6381 × 10-4</td><td>4.1507 × 10-4</td></tr><tr><td>(h)</td><td>4.9322 × 10-3</td><td>0.1302826</td></tr></table>

8. Simpson’s rule gives the following approximations.

<table><tr><td>Actual error</td><td>Error bound</td></tr><tr><td>(a) 0.0000857774</td><td>0.0000868056</td></tr><tr><td>(b） 0.00028483128</td><td>0.001215277778</td></tr><tr><td>0.00010520637</td><td>0.0001147849363</td></tr><tr><td>(d） 0.0001565719</td><td>0.0005334208049</td></tr></table>

9. The Midpoint rule gives the following approximations.

(a) 0.1582031  
(b) −0.2666667  
\*(c) 0.1743309  
(d) 0.1516327  
(e) −0.6753247  
(f) −0.1768200  
(g) 0.1180292  
(h) 1.8039148

10. The Midpoint rule gives the following approximations.

(a) 0.5  
(b) 0.03596025906  
(c) −0.01189525810  
(d) 0.2658385924

11. The Midpoint rule gives the following approximations.

<table><tr><td>Actual error</td><td>Error bound</td></tr><tr><td>(a) 0.0355469</td><td>0.0625</td></tr><tr><td>(b) 3.961 × 10-4</td><td>4.859×10-4</td></tr><tr><td>*（c） 0.0179285</td><td>0.0198486</td></tr><tr><td>(d) 8.9701 × 10-3</td><td>0.0833333</td></tr><tr><td>(e) 0.0564448</td><td>0.2808642</td></tr><tr><td>(f) 4.698×10-4</td><td>5.353 × 10-4</td></tr><tr><td>(g) 0.0337172</td><td>0.0403728</td></tr><tr><td>(h) 0.7847138</td><td>1.1494136</td></tr></table>

12. The Midpoint rule gives the following approximations.

<table><tr><td>Actual error</td><td>Error bound</td></tr><tr><td>(a) 0.0102872307</td><td>0.01041666667</td></tr><tr><td>(b） 0.01660954823 0.00848153788</td><td>0.03125</td></tr><tr><td>C (d） 0.0066752882</td><td>0.01222040272 0.01452122828</td></tr></table>

\*13. $\begin{array} { r } { f ( 1 ) = \frac { 1 } { 2 } } \end{array}$

14. Simpson’s rule gives the result $\textstyle { \frac { 1 3 } { 3 } }$ .

$^ \mathrm { * } \mathrm { 1 5 }$ . The degree of precision is 3.

16. The degree of precision is 3.

$^ *$ 17. $\begin{array} { r } { c _ { 0 } = \frac { 1 } { 3 } } \end{array}$ , $\begin{array} { r } { c _ { 1 } = \frac { 4 } { 3 } } \end{array}$ , $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 3 } } \end{array}$

18. $\begin{array} { r } { c _ { 0 } = \frac { 7 } { 3 } } \end{array}$ , $c _ { 1 } = - \textstyle { \frac { 2 } { 3 } }$ , $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 3 } } \end{array}$

$^ { * } 1 9$ . $\begin{array} { r } { c _ { 0 } = \frac { 1 } { 4 } } \end{array}$ , $\begin{array} { r } { c _ { 1 } = \frac { 3 } { 4 } } \end{array}$ , and $\begin{array} { r } { x _ { 1 } = \frac { 2 } { 3 } } \end{array}$ gives the highest degree of precision, which is 2.

20. $\begin{array} { r } { c _ { 1 } = \frac { 1 } { 2 } } \end{array}$ , $x _ { 0 } = 0 . 2 1 1 3 2 4 8 6 5$ and $x _ { 1 } = 0 . 7 8 8 6 7 5 1 3 5$ give the highest degree of precision, 3.

21. The following approximations are obtained from Formula (4.25) through Formula (4.32), respectively.

(a) 0.1024404, 0.1024598, 0.1024598, 0.1024598, 0.1024695, 0.1024663, 0.1024598, and 0.1024598   
(b) 0.7853982, 0.7853982, 0.7853982, 0.7853982, 0.7853982, 0.7853982, 0.7853982, and 0.7853982   
(c) 1.497171, 1.477536, 1.477529, 1.477523, 1.467719, 1.470981, 1.477512, and 1.477515   
(d) 4.950000, 2.740909, 2.563393, 2.385700, 1.636364, 1.767857, 2.074893, and 2.116379   
(e) 3.293182, 2.407901, 2.359772, 2.314751, 1.965260, 2.048634, 2.233251, and 2.249001   
(f) 0.5000000, 0.6958004, 0.7126032, 0.7306341, 0.7937005, 0.7834709, 0.7611137, and 0.7593572

22. We have

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td><td></td></tr><tr><td>(4.23)</td><td>(4.24)</td><td>(4.26)</td><td>(4.27)</td><td>(4.29)</td></tr><tr><td>5.43476</td><td>5.03420</td><td>5.03292</td><td>4.83393</td><td>5.03180</td></tr></table>

23. The errors in Exercise 16 are $1 . 6 \times 1 0 ^ { - 6 }$ , $5 . 3 \times 1 0 ^ { - 8 }$ , $- 6 . 7 \times 1 0 ^ { - 7 }$ , $- 7 . 2 \times 1 0 ^ { - 7 }$ , and $- 1 . 3 \times 1 0 ^ { - 6 }$ , respectively.

\*24. For

$$
\begin{array} { l } { f ( x ) = x : a _ { 0 } x _ { 0 } + a _ { 1 } ( x _ { 0 } + h ) + a _ { 2 } ( x _ { 0 } + 2 h ) = 2 x _ { 0 } h + 2 h ^ { 2 } ; } \\ { f ( x ) = x ^ { 2 } : a _ { 0 } x _ { 0 } ^ { 2 } + a _ { 1 } ( x _ { 0 } + h ) ^ { 2 } + a _ { 2 } ( x _ { 0 } + 2 h ) ^ { 2 } = 2 x _ { 0 } ^ { 2 } h + 4 x _ { 0 } h ^ { 2 } + \frac { 8 h ^ { 3 } } { 3 } ; } \\ { f ( x ) = x ^ { 3 } : a _ { 0 } x _ { 0 } ^ { 3 } + a _ { 1 } ( x _ { 0 } + h ) ^ { 3 } + a _ { 2 } ( x _ { 0 } + 2 h ) ^ { 3 } = 2 x _ { 0 } ^ { 3 } h + 6 x _ { 0 } ^ { 2 } h ^ { 2 } + 8 x _ { 0 } h ^ { 3 } + 4 h ^ { 4 } . } \end{array}
$$

Solving this linear system for $a _ { 0 } , \ a _ { 1 }$ , and $a _ { 2 }$ gives $\begin{array} { l } { { a _ { 0 } ~ = ~ \frac { h } { 3 } , a _ { 1 } ~ = ~ \frac { 4 h } { 3 } } } \end{array}$ , and $\begin{array} { l } { { a _ { 2 } ~ = ~ { \frac { h } { 3 } } } } \end{array}$ . Using $f ( x ) = x ^ { 4 }$ gives $f ^ { ( 4 ) } ( \xi ) = 2 4$ , so

$$
\frac { 1 } { 5 } \left( x _ { 2 } ^ { 5 } - x _ { 0 } ^ { 5 } \right) = \frac { h } { 3 } \left( x _ { 0 } ^ { 4 } + 4 x _ { 1 } ^ { 4 } + x _ { 2 } ^ { 4 } \right) + 2 4 k .
$$

Replacing $x _ { 1 }$ with $x _ { 0 } + h$ , $x _ { 2 }$ with $x _ { 0 } + 2 h$ and simplifying gives $k = - h ^ { 5 } / 9 0$

25. If $E ( x ^ { k } ) = 0$ , for all $k = 0 , 1 , \ldots , n$ and $E ( x ^ { n + 1 } ) \neq 0$ , then with $p _ { n + 1 } ( x ) = x ^ { n + 1 }$ , we have a polynomial of degree $n + 1$ for which $E ( p _ { n + 1 } ( x ) ) \neq 0$ . Let $p ( x ) = a _ { n } x ^ { n } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 }$ b e any polynomial of degree less than or equal to $n$ . Then $E ( p ( x ) ) = a _ { n } E ( x ^ { n } ) + \cdot \cdot \cdot + a _ { 1 } E ( x ) +$ $a _ { 0 } E ( 1 ) = 0$ . Conversely, if $E ( p ( x ) ) = 0$ , for all polynomials of degree less than or equal to $n$ , it follows that $E ( x ^ { k } ) = 0$ , for all $k = 0 , 1 , \ldots , n$ . Let $p _ { n + 1 } ( x ) = a _ { n + 1 } x ^ { n + 1 } + \cdot \cdot \cdot + a _ { 0 }$ be a polynomial of degree $n + 1$ for which $E ( p _ { n + 1 } ( x ) ) \neq 0$ . Since $a _ { n + 1 } \neq 0$ , we have

$$
x ^ { n + 1 } = { \frac { 1 } { a _ { n + 1 } } } p _ { n + 1 } ( x ) - { \frac { a _ { n } } { a _ { n + 1 } } } x ^ { n } - \cdot \cdot \cdot - { \frac { a _ { 0 } } { a _ { n + 1 } } } .
$$

Then

$$
\begin{array} { r c l } { E ( x ^ { n + 1 } ) } & { = } & { \displaystyle \frac { 1 } { a _ { n + 1 } } E ( p _ { n + 1 } ( x ) ) - \frac { a _ { n } } { a _ { n + 1 } } E ( x ^ { n } ) - \cdots - \frac { a _ { 0 } } { a _ { n + 1 } } E ( 1 ) } \\ & & { = } & { \displaystyle \frac { 1 } { a _ { n + 1 } } E ( p _ { n + 1 } ( x ) ) \neq 0 . } \end{array}
$$

Thus, the quadrature formula has degree of precision $n$ .

\*26. Using $n = 3$ in Theorem 4.2 gives

$$
\int _ { a } ^ { b } f ( x ) d x = \sum _ { i = 0 } ^ { 3 } a _ { i } f ( x _ { i } ) + \frac { h ^ { 5 } f ^ { ( 4 ) } ( \xi ) } { 2 4 } \int _ { 0 } ^ { 3 } t ( t - 1 ) ( t - 2 ) ( t - 3 ) d t .
$$

Since

$$
\int _ { 0 } ^ { 3 } t ( t - 1 ) ( t - 2 ) ( t - 3 ) d t = - \frac { 9 } { 1 0 } ,
$$

the error term is

$$
- 3 h ^ { 5 } f ^ { ( 4 ) } ( \xi ) / 8 0 .
$$

Also,

$$
a _ { i } = \int _ { x _ { 0 } } ^ { x _ { 3 } } \prod _ { { j = 0 } \atop { j \neq i } } ^ { 3 } { \frac { x - x _ { j } } { x _ { i } - x _ { j } } } d x , \mathrm { ~ f o r ~ e a c h ~ } i = 0 , 1 , 2 , 3 .
$$

Using the change of variables $x = x _ { 0 } + t h$ gives

$$
a _ { i } = h \int _ { 0 } ^ { 3 } \prod _ { { j = 0 } \atop { j \ne i } } ^ { 3 } \frac { t - j } { i - j } d t , \mathrm { ~ f o r ~ e a c h ~ } i = 0 , 1 , 2 , 3 .
$$

Evaluating the integrals gives

$$
a _ { 0 } = \frac { 3 h } { 8 } , \quad a _ { 1 } = \frac { 9 h } { 8 } , \quad a _ { 2 } = \frac { 9 h } { 8 } , \quad \mathrm { a n d } \quad a _ { 3 } = \frac { 3 h } { 8 } .
$$

# Exercise Set 4.4, page 210

1. The Composite Trapezoidal rule approximations are:

(a) 0.639900  
(b) 31.3653  
(c) 0.784241  
(d) −6.42872  
(e) −13.5760  
(f) 0.476977  
(g) 0.605498  
(h) 0.970926

2. The Composite Trapezoidal rule approximations and actual values are:   

<table><tr><td>Composite Trapezoidal Approximation</td><td>Actual Integral</td></tr><tr><td>(a) 0.91193343</td><td>0.92073549</td></tr><tr><td>*(b) 0.09363001</td><td>0.08802039</td></tr><tr><td>（c） -0.66468785</td><td>-0.66293045</td></tr><tr><td>(d) 0.36487225</td><td>0.36423547</td></tr></table>

3. The Composite Simpson’s rule approximations are:

(a) 0.99999998   
(b) 1.9999999   
(c) 2.2751458   
(d) −19.646796

4. We have

<table><tr><td>Composite Simpson&#x27;s Approximation</td><td>Actual Integral</td></tr><tr><td>(a) 0.92088605</td><td>0.92073549</td></tr><tr><td>*（b） 0.08809221</td><td>0.08802039</td></tr><tr><td>(c） -0.66292308</td><td>-0.66293045</td></tr><tr><td>(d） 0.36423967</td><td>0.36423547</td></tr></table>

5. The Composite Midpoint rule approximations are:

(a) 0.633096  
(b) 11.1568  
(c) 0.786700  
(d) −6.11274  
(e) −14.9985  
(f) 0.478751  
(g) 0.602961  
(h) 0.947868

6. We have

<table><tr><td>Composite Midpoint Approximation</td><td>Actual Integral</td></tr><tr><td>(a) 0.92862909</td><td>0.92073549</td></tr><tr><td>*(b) 0.08177145</td><td>0.08802039</td></tr><tr><td>（c） -0.66067279</td><td>-0.66293045</td></tr><tr><td>(d） 0.36342511</td><td>0.36423547</td></tr></table>

7. (a) The Composite Trapezoidal rule approximation is 3.15947567. (b) The Composite Simpson’s rule approximation is 3.10933713. (c) The Composite Midpoint rule approximation is 3.00906003.   
\*8. (a) The Composite Trapezoidal rule approximation is 0.4215820. (b) The Composite Simpson’s rule approximation is 0.4227162. (c) The Composite Midpoint rule approximation is 0.4249845.

\*9. $\alpha = 1 . 5$

10. $\operatorname { - 1 } ) = 1 , \ f ( - 0 . 5 ) = 2 , \ f ( 0 ) = 6 , \ f ( 0 . 5 ) = 3 , \ f ( 1 ) = 1$

11. (a) The Composite Trapezoidal rule requires $h < 0 . 0 0 0 9 2 2 2 9 5$ and $n \geq 2 1 6 8$ . (b) The Composite Simpson’s rule requires $h < 0 . 0 3 7 6 5 8$ and $n \geq 5 4$ . (c) The Composite Midpoint rule requires $h < 0 . 0 0 0 6 5 2 1 6$ and $n \geq 3 0 6 6$ .

12. (a) The Composite Trapezoidal rule requires $h < 0 . 0 0 6 9 6 6 9$ and $n \geq 4 5 1$ (b) The Composite Simpson’s rule requires $h < 0 . 1 3 2 7 4 9$ and $n \geq 2 4$ . (c) The Composite Midpoint rule requires $h < 0 . 0 0 4 9 2 6 3$ and $n \geq 6 3 6$ .

13. (a) The Composite Trapezoidal rule requires $h < 0 . 0 4 3 8 2$ and $n \geq 4 6$ . The approximation is 0.405471. (b) The Composite Simpson’s rule requires $h < 0 . 4 4 2 6 7$ and $n \geq 6$ . The approximation is 0.405466. (c) The Composite Midpoint rule requires $h < 0 . 0 3 0 9 8$ and $n \geq 6 4$ . The approximation is 0.405460.

14. (a) The Composite Trapezoidal rule requires $h < 0 . 0 1 0 9 5$ and $n \geq 9 1$ . With $n = 9 1$ , the approximation is 0.6363013. (b) The Composite Simpson’s rule requires $h \ < \ 0 . 1 7 3 2 0 5$ and $n \geq 6$ . With $n = 6$ , the approximation is 0.6362975. (c) The Composite Midpoint rule requires $h < 0 . 0 0 7 7 4 6 0$ and $n > 1 2 8$ . With $n = 1 3 0$ , the approximation is 0.6362875.

15. (a) Because the right and left limits at 0.1 and 0.2 for $f , \ f ^ { \prime }$ , and $f ^ { \prime \prime }$ are the same, the functions are continuous on $[ 0 , 0 . 3 ]$ . However,

$$
f ^ { \prime \prime \prime } ( x ) = { \left\{ \begin{array} { l l } { 6 , } & { 0 \leq x \leq 0 . 1 } \\ { 1 2 , } & { 0 . 1 < x \leq 0 . 2 } \\ { 1 2 , } & { 0 . 2 < x \leq 0 . 3 } \end{array} \right. }
$$

is discontinuous at $x = 0 . 1$

(b) We have 0.302506 with an error bound of $1 . 9 \times 1 0 ^ { - 4 }$ .

(c) We have 0.302425, and the value of the actual integral is the same.

$^ *$ 16. To show that the sum

$$
\sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) 2 h
$$

is a Riemann Sum, let $y _ { i } = x _ { 2 i }$ , for $i = 0 , 1 , \ldots { \frac { \pi } { 2 } }$ . Then $\Delta y _ { i } = y _ { i + 1 } - y _ { i } = 2 h$ and $y _ { i - 1 } \leq \xi _ { i } \leq$ $y _ { i }$ . Thus,

$$
\sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) \Delta y _ { j } = \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) 2 h
$$

is a Riemann Sum for $\textstyle { \int _ { a } ^ { b } f ^ { ( 4 ) } ( x ) d x }$ . Hence

$$
E ( f ) = - { \frac { h ^ { 5 } } { 9 0 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) = - { \frac { h ^ { 4 } } { 1 8 0 } } { \bigg [ } \sum _ { j = 1 } ^ { n / 2 } f ^ { ( 4 ) } ( \xi _ { j } ) 2 h { \bigg ] } \approx - { \frac { h ^ { 4 } } { 1 8 0 } } \int _ { a } ^ { b } f ^ { ( 4 ) } ( x ) d x = - { \frac { h ^ { 4 } } { 1 8 0 } } { \big [ } f ^ { \prime \prime \prime } ( b ) - f ^ { \prime \prime } ( b ) { \big ] }
$$

17. (a) For the Composite Trapezoidal rule, we have

$$
E ( f ) = - { \frac { h ^ { 3 } } { 1 2 } } \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) = - { \frac { h ^ { 2 } } { 1 2 } } \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) h = - { \frac { h ^ { 2 } } { 1 2 } } \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) \Delta x _ { j } ,
$$

where $\Delta x _ { j } = x _ { j + 1 } - x _ { j } = h$ for each $j$ . Since $\textstyle \sum _ { j = 1 } ^ { n } f ^ { \prime \prime } ( \xi _ { j } ) \Delta x _ { j }$ is a Riemann sum for $\begin{array} { r } { \int _ { a } ^ { b } f ^ { \prime \prime } ( x ) \ d x = f ^ { \prime } ( b ) - f ^ { \prime } ( a ) } \end{array}$ , we have

$$
E ( f ) \approx - { \frac { h ^ { 2 } } { 1 2 } } [ f ^ { \prime } ( b ) - f ^ { \prime } ( a ) ] .
$$

(b) For the Composite Midpoint rule, we have

$$
E ( f ) = { \frac { h ^ { 3 } } { 3 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { \prime \prime } ( \xi _ { j } ) = { \frac { h ^ { 2 } } { 6 } } \sum _ { j = 1 } ^ { n / 2 } f ^ { \prime \prime } ( \xi _ { j } ) ( 2 h ) .
$$

But $\textstyle \sum _ { j = 1 } ^ { n / 2 } f ^ { \prime \prime } ( \xi _ { j } ) ( 2 h )$ is a Riemann sum for $\begin{array} { r } { \int _ { a } ^ { b } f ^ { \prime \prime } ( x ) \ d x = f ^ { \prime } ( b ) - f ^ { \prime } ( a ) } \end{array}$ , so

$$
E ( f ) \approx \frac { h ^ { 2 } } { 6 } [ f ^ { \prime } ( b ) - f ^ { \prime } ( a ) ] .
$$

18. (a) Composite Trapezoidal Rule: With $h = 0 . 0 0 6 9 6 6 9$ , the error estimate is $2 . 5 4 1 \times 1 0 ^ { - 5 }$ . (b) Composite Simpson’s Rule: With $h = 0 . 1 3 2 7 4 9$ , the error estimate is $3 . 2 5 2 \times 1 0 ^ { - 5 }$ . (c) Composite Midpoint Rule: With $h = 0 . 0 0 4 9 2 6 3$ , the error estimate is $2 . 5 4 1 \times 1 0 ^ { - 5 }$ .

19. (a) The estimate using the Composite Trapezoidal rule is $- \textstyle { \frac { 1 } { 2 } } h ^ { 2 } \ln 2 = - 6 . 2 9 6 \times 1 0 ^ { - 6 }$ . (b) The estimate using the Composite Simpson’s rule is $- \textstyle { \frac { 1 } { 2 4 0 } } h ^ { 2 } = - 3 . 7 5 \times 1 0 ^ { - 6 }$ . (c) The estimate using the Composite Midpoint rule is $\textstyle { \frac { 1 } { 6 } } h ^ { 2 } \ln 2 = 6 . 9 3 2 \times 1 0 ^ { - 6 }$ .

20. (a) 0.68269822 obtained using $n = 1 0$ in Composite Simpson’s rule. (b) 0.95449101 obtained using $n = 1 4$ in Composite Simpson’s rule. (c) 0.99729312 obtained using $n = 2 0$ in Composite Simpson’s rule.

21. The length is approximately 15.8655.

$^ *$ 22. The length of the track is approximately 9858 ft.

23. Composite Simpson’s rule with $h = 0 . 2 5$ gives 2.61972 s.

24. An approximation for $T$ is 1054.694.

25. The length is approximately 58.47082, using $n = 1 0 0$ in the Composite Simpson’s rule.

$^ *$ 26. (a) For $p _ { 0 } = 0 . 5$ , we have $p _ { 6 } = 1 . 6 4 4 8 5 4$ with $n = 2 0$ in the Composite Simpson’s rule. (b) For $p _ { 0 } = 0 . 5$ , we have $p _ { 6 } = 1 . 6 4 5 0 8 5$ with $n = 4 0$ in the Composite Trapezoidal rule.

# Exercise Set 4.5, page 218

1. Romberg integration gives $R _ { 3 , 3 }$ as follows:

\*(a) 0.1922593  
(b) 0.1606105  
(c) −0.1768200  
(d) 0.08875677  
(e) 2.5879685  
(f) −0.7341567  
(g) 0.6362135  
(h) 0.6426970

2. Romberg integration gives $R _ { 3 , 3 }$ as follows:

(a) 1.45281435   
(b) 0.32795861   
(c) −10.51261013   
(d) 0.52681555

3. Romberg integration gives $R _ { 4 , 4 }$ as follows:

\*(a) 0.1922594  
(b) 0.1606028  
(c) −0.1768200  
(d) 0.08875528  
(e) 2.5886272  
(f) −0.7339728  
(g) 0.6362134  
(h) 0.6426991

4. Romberg integration gives $R _ { 4 , 4 }$ as follows:

(a) 1.45466031   
(b) 0.32456706   
(c) −10.52012212   
(d) 0.52659385

5. Romberg integration gives:

(a) 0.19225936 with $n = 4$ (b) 0.16060279 with $n = 5$ (c) −0.17682002 with $n = 4$ (d) 0.088755284 with $n = 5$ (e) 2.5886286 with $n = 6$ (f) −0.73396918 with $n = 6$ (g) 0.63621335 with $n = 4$ (h) 0.64269908 with $n = 5$

6. (a) $R _ { 6 , 6 } = 1 . 4 5 4 6 4 8 7 1$ , Actual Integral= 1.454648713 (b) $R _ { 7 , 7 } = 0 . 3 2 4 3 3 2 1 6$ , Actual Integral= 0.3243321549 (c) $R _ { 6 , 6 } = - 1 0 . 5 2 0 0 1 5 2 1$ , Actual Integral= −10.52001520 (d) $R _ { 6 , 6 } = 0 . 5 2 6 5 8 9 0 3$ , Actual Integral= 0.5265890342

7. $R _ { 3 3 } = 1 1 . 5 2 4 6$ \*8. $R _ { 2 1 } = 0 . 2 3 6 1$ \*9. $f ( 2 . 5 ) \approx 0 . 4 3 4 5 7$

10. $f ( 1 / 2 ) = 5 . 5$

11. $R _ { 3 1 } = 5$

12. Romberg integration gives:

(a) 62.4373714, 57.2885616, 56.4437507, 56.2630547, and 56.2187727 yields a prediction of 56.2.   
(b) 55.5722917, 56.2014707, 56.2055989, and 56.2040624 yields a prediction of 56.20.   
(c) 58.3626837, 59.0773207, 59.2688746, 59.3175220, 59.3297316, and 59.3327870 yields a prediction of 59.330.   
(d) 58.4220930, 58.4707174, 58.4704791, and 58.4704691 yields a prediction of 58.47047.   
(e) Consider the graph of the function.

\*13. We have

$$
\begin{array} { r c l } { { R _ { k , 2 } } } & { { = } } & { { \displaystyle \frac { 4 R _ { k , 1 } - R _ { k - 1 , 1 } } { 3 } = \frac { 1 } { 3 } \left[ R _ { k - 1 , 1 } + 2 h _ { k - 1 } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } } f ( a + ( i - 1 / 2 ) ) h _ { k - 1 } \right] \Bigg \} , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { 3 } \bigg [ \frac { h _ { k - 1 } } { 2 } ( f ( a ) + f ( b ) ) + h _ { k - 1 } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } - 1 } f ( a + i h _ { k - 1 } ) + 2 h _ { k - 1 } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } } f ( a + ( i - 1 / 2 ) h _ { k - 1 } ) \bigg ] , } } \end{array}
$$

Hence

$$
\begin{array} { r c l } { { R _ { k , 2 } } } & { { = } } & { { \displaystyle \frac { 1 } { 3 } \left[ h _ { k } ( f ( a ) + f ( b ) ) + 2 h _ { k } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } - 1 } f ( a + 2 i h _ { k } ) + 4 h _ { k } \sum _ { i = 1 } ^ { 2 ^ { k - 2 } } f ( a + ( 2 i - 1 ) h ) \right] } } \\ { { } } & { { = } } & { { \displaystyle \frac { h } { 3 } \left[ f ( a ) + f ( b ) + 2 \sum _ { i = 1 } ^ { M - 1 } f ( a + 2 i h ) + 4 \sum _ { i = 1 } ^ { M } f ( a + ( 2 i - 1 ) h ) \right] , } } \end{array}
$$

where $h = h _ { k }$ and $M = 2 ^ { k - 2 }$ .

14. First consider

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { 2 N - 1 } g ( i ) = g ( 1 ) + g ( 2 ) + g ( 3 ) + \cdots + g ( 2 N - 2 ) + g ( 2 N - 1 ) } } \\ { { \displaystyle \qquad = [ g ( 1 ) + g ( 3 ) + \cdots + g ( 2 N - 1 ) ] + [ g ( 2 ) + g ( 4 ) + \cdots + g ( 2 N - 2 ) ] } } \\ { { \displaystyle \qquad = \sum _ { i = 1 } ^ { N } g ( 2 i - 1 ) + \sum _ { i = 1 } ^ { N - 1 } g ( 2 i ) . } } \end{array}
$$

The result follows by setting

$$
g ( i ) = f \bigg ( a + \frac { i } { 2 } h _ { k - 1 } \bigg ) \quad \mathrm { a n d } \quad N = 2 ^ { k - 2 } .
$$

15. Equation (4.34) follows from

$$
\begin{array} { r c l } { { R _ { k , 1 } } } & { { = } } & { { \displaystyle \frac { \hbar _ { k } } { 2 } \left[ f ( \alpha ) + f ( b ) + 2 \sum _ { i = 1 } ^ { \infty - 1 } f ( \alpha + i \hbar _ { k - 1 } ) \right] } } \\ { { } } & { { } } & { { } } \\ { { = } } & { { \displaystyle \frac { \hbar _ { k } } { 2 } \left[ f ( \alpha ) + f ( b ) + 2 \sum _ { i = 1 } ^ { \infty - 1 } f ( \alpha + \frac { i } { 2 } \hbar _ { i - 1 } ) \right] } } \\ { { } } & { { } } & { { } } \\ { { = } } & { { \displaystyle \frac { \hbar _ { k } } { 2 } \left[ f ( \alpha ) + f ( b ) + 2 \sum _ { i = 1 } ^ { \infty - 1 } f ( \alpha + i \hbar _ { k - i } ) + 2 \sum _ { i = 1 } ^ { \infty } f ( \alpha + ( i - 1 / 2 ) \hbar _ { k - 1 } ) \right] } } \\ { { } } & { { } } & { { } } \\ { { = } } & { { \displaystyle \frac { 1 } { 2 } \left\{ \frac { \hbar _ { k - 1 } } { 2 } \left[ f ( \alpha ) + f ( b ) + 2 \sum _ { i = 1 } ^ { \infty - 2 } \sum _ { i = 1 } ^ { j - 1 } f ( \alpha + i \hbar _ { k - 1 } ) \right] + \hbar _ { k - 1 } \sum _ { i = 1 } ^ { \infty - 2 } f ( \alpha + ( i - 1 / 2 ) \hbar _ { k - 1 } ) \right\} } } \\ { { } } & { { } } & { { } } \\ { { = } } & { { \displaystyle \frac { 1 } { 2 } \left[ \hbar _ { k - 1 , 1 } + \hbar _ { k - 1 } \sum _ { i = 1 } ^ { \infty - 2 } f ( \alpha + ( i - 1 / 2 ) \hbar _ { k - 1 } ) \right] . } } \end{array}
$$

16. The approximation $\mathrm { e r f ( 1 ) } \approx 0 . 8 4 2 7 0 0 7 9$ is obtained using $n = 6$ .

# Exercise Set 4.6, page 227

1. Simpson’s rule gives

\*(a) $S ( 1 , 1 . 5 ) = 0 . 1 9 2 2 4 5 3 0$ , $S ( 1 , 1 . 2 5 ) = 0 . 0 3 9 3 7 2 4 3 4$ , $S ( 1 . 2 5 , 1 . 5 ) = 0 . 1 5 2 8 8 6 0 2$ , and the actual value is 0.19225935.   
(b) $S ( 0 , 1 ) = 0 . 1 6 2 4 0 1 6 8$ , $S ( 0 , 0 . 5 ) = 0 . 0 2 8 8 6 1 0 7 1$ , $S ( 0 . 5 , 1 ) = 0 . 1 3 1 8 6 1 4 0$ , and the actual value is 0.16060279.   
(c) $S ( 0 , 0 . 3 5 ) = - 0 . 1 7 6 8 2 1 5 6$ , $S ( 0 , 0 . 1 7 5 ) = - 0 . 0 8 7 7 2 4 3 8 2$ , $S ( 0 . 1 7 5 , 0 . 3 5 ) = - 0 . 0 8 9 0 9 5 7 3 6$ , and the actual value is $- 0 . 1 7 6 8 2 0 0 2$ .   
(d) $\begin{array} { r } { S ( 0 , \frac { \pi } { 4 } ) = 0 . 0 8 7 9 9 5 6 6 9 } \end{array}$ , $\begin{array} { r } { S ( 0 , \frac { \pi } { 8 } ) = 0 . 0 0 5 8 3 1 5 7 9 7 } \end{array}$ , $\begin{array} { r } { S ( \frac { \pi } { 8 } , \frac { \pi } { 4 } ) = 0 . 0 8 2 8 7 7 6 2 4 } \end{array}$ , and the actual value is 0.088755285.   
(e) $\begin{array} { r } { S ( 0 , \frac { \pi } { 4 } ) = 2 . 5 8 3 6 9 6 4 } \end{array}$ , $\begin{array} { r } { S ( 0 , \frac { \pi } { 8 } ) = 0 . 3 3 0 8 8 9 2 6 } \end{array}$ , $\begin{array} { r } { S ( \frac { \pi } { 8 } , \frac { \pi } { 4 } ) = 2 . 2 5 6 8 1 2 1 } \end{array}$ , and the actual value is 2.5886286.   
(f) $S ( 1 , 1 . 6 ) = - 0 . 7 3 9 1 0 5 3 3$ , $S ( 1 , 1 . 3 ) = - 0 . 2 6 1 4 1 2 4 4$ , $S ( 1 . 3 , 1 . 6 ) = - 0 . 4 7 3 0 5 3 5 1$ , and the actual value is $- 0 . 7 3 3 9 6 9 1 7$ .   
(g) $S ( 3 , 3 . 5 ) \ : = \ : 0 . 6 3 6 2 3 8 7 3$ , $S ( 3 , 3 . 2 5 ) \ : = \ : 0 . 3 2 5 6 7 0 9 5$ , $S ( 3 . 2 5 , 3 . 5 ) \ : = \ : 0 . 3 1 0 5 4 4 1 2$ , and the actual value is 0.63621334.   
(h) $\begin{array} { c } { { S ( 0 , { \frac { \pi } { 4 } } ) ~ = ~ 0 . 6 4 3 2 6 9 0 5 } } \end{array}$ , $\begin{array} { r } { S ( 0 , { \frac { \pi } { 8 } } ) = 0 . 3 7 3 1 5 0 0 2 } \end{array}$ , $S ( \textstyle { \frac { \pi } { 8 } } , \textstyle { \frac { \pi } { 4 } } ) \ = \ 0 . 2 6 9 5 8 2 7 0$ , and the actual value is 0.64269908.

2. Adaptive quadrature gives:

\*(a) 0.19226  
(b) 0.16072  
(c) −0.17682  
(d) 0.088709  
(e) 2.58770  
(f) −0.73447  
(g) 0.63622  
(h) 0.64273

3. Adaptive quadrature gives:

(a) 108.555281   
(b) 1724.966983   
(c) 15.306308   
(d) −18.945949

4. Adaptive quadrature gives:

<table><tr><td>Adaptive Quadrature Approximation</td><td>Actual Integral</td></tr><tr><td>(@)</td><td>2.00000103</td></tr><tr><td>(b）</td><td>2.00000000 1.37296499</td></tr><tr><td>（c）</td><td>1.372964103 0.23222150</td></tr><tr><td>(d)</td><td>5.113832671</td></tr></table>

5. Adaptive quadrature gives:

<table><tr><td></td><td>Simpson&#x27;s rule</td><td>Number evaluation</td><td>Error</td><td>Adaptive quadrature</td><td>Number evaluation</td><td>Error</td></tr><tr><td>(a)</td><td>-0.21515695</td><td>57</td><td>6.3 ×10-6</td><td>-0.21515062</td><td>229</td><td>1.0 ×10-8</td></tr><tr><td>(b）</td><td>0.95135226</td><td>83</td><td>9.6 ×10-6</td><td>0.95134257</td><td>217</td><td>1.1 × 10-7</td></tr><tr><td>（C）</td><td>-6.2831813</td><td>41</td><td>4.0 × 10-6</td><td>-6.2831852</td><td>109</td><td>1.1 × 10-7</td></tr><tr><td>(d)</td><td>5.8696024</td><td>27</td><td>2.6×10-6</td><td>5.8696044</td><td>109</td><td>4.0 × 10-9</td></tr></table>

\*6. Adaptive quadrature gives

$$
\int _ { 0 . 1 } ^ { 2 } \sin { \frac { 1 } { x } } d x \approx 1 . 1 4 5 4 \quad { \mathrm { a n d } } \quad \int _ { 0 . 1 } ^ { 2 } \cos { \frac { 1 } { x } } d x \approx 0 . 6 7 3 7 8 .
$$

7. $\int _ { 0 } ^ { 2 \pi } u ( t ) ~ d t \approx 0 . 0 0 0 0 1$

8. (a) $c _ { 1 } = - \textstyle { \frac { 1 } { 4 0 } }$ 140 , c 2 = $\begin{array} { r } { c _ { 2 } = \frac { 9 } { 6 8 0 } } \end{array}$ (b) $\int _ { 0 } ^ { 2 \pi } u ( t ) \ d t \approx - 0 . 0 2 3 4 8 1 9 4$

9. We have, for $h = b - a$

$$
\left| T ( a , b ) - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| \approx { \frac { h ^ { 3 } } { 1 6 } } \left| f ^ { \prime \prime } ( \mu ) \right|
$$

and

$$
\left| \int _ { a } ^ { b } f ( x ) \ d x - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| \approx { \frac { h ^ { 3 } } { 4 8 } } \left| f ^ { \prime \prime } ( \mu ) \right| .
$$

So

$$
\left| \int _ { a } ^ { b } f ( x ) ~ d x - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| \approx { \frac { 1 } { 3 } } \left| T ( a , b ) - T \left( a , { \frac { a + b } { 2 } } \right) - T \left( { \frac { a + b } { 2 } } , b \right) \right| .
$$

10. For $t$ between o and 1 we have the following values.

<table><tr><td>t</td><td>c(t)</td><td>s(t)</td></tr><tr><td>0.1</td><td>0.0999975</td><td>0.000523589</td></tr><tr><td>0.2</td><td>0.199921</td><td>0.00418759</td></tr><tr><td>0.3</td><td>0.299399</td><td>0.0141166</td></tr><tr><td>0.4</td><td>0.397475</td><td>0.0333568</td></tr><tr><td>0.5</td><td>0.492327</td><td>0.0647203</td></tr><tr><td>0.6</td><td>0.581061</td><td>0.110498</td></tr><tr><td>0.7</td><td>0.659650</td><td>0.172129</td></tr><tr><td>0.8</td><td>0.722844</td><td>0.249325</td></tr><tr><td>0.9</td><td>0.764972</td><td>0.339747</td></tr><tr><td>1.0</td><td>0.779880</td><td>0.438245</td></tr></table>

# Exercise Set 4.7, page 234

1. Gaussian quadrature gives:

(a) 0.1922687  
\*(b) 0.1594104  
(c) −0.1768190  
(d) 0.08926302  
(e) 2.5913247  
(f) −0.7307230  
(g) 0.6361966  
(h) 0.6423172

2. Gaussian quadrature with $n = 3$ gives:

(a) 0.1922594  
\*(b) 0.1605954  
(c) −0.1768200  
(d) 0.08875385  
(e) 2.5892580  
(f) −0.7337990  
(g) 0.6362132  
(h) 0.6427011

3. Gaussian quadrature gives:

(a) 0.1922594  
(b) 0.1606028  
(c) −0.1768200  
(d) 0.08875529  
(e) 2.5886327  
(f) −0.7339604  
(g) 0.6362133  
(h) 0.6426991

4. Gaussian quadrature with $n = 5$ gives:

(a) 0.1922594  
(b) 0.1606028  
(c) −0.1768200  
(d) 0.08875528  
(e) 2.5886286  
(f) −0.7339687  
(g) 0.6362133  
(h) 0.6426991

\*5. $a = 1$ , $b = 1$ , $c = \frac { 1 } { 3 }$ , $d = - { \frac { 1 } { 3 } }$ 6. $a = { \frac { 7 } { 1 5 } }$ , $b = { \frac { 1 6 } { 1 5 } }$ , $c = \frac { 7 } { 1 5 }$ , $d = \frac { 1 } { 1 5 }$ , e 15 1 $^ { * } 7$ . The Legendre polynomials $P _ { 2 } ( x )$ and $P _ { 3 } ( x )$ are given by

$$
P _ { 2 } ( x ) = \frac { 1 } { 2 } \left( 3 x ^ { 2 } - 1 \right) \quad \mathrm { a n d } \quad P _ { 3 } ( x ) = \frac { 1 } { 2 } \left( 5 x ^ { 3 } - 3 x \right) ,
$$

so their roots are easily verified.

For $n = 2$ ,

$$
c _ { 1 } = \int _ { - 1 } ^ { 1 } { \frac { x + 0 . 5 7 7 3 5 0 2 6 9 2 } { 1 . 1 5 4 7 0 0 5 } } ~ d x = 1
$$

and

$$
c _ { 2 } = \int _ { - 1 } ^ { 1 } { \frac { x - 0 . 5 7 7 3 5 0 2 6 9 2 } { - 1 . 1 5 4 7 0 0 5 } } ~ d x = 1 .
$$

For $n = 3$ ,

$$
c _ { 1 } = \int _ { - 1 } ^ { 1 } { \frac { x ( x + 0 . 7 7 4 5 9 6 6 6 9 2 ) } { 1 . 2 } } ~ d x = { \frac { 5 } { 9 } } ,
$$

$$
c _ { 2 } = \int _ { - 1 } ^ { 1 } { \frac { ( x + 0 . 7 7 4 5 9 6 6 6 9 2 ) ( x - 0 . 7 7 4 5 9 6 6 6 9 2 ) } { - 0 . 6 } } d x = { \frac { 8 } { 9 } } ,
$$

and

$$
c _ { 3 } = \int _ { - 1 } ^ { 1 } { \frac { x ( x - 0 . 7 7 4 5 9 6 6 6 9 2 ) } { 1 . 2 } } ~ d x = { \frac { 5 } { 9 } } .
$$

8. Let $\begin{array} { r } { P ( x ) = \prod _ { i = 1 } ^ { n } ( x - x _ { i } ) ^ { \cdot 2 } } \end{array}$ . Then $Q ( P ) = 0$ and $\textstyle \int _ { - 1 } ^ { 1 } P ( x ) \ d x \neq 0$

$^ { * } 9$ . (a) The approximations and errors using Maple’s routine with

$f : = x ^ { 2 } \cdot e x p ( x ) ; a : = - 1 ; b : = 1$ ; Quadrature(f $' ( x ) , x = a . . b , m e t h o d = g a u s s i a n | n | ,$ partition = p, output = information)

give the following approximations to the exact 10-digit value 0.878884623.

<table><tr><td>n</td><td>p</td><td>Number of Function Evaluations</td><td>Approximation</td><td>Error</td></tr><tr><td>8</td><td>1</td><td>8</td><td>0.878884623</td><td>0.0</td></tr><tr><td>4</td><td>2</td><td>8</td><td>0.878884546</td><td>8×10-8</td></tr><tr><td>2</td><td>8</td><td>8</td><td>0.878387796</td><td>5×10-4</td></tr></table>

(b) Gaussian quadrature chooses the evaluation points in an optimal way for the given interval. If the interval is partitioned it uses then uses points that are not optimal in the Gaussian sense, and less accuracy is to be expected.

# Exercise Set 4.8, page 248

1. Algorithm 4.4 with $n = m = 4$ gives:

(a) 0.3115733   
(b) 0.2552526   
\*(c) 16.50864   
(d) 1.476684

2. Algorithm 4.4 gives:

(a) 0.3115733 with $n = m = 2$ (b) 0.2552526 with $n = m = 4$ (c) 16.50864 with $n = m = 4$ (d) No result since it requires $n , m > 8 0 0$ .

3. Algorithm 4.4 with $n = 4$ and $m = 8$ , $n = 8$ and $m = 4$ , and $n = m = 6$ gives:

(a) 0.5119875, 0.5118533, 0.5118722  
(b) 1.718857, 1.718220, 1.718385  
(c) 1.001953, 1.000122, 1.000386  
(d) 0.7838542, 0.7833659, 0.7834362  
(e) −1.985611, −1.999182, −1.997353  
(f) 2.004596, 2.000879, 2.000980  
(g) 0.3084277, 0.3084562, 0.3084323  
(h) −22.61612, −19.85408, −20.14117

4. Algorithm 4.4 gives:

(a) 0.51184555 with $n = m = 1 4$ (b) 1.7182827 with $n = m = 2 0$ (c) 1.00000081 with $n = m = 2 8$ (d) 0.78333417 with $n = m = 2 0$ (e) −1.99999913 with $n = m = 4 4$ (f) 2.00000092 with $n = m = 3 4$ (g) 0.30842563 with $n = m = 1 2$ (h) −19.73920977 with $n = m = 1 4 4$

5. Algorithm 4.5 with $n = m = 2$ gives:

(a) 0.3115733   
(b) 0.2552446   
\*(c) 16.50863   
(d) 1.488875

6. Algorithm 4.5 gives:

(a) 0.3115733 with $n = m = 2$ and 4 function evaluations (b) 0.2552519 with $n = m = 3$ and 9 function evaluations (c) 16.508640 with $n = m = 3$ and 9 function evaluations (d) no result, since it requires $n , m > 5$

7. Algorithm 4.5 with $n = m = 3$ , $n = 3$ and $m = 4$ , $n = 4$ and $m = 3$ , and $n = m = 4$ gives:

(a) 0.5118655, 0.5118445, 0.5118655, 0.5118445, $2 . 1 \times 1 0 ^ { - 5 }$ , $1 . 3 \times 1 0 ^ { - 7 }$ , $2 . 1 \times 1 0 ^ { - 5 }$ , $1 . 3 \times 1 0 ^ { - 7 }$ (b) 1.718163, 1.718302, 1.718139, 1.718277, $1 . 2 \times 1 0 ^ { - 4 }$ , $2 . 0 \times 1 0 ^ { - 5 }$ , $1 . 4 \times 1 0 ^ { - 4 }$ , $4 . 8 \times 1 0 ^ { - 6 }$ (c) 1.000000, 1.000000, 1.0000000, 1.000000, 0, 0, 0, 0  
(d) 0.7833333, 0.7833333, 0.7833333, 0.7833333, 0, 0, 0, 0  
(e) $- 1 . 9 9 1 8 7 8 , - 2 . 0 0 0 1 2 4 , - 1 . 9 9 1 8 7 8 , - 2 . 0 0 0 1 2 4 , 8 . 1 \times 1 0 ^ { - 3 } , 1 . 2 \times 1 0 ^ { - 4 } , 8 . 1 \times 1 0 ^ { - 3 } , 1 . 2 \times 1 0 ^ { - 4 }$ (f) 2. $0 0 1 4 9 4 , 2 . 0 0 0 0 8 0 , 2 . 0 0 1 3 8 8 , 1 . 9 9 9 9 8 4 , 1 . 5 \times 1 0 ^ { - 3 } , 8 \times 1 0 ^ { - 5 } , 1 . 4 \times 1 0 ^ { - 3 } , 1 . 6 \times 1 0 ^ { - 5 }$ (g) 0.3084151, 0.3084145, 0.3084246, 0.3084245, $1 0 ^ { - 5 }$ , $5 . 5 \times 1 0 ^ { - 7 }$ , $1 . 1 \times 1 0 ^ { - 5 }$ , $6 . 4 \times 1 0 ^ { - 7 }$ (h) −12.74790, −21.21539, −11.83624, −20.30373, 7.0, 1.5, 7.9, 0.564

8. Algorithm 4.5 with $n = m = 5$ gives:

(a) 0.51184464, error $3 \times 1 0 ^ { - 1 0 }$ (b) 1.7182816, error $2 . 2 \times 1 0 ^ { - 7 }$ (c) 1.0000000, error 0  
(d) 0.78333333, error 0  
(e) −1.9999989, error $1 . 1 \times 1 0 ^ { - 6 }$ (f) 2.0000001, error $1 . 1 \times 1 0 ^ { - 7 }$ (g) 0.30842509, error $4 . 3 \times 1 0 ^ { - 8 }$ (h) 19.712428, error 0.0268

9. Algorithm 4.4 with $n = m = 1 4$ gives 0.1479103, and Algorithm 4.5 with $n = m = 4$ gives 0.1506823.

\*10. $\begin{array} { r } { \iint _ { R } { \sqrt { x y + y ^ { 2 } } } \ d A \approx 1 3 . 1 5 2 2 9 } \end{array}$

11. The approximation to the center of mass is $( { \overline { { x } } } , { \overline { { y } } } )$ , where $\overline { { x } } = 0 . 3 8 0 6 3 3 3$ and $\overline { { y } } = 0 . 3 8 2 2 5 5 8$ .

12. The approximation from Algorithm 4.5 with $n = m = 5$ is $\overline { { x } } = 0 . 3 8 2 0 5 4 7$ and $\overline { { y } } = 0 . 3 8 1 3 9 7 6$ .

13. The area is approximately 1.0402528.

14. The area approximation from Algorithm 4.5 is 1.0402523.

15. Algorithm 4.6 with $n = m = p = 2$ gives the first listed value. The second is the exact result.

(a) 5.204036, $e ( e ^ { 0 . 5 } - 1 ) ( e - 1 ) ^ { 2 }$ (b) 0.08429784, $\textstyle { \frac { 1 } { 1 2 } }$

(c) 0.08641975, $\textstyle { \frac { 1 } { 1 4 } }$ (d) 0.09722222, $\textstyle { \frac { 1 } { 1 2 } }$ (e) 7.103932, $2 + { \textstyle { \frac { 1 } { 2 } } } \pi ^ { 2 }$ (f) 1.428074, $\begin{array} { r } { \frac { 1 } { 2 } ( e ^ { 2 } + 1 ) - e } \end{array}$

16. Gaussian quadrature with $n = m = p = 3$ gives:

(a) 5.206442   
(b) 0.08333333   
(c) 0.07166667   
(d) 0.08333333   
(e) 6.928161   
(f) 1.474577

17. Algorithm 4.6 with $n = m = p = 4$ gives the first listed value. The second is from Algorithm 4.6 with $n = m = p = 5$ .

(a) 5.206447, 5.206447   
(b) 0.08333333,0.08333333   
(c) 0.07142857,0.07142857   
(d) 0.08333333,0.08333333   
(e) 6.934912,6.934801   
(f) 1.476207, 1.476246

18. Gaussian quadrature with $n = m = p = 4$ gives 3.0521250. The exact result is 3.0521249.

19. The approximation 20.41887 requires 125 functional evaluations.

# Exercise Set 4.9, page 254

1. The Composite Simpson’s rule gives:

\*(a) 0.5284163   
(b) 4.266654   
(c) 0.4329748   
(d) 0.8802210

2. The Composite Simpson’s Rule gives:

(a) 1.076163   
(b) 20.07458

3. The Composite Simpson’s rule gives:

\*(a) 0.4112649  
(b) 0.2440679  
(c) 0.05501681  
(d) 0.2903746

4. The Composite Simpson’s Rule gives:

\*(a) 1.1107218 with $n = 1 6$ (b) 0.58904782 with $n = 1 2$

5. The escape velocity is approximately 6.9450 mi/s.

\*6. The polynomial $L _ { n } ( x )$ has $n$ distinct zeros in $| 0 , \infty )$ . Let $x _ { 1 } , . . . , x _ { n }$ be the $n$ distinct zeros of $L _ { n }$ and define, for each $i = 1 , . . . , n$ ,

$$
c _ { n , i } = \int _ { 0 } ^ { \infty } e ^ { - x } \prod _ { j = 1 \atop j \neq i } ^ { n } { \frac { ( x - x _ { j } ) } { ( x _ { i } - x _ { j } ) } } d x .
$$

Let $P ( x )$ be any polynomial of degree $n - 1$ or less, and let $P _ { n - 1 } ( x )$ be the $( n - 1 )$ th Lagrange polynomial for $P$ on the nodes $x _ { 1 } , . . . , x _ { n }$ . As in the proof of Theorem 4.7,

$$
\int _ { 0 } ^ { \infty } P ( x ) e ^ { - x } \ d x = \int _ { 0 } ^ { \infty } P _ { n - 1 } ( x ) e ^ { - x } \ d x = \sum _ { i = 1 } ^ { n } c _ { n , i } P ( x _ { i } ) ,
$$

so the quadrature formula is exact for polynomials of degree $n - 1$ or less.

If $P ( x )$ has degree $2 n - 1$ or less, then $P ( x )$ can be divided by the $n$ th Laguerre polynomial $L _ { n } ( x )$ to obtain

$$
P ( x ) = Q ( x ) L _ { n } ( x ) + R ( x ) ,
$$

where $Q ( x )$ and $R ( x )$ are both polynomials of degree less than $n$ . As in proof of Theorem 4.7, the orthogonality of the Laguerre polynomials on $[ 0 , \infty )$ implies that

$$
Q ( x ) = \sum _ { i = 0 } ^ { n - 1 } d _ { i } L _ { i } ( x ) ,
$$

for some constants $d _ { i }$ .

Thus

$$
{ \begin{array} { r l } { \displaystyle \int _ { 0 } ^ { \infty } e ^ { - x } P ( x ) \ d x = } & { \displaystyle \int _ { 0 } \sum _ { i = 0 } ^ { \infty } d _ { i } L _ { i } ( x ) L _ { n } ( x ) e ^ { - x } \ d x + \int _ { 0 } ^ { \infty } e ^ { - x } R ( x ) \ d x } \\ & { \quad \quad = \displaystyle \sum _ { i = 0 } ^ { n - 1 } d _ { i } \int _ { 0 } ^ { \infty } L _ { i } ( x ) L _ { n } ( x ) e ^ { - x } \ d x + \sum _ { i = 1 } ^ { n } c _ { n , i } R ( x _ { i } ) } \\ & { \quad \quad = \displaystyle 0 + \sum _ { i = 1 } ^ { n } c _ { n , i } R ( x _ { i } ) = \sum _ { i = 1 } ^ { n } c _ { n , i } R ( x _ { i } ) . } \end{array} }
$$

But

$$
P ( x _ { i } ) = Q ( x _ { i } ) L _ { n } ( x _ { i } ) + R ( x _ { i } ) = 0 + R ( x _ { i } ) = R ( x _ { i } ) ,
$$

so

$$
\int _ { 0 } ^ { \infty } e ^ { - x } P ( x ) \ d x = \sum _ { i = 1 } ^ { n } c _ { n , i } P ( x _ { i } ) .
$$

Hence the quadrature formula has degree of precision $2 n - 1$ .

7. With $n = 2$ we have

$$
\int _ { 0 } ^ { \infty } e ^ { - x } f ( x ) d x \approx 0 . 8 5 3 5 5 3 4 f ( 0 . 5 8 5 7 8 6 4 ) + 0 . 1 4 6 4 4 6 6 f ( 3 . 4 1 4 2 1 3 6 ) ,
$$

and with $n = 3$ we have

$$
\int _ { 0 } ^ { \infty } e ^ { - x } f ( x ) d x \approx 0 . 7 1 1 0 9 3 0 f ( 0 . 4 1 5 7 7 4 6 ) + 0 . 2 7 8 5 1 7 7 f ( 2 . 2 9 4 2 8 0 4 ) . + 0 . 0 1 0 3 8 9 3 f ( 6 . 2 8 9 9 4 5 1 ) ^ { \prime }
$$

8. For $n = 2$ we have 0.9238795. For $n = 3$ we have 0.9064405.

9. For $n = 2$ we have 2.9865139. For $n = 3$ we have 2.9958198.

# Initial-Value Problems for Ordinary Differential Equations

Exercise Set 5.1, page 264

1. \*(a) Since $f ( t , y ) = y \cos t$ , we have ${ \frac { \partial f } { \partial y } } ( t , y ) = \cos t$ , and $f$ satisfies a Lipschitz condition in $y$ with $L = 1$ on

$$
D = \{ ( t , y ) | 0 \leq t \leq 1 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is $y ( t ) = e ^ { \sin t }$

(b) Since $f ( t , y ) = { \frac { \mathit { \omega } ^ { 2 } } { t } } y + t ^ { 2 } e ^ { t }$ , we have ${ \frac { \partial f } { \partial y } } = { \frac { 2 } { t } }$ , and $f$ satisfies a Lipschitz condition in $y$ with $L = 2$ on

$$
D = \{ ( t , y ) | 1 \leq t \leq 2 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is $y ( t ) = t ^ { 2 } ( e ^ { t } - e )$ .

(c) Since $f ( t , y ) = - \frac { 2 } { t } y + t ^ { 2 } e ^ { t }$ , we have ${ \frac { \partial f } { \partial y } } = - { \frac { 2 } { t } }$ , and $f$ satisfies a Lipschitz condition in $y$ with $L = 2$ on

$$
D = \{ ( t , y ) | 1 \leq t \leq 2 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is

$$
y ( t ) = ( t ^ { 4 } e ^ { t } - 4 t ^ { 3 } e ^ { t } + 1 2 t ^ { 2 } e ^ { t } - 2 4 t e ^ { t } + 2 4 e ^ { t } + ( \sqrt { 2 } - 9 ) e ) / t ^ { 2 } .
$$

(d) Since $f ( t , y ) = \frac { 4 t ^ { 3 } y } { 1 + t ^ { 4 } }$ we have $\frac { \partial f } { \partial y } = \frac { 4 t ^ { 3 } } { 1 + t ^ { 4 } }$ , and $f$ satisfies a Lipschitz condition in $y$ with $L = 2$ on

$$
D = \{ ( t , y ) | 0 \leq t \leq 1 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is $y ( t ) = 1 + t ^ { 4 }$ .

2. (a) Since $f ( t , y ) = e ^ { t - y }$ , we have $\frac { \partial f } { \partial y } ( t , y ) = - e ^ { t - y }$ , and $f$ does not satisfies a Lipschitz condition in $y$ o n

$$
D = \{ ( t , y ) | 0 \leq t \leq 1 , - \infty < y < \infty \} .
$$

But there is a unique solution, which is $y ( t ) = \ln ( e ^ { t } - 1 + e )$ .

(b) Since $f ( t , y ) = t ^ { - 2 } ( \sin ( 2 t ) - 2 t y )$ , we have $\frac { \partial f } { \partial y } = - 2 / t$ = −2/t, and f satisfies a Lipschitz condition in $y$ with $L = 2$ on

$$
D = \{ ( t , y ) | 1 \leq t \leq 2 , - \infty < y < \infty \} .
$$

Also, $f$ is continuous on $D$ , so there exists a unique solution, which is $y ( t ) = \frac { 1 } { 2 } ( 4 + \cos 2 -$ $\cos ( 2 t ) ) t ^ { - 2 }$ .

(c) Since $f ( t , y ) = - y + t y ^ { 1 / 2 }$ , we have $\frac { \partial f } { \partial y } = - 1 + ( t / 2 ) y ^ { - 1 / 2 }$ , and $f$ does not satisfies a Lipschitz condition in $y$ on

$$
D = \{ ( t , y ) | 2 \leq t \leq 3 , - \infty < y < \infty \} .
$$

But there is a unique solution, which is $y ( t ) = \left( t - 2 + \sqrt { 2 } e ^ { 1 - t / 2 } \right) ^ { 2 }$ .

(d) Since $f ( t , y ) = { \frac { t y + y } { t y + t } }$ , we have $\frac { \partial f } { \partial y } = \frac { t + 1 } { t ( y + 1 ) ^ { 2 } }$ and $f$ does not satisfies a Lipschitz condition in $y$ o n

$$
D = \{ ( t , y ) | 2 \leq 4 \leq 1 , - \infty < y < \infty \} .
$$

But there is a unique solution, which is implicitly given by $y ( t ) - t - 2 = \ln ( 2 t / y ( t ) )$

3. (a) Lipschitz constant $L = 1$ ; it is a well-posed problem. (b) Lipschitz constant $L = 1$ ; it is a well-posed problem. (c) Lipschitz constant $L = 1$ ; it is a well-posed problem. (d) The function $f$ does not satisfy a Lipschitz condition, so Theorem 5.6 cannot be used.

4. (a) The function $f$ does not satisfy a Lipschitz condition, so Theorem 5.6 cannot be used. (b) Lipschitz constant $L = 1$ ; it is a well-posed problem. (c) Lipschitz constant $L = 1$ ; it is a well-posed problem. (d) The function $f$ does not satisfy a Lipschitz condition, so Theorem 5.6 cannot be used.

5. $^ { * } ( \mathrm { a } )$ Differentiating

$$
y ^ { 3 } t + y t = 2 \quad { \mathrm { g i v e s } } \quad 3 y ^ { 2 } y ^ { \prime } t + y ^ { 3 } + y ^ { \prime } t + y = 0 .
$$

Solving for $y ^ { \prime }$ gives the original differential equation, and setting $t = 1$ and $y = 1$ verifies the initial condition. To approximate $y ( 2 )$ , use Newton’s method to solve the equation $y ^ { 3 } + y - 1 = 0$ . This gives $y ( 2 ) \approx 0 . 6 8 2 3 2 7 8$ .

(b) Differentiating

$$
y \sin t + t ^ { 2 } e ^ { y } + 2 y - 1 = 0 \quad { \mathrm { g i v e s } } \quad y ^ { \prime } \sin t + y \cos t + 2 t e ^ { y } + t ^ { 2 } e ^ { y } y ^ { \prime } + 2 y ^ { \prime } = 0 .
$$

Solving for $y ^ { \prime }$ gives the original differential equation, and setting $t = 1$ and $y = 0$ verifies the initial condition. To approximate $y ( 2 )$ , use Newton’s method to solve the equation $( 2 + \sin 2 ) y + 4 e ^ { y } - 1 = 0$ . This gives $y ( 2 ) \approx - 0 . 4 9 4 6 5 9 9$ .

$^ { * } 6$ . Let $( t , y _ { 1 } )$ and $( t , y _ { 2 } )$ be in $D$ . Holding $t$ fixed, define $g ( y ) = f ( t , y )$ . Suppose $y _ { 1 } < y _ { 2 }$ . Since the line joining $( t , y _ { 1 } )$ to $( t , y _ { 2 } )$ lies in $D$ and $f$ is continuous on $D$ , we have $g \in C [ y _ { 1 } , y _ { 2 } ]$ .

Further, g′(y) = ∂f (t, y) . Using the Mean Value Theorem on g, a number ξ, for y1 < ξ < y2, ∂y   
exists with

$$
g ( y _ { 2 } ) - g ( y _ { 1 } ) = g ^ { \prime } ( \xi ) ( y _ { 2 } - y _ { 1 } ) .
$$

Thus

$$
f ( t , y _ { 2 } ) - f ( t , y _ { 1 } ) = \frac { \partial f ( t , \xi ) } { \partial y } ( y _ { 2 } - y _ { 1 } )
$$

and

$$
| f ( t , y _ { 2 } ) - f ( t , y _ { 1 } ) | \leq L \left| y _ { 2 } - y _ { 1 } \right| .
$$

The proof is similar if $y _ { 2 } < y _ { 1 }$ . Therefore, $f$ satisfies a Lipschitz condition on $D$ in the variable $y$ with Lipschitz constant $L$ .

7. Let $( t _ { 1 } , y _ { 1 } )$ and $( t _ { 2 } , y _ { 2 } )$ be in $D$ , with $a \leq t _ { 1 } \leq b$ , $a \leq t _ { 2 } \leq b$ , $- \infty < y _ { 1 } < \infty$ , and $- \infty < y _ { 2 } <$ $\infty$ .

For $0 \leq \lambda \leq 1$ , we have

$$
( 1 - \lambda ) a \leq ( 1 - \lambda ) t _ { 1 } \leq ( 1 - \lambda ) b \quad \mathrm { a n d } \quad \lambda a \leq \lambda t _ { 2 } \leq \lambda b .
$$

Hence

$$
a = ( 1 - \lambda ) a + \lambda a \leq ( 1 - \lambda ) t _ { 1 } + \lambda t _ { 2 } \leq ( 1 - \lambda ) b + \lambda b = b .
$$

Also, $- \infty < ( 1 - \lambda ) y _ { 1 } + \lambda y _ { 2 } < \infty$ , so $D$ is convex.

8. (a) Since $y ( t ) = 1 - e ^ { - t }$ , we have

$$
z ( t ) = 1 - e ^ { - t } + \delta \left( t - 1 + e ^ { - t } \right) + \varepsilon _ { 0 } e ^ { - t } \quad \mathrm { a n d } \quad | y ( t ) - z ( t ) | \leq 2 | \delta | + | \varepsilon _ { 0 } | < 3 \varepsilon ,
$$

so the problem is well posed.

(b) Since $y ( t ) = - t - 1$ , we have

$$
z ( t ) = - t - 1 + \delta \left( - t - 1 + e ^ { t } \right) + \varepsilon _ { 0 } e ^ { t } \quad \mathrm { a n d } \quad | y ( t ) - z ( t ) | \leq 4 . 4 | \delta | + 7 . 4 | \varepsilon _ { 0 } | < 1 1 . 8 \varepsilon ,
$$

so the problem is well posed.

(c) Since $y ( t ) = t ^ { 2 } \left( e ^ { t } - e \right)$ , we have

$$
z ( t ) = t ^ { 2 } \left( e ^ { t } - e \right) + t ^ { 2 } \left( \varepsilon _ { 0 } + \delta \ln t \right) \quad \mathrm { a n d } \quad | y ( t ) - z ( t ) | \le 4 ( | \varepsilon _ { 0 } | + \ln 2 | \delta | ) < 6 . 8 \varepsilon ,
$$

so the problem is well posed.

(d) Since

$$
y ( t ) = \frac { t ^ { 4 } e ^ { t } - 4 t ^ { 3 } e ^ { t } + 1 2 t ^ { 2 } e ^ { t } - 2 4 t e ^ { t } + 2 4 e ^ { t } } { t ^ { 2 } } + \frac { \left( \sqrt { 2 } - 9 \right) e } { t ^ { 2 } } ,
$$

we have

$$
z ( t ) = { \frac { t ^ { 4 } e ^ { t } - 4 t ^ { 3 } e ^ { t } + 1 2 t ^ { 2 } e ^ { t } - 2 4 t e ^ { t } + 2 4 e ^ { t } } { t ^ { 2 } } } + { \frac { \left( { \sqrt { 2 } } - 9 \right) e } { t ^ { 2 } } } + { \frac { 1 } { 4 } } \delta t ^ { 2 } + { \frac { \varepsilon _ { 0 } - \delta / 4 } { t ^ { 2 } } }
$$

and

$$
| y ( t ) - z ( t ) | \leq | \delta | + | \varepsilon _ { 0 } | + | \delta | / 4 < 2 . 2 5 \varepsilon ,
$$

so the problem is well posed.

$^ { * } 9$ . (a) Since $y ^ { \prime } = f ( t , y ( t ) )$ , we have

$$
\int _ { a } ^ { t } y ^ { \prime } ( z ) \ d z = \int _ { a } ^ { t } f ( z , y ( z ) ) \ d z .
$$

So

$$
y ( t ) - y ( a ) = \int _ { a } ^ { t } f ( z , y ( z ) ) \ d z
$$

and

$$
y ( t ) = \alpha + \int _ { a } ^ { t } f ( z , y ( z ) ) \ d z .
$$

The iterative method follows from this equation.

(b) We have

$$
y _ { 0 } ( t ) = 1 , y _ { 1 } ( t ) = 1 + { \frac { 1 } { 2 } } t ^ { 2 } , y _ { 2 } ( t ) = 1 + { \frac { 1 } { 2 } } t ^ { 2 } - { \frac { 1 } { 6 } } t ^ { 3 } , \mathrm { a n d } y _ { 3 } ( t ) = 1 + { \frac { 1 } { 2 } } t ^ { 2 } - { \frac { 1 } { 6 } } t ^ { 3 } + { \frac { 1 } { 2 4 } } t ^ { 4 } .
$$

(c) We have

$$
y ( t ) = 1 + \frac { 1 } { 2 } t ^ { 2 } - \frac { 1 } { 6 } t ^ { 3 } + \frac { 1 } { 2 4 } t ^ { 4 } - \frac { 1 } { 1 2 0 } t ^ { 5 } + \cdots .
$$

# Exercise Set 5.2, page 273

1. Euler’s method gives the approximations in the following tables.

<table><tr><td rowspan="7">*(a)</td><td colspan="3">y(ti)</td></tr><tr><td>i</td><td>ti</td><td>Wi</td></tr><tr><td>1 2</td><td>0.500</td><td>0.0000000 0.2836165</td></tr><tr><td>1.000</td><td>1.1204223</td><td>3.2190993</td></tr></table>

<table><tr><td colspan="4"></td></tr><tr><td rowspan="3">(b) i</td><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>2.500</td><td>2.0000000</td><td>1.8333333</td></tr><tr><td>2</td><td>3.000</td><td>2.6250000</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="4">C</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.250</td><td>2.7500000</td><td>2.7789294</td></tr><tr><td>2</td><td>1.500</td><td>3.5500000</td><td>3.6081977</td></tr><tr><td>3</td><td>1.750</td><td>4.3916667</td><td>4.4793276</td></tr><tr><td>4</td><td>2.000</td><td>5.2690476</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Wi 1.2500000</td><td>y(ti) 1.3291498</td></tr><tr><td>1 2</td><td>0.250 0.500</td><td>1.6398053</td><td>1.7304898</td></tr><tr><td>3</td><td>0.750</td><td>2.0242547</td><td>2.0414720</td></tr><tr><td>4</td><td>1.000</td><td>2.2364573</td><td>2.1179795</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

2. Euler’s method gives the approximations in the following tables.

<table><tr><td rowspan="3">(a)</td><td></td></tr><tr><td>ti Wi</td></tr><tr><td>0.5 1.183939721</td></tr><tr><td>1.0</td><td>1.436252216</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td></td></tr><tr><td>Wi</td></tr><tr><td>1.5 2.333333333</td></tr><tr><td>2.0</td><td>2.708333333</td></tr><tr><td rowspan="3">(c)</td><td></td></tr><tr><td>ti Wi</td></tr><tr><td>2.25 2.207106781</td></tr><tr><td>2.50</td><td>2.490998908</td></tr><tr><td>2.75</td><td>2.854680348</td></tr><tr><td>3.00</td><td>3.302596464</td></tr></table>

<table><tr><td rowspan="3">(d) ti</td><td></td></tr><tr><td>Wi</td></tr><tr><td></td></tr><tr><td>1.25</td><td>1.227324357</td></tr><tr><td>1.50</td><td>0.8321501572</td></tr><tr><td>1.75</td><td>0.5704467722</td></tr><tr><td>2.00</td><td>0.3788266146</td></tr></table>

3. The actual errors and error bounds for the approximations in Exercise 1 are given in the following tables.

<table><tr><td colspan="4">*(a)</td></tr><tr><td>t</td><td>Actual error</td><td>Error bound</td><td></td></tr><tr><td>0.5</td><td></td><td>0.2836165</td><td>11.3938</td></tr><tr><td>1.0</td><td>2.0986771</td><td></td><td>42.3654</td></tr></table>

<table><tr><td colspan="2">(b)</td><td colspan="2"></td></tr><tr><td rowspan="3"></td><td>Actual</td><td>error</td><td>Error rbound</td></tr><tr><td>t</td><td></td><td></td></tr><tr><td>2.5 3.0</td><td>0.166667 0.125000</td><td>0.429570 1.59726</td></tr></table>

<table><tr><td colspan="4">(c)</td></tr><tr><td>t</td><td>Actual</td><td>error Error</td><td>bound</td></tr><tr><td></td><td>1.25</td><td>0.0289294</td><td>0.0355032</td></tr><tr><td>1.50</td><td></td><td>0.0581977</td><td>0.0810902</td></tr><tr><td></td><td>1.75</td><td>0.0876610</td><td>0.139625</td></tr><tr><td></td><td>2.00</td><td>0.117247</td><td>0.214785</td></tr></table>

<table><tr><td colspan="2">(d)</td></tr><tr><td>t</td><td>Actual error</td></tr><tr><td>0.25</td><td>0.0791498</td></tr><tr><td>0.50</td><td>0.0906844</td></tr><tr><td>0.75</td><td>0.0172174</td></tr><tr><td>1.00</td><td>0.118478</td></tr></table>

For Part (d), error bound formula (5.10) cannot be applied since $L = 0$ .

4. The actual errors and error bounds for the approximations in Exercise 1 are given in the following tables.

<table><tr><td>(a) ti</td><td>lwi-y(ti)l</td><td>Error bound</td></tr><tr><td>0.5 1.0</td><td>0.030083340 0.053627909</td><td>0.06651369683 0.3254413801</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td colspan="2"></td></tr><tr><td>|wi-y(ti)l</td><td>Error bound</td></tr><tr><td>1.5</td><td>0.020768633 0.02518894623</td></tr><tr><td>2.0</td><td>0.033324054</td><td>0.05494617010</td></tr></table>

<table><tr><td colspan="2">C</td><td colspan="2">Error bound</td></tr><tr><td>ti 2.25</td><td></td><td>lwi-y(ti)l 0.037014328</td><td>0.04985076072</td></tr><tr><td>2.50</td><td></td><td>0.073453039</td><td>0.1100812516</td></tr><tr><td>2.75</td><td></td><td>0.110513485</td><td>0.1828526997</td></tr><tr><td></td><td>3.00</td><td>0.148690185</td><td>0.2707763338</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2">Error bound</td></tr><tr><td>ti</td><td></td><td>lwi-y(ti)l</td><td></td></tr><tr><td>1.25 1.50</td><td></td><td>0.175874613 0.1842599898</td><td>0.3053253946 0.8087218666</td></tr><tr><td>1.75</td><td></td><td>0.1675629993</td><td>1.638682338</td></tr><tr><td>2.00</td><td></td><td>0.1508604834</td><td>3.007055822</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

5. Euler’s method gives the approximations in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2</td><td>1.200</td><td>1.0082645</td><td>1.0149523</td></tr><tr><td>4 6</td><td>1.400</td><td>1.0385147 1.0784611</td><td>1.0475339 1.0884327</td></tr><tr><td>8</td><td>1.600 1.800</td><td>1.1232621</td><td>1.1336536</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>2.000</td><td>1.1706516</td><td>1.1812322</td></tr></table>

<table><tr><td rowspan="8">*(b) ti</td><td colspan="3"></td></tr><tr><td colspan="3"></td></tr><tr><td>i</td><td>Wi</td><td>y(ti) 0.4896817</td></tr><tr><td>2 4</td><td>1.400 0.4388889 1.800 1.0520380</td><td>1.1994386</td></tr><tr><td>6 2.200</td><td>1.8842608</td><td>2.2135018</td></tr><tr><td>8 2.600</td><td>3.0028372</td><td>3.6784753</td></tr><tr><td>10 3.000</td><td>4.5142774</td><td>5.8741000</td></tr><tr><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="4">C</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2</td><td>0.400</td><td>-1.6080000</td><td>-1.6200510</td></tr><tr><td>4</td><td>0.800</td><td>-1.3017370</td><td>-1.3359632</td></tr><tr><td>6</td><td>1.200</td><td>-1.1274909</td><td>-1.1663454</td></tr><tr><td>8</td><td>1.600</td><td>-1.0491191</td><td>-1.0783314</td></tr><tr><td>10</td><td>2.000</td><td>-1.0181518</td><td>-1.0359724</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="2"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2 4</td><td>0.2</td><td>0.1083333 0.1620833</td><td>0.1626265 0.2051118</td></tr><tr><td>6</td><td>0.4 0.6</td><td>0.3455208</td><td>0.3765957</td></tr><tr><td>8</td><td></td><td></td><td>0.6461052</td></tr><tr><td></td><td>0.8</td><td>0.6213802</td><td></td></tr><tr><td>10</td><td>1.0</td><td>0.9803451</td><td>1.0022460</td></tr></table>

6. Euler’s method gives the approximations in the following tables.

<table><tr><td colspan="4">(a) 0.2</td></tr><tr><td></td><td>i</td><td>ti</td><td>Wi</td></tr><tr><td colspan="4">2</td></tr><tr><td colspan="2">3</td><td>0.3</td><td>1.513709064</td></tr><tr><td colspan="2">9 10</td><td>0.9 1.0</td><td>1.631412128 1.579669485</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td></td><td>Wi</td></tr><tr><td>3</td><td>2</td><td>1.2</td><td>-1.253297013</td></tr><tr><td></td><td>1.3</td><td></td><td>-1.181899131</td></tr><tr><td>9</td><td>1.9</td><td></td><td>-0.9150285539</td></tr><tr><td>10</td><td>2.0</td><td></td><td>-0.8861569244</td></tr></table>

<table><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td rowspan="2"></td></tr><tr><td>5</td><td>2.0</td><td>-1.248872291</td></tr><tr><td>6</td><td></td><td>2.2</td><td>-1.217791320</td></tr><tr><td>8</td><td>2.6</td><td></td><td>-1.174414016</td></tr><tr><td>9</td><td>2.8</td><td></td><td>-1.158657534</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td></tr><tr><td>5</td><td>0.5</td><td>1.255609618</td></tr><tr><td>6</td><td>0.6</td><td>1.352114314</td></tr><tr><td>9</td><td>0.9</td><td>1.624904878</td></tr><tr><td>10</td><td>1.0</td><td>1.700214869</td></tr></table>

7. The actual errors for the approximations in Exercise 3 are in the following tables.

<table><tr><td rowspan="3">(a)</td><td></td></tr><tr><td>t Actual error</td></tr><tr><td>1.2</td></tr><tr><td>1.5</td><td>0.0066879 0.0095942</td></tr><tr><td>1.7</td><td>0.0102229</td></tr><tr><td>2.0</td><td>0.0105806</td></tr><tr><td></td><td></td></tr></table>

<table><tr><td rowspan=1 colspan=1>*(b)</td><td rowspan=1 colspan=1>t   Actual error</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.4   0.0507928</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0    0.2240306</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.4    0.4742818</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0    1.3598226</td></tr></table>

<table><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>t   Actualerror</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.4   0.0120510</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0    0.0391546</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.4    0.0349030</td></tr><tr><td rowspan=1 colspan=2>2.0    0.0178206</td></tr></table>

<table><tr><td rowspan="3">(d)</td><td></td></tr><tr><td></td></tr><tr><td>t Actual error</td></tr><tr><td>0.2</td><td>0.0542931</td></tr><tr><td>0.5 0.7</td><td>0.0363200</td></tr><tr><td></td><td>0.0273054</td></tr><tr><td>1.0</td><td>0.0219009</td></tr></table>

8. The actual errors for the approximations in Exercise 5 are in the following tables.

<table><tr><td rowspan="3">(a)</td><td></td></tr><tr><td>t Actual error</td></tr><tr><td>0.2</td></tr><tr><td rowspan="4">0.3 1.0</td><td>0.028103580</td></tr><tr><td>0.045819156</td></tr><tr><td>0.9 0.084450802</td></tr><tr><td>0.079669485</td></tr></table>

<table><tr><td rowspan="4">(b)</td><td></td></tr><tr><td>Actual error</td></tr><tr><td>t</td></tr><tr><td>1.2 0.015002391</td></tr><tr><td>1.3</td><td>0.018712043</td></tr><tr><td>1.9</td><td>0.0241936829</td></tr><tr><td>2.0</td><td>0.0240823020</td></tr></table>

<table><tr><td rowspan=1 colspan=1>C)</td><td rowspan=1 colspan=1>t   Actual error</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0  0.084461042</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.2  0.076326327</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.6  0.0636812222.8  0.058733770</td></tr></table>

<table><tr><td rowspan=1 colspan=1>(d)</td><td rowspan=1 colspan=1>t   Actualerror</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.5  0.034195658</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6  0.028816902</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.9  0.007708304</td></tr><tr><td rowspan=1 colspan=2>1.0  0.001655184</td></tr></table>

$^ { * } 9$ . Euler’s method gives the approximations in the following table.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.1</td><td>0.271828</td><td>0.345920</td></tr><tr><td>5</td><td>1.5</td><td>3.18744</td><td>3.96767</td></tr><tr><td>6</td><td>1.6</td><td>4.62080</td><td>5.70296</td></tr><tr><td>9</td><td>1.9</td><td>11.7480</td><td>14.3231</td></tr><tr><td>10</td><td>2.0</td><td>15.3982</td><td>18.6831</td></tr></table>

(b) Linear interpolation gives the approximations in the following table.

<table><tr><td>t</td><td>Approximation</td><td>y(t)</td><td>Error</td></tr><tr><td>1.04</td><td>0.108731</td><td>0.119986</td><td>0.01126</td></tr><tr><td>1.55</td><td>3.90412</td><td>4.78864</td><td>0.8845</td></tr><tr><td>1.97</td><td>14.3031</td><td>17.2793</td><td>2.976</td></tr></table>

(c) $h < 0 . 0 0 0 6 4$

10. (a) We have

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.05</td><td>-0.9500000</td><td>-0.9523810</td></tr><tr><td>2</td><td>1.10</td><td>-0.9045353</td><td>-0.9090909</td></tr><tr><td>11</td><td>1.55</td><td>-0.6263495</td><td>-0.6451613</td></tr><tr><td>12</td><td>1.60</td><td>-0.6049486</td><td>-0.6250000</td></tr><tr><td>19</td><td>1.95</td><td>-0.4850416</td><td>-0.5128205</td></tr><tr><td>20</td><td>2.00</td><td>-0.4712186</td><td>-0.5000000</td></tr></table>

(b) (i) $y ( 1 . 0 5 2 ) \approx - 0 . 9 4 8 1 8 1 4$ (ii) $y ( 1 . 5 5 5 ) \approx - 0 . 6 2 4 2 0 9 4$ (iii) $y ( 1 . 9 7 8 ) \approx - 0 . 4 7 7 3 0 0 7$

11. (a) Euler’s method produces the following approximation to $y ( 5 ) = 5 . 0 0 6 7 4$

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>h= 0.2</td><td rowspan=1 colspan=1>h=0.1</td><td rowspan=1 colspan=1>h=0.05</td></tr><tr><td rowspan=1 colspan=1>WN</td><td rowspan=1 colspan=1>5.00377</td><td rowspan=1 colspan=1>5.00515</td><td rowspan=1 colspan=1>5.00592</td></tr></table>

(b) $h = { \sqrt { 2 \times 1 0 ^ { - 6 } } } \approx 0 . 0 0 1 4 1 4 2 .$

$^ { * } 1 2$ . For $t > 0$ , the approximations are zero and are not adequate approximations until the solution becomes close to zero. This behavior does not violate Theorem 5.9.

13. (a) $1 . 0 2 1 9 5 7 = y ( 1 . 2 5 ) \approx 1 . 0 1 4 9 7 8$ , $1 . 1 6 4 3 9 0 = y ( 1 . 9 3 ) \approx 1 . 1 5 3 9 0 2$ \*(b) $1 . 9 2 4 9 6 2 = y ( 2 . 1 ) \approx 1 . 6 6 0 7 5 6$ , $4 . 3 9 4 1 7 0 = y ( 2 . 7 5 ) \approx 3 . 5 2 6 1 6 0$ (c) $- 1 . 1 3 8 2 7 7 = y ( 1 . 3 ) \approx - 1 . 1 0 3 6 1 8 , - 1 . 0 4 1 2 6 7 =$ $- 1 . 1 0 3 6 1 8 , - 1 . 0 4 1 2 6 7 = y ( 1 . 9 3 ) \approx - 1 . 0 2 2 2 8 3$ (d) 0.3140018 = y(0.54) ≈ 0.2828333, $0 . 8 8 6 6 3 1 8 = y ( 0 . 9 4 ) \approx 0 . 8 6 6 5 5 2 1$

14. (a) $1 . 4 1 1 7 6 4 7 0 6 = y ( 0 . 2 5 ) \approx 1 . 4 4 3 9 8 3 2 4 5 , 1 . 5 3 3 5 9 4 2 9 5 = y ( 0 . 9 3 ) \approx 1 . 6 1 5 8 8 9 3 3 5$ (b) $- 1 . 2 3 3 1 5 1 7 3 1 = y ( 1 . 2 5 ) \approx - 1 . 2 1 7 5 9 8 0 7 2$ , $- 0 . 9 3 0 2 3 0 4 6 1 4 = y ( 1 . 9 3 ) \approx - 0 . 9 0 6 3 6 7 0 6 5 0$ (c) $- 1 . 3 1 2 5 = y ( 2 . 1 0 ) \approx , - 1 . 2 3 3 3 3 1 8 0 6 - 1 . 2 2 2 2 2 2 2 2 2 = y ( 2 . 7 5 ) \approx - 1 . 1 6 2 5 9 6 6 5 4 . 9 9 9 6 9$ 4 (d) $1 . 3 2 6 1 9 6 8 5 2 = y ( 0 . 5 4 ) \approx 1 . 2 9 4 2 1 1 4 9 6 , 1 . 6 6 1 3 6 1 7 5 1 = y ( 0 . 9 4 ) \approx 1 . 6 5 5 0 2 8 8 7 4$

15. (a) h = 10−n/2 (b) The minimal error is $1 0 ^ { - n / 2 } ( e - 1 ) + 5 e 1 0 ^ { - n - 1 }$ . (c)

<table><tr><td>t</td><td>w(h = 0.1)</td><td>w(h = 0.01)</td><td>y(t)</td><td>Error (n= 8)</td></tr><tr><td>0.5</td><td>0.40951</td><td>0.39499</td><td>0.39347</td><td>1.5 ×10-4</td></tr><tr><td>1.0</td><td>0.65132</td><td>0.63397</td><td>0.63212</td><td>3.1 ×10-4</td></tr></table>

16. We have

<table><tr><td>j</td><td>tj</td></tr><tr><td></td><td>Wj</td></tr><tr><td>20 2</td><td>0.702938</td></tr><tr><td>40 4</td><td>-0.0457793</td></tr><tr><td>60 6</td><td>0.294870</td></tr><tr><td>80 8</td><td>0.341673</td></tr><tr><td>100 10</td><td>0.139432</td></tr></table>

17. (b) $w _ { 5 0 } = 0 . 1 0 4 3 0 \approx p ( 5 0 )$ (c) Since $p ( t ) = 1 - 0 . 9 9 e ^ { - 0 . 0 0 2 t }$ , $p ( 5 0 ) = 0 . 1 0 4 2 1$ .

# Exercise Set 5.3, page 281

1. Taylor’s method of order two gives the approximations in the following tables.

<table><tr><td rowspan="3">*(a)</td><td>ti Wi</td><td>y(ti)</td></tr><tr><td>0.50 0.12500000</td><td>0.28361652</td></tr><tr><td>1.00 2.02323897</td><td>3.21909932</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td></td></tr><tr><td>2.50 1.75000000 3.00 2.42578125</td><td>1.83333333 2.50000000</td></tr></table>

<table><tr><td colspan="2">C ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>1.25</td><td>2.78125000</td><td>2.77892944</td></tr><tr><td></td><td>1.50</td><td>3.61250000</td><td>3.60819766</td></tr><tr><td></td><td>1.75</td><td>4.48541667</td><td>4.47932763</td></tr><tr><td></td><td>2.00</td><td>5.39404762</td><td>5.38629436</td></tr></table>

<table><tr><td colspan="2">(d) ti</td><td></td><td>y(ti)</td></tr><tr><td>0.25</td><td></td><td>1.34375000</td><td>1.32914981</td></tr><tr><td></td><td>0.50</td><td>1.77218707</td><td>1.73048976</td></tr><tr><td></td><td>0.75</td><td>2.11067606</td><td>2.04147203</td></tr><tr><td>1.00</td><td></td><td>2.20164395</td><td>2.11797955</td></tr></table>

2. Taylor’s method of order two gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.50</td><td>1.2130077</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4893295</td><td>1.4898801</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2437184</td><td>2.2441211</td></tr><tr><td>2.50</td><td>2.5634054</td><td>2.5644519</td></tr><tr><td>2.75</td><td>2.9633902</td><td>2.9651394</td></tr><tr><td>3.00</td><td>3.4486992</td><td>3.4512866</td></tr></table>

<table><tr><td rowspan="3">(b) ti 1.50</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.3564815</td><td>2.3541020</td></tr><tr><td>2.00 2.7454763</td><td>2.7416574</td></tr></table>

<table><tr><td rowspan="2">ti</td><td colspan="2">Wi y(ti)</td></tr><tr><td></td><td>1.4031990</td></tr><tr><td>1.25 1.50</td><td>1.4626530 1.0785177</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.79184185</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.574516240</td><td>0.52968710</td></tr></table>

3. Taylor’s method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">*(a)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td colspan="2">0.50</td><td>0.25781250</td><td>0.28361652 3.21909932</td></tr></table>

<table><tr><td colspan="2">(b)</td><td colspan="2"></td></tr><tr><td rowspan="2"></td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.50</td><td>1.81250000</td><td>1.83333333</td></tr><tr><td></td><td>3.00</td><td>2.48591644</td><td>2.50000000</td></tr></table>

<table><tr><td colspan="3">ti Wi</td><td rowspan="2">y(ti)</td></tr><tr><td colspan="3">C</td></tr><tr><td></td><td>1.25</td><td>2.77897135</td><td>2.77892944</td></tr><tr><td></td><td>1.50</td><td>3.60826562</td><td>3.60819766</td></tr><tr><td></td><td>1.75</td><td>4.47941561</td><td>4.47932763</td></tr><tr><td></td><td>2.00</td><td>5.38639966</td><td>5.38629436</td></tr></table>

<table><tr><td colspan="4">(d)</td></tr><tr><td></td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>0.25</td><td>1.32893880</td><td>1.32914981</td></tr><tr><td></td><td>0.50</td><td>1.72966730</td><td>1.73048976</td></tr><tr><td></td><td>0.75</td><td>2.03993417</td><td>2.04147203</td></tr><tr><td></td><td>1.00</td><td>2.11598847</td><td>2.11797955</td></tr></table>

4. Taylor’s method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a) ti</td><td>y(ti)</td></tr><tr><td>0.50</td><td>Wi 1.2140485</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4898968</td><td>1.4898801</td></tr></table>

<table><tr><td colspan="2">(b) ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.50</td><td></td><td>2.3541059</td><td>2.3541020</td></tr><tr><td></td><td>2.00</td><td>2.7416702</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2441297</td><td>2.2441211</td></tr><tr><td>2.50</td><td>2.5644662</td><td>2.5644519</td></tr><tr><td>2.75</td><td>2.9652116</td><td>2.9651394</td></tr><tr><td>3.00</td><td>3.4513065</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.4090648</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0217897</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.74234451</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.53314083</td><td>0.52968710</td></tr></table>

5. Taylor’s method of order two gives the approximations in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td></td><td colspan="3">Order 2</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1 2</td><td>1.1 1.2</td><td>1.214999 1.465250</td><td>1.215886 1.467570</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td colspan="4">Order 2</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>0.5</td><td>0.5000000</td><td>0.5158868</td></tr><tr><td>2</td><td>1.0</td><td>1.076858</td><td>1.091818</td></tr></table>

<table><tr><td colspan="4">*（c)</td></tr><tr><td></td><td colspan="3">Order 2</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1 2</td><td>1.5</td><td>-2.000000</td><td>-1.500000</td></tr><tr><td></td><td>2.0</td><td>-1.777776</td><td>-1.333333</td></tr><tr><td>3</td><td>2.5</td><td>-1.585732</td><td>-1.250000</td></tr><tr><td>4</td><td>3.0</td><td>-1.458882</td><td>-1.200000</td></tr></table>

<table><tr><td colspan="4">(d)</td></tr><tr><td>i</td><td>ti</td><td>Order 2 Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>0.25</td><td>1.093750</td><td>1.087088</td></tr><tr><td>2</td><td>0.50</td><td>1.312319</td><td>1.289805</td></tr><tr><td>3</td><td>0.75</td><td>1.538468</td><td>1.513490</td></tr><tr><td>4</td><td>1.0</td><td>1.720480</td><td>1.701870</td></tr></table>

6. Taylor’s method of order two gives the approximations in the following tables.

<table><tr><td rowspan="2">(a)</td><td colspan="3"></td></tr><tr><td></td><td></td></tr><tr><td>i 2</td><td>ti</td><td>Wi 1.3492187</td></tr><tr><td>4</td><td>0.2</td><td>1.5546191</td></tr><tr><td>6</td><td>0.4</td><td>1.6184028</td></tr><tr><td></td><td>0.6</td><td>1.5840995</td></tr><tr><td>8</td><td>0.8</td><td></td></tr><tr><td>10</td><td>1.0</td><td>1.4976289</td></tr></table>

<table><tr><td colspan="2">(b)</td></tr><tr><td>i ti</td><td>Wi</td></tr><tr><td>2</td><td>1.2 -1.2697379</td></tr><tr><td>4</td><td>1.4 −1.1441477</td></tr><tr><td>6</td><td>1.6 -1.0485714</td></tr><tr><td>8</td><td>1.8 -0.97321601</td></tr><tr><td>10 2.0</td><td>-0.91214217</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">i ti</td></tr><tr><td>2 1.4</td><td>Wi -1.6024604</td></tr><tr><td>4</td><td>1.8 -1.4206863</td></tr><tr><td>6</td><td>2.2</td></tr><tr><td></td><td>-1.3217746 -1.2601896</td></tr><tr><td>8</td><td>2.6 -1.2182831</td></tr><tr><td colspan="2">10 3.0</td></tr></table>

<table><tr><td colspan="2">(d)</td></tr><tr><td colspan="2">i ti Wi</td></tr><tr><td>2 0.2</td><td>1.0581740</td></tr><tr><td>4 0.4</td><td>1.2044189</td></tr><tr><td>6</td><td>1.3846529</td></tr><tr><td>0.6 8 0.8</td><td>1.5584034</td></tr><tr><td>10 1.0</td><td>1.7043395</td></tr></table>

7. Taylor’s method of order four gives the approximations in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td>i</td><td>ti</td><td>Order 4 Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.1</td><td>1.215883</td><td>1.215886</td></tr><tr><td>2</td><td>1.2</td><td>1.467561</td><td>1.467570</td></tr></table>

<table><tr><td colspan="4">*（c)</td></tr><tr><td>i</td><td>ti</td><td>Order 4 Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.5</td><td>-2.000000</td><td>-1.500000</td></tr><tr><td>2</td><td>2.0</td><td>-1.679012</td><td>-1.333333</td></tr><tr><td>3</td><td>2.5</td><td>-1.484493</td><td>-1.250000</td></tr><tr><td>4</td><td>3.0</td><td>−1.374440</td><td>−1.200000</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Order 4 Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>0.5</td><td>0.5156250</td><td>0.5158868</td></tr><tr><td>2</td><td>1.0</td><td>1.091267</td><td>1.091818</td></tr></table>

<table><tr><td colspan="4">(d) Order 4</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>0.25</td><td>1.086426</td><td>1.087088</td></tr><tr><td>2</td><td>0.50</td><td>1.288245</td><td>1.289805</td></tr><tr><td>3</td><td>0.75</td><td>1.512576</td><td>1.513490</td></tr><tr><td>4</td><td>1.0</td><td>1.701494</td><td>1.701870</td></tr></table>

8. Taylor’s method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td></tr><tr><td colspan="2">i</td></tr><tr><td>ti 2 0.2</td><td>Wi</td></tr><tr><td>4</td><td>1.3461270 0.4 1.5517144</td></tr><tr><td>6</td><td>0.6 1.6176616</td></tr><tr><td>8 0.8</td><td>1.5853873</td></tr><tr><td>10 1.0</td><td>1.5000175</td></tr></table>

<table><tr><td colspan="1" rowspan="1">(b)</td><td colspan="1" rowspan="1">i    ti         Wi</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">2   1.2   -1.2683126</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">4   1.4   -1.1422607</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">6   1.6   -1.0465749</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">8   1.8  -0.97124644</td></tr><tr><td colspan="2" rowspan="1">10 2.0  -0.91025180</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">i</td></tr><tr><td>ti 1.4</td><td>Wi</td></tr><tr><td>2 4</td><td>-1.5618034 1.8 -1.3887436</td></tr><tr><td>6</td><td>2.2 -1.2971040</td></tr><tr><td>8 2.6</td><td>-1.2404156</td></tr><tr><td>10 3.0</td><td>-1.2018912</td></tr></table>

<table><tr><td colspan="2">(d)</td></tr><tr><td colspan="2">i ti</td></tr><tr><td>2 0.2</td><td>Wi</td></tr><tr><td>4 0.4</td><td>1.0571619 1.2014475</td></tr><tr><td>6</td><td>1.3809015</td></tr><tr><td>0.6 8 0.8</td><td>1.5550142</td></tr><tr><td>10 1.0</td><td>1.7018616</td></tr></table>

\*9. (a) Taylor’s method of order two gives the results in the following table.

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.1</td><td>0.3397852</td><td>0.3459199</td></tr><tr><td>5</td><td>1.5</td><td>3.910985</td><td>3.967666</td></tr><tr><td>6</td><td>1.6</td><td>5.643081</td><td>5.720962</td></tr><tr><td>9</td><td>1.9</td><td>14.15268</td><td>14.32308</td></tr><tr><td>10</td><td>2.0</td><td>18.46999</td><td>18.68310</td></tr></table>

(b) Linear interpolation gives

$y ( 1 . 0 4 ) \approx 0 . 1 3 5 9 1 3 9 , \quad y ( 1 . 5 5 ) \approx 4 . 7 7 7 0 3 3 \quad \mathrm { a n d } \quad y ( 1 . 9 7 ) \approx 1 7 . 1 7 4 8 0 .$

Actual values are

$$
y ( 1 . 0 4 ) = 0 . 1 1 9 9 8 7 5 , \quad y ( 1 . 5 5 ) = 4 . 7 8 8 6 3 5 \quad \mathrm { a n d } \quad y ( 1 . 9 7 ) = 1 7 . 2 7 9 3 0 .
$$

(c) Taylor’s method of order four gives the results in the following table.

<table><tr><td>i ti</td><td>Wi</td></tr><tr><td>1</td><td>1.1 0.3459127</td></tr><tr><td>5</td><td>1.5 3.967603</td></tr><tr><td>6</td><td>5.720875</td></tr><tr><td>9</td><td>1.6 1.9 14.32290</td></tr><tr><td>10</td><td>2.0 18.68287</td></tr></table>

(d) Cubic Hermite interpolation gives

$$
y ( 1 . 0 4 ) \approx 0 . 1 1 9 9 7 0 4 , \quad y ( 1 . 5 5 ) \approx 4 . 7 8 8 5 2 7 , \quad \mathrm { a n d } \quad y ( 1 . 9 7 ) \approx 1 7 . 2 7 9 0 4 .
$$

10. (a) Taylor’s method of order two gives the results in the following table.

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.05</td><td>-0.9525000</td><td>-0.9523810</td></tr><tr><td>2</td><td>1.10</td><td>-0.9093138</td><td>-0.9090909</td></tr><tr><td>11</td><td>1.55</td><td>-0.6459788</td><td>-0.6451613</td></tr><tr><td>12</td><td>1.60</td><td>-0.6258649</td><td>-0.6250000</td></tr><tr><td>19</td><td>1.95</td><td>-0.5139781</td><td>-0.5128205</td></tr><tr><td>20</td><td>2.00</td><td>-0.5011957</td><td>-0.5000000</td></tr></table>

(b) Linear interpolation gives

$y ( 1 . 0 5 2 ) \approx - 0 . 9 5 0 7 7 2 6 , \quad y ( 1 . 5 5 5 ) \approx - 0 . 6 4 3 9 6 7 4 ,$ and $y ( 1 . 9 7 8 ) \approx - 0 . 5 0 6 8 1 9 9$

Actual values are

y(1.052) = −0.9505703, $y ( 1 . 5 5 5 ) = - 0 . 6 4 3 0 8 6 8$ , and $y ( 1 . 9 7 8 ) = - 0 . 5 0 5 5 6 1 2$

(c) Taylor’s method of order four gives the results in the following table.

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1</td><td>1.05</td><td>-0.9523813</td><td>-0.9523810</td></tr><tr><td>2</td><td>1.10</td><td>-0.9090914</td><td>-0.9090909</td></tr><tr><td>11</td><td>1.55</td><td>-0.6451629</td><td>-0.6451613</td></tr><tr><td>12</td><td>1.60</td><td>-0.6250017</td><td>-0.6250000</td></tr><tr><td>19</td><td>1.95</td><td>-0.5128226</td><td>-0.5128205</td></tr><tr><td>20</td><td>2.00</td><td>-0.5000022</td><td>-0.5000000</td></tr></table>

(d) Cubic Hermite interpolation gives

y(1.052) ≈ −0.9505706, y(1.555) ≈ −0.6430884, and $y ( 1 . 9 7 8 ) \approx - 0 . 5 0 5 5 6 3 3$

11. (a) The approximations for the velocity are in the following table.

<table><tr><td>i</td><td>ti</td><td>Order 2</td><td>Order 4</td></tr><tr><td>2</td><td>0.2</td><td>5.86595</td><td>5.86433</td></tr><tr><td>5</td><td>0.5</td><td>2.82145</td><td>2.81789</td></tr><tr><td>7</td><td>0.7</td><td>0.84926</td><td>0.84455</td></tr><tr><td>10</td><td>1.0</td><td>-2.08606</td><td>-2.09015</td></tr></table>

(b) The maximum height occurs at approximately 0.8 s.

12. Taylor’s method of order two gives the following:

<table><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>0.5</td><td>0.5146389</td></tr><tr><td>5 10</td><td>1.0</td><td>1.249305</td></tr><tr><td>15</td><td>1.5</td><td>2.152599</td></tr><tr><td>20</td><td>2.0</td><td>2.095185</td></tr></table>

# Exercise Set 5.4, page 291

1. The Modified Euler method gives the approximations in the following tables.

<table><tr><td rowspan="3">(a) t</td><td colspan="2"></td></tr><tr><td>Modified Euler</td><td>y(t)</td></tr><tr><td>0.5</td><td>0.5602111 0.2836165</td></tr><tr><td>1.0</td><td>5.3014898</td><td>3.2190993</td></tr></table>

<table><tr><td rowspan="3">(b) t</td><td colspan="2"></td></tr><tr><td>Modified Euler</td><td>y(t)</td></tr><tr><td>2.5</td><td>1.8125000</td></tr><tr><td>3.0</td><td>2.4815531</td><td>1.8333333 2.5000000</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3"></td></tr><tr><td>t</td><td>Modified Euler</td><td>y(t)</td></tr><tr><td>1.25 1.50</td><td>2.7750000</td><td>2.7789294 3.6081977</td></tr><tr><td>1.75</td><td>3.6008333 4.4688294</td><td>4.4793276</td></tr><tr><td>2.00</td><td>5.3728586</td><td></td></tr><tr><td></td><td></td><td>5.3862944</td></tr></table>

<table><tr><td rowspan="2">t</td><td colspan="2"></td></tr><tr><td>Modified Euler</td><td>y(t)</td></tr><tr><td>0.25</td><td>1.3199027</td><td>1.3291498</td></tr><tr><td>0.50</td><td>1.7070300</td><td>1.7304898</td></tr><tr><td>0.75</td><td>2.0053560</td><td>2.0414720</td></tr><tr><td>1.00</td><td>2.0770789</td><td>2.1179795</td></tr></table>

2. The Modified Euler method gives the approximations in the following tables.

<table><tr><td rowspan="3">(a) ti</td><td></td><td></td></tr><tr><td>Wi</td><td>y(ti)</td></tr><tr><td>0.50 1.2181261 1.00 1.4975545</td><td>1.2140231 1.4898801</td></tr></table>

<table><tr><td colspan="2">(b) ti Wi</td><td></td><td>y(ti)</td></tr><tr><td>1.50</td><td></td><td>2.3541667</td><td>2.3541020</td></tr><tr><td>2.00</td><td></td><td>2.7417451</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="2">(c) ti Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2454995</td><td>2.2441211</td></tr><tr><td>2.50</td><td>2.5671560</td><td>2.5644519</td></tr><tr><td>2.75</td><td>2.9691945</td><td>2.9651938</td></tr><tr><td>3.00</td><td>3.4565684</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="2">(d) ti Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.4160751</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0310111</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.75226668</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.54324500</td><td>0.52968710</td></tr></table>

3. The Modified Euler method gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Modified Euler Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td></td><td>1.0147137</td><td>1.0149523</td></tr><tr><td></td><td>1.5</td><td>1.0669093</td><td>1.0672624</td></tr><tr><td>1.7</td><td></td><td>1.1102751</td><td>1.1106551</td></tr><tr><td>2.0</td><td></td><td></td><td>1.1812322</td></tr><tr><td></td><td></td><td>1.1808345</td><td></td></tr></table>

<table><tr><td colspan="2">(b)</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td colspan="2">Modified Euler</td></tr><tr><td rowspan="2"></td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td colspan="2"></td><td></td></tr><tr><td>2.0</td><td>1.4</td><td>0.4850495 1.6384229</td><td>0.4896817 1.6612818</td></tr><tr><td>2.4</td><td></td><td>2.8250651</td><td>2.8765514</td></tr><tr><td>3.0</td><td></td><td>5.7075699</td><td>5.8741000</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3">Modified Euler</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.4</td><td>-1.6229206</td><td>-1.6200510</td></tr><tr><td>1.0</td><td>-1.2442903</td><td>-1.2384058</td></tr><tr><td>1.4</td><td>-1.1200763</td><td>-1.1146484</td></tr><tr><td>2.0</td><td>-1.0391938</td><td>-1.0359724</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3">Modified Euler</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.1742708</td><td>0.1626265</td></tr><tr><td>0.5</td><td>0.2878200</td><td>0.2773617</td></tr><tr><td>0.7</td><td>0.5088359</td><td>0.5000658</td></tr><tr><td>1.0</td><td>1.0096377</td><td>1.0022460</td></tr></table>

4. The Modified Euler method gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>ti</td><td>Modified Euler Wi</td><td>y(ti)</td></tr><tr><td>0.5</td><td>1.597265955</td><td>1.6</td></tr><tr><td>0.6</td><td>1.615015699</td><td>1.617647059</td></tr><tr><td>0.9</td><td>1.545108042</td><td>1.546961326</td></tr><tr><td>1.0</td><td>1.498430678</td><td>1.5</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3">Modified Euler</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.1</td><td>-1.347996027</td><td>-1.347822707</td></tr><tr><td>1.2</td><td>-1.268565970</td><td>-1.268299404</td></tr><tr><td>1.9</td><td>-0.9395411781</td><td>-0.9392222368</td></tr><tr><td>2.0</td><td>-0.9105471247</td><td>-0.9102392264</td></tr></table>

<table><tr><td></td><td colspan="4"></td><td></td></tr><tr><td>ti</td><td>Modified Euler Wi</td><td>y(ti)</td><td>ti</td><td>Modified Euler Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>-1.72</td><td>-1.714285714</td><td>0.5</td><td>1.289770701</td><td>1.289805276</td></tr><tr><td>1.4</td><td>-1.561272503</td><td>-1.555555556</td><td>0.6</td><td>1.380583709</td><td>1.380931216</td></tr><tr><td>2.8</td><td>-1.219717333</td><td>-1.217391304</td><td>0.9</td><td>1.631230851</td><td>1.632613182</td></tr><tr><td>3.0</td><td>-1.202119310</td><td>-1.2</td><td>1.0</td><td>1.700210296</td><td>1.701870053</td></tr></table>

5. The Midpoint method gives the approximations in the following tables.

<table><tr><td colspan="2">(a) t</td><td>y(t)</td></tr><tr><td></td><td>Midpoint 0.2646250</td><td></td></tr><tr><td>0.5 1.0</td><td>3.1300023</td><td>0.2836165 3.2190993</td></tr></table>

<table><tr><td rowspan="3">(b) t</td><td colspan="2"></td></tr><tr><td>Midpoint</td><td>y(t)</td></tr><tr><td>2.5 1.7812500</td><td>1.8333333</td></tr><tr><td>3.0</td><td>2.4550638</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="2">C</td><td></td></tr><tr><td rowspan="3">t</td><td>Midpoint</td><td>y(t)</td></tr><tr><td>1.25 2.7777778</td><td>2.7789294</td></tr><tr><td>3.6060606</td><td>3.6081977</td></tr><tr><td>1.50 1.75</td><td>4.4763015</td><td>4.4793276</td></tr><tr><td>2.00</td><td>5.3824398</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="2"></td><td></td></tr><tr><td>t</td><td>Midpoint</td><td>y(t)</td></tr><tr><td>0.25</td><td>1.3337962</td><td>1.3291498</td></tr><tr><td>0.50</td><td>1.7422854</td><td>1.7304898</td></tr><tr><td>0.75</td><td>2.0596374</td><td>2.0414720</td></tr><tr><td>1.00</td><td>2.1385560</td><td>2.1179795</td></tr></table>

6. The Midpoint method gives the approximations in the following tables.

<table><tr><td rowspan="3">(a) ti</td><td></td><td></td></tr><tr><td>Wi</td><td>y(ti)</td></tr><tr><td>0.50 1.2154305</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4932390</td><td>1.4898801</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2446171</td><td>2.2441211</td></tr><tr><td>2.50</td><td>2.562980</td><td>2.5644519</td></tr><tr><td>2.75</td><td>2.9663178</td><td>2.9651938</td></tr><tr><td>3.00</td><td>3.4526648</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="2">(b) ti Wi</td><td></td><td>y(ti)</td></tr><tr><td>1.50</td><td></td><td>2.3552632</td><td>2.3541020</td></tr><tr><td>2.00</td><td></td><td>2.7435126</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.4365103</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0516739</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.76935826</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.55667863</td><td>0.52968710</td></tr></table>

7. The Midpoint method gives the approximations in the following tables.

<table><tr><td colspan="4">(a) Midpoint</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">ti</td></tr><tr><td colspan="4">1.2</td></tr><tr><td colspan="4">1.5</td></tr><tr><td colspan="2">1.7</td><td>1.0677427 1.1111478</td><td>1.0672624 1.1106551</td></tr><tr><td colspan="4">2.0 1.1817275</td></tr></table>

<table><tr><td colspan="2">*（b) Midpoint ti</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>1.4</td><td>0.4861770</td><td>0.4896817</td></tr><tr><td></td><td>2.0</td><td>1.6438889</td><td>1.6612818</td></tr><tr><td></td><td>2.4</td><td>2.8364357</td><td>2.8765514</td></tr><tr><td></td><td>3.0</td><td>5.7386475</td><td>5.8741000</td></tr></table>

<table><tr><td rowspan="7">C ti 0.4</td><td></td></tr><tr><td>Midpoint Wi y(ti)</td></tr><tr><td></td></tr><tr><td>-1.6192966 -1.6200510</td></tr><tr><td>-1.2402470 -1.2384058</td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>1.0</td><td></td></tr><tr><td>1.4 -1.1175165</td><td>-1.1146484</td></tr><tr><td>2.0 -1.0382227</td><td>-1.0359724</td></tr></table>

<table><tr><td colspan="2">(d) Midpoint</td><td></td></tr><tr><td colspan="3">ti Wi</td></tr><tr><td>0.2</td><td></td><td>y(ti)</td></tr><tr><td>0.5</td><td>0.1722396 0.2848046</td><td>0.1626265 0.2773617</td></tr><tr><td>0.7</td><td>0.5056268</td><td>0.5000658</td></tr><tr><td></td><td></td><td></td></tr><tr><td>1.0</td><td>1.0063347</td><td>1.0022460</td></tr></table>

8. The Midpoint method gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td colspan="2"></td></tr><tr><td>ti</td><td></td><td>Midpoint Wi</td><td>y(ti)</td></tr><tr><td></td><td>0.5</td><td>1.599403030</td><td>1.6</td></tr><tr><td></td><td>0.6</td><td>1.616526285</td><td>1.617647059</td></tr><tr><td></td><td>0.9</td><td>1.544954509</td><td>1.546961326</td></tr><tr><td></td><td>1.0</td><td>1.497941308</td><td>1.5</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td colspan="3">Midpoint</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.1</td><td>-1.348356626</td><td>-1.347822707</td></tr><tr><td>1.2</td><td>-1.269137742</td><td>-1.268299404</td></tr><tr><td>1.9</td><td>-0.9403364427</td><td>-0.9392222368</td></tr><tr><td>2.0</td><td>-0.9113264950</td><td>-0.9102392264</td></tr></table>

<table><tr><td colspan="2">(c)</td></tr><tr><td colspan="2">Midpoint</td></tr><tr><td>ti</td><td>Wi y(ti)</td></tr><tr><td>1.2</td><td>-1.738181818 -1.714285714</td></tr><tr><td>1.4 -1.579759806</td><td>-1.555555556</td></tr><tr><td>2.8</td><td>-1.227670824 -1.217391304</td></tr><tr><td>3.0</td><td>-1.209389666 -1.2</td></tr></table>

<table><tr><td colspan="2">(d)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Midpoint Wi</td><td>y(ti)</td></tr><tr><td colspan="2">0.5</td><td>1.291506468</td><td>1.289805276</td></tr><tr><td colspan="2">0.6</td><td>1.382581697</td><td>1.380931216</td></tr><tr><td colspan="2">0.9</td><td>1.633368805</td><td>1.632613182</td></tr><tr><td colspan="2">1.0</td><td>1.702247783</td><td>1.701870053</td></tr></table>

9. Heun’s method gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.50</td><td>0.2710885</td><td>0.2836165</td></tr><tr><td>1.00</td><td>3.1327255</td><td>3.2190993</td></tr></table>

<table><tr><td colspan="3">（b)</td></tr><tr><td colspan="3"></td></tr><tr><td colspan="3">Heun</td></tr><tr><td rowspan="2">ti</td><td></td><td>y(ti)</td></tr><tr><td>Wi</td><td></td></tr><tr><td>2.50</td><td>1.8464828</td><td>1.8333333</td></tr><tr><td>3.00</td><td>2.5094123</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>2.7788462</td><td>2.7789294</td></tr><tr><td>1.50</td><td>3.6080529</td><td>3.6081977</td></tr><tr><td>1.75</td><td>4.4791319</td><td>4.4793276</td></tr><tr><td>2.00</td><td>5.3860533</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3"></td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.25</td><td>1.3295717</td><td>1.3291498</td></tr><tr><td>0.50</td><td>1.7310350</td><td>1.7304898</td></tr><tr><td>0.75</td><td>2.0417476</td><td>2.0414720</td></tr><tr><td>1.00</td><td>2.1176975</td><td>2.1179795</td></tr></table>

10. Heun’s method gives the approximations in the following tables.

<table><tr><td colspan="2">(a) ti</td><td>y(ti)</td></tr><tr><td>0.50</td><td>Wi 1.2139924</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4897542</td><td>1.4898801</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td colspan="2"></td></tr><tr><td>Wi</td><td>y(ti)</td></tr><tr><td>1.50</td><td>2.3540516 2.3541020</td></tr><tr><td>2.00</td><td>2.7415759</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25 2.50</td><td>2.2441050 2.5644270</td><td>2.2441211 2.5644520</td></tr><tr><td>2.75</td><td>2.9651642</td><td>2.9651938</td></tr><tr><td>3.00</td><td>3.4512546</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="3">d</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.3981322</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0114609</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.7338609</td><td>0.7380098</td></tr><tr><td>2.00</td><td>0.5262880</td><td>0.5296871</td></tr></table>

11. Heun’s method gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>1.0149305</td><td>1.0149523</td></tr><tr><td>1.5</td><td>1.0672363</td><td>1.0672624</td></tr><tr><td>1.7</td><td>1.1106289</td><td>1.1106551</td></tr><tr><td>2.0</td><td>1.1812064</td><td>1.1812322</td></tr></table>

<table><tr><td colspan="3">*(b)</td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Heun Wi</td><td>y(ti)</td></tr><tr><td>1.4</td><td>0.4895074</td><td>0.4896817</td></tr><tr><td>2.0</td><td>1.6602954</td><td>1.6612818</td></tr><tr><td>2.4</td><td>2.8741491</td><td>2.8765514</td></tr><tr><td>3.0</td><td>5.8652189</td><td>5.8741000</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.4</td><td>-1.6201023</td><td>-1.6200510</td></tr><tr><td>1.0</td><td>-1.2383500</td><td>-1.2384058</td></tr><tr><td>1.4</td><td>-1.1144745</td><td>-1.1146484</td></tr><tr><td>2.0</td><td>-1.0357989</td><td>-1.0359724</td></tr></table>

<table><tr><td colspan="4">(d)</td></tr><tr><td colspan="4">Heun</td></tr><tr><td rowspan="5"></td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.1614497</td><td>0.1626265</td></tr><tr><td>0.5</td><td>0.2765100</td><td>0.2773617</td></tr><tr><td>0.7</td><td>0.4994538</td><td></td></tr><tr><td>1.0</td><td>1.0018114</td><td>0.5000658 1.0022460</td></tr></table>

12. Heun’s method gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Heun Wi</td><td>y(ti)</td></tr><tr><td colspan="2">0.5</td><td>1.599939902</td><td>1.6</td></tr><tr><td colspan="2">0.6</td><td>1.617600330</td><td>1.617647059</td></tr><tr><td colspan="2">0.9</td><td>1.546961530</td><td>1.546961326</td></tr><tr><td colspan="2">1.0</td><td>1.500010266</td><td>1.5</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Heun Wi</td><td>y(ti)</td></tr><tr><td>1.1</td><td>-1.347797247</td><td>-1.347822707</td></tr><tr><td>1.2</td><td>-1.268261121</td><td>-1.268299404</td></tr><tr><td>1.9</td><td>-0.9391794862</td><td>-0.9392222368</td></tr><tr><td>2.0</td><td>-0.9101980983</td><td>-0.9102392264</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3">Heun</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>-1.710175817</td><td>-1.714285714</td></tr><tr><td>1.4</td><td>-1.551807512</td><td>-1.555555556</td></tr><tr><td>2.8</td><td>-1.216030469</td><td>-1.217391304</td></tr><tr><td>3.0</td><td>-1.198763172</td><td>-1.2</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Heun Wi</td><td>y(ti)</td></tr><tr><td>0.5</td><td>1.289772720</td><td>1.289805276</td></tr><tr><td>0.6</td><td>1.380888251</td><td>1.380931216</td></tr><tr><td>0.9</td><td>1.632584856</td><td>1.632613182</td></tr><tr><td></td><td></td><td></td></tr><tr><td>1.0</td><td>1.701855837</td><td>1.701870053</td></tr></table>

13. The Runge-Kutta method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Runge-Kutta Wi</td><td>y（(ti)</td></tr><tr><td colspan="2">0.5</td><td>0.2969975</td><td>0.2836165</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td colspan="4">Runge-Kutta</td></tr><tr><td>ti</td><td></td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.5</td><td></td><td>1.8333234</td><td>1.8333333</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>3.0</td><td></td><td>2.4999712</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>2.7789095</td><td>2.7789294</td></tr><tr><td>1.50</td><td>3.6081647</td><td>3.6081977</td></tr><tr><td>1.75</td><td>4.4792846</td><td>4.4793276</td></tr><tr><td>2.00</td><td>5.3862426</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Runge-Kutta Wi</td><td>y(ti)</td></tr><tr><td>0.25</td><td>1.3291650</td><td>1.3291498</td></tr><tr><td>0.50</td><td>1.7305336</td><td>1.7304898</td></tr><tr><td>0.75</td><td>2.0415436</td><td>2.0414720</td></tr><tr><td>1.00</td><td>2.1180636</td><td>2.1179795</td></tr></table>

14. The Runge-Kutta method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a) ti</td><td>y(ti)</td></tr><tr><td>0.50</td><td>Wi 1.2140409</td><td>1.2140231</td></tr><tr><td>1.00</td><td>1.4899213</td><td>1.4898801</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.25</td><td>2.2441194</td><td>2.2441211</td></tr><tr><td>2.50 2.75</td><td>2.5644488 2.9651894</td><td>2.5644519 2.9651938</td></tr><tr><td>3.00</td><td>3.4512811</td><td>3.4512866</td></tr></table>

<table><tr><td colspan="2">(b) ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.50</td><td></td><td>2.3541032</td><td>2.3541020</td></tr><tr><td></td><td>2.00</td><td>2.7416591</td><td>2.7416574</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.25</td><td>1.4033566</td><td>1.4031990</td></tr><tr><td>1.50</td><td>1.0165586</td><td>1.0164101</td></tr><tr><td>1.75</td><td>0.73813168</td><td>0.73800977</td></tr><tr><td>2.00</td><td>0.52978556</td><td>0.52968710</td></tr></table>

15. The Runge-Kutta method of order four gives the approximations in the following tables.

<table><tr><td colspan="2">(a)</td><td rowspan="2">y(ti)</td></tr><tr><td>ti</td><td>Runge-Kutta Wi</td></tr><tr><td>1.2</td><td>1.0149520</td><td>1.0149523</td></tr><tr><td>1.5</td><td>1.0672620</td><td>1.0672624</td></tr><tr><td>1.7</td><td>1.1106547</td><td>1.1106551</td></tr><tr><td>2.0</td><td>1.1812319</td><td>1.1812322</td></tr></table>

<table><tr><td colspan="2">*(b)</td><td colspan="2"></td></tr><tr><td colspan="2">ti</td><td>Runge-Kutta Wi</td><td>y(ti)</td></tr><tr><td></td><td></td><td>0.4896842</td><td>0.4896817</td></tr><tr><td></td><td>1.4 2.0</td><td>1.6612651</td><td>1.6612818</td></tr><tr><td></td><td>2.4</td><td>2.8764941</td><td>2.8765514</td></tr><tr><td></td><td>3.0</td><td>5.8738386</td><td>5.8741000</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="2"></td></tr><tr><td colspan="2">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi y(ti)</td></tr><tr><td>0.4</td><td>-1.6200576 -1.6200510</td></tr><tr><td>1.0 -1.2384307</td><td>-1.2384058</td></tr><tr><td>1.4 -1.1146769</td><td>-1.1146484</td></tr><tr><td>2.0</td><td>-1.0359922 -1.0359724</td></tr></table>

<table><tr><td colspan="2">(d)</td><td rowspan="2"></td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td></td><td>ti</td><td>Wi</td></tr><tr><td>0.2</td><td>0.1627655</td><td>0.1626265</td></tr><tr><td>0.5</td><td>0.2774767</td><td>0.2773617</td></tr><tr><td>0.7</td><td>0.5001579</td><td>0.5000658</td></tr><tr><td>1.0</td><td>1.0023207</td><td>1.0022460</td></tr></table>

16. The Runge-Kutta method gives the approximations in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.5</td><td>1.599998664</td><td>1.6</td></tr><tr><td>0.6</td><td>1.617645445</td><td>1.617647059</td></tr><tr><td>0.9</td><td>1.546959536</td><td>1.546961326</td></tr><tr><td>1.0</td><td>1.499998299</td><td>1.5</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.1</td><td>-1.347822676</td><td>-1.347822707</td></tr><tr><td>1.2</td><td>-1.268299357</td><td>-1.268299404</td></tr><tr><td>1.9</td><td>-0.9392221816</td><td>-0.9392222368</td></tr><tr><td>2.0</td><td>-0.9102391733</td><td>-0.9102392264</td></tr></table>

<table><tr><td colspan="3">C</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>-1.714245180</td><td>-1.714285714</td></tr><tr><td>1.4</td><td>-1.555522884</td><td>-1.555555556</td></tr><tr><td>2.8</td><td>-1.217380872</td><td>-1.217391304</td></tr><tr><td>3.0</td><td>-1.199990539</td><td>-1.2</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td colspan="3">Runge-Kutta</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.5</td><td>1.289807149</td><td>1.289805276</td></tr><tr><td>0.6</td><td>1.380932547</td><td>1.380931216</td></tr><tr><td>0.9</td><td>1.632611867</td><td>1.632613182</td></tr><tr><td>1.0</td><td>1.701867708</td><td>1.701870053</td></tr></table>

17. Linear interpolation gives the following results.

(a) $1 . 0 2 2 1 1 6 7 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9$ , $1 . 1 6 4 0 3 4 7 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ (b) $1 . 9 0 8 6 5 0 0 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6 , \ 4 . 3 1 0 5 9 1 3 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ (c) $- 1 . 1 4 6 1 4 3 4 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8$ , $- 1 . 0 4 5 4 8 5 4 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 2 6 6 5$ (d) $0 . 3 2 7 1 4 7 0 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8$ , $0 . 8 9 6 7 0 7 3 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

18. Linear interpolation gives the following results.

(a) $1 . 6 0 4 3 6 5 8 5 3 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8$ , $1 . 5 2 6 4 3 7 0 9 6 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 4 7 4 6 0 6 2 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1$ , $- 0 . 9 3 0 8 4 2 9 6 2 1 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4$ (c) $- 1 . 6 4 0 6 3 6 2 5 2 \approx y ( 1 . 3 ) = - 1 . 6 2 5$ , $- 1 . 2 0 8 2 7 8 6 1 8 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 6 0 9 5 9 0 4 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2$ , $1 . 6 5 8 8 2 2 6 2 9 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 1$

19. Linear interpolation gives the following results.

(a) $1 . 0 2 2 7 8 6 3 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9$ , $1 . 1 6 4 9 2 4 7 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ (b) $1 . 9 1 5 3 7 4 9 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6 , ~ 4 . 3 3 1 2 9 3 9 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ (c) $- 1 . 1 4 3 2 0 7 0 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8 .$ , $- 1 . 0 4 4 3 7 4 3 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 2 6 6 5$ (d) $0 . 3 2 4 0 8 3 9 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8 , \ 0 . 8 9 3 4 1 5 2 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

20. Linear interpolation gives the following results.

(a) $1 . 6 0 5 2 5 2 3 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8$ , $1 . 5 2 6 1 4 9 2 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 5 3 7 9 3 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1$ , $- 0 . 9 3 1 6 3 3 4 6 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4$ (c) $- 1 . 6 5 8 9 7 0 8 \approx y ( 1 . 3 ) = - 1 . 6 2 5 , \ : \ : - 1 . 2 1 5 7 8 8 1 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 7 9 3 6 6 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2 .$ , $1 . 6 6 0 9 2 0 4 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 1$

21. Linear interpolation gives the following results.

(a) $1 . 0 2 2 3 5 9 8 5 0 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9$ , $1 . 1 6 4 4 0 3 7 0 6 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ (b) $1 . 8 8 0 8 4 8 0 4 9 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6$ , $4 . 4 0 8 4 2 6 1 1 5 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ (c) $- 1 . 1 4 0 3 4 6 9 5 6 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8 .$ , $- 1 . 0 4 1 8 2 0 2 5 6 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 2 6 6 5$ (d) $0 . 3 1 6 2 5 6 9 8 9 7 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8 , \ 0 . 8 8 8 6 6 1 3 4 2 6 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

22. Linear interpolation gives the following results.

(a) $1 . 6 0 7 0 0 4 0 7 3 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8 , \ 1 . 5 2 8 1 8 1 0 2 4 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 4 4 1 3 9 2 9 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1$ , $- . 9 3 0 4 8 5 0 6 9 8 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4$ (c) $- 1 . 6 3 0 9 9 1 6 6 4 \approx y ( 1 . 3 ) = - 1 . 6 2 5$ , $- 1 . 2 0 4 8 0 6 7 2 6 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 6 2 1 8 9 3 2 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2$ , $1 . 6 6 0 2 9 3 2 4 8 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 1$

23. Linear interpolation gives the following results.

(a) $1 . 0 2 2 3 8 2 6 \approx y ( 1 . 2 5 ) = 1 . 0 2 1 9 5 6 9$ , $1 . 1 6 4 4 2 9 2 \approx y ( 1 . 9 3 ) = 1 . 1 6 4 3 9 0 1$ (b) $1 . 9 3 7 3 6 7 2 \approx y ( 2 . 1 ) = 1 . 9 2 4 9 6 1 6$ , $4 . 4 1 3 4 7 4 5 \approx y ( 2 . 7 5 ) = 4 . 3 9 4 1 6 9 7$ (c) $- 1 . 1 4 0 5 2 5 2 \approx y ( 1 . 3 ) = - 1 . 1 3 8 2 7 6 8 .$ , $- 1 . 0 4 2 0 2 1 1 \approx y ( 1 . 9 3 ) = - 1 . 0 4 1 2 6 6 5$ (d) $0 . 3 1 7 1 6 5 2 6 \approx y ( 0 . 5 4 ) = 0 . 3 1 4 0 0 1 8$ , $0 . 8 8 9 1 9 7 3 0 \approx y ( 0 . 9 4 ) = 0 . 8 8 6 6 3 1 8$

24. Linear interpolation gives the following results.

(a) $1 . 6 0 7 0 5 7 3 7 6 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8$ , $1 . 5 2 8 1 7 5 0 4 1 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 4 4 5 5 2 3 8 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1$ , $- 0 . 9 3 0 5 2 7 2 7 9 1 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4$ (c) $- 1 . 6 3 4 8 8 4 0 3 2 \approx y ( 1 . 3 ) = - 1 . 6 2 5$ , $- 1 . 2 0 6 0 7 7 1 5 6 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 6 2 5 7 3 0 8 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2$ $9 6 8 5 2 , 1 . 6 6 0 3 1 4 2 0 3 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 .$ 1

25. Cubic Hermite interpolation gives the following results.

(a) $1 . 0 2 1 9 5 6 9 = y ( 1 . 2 5 ) \approx 1 . 0 2 1 9 5 5 0$ , $1 . 1 6 4 3 9 0 2 = y ( 1 . 9 3 ) \approx 1 . 1 6 4 3 8 9 8$ \*(b) $1 . 9 2 4 9 6 1 7 = y ( 2 . 1 0 ) \approx 1 . 9 2 4 9 2 1 7 ,$ $4 . 3 9 4 1 6 9 7 = y ( 2 . 7 5 ) \approx 4 . 3 9 3 9 9 4 3$ (c) $- 1 . 1 3 8 2 6 8 = y ( 1 . 3 ) \approx - 1 . 1 3 8 3 0 3 6$ , $- 1 . 0 4 1 2 6 6 6 = y ( 1 . 9 3 ) \approx - 1 . 0 4 1 2 8 6 2$ (d) $0 . 3 1 4 0 0 1 8 4 = y ( 0 . 5 4 ) \approx 0 . 3 1 4 1 0 5 7 9 , 0 . 8 8 6 6 3 1 7 6 = y ( 0 . 9 4 ) \approx 0 . 8 8 6 7 0 6 5 3$

26. Cubic Hermite interpolation gives the following results.

(a) $1 . 6 1 0 4 0 3 1 0 8 \approx y ( 0 . 5 4 ) = 1 . 6 1 0 4 0 5 6 9 8$ , $1 . 5 2 8 9 8 7 6 2 2 \approx y ( 0 . 9 4 ) = 1 . 5 2 8 9 8 7 0 4 6$ (b) $- 1 . 2 3 3 1 4 9 6 2 0 \approx y ( 1 . 2 5 ) = - 1 . 2 3 3 1 5 1 7 3 1 , \ : \ : - 0 . 9 3 0 2 3 0 2 4 7 4 \approx y ( 1 . 9 3 ) = - 0 . 9 3 0 2 3 0 4 6 1 4 7 3 . \ : ( 1 . 9 3 3 )$ (c) $- 1 . 6 2 4 8 0 6 7 4 6 \approx y ( 1 . 3 ) = - 1 . 6 2 5$ , $- 1 . 2 1 4 6 4 2 6 0 1 \approx y ( 2 . 9 3 ) = - 1 . 2 0 5 7 6 1 3 1 7$ (d) $1 . 3 2 6 1 9 5 3 9 0 \approx y ( 0 . 5 4 ) = 1 . 3 2 6 1 9 6 8 5 2 , 1 . 6 6 1 3 5 8 5 5 8 \approx y ( 0 . 9 4 ) = 1 . 6 6 1 3 6 1 7 5 1$

27. The Modified Euler method and the Midpoint method give the same results when applied to the initial-value problem

$$
y ^ { \prime } = f ( t , y ) = - y + t + 1 , \quad \mathrm { f o r } \quad 0 \leq t \leq 1 \quad \mathrm { a n d } \quad y ( 0 ) = 1
$$

with any choice of $h$ because the equation is linear in both $y$ and $t$ .

The equation for the Midpoint method has $w _ { 0 } = 1$ and

$$
\begin{array} { r l } & { w _ { i + 1 } = w _ { i } + h f ( t _ { i } + 0 . 5 h , w _ { i } + 0 . 5 h f ( t _ { i } , w _ { i } ) ) } \\ & { \qquad = w _ { i } + h f ( t _ { i } + 0 . 5 h , w _ { i } + 0 . 5 h ( - w _ { i } + t _ { i } + 1 ) ) } \\ & { \qquad = w _ { i } + h ( - w _ { i } - 0 . 5 h ( - w _ { i } + t _ { i } + 1 ) + t _ { i } + 0 . 5 h + 1 ) } \\ & { \qquad = w _ { i } ( 1 - h + 0 . 5 h ^ { 2 } ) + t _ { i } ( h - 0 . 5 h ^ { 2 } ) + h . } \end{array}
$$

The equation for the Modified Euler method has $w _ { 0 } = 1$ and

$$
\begin{array} { l } { w _ { i + 1 } = w _ { i } + 0 . 5 h \big ( f ( t _ { i } , w _ { i } ) + f ( t _ { i + 1 } , w _ { i } + h f ( t _ { i } , w _ { i } ) \big ) } \\ { \qquad = w _ { i } + 0 . 5 h \big ( - w _ { i } + t _ { i } + 1 - w _ { i } - h ( - w _ { i } + t _ { i } + 1 ) + t _ { i } + h + 1 \big ) } \\ { \qquad = w _ { i } + 0 . 5 h \big ( - w _ { i } + t _ { i } + 1 - w _ { i } - h ( - w _ { i } + t _ { i } + 1 ) + t _ { i } + h + 1 \big ) } \\ { \qquad = w _ { i } ( 1 - h + 0 . 5 h ^ { 2 } ) + t _ { i } ( h - 0 . 5 h ^ { 2 } ) + h . } \end{array}
$$

28. (a) The water level is 6.526747 ft. (b) The tank will be empty in 25 min.

29. In 0.2 seconds we have approximately 2099 units of KOH.

$^ *$ 30. Using the notation $y _ { i + 1 } = y ( t _ { i + 1 } )$ , $y _ { i } = y ( t _ { i } )$ , and $f _ { i } = f ( t _ { i } , y ( t _ { i } ) )$ , we have

$$
h \tau _ { i + 1 } = y _ { i + 1 } - y _ { i } - a _ { 1 } f _ { i } - a _ { 2 } f ( t _ { i } + \alpha _ { 2 } , y _ { i } + \delta _ { 2 } f _ { i } ) .
$$

Expanding $y _ { i + 1 }$ and $f ( t _ { i } + \alpha _ { 2 } , y _ { i } + \delta _ { 2 } f _ { i } )$ in Taylor series about $t _ { i }$ and $f ( t _ { i } , y _ { i } )$ gives

$$
\begin{array} { r l } { h \tau _ { + 1 } = ( h - a _ { 1 } - a _ { 2 } ) f _ { i } + \frac { h ^ { 2 } } { 2 } \int _ { - } ^ { t } d \sigma _ { 2 } c _ { 2 } f _ { i } ( i _ { 2 } , y _ { i } ) } \\ { - \sigma _ { 2 } \dot { \sigma } _ { 2 } f _ { i } \dot { \sigma } _ { 1 } ( i _ { 2 } , y _ { i } ) + \frac { h ^ { 3 } } { 6 } \int _ { - } ^ { t } d \sigma _ { 2 } \frac { \sigma _ { 2 } ^ { 2 } } { 2 } f _ { i } ( i _ { 4 } , y _ { i } ) } \\ { - \sigma _ { 2 } \sigma _ { 2 } \dot { \sigma } _ { 2 } f _ { i } f _ { i } ( i _ { 4 } , y _ { i } ) - a _ { 2 } \frac { \sigma _ { 2 } ^ { 2 } } { 2 } \int _ { - } ^ { t } d \sigma _ { 2 } ( i _ { 2 } , y _ { i } ) + i \cdots } \\ { = ( h - a _ { 1 } - a _ { 2 } ) f _ { i } + \bigg ( \frac { h ^ { 2 } } { 2 } - a _ { 2 } \sigma _ { 2 } \bigg ) f _ { i } ( i _ { 4 } , y _ { i } ) } \\ { + \bigg ( \frac { h ^ { 2 } } { 2 } - a _ { 2 } \dot { \sigma } _ { 2 } \bigg ) f _ { i } f _ { i } ( i _ { 4 } , y _ { i } ) + \bigg ( \frac { h ^ { 3 } } { 6 } - a _ { 2 } \frac { \sigma _ { 2 } ^ { 2 } } { 2 } \bigg ) f _ { i } ( i _ { 4 } , y _ { i } ) } \\ { + \bigg ( \frac { h ^ { 3 } } { 8 } - a _ { 2 } \sigma _ { 2 } \dot { \sigma } _ { 2 } \bigg ) f _ { i } f _ { i } \dot { \sigma } _ { 1 } ( i _ { 4 } , y _ { i } ) + \bigg ( \frac { h ^ { 3 } } { 6 } - a _ { 2 } \frac { \sigma _ { 2 } ^ { 2 } } { 2 } \bigg ) f _ { i } ^ { 2 } f _ { i } ( i _ { 4 } , y _ { i } ) } \\ { + \frac { h ^ { 3 } } { 6 } \left( f _ { i } ( i _ { 4 } , y _ { i } ) f _ { i } ( i _ { 4 } , y _ { i } ) + f _ { i } ^ { 2 } f _ { i } ^ { 2 } ( i _ { 5 } , y _ { i } ) \right) + \cdots } \end{array}
$$

Regardless of the choice of $u _ { 1 } , u _ { 2 } , \alpha _ { 2 }$ , and $\delta _ { 2 }$ , the term

$$
\frac { h ^ { 3 } } { 6 } \left[ f _ { t } ( y _ { i } , t _ { i } ) f _ { y } ( t _ { i } , y _ { i } ) + f _ { i } f _ { y } ^ { 2 } ( t _ { i } , y _ { i } ) \right]
$$

cannot be canceled.

31. The appropriate constants are

$$
\alpha _ { 1 } = \delta _ { 1 } = \alpha _ { 2 } = \delta _ { 2 } = \gamma _ { 2 } = \gamma _ { 3 } = \gamma _ { 4 } = \gamma _ { 5 } = \gamma _ { 6 } = \gamma _ { 7 } = \frac { 1 } { 2 } \quad \mathrm { a n d } \quad \alpha _ { 3 } = \delta _ { 3 } = 1 .
$$

# Exercise Set 5.5, page 300

1. The Runge-Kutta-Fehlberg Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.2093900</td><td>0.0298184</td><td>0.2093900</td><td>0.0298337</td></tr><tr><td>3</td><td>0.5610469</td><td>0.4016438</td><td>0.1777496</td><td>0.4016860</td></tr><tr><td>5</td><td>0.8387744</td><td>1.5894061</td><td>0.1280905</td><td>1.5894600</td></tr><tr><td>7</td><td>1.0000000</td><td>3.2190497</td><td>0.0486737</td><td>3.2190993</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>2.2500000</td><td>1.4499988</td><td>0.2500000</td><td>1.4500000</td></tr><tr><td>2</td><td>2.5000000</td><td>1.8333332</td><td>0.2500000</td><td>1.8333333</td></tr><tr><td>3</td><td>2.7500000</td><td>2.1785718</td><td>0.2500000</td><td>2.1785714</td></tr><tr><td>4</td><td>3.0000000</td><td>2.5000005</td><td>0.2500000</td><td>2.5000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.2500000</td><td>2.7789299</td><td>0.2500000</td><td>2.7789294</td></tr><tr><td>2</td><td>1.5000000</td><td>3.6081985</td><td>0.2500000</td><td>3.6081977</td></tr><tr><td>3</td><td>1.7500000</td><td>4.4793288</td><td>0.2500000</td><td>4.4793276</td></tr><tr><td>4</td><td>2.0000000</td><td>5.3862958</td><td>0.2500000</td><td>5.3862944</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.2500000</td><td>1.3291478</td><td>0.2500000</td><td>1.3291498</td></tr><tr><td>2</td><td>0.5000000</td><td>1.7304857</td><td>0.2500000</td><td>1.7304898</td></tr><tr><td>3</td><td>0.7500000</td><td>2.0414669</td><td>0.2500000</td><td>2.0414720</td></tr><tr><td>4</td><td>1.0000000</td><td>2.1179750</td><td>0.2500000</td><td>2.1179795</td></tr></table>

2. The Runge-Kutta-Fehlberg Algorithm gives the results in the following tables. \*(a)   

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.0500000</td><td>1.1038574</td><td>0.0500000</td><td>1.1038574</td></tr><tr><td>2</td><td>1.1000000</td><td>1.2158864</td><td>0.0500000</td><td>1.2158863</td></tr><tr><td>3</td><td>1.1500000</td><td>1.3368393</td><td>0.0500000</td><td>1.3368393</td></tr><tr><td>4</td><td>1.2000000</td><td>1.4675697</td><td>0.0500000</td><td>1.4675696</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.2500000</td><td>0.2522868</td><td>0.2500000</td><td>0.2522868</td></tr><tr><td>2</td><td>0.5000000</td><td>0.5158867</td><td>0.2500000</td><td>0.5158868</td></tr><tr><td>3</td><td>0.7500000</td><td>0.7959445</td><td>0.2500000</td><td>0.7959446</td></tr><tr><td>4</td><td>1.0000000</td><td>1.0918182</td><td>0.2500000</td><td>1.0918183</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>1.1382206</td><td>-1.7834313</td><td>0.1382206</td><td>-1.7834282</td></tr><tr><td>3</td><td>1.6364797</td><td>-1.4399709</td><td>0.3071709</td><td>-1.4399551</td></tr><tr><td>5</td><td>2.6364797</td><td>-1.2340532</td><td>0.5000000</td><td>-1.2340298</td></tr><tr><td>6</td><td>3.0000000</td><td>-1.2000195</td><td>0.3635203</td><td>-1.2000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.5000000</td><td>0.0416667</td><td>0.5000000</td><td>0.0416667</td></tr><tr><td>2</td><td>1.0000000</td><td>0.3333333</td><td>0.5000000</td><td>0.3333333</td></tr><tr><td>3</td><td>1.5000000</td><td>1.1250000</td><td>0.5000000</td><td>1.1250000</td></tr><tr><td>4</td><td>2.0000000</td><td>2.6666667</td><td>0.5000000</td><td>2.6666667</td></tr></table>

3. The Runge-Kutta-Fehlberg Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>1.1101946</td><td>1.0051237</td><td>0.1101946</td><td>1.0051237</td></tr><tr><td>5</td><td>1.7470584</td><td>1.1213948</td><td>0.2180472</td><td>1.1213947</td></tr><tr><td>7</td><td>2.3994350</td><td>1.2795396</td><td>0.3707934</td><td>1.2795395</td></tr><tr><td>11</td><td>4.0000000</td><td>1.6762393</td><td>0.1014853</td><td>1.6762391</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>4</td><td>1.5482238</td><td>0.7234123</td><td>0.1256486</td><td>0.7234119</td></tr><tr><td>7</td><td>1.8847226</td><td>1.3851234</td><td>0.1073571</td><td>1.3851226</td></tr><tr><td>10</td><td>2.1846024</td><td>2.1673514</td><td>0.0965027</td><td>2.1673499</td></tr><tr><td>16</td><td>2.6972462</td><td>4.1297939</td><td>0.0778628</td><td>4.1297904</td></tr><tr><td>21</td><td>3.0000000</td><td>5.8741059</td><td>0.0195070</td><td>5.8741000</td></tr></table>


<!-- chunk 0003: pages 141-210 -->
<table><tr><td>i</td><td>t</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.1633541</td><td>-1.8380836</td><td>0.1633541</td><td>-1.8380836</td></tr><tr><td>5</td><td>0.7585763</td><td>-1.3597623</td><td>0.1266248</td><td>-1.3597624</td></tr><tr><td>9</td><td>1.1930325</td><td>-1.1684827</td><td>0.1048224</td><td>-1.1684830</td></tr><tr><td>13</td><td>1.6229351</td><td>-1.0749509</td><td>0.1107510</td><td>-1.0749511</td></tr><tr><td>17</td><td>2.1074733</td><td>-1.0291158</td><td>0.1288897</td><td>-1.0291161</td></tr><tr><td>23</td><td>3.0000000</td><td>-1.0049450</td><td>0.1264618</td><td>-1.0049452</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.3986051</td><td>0.3108201</td><td>0.3986051</td><td>0.3108199</td></tr><tr><td>3</td><td>0.9703970</td><td>0.2221189</td><td>0.2866710</td><td>0.2221186</td></tr><tr><td>5</td><td>1.5672905</td><td>0.1133085</td><td>0.3042087</td><td>0.1133082</td></tr><tr><td>8</td><td>2.0000000</td><td>0.0543454</td><td>0.0902302</td><td>0.0543455</td></tr></table>

4. Steps 3 and 6 must use the new equations. Step 4 must now use

$$
R = \frac { 1 } { h } \bigg | - \frac { 1 } { 1 6 0 } K _ { 1 } - \frac { 1 2 5 } { 1 7 9 5 2 } K _ { 3 } + \frac { 1 } { 1 4 4 } K _ { 4 } - \frac { 1 2 } { 1 9 5 5 } K _ { 5 } - \frac { 3 } { 4 4 } K _ { 6 } + \frac { 1 2 5 } { 1 1 5 9 2 } K _ { 7 } + \frac { 4 3 } { 6 1 6 } K _ { 8 } \bigg | ,
$$

and in Step 8 we must change to $\delta = 0 . 8 7 1 ( T O L / R ) ^ { 1 / 5 }$ . Repeating Exercise 3 using the Runge-Kutta-Verner method gives the results in the following tables.

\*(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.42087564</td><td>1.05149775</td><td>0.42087564</td><td>1.05150868</td></tr><tr><td>3</td><td>2.28874724</td><td>1.25203709</td><td>0.50000000</td><td>1.25204675</td></tr><tr><td>5</td><td>3.28874724</td><td>1.50135401</td><td>0.50000000</td><td>1.50136369</td></tr><tr><td>7</td><td>4.00000000</td><td>1.67622922</td><td>0.21125276</td><td>1.67623914</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>1.27377960</td><td>0.31440170</td><td>0.27377960</td><td>0.31440111</td></tr><tr><td>4</td><td>1.93610139</td><td>1.50471956</td><td>0.20716801</td><td>1.50471717</td></tr><tr><td>7</td><td>2.48318866</td><td>3.19129592</td><td>0.17192536</td><td>3.19129017</td></tr><tr><td>11</td><td>3.00000000</td><td>5.87411325</td><td>0.05925262</td><td>5.87409998</td></tr></table>

(c)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.50000000</td><td>-1.53788271</td><td>0.50000000</td><td>-1.53788284</td></tr><tr><td>5</td><td>1.26573379</td><td>-1.14736319</td><td>0.17746598</td><td>-1.14736283</td></tr><tr><td>9</td><td>1.99742532</td><td>-1.03615509</td><td>0.19229794</td><td>-1.03615478</td></tr><tr><td>14</td><td>3.00000000</td><td>-1.00494544</td><td>0.10525374</td><td>-1.00494525</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>0.50000000</td><td>0.29875168</td><td>0.50000000</td><td>0.29875178</td></tr><tr><td>2</td><td>1.00000000</td><td>0.21662609</td><td>0.50000000</td><td>0.21662642</td></tr><tr><td>4</td><td>1.74337091</td><td>0.08624885</td><td>0.27203938</td><td>0.08624932</td></tr><tr><td>6</td><td>2.00000000</td><td>0.05434531</td><td>0.03454832</td><td>0.05434551</td></tr></table>

5. (a) The number of infectives is $y ( 3 0 ) \approx 8 0 2 9 5 . 7$ . (b) The limiting value for the number of infectives for this model is $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } y ( t ) = 1 0 0 , 0 0 0 } \end{array}$ .

6. With $T O L = 0 . 0 1$ , $H M I N = 0 . 0 1$ , $H M A X = 1$ , we have

$$
z ( 3 0 ) \approx 8 1 , \quad x ( 3 0 ) \approx 1 9 7 5 4 , \quad \mathrm { a n d } \quad y ( 3 0 ) \approx 8 0 1 6 5 .
$$

# Exercise Set 5.6, page 314

1. The Adams-Bashforth methods give the results in the following tables.

\*(a)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td></tr><tr><td>0.4</td><td>0.1200522</td><td>0.1507778</td><td>0.1507778</td><td>0.1507778</td><td>0.1507778</td></tr><tr><td>0.6</td><td>0.4153551</td><td>0.4613866</td><td>0.4960196</td><td>0.4960196</td><td>0.4960196</td></tr><tr><td>0.8</td><td>1.1462844</td><td>1.2512447</td><td>1.2961260</td><td>1.3308570</td><td>1.3308570</td></tr><tr><td>1.0</td><td>2.8241683</td><td>3.0360680</td><td>3.1461400</td><td>3.1854002</td><td>3.2190993</td></tr><tr><td>2.2</td><td>1.3666667</td><td>1.3666667</td><td>1.3666667</td><td>1.3666667</td><td>1.3666667</td></tr><tr><td>2.4</td><td>1.6750000</td><td>1.6857143</td><td>1.6857143</td><td>1.6857143</td><td>1.6857143</td></tr><tr><td>2.6</td><td>1.9632431</td><td>1.9794407</td><td>1.9750000</td><td>1.9750000</td><td>1.9750000</td></tr><tr><td>2.8</td><td>2.2323184</td><td>2.2488759</td><td>2.2423065</td><td>2.2444444</td><td>2.2444444</td></tr><tr><td>3.0</td><td>2.4884512</td><td>2.5051340</td><td>2.4980306</td><td>2.5011406</td><td>2.5000000</td></tr></table>

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>1.2</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td></tr><tr><td>1.4</td><td>3.2734823</td><td>3.2710611</td><td>3.2710611</td><td>3.2710611</td><td>3.2710611</td></tr><tr><td>1.6</td><td>3.9567107</td><td>3.9514231</td><td>3.9520058</td><td>3.9520058</td><td>3.9520058</td></tr><tr><td>1.8</td><td>4.6647738</td><td>4.6569191</td><td>4.6582078</td><td>4.6580160</td><td>4.6580160</td></tr><tr><td>2.0</td><td>5.3949416</td><td>5.3848058</td><td>5.3866452</td><td>5.3862177</td><td>5.3862944</td></tr></table>

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td></tr><tr><td>0.4</td><td>1.5986417</td><td>1.5712255</td><td>1.5712255</td><td>1.5712255</td><td>1.5712255</td></tr><tr><td>0.6</td><td>1.9386951</td><td>1.8827238</td><td>1.8750869</td><td>1.8750869</td><td>1.8750869</td></tr><tr><td>0.8</td><td>2.1766821</td><td>2.0844122</td><td>2.0698063</td><td>2.0789180</td><td>2.0789180</td></tr><tr><td>1.0</td><td>2.2369407</td><td>2.1115540</td><td>2.0998117</td><td>2.1180642</td><td>2.1179795</td></tr></table>

2. The Adams-Bashforth methods give the results in the following tables.

(a)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>1.349857812</td><td></td><td></td><td></td><td>1.346153846</td></tr><tr><td>0.4</td><td>1.556590819</td><td>1.548505437</td><td>1.551742825</td><td></td><td>1.551724138</td></tr><tr><td>0.6</td><td>1.618098483</td><td>1.613103414</td><td>1.618495896</td><td>1.618045413</td><td>1.617647059</td></tr><tr><td>0.8</td><td>1.581123788</td><td>1.581537429</td><td>1.586784646</td><td>1.585534486</td><td>1.585365854</td></tr><tr><td>1.0</td><td>1.493132968</td><td>1.497482321</td><td>1.501365685</td><td>1.499907131</td><td>1.5</td></tr></table>

(b)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>1.2</td><td>-1.270097903</td><td></td><td></td><td></td><td>-1.268299404</td></tr><tr><td>1.4</td><td>-1.145585721</td><td>-1.14555416</td><td>-1.142395930</td><td></td><td>-1.142245242</td></tr><tr><td>1.6</td><td>-1.050436722</td><td>-1.045646519</td><td>-1.046822255</td><td>-1.046486051</td><td>-1.046559939</td></tr><tr><td>1.8</td><td>-0.9752223844</td><td>-0.9702763545</td><td>-0.9715163192</td><td>-0.9711385301</td><td>-0.9712326550</td></tr><tr><td>2.0</td><td>-0.9141608282</td><td>-0.9093053788</td><td>-0.9105163922</td><td>-0.9101442242</td><td>-0.9102392264</td></tr></table>

(c)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t）</td></tr><tr><td>1.4</td><td>-1.608147341</td><td></td><td></td><td></td><td>-1.555555556</td></tr><tr><td>1.8</td><td>-1.1429612993</td><td>-1.359101590</td><td>-1.404013030</td><td></td><td>-1.384615385</td></tr><tr><td>2.2</td><td>-1.331187984</td><td>-1.269164344</td><td>-1.314903737</td><td>-1.283404253</td><td>-1.294117647</td></tr><tr><td>2.6</td><td>-1.268712599</td><td>-1.217326056</td><td>-1.253881487</td><td>-1.229097787</td><td>-1.238095238</td></tr><tr><td>3.0</td><td>-1.225776866</td><td>-1.182688385</td><td>-1.212496957</td><td>-1.192208061</td><td>－1.200000000</td></tr></table>

(d)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td> 5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>1.058717655</td><td></td><td></td><td></td><td>1.057181007</td></tr><tr><td>0.4</td><td>1.207722688</td><td>1.202476610</td><td>1.200816932</td><td></td><td>1.201486010</td></tr><tr><td>0.6</td><td>1.389363032</td><td>1.381043540</td><td>1.379947852</td><td>1.381296110</td><td>1.380931216</td></tr><tr><td>0.8</td><td>1.562852894</td><td>1.554374654</td><td>1.554384988</td><td>1.555455875</td><td>1.555031423</td></tr><tr><td>1.0</td><td>1.707692156</td><td>1.700926322</td><td>1.701562220</td><td>1.702136018</td><td>1.701870053</td></tr></table>

3. The Adams-Bashforth methods give the results in the following tables.

(a)

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>1.2</td><td>1.0161982</td><td>1.0149520</td><td>1.0149520</td><td>1.0149520</td><td>1.0149523</td></tr><tr><td>1.4</td><td>1.0497665</td><td>1.0468730</td><td>1.0477278</td><td>1.0475336</td><td>1.0475339</td></tr><tr><td>1.6</td><td>1.0910204</td><td>1.0875837</td><td>1.0887567</td><td>1.0883045</td><td>1.0884327</td></tr><tr><td>1.8</td><td>1.1363845</td><td>1.1327465</td><td>1.1340093</td><td>1.1334967</td><td>1.1336536</td></tr><tr><td>2.0</td><td>1.1840272</td><td>1.1803057</td><td>1.1815967</td><td>1.1810689</td><td>1.1812322</td></tr><tr><td>1.4</td><td>0.4867550</td><td>0.4896842</td><td>0.4896842</td><td>0.4896842</td><td>0.4896817</td></tr><tr><td>1.8</td><td>1.1856931</td><td>1.1982110</td><td>1.1990422</td><td>1.1994320</td><td>1.1994386</td></tr><tr><td>2.2</td><td>2.1753785</td><td>2.2079987</td><td>2.2117448</td><td>2.2134792</td><td>2.2135018</td></tr><tr><td>2.6</td><td>3.5849181</td><td>3.6617484</td><td>3.6733266</td><td>3.6777236</td><td>3.6784753</td></tr><tr><td>3.0</td><td>5.6491203</td><td>5.8268008</td><td>5.8589944</td><td>5.8706101</td><td>5.8741000</td></tr></table>

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.5</td><td>-1.5357010</td><td>-1.5381988</td><td>-1.5379372</td><td>-1.5378676</td><td>-1.5378828</td></tr><tr><td>1.0</td><td>-1.2374093</td><td>-1.2389605</td><td>-1.2383734</td><td>-1.2383693</td><td>-1.2384058</td></tr><tr><td>1.5</td><td>-1.0952910</td><td>-1.0950952</td><td>-1.0947925</td><td>-1.0948481</td><td>-1.0948517</td></tr><tr><td>2.0</td><td>-1.0366643</td><td>-1.0359996</td><td>-1.0359497</td><td>-1.0359760</td><td>-1.0359724</td></tr></table>

<table><tr><td>t</td><td>2-step</td><td>3-step</td><td>4-step</td><td>5-step</td><td>y(t)</td></tr><tr><td>0.2</td><td>0.1739041</td><td>0.1627655</td><td>0.1627655</td><td>0.1627655</td><td>0.1626265</td></tr><tr><td>0.4</td><td>0.2144877</td><td>0.2026399</td><td>0.2066057</td><td>0.2052405</td><td>0.2051118</td></tr><tr><td>0.6</td><td>0.3822803</td><td>0.3747011</td><td>0.3787680</td><td>0.3765206</td><td>0.3765957</td></tr><tr><td>0.8</td><td>0.6491272</td><td>0.6452640</td><td>0.6487176</td><td>0.6471458</td><td>0.6461052</td></tr><tr><td>1.0</td><td>1.0037415</td><td>1.0020894</td><td>1.0064121</td><td>1.0073348</td><td>1.0022460</td></tr></table>

4. The Adams-Moulton methods give the results in the following tables.

(1a)

<table><tr><td>ti</td><td>2-step</td><td>3-step</td><td>4-step</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td><td>0.0268128</td></tr><tr><td>0.4</td><td>0.1533627</td><td>0.1507778</td><td>0.1507778</td><td>0.1507778</td></tr><tr><td>0.6</td><td>0.5030068</td><td>0.4979042</td><td>0.4960196</td><td>0.4960196</td></tr><tr><td>0.8</td><td>1.3463142</td><td>1.3357923</td><td>1.3322919</td><td>1.3308570</td></tr><tr><td>1.0</td><td>3.2512866</td><td>3.2298092</td><td>3.2227484</td><td>3.2190993</td></tr><tr><td>1.2</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td><td>2.6187859</td></tr><tr><td>1.4</td><td>3.2711394</td><td>3.2710611</td><td>3.2710611</td><td>3.2710611</td></tr><tr><td>1.6</td><td>3.9521454</td><td>3.9519886</td><td>3.9520058</td><td>3.9520058</td></tr><tr><td>1.8</td><td>4.6582064</td><td>4.6579866</td><td>4.6580211</td><td>4.6580160</td></tr><tr><td>2.0</td><td>5.3865293</td><td>5.3862558</td><td>5.3863027</td><td>5.3862944</td></tr></table>

(1d)

<table><tr><td>ti</td><td>2-step</td><td>3-step</td><td>4-step</td><td>y(ti)</td></tr><tr><td>0.2</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td><td>1.2529306</td></tr><tr><td>0.4</td><td>1.5700866</td><td>1.5712255</td><td>1.5712255</td><td>1.5712255</td></tr><tr><td>0.6</td><td>1.8738414</td><td>1.8757546</td><td>1.8750869</td><td>1.8750869</td></tr><tr><td>0.8</td><td>2.0787117</td><td>2.0803067</td><td>2.0789471</td><td>2.0789180</td></tr><tr><td>1.0</td><td>2.1196912</td><td>2.1199024</td><td>2.1178679</td><td>2.1179795</td></tr></table>

5. Algorithm 5.4 gives the results in the following tables.

<table><tr><td rowspan="2">*（a)</td><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>0.2</td><td>0.0269059</td><td>0.0268128</td></tr><tr><td></td><td>0.4</td><td>0.1510468</td><td>0.1507778</td></tr><tr><td></td><td>0.6</td><td>0.4966479</td><td>0.4960196</td></tr><tr><td></td><td>0.8</td><td>1.3408657</td><td>1.3308570</td></tr><tr><td></td><td>1.0</td><td>3.2450881</td><td>3.2190993</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2.2</td><td>1.3666610</td><td>1.3666667</td></tr><tr><td>2.4</td><td>1.6857079</td><td>1.6857143</td></tr><tr><td>2.6</td><td>1.9749941</td><td>1.9750000</td></tr><tr><td>2.8</td><td>2.2446995</td><td>2.2444444</td></tr><tr><td>3.0</td><td>2.5003083</td><td>2.5000000</td></tr></table>

<table><tr><td colspan="3">(c)</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>1.2</td><td>2.6187787</td><td>2.6187859</td></tr><tr><td>1.4</td><td>3.2710491</td><td>3.2710611</td></tr><tr><td>1.6</td><td>3.9519900</td><td>3.9520058</td></tr><tr><td>1.8</td><td>4.6579968</td><td>4.6580160</td></tr><tr><td>2.0</td><td>5.3862715</td><td>5.3862944</td></tr></table>

<table><tr><td colspan="2">(d)</td><td>y(ti)</td></tr><tr><td>ti</td><td>Wi</td><td></td></tr><tr><td>0.2</td><td>1.2529350</td><td>1.2529306</td></tr><tr><td>0.4</td><td>1.5712383</td><td>1.5712255</td></tr><tr><td>0.6</td><td>1.8751097</td><td>1.8750869</td></tr><tr><td>0.8</td><td>2.0796618</td><td>2.0789180</td></tr><tr><td>1.0</td><td>2.1192575</td><td>2.1179795</td></tr></table>

6. Algorithm 5.4 gives the results in the following tables.

<table><tr><td rowspan="3">(a)</td><td></td></tr><tr><td></td></tr><tr><td>ti Wi</td></tr><tr><td>0.2</td><td>1.3461536</td></tr><tr><td>0.4</td><td>1.5516984</td></tr><tr><td>0.6</td><td>1.6175240</td></tr><tr><td>0.8</td><td>1.5851977</td></tr><tr><td>1.0</td><td>1.4998499</td></tr></table>

<table><tr><td rowspan="3">(b) ti</td><td></td></tr><tr><td>Wi</td></tr><tr><td></td></tr><tr><td>1.2</td><td>-1.2682994</td></tr><tr><td>1.4</td><td>-1.1422321</td></tr><tr><td>1.6</td><td>-1.0465369</td></tr><tr><td>1.8</td><td>-0.9712077</td></tr><tr><td>2.0</td><td>-0.9102149</td></tr></table>

<table><tr><td rowspan="3">C</td><td></td></tr><tr><td></td></tr><tr><td>ti Wi</td></tr><tr><td>1.2</td><td>-1.7142452</td></tr><tr><td>1.6</td><td>-1.4545197</td></tr><tr><td>2.0</td><td>-1.3312918</td></tr><tr><td>2.4</td><td>-1.2614431</td></tr><tr><td>2.8</td><td>-1.2159883</td></tr></table>

<table><tr><td colspan="2">(d)</td></tr><tr><td colspan="2"></td></tr><tr><td>ti</td><td>Wi</td></tr><tr><td>0.2</td><td>1.0571822</td></tr><tr><td>0.4</td><td>1.2015654</td></tr><tr><td>0.6</td><td>1.3810423</td></tr><tr><td>0.8</td><td>1.5550968</td></tr><tr><td>1.0</td><td>1.7018941</td></tr></table>

7. The Adams Fourth-order Predictor-Corrector Algorithm gives the results in the following tables.

<table><tr><td>(a) t</td><td>y(t) w</td></tr><tr><td>1.2 1.0149520</td><td>1.0149523</td></tr><tr><td>1.4 1.0475227</td><td>1.0475339</td></tr><tr><td>1.6 1.0884141</td><td>1.0884327</td></tr><tr><td>1.8</td><td>1.1336331 1.1336536</td></tr><tr><td>2.0 1.1812112</td><td>1.1812322</td></tr></table>

<table><tr><td colspan="3">(b)</td></tr><tr><td>t</td><td>w</td><td>y(t)</td></tr><tr><td>.4</td><td>0.4896842</td><td>0.4896817</td></tr><tr><td>1.8</td><td>1.1994245</td><td>1.1994386</td></tr><tr><td>2.2</td><td>2.2134701</td><td>2.2135018</td></tr><tr><td>2.6</td><td>3.6784144</td><td>3.6784753</td></tr><tr><td>3.0</td><td>5.8739518</td><td>5.8741000</td></tr></table>

<table><tr><td colspan="2"></td></tr><tr><td colspan="2"></td></tr><tr><td>t</td><td>w</td></tr><tr><td>0.5</td><td>-1.5378788 -1.5378828</td></tr><tr><td>1.0</td><td>-1.2384134 -1.2384058</td></tr><tr><td>1.5</td><td>-1.0948609 -1.0948517</td></tr><tr><td>2.0</td><td>-1.0359757 -1.0359724</td></tr></table>

<table><tr><td>(d) t</td><td>y(t) w</td></tr><tr><td>0.2 0.1627655</td><td>0.1626265</td></tr><tr><td>0.4 0.2048557</td><td>0.2051118</td></tr><tr><td>0.6 0.3762804</td><td>0.3765957</td></tr><tr><td>0.8 0.6458949</td><td>0.6461052</td></tr><tr><td>1.0 1.0021372</td><td>1.0022460</td></tr></table>

8. The new algorithm gives the results in the following tables.

(a)

<table><tr><td>ti</td><td>Wi(p= 2)</td><td>Wi(p = 3)</td><td>Wi(p= 4)</td><td>y(ti)</td></tr><tr><td>1.2</td><td>1.0149520</td><td>1.0149520</td><td>1.0149520</td><td>1.0149523</td></tr><tr><td>1.5</td><td>1.0672499</td><td>1.0672499</td><td>1.0672499</td><td>1.0672624</td></tr><tr><td>1.7</td><td>1.1106394</td><td>1.1106394</td><td>1.1106394</td><td>1.1106551</td></tr><tr><td>2.0</td><td>1.1812154</td><td>1.1812154</td><td>1.1812154</td><td>1.1812322</td></tr></table>

<table><tr><td>ti</td><td>Wi(p = 2)</td><td>Wi(p= 3)</td><td>wi(p = 4)</td><td>y(ti)</td></tr><tr><td>1.4</td><td>0.4896842</td><td>0.4896842</td><td>0.4896842</td><td>0.4896817</td></tr><tr><td>2.0</td><td>1.6613427</td><td>1.6613509</td><td>1.6613517</td><td>1.6612818</td></tr><tr><td>2.4</td><td>2.8767835</td><td>2.8768112</td><td>2.8768140</td><td>2.8765514</td></tr><tr><td>3.0</td><td>5.8754422</td><td>5.8756045</td><td>5.8756224</td><td>5.8741000</td></tr></table>

<table><tr><td>ti</td><td>Wi(p= 2)</td><td>wi(p = 3)</td><td>Wi(p= 4)</td><td>y(ti)</td></tr><tr><td>0.4</td><td>-1.6200494</td><td>-1.6200494</td><td>-1.6200494</td><td>-1.6200510</td></tr><tr><td>1.0</td><td>-1.2384104</td><td>-1.2384105</td><td>-1.2384105</td><td>-1.2384058</td></tr><tr><td>1.4</td><td>-1.1146533</td><td>-1.1146536</td><td>-1.1146536</td><td>-1.1146484</td></tr><tr><td>2.0</td><td>-1.0359139</td><td>-1.0359740</td><td>-1.0359740</td><td>-1.0359724</td></tr></table>

<table><tr><td>ti</td><td>Wi(p=2)</td><td>Wi(p= 3)</td><td>Wi(p= 4)</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.1627655</td><td>0.1627655</td><td>0.1627655</td><td>0.1626265</td></tr><tr><td>0.5</td><td>0.2774037</td><td>0.2773333</td><td>0.2773468</td><td>0.2773617</td></tr><tr><td>0.7</td><td>0.5000772</td><td>0.5000259</td><td>0.5000356</td><td>0.5000658</td></tr><tr><td>1.0</td><td>1.0022473</td><td>1.0022273</td><td>1.0022311</td><td>1.0022460</td></tr></table>

9. (a) With $h = 0 . 0 1$ , the three-step Adams-Moulton method gives the values in the following table.

<table><tr><td>i</td><td>ti</td></tr><tr><td>10 0.1</td><td>1.317218</td></tr><tr><td>20</td><td>0.2 1.784511</td></tr></table>

(b) Newton’s method will reduce the number of iterations per step from three to two, using the stopping criterion

$$
| w _ { i } ^ { ( k ) } - w _ { i } ^ { ( k - 1 ) } | \leq 1 0 ^ { - 6 } .
$$

10. Milne-Simpson’s Predictor-Corrector method gives the results in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>2</td><td>1.2</td><td>1.01495200</td><td>1.01495231</td></tr><tr><td>5</td><td>1.5</td><td>1.06725997</td><td>1.06726235</td></tr><tr><td>7</td><td>1.7</td><td>1.11065221</td><td>1.11065505</td></tr><tr><td>10</td><td>2.0</td><td>1.18122584</td><td>1.18123222</td></tr></table>

<table><tr><td rowspan="2">(b)</td><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td></td><td>2</td><td>1.4</td><td>0.48968417</td><td>0.48968166</td></tr><tr><td></td><td>5</td><td>2.0</td><td>1.66126150</td><td>1.66128176</td></tr><tr><td></td><td>7</td><td>2.4</td><td>2.87648763</td><td>2.87655142</td></tr><tr><td></td><td>10</td><td>3.0</td><td>5.87375555</td><td>5.87409998</td></tr></table>

<table><tr><td rowspan="2">(c)</td><td rowspan="2"></td><td colspan="6">(d)</td></tr><tr><td>Wi</td><td>y(ti)</td><td>i</td><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>5</td><td>0.5</td><td>-1.53788255</td><td>-1.53788284</td><td>2</td><td>0.2</td><td>0.16276546</td><td>0.16262648</td></tr><tr><td>10</td><td>1.0</td><td>-1.23840789</td><td>-1.23840584</td><td>5</td><td>0.5</td><td>0.27741080</td><td>0.27736167</td></tr><tr><td>15</td><td>1.5</td><td>-1.09485532</td><td>-1.09485175</td><td>7</td><td>0.7</td><td>0.50008713</td><td>0.50006579</td></tr><tr><td>20</td><td>2.0</td><td>-1.03597247</td><td>-1.03597242</td><td>10</td><td>1.0</td><td>1.00215439</td><td>1.00224598</td></tr></table>

11. $^ *$ (a) For some $\xi _ { i }$ in $( t _ { i - 1 } , t _ { i } )$ ,

$$
f ( t , y ( t _ { i } ) ) = P _ { 1 } ( t ) + \frac { f ^ { \prime \prime } ( \xi _ { i } , y ( \xi _ { i } ) ) } { 2 } ( t - t _ { i } ) ( t - t _ { i - 1 } ) ,
$$

where $P _ { 1 } ( t )$ is the linear Lagrange polynomial

$$
P _ { 1 } ( t ) = \frac { ( t - t _ { i - 1 } ) } { ( t _ { i } - t _ { i - 1 } ) } f ( t _ { i } , y ( t _ { i } ) ) + \frac { ( t - t _ { i } ) } { ( t _ { i - 1 } - t _ { i } ) } f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) .
$$

Thus

$$
\begin{array} { l } { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } P _ { 1 } ( t ) ~ d t = \frac { f ( t _ { i } , y ( t _ { i } ) ) } { t _ { i } - t _ { i - 1 } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i - 1 } ) ~ d t + \frac { f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) } { t _ { i - 1 } - t _ { i } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i } ) ~ d t } \\ { \displaystyle \qquad = \frac { 3 h } { 2 } f ( t _ { i } , y ( t _ { i } ) ) - \frac { h } { 2 } f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) . } \end{array}
$$

Since $( t - t _ { i } ) ( t - t _ { i - 1 } )$ does not change sign on $\left( { { t } _ { i } } , { { t } _ { i + 1 } } \right)$ , the Mean Value Theorem for Integrals gives

$$
\begin{array} { r l } & { \int _ { t _ { i } } ^ { t _ { i + 1 } } \frac { f ^ { \prime \prime } ( \xi _ { i } , y ( \xi _ { i } ) ) ( t - t _ { i } ) ( t - t _ { i - 1 } ) } { 2 } d t = \frac { f ^ { \prime \prime } ( \mu , y ( \mu ) ) } { 2 } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i } ) ( t - t _ { i - 1 } ) d t } \\ & { \qquad = \frac { 5 h ^ { 2 } f ^ { \prime \prime } ( \mu , y ( \mu ) ) } { 1 2 } . } \end{array}
$$

Replacing $y ( t _ { j } )$ with $w _ { j }$ , for $j = i - 1 , i$ , and $i + 1$ in the formula

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t
$$

gives

$$
w _ { i + 1 } = w _ { i } + { \frac { h \left[ 3 f ( t _ { i } , w _ { i } ) - f ( t _ { i - 1 } , w _ { i - 1 } ) \right] } { 2 } } ,
$$

and the local truncation error is

$$
\tau _ { i + 1 } ( h ) = \frac { 5 h ^ { 2 } y ^ { \prime \prime \prime } ( \mu ) } { 1 2 } ,
$$

for some $\mu$ in $( t _ { i - 1 } , t _ { i + 1 } )$

(b) Using the backward difference polynomial with $m = 4$ gives

$$
\begin{array} { l } { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t = \sum _ { k = 0 } ^ { 3 } \nabla ^ { k } f ( t _ { i } , y ( t _ { i } ) ) h ( - 1 ) ^ { k } \int _ { 0 } ^ { 1 } \left( \begin{array} { c } { - s } \\ { k } \end{array} \right) d s } \\ { \displaystyle \qquad + \frac { h ^ { 5 } } { 2 4 } \int _ { 0 } ^ { 1 } s ( s + 1 ) ( s + 2 ) ( s + 3 ) f ^ { ( 4 ) } ( \xi _ { i } , y ( \xi _ { i } ) ) \ d s . } \end{array}
$$

From Table 5.10 we have,

$$
\begin{array} { r l } { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t = h \biggl [ f ( t _ { i } , y ( t _ { i } ) ) + \frac { 1 } { 2 } \nabla f ( t _ { i } , y ( t _ { i } ) ) + \frac { 5 } { 1 2 } \nabla ^ { 2 } f ( t _ { i } , y ( t _ { i } ) ) } & { } \\ { \displaystyle } & { \qquad + \frac { 3 } { 8 } \nabla ^ { 3 } f ( t _ { i } , y ( t _ { i } ) ) \biggr ] } \\ { \displaystyle } & { \qquad + \frac { h ^ { 5 } } { 2 4 } \int _ { 0 } ^ { 1 } s ( s + 1 ) ( s + 2 ) ( s + 3 ) f ^ { ( 4 ) } ( \xi _ { i } , y ( \xi _ { i } ) ) \ d s . } \end{array}
$$

Since

$$
\begin{array} { r l } & { \nabla f ( t _ { i } , y ( t _ { i } ) ) = f ( t _ { i } , y ( t _ { i } ) ) - f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) , } \\ & { \nabla ^ { 2 } f ( t _ { i } , y ( t _ { i } ) ) = f ( t _ { i } , y ( t _ { i } ) ) - 2 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) , } \\ & { \nabla ^ { 3 } f ( t _ { i } , y ( t _ { i } ) ) = f ( t _ { i } , y ( t _ { i } ) ) - 3 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 3 f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) - f ( t _ { i - 3 } , y ( t _ { i - 3 } ) ) , } \end{array}
$$

and $s ( s + 1 ) ( s + 2 ) ( s + 3 )$ does not change sign on $( 0 , 1 )$ , we can simplify this and use the Mean Value Theorem for Integrals to obtain

$$
\begin{array} { r l } & { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t = h \biggl [ 5 5 f ( t _ { i } , y ( t _ { i } ) ) - 5 9 f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 3 7 f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) } \\ & { \qquad \quad - \ 9 f ( t _ { i - 3 } , y ( t _ { i - 3 } ) ) \biggr ] + \frac { h ^ { 5 } } { 2 4 } f ^ { ( 4 ) } ( \mu , y ( \mu ) ) \int _ { 0 } ^ { 1 } s ( s + 1 ) ( s + 2 ) ( s + 3 ) \ d s } \end{array}
$$

for some $\mu$ in $( t _ { i - 3 } , t _ { i + 1 } )$ . The local truncation error form follows from the fact that

$$
\int _ { 0 } ^ { 1 } s ( s + 1 ) ( s + 2 ) ( s + 3 ) \ d s = { \frac { 2 5 1 } { 3 0 } } .
$$

$^ { \ast } 1 2$ . Using the notation $y = y ( t _ { i } )$ $\mathsf { \Phi } = y ( t _ { i } ) , f = f ( t _ { i } , y ( t _ { i } ) ) , f _ { t } = f _ { t } ( t _ { i } , y ( t _ { i } ) )$ , etc., we have

$$
\begin{array} { l } { { \displaystyle y + h f + \frac { h ^ { 2 } } { 2 } ( f _ { t } + f f _ { y } ) + \frac { h ^ { 3 } } { 6 } \left( f _ { t t } + f _ { t } f _ { y } + 2 f f _ { y t } + f f _ { y } ^ { 2 } + f ^ { 2 } f _ { y y } \right) } } \\ { { \displaystyle \quad = y + a h f + b h \left[ f - h ( f _ { t } + f f _ { y } ) + \frac { h ^ { 2 } } { 2 } \left( f _ { t t } + f _ { t } f _ { y } + 2 f f _ { y t } + f f _ { y } ^ { 2 } + f ^ { 2 } f _ { y y } \right) \right] } } \\ { { \displaystyle \quad + c h \left[ f - 2 h ( f _ { t } + f f _ { y } ) + 2 h ^ { 2 } \left( f _ { t t } + f _ { t } f _ { y } + 2 f f _ { y t } + f f _ { y } ^ { 2 } + f ^ { 2 } f _ { y y } \right) \right] . } } \end{array}
$$

Thus

$$
a + b + c = 1 , \quad - b - 2 c = \frac { 1 } { 2 } , \quad \mathrm { a n d } \quad \frac { 1 } { 2 } b + 2 c = \frac { 1 } { 6 } .
$$

This system has the solution

$$
a = { \frac { 2 3 } { 1 2 } } , \quad b = - { \frac { 1 6 } { 1 2 } } , \quad { \mathrm { a n d } } \quad c = { \frac { 5 } { 1 2 } } .
$$

13. Newton’s divided-difference formula gives

$$
\begin{array} { l } { \displaystyle f ( t , y ( t ) ) = \frac { 1 } { 2 h ^ { 2 } } ( t - t _ { i } ) ( t - t _ { i + 1 } ) f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) \ - \frac { 1 } { h ^ { 2 } } ( t - t _ { i - 1 } ) ( t - t _ { i + 1 } ) f ( t _ { i } , y ( t _ { i } ) ) } \\ { \displaystyle \qquad + \frac { 1 } { 2 h ^ { 2 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) + \frac { 1 } { 6 } \frac { d ^ { 3 } } { d t ^ { 3 } } f ( \xi , y ( \xi ) ) ( t - t _ { i - 1 } ) ( t - t _ { i } ) ( t - t _ { i + 1 } ) } \end{array}
$$

so

$$
\int _ { t _ { i } } ^ { t _ { i + 1 } } y ^ { \prime } ( t ) d t = \int _ { t _ { i } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t
$$

and

$$
\begin{array} { l }  { + 1 ) - y ( t _ { i } ) = { \displaystyle \frac { f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) } { 2 h ^ { 2 } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i } ) ( t - t _ { i + 1 } ) d t - { \displaystyle \frac { f ( t _ { i } , y ( t _ { i } ) ) } { h ^ { 2 } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) d t } } } \\ { { \displaystyle ~ + ~ { \displaystyle \frac { f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) } { 2 h ^ { 2 } } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) d t } + { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } \frac { f ^ { \prime \prime \prime } ( \xi , y ( \xi ) ) } { 6 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) d t } } \\ { { \displaystyle ~ = { \displaystyle \frac { - h } { 1 2 } } f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + { \displaystyle \frac { 2 h } { 3 } } f ( t _ { i } , y ( t _ { i } ) ) + { \displaystyle \frac { 5 h } { 1 2 } } f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) } } \\ { { \displaystyle ~ + ~ { \displaystyle \frac { f ^ { \prime \prime } ( \mu , y ( \mu ) ) } { 6 } \int _ { t _ { i } } ^ { t _ { i + 1 } } ( t - t _ { i - 1 } ) ( t - t _ { i } ) ( t - t _ { i + 1 } ) d t } . } } \end{array}
$$

The last part follows from Theorem 4.2. Further integration yields Formula (5.37) and the local truncation error.

$^ { * } 1 4$ . We have

$$
\begin{array} { l } { { \displaystyle y ( t _ { i + 1 } ) - y ( t _ { i - 1 } ) = \int _ { t _ { i - 1 } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) d t } } \\ { { \displaystyle \qquad = \frac { h } { 3 } \left[ f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 4 f ( t _ { i } , y ( t _ { i } ) ) + f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) \right] - \frac { h ^ { 5 } } { 9 0 } f ^ { ( 4 ) } ( \xi , y ( \xi ) ) . } } \end{array}
$$

This leads to the difference equation

$$
w _ { i + 1 } = w _ { i - 1 } + \frac { h \left[ f ( t _ { i - 1 } , w _ { i - 1 } ) + 4 f ( t _ { i } , w _ { i } ) + f ( t _ { i + 1 } , w _ { i + 1 } ) \right] } { 3 } ,
$$

with local truncation error

$$
\tau _ { i + 1 } ( h ) = \frac { - h ^ { 4 } y ^ { ( 5 ) } ( \xi ) } { 9 0 } .
$$

15. To derive Milne’s method, integrate $y ^ { \prime } ( t ) = f ( t , y ( t ) )$ on the interval $[ t _ { i - 3 } , t _ { i + 1 } ]$ to obtain

$$
y ( t _ { i + 1 } ) - y ( t _ { i - 3 } ) = \int _ { t _ { i - 3 } } ^ { t _ { i + 1 } } f ( t , y ( t ) ) \ d t .
$$

Using the open Newton-Cotes formula (4.31) on page 201, we have

$$
y ( t _ { i + 1 } ) - y ( t _ { i - 3 } ) = \frac { 4 h [ 2 f ( t _ { i } , y ( t _ { i } ) ) - f ( t _ { i - 1 } , y ( t _ { i - 1 } ) ) + 2 f ( t _ { i - 2 } , y ( t _ { i - 2 } ) ) ] } { 3 } + \frac { 1 4 h ^ { 5 } f ^ { ( 4 ) } ( \xi , y ( \xi ) ) } { 4 5 } .
$$

The difference equation becomes

$$
w _ { i + 1 } = w _ { i - 3 } + \frac { h [ 8 f ( t _ { i } , w _ { i } ) - 4 f ( t _ { i - 1 } , w _ { i - 1 } ) + 8 f ( t _ { i - 2 } , w _ { i - 2 } ) ] } { 3 } ,
$$

with local truncation error

$$
\tau _ { i + 1 } ( h ) = \frac { 1 4 h ^ { 4 } y ^ { ( 5 ) } ( \xi ) } { 4 5 } .
$$

$^ { * } 1 6$ . The entries are generated by evaluating the following integrals:

$$
\begin{array} { l } { { k = 0 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = \displaystyle \int _ { 0 } ^ { 1 } d s = 1 , } } \\ { { k = 1 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = - \displaystyle \int _ { 0 } ^ { 1 } - s d s = \displaystyle \frac { 1 } { 2 } , } } \\ { { k = 2 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = \displaystyle \int _ { 0 } ^ { 1 } \frac { s \left( s + 1 \right) } { 2 } d s = \displaystyle \frac { 5 } { 1 2 } , } } \\ { { k = 3 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = - \displaystyle \int _ { 0 } ^ { 1 } \frac { - s \left( s + 1 \right) \left( s + 2 \right) } { 6 } d s = \displaystyle \frac { 3 } { 8 } , } } \\ { { k = 4 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = \displaystyle \int _ { 0 } ^ { 1 } \frac { s \left( s + 1 \right) \left( s + 2 \right) \left( s + 3 \right) } { 2 4 } d s = \displaystyle \frac { 2 5 1 } { 7 2 0 } , \quad \mathrm { a n d } } } \\ { { k = 5 \left. - 1 \right. ^ { k } \displaystyle \int _ { 0 } ^ { 1 } \left( { { { { \bf \Pi } } ^ { - s } } } \right) d s = - \displaystyle \int _ { 0 } ^ { 1 } - s \left( s + 1 \right) \left( s + 2 \right) \left( s + 3 \right) \left( s + 4 \right) } d s = \displaystyle \frac { 9 5 } { 2 8 8 } . }  \end{array}
$$

# Exercise Set 5.7, page 320

1. The Adams Variable Step-Size Predictor-Corrector Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>0.04275596</td><td>0.00096891</td><td>0.04275596</td><td>0.00096887</td></tr><tr><td>5</td><td>0.22491460</td><td>0.03529441</td><td>0.05389076</td><td>0.03529359</td></tr><tr><td>12</td><td>0.60214994</td><td>0.50174348</td><td>0.05389076</td><td>0.50171761</td></tr><tr><td>17</td><td>0.81943926</td><td>1.45544317</td><td>0.04345786</td><td>1.45541453</td></tr><tr><td>22</td><td>0.99830392</td><td>3.19605697</td><td>0.03577293</td><td>3.19602842</td></tr><tr><td>26</td><td>1.00000000</td><td>3.21912776</td><td>0.00042395</td><td>3.21909932</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>2.06250000</td><td>1.12132350</td><td>0.06250000</td><td>1.12132353</td></tr><tr><td>5</td><td>2.31250000</td><td>1.55059834</td><td>0.06250000</td><td>1.55059524</td></tr><tr><td>9</td><td>2.62471924</td><td>2.00923157</td><td>0.09360962</td><td>2.00922829</td></tr><tr><td>13</td><td>2.99915773</td><td>2.49895243</td><td>0.09360962</td><td>2.49894707</td></tr><tr><td>17</td><td>3.00000000</td><td>2.50000535</td><td>0.00021057</td><td>2.50000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.06250000</td><td>2.18941363</td><td>0.06250000</td><td>2.18941366</td></tr><tr><td>4</td><td>1.25000000</td><td>2.77892931</td><td>0.06250000</td><td>2.77892944</td></tr><tr><td>8</td><td>1.85102559</td><td>4.84179835</td><td>0.15025640</td><td>4.84180141</td></tr><tr><td>12</td><td>2.00000000</td><td>5.38629105</td><td>0.03724360</td><td>5.38629436</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.06250000</td><td>1.06817960</td><td>0.06250000</td><td>1.06817960</td></tr><tr><td>5</td><td>0.31250000</td><td>1.42861668</td><td>0.06250000</td><td>1.42861361</td></tr><tr><td>10</td><td>0.62500000</td><td>1.90768386</td><td>0.06250000</td><td>1.90767015</td></tr><tr><td>13</td><td>0.81250000</td><td>2.08668486</td><td>0.06250000</td><td>2.08666541</td></tr><tr><td>16</td><td>1.00000000</td><td>2.11800208</td><td>0.06250000</td><td>2.11797955</td></tr></table>

\*(a)

2. The Adams Variable Step-Size Predictor-Corrector Algorithm gives the results in the following tables.   

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>1.05000000</td><td>1.10385717</td><td>0.05000000</td><td>1.10385738</td></tr><tr><td>2</td><td>1.10000000</td><td>1.21588587</td><td>0.05000000</td><td>1.21588635</td></tr><tr><td>3</td><td>1.15000000</td><td>1.33683848</td><td>0.05000000</td><td>1.33683925</td></tr><tr><td>4</td><td>1.20000000</td><td>1.46756885</td><td>0.05000000</td><td>1.46756957</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>1</td><td>0.20000000</td><td>0.20120278</td><td>0.20000000</td><td>0.20120267</td></tr><tr><td>2</td><td>0.40000000</td><td>0.40861919</td><td>0.20000000</td><td>0.40861896</td></tr><tr><td>3</td><td>0.60000000</td><td>0.62585310</td><td>0.20000000</td><td>0.62585275</td></tr><tr><td>4</td><td>0.80000000</td><td>0.85397394</td><td>0.20000000</td><td>0.85396433</td></tr><tr><td>5</td><td>1.00000000</td><td>1.09183759</td><td>0.20000000</td><td>1.09181825</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>yi</td></tr><tr><td>5</td><td>1.16289739</td><td>-1.75426113</td><td>0.03257948</td><td>-1.75426455</td></tr><tr><td>10</td><td>1.32579477</td><td>-1.60547206</td><td>0.03257948</td><td>-1.60547731</td></tr><tr><td>15</td><td>1.57235777</td><td>-1.46625721</td><td>0.04931260</td><td>-1.46626230</td></tr><tr><td>20</td><td>1.92943707</td><td>-1.34978308</td><td>0.07694168</td><td>-1.34978805</td></tr><tr><td>25</td><td>2.47170180</td><td>-1.25358275</td><td>0.11633076</td><td>-1.25358804</td></tr><tr><td>30</td><td>3.00000000</td><td>-1.19999513</td><td>0.10299186</td><td>-1.20000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>1</td><td>0.06250000</td><td>1.00583097</td><td>0.06250000</td><td>1.00583095</td></tr><tr><td>5</td><td>0.31250000</td><td>1.13099427</td><td>0.06250000</td><td>1.13098105</td></tr><tr><td>10</td><td>0.62500000</td><td>1.40361751</td><td>0.06250000</td><td>1.40360196</td></tr><tr><td>12</td><td>0.81250000</td><td>1.56515769</td><td>0.09375000</td><td>1.56514800</td></tr><tr><td>14</td><td>1.00000000</td><td>1.70186884</td><td>0.09375000</td><td>1.70187005</td></tr></table>

3. The following tables list representative results from the Adams Variable Step-Size Predictor-Corrector Algorithm.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>1.10431651</td><td>1.00463041</td><td>0.02086330</td><td>1.00463045</td></tr><tr><td>15</td><td>1.31294952</td><td>1.03196889</td><td>0.02086330</td><td>1.03196898</td></tr><tr><td>25</td><td>1.59408142</td><td>1.08714711</td><td>0.03122028</td><td>1.08714722</td></tr><tr><td>35</td><td>2.00846205</td><td>1.18327922</td><td>0.04824992</td><td>1.18327937</td></tr><tr><td>45</td><td>2.66272188</td><td>1.34525123</td><td>0.07278716</td><td>1.34525143</td></tr><tr><td>52</td><td>3.40193112</td><td>1.52940900</td><td>0.11107035</td><td>1.52940924</td></tr><tr><td>57</td><td>4.00000000</td><td>1.67623887</td><td>0.12174963</td><td>1.67623914</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>1.18519603</td><td>0.20333499</td><td>0.03703921</td><td>0.20333497</td></tr><tr><td>15</td><td>1.55558810</td><td>0.73586642</td><td>0.03703921</td><td>0.73586631</td></tr><tr><td>25</td><td>1.92598016</td><td>1.48072467</td><td>0.03703921</td><td>1.48072442</td></tr><tr><td>35</td><td>2.29637222</td><td>2.51764797</td><td>0.03703921</td><td>2.51764743</td></tr><tr><td>45</td><td>2.65452689</td><td>3.92602442</td><td>0.03092051</td><td>3.92602332</td></tr><tr><td>55</td><td>2.94341188</td><td>5.50206466</td><td>0.02584049</td><td>5.50206279</td></tr><tr><td>61</td><td>3.00000000</td><td>5.87410206</td><td>0.00122679</td><td>5.87409998</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>0.16854008</td><td>-1.83303780</td><td>0.03370802</td><td>-1.83303783</td></tr><tr><td>17</td><td>0.64833341</td><td>-1.42945306</td><td>0.05253230</td><td>-1.42945304</td></tr><tr><td>27</td><td>1.06742915</td><td>-1.21150951</td><td>0.04190957</td><td>-1.21150932</td></tr><tr><td>41</td><td>1.75380240</td><td>-1.05819340</td><td>0.06681937</td><td>-1.05819325</td></tr><tr><td>51</td><td>2.50124702</td><td>-1.01335240</td><td>0.07474446</td><td>-1.01335258</td></tr><tr><td>61</td><td>3.00000000</td><td>-1.00494507</td><td>0.01257155</td><td>-1.00494525</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>0.28548652</td><td>0.32153668</td><td>0.05709730</td><td>0.32153674</td></tr><tr><td>15</td><td>0.85645955</td><td>0.24281066</td><td>0.05709730</td><td>0.24281095</td></tr><tr><td>20</td><td>1.35101725</td><td>0.15096743</td><td>0.09891154</td><td>0.15096772</td></tr><tr><td>25</td><td>1.66282314</td><td>0.09815109</td><td>0.06236118</td><td>0.09815137</td></tr><tr><td>29</td><td>1.91226786</td><td>0.06418555</td><td>0.06236118</td><td>0.06418579</td></tr><tr><td>33</td><td>2.00000000</td><td>0.05434530</td><td>0.02193303</td><td>0.05434551</td></tr></table>

\*4. Change the following steps:

STEP 1 Set up an algorithm, denoted $R K 5$ , for the Runge Kutta Method of Order 5. STEP 3 Call $R K 5 ( h , w _ { 0 } , t _ { 0 } , w _ { 1 } , t _ { 1 } , w _ { 2 } , t _ { 2 } , w _ { 3 } , t _ { 3 } , w _ { 4 } , t _ { 4 } )$ :

$$
\begin{array} { r l } { \mathrm { S e t } } & { N F L A G = 1 ; } \\ & { i = 5 ; } \\ & { t = t _ { 4 } + h . } \end{array}
$$

STEP 5 Set

$$
\begin{array} { r l } & { W P = w _ { i - 1 } + \frac { h } { 7 2 0 } \bigg [ 1 9 0 1 f ( t _ { i - 1 } , w _ { i - 1 } ) - 2 7 7 4 f ( t _ { i - 2 } , w _ { i - 2 } ) } \\ & { \qquad + 2 6 1 6 f ( t _ { i - 3 } , w _ { i - 3 } ) - 1 2 7 4 f ( t _ { i - 4 } , w _ { i - 4 } ) + 2 5 1 f ( t _ { i - 5 } , w _ { i - 5 } ) \bigg ] ; } \\ & { W C = w _ { i - 1 } + \frac { h } { 7 2 0 } \bigg [ 2 5 1 f ( t , W P ) + 6 4 6 f ( t _ { i - 1 } , w _ { i - 1 } ) - 2 6 4 f ( t _ { i - 2 } , w _ { i - 2 } ) } \\ & { \qquad + 1 0 6 f ( t _ { i - 3 } , w _ { i - 3 } ) - 1 9 f ( t _ { i - 4 } , w _ { i - 4 } ) \bigg ] ; } \\ & { \sigma = 2 7 | W C - W P | / ( 5 0 2 ) h . } \end{array}
$$

$\begin{array} { l } { S T E P ~ \delta } \\ { S T E P ~ \mathit { 1 2 } } \\ { S T E P ~ \mathit { 1 5 } } \\ { S T E P ~ \mathit { 1 6 } } \end{array}$ If $N F L A G = 1$ then for $j = i - 4 , i - 3 , i - 2 , i - 1 , i$ Set $q = ( 0 . 5 T O L / \sigma ) ^ { \frac { 1 } { 5 } }$ If $t _ { i - 1 } + 5 h > b$ , then set $h = ( b - t _ { i - 1 } ) / 5$ Call $R K 5 ( h , w _ { i - 1 } , t _ { i - 1 } , w _ { i } , t _ { i } , w _ { i + 1 } , t _ { i + 1 } , w _ { i + 2 } , t _ { i + 2 } , w _ { i + 3 } , t _ { i + 3 } ) ;$

Set $N F L A G = 1$ ; $i = i + 4$ . STEP 17 Set $q = ( 0 . 5 T O L / \sigma ) ^ { \frac { 1 } { 5 } }$ .

STEP 19 else

The following are the results obtained by applying the new algorithm to the problems in Exercise 3.

\*(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>1.17529879</td><td>1.01186066</td><td>0.03505976</td><td>1.01186063</td></tr><tr><td>15</td><td>1.56737794</td><td>1.08139480</td><td>0.05580055</td><td>1.08139470</td></tr><tr><td>25</td><td>2.25808774</td><td>1.24445586</td><td>0.08897663</td><td>1.24445574</td></tr><tr><td>35</td><td>3.51328927</td><td>1.55692781</td><td>0.14118166</td><td>1.55692763</td></tr><tr><td>40</td><td>4.00000000</td><td>1.67623932</td><td>0.09734215</td><td>1.67623914</td></tr><tr><td>5</td><td>1.33993400</td><td>0.40368020</td><td>0.06798680</td><td>0.40368021</td></tr><tr><td>15</td><td>2.13987639</td><td>2.03689764</td><td>0.07343117</td><td>2.03689764</td></tr><tr><td>25</td><td>2.78633514</td><td>4.58497685</td><td>0.05029339</td><td>4.58497677</td></tr><tr><td>30</td><td>2.99000695</td><td>5.80662141</td><td>0.00249826</td><td>5.80662127</td></tr><tr><td>34</td><td>3.00000000</td><td>5.87410012</td><td>0.00249826</td><td>5.87409998</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>0.32371968</td><td>-1.68713369</td><td>0.06474394</td><td>-1.68713361</td></tr><tr><td>15</td><td>0.98679855</td><td>-1.24400623</td><td>0.08248419</td><td>-1.24400610</td></tr><tr><td>20</td><td>1.39921950</td><td>-1.11481699</td><td>0.08248419</td><td>-1.11481718</td></tr><tr><td>25</td><td>1.81164045</td><td>-1.05200140</td><td>0.08248419</td><td>-1.05200171</td></tr><tr><td>29</td><td>2.23962447</td><td>-1.02242929</td><td>0.13150782</td><td>-1.02242946</td></tr><tr><td>33</td><td>2.76565574</td><td>-1.00789049</td><td>0.13150782</td><td>-1.00789033</td></tr><tr><td>39</td><td>3.00000000</td><td>-1.00494544</td><td>0.02056729</td><td>-1.00494525</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>Yi</td></tr><tr><td>5</td><td>0.49509708</td><td>0.29938376</td><td>0.09901942</td><td>0.29938377</td></tr><tr><td>15</td><td>1.27560008</td><td>0.16486635</td><td>0.03572768</td><td>0.16486623</td></tr><tr><td>20</td><td>1.65480865</td><td>0.09938119</td><td>0.10258441</td><td>0.09938111</td></tr><tr><td>25</td><td>1.94399098</td><td>0.06049879</td><td>0.02800451</td><td>0.06049858</td></tr><tr><td>27</td><td>2.00000000</td><td>0.05434569</td><td>0.02800451</td><td>0.05434551</td></tr></table>

5. The current after 2 seconds is approximately $i ( 2 ) = 8 . 6 9 3$ amperes.

# Exercise Set 5.8, page 327

1. The Extrapolation Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>0.25</td><td>0.04543132</td><td>0.25</td><td>3</td><td>0.04543123</td></tr><tr><td>2</td><td>0.50</td><td>0.28361684</td><td>0.25</td><td>3</td><td>0.28361652</td></tr><tr><td>3</td><td>0.75</td><td>1.05257634</td><td>0.25</td><td>4</td><td>1.05257615</td></tr><tr><td>4</td><td>1.00</td><td>3.21909944</td><td>0.25</td><td>4</td><td>3.21909932</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>2.25</td><td>1.44999987</td><td>0.25</td><td>3</td><td>1.45000000</td></tr><tr><td>2</td><td>2.50</td><td>1.83333321</td><td>0.25</td><td>3</td><td>1.83333333</td></tr><tr><td>3</td><td>2.75</td><td>2.17857133</td><td>0.25</td><td>3</td><td>2.17857143</td></tr><tr><td>4</td><td>3.00</td><td>2.49999993</td><td>0.25</td><td>3</td><td>2.50000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>1.25</td><td>2.77892942</td><td>0.25</td><td>3</td><td>2.77892944</td></tr><tr><td>2</td><td>1.50</td><td>3.60819763</td><td>0.25</td><td>3</td><td>3.60819766</td></tr><tr><td>3</td><td>1.75</td><td>4.47932759</td><td>0.25</td><td>3</td><td>4.47932763</td></tr><tr><td>4</td><td>2.00</td><td>5.38629431</td><td>0.25</td><td>3</td><td>5.38629436</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>1.32914981</td><td>0.25</td><td>3</td><td>1.32914981</td></tr><tr><td>2</td><td>0.50</td><td>1.73048976</td><td>0.25</td><td>3</td><td>1.73048976</td></tr><tr><td>3</td><td>0.75</td><td>2.04147203</td><td>0.25</td><td>3</td><td>2.04147203</td></tr><tr><td>4</td><td>1.00</td><td>2.11797954</td><td>0.25</td><td>3</td><td>2.11797955</td></tr></table>

2. The Extrapolation Algorithm gives the results in the following tables. \*(a)   

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>1.05</td><td>1.10385729</td><td>0.05</td><td>2</td><td>1.10385738</td></tr><tr><td>2</td><td>1.10</td><td>1.21588614</td><td>0.05</td><td>2</td><td>1.21588635</td></tr><tr><td>3</td><td>1.15</td><td>1.33683891</td><td>0.05</td><td>2</td><td>1.33683925</td></tr><tr><td>4</td><td>1.20</td><td>1.46756907</td><td>0.05</td><td>2</td><td>1.46756957</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>0.25228680</td><td>0.25</td><td>3</td><td>0.25228680</td></tr><tr><td>2</td><td>0.50</td><td>0.51588678</td><td>0.25</td><td>3</td><td>0.51588678</td></tr><tr><td>3</td><td>0.75</td><td>0.79594460</td><td>0.25</td><td>2</td><td>0.79594458</td></tr><tr><td>4</td><td>1.00</td><td>1.09181828</td><td>0.25</td><td>3</td><td>1.09181825</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>1.50</td><td>-1.50000055</td><td>0.50</td><td>5</td><td>-1.50000000</td></tr><tr><td>2</td><td>2.00</td><td>-1.33333435</td><td>0.50</td><td>3</td><td>-1.33333333</td></tr><tr><td>3</td><td>2.50</td><td>-1.25000074</td><td>0.50</td><td>3</td><td>-1.25000000</td></tr><tr><td>4</td><td>3.00</td><td>-1.20000090</td><td>0.50</td><td>2</td><td>-1.20000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>hi</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>1.08708817</td><td>0.25</td><td>3</td><td>1.08708823</td></tr><tr><td>2</td><td>0.50</td><td>1.28980537</td><td>0.25</td><td>3</td><td>1.28980528</td></tr><tr><td>3</td><td>0.75</td><td>1.51349008</td><td>0.25</td><td>3</td><td>1.51348985</td></tr><tr><td>4</td><td>1.00</td><td>1.70187009</td><td>0.25</td><td>3</td><td>1.70187005</td></tr></table>

3. The Extrapolation Algorithm gives the results in the following tables.

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>1.50</td><td>1.06726237</td><td>0.50</td><td>4</td><td>1.06726235</td></tr><tr><td>2</td><td>2.00</td><td>1.18123223</td><td>0.50</td><td>3</td><td>1.18123222</td></tr><tr><td>3</td><td>2.50</td><td>1.30460372</td><td>0.50</td><td>3</td><td>1.30460371</td></tr><tr><td>4</td><td>3.00</td><td>1.42951608</td><td>0.50</td><td>3</td><td>1.42951607</td></tr><tr><td>5</td><td>3.50</td><td>1.55364771</td><td>0.50</td><td>3</td><td>1.55364770</td></tr><tr><td>6</td><td>4.00</td><td>1.67623915</td><td>0.50</td><td>3</td><td>1.67623914</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>1.50</td><td>0.64387537</td><td>0.50</td><td>4</td><td>0.64387533</td></tr><tr><td>2</td><td>2.00</td><td>1.66128182</td><td>0.50</td><td>5</td><td>1.66128176</td></tr><tr><td>3</td><td>2.50</td><td>3.25801550</td><td>0.50</td><td>5</td><td>3.25801536</td></tr><tr><td>4</td><td>3.00</td><td>5.87410027</td><td>0.50</td><td>5</td><td>5.87409998</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>0.50</td><td>-1.53788284</td><td>0.50</td><td>4</td><td>-1.53788284</td></tr><tr><td>2</td><td>1.00</td><td>-1.23840584</td><td>0.50</td><td>5</td><td>-1.23840584</td></tr><tr><td>3</td><td>1.50</td><td>-1.09485175</td><td>0.50</td><td>5</td><td>-1.09485175</td></tr><tr><td>4</td><td>2.00</td><td>-1.03597242</td><td>0.50</td><td>5</td><td>-1.03597242</td></tr><tr><td>5</td><td>2.50</td><td>-1.01338570</td><td>0.50</td><td>5</td><td>-1.01338570</td></tr><tr><td>6</td><td>3.00</td><td>-1.00494526</td><td>0.50</td><td>4</td><td>-1.00494525</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>h</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>0.50</td><td>0.29875177</td><td>0.50</td><td>4</td><td>0.29875178</td></tr><tr><td>2</td><td>1.00</td><td>0.21662642</td><td>0.50</td><td>4</td><td>0.21662642</td></tr><tr><td>3</td><td>1.50</td><td>0.12458565</td><td>0.50</td><td>4</td><td>0.12458565</td></tr><tr><td>4</td><td>2.00</td><td>0.05434552</td><td>0.50</td><td>4</td><td>0.05434551</td></tr></table>

\*4. The population after five years is $y ( 5 ) \approx 5 6 , 7 5 1$ .

# Exercise Set 5.9, page 337

1. The Runge-Kutta for Systems Algorithm gives the results in the following tables. \*(a)   

<table><tr><td>ti</td><td>W1i</td><td>U1i</td><td>W2i</td><td>U2i</td></tr><tr><td>0.200</td><td>2.12036583</td><td>2.12500839</td><td>1.50699185</td><td>1.51158743</td></tr><tr><td>0.400</td><td>4.44122776</td><td>4.46511961</td><td>3.24224021</td><td>3.26598528</td></tr><tr><td>0.600</td><td>9.73913329</td><td>9.83235869</td><td>8.16341700</td><td>8.25629549</td></tr><tr><td>0.800</td><td>22.67655977</td><td>23.00263945</td><td>21.34352778</td><td>21.66887674</td></tr><tr><td>1.000</td><td>55.66118088</td><td>56.73748265</td><td>56.03050296</td><td>57.10536209</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>u2i</td></tr><tr><td>0.500</td><td>0.95671390</td><td>0.95672798</td><td>-1.08381950</td><td>-1.08383310</td></tr><tr><td>1.000</td><td>1.30654440</td><td>1.30655930</td><td>-0.83295364</td><td>-0.83296776</td></tr><tr><td>1.500</td><td>1.34416716</td><td>1.34418117</td><td>-0.56980329</td><td>-0.56981634</td></tr><tr><td>2.000</td><td>1.14332436</td><td>1.14333672</td><td>-0.36936318</td><td>-0.36937457</td></tr></table>

(c)

<table><tr><td>ti</td><td>W1i</td><td>Uli</td><td>W2i</td><td>u2i</td><td>W3i</td><td>U3i</td></tr><tr><td>0.5</td><td>0.70787076</td><td>0.70828683</td><td>-1.24988663</td><td>-1.25056425</td><td>0.39884862</td><td>0.39815702</td></tr><tr><td>1.0</td><td>-0.33691753</td><td>-0.33650854</td><td>-3.01764179</td><td>-3.01945051</td><td>-0.29932294</td><td>-0.30116868</td></tr><tr><td>1.5</td><td>-2.41332734</td><td>-2.41345688</td><td>-5.40523279</td><td>-5.40844686</td><td>-0.92346873</td><td>-0.92675778</td></tr><tr><td>2.0</td><td>-5.89479008</td><td>-5.89590551</td><td>-8.70970537</td><td>-8.71450036</td><td>-1.32051165</td><td>-1.32544426</td></tr></table>

(d)

<table><tr><td>ti</td><td>W1i</td><td>U1i</td><td>W2i</td><td>U2i</td><td>W3i</td><td>u3i</td></tr><tr><td>0.2</td><td>1.38165297</td><td>1.38165325</td><td>1.00800000</td><td>1.00800000</td><td>-0.61833075</td><td>-0.61833075</td></tr><tr><td>0.5</td><td>1.90753116</td><td>1.90753184</td><td>1.12500000</td><td>1.12500000</td><td>-0.09090565</td><td>-0.09090566</td></tr><tr><td>0.7</td><td>2.25503524</td><td>2.25503620</td><td>1.34300000</td><td>1.34000000</td><td>0.26343971</td><td>0.26343970</td></tr><tr><td>1.0</td><td>2.83211921</td><td>2.83212056</td><td>2.00000000</td><td>2.00000000</td><td>0.88212058</td><td>0.88212056</td></tr></table>

(a)

2. The Runge-Kutta for Systems Algorithm gives the results in the following tables.   

<table><tr><td>t</td><td>W1</td><td>W2</td><td>U1</td><td>u2</td></tr><tr><td>0.2</td><td>-0.80590898</td><td>0.28590898</td><td>-0.8059123490</td><td>0.2859123490</td></tr><tr><td>0.4</td><td>-0.65276041</td><td>0.77276041</td><td>-0.652770464</td><td>0.772770464</td></tr><tr><td>0.6</td><td>-0.60003597</td><td>1.52003597</td><td>-0.600058462</td><td>1.520058462</td></tr><tr><td>0.8</td><td>-0.73647147</td><td>2.61647147</td><td>-0.736516212</td><td>2.616516212</td></tr><tr><td>1.0</td><td>-1.19444462</td><td>4.19444462</td><td>-1.194528050</td><td>4.194528050</td></tr></table>

(b)

<table><tr><td>t</td><td>W1</td><td>W2</td><td>u1</td><td>U2</td></tr><tr><td>0.2</td><td>-3.62420001</td><td>5.28560000</td><td>-3.624208274</td><td>5.285611032</td></tr><tr><td>0.6</td><td>-5.10631940</td><td>6.48842582</td><td>-5.106356400</td><td>6.488475200</td></tr><tr><td>1.0</td><td>-7.15475346</td><td>8.87300454</td><td>-7.154845484</td><td>8.87312731</td></tr><tr><td>1.4</td><td>-10.20540766</td><td>13.02054346</td><td>-10.20559990</td><td>13.02079987</td></tr><tr><td>1.8</td><td>-14.90857362</td><td>19.79809804</td><td>-14.90894239</td><td>19.79858986</td></tr></table>

(c)

<table><tr><td>t</td><td>W1</td><td>W2</td><td>W3</td><td>U1</td><td>u2</td><td>u3</td></tr><tr><td>0.2</td><td>2.82820001</td><td>-1.36717100</td><td>1.29430535</td><td>2.828199216</td><td>-1.367172763</td><td>1.294303950</td></tr><tr><td>0.4</td><td>2.34715282</td><td>-1.70213314</td><td>1.35096843</td><td>2.347150799</td><td>-1.702138886</td><td>1.350962985</td></tr><tr><td>0.6</td><td>1.61165492</td><td>-2.06862759</td><td>1.12031748</td><td>1.611651361</td><td>-2.068641364</td><td>1.120303523</td></tr><tr><td>0.8</td><td>0.68019035</td><td>-2.55506790</td><td>0.53282506</td><td>0.680185091</td><td>-2.555096786</td><td>0.532795132</td></tr><tr><td>1.0</td><td>-0.38623048</td><td>-3.28594071</td><td>-0.51207026</td><td>-0.386237443</td><td>-3.285996825</td><td>-0.512128574</td></tr></table>

<table><tr><td>t</td><td>W1</td><td>W2</td><td>W3</td><td>u1</td><td>u2</td><td>U3</td></tr><tr><td>0.2</td><td>5.85399925</td><td>-6.58493690</td><td>-5.51120222</td><td>6.655197738</td><td>-6.582587709</td><td>-5.507713390</td></tr><tr><td>0.6</td><td>13.58890681</td><td>-2.95418927</td><td>-4.51808620</td><td>14.00287757</td><td>-2.921029767</td><td>-4.45343131</td></tr><tr><td>1.0</td><td>41.49825592</td><td>13.88034475</td><td>26.10907731</td><td>41.57707969</td><td>14.18586490</td><td>26.71881714</td></tr><tr><td>1.4</td><td>134.58778600</td><td>135.26098840</td><td>267.46411360</td><td>134.5550923</td><td>137.5527145</td><td>272.0466805</td></tr><tr><td>1.8</td><td>443.12659480</td><td>882.03172470</td><td>1760.52619100</td><td>443.8948036</td><td>897.3731894</td><td>1791.208540</td></tr></table>

3. The Runge-Kutta for Systems Algorithm gives the results in the following tables. \*(a)   

<table><tr><td>ti</td><td>W1i</td><td>Yi</td></tr><tr><td>0.200</td><td>0.00015352</td><td>0.00015350</td></tr><tr><td>0.500</td><td>0.00742968</td><td>0.00743027</td></tr><tr><td>0.700</td><td>0.03299617</td><td>0.03299805</td></tr><tr><td>1.000</td><td>0.17132224</td><td>0.17132880</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>Yi</td></tr><tr><td>1.200</td><td>0.96152437</td><td>0.96152583</td></tr><tr><td>1.500</td><td>0.77796897</td><td>0.77797237</td></tr><tr><td>1.700</td><td>0.59373369</td><td>0.59373830</td></tr><tr><td>2.000</td><td>0.27258237</td><td>0.27258872</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>yi</td></tr><tr><td>1.000</td><td>3.73162695</td><td>3.73170445</td></tr><tr><td>2.000</td><td>11.31424573</td><td>11.31452924</td></tr><tr><td>3.000</td><td>34.04395688</td><td>34.04517155</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>W2i</td></tr><tr><td>1.200</td><td>0.27273759</td><td>0.27273791</td></tr><tr><td>1.500</td><td>1.08849079</td><td>1.08849259</td></tr><tr><td>1.700</td><td>2.04353207</td><td>2.04353642</td></tr><tr><td>2.000</td><td>4.36156675</td><td>4.36157780</td></tr></table>

(a)

4. The Runge-Kutta for Systems Algorithm gives the results in the following tables.   

<table><tr><td>t</td><td>W1</td><td>W2</td><td>y(t)</td></tr><tr><td>0.2</td><td>2.58096738</td><td>3.92714601</td><td>2.580977391</td></tr><tr><td>0.4</td><td>3.62954528</td><td>6.73995658</td><td>3.629577204</td></tr><tr><td>0.6</td><td>5.36685193</td><td>10.90938990</td><td>5.366926682</td></tr><tr><td>0.8</td><td>8.12969935</td><td>17.13695552</td><td>8.129852884</td></tr><tr><td>1.0</td><td>12.42741665</td><td>26.46948024</td><td>12.42770981</td></tr></table>

<table><tr><td>t</td><td>W1</td><td>W2</td><td>y(t)</td></tr><tr><td>1.2</td><td>4.77485600</td><td>4.64248546</td><td>4.774444444</td></tr><tr><td>1.6</td><td>7.11125088</td><td>6.91189139</td><td>7.110625000</td></tr><tr><td>2.0</td><td>10.25079116</td><td>8.75041113</td><td>10.25000000</td></tr><tr><td>2.4</td><td>14.09462248</td><td>10.45592060</td><td>14.09361111</td></tr><tr><td>2.8</td><td>18.60884185</td><td>12.10964620</td><td>18.60755102</td></tr></table>

<table><tr><td>t</td><td>W1</td><td>W2</td><td>W3</td><td>y(t)</td></tr><tr><td>0.2</td><td>2.98086667</td><td>0.82393333</td><td>9.46726667</td><td>2.980875497</td></tr><tr><td>0.6</td><td>4.16962578</td><td>5.48759308</td><td>15.03205266</td><td>4.170122771</td></tr><tr><td>1.0</td><td>7.89009498</td><td>14.13487020</td><td>30.45672422</td><td>7.892270823</td></tr><tr><td>1.4</td><td>16.74506147</td><td>32.50687231</td><td>66.24043865</td><td>16.75205379</td></tr><tr><td>1.8</td><td>36.77072349</td><td>72.93612397</td><td>146.58698330</td><td>36.79085705</td></tr></table>

<table><tr><td>t</td><td>W1</td><td>W2</td><td>W3</td><td>y(t)</td></tr><tr><td>1.2</td><td>3.73466631</td><td>9.41446279</td><td>8.04259896</td><td>3.734666667</td></tr><tr><td>1.4</td><td>5.78971770</td><td>11.19022983</td><td>9.67114868</td><td>5.789714286</td></tr><tr><td>1.6</td><td>8.23100886</td><td>13.27065559</td><td>11.11173381</td><td>8.231000000</td></tr><tr><td>1.8</td><td>11.11645980</td><td>15.62867678</td><td>12.45708169</td><td>11.11644444</td></tr><tr><td>2.0</td><td>14.50002275</td><td>18.25003892</td><td>13.75001862</td><td>14.50000000</td></tr></table>

$^ { * } 5$ . To approximate the solution of the $m$ th–order system of first–order initial–value problems

$$
u _ { j } ^ { \prime } = f _ { j } ( t , u _ { 1 } , u _ { 2 } , \ldots , u _ { m } ) , j = 1 , 2 , \ldots , m , \mathrm { f o r } a \leq t \leq b , u _ { j } ( a ) = \alpha _ { j } , j = 1 , 2 , \ldots , m ,
$$

at $( n + 1 )$ equally spaced numbers in the interval $[ a , b ]$ ;

INPUT endpoints $a , b$ ; number of equations $m$ ; integer $N$ ; initial conditions $\alpha _ { 1 } , \ldots , \alpha _ { m }$ .   
OUTPUT approximations $w _ { i , j }$ to $u _ { j } ( t _ { i } )$ . STEP 1 Set $h = ( b - a ) / N$ ;   
STEP 2 For $j = 1 , 2 , \dots , m$ set $w _ { 0 , j } = \alpha _ { j }$ .   
STEP 3 OUTPUT $( t _ { 0 } , w _ { 0 , 1 } , w _ { 0 , 2 } , \ldots , w _ { 0 , m } )$ .

$S T E P 4$ For $i = { 1 , 2 , 3 }$ do Steps 5–11.

$$
\begin{array} { r l } & { k _ { 1 , j } = h f _ { j } ( t _ { i - 1 } , w _ { i - 1 , 1 } , \ldots , w _ { i - 1 , m } ) . } \\ & { \mathrm { ~ F o r ~ } j = 1 , 2 , \ldots , m \mathrm { ~ s e t } } \\ & { k _ { 2 , j } = h f _ { j } \left( t _ { i - 1 } + \frac { h } { 2 } , w _ { i - 1 , 1 } + \frac { 1 } { 2 } k _ { 1 , 1 } , w _ { i - 1 , 2 } + \frac { 1 } { 2 } k _ { 1 , 2 } , \ldots , w _ { i - 1 , m } + \frac { 1 } { 2 } k _ { 1 , m } \right) . } \\ & { \mathrm { ~ F o r ~ } j = 1 , 2 , \ldots , m \mathrm { ~ s e t } } \\ & { k _ { 3 , j } = h f _ { j } \left( t _ { i - 1 } + \frac { 1 } { 2 } , w _ { i - 1 , 1 } + \frac { 1 } { 2 } k _ { 2 , 1 } , w _ { i - 1 , 2 } + \frac { 1 } { 2 } k _ { 2 , 2 } , \ldots , w _ { i - 1 , m } + \frac { 1 } { 2 } k _ { 2 , m } \right) . } \\ & { \mathrm { ~ F o r ~ } j = 1 , 2 , \ldots , m \mathrm { ~ s e t } } \\ & { k _ { 4 , j } = h f _ { j } ( t _ { i - 1 } + h , w _ { i - 1 , 1 } + k _ { 3 , 1 } , w _ { i - 1 , 2 } + k _ { 3 , 2 } , \ldots , w _ { i - 1 , m } + k _ { 3 , m } ) . } \\ & { \mathrm { ~ F o r ~ } j = 1 , 2 , \ldots , m \mathrm { ~ s e t } } \\ & { w _ { i , j } = w _ { i - 1 , j } + ( k _ { 1 , j } + 2 k _ { 2 , j } + 2 k _ { 3 , j } + k _ { 4 , j } ) / 6 . } \\ & { \mathrm { ~ S e t ~ } t _ { i } = { } _ { i } + h . } \end{array}
$$

STEP 12 For $i = 4 , \ldots , N$ do Steps 13–16. STEP 13 Set $t _ { i } = a + i h$ . STEP 14 For $j = 1 , 2 , \dots , m$ set

$$
\begin{array} { l } { w _ { i , j } ^ { ( 0 ) } = w _ { i - 1 , j } + h \bigg [ 5 5 f _ { j } \big ( t _ { i - 1 } , w _ { i - 1 , 1 } , \ldots , w _ { i - 1 , m } \big ) - 5 9 f _ { j } \big ( t _ { i - 2 } , w _ { i - 2 , 1 } , \ldots , w _ { i - 2 , m } \big ) } \\ { \qquad + 3 7 f _ { j } \big ( t _ { i - 3 } , w _ { i - 3 , 1 } , \ldots , w _ { i - 3 , m } \big ) - 9 f _ { j } \big ( t _ { i - 4 } , w _ { i - 4 , 1 } , \ldots , w _ { i - 4 , m } \big ) \bigg ] \bigg / 2 4 . } \end{array}
$$

STEP 15 For $j = 1 , 2 , \dots , m$ set

$$
\begin{array} { r } { w _ { i , j } = w _ { i - 1 , j } + h \bigg [ 9 f _ { j } \left( t _ { i } , w _ { i , 1 } ^ { ( 0 ) } , \ldots , w _ { i , m } ^ { ( 0 ) } \right) + 1 9 f _ { j } ( t _ { i - 1 } , w _ { i - 1 , 1 } , \ldots , w _ { i - 1 , m } ) } \\ { - \left. 5 f _ { j } ( t _ { i - 2 } , w _ { i - 2 , 1 } , \ldots , w _ { i - 2 , m } ) + f _ { j } ( t _ { i - 3 } , w _ { i - 3 , 1 } , \ldots , w _ { i - 3 , m } ) \right] \bigg / 2 4 . } \end{array}
$$

STEP 17 STOP

6. The Adams Fourth-Order Predictor-Corrector method for systems applied to the problems in Exercise 2 gives the results in the following tables.

(a)

<table><tr><td>ti</td><td>w1(ti)</td><td>u1(ti)</td><td>w2(ti)</td><td>u2(ti)</td></tr><tr><td>0.2</td><td>-0.80590898</td><td>-0.80591235</td><td>0.28590898</td><td>0.28591235</td></tr><tr><td>0.4</td><td>-0.65276394</td><td>-0.65277046</td><td>0.77276394</td><td>0.77277046</td></tr><tr><td>0.6</td><td>-0.60005208</td><td>-0.60005846</td><td>1.52005208</td><td>1.52005846</td></tr><tr><td>0.8</td><td>-0.73651161</td><td>-0.73651621</td><td>2.61651161</td><td>2.61651621</td></tr><tr><td>1.0</td><td>-1.19452854</td><td>-1.19452805</td><td>4.19452854</td><td>4.19452805</td></tr></table>

(b)

<table><tr><td>ti</td><td>W1(ti)</td><td>u1(ti)</td><td>w2(ti)</td><td>u2(ti)</td></tr><tr><td>0.2</td><td>-3.62420001</td><td>-3.62420827</td><td>5.28560000</td><td>5.28561103</td></tr><tr><td>0.8</td><td>-5.10631940</td><td>-5.10635640</td><td>6.48842583</td><td>6.48847520</td></tr><tr><td>1.0</td><td>-7.15480610</td><td>-7.15484549</td><td>8.87307476</td><td>8.87312731</td></tr><tr><td>1.4</td><td>-10.20556525</td><td>-10.20559990</td><td>13.02075362</td><td>13.02079987</td></tr><tr><td>1.8</td><td>-14.90892678</td><td>-14.90894239</td><td>19.79856900</td><td>19.79858986</td></tr></table>

(c)

<table><tr><td>ti</td><td>w1(ti)</td><td>u1(ti)</td><td>w2(ti)</td><td>u2(ti)</td><td>w3(ti)</td><td>u3(ti)</td></tr><tr><td>0.2</td><td>2.82820001</td><td>2.82819922</td><td>-1.36717100</td><td>-1.36717276</td><td>1.29430535</td><td>1.29430395</td></tr><tr><td>0.4</td><td>2.34715270</td><td>2.34715080</td><td>-1.70213589</td><td>-1.70213889</td><td>1.35096690</td><td>1.35096298</td></tr><tr><td>0.6</td><td>1.61165288</td><td>1.61165136</td><td>-2.06863957</td><td>-2.06864136</td><td>1.12030805</td><td>1.12030352</td></tr><tr><td>0.8</td><td>0.68018456</td><td>0.68018509</td><td>-2.55509734</td><td>-2.55509679</td><td>0.53279799</td><td>0.53279513</td></tr><tr><td>1.0</td><td>-0.38624142</td><td>-0.38623744</td><td>-3.28600244</td><td>-3.28599682</td><td>-0.51213132</td><td>-0.51212857</td></tr></table>

(d)

<table><tr><td>ti</td><td>w1(ti)</td><td>u1(ti)</td><td>W2(ti)</td><td>u2(ti)</td><td>W3(ti)</td><td>u3(ti)</td></tr><tr><td>0.2</td><td>5.85399925</td><td>6.65519774</td><td>-6.58493690</td><td>-6.58258771</td><td>-5.51120222</td><td>-5.50771339</td></tr><tr><td>0.8</td><td>13.58890681</td><td>14.00287756</td><td>-2.95418927</td><td>-2.92102977</td><td>-4.51808620</td><td>-4.45343131</td></tr><tr><td>1.0</td><td>41.45180376</td><td>41.57707970</td><td>13.61528979</td><td>14.18586491</td><td>25.57139128</td><td>26.71881709</td></tr><tr><td>1.4</td><td>134.28466702</td><td>134.55509227</td><td>132.41529876</td><td>137.55271457</td><td>261.76615143</td><td>272.04668062</td></tr><tr><td>1.8</td><td>441.61837376</td><td>443.89480356</td><td>860.12763808</td><td>897.37318983</td><td>1716.71350110</td><td>1791.20854020</td></tr></table>

7. The Adams Fourth-Order Predictor-Corrector method for systems applied to the problems in Exercise 1 gives the results in the following tables.

(a)

<table><tr><td>ti</td><td>W1i</td><td>U1i</td><td>W2i</td><td>U2i</td></tr><tr><td>0.200</td><td>2.12036583</td><td>2.12500839</td><td>1.50699185</td><td>1.51158743</td></tr><tr><td>0.400</td><td>4.44122776</td><td>4.46511961</td><td>3.24224021</td><td>3.26598528</td></tr><tr><td>0.600</td><td>9.73913329</td><td>9.83235869</td><td>8.16341700</td><td>8.25629549</td></tr><tr><td>0.800</td><td>22.52673210</td><td>23.00263945</td><td>21.20273983</td><td>21.66887674</td></tr><tr><td>1.000</td><td>54.81242211</td><td>56.73748265</td><td>55.20490157</td><td>57.10536209</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>U2i</td></tr><tr><td>0.500</td><td>0.95675505</td><td>0.95672798</td><td>-1.08385916</td><td>-1.08383310</td></tr><tr><td>1.000</td><td>1.30659995</td><td>1.30655930</td><td>-0.83300571</td><td>-0.83296776</td></tr><tr><td>1.500</td><td>1.34420613</td><td>1.34418117</td><td>-0.56983853</td><td>-0.56981634</td></tr><tr><td>2.000</td><td>1.14334795</td><td>1.14333672</td><td>-0.36938396</td><td>-0.36937457</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>uli</td><td>W2i</td><td>u2i</td><td>W3i</td><td>u3i</td></tr><tr><td>0.5</td><td>0.70787076</td><td>0.70828683</td><td>-1.24988663</td><td>-1.25056425</td><td>0.39884862</td><td>0.39815702</td></tr><tr><td>1.0</td><td>-0.33691753</td><td>-0.33650854</td><td>-3.01764179</td><td>-3.01945051</td><td>-0.29932294</td><td>-0.30116868</td></tr><tr><td>1.5</td><td>-2.41332734</td><td>-2.41345688</td><td>-5.40523279</td><td>-5.40844686</td><td>-0.92346873</td><td>-0.92675778</td></tr><tr><td>2.0</td><td>-5.88968402</td><td>-5.89590551</td><td>-8.72213325</td><td>-8.71450036</td><td>-1.32972524</td><td>-1.32544426</td></tr></table>

(d)

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>U2i</td><td>W3i</td><td>u3i</td></tr><tr><td>0.2</td><td>1.38165297</td><td>1.38165325</td><td>1.00800000</td><td>1.00800000</td><td>-0.61833075</td><td>-0.61833075</td></tr><tr><td>0.5</td><td>1.90752882</td><td>1.90753184</td><td>1.12500000</td><td>1.12500000</td><td>-0.09090527</td><td>-0.09090566</td></tr><tr><td>0.7</td><td>2.25503040</td><td>2.25503620</td><td>1.34300000</td><td>1.34300000</td><td>0.26344040</td><td>0.26343970</td></tr><tr><td>1.0</td><td>2.83211032</td><td>2.83212056</td><td>2.00000000</td><td>2.00000000</td><td>0.88212163</td><td>0.88212056</td></tr></table>

8. The approximations for the swinging pendulum problems are given in the tables:

<table><tr><td colspan="2">(a)</td></tr><tr><td colspan="2"></td></tr><tr><td>ti</td><td>0</td></tr><tr><td colspan="2">1.0 -0.365903 2.0 -0.0150563</td></tr></table>

<table><tr><td rowspan="3">(b)</td><td></td></tr><tr><td></td></tr><tr><td>ti 0</td></tr><tr><td>1.0</td><td>-0.338253</td></tr><tr><td>2.0</td><td>-0.0862680</td></tr></table>

9. The predicted number of prey, $x _ { 1 i }$ , and predators, $x _ { 2 i }$ , are given in the following table.

<table><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>X1i</td><td>X2i</td></tr><tr><td>10</td><td>1.0</td><td>4393</td><td>1512</td></tr><tr><td>20</td><td>2.0</td><td>288</td><td>3175</td></tr><tr><td>30</td><td>3.0</td><td>32</td><td>2042</td></tr><tr><td>40</td><td>4.0</td><td>25</td><td>1258</td></tr></table>

10. The predicted number of prey, $x _ { 1 i }$ , and predators, $x _ { 2 i }$ , are given in the following table.

<table><tr><td colspan="4"></td></tr><tr><td>i</td><td>ti</td><td>W1i</td><td>W2i</td></tr><tr><td>6</td><td>1.2</td><td>2211</td><td>11469</td></tr><tr><td>12</td><td>2.4</td><td>175</td><td>17492</td></tr><tr><td>18</td><td>3.6</td><td>2</td><td>19704</td></tr></table>

A stable solution is $x _ { 1 } = 8 0 0 0$ and $x _ { 2 } = 4 0 0 0$ .

# Exercise Set 5.10, page 347

1. Let $L$ be the Lipschitz constant for $\phi$ . Then

$$
u _ { i + 1 } - v _ { i + 1 } = u _ { i } - v _ { i } + h [ \phi ( t _ { i } , u _ { i } , h ) - \phi ( t _ { i } , v _ { i } , h ) ] _ { \mathrm { t } }
$$

so

$$
\begin{array} { r } { \left| u _ { i + 1 } - v _ { i + 1 } \right| \leq ( 1 + h L ) | u _ { i } - v _ { i } | \leq ( 1 + h L ) ^ { i + 1 } | u _ { 0 } - v _ { 0 } | . } \end{array}
$$

2. $^ { * } ( \mathrm { a } )$ For the Adams-Bashforth Method,

F $^ { \ast } ( t _ { i } , h , w _ { i + 1 } , w _ { i } , w _ { i - 1 } , w _ { i - 2 } , w _ { i - 3 } ) = \frac { 1 } { 2 4 } \bigg [ 5 5 f ( t _ { i } , w _ { i } ) - 5 9 f ( t _ { i - 1 } , w _ { i - 1 } ) + 3 7 f ( t _ { i - 2 } , w _ { i - 2 } ) - 9 f ( t _ { i - 3 } , w _ { i - 1 } ) \bigg ]$ 3, wi−3), so if $f \equiv 0$ , then $F \equiv 0$ . The same result holds for the Adams-Moulton method.

(b) If $f$ has Lipschitz constant $L$ , then

$$
\begin{array} { r l r } {  { \vert F ( t _ { i } , h , w _ { i + 1 } , \dots , w _ { i - 3 } ) - F ( t _ { i } , h , v _ { i + 1 } , \dots , v _ { i - 3 } ) \vert \leq \frac { L } { 2 4 } \bigg [ 5 5 \vert w _ { i } - v _ { i } \vert + 5 9 \vert w _ { i - 1 } - v _ { i - 1 } \vert } } \\ & { } & { \qquad + 3 7 \vert w _ { i - 2 } - v _ { i - 2 } \vert + 9 \vert w _ { i - 3 } - v _ { i - 3 } \vert \bigg ] , } \end{array}
$$

so C $\begin{array} { r } { C = \frac { 5 9 } { 2 4 } L } \end{array}$ will suffice. A similar result holds for the Adams-Moulton method, but with $\begin{array} { r } { C = \frac { \mathrm { { 1 9 } } } { 2 4 } L } \end{array}$ .

3. By Exercise 31 in Section 5.4, we have

$$
\begin{array} { l c l } { \phi ( t , w , h ) } & { = } & { \displaystyle \frac { 1 } { 6 } f ( t , w ) + \frac { 1 } { 3 } f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f ( t , w ) \biggr ) } \\ & & { \displaystyle + \frac { 1 } { 3 } f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f ( t , w ) \biggr ) \biggr ) } \\ & & { \displaystyle + \frac { 1 } { 6 } f \biggl ( t + h , w + h f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f \biggl ( t + \frac { 1 } { 2 } h , w + \frac { 1 } { 2 } h f ( t , w ) \biggr ) \biggr ) \biggr ) , } \end{array}
$$

so

$$
\phi ( t , w , 0 ) = \frac { 1 } { 6 } f ( t , w ) + \frac { 1 } { 3 } f ( t , w ) + \frac { 1 } { 3 } f ( t , w ) + \frac { 1 } { 6 } f ( t , w ) = f ( t , w ) .
$$

$^ { * } 4$ . (a) Expand $y ( t _ { i + 1 } )$ and $y ( t _ { i + 2 } )$ in Taylor polynomials and simplify.

(b) $w _ { 2 } = 0 . 1 8 0 6 5 \approx y ( 0 . 2 ) = 0 . 1 8 1 2 7 , w _ { 5 } = 0 . 3 5 7 8 5 \approx y ( 0 . 5 ) = 0 . 3 9 3 4 7$ , $w _ { 7 } = 0 . 1 5 3 4 0 \approx$ $y ( 0 . 7 ) = 0 . 5 0 3 4 1$ , and $w _ { 1 0 } = - 9 . 7 8 2 2 \approx y ( 1 . 0 ) = 0 . 6 3 2 1 2$   
(c) $w _ { 2 0 } = - 6 0 . 4 0 2 \approx y ( 0 . 2 )$ , $w _ { 5 0 } = - 1 . 3 7 \times 1 0 ^ { 1 7 } \approx y ( 0 . 5 )$ , $w _ { 7 0 } = - 5 . 1 1 \times 1 0 ^ { 3 2 6 } \approx y ( 0 . 7 )$ , and $w _ { 1 0 0 } = - 1 . 1 6 \times 1 0 ^ { 4 1 } \approx y ( 1 . 0 )$   
(d) The method is consistent but not stable or convergent.

5. (a) The local truncation error is $\begin{array} { r } { \tau _ { i + 1 } = \frac { 1 } { 4 } h ^ { 3 } y ^ { ( 4 ) } ( \xi _ { i } ) } \end{array}$ , for some $\xi$ , where $t _ { i - 2 } < \xi _ { i } < t _ { i + 1 }$ . (b) The method is consistent but unstable and not convergent.

6. For $h = 0 . 1$ :

$w _ { 1 0 } = 0 . 3 6 7 8 8 2 6 \approx y ( 1 ) = 0 . 3 6 7 8 7 9 4$ , a $\mathrm { \Delta \ n d ~ } \ w _ { 1 0 0 } = 3 . 8 4 9 1 7 \approx y ( 1 0 ) = 0 . 0 0 0 0 4 5 4 .$ . For $h = 0 . 0 1$ : $w _ { 1 0 0 } = 0 . 3 6 7 8 7 9 4 \approx y ( 1 ) = 0 . 3 6 7 8 7 9 4$ and $w _ { 1 0 0 0 } = 0 . 0 0 0 1 0 9 1 \approx y ( 1 0 ) = 0 . 0 0 0 0 4 5 4$ .

7. The method is unstable.

\*8. $w _ { 2 } = 4 \varepsilon$ , $w _ { 3 } = 1 3 \varepsilon$ , $w _ { 4 } = 4 0 \varepsilon$ , $w _ { 5 } = 1 2 1 \varepsilon$ , $w _ { 6 } = 3 6 4 \varepsilon$

# Exercise Set 5.11, page 354

1. Euler’s method gives the results in the following tables.

<table><tr><td rowspan="7">*(a) 0.500</td><td>ti Wi</td><td>Yi</td></tr><tr><td>0.200 0.027182818</td><td>0.449328964</td></tr><tr><td>0.000027183</td><td>0.030197383</td></tr><tr><td>0.700 0.000000272</td><td>0.004991594</td></tr><tr><td>1.000 0.000000000</td><td>0.000335463</td></tr><tr><td></td><td></td></tr></table>

<table><tr><td colspan="2"></td><td rowspan="2">yi</td></tr><tr><td>ti</td><td>Wi</td></tr><tr><td>0.200</td><td>0.373333333</td><td>0.046105213</td></tr><tr><td>0.500</td><td>-0.093333333</td><td>0.250015133</td></tr><tr><td>0.700</td><td>0.146666667</td><td>0.490000277</td></tr><tr><td>1.000</td><td>1.333333333</td><td>1.000000001</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>Yi</td></tr><tr><td>0.500</td><td>16.47925</td><td>0.479470939</td></tr><tr><td>1.000</td><td>256.7930</td><td>0.841470987</td></tr><tr><td>1.500</td><td>4096.142</td><td>0.997494987</td></tr><tr><td>2.000</td><td>65523.12</td><td>0.909297427</td></tr></table>

<table><tr><td rowspan="2">ti</td><td>Wi</td><td>Yi</td></tr><tr><td>6.128259</td><td>1.000000001</td></tr><tr><td>0.200</td><td>-378.2574</td><td>1.000000000</td></tr><tr><td>0.500 0.700</td><td>-6052.063</td><td>1.000000000</td></tr><tr><td></td><td>387332.0</td><td>1.000000000</td></tr><tr><td>1.000</td><td></td><td></td></tr></table>

2. Euler’s method gives the results in the following tables.

<table><tr><td colspan="2">(a) ti Wi</td><td>Yi</td></tr><tr><td>0.2</td><td>1.4631026</td><td>1.5892822</td></tr><tr><td>0.4</td><td>1.5421118</td><td>1.6271500</td></tr><tr><td>0.6</td><td>1.8223081</td><td>1.8719059</td></tr><tr><td>0.8</td><td>2.2104643</td><td>2.2438566</td></tr><tr><td>1.0</td><td>2.6960402</td><td>2.7250198</td></tr></table>

<table><tr><td colspan="2">(b)</td><td></td></tr><tr><td>ti</td><td>Wi 0.2</td><td>yi 0.56787944</td></tr><tr><td colspan="3">0.2</td></tr><tr><td rowspan="2">0.4 0.6</td><td>0.4</td><td>0.44978707</td></tr><tr><td>0.6</td><td>0.60673795</td></tr><tr><td>0.8</td><td>0.8 1.00012341</td><td>0.80091188</td></tr><tr><td colspan="3">1.0 1.0</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>yi</td></tr><tr><td>1.25</td><td>0.2500008</td><td>0.48848225</td></tr><tr><td>1.75</td><td>-1.5816058</td><td>0.18657591</td></tr><tr><td>2.25</td><td>-13.2433087</td><td>0.08779149</td></tr><tr><td>2.75</td><td>-100.7565966</td><td>0.04808415</td></tr></table>

<table><tr><td colspan="2">ti Wi</td><td>yi</td></tr><tr><td>0.25</td><td>5.0000000</td><td>0.96217447</td></tr><tr><td>0.75</td><td>65.137212</td><td>0.73168856</td></tr><tr><td>1.25</td><td>1030.7344</td><td>0.31532236</td></tr><tr><td>1.75</td><td>16486.497</td><td>-0.17824606</td></tr></table>

3. The Runge-Kutta fourth order method gives the results in the following tables.

<table><tr><td colspan="2">(a) ti</td><td>Wi</td><td>Yi</td></tr><tr><td colspan="2"></td><td>0.45881186</td><td>0.44932896</td></tr><tr><td colspan="2">0.200 0.500</td><td>0.03181595</td><td>0.03019738</td></tr><tr><td colspan="2">0.700</td><td>0.00537013</td><td>0.00499159</td></tr><tr><td colspan="2">1.000</td><td>0.00037239</td><td>0.00033546</td></tr></table>

<table><tr><td colspan="2">(b) ti</td><td>Wi</td><td>yi</td></tr><tr><td colspan="2"></td><td>0.07925926</td><td>0.04610521</td></tr><tr><td colspan="2">0.200 0.500</td><td>0.25386145</td><td>0.25001513</td></tr><tr><td colspan="2">0.700</td><td>0.49265127</td><td>0.49000028</td></tr><tr><td colspan="2">1.000</td><td>1.00250560</td><td>1.00000000</td></tr><tr><td colspan="4">(c)</td></tr><tr><td></td><td>ti</td><td>Wi</td><td>yi</td></tr><tr><td></td><td>0.500</td><td>188.3082</td><td>0.47947094</td></tr><tr><td></td><td>1.000</td><td>35296.68</td><td>0.84147099</td></tr><tr><td></td><td>1.500</td><td>6632737</td><td>0.99749499</td></tr><tr><td>2.000</td><td></td><td>1246413200</td><td>0.90929743</td></tr></table>

<table><tr><td colspan="3">(d)</td></tr><tr><td>ti</td><td>Wi</td><td>yi</td></tr><tr><td>0.200</td><td>-215.7459</td><td>1.00000000</td></tr><tr><td>0.500</td><td>-555750.0</td><td>1.00000000</td></tr><tr><td>0.700</td><td>-104435653</td><td>1.00000000</td></tr><tr><td>1.000</td><td>-269031268010</td><td>1.00000000</td></tr></table>

4. The Runge-Kutta fourth order method gives the results in the following tables.

<table><tr><td rowspan=1 colspan=1>(a)</td><td rowspan=1 colspan=1>ti       Wi           Yi</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.2  1.5895980  1.5892822</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.4  1.6274132  1.6271500</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6  1.8720749  1.8719059</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.8  2.2439777  2.2438566</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.0 2.7251239  2.7250198</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td>ti 0.2</td><td></td><td>Wi 0.5822584</td><td>Yi 0.56787944</td></tr><tr><td>0.4</td><td></td><td>0.4537551</td><td>0.44978707</td></tr><tr><td>0.6</td><td></td><td>0.6075593</td><td>0.60673795</td></tr><tr><td></td><td>0.8</td><td>0.8010630</td><td>0.80091188</td></tr><tr><td></td><td>1.0</td><td>1.0001495</td><td>1.00012341</td></tr></table>

<table><tr><td colspan="2">(c) ti</td><td colspan="2"></td></tr><tr><td colspan="2"></td><td>Wi</td><td>yi</td></tr><tr><td colspan="2">1.25</td><td>0.8240614</td><td>0.48848225</td></tr><tr><td colspan="2">1.75</td><td>4.9786559</td><td>0.18657591</td></tr><tr><td colspan="2">2.25</td><td>66.9187958</td><td>0.08779149</td></tr><tr><td colspan="2">2.75</td><td>930.8525134</td><td>0.04808415</td></tr></table>

<table><tr><td colspan="4">d</td></tr><tr><td></td><td>ti</td><td>Wi</td><td>Yi</td></tr><tr><td></td><td>0.25</td><td>-12.8205769</td><td>0.96217447</td></tr><tr><td></td><td>0.75</td><td>-2591.69792</td><td>0.73168856</td></tr><tr><td></td><td>1.25</td><td>-487165.725</td><td>0.31532236</td></tr><tr><td></td><td>1.75</td><td>-91547464.8</td><td>-0.17824606</td></tr></table>

5. The Adams Fourth-Order Predictor-Corrector Algorithm gives the results in the following tables.

<table><tr><td colspan="2">(a) ti Wi</td><td></td><td>yi</td></tr><tr><td></td><td>0.200</td><td>0.4588119</td><td>0.4493290</td></tr><tr><td></td><td>0.500</td><td>-0.0112813</td><td>0.0301974</td></tr><tr><td></td><td>0.700</td><td>0.0013734</td><td>0.0049916</td></tr><tr><td></td><td>1.000</td><td>0.0023604</td><td>0.0003355</td></tr></table>

<table><tr><td colspan="2">(b) ti</td><td>Wi</td><td>Yi</td></tr><tr><td rowspan="3"></td><td>0.200</td><td>0.0792593</td><td>0.0461052</td></tr><tr><td>0.500</td><td>0.1554027</td><td>0.2500151</td></tr><tr><td>0.700</td><td>0.5507445</td><td>0.4900003</td></tr><tr><td></td><td>1.000</td><td>0.7278557</td><td>1.0000000</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti 0.500</td><td>Wi 188.3082</td><td>Yi 0.4794709</td></tr><tr><td>1.000</td><td>38932.03</td><td>0.8414710</td></tr><tr><td>1.500</td><td>9073607</td><td>0.9974950</td></tr><tr><td></td><td></td><td></td></tr><tr><td>2.000</td><td>2115741299</td><td>0.9092974</td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>Yi</td></tr><tr><td>0.200</td><td>-215.7459</td><td>1.000000001</td></tr><tr><td>0.500</td><td>-682637.0</td><td>1.000000000</td></tr><tr><td>0.700</td><td>-159172736</td><td>1.000000000</td></tr><tr><td>1.000</td><td>-566751172258</td><td>1.000000000</td></tr></table>

6. The Adams Fourth-Order Predictor-Corrector Algorithm gives the results in the following tables.

<table><tr><td colspan="3">(a)</td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.2</td><td>1.5895980</td><td>1.5892822</td></tr><tr><td>0.4</td><td>1.6263206</td><td>1.6271500</td></tr><tr><td>0.6</td><td>1.8709345</td><td>1.8719059</td></tr><tr><td>0.8</td><td>2.2432194</td><td>2.2438566</td></tr><tr><td>1.0</td><td>2.7246942</td><td>2.7250198</td></tr></table>

<table><tr><td rowspan=2 colspan=1>(b)</td><td rowspan=1 colspan=1>ti       Wi          y(ti)</td></tr><tr><td rowspan=1 colspan=1>0.2  0.5822584  0.56787944</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.4  0.3911238  0.44978707</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6  0.5971191  0.60673795</td></tr><tr><td rowspan=1 colspan=2>0.8  0.7826888  0.80091188</td></tr><tr><td rowspan=1 colspan=2>1.0  1.0082013  1.00012341</td></tr></table>

<table><tr><td colspan="3">(c)</td></tr><tr><td>ti</td><td>Wi 0.8240614</td><td>y(ti) 0.48848225</td></tr><tr><td>1.25 1.75</td><td>4.9786559</td><td>0.18657591</td></tr><tr><td>2.25</td><td>200.8236197</td><td>0.08779149</td></tr><tr><td>2.75</td><td>10272.0539300</td><td>0.04808415</td></tr><tr><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="3"></td></tr><tr><td>ti</td><td>Wi</td><td>y(ti)</td></tr><tr><td>0.25</td><td>-12.820577</td><td>0.96217447</td></tr><tr><td>0.75</td><td>-2591.6979</td><td>0.73168856</td></tr><tr><td>1.25</td><td>-598288.88</td><td>0.31532236</td></tr><tr><td>1.75</td><td>-139504990</td><td>-0.17824606</td></tr></table>

7. The Trapezoidal Algorithm gives the results in the following tables.

<table><tr><td rowspan="7">*(a)</td><td colspan="4"></td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>0.200</td><td>0.39109643</td><td>2</td><td>0.44932896</td></tr><tr><td>0.500</td><td>0.02134361</td><td>2</td><td>0.03019738</td></tr><tr><td>0.700</td><td>0.00307084</td><td>2</td><td>0.00499159</td></tr><tr><td>1.000</td><td>0.00016759</td><td>2</td><td>0.00033546</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>0.200</td><td>0.04000000</td><td>2</td><td>0.04610521</td></tr><tr><td>0.500</td><td>0.25000000</td><td>2</td><td>0.25001513</td></tr><tr><td>0.700</td><td>0.49000000</td><td>2</td><td>0.49000028</td></tr><tr><td>1.000</td><td>1.00000000</td><td>2</td><td>1.00000000</td></tr><tr><td colspan="4">(c)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>0.500</td><td>0.66291133</td><td>2</td><td>0.47947094</td></tr><tr><td>1.000</td><td>0.87506346</td><td>2</td><td>0.84147099</td></tr><tr><td>1.500</td><td>1.00366141</td><td>2</td><td>0.99749499</td></tr><tr><td>2.000</td><td>0.91053267</td><td>2</td><td>0.90929743</td></tr></table>

<table><tr><td colspan="2">(d) ti 0.200</td><td>Wi k</td><td></td><td>Yi</td></tr><tr><td colspan="2"></td><td>-1.07568307</td><td>4</td><td>1.00000000</td></tr><tr><td colspan="2">0.500</td><td>-0.97868360</td><td>4</td><td>1.00000000</td></tr><tr><td colspan="2">0.700</td><td>-0.99046408</td><td>3</td><td>1.00000000</td></tr><tr><td colspan="2">1.000</td><td>-1.00284456</td><td>3</td><td>1.00000000</td></tr></table>

8. The Trapezoidal Algorithm gives the results in the following tables.

<table><tr><td colspan="4">(a)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>y(ti)</td></tr><tr><td>0.2</td><td>1.58152229</td><td>2</td><td>1.5892822</td></tr><tr><td>0.4</td><td>1.62161373</td><td>2</td><td>1.6271500</td></tr><tr><td>0.6</td><td>1.86902118</td><td>2</td><td>1.8719059</td></tr><tr><td>0.8</td><td>2.24264359</td><td>2</td><td>2.2438566</td></tr><tr><td>1.0</td><td>2.72470482</td><td>2</td><td>2.7250198</td></tr></table>

<table><tr><td colspan="4">(b)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>y(ti)</td></tr><tr><td>0.2</td><td>0.50203131</td><td>2</td><td>0.56787944</td></tr><tr><td>0.4</td><td>0.43355903</td><td>2</td><td>0.44978707</td></tr><tr><td>0.6</td><td>0.60372878</td><td>2</td><td>0.60673795</td></tr><tr><td>0.8</td><td>0.80041431</td><td>2</td><td>0.80091188</td></tr><tr><td>1.0</td><td>1.00004603</td><td>2</td><td>1.00012341</td></tr></table>

<table><tr><td colspan="4">(c)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>y(ti)</td></tr><tr><td>1.25</td><td>0.49787835</td><td>2</td><td>0.48848225</td></tr><tr><td>1.75</td><td>0.18503499</td><td>2</td><td>0.18657591</td></tr><tr><td>2.25</td><td>0.08754204</td><td>2</td><td>0.08779149</td></tr><tr><td>2.75</td><td>0.04802381</td><td>2</td><td>0.04808415</td></tr></table>

<table><tr><td colspan="4">(d)</td></tr><tr><td>ti</td><td>Wi</td><td>k</td><td>y(ti)</td></tr><tr><td>0.25</td><td>1.39753016</td><td>2</td><td>0.96217447</td></tr><tr><td>0.75</td><td>0.81057360</td><td>2</td><td>0.73168856</td></tr><tr><td>1.25</td><td>0.33002435</td><td>2</td><td>0.31532236</td></tr><tr><td>1.75</td><td>-0.17533094</td><td>2</td><td>-0.17824606</td></tr></table>

9. The Runge-Kutta fourth-order method gives the results in the following tables.

(a)

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>U2i</td></tr><tr><td>0.100</td><td>-96.33011</td><td>0.66987648</td><td>193.6651</td><td>-0.33491554</td></tr><tr><td>0.200</td><td>-28226.32</td><td>0.67915383</td><td>56453.66</td><td>-0.33957692</td></tr><tr><td>0.300</td><td>-8214056</td><td>0.69387881</td><td>16428113</td><td>-0.34693941</td></tr><tr><td>0.400</td><td>-2390290586</td><td>0.71354670</td><td>4780581173</td><td>-0.35677335</td></tr><tr><td>0.500</td><td>-695574560790</td><td>0.73768711</td><td>1391149121600</td><td>-0.36884355</td></tr></table>

<table><tr><td>ti</td><td>W1i</td><td>u1i</td><td>W2i</td><td>u2i</td></tr><tr><td>0.100</td><td>0.61095960</td><td>0.66987648</td><td>-0.21708179</td><td>-0.33491554</td></tr><tr><td>0.200</td><td>0.66873489</td><td>0.67915383</td><td>-0.31873903</td><td>-0.33957692</td></tr><tr><td>0.300</td><td>0.69203679</td><td>0.69387881</td><td>-0.34325535</td><td>-0.34693941</td></tr><tr><td>0.400</td><td>0.71322103</td><td>0.71354670</td><td>-0.35612202</td><td>-0.35677335</td></tr><tr><td>0.500</td><td>0.73762953</td><td>0.73768711</td><td>-0.36872840</td><td>-0.36884355</td></tr></table>

10. Since $y ^ { \prime } = \lambda y$ , we have

$$
k _ { 1 } = h \lambda w _ { i } , \quad k _ { 2 } = h \lambda \big ( w _ { i } + h \lambda w _ { i } / 2 \big ) , \quad k _ { 3 } = h \lambda \big ( w _ { i } + h \lambda w _ { i } / 2 + h ^ { 2 } \lambda ^ { 2 } w _ { i } / 4 \big ) ,
$$

and

$$
k _ { 4 } = h \lambda \left( w _ { i } + h \lambda w _ { i } + h ^ { 2 } \lambda ^ { 2 } w _ { i } / 2 + h ^ { 3 } \lambda ^ { 3 } w _ { i } / 4 \right) .
$$

Thus

$$
\begin{array} { l } { { w _ { i + 1 } = w _ { i } + \displaystyle \frac { 1 } { 6 } ( k _ { 1 } + 2 k _ { 2 } + 2 k _ { 3 } + k _ { 4 } ) } } \\ { { \mathrm { } = w _ { i } + \displaystyle \frac { w _ { i } } { 6 } \left( h \lambda + 2 h \lambda + h ^ { 2 } \lambda ^ { 2 } + 2 h \lambda + h ^ { 2 } \lambda ^ { 2 } + h ^ { 3 } \lambda ^ { 3 } / 2 + h \lambda + h ^ { 2 } \lambda ^ { 2 } + \displaystyle \frac { 1 } { 2 } h ^ { 3 } \lambda ^ { 3 } + \displaystyle \frac { 1 } { 4 } h ^ { 4 } \lambda ^ { 4 } \right) } } \\ { { \mathrm { } = \left( 1 + h \lambda + \displaystyle \frac { 1 } { 2 } h ^ { 2 } \lambda ^ { 2 } + \displaystyle \frac { 1 } { 6 } h ^ { 3 } \lambda ^ { 3 } + \displaystyle \frac { 1 } { 2 4 } h ^ { 4 } \lambda ^ { 4 } \right) w _ { i } . } } \end{array}
$$

$^ *$ 11. Using Eq. (4.25) gives $\begin{array} { r } { \tau _ { i + 1 } = \frac { - y ^ { \prime \prime \prime } ( \xi _ { i } ) } { 1 2 } h ^ { 2 } } \end{array}$ , for some $t _ { i } < \xi _ { i } < t _ { i + 1 }$ , and by Definition 5.18, the Trapezoidal method is consistent. Once again using Eq. (4.25) gives

$$
y ( t _ { i + 1 } ) = y ( t _ { i } ) + { \frac { h } { 2 } } [ f ( t _ { i } , y ( t _ { i } ) ) + f ( t _ { i + 1 } , y ( t _ { i + 1 } ) ) ] - { \frac { y ^ { \prime \prime \prime } ( \xi _ { i } ) } { 1 2 } } h ^ { 3 } .
$$

Subtracting the difference equation and using the Lipschitz constant $L$ for $f$ gives

$$
| y ( t _ { i + 1 } ) - w _ { i + 1 } | \leq | y ( t _ { i } ) - w _ { i } | + \frac { h L } { 2 } | y ( t _ { i } ) - w _ { i } | + \frac { h L } { 2 } | y ( t _ { i + 1 } ) - w _ { i + 1 } | + \frac { h ^ { 3 } } { 1 2 } | y ^ { \prime \prime \prime } ( \xi _ { i } ) | .
$$

Let $M = \mathrm { m a x } _ { a \leq x \leq b } | y ^ { \prime \prime \prime } ( x ) |$ . Then, assuming $h L \neq 2$ ,

$$
| y ( t _ { i + 1 } ) - w _ { i + 1 } | \leq \frac { 2 + h L } { 2 - h L } | y ( t _ { i } ) - w _ { i } | + \frac { h ^ { 3 } } { 6 ( 2 - h L ) } M .
$$

Using Lemma 5.8, we have

$$
\left| y ( t _ { i + 1 } ) - w _ { i + 1 } \right| \leq e ^ { 2 ( b - a ) L / ( 2 - h L ) } \bigg [ \frac { M h ^ { 2 } } { 1 2 L } + | \alpha - w _ { 0 } | \bigg ] - \frac { M h ^ { 2 } } { 1 2 L } .
$$

So if $h L \neq 2$ , the Trapezoidal method is convergent, and consequently stable.

12. The Backward Euler method applied to $y ^ { \prime } = \lambda y$ gives

$$
w _ { i + 1 } = { \frac { w _ { i } } { 1 - h \lambda } } , \quad \mathrm { s o } \quad Q ( h \lambda ) = { \frac { 1 } { 1 - h \lambda } } .
$$

13. The following tables list the results of the Backward Euler method applied to the problems in Exercise 1.

(1a)

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>0.75298666</td><td>2</td><td>0.44932896</td></tr><tr><td>5</td><td>0.5</td><td>0.10978082</td><td>2</td><td>0.03019738</td></tr><tr><td>7</td><td>0.7</td><td>0.03041020</td><td>2</td><td>0.00499159</td></tr><tr><td>10</td><td>1.0</td><td>0.00443362</td><td>2</td><td>0.00033546</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>0.08148148</td><td>2</td><td>0.04610521</td></tr><tr><td>5</td><td>0.5</td><td>0.25635117</td><td>2</td><td>0.25001513</td></tr><tr><td>7</td><td>0.7</td><td>0.49515013</td><td>2</td><td>0.49000028</td></tr><tr><td>10</td><td>1.0</td><td>1.00500556</td><td>2</td><td>1.00000000</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.5</td><td>0.50495522</td><td>2</td><td>0.47947094</td></tr><tr><td>4</td><td>1.0</td><td>0.83751817</td><td>2</td><td>0.84147099</td></tr><tr><td>6</td><td>1.5</td><td>0.99145076</td><td>2</td><td>0.99749499</td></tr><tr><td>8</td><td>2.0</td><td>0.90337560</td><td>2</td><td>0.90929743</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>1.00348713</td><td>3</td><td>1.00000000</td></tr><tr><td>5</td><td>0.5</td><td>1.00000262</td><td>2</td><td>1.00000000</td></tr><tr><td>7</td><td>0.7</td><td>1.00000002</td><td>1</td><td>1.00000000</td></tr><tr><td>10</td><td>1.0</td><td>1.00000000</td><td>1</td><td>1.00000000</td></tr></table>

14. The following tables list the results of the Backward Euler method applied to the problems in Exercise 2.   

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>1.67216224</td><td>2</td><td>1.58928220</td></tr><tr><td>4</td><td>0.4</td><td>1.69987544</td><td>2</td><td>1.62715998</td></tr><tr><td>6</td><td>0.6</td><td>1.92400672</td><td>2</td><td>1.87190587</td></tr><tr><td>8</td><td>0.8</td><td>2.28233119</td><td>2</td><td>2.24385657</td></tr><tr><td>10</td><td>1.0</td><td>2.75757631</td><td>2</td><td>2.72501978</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>2</td><td>0.2</td><td>0.87957046</td><td>2</td><td>0.56787944</td></tr><tr><td>4</td><td>0.4</td><td>0.56989261</td><td>2</td><td>0.44978707</td></tr><tr><td>6</td><td>0.6</td><td>0.64247315</td><td>2</td><td>0.60673795</td></tr><tr><td>8</td><td>0.8</td><td>0.81061829</td><td>2</td><td>0.80091188</td></tr><tr><td>10</td><td>1.0</td><td>1.00265457</td><td>2</td><td>1.00012341</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>yi</td></tr><tr><td>1</td><td>1.25</td><td>0.55006309</td><td>2</td><td>0.51199999</td></tr><tr><td>3</td><td>1.75</td><td>0.19753128</td><td>2</td><td>0.18658892</td></tr><tr><td>5</td><td>2.25</td><td>0.09060118</td><td>2</td><td>0.08779150</td></tr><tr><td>7</td><td>2.75</td><td>0.04900207</td><td>2</td><td>0.04808415</td></tr></table>

<table><tr><td>i</td><td>ti</td><td>Wi</td><td>k</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>0.79711852</td><td>2</td><td>0.96217447</td></tr><tr><td>3</td><td>0.75</td><td>0.72203841</td><td>2</td><td>0.73168856</td></tr><tr><td>5</td><td>1.25</td><td>0.31248267</td><td>2</td><td>0.31532236</td></tr><tr><td>7</td><td>1.75</td><td>-0.17796016</td><td>2</td><td>-0.17824606</td></tr></table>

15. (a) The Trapezoidal method applied to the test equation gives

$$
w _ { j + 1 } = { \frac { 1 + { \frac { h \lambda } { 2 } } } { 1 - { \frac { h \lambda } { 2 } } } } ~ w _ { j } , \quad \mathrm { s o } \quad Q ( h \lambda ) = { \frac { 2 + h \lambda } { 2 - h \lambda } } .
$$

Thus, $| Q ( h \lambda ) | < 1$ , whenever $\mathrm { R e } ( h \lambda ) < 0$ .

(b) The Backward Euler method applied to the test equation gives

$$
w _ { j + 1 } = { \frac { w _ { j } } { 1 - h \lambda } } , \quad \mathrm { s o } \quad Q ( h \lambda ) = { \frac { 1 } { 1 - h \lambda } } .
$$

Thus, $| Q ( h \lambda ) | < 1$ , whenever $\mathrm { R e } ( h \lambda ) < 0$ .

# Direct Methods for Solving Linear Systems

# Exercise Set 6.1, page 368

1. \*(a) Intersecting lines with solution $x _ { 1 } = x _ { 2 } = 1$ . (b) One line, so there is an infinite number of solutions with $\begin{array} { r } { x _ { 2 } = \frac { 3 } { 2 } - \frac { 1 } { 2 } x _ { 1 } } \end{array}$ . (c) One line, so there is an infinite number of solutions with $\begin{array} { r } { x _ { 2 } = - \frac { 1 } { 2 } x _ { 1 } } \end{array}$ . \*(d) Intersecting lines with solution $\textstyle x _ { 1 } = { \frac { 2 } { 7 } }$ and $\textstyle x _ { 2 } = - { \frac { 1 1 } { 7 } }$ .

2. (a) Intersecting lines whose solution is $x _ { 1 } = x _ { 2 } = 0$ . (b) Parallel lines, so there is no solution. (c) Three lines in the plane that do not intersect at a common point. (d) Two planes in space which intersect in a line with $\textstyle x _ { 1 } = - { \frac { 5 } { 4 } } x _ { 2 }$ and $\begin{array} { r } { x _ { 3 } = \frac { 3 } { 2 } x _ { 2 } + 1 } \end{array}$

3. Gaussian elimination gives the following solutions.

(a) $x _ { 1 } = 1 . 0$ , $x _ { 2 } = - 0 . 9 8$ , x3 = 2.9 (b) $x _ { 1 } = 1 . 1$ , $x _ { 2 } = - 1 . 1$ , $x _ { 3 } = 2 . 9$

4. Gaussian elimination gives the following solutions.

$$
\begin{array} { l l } { { x _ { 1 } = - 0 . 7 0 , x _ { 2 } = 1 . 1 , x _ { 3 } = 2 . 9 } } \\ { { \nonumber } } \\ { { x _ { 1 } = - 0 . 8 8 , x _ { 2 } = 0 . 7 4 , x _ { 3 } = 3 . 0 } } \end{array}
$$

5. Gaussian elimination gives the following solutions.

\*(a) $x _ { 1 } = 1 . 1 8 7 5 , x _ { 2 } = 1 . 8 1 2 5 , x _ { 3 } = 0 . 8 7 5$ with one row interchange required (b) $x _ { 1 } = - 1 , x _ { 2 } = 0 , x _ { 3 } = 1$ with no interchange required (c) $x _ { 1 } = 1 . 5 , x _ { 2 } = \mathrm { { ^ 2 } } , x _ { 3 } = - 1 . 2 , x _ { 4 } = \mathrm { { ^ 3 } }$ with no interchange required (d) No unique solution

6. Gaussian elimination gives the following solutions.

(a) $x _ { 1 } = - 4$ , $x _ { 2 } = - 8$ , $x _ { 3 } = - 6$ with one row interchange required (b) $\textstyle x _ { 1 } = { \frac { 2 2 } { 9 } }$ , $\textstyle x _ { 2 } = - { \frac { 4 } { 9 } }$ , $x _ { 3 } = { \textstyle { \frac { 4 } { 3 } } } , x _ { 4 } = 1$ with one row interchange required

(c) $x _ { 1 } = 1 3$ , $x _ { 2 } = 8$ , $x _ { 3 } = 8 , x _ { 4 } = 5$ with one row interchange required.   
(d) $x _ { 1 } = - 1$ , $x _ { 2 } = 2$ , $x _ { 3 } = 0 , x _ { 4 } = 1$ with one row interchange required.

7. Gaussian elimination with Digits:=10 gives the following solutions:

(a) $x _ { 1 } = - 2 2 7 . 0 7 6 9$ , $x _ { 2 } = 4 7 6 . 9 2 3 1$ , $x _ { 3 } = - 1 7 7 . 6 9 2 3$ ;   
(b) $x _ { 1 } = 1 . 0 0 1 2 9 1$ , $x _ { 2 } = 1$ , $x _ { 3 } = 1 . 0 0 1 5 5$ ;   
(c) $x _ { 1 } = - 0 . 0 3 1 7 4 6 0 0$ , $x _ { 2 } = 0 . 5 9 5 2 3 7 7$ , $x _ { 3 } = - 2 . 3 8 0 9 5 1$ , $x _ { 4 } = 2 . 7 7 7 7 7 7 7$ ;   
(d) $x _ { 1 } = 1 . 9 1 8 1 2 9$ , $x _ { 2 } = 1 . 9 6 4 9 1 2$ , $x _ { 3 } = - 0 . 9 8 8 3 0 4 1$ , $x _ { 4 } = - 3 . 1 9 2 9 8 2$ , $x _ { 5 } = - 1 . 1 3 4 5 0 3$ .

8. Gaussian elimination with Digits:=10 gives the following solutions:

(a) $x _ { 1 } = 0 . 9 7 9 8 6 5 7 7 2 0$ , $x _ { 2 } = 4 . 2 8 1 8 7 9 1 9 1$ , $x _ { 3 } = 1 7 . 4 8 3 2 2 1 4 7$ ;   
(b) $x _ { 1 } = 6 . 4 6 1 4 4 7 6 2 0$ , $x _ { 2 } = 8 . 3 9 4 3 2 1 0 9 2$ , $x _ { 3 } = - 0 . 0 1 3 4 7 3 6 8 6 1 8$ ;   
(c) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 9$ , $x _ { 2 } = - 4 . 6 7 7 9 8 7 7 6$ , $x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 9$ , $x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2$ ;   
(d) $x _ { 1 } = 1 3 . 4 9 9 9 9 9 9 8$ , $x _ { 2 } = - 1 1 . 5 0 0 0 0 0 0 0 0 0 0$ , $x _ { 3 } = 2 3 . 7 5 0 0 0 0 0 3$ , $x _ { 4 } = 1 2 1 . 5 0 0 0 0 3 , x _ { 5 } =$ 97.75000025.

$^ { * } 9$ . (a) When $\alpha = - 1 / 3$ , there is no solution. (b) When $\alpha = 1 / 3$ , there is an infinite number of solutions with $x _ { 1 } = x _ { 2 } + 1 . 5$ , and $x _ { 2 }$ is arbitrary. (c) If $\alpha \neq \pm 1 / 3$ , then the unique solution is

$$
x _ { 1 } = \frac { 3 } { 2 ( 1 + 3 \alpha ) } \quad \mathrm { a n d } \quad x _ { 2 } = \frac { - 3 } { 2 ( 1 + 3 \alpha ) } .
$$

10. (a) $\alpha = 1$ (b) $\alpha = - 1$ (c) $x _ { 1 } = - 1 / ( 1 - \alpha ) , x _ { 2 } = 1 , x _ { 3 } = 1 / ( 1 - \alpha )$

11. Suppose $x _ { 1 } ^ { \prime } , . . . , x _ { n } ^ { \prime }$ is a solution to the linear system (6.1).

(i) The new system becomes

$$
\begin{array} { c } { E _ { 1 } : a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + . . . + a _ { 1 n } x _ { n } = b _ { 1 } } \\ { \ \qquad \vdots } \\ { E _ { i } : \lambda a _ { i 1 } x _ { 1 } + \lambda a _ { i 2 } x _ { 2 } + . . . + \lambda a _ { i n } x _ { n } = \lambda b _ { i } } \\ { \ \qquad \vdots } \\ { E _ { n } : a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + . . . + a _ { n n } x _ { n } = b _ { n } . } \end{array}
$$

Clearly, $x _ { 1 } ^ { \prime } , . . . , x _ { n } ^ { \prime }$ satisfies this system. Conversely, if $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ satisfies the new system, dividing $E _ { i }$ by $\lambda$ shows $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ also satisfies (6.1).

(ii) The new system becomes

$$
\begin{array} { c } { E _ { 1 } : a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + . . . + a _ { 1 n } x _ { n } = b _ { 1 } } \\ { \ } \\ { \vdots } \\ { E _ { i } : ( a _ { i 1 } + \lambda a _ { j 1 } ) x _ { 1 } + ( a _ { i 2 } + \lambda a _ { j 2 } ) x _ { 2 } + . . . + ( a _ { i n } + \lambda a _ { j n } ) x _ { n } = b _ { i } + \lambda b _ { j } } \\ { \ } \\ { \vdots } \\ { E _ { n } : a _ { n 1 } x _ { 1 } + a _ { n 2 } x _ { 2 } + . . . + a _ { n n } x _ { n } = b _ { n } . } \end{array}
$$

Clearly, $x _ { 1 } ^ { \prime } , . . . , x _ { n } ^ { \prime }$ satisfies all but possibly the $i$ th equation. Multiplying $E _ { j }$ by $\lambda$ gives

$$
\lambda a _ { j 1 } x _ { 1 } ^ { \prime } + \lambda a _ { j 2 } x _ { 2 } ^ { \prime } + . . . + \lambda a _ { j n } x _ { n } ^ { \prime } = \lambda b _ { j } ,
$$

which can be subtracted from $E _ { i }$ in the new system results in the system (6.1). Thus, $x _ { 1 } ^ { \prime } , . . . , x _ { n } ^ { \prime }$ satisfies the new system. Conversely, if $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ is a solution to the new system, then all but possibly $E _ { i }$ of (6.1) are satisfied by $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ . Multiplying $E _ { j }$ of the new system by $- \lambda$ gives

$$
- \lambda a _ { j 1 } x _ { 1 } ^ { * } - \lambda a _ { j 2 } x _ { 2 } ^ { * } - . . . - \lambda a _ { j n } x _ { n } ^ { * } = - \lambda b _ { j } .
$$

Adding this to $E _ { i }$ in the new system produces $E _ { i }$ of (6.1). Thus, $x _ { 1 } ^ { * } , . . . , x _ { n } ^ { * }$ is a solution of (6.1).

(iii) The new system and the old system have the same set of equations to satisfy. Thus, they have the same solution set.

\*12. Change Algorithm 6.1 as follows:

STEP 1 For $i = 1 , \ldots , n$ do STEPS 2, 3, and 4.   
STEP 4 For $j = 1 , \dotsc , i - 1 , i + 1 , \dotsc , n$ do STEPS 5 and 6.   
STEP 8 For $i = 1 , \ldots , n$ set $x _ { i } = a _ { i , n + 1 } / a _ { i i }$ .

In addition, delete STEP 9.

13. The Gauss-Jordan method gives the following results.

(a) $x _ { 1 } = 0 . 9 8 , x _ { 2 } = - 0 . 9 8 , x _ { 3 } = 2 . 9$ (b) $x _ { 1 } = 1 . 1 , x _ { 2 } = - 1 . 0 , x _ { 3 } = 2 . 9$

14. The Gauss-Jordan method with single precision arithmetic gives the following solutions.

(a) $x _ { 1 } = - 2 2 7 . 0 7 8 7$ , $x _ { 2 } = 4 7 6 . 9 2 6 \div 2$ , $x _ { 3 } = - 1 7 7 . 6 9 3 4$   
(b) $x _ { 1 } = 1 . 0 0 0 0 3 6$ , $x _ { 2 } = 0 . 9 9 9 9 9 9 1$ , $x _ { 3 } = 0 . 9 9 8 6 0 5 2$   
(c) $x _ { 1 } = - 0 . 0 3 1 7 7 1 2 0$ , $x _ { 2 } = 0 . 5 9 5 5 5 7 2$ , $x _ { 3 } = - 2 . 3 8 1 7 6 8$ , $x _ { 4 } = 2 . 7 7 8 3 2 9$   
(d) $x _ { 1 } = 1 . 9 1 8 1 2 9$ , $x _ { 2 } = 1 . 9 6 4 9 1 2$ , $x _ { 3 } = - 0 . 9 8 8 3 0 3 6$ , $x _ { 4 } = - 3 . 1 9 2 9 8 2$ , $x _ { 5 } = - 1 . 1 3 4 5 0 3$

\*15. The results for are listed in the following table. (The abbreviations M/D and A/S are used for multiplications/divisions and additions/subtractions, respectively.)   

<table><tr><td colspan="3">Gaussian elimination</td><td colspan="2">Gauss-Jordan</td></tr><tr><td>n</td><td>M/D</td><td>A/S</td><td>M/D</td><td>A/S</td></tr><tr><td>3</td><td>17</td><td>11</td><td>21</td><td>12</td></tr><tr><td>10</td><td>430</td><td>375</td><td>595</td><td>495</td></tr><tr><td>50</td><td>44150</td><td>42875</td><td>64975</td><td>62475</td></tr><tr><td>100</td><td>343300</td><td>338250</td><td>509950</td><td>499950</td></tr></table>

\*16. (a) The Gaussian elimination procedure requires

and

$$
{ \frac { n ^ { 3 } - n } { 3 } } ~ \mathrm { A d d i t i o n s } / \mathrm { S u b t r a c t i o n s } .
$$

The additional elimination steps are:

$$
\mathrm { F o r } \ i = n , n - 1 , . . . , 2
$$

$$
\mathrm { s e t } a _ { j , n + 1 } = a _ { j , n + 1 } - \frac { a _ { j i } a _ { i , n + 1 } } { a _ { i i } } .
$$

This requires

and

$$
\frac { n ( n - 1 ) } { 2 } \mathrm { \ A d d i t i o n s / S u b t r a c t i o n s } .
$$

Solving for

$$
x _ { i } = \frac { a _ { i , n + 1 } } { a _ { i i } }
$$

requires $n$ divisions. Thus, the totals are

$$
\mathrm { ~ \frac { \it { n ^ { 3 } } } { 3 } + \frac { 3 \it { n ^ { 2 } } } { 2 } - \frac { 5 \it { n } } { 6 } M u l t i p l i c a t i o n s / D i v i s i o n s }
$$

and

$$
{ \frac { n ^ { 3 } } { 3 } } + { \frac { n ^ { 2 } } { 2 } } - { \frac { 5 n } { 6 } } ~ { \mathrm { A d d i t i o n s / S u b t r a c t i o n s } } .
$$

(b) The results are listed in the following table. In this table the abbreviations M/D and A/S are used for Multiplications/Divisions and for Additions/Subtractions, respectively.   

<table><tr><td colspan="3">Gaussian Elimination</td><td colspan="2">Gauss-Jordan</td><td colspan="2">Hybrid</td></tr><tr><td>n</td><td>M/D</td><td>A/S</td><td>M/D</td><td>A/S</td><td>M/D</td><td>A/S</td></tr><tr><td>3</td><td>17</td><td>11</td><td>21</td><td>12</td><td>20</td><td>11</td></tr><tr><td>10</td><td>430</td><td>375</td><td>595</td><td>495</td><td>475</td><td>375</td></tr><tr><td>50</td><td>44150</td><td>42875</td><td>64975</td><td>62475</td><td>45375</td><td>42875</td></tr><tr><td>100</td><td>343300</td><td>338250</td><td>509950</td><td>499950</td><td>348250</td><td>338250</td></tr></table>

17. The Gaussian-Elimination–Gauss-Jordan hybrid method gives the following results.

(a) $x _ { 1 } = 1 . 0 , x _ { 2 } = - 0 . 9 8 , x _ { 3 } = 2 . 9$ (b) $x _ { 1 } = 1 . 0 , x _ { 2 } = - 1 . 0 , x _ { 3 } = 2 . 9$

18. The Gauss-Jordan hybrid method with single-precision arithmetic gives the following solutions.

(a) 227.0788, 476.9262, 177.6934   
(b) 0.9990999, 0.9999991, 0.9986052   
(c) −0.03177060, 0.5955554, −2.381768, 2.778329   
(d) $x _ { 1 } = 1 . 9 1 8 1 2 6$ , $x _ { 2 } = 1 . 9 6 4 9 1 6$ , $x _ { 3 } = - 0 . 9 8 8 3 0 2 7$ , $x _ { 4 } = - 3 . 1 9 2 9 8 2$ , $x _ { 5 } = - 1 . 1 3 4 5 0 3$

19. (a) There is sufficient food to satisfy the average daily consumption.

(b) We could add 200 of species 1, or 150 of species 2, or 100 of species 3, or 100 of species 4.   
(c) Assuming none of the increases indicated in part (b) was selected, species 2 could be increased by 650, or species 3 could be increased by 150, or species 4 could be increased by 150.   
(d) Assuming none of the increases indicated in parts (b) or (c) were selected, species 3 could be increased by 150, or species 4 could be increased by 150.

$^ *$ 20. (a) For the Trapezoidal rule $m = n = 1$ , $x _ { 0 } = 0$ , $x _ { 1 } = 1$ so that for $i = 0$ and 1, we have

$$
\begin{array} { l } { { \displaystyle u ( x _ { i } ) = f ( x _ { i } ) + \int _ { 0 } ^ { 1 } K ( x _ { i } , t ) u ( t ) ~ d t } } \\ { { \displaystyle \quad = f ( x _ { i } ) + \frac { 1 } { 2 } \left[ K ( x _ { i } , 0 ) u ( 0 ) + K ( x _ { i } , 1 ) u ( 1 ) \right] . } } \end{array}
$$

Substituting for $x _ { i }$ gives the desired equations.

(b) We have $n = 4$ , $\begin{array} { r } { h = \frac { 1 } { 4 } } \end{array}$ , $x _ { 0 } = 0$ , $\textstyle x _ { 1 } = { \frac { 1 } { 4 } }$ , $\begin{array} { r } { x _ { 2 } = \frac { 1 } { 2 } } \end{array}$ , $\textstyle x _ { 3 } = { \frac { 3 } { 4 } }$ , and $x _ { 4 } = 1$ , so

$$
\begin{array} { l } { { \displaystyle u ( x _ { i } ) = f ( x _ { i } ) + \frac { h } { 2 } \biggl [ K ( x _ { i } , 0 ) u ( 0 ) + 2 K \left( x _ { i } , \frac 1 4 \right) u \left( \frac 1 4 \right) } } \\ { { \displaystyle \phantom { \frac { 1 } { 1 } } + 2 K \left( x _ { i } , \frac 1 2 \right) u \left( \frac 1 2 \right) + 2 K \left( x _ { i } , \frac 3 4 \right) u \left( \frac 3 4 \right) + K ( x _ { i } , 1 ) u ( 1 ) \biggr ] , } } \end{array}
$$

for $i = { 0 , 1 , 2 , 3 , 4 }$ . This gives

$$
( x _ { i } ) = x _ { i } ^ { 2 } + \frac { 1 } { 8 } \left[ e ^ { x _ { i } } u ( 0 ) + 2 e ^ { \left| x _ { i } - \frac { 1 } { 4 } \right| } u \left( \frac { 1 } { 4 } \right) + 2 e ^ { \left| x _ { i } - \frac { 1 } { 2 } \right| } u \left( \frac { 1 } { 2 } \right) + 2 e ^ { \left| x _ { i } - \frac { 3 } { 4 } \right| } u \left( \frac { 3 } { 4 } \right) + e ^ { \left| x _ { i } - 1 \right| } u ( 1 ) \right] ,
$$

for each $i = 1 , \ldots , 4$ . The $5 \times 5$ linear system has solution $u ( 0 ) = - 1 . 1 5 4 2 5 5$ , $\begin{array} { l } { { u \left( \frac 1 4 \right) = } } \end{array}$ $- 0 . 9 0 9 3 2 9 8$ , $\begin{array} { r } { u \left( \frac { 1 } { 2 } \right) = - 0 . 7 1 5 3 1 4 5 } \end{array}$ , $\begin{array} { r } { u \left( \frac { 3 } { 4 } \right) = - 0 . 5 4 7 2 9 4 9 } \end{array}$ , and $u ( 1 ) = - 0 . 3 9 3 1 2 6 1$ .

(c) The Composite Simpson’s rule gives

$$
\begin{array} { c l l } { \displaystyle \int _ { 0 } ^ { 1 } K ( x _ { i } , t ) u ( t ) \ d t = \frac { h } { 3 } \left[ K ( x _ { i } , 0 ) u ( 0 ) + 4 K \left( x _ { i } , \frac 1 4 \right) u \left( \frac 1 4 \right) + 2 K \left( x _ { i } , \frac 1 2 \right) u \left( \frac 1 2 \right) + \right. } \\ { \displaystyle \left. 4 K \left( x _ { i } , \frac 3 4 \right) u \left( \frac 3 4 \right) + K ( x _ { i } , 1 ) u ( 1 ) \right] , } \end{array}
$$

which results in the linear equations

$$
( x _ { i } ) = x _ { i } ^ { 2 } + { \frac { 1 } { 1 2 } } \left[ e ^ { x _ { i } } u ( 0 ) + 4 e ^ { \left| x _ { i } - { \frac { 1 } { 4 } } \right| } u \left( { \frac { 1 } { 4 } } \right) + 2 e ^ { \left| x _ { i } - { \frac { 1 } { 2 } } \right| } u \left( { \frac { 1 } { 2 } } \right) + 4 e ^ { \left| x _ { i } - { \frac { 3 } { 4 } } \right| } u \left( { \frac { 3 } { 4 } } \right) + e ^ { \left| x _ { i } - 1 \right| } u ( 1 ) \right] .
$$

The $5 \times 5$ linear system has solutions $u ( 0 ) = - 1 . 2 3 4 2 8 6$ , $\begin{array} { r } { u \left( \frac { 1 } { 4 } \right) = - 0 . 9 5 0 7 2 9 2 } \end{array}$ , $\begin{array} { l } { { u \left( \frac 1 2 \right) = } } \end{array}$ $- 0 . 7 6 5 9 4 0 0$ , $\begin{array} { r } { u \left( \frac { 3 } { 4 } \right) = - 0 . 5 8 4 4 7 3 7 } \end{array}$ , and $u ( 1 ) = - 0 . 4 4 8 4 9 7 5$ .

# Exercise Set 6.2, page 379

1. The following row interchanges are required for these systems.

(a) none   
\*(b) Interchange rows 2 and 3. (c) none   
(d) Interchange rows 1 and 2.

2. The following row interchanges are required for these systems.

(a) none (b) none (c) none (d) none

3. The following row interchanges are required for these systems.

(a) Interchange rows 1 and 2. \*(b) Interchange rows 1 and 3. (c) Interchange rows 1 and 2, then interchange rows 2 and 3. (d) Interchange rows 1 and 2.

4. The following row interchanges are required for these systems.

(a) Interchange rows 2 and 3.   
(b) Interchange rows 1 and 3.   
(c) Interchange rows 1 and 3, then interchange rows 2 and 3.   
(d) Interchange rows 1 and 2.

5. The following row interchanges are required for these systems.

(a) Interchange rows 1 and 3, then interchange rows 2 and 3.   
\*(b) Interchange rows 2 and 3.   
(c) Interchange rows 2 and 3.   
(d) Interchange rows 1 and 3, then interchange rows 2 and 3.

6. The following row interchanges are required for these systems.

(a) Interchange rows 2 and 3.  
(b) none  
(c) Interchange rows 1 and 2, then interchange rows 2 and 3.(d) none

7. The following row interchanges are required for these systems.

(a) Interchange rows 1 and 2, and columns 1 and 3, then interchange rows 2 and 3, and columns 2 and 3.   
\*(b) Interchange rows 1 and 2, and columns 1 and 3, then interchange rows 2 and 3.   
(c) Interchange rows 1 and 2, and columns 1 and 3, then interchange rows 2 and 3. (d) Interchange rows 1 and 2, and columns 1 and 2, then interchange rows 2 and 3; and columns 2 and 3.

8. The following row interchanges are required for these systems.

(a) Interchange rows 1 and 2, and columns 1 and 3.   
(b) Interchange rows 1 and 2, and columns 1 and 2, then interchange rows 2 and 3.   
(c) Interchange rows 1 and 3, and columns 1 and 2, then interchange rows 2 and 3, and columns 2 and 3.   
(d) Interchange rows 1 and 2.

9. Gaussian elimination with three-digit chopping arithmetic gives the following results.

$$
\begin{array} { l l } { { } } & { { x _ { 1 } = 3 0 . 0 , x _ { 2 } = 0 . 9 9 0 } } \\ { { } } & { { x _ { 1 } = 0 . 0 0 , x _ { 2 } = 1 0 . 0 , x _ { 3 } = 0 . 1 4 2 } } \\ { { } } & { { x _ { 1 } = 0 . 2 0 6 , x _ { 2 } = 0 . 0 1 5 4 , x _ { 3 } = - 0 . 0 1 5 6 , x _ { 4 } = - 0 . 7 1 6 } } \\ { { } } & { { x _ { 1 } = 0 . 8 2 8 , x _ { 2 } = - 3 . 3 2 , x _ { 3 } = 0 . 1 5 3 , x _ { 4 } = 4 . 9 1 } } \end{array}
$$

10. Gaussian elimination with three-digit chopping arithmetic gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 9 . 9 8$

(b) $x _ { 1 } = 1 2 . 0$ , $x _ { 2 } = 0 . 4 9 2 , x _ { 3 } = - 9 . 7 8$ (c) $\begin{array} { l } { { \begin{array} { r l } & { \cdots \mathrm { ~ s - y ~ } , \cdots } \\ & { x _ { 1 } = - 8 . 2 5 , x _ { 2 } = - 8 . 0 0 , x _ { 3 } = - 0 . 0 3 3 9 , x _ { 4 } = 0 . 0 5 6 6 } \end{array} } } \\ { { \begin{array} { r l } & { x _ { 1 } = 1 . 3 3 , x _ { 2 } = - 4 . 6 6 , x _ { 3 } = - 4 . 0 4 , x _ { 4 } = - 1 . 6 6 } \end{array} } } \end{array}$ (d)

11. Gaussian elimination with three-digit rounding arithmetic gives the following results.

(a) $x _ { 1 } = - 1 0 . 0$ , $x _ { 2 } = 1 . 0 1$ (b) $x _ { 1 } = 0 . 0 0$ , $x _ { 2 } = 1 0 . 0$ , $x _ { 3 } = 0 . 1 4 3$ (c) $x _ { 1 } = 0 . 1 8 5$ , $x _ { 2 } = 0 . 0 1 0 3$ , $x _ { 3 } = - 0 . 0 2 0 0$ , $x _ { 4 } = - 1 . 1 2$ (d) $x _ { 1 } = 0 . 7 9 9$ , $x _ { 2 } = - 3 . 1 2$ , $x _ { 3 } = 0 . 1 5 1$ , $x _ { 4 } = 4 . 5 6$

12. Gaussian elimination with three-digit rounding arithmetic gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 1 0 . 0$ (b) $x _ { 1 } = 1 2 . 0$ , $x _ { 2 } = 0 . 4 9 9$ , $x _ { 3 } = - 1 . 9 8$ (c) x1 = 0.0896, x2 = −0.0639, x3 = −0.0361, x4 = 0.0467 (d) $\mathfrak { c } _ { 1 } = 1 . 3 5 , x _ { 2 } = - 4 . 7 3 , x _ { 3 } = - 4 . 0 7 , x _ { 4 } = - 1 . 6 5$

13. Gaussian elimination with partial pivoting and three-digit chopping arithmetic gives the following results.

\*(a) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$ (b) $x _ { 1 } = - 0 . 1 6 3$ , $x _ { 2 } = 9 . 9 8 , x _ { 3 } = 0 . 1 4 2$ (c) $x _ { 1 } = 0 . 1 7 7$ , $x _ { 2 } = - 0 . 0 0 7 2$ , $x _ { 3 } = - 0 . 0 2 0 8$ , $x _ { 4 } = - 1 . 1 8$ (d) $x _ { 1 } = 0 . 7 7 7$ , $x _ { 2 } = - 3 . 1 0$ , $x _ { 3 } = 0 . 1 6 1$ , $x _ { 4 } = 4 . 5 0$

14. Gaussian elimination with partial pivoting gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 9 . 9 8$ (b) $x _ { 1 } = 1 2 . 0$ , $x _ { 2 } = 0 . 5 0 4$ , $x _ { 3 } = - 9 . 7 8$ (d) (c) $\begin{array} { l } { { x _ { 1 } = 0 . 0 9 2 8 , x _ { 2 } = - 0 . 0 6 3 1 , x _ { 3 } = - 0 . 0 3 5 6 , x _ { 4 } = 0 . 0 4 6 8 } } \\ { { \nonumber } } \\ { { x _ { 1 } = 1 . 3 3 , x _ { 2 } = - 4 . 6 6 , x _ { 3 } = - 4 . 0 4 , x _ { 4 } = - 1 . 6 6 } } \end{array}$

15. Gaussian elimination with partial pivoting and three-digit rounding arithmetic gives the following results.

(a) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$ (b) $x _ { 1 } = 0 . 0 0$ , $x _ { 2 } = 1 0 . 0$ , $x _ { 3 } = 0 . 1 4 3$ (c) $x _ { 1 } = 0 . 1 7 8$ , $x _ { 2 } = 0 . 0 1 2 7$ , $x _ { 3 } = - 0 . 0 2 0 4$ , $x _ { 4 } = - 1 . 1 6$ (d) $x _ { 1 } = 0 . 8 4 5$ , $x _ { 2 } = - 3 . 3 7$ , $x _ { 3 } = 0 . 1 8 \mathrm { { 2 } }$ , $x _ { 4 } = 5 . 0 7$

16. Gaussian elimination with partial pivoting and three-digit chopping arithmetic gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 1 0 . 0$ (b) $x _ { 1 } = 1 2 . 0$ , $x _ { 2 } = 0 . 4 9 9$ , $x _ { 3 } = - 1 . 9 8$

$$
\begin{array} { l } { { x _ { 1 } = 0 . 0 9 2 7 , x _ { 2 } = - 0 . 0 6 3 1 , x _ { 3 } = - 0 . 0 3 6 2 , x _ { 4 } = 0 . 0 4 6 5 } } \\ { { \nonumber } } \\ { { x _ { 1 } = 1 . 3 5 , x _ { 2 } = - 4 . 7 3 , x _ { 3 } = - 4 . 0 7 , x _ { 4 } = - 1 . 6 5 } } \end{array}
$$

17. Gaussian elimination with scaled partial pivoting and three-digit chopping arithmetic gives the following results.

$$
\begin{array} { l } { { = 1 0 . 0 , x _ { 2 } = 1 . 0 0 } } \\ { { = - 0 . 1 6 3 , x _ { 2 } = 9 . 9 8 , x _ { 3 } = 0 . 1 4 2 } } \\ { { = 0 . 1 7 1 , x _ { 2 } = 0 . 0 1 0 2 , x _ { 3 } = - 0 . 0 2 1 7 , x _ { 4 } = - 1 . 2 7 } } \\ { { = 0 . 6 8 7 , x _ { 2 } = - 2 . 6 6 , x _ { 3 } = 0 . 1 1 7 , x _ { 4 } = 3 . 5 9 } } \end{array}
$$

18. Gaussian elimination with scaled partial pivoting gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 9 . 9 8$   
(b) $x _ { 1 } = 0 . 9 9 3$ , $x _ { 2 } = 0 . 5 0 0$ , $x _ { 3 } = - 1 . 0 0$   
(c) $\begin{array} { l } { { x _ { 1 } = 0 . 0 9 3 0 , x _ { 2 } = - 0 . 0 6 3 1 , x _ { 3 } = - 0 . 0 3 5 9 , x _ { 4 } = 0 . 0 4 6 \tilde { \iota } } } \\ { { \phantom { x _ { 1 } = } } } \\ { { x - 1 = 1 . 3 3 , x _ { 2 } = - 4 . 6 6 , x _ { 3 } = - 4 . 0 4 , x _ { 4 } = - 1 . 6 6 } } \end{array}$   
(d)

19. Gaussian elimination with scaled partial pivoting and three-digit rounding arithmetic gives the following results.

(a) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$ (b) $x _ { 1 } = 0 . 0 0$ , $x _ { 2 } = 1 0 . 0$ , $x _ { 3 } = 0 . 1 4 3$ (c) $x _ { 1 } = 0 . 1 8 0$ , $x _ { 2 } = 0 . 0 1 2 8$ , $x _ { 3 } = - 0 . 0 2 0 0$ , $x _ { 4 } = - 1 . 1 3$ (d) $x _ { 1 } = 0 . 7 8 3$ , $x _ { 2 } = - 3 . 1 2$ , $x _ { 3 } = 0 . 1 4 7$ , $x _ { 4 } = 4 . 5 3$

20. Gaussian elimination with scaled partial pivoting and three-digit chopping arithmetic gives the following results.

(a) $x _ { 1 } = 1 . 0 0$ , $x _ { 2 } = 1 0 . 0$ (b) $x _ { 1 } = 1 . 0 3$ , $x _ { 2 } = 0 . 5 0 2$ , $x _ { 3 } = - 1 . 0 1$ (c) $x _ { 1 } = 0 . 0 9 2 7 , x _ { 2 } = - 0 . 0 6 3 0 , x _ { 3 } = - 0 . 0 3 6 0 , x _ { 4 } = 0 . 0 4 6 7$ (d) $x _ { 1 } = 1 . 3 5 , x _ { 2 } = - 4 . 7 3 , x _ { 3 } = - 4 . 0 7 , x _ { 4 } = - 1 . 6 5$

21. Using Algorithm 6.1 in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 0 . 0 0 0 0 0 0 0 3 3$ , $x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 1 , x _ { 3 } = 0 . 1 4 2 8 5 7 1 4 2 9$   
(c) $c _ { 1 } = 0 . 1 7 6 8 2 5 2 9 5 8 , x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 1 3 , x _ { 3 } = - 0$ $x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 1 3 , x _ { 3 } = - 0 . 0 2 0 6 5 4 0 5 0 3 , x _ { 4 } =$ −1.182608714   
(d) $x _ { 1 } = 0 . 7 8 8 3 9 3 7 8 4 2 , x _ { 2 } = - 3 . 1 2 5 4 1 3 6 7 2 , x _ { 3 } = 0 . 1 6 7 5 9 6 5 9 5 1 , x _ { }$ $x _ { 4 } = 4 . 5 5 7 0 0 2 5 2 1$

22. Using Algorithm 6.1 in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 1 . 0 0 0 0 0 0 3 0 0 , x _ { 2 } = 0 . 5 0 0 0 0 0 0 1 , x _ { 3 } = - 1 . 0 0 0 0 0 0 3 0 6$   
(c) $x _ { 1 } = 0 . 0 9 2 7 6 1 0 4 6 7 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 2 6 , x _ { 3 } = - 0 . 0 3 6 2 4 5 8 2 2 6 7 , x _ { 4 } = 0 . 0 4 6 7 0 9 4 3 3 9 2 6 , x _ { 5 } = - 0 . 0 3 6 3 5 2 2 6 7 9 4 9 4 6 7 0 .$ 801939

(d) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 9 , x _ { 2 } = - 4 . 6 7 7 9 8 7 7 5 5 , x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 9 , x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2 , x _ { 5 } = - 4 . 7 5 6 9 6 7 5 9 7 9 9 .$

23. Using Algorithm 6.2 in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 , x _ { 3 } = 0 . 1 4 2 8 5 7 1 4 2$   
(c) $s _ { 1 } = 0 . 1 7 6 8 2 5 2 9 7 5 , x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 0 9 , x _ { 3 } = - ($ 0.0206540502, x4 = −1.182608696   
(d) $x _ { 1 } = 0 . 7 8 8 3 9 3 7 8 6 3 , x _ { 2 } = - 3 . 1 2 5 4 1 3 6 8 0 , x _ { 3 } = 0 . 1 6 7 5 9 6 5 9 8 0 , x _ { 4 } = 4 . 5 5 7 0 0 2 5 1$

24. Using Algorithm 6.2 in Maple with $D i g i t s { : = } 1 0$ gives

(a) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 1 . 0 0 0 0 0 0 3 0 0 , x _ { 2 } = 0 . 5 0 0 0 0 0 0 1 , x _ { 3 } = - 1 . 0 0 0 0 0 0 3 0 6$   
(c) $x _ { 1 } = 0 . 0 9 2 7 6 1 0 4 7 0 4 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 6 1 , x _ { 3 } = - 0 . 0 3 6 2 4 5 8 2 2 6 4 , x _ { 4 } =$ 0.04670801938   
(d) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 9 , x _ { 2 } = - 4 . 6 7 7 9 8 7 7 5 5 , x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 9 , x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2 6 7 5 9 .$

25. Using Algorithm 6.3 in Maple with $D i g i t s { : = } 1 0$ gives

(a) $x _ { 1 } = 1 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 0 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 , x _ { 3 } = 0 . 1 4 2 8 5 7 1 4 2 9$   
(c) $s _ { 1 } = 0 . 1 7 6 8 2 5 2 9 7 7 , x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 0 9 , x _ { 3 } = - 0$ 0.0206540501, $x _ { 4 } = - 1 . 1 8 2 6 0 8 6 9 3$   
(d) $x _ { 1 } = 0 . 7 8 8 3 9 3 7 8 4 2$ , $x _ { 2 } = - 3 . 1 2 5 4 1 3 6 7 2 , x _ { 3 } = 0 . 1 6 7 5 9 6 5 9 5 2 , x _ { 4 } =$ $x _ { 4 } = 4 . 0 5 5 7 0 0 2 5 2$

26. Using Algorithm 6.3 in Maple with $D i g i t s { : = } 1 0$ gives

(a) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 0 . 5 0 0 0 0 0 0 0 , x _ { 3 } = - 1 . 0 0 0 0 0 0 0 0$   
(c) $x _ { 1 } = 0 . 0 9 2 7 6 1 0 4 7 0 5 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 6 1 , x _ { 3 } = - 0 . 0 3 6 2 4 5 8 2 2 6 4 ,$ $x _ { 4 } = 0 . 0 4 6 7 0 8 0 1 9 3 8$   
(d) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 9 , x _ { 2 } = - 4 . 6 7 7 9 8 7 7 5 5 , x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 9 , x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2 5 6 , x _ { 5 } = - 4 . 7 5 7 7 3 8 7 7 7 9 9 9 .$

27. Using Gaussian elimination with complete pivoting gives:

(a) $x _ { 1 } = 9 . 9 8 , x _ { 2 } = 1 . 0 0$ (b) $x _ { 1 } = 0 . 0 7 2 4 , x _ { 2 } = 1 0 . 0 , x _ { 3 } = 0 . 0 9 5 2$ (c) $\mathfrak { c } _ { 1 } = 0 . 1 6 1 , x _ { 2 } = 0 . 0 1 2 5 , x _ { 3 } = - 0 . 0 2 3 2 , x _ { 4 } = - 1$ .42 (d) $x _ { 1 } = 0 . 7 1 9 , x _ { 2 } = - 2 . 8 6 , x _ { 3 } = 0 . 1 4 6 , x _ { 4 } = 4 . 0 0$

28. Gaussian elimination with complete pivoting gives the following results.

(a) $x _ { 1 } = 1 . 0 0 , x _ { 2 } = 9 . 9 8$ (b) $x _ { 1 } = 0 . 9 8 2 , x _ { 2 } = 0 . 5 0 0 , x _ { 3 } = - 0 . 9 9 4$ (c) $x _ { 1 } = 0 . 0 9 3 3 , x _ { 2 } = - 0 . 0 6 3 1 , x _ { 3 } = - 0 . 0 3 6 0 , 0 . 0 4 6 4$ 4 (d) $x _ { 1 } = 1 . 3 3 , x _ { 2 } = - 4 . 6 6 , x _ { 3 } = - 4 . 0 4 , x _ { 4 } = - 1 . 6 5$

29. Using Gaussian elimination with complete pivoting and three-digit rounding arithmetic gives:

(a) $x _ { 1 } = 1 0 . 0 , x _ { 2 } = 1 . 0 0$

$$
\begin{array} { l } { x _ { 1 } = 0 . 0 0 , x _ { 2 } = 1 0 . 0 , x _ { 3 } = 0 . 1 4 3 } \\ { x _ { 1 } = 0 . 1 7 9 , x _ { 2 } = 0 . 0 1 2 7 , x _ { 3 } = - 0 . 0 2 0 3 , x _ { 4 } = - 1 . 1 5 } \\ { x _ { 1 } = 0 . 8 7 4 , x _ { 2 } = - 3 . 4 9 , x _ { 3 } = 0 . 1 9 2 , x _ { 4 } = 5 . 3 3 } \end{array}
$$

30. Gaussian elimination with complete pivoting and three-digit rounding gives the following results.

(a) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$   
(b) $x _ { 1 } = 1 0 . 0$ , $x _ { 2 } = 1 . 0 0$   
(c) $x _ { 1 } = 0 . 0 9 2 6$ $; x _ { 2 } = - 0 . 0 6 \div 2 9 , x _ { 3 } = - 0 . 0 3 6 1 , x _ { 4 } = 0 . 0 4 6 6$   
(d) $x _ { 1 } = 1 . 3 3$ , $x _ { 2 } = - 4 . 6 8$ , $x _ { 3 } = - 4 . 0 6$ , $x _ { 4 } = - 1 . 6 5$

$^ { * } 3 1$ . The only system which does not require row interchanges is (a), where $\alpha = 6$

$^ { * } 3 2$ . Change Algorithm 6.2 as follows:

Add to STEP 1.

$$
N C O L ( i ) = i
$$

Replace STEP 3 with the following.

Let $p$ and $q$ be the smallest integers with $i \le p$ , $q \leq n$ and

$$
\begin{array} { r } { | a ( N R O W ( p ) , N C O L ( q ) ) | = \operatorname* { m a x } _ { i \leq k , j \leq n } | a ( N R O W ( k ) , N C O L ( j ) ) | . } \end{array}
$$

Add to STEP 4.

$$
A ( N R O W ( p ) , N C O L ( q ) ) = 0
$$

Add to STEP 5.

If $N C O L ( q ) \neq N C O L ( i )$ then set

Replace STEP 7 with the following.

Set

$$
m ( N R O W ( j ) , N C O L ( i ) ) = \frac { a ( N R O W ( j ) , N C O L ( i ) ) } { a ( N R O W ( i ) , N C O L ( i ) ) } .
$$

Replace in STEP 8:

$$
m ( N R O W ( j ) , i ) \mathrm { b y } m ( N R O W ( j ) , N C O L ( i ) )
$$

Replace in STEP 9:

$$
a ( N R O W ( n ) , n ) \mathrm { b y } a ( N R O W ( n ) , N C O L ( n ) )
$$

Replace STEP 10 with the following.

Set

$$
X ( N C O L ( n ) ) = { \frac { a ( N R O W ( n ) , n + 1 ) } { a ( N R O W ( n ) , N C O L ( n ) ) } } .
$$

Replace STEP 11 with the following.

Set

$$
X ( N C O L ( i ) ) = \frac { a ( N R O W ( i ) , n + 1 ) - \sum _ { j = i + 1 } ^ { n } a ( N R O W ( i ) , N C O L ( j ) ) \cdot X ( N C O L ( j ) ) } { A ( N R O W ( i ) , N C O L ( i ) ) } .
$$

Replace STEP 12 with the following.

33. Using the Complete Pivoting Algorithm in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 0 . 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 , x _ { 3 } = 0 . 1 4 2 8 5 7 1 4 2 9$   
(c) $\begin{array} { r } { \mathfrak { c } _ { 1 } = 0 . 1 7 6 8 2 5 2 9 7 4 , x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 0 8 7 , x _ { 3 } = - } \end{array}$ $\begin{array} { r } { x _ { 2 } = 0 . 0 1 2 6 9 2 6 9 0 8 7 , x _ { 3 } = - 0 . 0 2 0 6 5 4 0 5 0 1 5 , } \end{array}$ $x _ { 4 } = - 1 . 1 8 2 6 0 8 6 9 7$   
(d) $x _ { 1 } = 0 . 1 7 8 8 3 9 3 7 8 4 0 , x _ { 2 } = - 3 . 1 2 5 4 1 3 6 6 9 , x _ { 3 } = 0 . 1 6 7 5 9 6 5 9 7 1 , x _ { 4 } = 4 . 5 5 7 0 0 2 5 1 6$

34. Using the Complete Pivoting Algorithm in Maple with Digits:=10 gives

(a) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 0 0 0 , x _ { 2 } = 1 0 . 0 0 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 1 . 0 0 0 0 0 0 0 1 , x _ { 2 } = 0 . 5 0 0 0 0 0 0 0 0 , x _ { 3 } = - 1 . 0 0 0 0 0 0 0 1$   
(c) $\begin{array} { r } { \mathfrak { c } _ { 1 } = 0 . 0 9 2 7 6 1 0 4 7 0 1 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 6 0 , x _ { 3 } = } \end{array}$ $1 , x _ { 2 } = - 0 . 0 6 2 9 9 4 3 3 9 6 0 , x _ { 3 } = - 0 . 0 3 6 2 4 5 8 2 2 6 7 .$ , $x _ { 4 } = 0 . 0 4 6 7 0 8 0 1 9 3 7$   
(d) $x _ { 1 } = 1 . 3 4 9 4 4 8 5 5 7 , x _ { 2 } = - 4 . 6 7 7 9 8 7 7 5 0 , x _ { 3 } = - 4 . 0 3 2 8 9 3 7 7 8 , x _ { 4 } = - 1 . 6 5 6 6 3 7 7 3 2 , x _ { 5 } = - 4 . 0 9 6 9 3 7 8 7 8 7 9 .$

# Exercise Set 6.3, page 390

1. (a) $\left[ - 1 8 \right]$ (b) "00# (c) 


4
3
7

 (d) -−4 8 −16

2. (a) $\begin{array} { r } { \left[ \begin{array} { l } { 3 } \\ { 0 } \end{array} \right] } \end{array}$ (b) "12# $* ( \mathrm { c } ) \quad \left[ \begin{array} { c } { { 9 } } \\ { { - 1 } } \\ { { 1 4 } } \end{array} \right]$ (d) -10 −9 −4

3. (a) $\left[ { \begin{array} { r r } { - 4 } & { 1 0 } \\ { 1 } & { 1 5 } \end{array} } \right]$ (b) " $\begin{array} { r } { \left[ \begin{array} { r r r } { 1 1 } & { 4 } & { - 8 } \\ { 6 } & { 1 3 } & { - 1 2 } \end{array} \right] \quad \mathrm { ( c ) } \quad \left[ \begin{array} { r r r } { - 1 } & { 5 } & { - 3 } \\ { 3 } & { 4 } & { - 1 1 } \\ { - 6 } & { - 7 } & { - 4 } \end{array} \right] \quad \mathrm { ( d ) } \quad \left[ \begin{array} { r r } { - 2 } & { 1 } \\ { - 1 4 } & { 7 } \\ { 6 } & { 1 } \end{array} \right] } \end{array}$

$$
\left[ { \begin{array} { r r } { - 1 9 } & { 1 6 } \\ { - 1 5 } & { 6 } \end{array} } \right] \qquad { \begin{array} { r r } { * ( \mathrm { b } ) } & { \left[ { \begin{array} { r r } { - 1 1 } & { 8 } & { 3 } \\ { - 1 6 } & { 1 2 } & { 2 } \end{array} } \right] } \end{array} } \qquad ( \mathrm { c } ) \left[ { \begin{array} { r r } { 5 } & { - 1 6 } & { 1 5 } \\ { - 1 4 } & { 2 4 } & { - 1 8 } \\ { - 2 3 } & { 1 4 } & { - 1 } \end{array} } \right] ( \mathrm { d } )  &  \left[ { \begin{array} { r r } { - 7 } & { 7 } \\ { - 1 } & { - 9 } \\ { 1 8 } & { - 2 5 } \end{array} } \right]
$$

5. Determine if the matrices are nonsingular, and if so, find the inverse.

(a) The matrix is singular.

$$
* ( \mathrm { b } ) \quad \left[ \begin{array} { r r r } { { - \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } \\ { { \frac { 5 } { 8 } } } & { { - \frac { 1 } { 8 } } } & { { - \frac { 1 } { 8 } } } \\ { { \frac { 1 } { 8 } } } & { { - \frac { 5 } { 8 } } } & { { \frac { 3 } { 8 } } } \end{array} \right]
$$

(c) The matrix is singular.

$$
\left[ { \begin{array} { r r r r } { { \frac { 1 } { 4 } } } & { 0 } & { 0 } & { 0 } \\ { - { \frac { 3 } { 1 4 } } } & { { \frac { 1 } { 7 } } } & { 0 } & { 0 } \\ { { \frac { 3 } { 2 8 } } } & { - { \frac { 1 1 } { 7 } } } & { 1 } & { 0 } \\ { - { \frac { 1 } { 2 } } } & { 1 } & { - 1 } & { 1 } \end{array} } \right]
$$

6. Determine if the matrices are nonsingular, and if so, find the inverse.

(a)

$$
{ \left[ \begin{array} { l l l } { 1 } & { 2 } & { - 1 } \\ { 0 } & { 1 } & { 2 } \\ { - 1 } & { 4 } & { 3 } \end{array} \right] } ^ { - 1 } = { \left[ \begin{array} { l l l } { { \frac { 1 } { 2 } } } & { 1 } & { - { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 5 } } } & { - { \frac { 1 } { 5 } } } & { { \frac { 1 } { 5 } } } \\ { - { \frac { 1 } { 1 0 } } } & { { \frac { 3 } { 5 } } } & { - { \frac { 1 } { 1 0 } } } \end{array} \right] }
$$

$$
{ \left[ \begin{array} { l l l } { 1 } & { 2 } & { 0 } \\ { 2 } & { 1 } & { - 1 } \\ { 3 } & { 1 } & { 1 } \end{array} \right] } ^ { - 1 } = { \left[ \begin{array} { l l l } { - { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 4 } } } \\ { { \frac { 5 } { 8 } } } & { - { \frac { 1 } { 8 } } } & { - { \frac { 1 } { 8 } } } \\ { { \frac { 1 } { 8 } } } & { - { \frac { 5 } { 8 } } } & { { \frac { 3 } { 8 } } } \end{array} \right] }
$$

(c) The matrix is singular.

$$
\left[ { \begin{array} { c c c c } { 2 } & { 0 } & { 0 } & { 2 } \\ { 1 } & { 1 } & { 0 } & { 2 } \\ { 2 } & { - 1 } & { 3 } & { 1 } \\ { 3 } & { - 1 } & { 4 } & { 3 } \end{array} } \right] ^ { - 1 } = \left[ { \begin{array} { c c c c } { 1 } & { 0 } & { 1 } & { - 1 } \\ { - 1 } & { { \frac { 5 } { 3 } } } & { { \frac { 5 } { 3 } } } & { - 1 } \\ { - 1 } & { { \frac { 2 } { 3 } } } & { { \frac { 2 } { 3 } } } & { 0 } \\ { 0 } & { - { \frac { 1 } { 3 } } } & { - { \frac { 4 } { 3 } } } & { 1 } \end{array} } \right]
$$

7. The solutions to the linear systems obtained in parts (a) and (b) are, from left to right,

$$
3 , - 6 , - 2 , - 1 \quad { \mathrm { a n d } } \quad 1 , 1 , 1 , 1 .
$$

8. The solutions to the linear systems obtained in parts (a) and (b) are, from left to right and top to bottom:

$$
- \frac { 2 } { 7 } , - \frac { 1 3 } { 1 4 } , - \frac { 3 } { 1 4 } ; \quad \frac { 1 7 } { 7 } , - \frac { 1 9 } { 1 4 } , - \frac { 4 1 } { 1 4 } ; \quad 1 , 1 , 1 \quad \mathrm { a n d } \quad \left. - \frac { 1 } { 7 } , \frac { 2 } { 7 } , \frac { 1 } { 7 } . \right.
$$

9. (a) Suppose $\ddot { A }$ and $\hat { A }$ are both inverses of $A$ . Then $A { \tilde { A } } = { \tilde { A } } A = I$ and $A { \hat { A } } = { \hat { A } } A = I$ . Thus,

$$
\tilde { A } = \tilde { A } I = \tilde { A } ( A \hat { A } ) = ( \tilde { A } A ) \hat { A } = I \hat { A } = \hat { A } .
$$

(b) We have

$$
( A B ) ( B ^ { - 1 } A ^ { - 1 } ) = A ( B B ^ { - 1 } ) A ^ { - 1 } = A I A ^ { - 1 } = A A ^ { - 1 } = I
$$

and

$$
( B ^ { - 1 } A ^ { - 1 } ) ( A B ) = B ^ { - 1 } ( A ^ { - 1 } A ) B = B ^ { - 1 } I B = B ^ { - 1 } B = I .
$$

So $( A B ) ^ { - 1 } = B ^ { - 1 } A ^ { - 1 }$ since the inverse is unique.

(c) Since $A ^ { - 1 } A = A A ^ { - 1 } = I$ , it follows that $A ^ { - 1 }$ is nonsingular. Since the inverse is unique, we have $( A ^ { - 1 } ) ^ { - 1 } = A$ .

10. (a) Not true. Let

$$
A = { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 0 } \end{array} \right] } \quad { \mathrm { a n d } } \quad B = { \left[ \begin{array} { l l } { 1 } & { - 1 } \\ { - 1 } & { 2 } \end{array} \right] } . \quad { \mathrm { T h e n } } \quad A B = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 1 } & { - 1 } \end{array} \right] }
$$

is not symmetric.

(b) True. Let $A$ be a nonsingular symmetric matrix. By Theorem 6.13 (d), $\left( A ^ { - 1 } \right) ^ { t } = \left( A ^ { t } \right) ^ { - 1 }$ . Thus, $\left( A ^ { - 1 } \right) ^ { t } = \left( A ^ { t } \right) ^ { - 1 } = A ^ { - 1 }$ and $A ^ { - 1 }$ is symmetric.

(c) Not true. Use the matrices $A$ and $B$ from part (a).

11. (a) If $C = A B$ , where $A$ and $B$ are lower triangular, then $a _ { i k } = 0$ if $k > i$ and $b _ { k j } = 0$ if $k < j$ . Thus

$$
c _ { i j } = \sum _ { k = 1 } ^ { n } a _ { i k } b _ { k j } = \sum _ { k = j } ^ { i } a _ { i k } b _ { k j } ,
$$

which will have the sum zero unless $j \le i$ . Hence $C$ is lower triangular.

(b) We have $a _ { i k } = 0$ if $k < i$ and $b _ { k j } = 0$ if $k > j$ . The steps are similar to those in part (a). (c) Let $L$ be a nonsingular lower triangular matrix. To obtain the $i$ th column of $L ^ { - 1 }$ , solve $n$ linear systems of the form

$$
\begin{array} { r l } & { \begin{array} { c c c c c c c c } { l _ { 1 1 } } & { 0 } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { 0 } \\ { l _ { 2 1 } } & { l _ { 2 2 } } & & & & & { \vdots } \\ { \vdots } & { \vdots } & & & & & { \vdots } \\ { \vdots } & { \vdots } & { \ddots } & & & & & { \vdots } \\ { l _ { i 1 } } & { l _ { i 2 } } & { \cdots } & & & & & { \vdots } \\ { l _ { i 1 } } & { l _ { i 2 } } & { \cdots } & { l _ { i i } } & & & & { \vdots } \\ { \vdots } & { \vdots } & & & & & { \vdots } \\ { \vdots } & { \vdots } & & & & & { \ddots } & & \\ { l _ { n 1 } } & { l _ { n 2 } } & { \cdots } & { \cdots } & { \cdots } & { l _ { n n } } \end{array} \} \begin{array} { c } { [ x _ { 1 } ] } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \end{array} \} = [ \begin{array} { c } { [ 0 ] } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { 1 } \\ { 0 } \end{array} ] , } \\ &  \begin{array} { c } { \vdots } \\ { \vdots } \\ { \vdots } \\ { l _ { n 1 } } \end{array} \begin{array} { c } { [ \begin{array} { c } { \begin{array} { c } { \begin{array} { c } { r } \end{array} } \end{array} ] } \\ { \vdots } \\ { \vdots } \\ { 0 } \end{array} ] } \\  [ \begin{array} { c } { \begin{array} { c } { \begin{array} { c } { \begin{array} { c } { r } \end{array} } \end{array} } \\ { \vdots } \\ { \vdots } \\ { \ddots } \\ { 0 } \end{array} ] } \end{array} \end{array} \end{array}
$$

where the 1 appears in the $i$ th position to obtain the $i$ th column of $L ^ { - 1 }$ .

$^ *$ 12. (a) Following the steps of Algorithm 6.1 with $m - 1$ additional columns in the augmented matrix gives the following:

Reduction Steps 1–6: Multiplications/Divisions:

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ 1 + ( m + n - i ) \right\} = \displaystyle \sum _ { i = 1 } ^ { n - 1 } \left\{ n ( m + n + 1 ) - ( m + 2 n + 1 ) i + i ^ { 2 } \right\} } } \\ { { = \displaystyle \frac { 1 } { 2 } m n ^ { 2 } - \frac { 1 } { 2 } m n + \frac { 1 } { 3 } n ^ { 3 } - \frac { 1 } { 3 } n } } \end{array}
$$

Additions/Subtractions:

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ m + n - i \right\} = \sum _ { i = 1 } ^ { n - 1 } \left\{ n ( m + n ) - ( m + 2 n ) i + i ^ { 2 } \right\} } } \\ { { = \displaystyle \frac { 1 } { 2 } m n ^ { 2 } - \frac { 1 } { 2 } m n + \frac { 1 } { 3 } n ^ { 3 } - \frac { 1 } { 2 } n ^ { 2 } + \frac { 1 } { 6 } n } } \end{array}
$$

Backward Substitution Steps 8–9:

Multiplications/Divisions:

$$
m \left[ 1 + \sum _ { i = 1 } ^ { n - 1 } ( n - i + 1 ) \right] = m \left[ 1 + \frac { n ( n + 1 ) } { 2 } - 1 \right] = \frac 1 2 m n ^ { 2 } + \frac 1 2 m n
$$

Additions/Subtractions:

$$
m \left[ \sum _ { i = 1 } ^ { n - 1 } ( n - i ) \right] = \frac { 1 } { 2 } m n ^ { 2 } - \frac { 1 } { 2 } m n
$$

Total:

Multiplications/Divisions: ${ \begin{array} { l } { { \frac { 1 } { 3 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 3 } } n } \end{array} }$ Additions/Subtractions: $\textstyle { \frac { 1 } { 3 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 2 } } n ^ { 2 } - m n + { \frac { 1 } { 6 } } n$

(b) For the reduction phase: Multiplications/Divisions:

$$
\begin{array} { c } { { \displaystyle { \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \left\{ 1 + \sum _ { k = i + 1 } ^ { n + m } 1 \right\} = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 ; j \neq i } ^ { n } ( m + n + 1 - i ) = \sum _ { i = 1 } ^ { n } \{ ( n - 1 ) ( m + n + 1 ) - ( n - 1 ) i \} } } } \\ { { = \displaystyle { \frac { 1 } { 2 } { n } ^ { 3 } + m n ^ { 2 } - m n - \frac { 1 } { 2 } n } } } \end{array}
$$

Additions/Subtractions:

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 ; j \neq i } ^ { n } \sum _ { k = i + 1 } ^ { n + m } 1 = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 ; j \neq i } ^ { n } ( n + m - i ) = \sum _ { i = 1 } ^ { n } \{ ( n - 1 ) ( m + n ) - ( n - 1 ) i \} } } \\ { { \displaystyle \qquad = \frac { 1 } { 2 } n ^ { 3 } + m n ^ { 2 } - m n - n ^ { 2 } + \frac { 1 } { 2 } n } } \end{array}
$$

Backward Substitution Steps:

Multiplications/Divisions:

$$
\sum _ { k = 1 } ^ { m } \sum _ { i = 1 } ^ { n } 1 = m n
$$

Additions/Subtractions: none

Totals:

Multiplications/Divisions: ${ \begin{array} { l } { { \frac { 1 } { 2 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 2 } } n } \end{array} }$ Additions/Subtractions: $\textstyle { \frac { 1 } { 2 } } n ^ { 3 } + m n ^ { 2 } - n ^ { 2 } - m n + { \frac { 1 } { 2 } } n$

(c) When $m = n$ we have the following:

Gaussian Elimination

Multiplications/Divisions: $\textstyle { \frac { 1 } { 3 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 3 } } n = { \frac { 4 } { 3 } } n ^ { 3 } - { \frac { 1 } { 3 } } n$ Additions/Subtractions: ${ \textstyle { \frac { 1 } { 3 } } } n ^ { 3 } + m n ^ { 2 } - { \textstyle { \frac { 1 } { 2 } } } n ^ { 2 } - m n + { \textstyle { \frac { 1 } { 6 } } } n = { \textstyle { \frac { 4 } { 3 } } } n ^ { 3 } - { \textstyle { \frac { 3 } { 2 } } } n ^ { 2 } + { \textstyle { \frac { 1 } { 6 } } } n$

Gauss-Jordan Elimination

Multiplications/Divisions: ${ \begin{array} { l } { { \frac { 1 } { 2 } } n ^ { 3 } + m n ^ { 2 } - { \frac { 1 } { 2 } } n = { \frac { 3 } { 2 } } n ^ { 3 } - { \frac { 1 } { 2 } } n } \end{array} }$ Additions/Subtractions: ${ \begin{array} { l } { { \frac { 1 } { 2 } } n ^ { 3 } + m n ^ { 2 } - n ^ { 2 } - m n + { \frac { 1 } { 2 } } n = { \frac { 3 } { 2 } } n ^ { 3 } - 2 n ^ { 2 } + { \frac { 1 } { 2 } } n } \end{array} }$

(d) To find the inverse of the $n \times n$ matrix $A$

INPUT $n \times n$ matrix $A = \left( a _ { i j } \right)$ .

OUTPUT $n \times n$ matrix $B = A ^ { - 1 }$

Step 1 Initialize the $n \times n$ matrix $B = ( b _ { i j } )$ to

$$
b _ { i j } = { \left\{ \begin{array} { l l } { 0 } & { i \neq j , } \\ { 1 } & { i = j } \end{array} \right. }
$$

Step 2 For $i = 1 , \ldots , n - 1$ do Steps 3, 4, and 5.

Step 3 Let $p$ be the smallest integer with $i \le p \le n$ and $a _ { p , i } \neq 0$ . If no integer $p$ can be found then OUTPUT ( $A$ is singular’); STOP.

Step 4 If $p \neq i$ then perform $( E _ { p } )  ( E _ { i } )$

Step 5 For $j = i + 1 , \ldots , n$ do Steps 6 through 9.

Step 6 Set $m _ { j i } = a _ { j i } / a _ { i i }$ .   
Step 7 For $k = i + 1 , \ldots , n$ set $a _ { j k } = a _ { j k } - m _ { j i } a _ { i k }$ ; $a _ { i j } = 0$   
Step 8 For $k = 1 , \ldots , i - 1$ set $b _ { j k } = b _ { j k } - m _ { j i } b _ { i k }$ .   
Step 9 Set $b _ { j i } = - m _ { j i }$ .

Step 10 If $a _ { n n } = 0$ then OUTPUT ( $A$ is singular’);

STOP.

Step 11 For $j = 1 , \dotsc , n$ do Steps 12, 13 and 14.

Step 12 Set $b _ { n j } = b _ { n j } / a _ { n n }$ . Step 13 For set $i = n - 1 , \dotsc , j$ $\begin{array} { r } { b _ { i j } = \left( b _ { i j } - \sum _ { k = i + 1 } ^ { n } a _ { i k } b _ { k j } \right) / a _ { i i } } \end{array}$ Step 14 set $\begin{array} { r } { b _ { i j } = - \left\lfloor \sum _ { k = i + 1 } ^ { n } a _ { i k } b _ { k j } \right\rfloor / a _ { i i } } \end{array}$ $i = j - 1 , \ldots , 1$ .

Step 15 OUTPUT ( $B$ ); STOP.

Reduction Steps 2–9:

Multiplications/Divisions:

$$
\sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ 1 + \sum _ { k = i + 1 } ^ { n } 1 + \sum _ { k = 1 } ^ { i - 1 } 1 \right\} = \sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ 1 + n - i + i - 1 \right\} = { \frac { n ^ { 2 } ( n - 1 ) } { 2 } }
$$

Additions/Subtractions:

$$
\sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \left\{ \sum _ { k = i + 1 } ^ { n } 1 + \sum _ { k = 1 } ^ { i - 1 } 1 \right\} = \sum _ { i = 1 } ^ { n - 1 } \sum _ { j = i + 1 } ^ { n } \{ n - i + i - 1 \} = { \frac { n ( n - 1 ) ^ { 2 } } { 2 } }
$$

Backward Substitution Steps 11–14:

Multiplications/Divisions:

$$
\begin{array} { c } { { \displaystyle \sum _ { i = 1 } ^ { n } \left\{ 1 + \sum _ { i = j } ^ { n - 1 } \left\{ 1 + \sum _ { k = i + 1 } ^ { n } 1 \right\} + \sum _ { i = 1 } ^ { j - 1 } \left\{ 1 + \sum _ { k = i + 1 } ^ { n } 1 \right\} \right\} = \sum _ { j = 1 } ^ { n } \left\{ 1 + \sum _ { i = j } ^ { n - 1 } ( n + 1 - i ) + \sum _ { i = 1 } ^ { j - 1 } ( n + 1 - i ) \right\} = \displaystyle \sum _ { i = 1 } ^ { j - 1 } ( n + 1 - i ) ^ { i } = \sum _ { j = 1 } ^ { n } ( n - 1 - i ) ^ { j } } } \\ { { = \displaystyle \sum _ { j = 1 } ^ { n } \left[ 1 + \sum _ { i = 1 } ^ { n - 1 } ( n + 1 - i ) \right] } } \\ { { = \displaystyle \sum _ { j = 1 } ^ { n } \frac { n ( n + 1 ) } { 2 } = \frac { n ^ { 2 } ( n + 1 ) } { 2 } = \frac { n ^ { 2 } ( n + 1 ) } { 2 } = \frac { ( n + 1 ) } { 2 } } } \end{array}
$$

Additions/Subtractions:

$$
\begin{array} { c } { { \displaystyle \sum _ { j = 1 } ^ { n } \left\{ \sum _ { i = j } ^ { n - 1 } ( 1 + n - i - 1 ) + \sum _ { i = 1 } ^ { j - 1 } ( n - i - 1 ) \right\} = \sum _ { j = 1 } ^ { n } \sum _ { i = 1 } ^ { n - 1 } ( n - i ) - j + 1 } } \\ { { = \displaystyle \sum _ { j = 1 } ^ { n } \left[ \frac { n ( n - 1 ) } { 2 } + 1 - j \right] } } \\ { { = \displaystyle \frac { n ^ { 2 } ( n - 1 ) } { 2 } + n - \frac { n ( n + 1 ) } { 2 } } } \\ { { = \displaystyle \frac { n ^ { 3 } } { 2 } - n ^ { 2 } + \frac { 1 } { 2 } n } } \end{array}
$$

Totals:

Multiplications/Divisions: ${ \frac { n ^ { 2 } ( n - 1 ) } { 2 } } + { \frac { n ^ { 2 } ( n + 1 ) } { 2 } } = n ^ { 3 }$ Additions/Subtractions: ${ \frac { n ( n - 1 ) ^ { 2 } } { 2 } } + { \frac { n ^ { 3 } } { 2 } } - n ^ { 2 } + { \frac { 1 } { 2 } } n = n ^ { 3 } - 2 n ^ { 2 } + n$

(e) Let $\left\lfloor A ^ { - 1 } \right\rfloor _ { i , j }$ denote the entries of $A ^ { - 1 }$ , for $1 \leq i , j \leq n$ . For each $i = 1 , \ldots , n$ , we have

$$
x _ { i } = \sum _ { j = 1 } ^ { n } [ A ^ { - 1 } ] _ { i , j } b _ { j } .
$$

This requires $_ { n }$ multiplications and $n - 1$ additions for each $i$ . The total number of computations is:

$n ^ { 2 }$ Multiplications/Divisions and ${ n ^ { 2 } } - n$ Additions/Subtractions.

(f) For $m$ linear systems, we have $m n ^ { 2 }$ Multiplications/Divisions and $m ( n ^ { 2 } \mathrm { ~ - ~ } n )$ Additions/Subtractions.

(g)

<table><tr><td colspan="3">Gaussian Elimination (part a)</td><td colspan="2">Inverting A and forming A-1b</td></tr><tr><td>n</td><td>Multiplications Divisions</td><td>Additions Subtractions</td><td>Multiplications Divisions</td><td>Additions Subtractions</td></tr><tr><td>3</td><td>9m+8</td><td>6m+5</td><td>9m+27</td><td>6m+12</td></tr><tr><td>10</td><td>100m + 330</td><td>90m+285</td><td>100m +1000</td><td>90m+810</td></tr><tr><td>50</td><td>2500m +41650</td><td>2450m + 40425</td><td>2500m +125000</td><td>2450m +120050</td></tr><tr><td>100</td><td>10000m +333300</td><td>9900m + 328350</td><td>10000m+1000000</td><td>9900m + 980100</td></tr></table>

13. The answers are the same as those in Exercise 1.

\*14. No, since the products $A _ { i j } B _ { j k }$ , for $1 \leq i$ , $j$ , $k \leq 2$ , cannot be formed.

(c) The following are necessary and sufficient conditions:

(i) The number of columns of $A$ is the same as the number of rows of $B$ . (ii) The number of vertical lines of $A$ equals the number of horizontal lines of $B$ . (iii) The placement of the vertical lines of $A$ is identical to placement of the horizontal lines of $B$ .

$$
A ^ { 2 } = { \left[ \begin{array} { l l l } { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 3 } \\ { { \frac { 1 } { 6 } } } & { 0 } & { 0 } \end{array} \right] } , \quad A ^ { 3 } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } , \quad A ^ { 4 } = A , \quad A ^ { 5 } = A ^ { 2 } , \quad A ^ { 6 } = I , \ldots A
$$

(b)

<table><tr><td></td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td></tr><tr><td>Age 1</td><td>6000</td><td>36000</td><td>12000</td><td>6000</td></tr><tr><td>Age 2</td><td>6000</td><td>3000</td><td>18000</td><td>6000</td></tr><tr><td>Age 3</td><td>6000</td><td>2000</td><td>1000</td><td>6000</td></tr></table>

(c) We have

$$
A ^ { - 1 } = { \left[ \begin{array} { l l l } { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 3 } \\ { { \frac { 1 } { 6 } } } & { 0 } & { 0 } \end{array} \right] } ~ .
$$

The $i , j$ -entry is the number of beetles of age $i$ necessary to produce one beetle of age $j$ .

16. (a) For each $k = 1 , 2 , \ldots , m$ , the number $a _ { i k }$ represents the total number of plants of type $v _ { i }$ eaten by herbivores in the species $h _ { k }$ . The number of herbivores of types $h _ { k }$ eaten by species $c _ { j }$ is $b _ { k j }$ . Thus, the total number of plants of type $v _ { i }$ ending up in species $c _ { j }$ is $a _ { i 1 } b _ { 1 j } + a _ { i 2 } b _ { 2 j } + . . . + a _ { i m } b _ { m j } = ( A B ) _ { i j }$ .

(b) We first assume $n = m = k$ so that the matrices will have inverses. Let $x _ { 1 } , . . . , x _ { n }$ represent the vegetations of type $v _ { 1 } , . . . , v _ { n }$ , l ${ \mathfrak { x } } y _ { 1 } , . . . , y _ { n }$ represent the number of herbivores of species $h _ { 1 } , . . . , h _ { n }$ , and let $z _ { 1 } , . . . , z _ { n }$ represent the number of carnivores of species $c _ { 1 } , . . . , c _ { n }$ . If

$$
{ \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} \right] } = A { \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } , \quad { \mathrm { t h e n } } \quad \quad { \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } = A ^ { - 1 } \left[ { \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { n } } \end{array} } \right] .
$$

Thus, $( A ^ { - 1 } ) _ { i , j }$ represents the amount of type $v _ { j }$ plants eaten by a herbivore of species $h _ { i }$ .

Similarly, if

$$
{ \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } = B { \left[ \begin{array} { l } { z _ { 1 } } \\ { z _ { 2 } } \\ { \vdots } \\ { z _ { n } } \end{array} \right] } , \quad { \mathrm { t h e n } } \quad { \left[ \begin{array} { l } { z _ { 1 } } \\ { z _ { 2 } } \\ { \vdots } \\ { z _ { n } } \end{array} \right] } = B ^ { - 1 } { \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { \vdots } \\ { y _ { n } } \end{array} \right] } .
$$

Thus, $\left( B ^ { - 1 } \right) _ { i , j }$ represents the number of herbivores of species $h _ { j }$ eaten by a carnivore of species $c _ { i }$ . If $x = A y$ and $y = B z$ , then $x = A B z$ and $z = ( A B ) ^ { - 1 } x$ . But, $y = A ^ { - 1 } x$ and $z = B ^ { - 1 } y$ , so $z = B ^ { - 1 } A ^ { - 1 } x$ .

17. (a) We have

$$
\left[ { \begin{array} { r r r r } { 7 } & { 4 } & { 4 } & { 0 } \\ { - 6 } & { - 3 } & { - 6 } & { 0 } \\ { 0 } & { 0 } & { 3 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } \right] \left[ { \begin{array} { r r r r } { 2 ( x _ { 0 } - x _ { 1 } ) + \alpha _ { 0 } + \alpha _ { 1 } } \\ { 3 ( x _ { 1 } - x _ { 0 } ) - \alpha _ { 1 } - 2 \alpha _ { 0 } } \\ { \alpha _ { 0 } } \\ { x _ { 0 } } \end{array} } \right] = \left[ { \begin{array} { r r r r } { 2 ( x _ { 0 } - x _ { 1 } ) + 3 \alpha _ { 0 } + 3 \alpha _ { 1 } } \\ { 3 ( x _ { 1 } - x _ { 0 } ) - 3 \alpha _ { 1 } - 6 \alpha _ { 0 } } \\ { 3 \alpha _ { 0 } } \\ { x _ { 0 } } \end{array} } \right]
$$

$$
B = A ^ { - 1 } = { \left[ \begin{array} { l l l l } { - 1 } & { - { \frac { 4 } { 3 } } } & { - { \frac { 4 } { 3 } } } & { 0 } \\ { 2 } & { { \frac { 7 } { 3 } } } & { 2 } & { 0 } \\ { 0 } & { 0 } & { { \frac { 1 } { 3 } } } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

$^ *$ 18. (a) In component form:

$$
\begin{array} { r } { ( a _ { 1 1 } x _ { 1 } - b _ { 1 1 } y _ { 1 } + a _ { 1 2 } x _ { 2 } - b _ { 1 2 } y _ { 2 } ) + ( b _ { 1 1 } x _ { 1 } + a _ { 1 1 } y _ { 1 } + b _ { 1 2 } x _ { 2 } + a _ { 1 2 } y _ { 2 } ) i = c _ { 1 } + i d _ { 1 } , } \\ { ( a _ { 2 1 } x _ { 1 } - b _ { 2 1 } y _ { 1 } + a _ { 2 2 } x _ { 2 } - b _ { 2 2 } y _ { 2 } ) + ( b _ { 2 1 } x _ { 1 } + a _ { 2 1 } y _ { 1 } + b _ { 2 2 } x _ { 2 } + a _ { 2 2 } y _ { 2 } ) i = c _ { 2 } + i d _ { 2 } , } \end{array}
$$

which yields

$$
\begin{array} { r l } & { a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } - b _ { 1 1 } y _ { 1 } - b _ { 1 2 } y _ { 2 } = c _ { 1 } , } \\ & { b _ { 1 1 } x _ { 1 } + b _ { 1 2 } x _ { 2 } + a _ { 1 1 } y _ { 1 } + a _ { 1 2 } y _ { 2 } = d _ { 1 } , } \\ & { a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } - b _ { 2 1 } y _ { 1 } - b _ { 2 2 } y _ { 2 } = c _ { 2 } , } \\ & { b _ { 2 1 } x _ { 1 } + b _ { 2 2 } x _ { 2 } + a _ { 2 1 } y _ { 1 } + a _ { 2 2 } y _ { 2 } = d _ { 2 } . } \end{array}
$$

(b) The system

$$
{ \left[ \begin{array} { l l l l } { 1 } & { 3 } & { 2 } & { - 2 } \\ { - 2 } & { 2 } & { 1 } & { 3 } \\ { 2 } & { 4 } & { - 1 } & { - 3 } \\ { 1 } & { 3 } & { 2 } & { 4 } \\ & & & \end{array} \right] } \quad { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \end{array} \right] } = { \left[ \begin{array} { l } { 5 } \\ { 2 } \\ { 4 } \\ { - 1 } \\ { } \end{array} \right] }
$$

has the solution $x _ { 1 } = - 1 . 2$ , $x _ { 2 } = 1$ , $y _ { 1 } = 0 . 6$ , and $y _ { 2 } = - 1$ .

# Exercise Set 6.4, page 399

1. The determinants of the matrices are:

\*(a) $^ { - 8 }$ (b) 14 (c) 0 (d) 3

2. The determinants of the matrices are:

(a) 8 $\mathrm { ( b ) } \ - 8$ (c) 0 (d) 0

3. The answers are the same as in Exercise 1.

4. The answers are the same as in Exercise 2.

$^ { * } 5$ . The matrix is singular when $\alpha = - \frac { 3 } { 2 }$ and when $\alpha = 2$

6. The matrix is singular when $\alpha = 6$ .

$^ { * } 7$ . The system has no solutions when $\alpha = - 5$

8. The system has no solutions when $\alpha = - 5$ .

$^ { * } 9$ . When $n = 2$ , $\operatorname* { d e t } A = a _ { 1 1 } a _ { 2 2 } - a _ { 1 2 } a _ { 2 1 }$ requires 2 multiplications and 1 subtraction. Since

$$
2 ! \sum _ { k = 1 } ^ { 1 } { \frac { 1 } { k ! } } = 2 \quad { \mathrm { ~ a n d ~ } } 2 ! - 1 = 1 ,
$$

the formula holds for $n = 2$ . Assume the formula is true for $n = 2 , . . . , m$ , and let $A$ be an $( m + 1 ) \times ( m + 1 )$ matrix. Then

$$
\operatorname * { d e t } A = \sum _ { j = 1 } ^ { m + 1 } a _ { i j } A _ { i j } ,
$$

for any $i$ , where $1 \leq i \leq m + 1$ . To compute each $A _ { i j }$ requires

$$
m ! \sum _ { k = 1 } ^ { m - 1 } \frac { 1 } { k ! } \mathrm { m u l t i p l i c a t i o n s } \mathrm { a n d } m ! - 1 \mathrm { a d d i t i o n s / s u b t r a c t i o n s } .
$$

Thus, the number of multiplications for $\operatorname { d e t } A$ is

$$
( m + 1 ) \left[ m ! \sum _ { k = 1 } ^ { m - 1 } { \frac { 1 } { k ! } } \right] + ( m + 1 ) = ( m + 1 ) ! \left[ \sum _ { k = 1 } ^ { m - 1 } { \frac { 1 } { k ! } } + { \frac { 1 } { m ! } } \right] = ( m + 1 ) ! \sum _ { k = 1 } ^ { m } { \frac { 1 } { k ! } } ,
$$

and the number of additions/subtractions is

$$
( m + 1 ) \left[ m ! - 1 \right] + m = ( m + 1 ) ! - 1 .
$$

By the principle of mathematical induction, the formula is valid for any $n \geq 2$ .

10. Let

$$
A = \left[ \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] \quad \mathrm { a n d } \quad \tilde { A } = \left[ \begin{array} { l l l } { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right] .
$$

Expanding along the third rows gives

$$
{ \begin{array} { r l } { \operatorname* { d e t } A = a _ { 3 1 } \operatorname* { d e t } { \left[ \begin{array} { l l } { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 2 } } & { a _ { 2 3 } } \end{array} \right] } - a _ { 3 2 } \operatorname* { d e t } { \left[ \begin{array} { l l } { a _ { 1 1 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 3 } } \end{array} \right] } + a _ { 3 3 } \operatorname* { d e t } { \left[ \begin{array} { l l } { a _ { 1 1 } } & { a _ { 1 2 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } \end{array} \right] } } \\ { = a _ { 3 1 } { \left( a _ { 1 2 } a _ { 2 3 } - a _ { 1 3 } a _ { 2 2 } \right) } - a _ { 3 2 } { \left( a _ { 1 1 } a _ { 2 3 } - a _ { 1 3 } a _ { 2 1 } \right) } + a _ { 3 3 } { \left( a _ { 1 1 } a _ { 2 2 } - a _ { 1 2 } a _ { 2 1 } \right) } } \end{array} }
$$

and

$$
\begin{array} { r l } & { \operatorname* { d e t } \tilde { A } = a _ { 3 1 } \operatorname* { d e t } \left[ \frac { a _ { 2 2 } } { a _ { 1 2 } } \quad a _ { 2 3 } \right] - a _ { 3 2 } \operatorname* { d e t } \left[ \frac { a _ { 2 1 } } { a _ { 1 1 } } \quad a _ { 2 3 } \right] + a _ { 3 3 } \operatorname* { d e t } \left[ \begin{array} { l l } { a _ { 2 1 } } & { a _ { 2 2 } } \\ { a _ { 1 1 } } & { a _ { 1 2 } } \end{array} \right] } \\ & { \qquad = a _ { 3 1 } ( a _ { 1 3 } a _ { 2 2 } - a _ { 1 2 } a _ { 2 3 } ) - a _ { 3 2 } ( a _ { 1 3 } a _ { 2 1 } - a _ { 1 1 } a _ { 2 3 } ) + a _ { 3 3 } ( a _ { 1 2 } a _ { 2 1 } - a _ { 1 1 } a _ { 2 2 } ) = - \operatorname* { d e t } A . } \end{array}
$$

The other two cases are similar.

$^ *$ 11. The result follows from $\operatorname* { d e t } A B = \operatorname* { d e t } A \cdot \operatorname* { d e t } B$ and Theorem 6.17.

12. (a) The solution is $x _ { 1 } = 0$ , $x _ { 2 } = 1 0$ , and $x _ { 3 } = 2 6$ . (b) We have $D _ { 1 } = - 1$ , $D _ { 2 } = 3$ , $D _ { 3 } = 7$ , and $D = 0$ , and there are no solutions. (c) We have $D _ { 1 } = D _ { 2 } = D _ { 3 } = D = 0$ , and there are infinitely many solutions. (d) Cramer’s rule requires 39 Multiplications/Divisions and 20 Additions/Subtractions.

$^ *$ 13. (a) If $D _ { i }$ is the determinant of the matrix formed by replacing the $i$ th column of $A$ with b and if $D = \det A$ , then

$$
x _ { i } = D _ { i } / D , \mathrm { ~ f o r ~ } i = 1 , \ldots , n .
$$

(b) $( n + 1 ) ! \left( \sum _ { k = 1 } ^ { n - 1 } { \frac { 1 } { k ! } } \right) + n$ multiplications/divisions; $( n + 1 ) ! - n - 1$ additions/subtractions.

# Exercise Set 6.5, page 409

1. The solutions to the linear systems are as follows.

\*(a) $x _ { 1 } = - 3$ , $x _ { 2 } = 3$ , $x _ { 3 } = 1$ (b) $\begin{array} { r } { x _ { 1 } = \frac { 1 } { 2 } } \end{array}$ , $x _ { 2 } = - \frac { \mathsf { y } } { 2 }$ , $\begin{array} { r } { x _ { 3 } = \frac { 7 } { 2 } } \end{array}$

2. The solutions to the linear systems are as follows.

(a) $x _ { 1 } = 1 1 / 2 0$ , $x _ { 2 } = 3 / 1 0$ , x3 = 2 / 5 (b) $x _ { 1 } = 1 7 6$ , $x _ { 2 } = - 5 0$ , $x _ { 3 } = 2 4$

3. (a) $P = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] }$ \* $( \mathrm { b } ) ~ P = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }$ (c) $P = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] }$ (d) $P = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } & { 0 } \end{array} \right] }$

4. (a) $P = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { } & { } & { } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }$ (b) $P = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] }$ (c) $P = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \end{array} \right] }$ (d) $P = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] }$

5. \*( ${ \mathrm { ~ a ) ~ } } L = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 1 . 5 } & { 1 } & { 0 } \\ { 1 . 5 } & { 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } U = { \left[ \begin{array} { l l l } { 2 } & { - 1 } & { 1 } \\ { 0 } & { 4 . 5 } & { 7 . 5 } \\ { 0 } & { 0 } & { - 4 } \end{array} \right] }$ (b) $\begin{array}{c} { \begin{array} { r l } & { L = { \Biggl [ } { \mathrm { - } } 2 . 1 0 6 7 1 9 \qquad \ 0 \qquad 0 { \mathrm { } } { \mathrm { } } } \\ & { \left. 3 . 0 6 7 1 9 3 \qquad 1 . 1 9 7 7 5 6 \ 1 { \mathrm { } } ^ { \mathrm { } } \right] \ { \mathrm { a n d } } \ U = { \Biggl [ } { \begin{array} { c c c c } { 1 . 0 1 2 } & { - 2 . 1 3 2 } & { 3 . 1 0 4 } \\ { 0 } & { - 0 . 3 9 5 5 2 5 7 } & { - 0 . 4 7 3 7 4 4 3 } \\ { 0 } & { 0 } & { - 8 . 9 3 9 1 4 1 } \end{array} } { \Biggl ] } } \\ & { L = { \Biggl [ } 0 . 5 \qquad 0 \qquad 0 \qquad 0 } \\ { 0 . \qquad 1 \qquad 1 \qquad 0 \qquad 0 } \\ { 0 \qquad \quad - 2 \qquad 1 \ 1 0 } & { 0 } \\ { 1 \qquad \quad - 1 . 3 3 3 3 3 \ 2 \ 1 4 } \end{array} \qquad { \mathrm { a n d } } \ U = { \Biggl [ } { \begin{array} { c c c c } { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 . 5 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 . 5 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } { \Biggr ] } } \end{array} $ (c)   
(d) $L = \left[ \begin{array} { c c c c } { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { - 1 . 8 4 9 1 9 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { - 0 . 4 5 9 6 4 3 3 } } & { { - 0 . 2 5 0 1 2 1 9 } } & { { 1 } } & { { 0 } } \\ { { 2 . 7 6 8 6 6 1 } } & { { - 0 . 3 0 7 9 4 3 5 } } & { { - 5 . 3 5 2 2 8 3 } } & { { 1 } } \end{array} \right]$ and $U = \left[ \begin{array} { c c c c } { { 2 . 1 7 5 6 0 0 } } & { { 4 . 0 2 3 0 9 9 } } & { { - 2 . 1 7 3 1 9 9 } } & { { 5 . 1 9 6 7 0 0 } } \\ { { 0 } } & { { 1 3 . 4 3 9 4 7 } } & { { - 4 . 0 1 8 6 6 0 } } & { { 1 0 . 8 0 6 9 8 } } \\ { { 0 } } & { { 0 } } & { { - 0 . 8 9 2 9 5 1 0 } } & { { 5 . 0 9 1 6 9 2 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 2 . 0 3 6 1 4 } } \end{array} \right]$   
6. (a) $L = \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } \\ { - 1 } & { 1 / 2 } & { 1 } \end{array} } \right] { \mathrm { ~ a n d ~ } } U = \left[ { \begin{array} { c c c } { 1 } & { - 1 } & { 0 } \\ { 0 } & { 4 } & { 3 } \\ { 0 } & { 0 } & { 1 / 2 } \end{array} } \right]$   
(b) $L = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 3 / 5 } & { 1 } & { 0 } \\ { 6 / 5 } & { - 3 8 / 1 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } U = { \left[ \begin{array} { l l l } { 1 / 3 } & { 1 / 2 } & { - 1 / 4 } \\ { 0 } & { 1 1 / 3 0 } & { 2 1 / 4 0 } \\ { 0 } & { 0 } & { 2 4 1 / 8 8 } \end{array} \right] }$ (c) $L = \left[ { \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { - 1 / 2 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { - 6 / 7 } & { 1 } & { 0 } \\ { - 1 } & { 6 / 7 } & { - 4 / 2 5 } & { 1 } \end{array} } \right]$ and   
(d) ${ \begin{array} { l } { U = { \left[ \begin{array} { l l l l l } { 2 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 7 / 2 } & { 3 } & { 0 } \\ { 0 } & { 0 } & { 2 5 / 7 } & { 4 } \\ { 0 } & { 0 } & { 0 } & { 1 4 1 / 2 5 } \end{array} \right] } } \\ { L = { \left[ \begin{array} { l l l l l } { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { - 0 . 6 0 6 1 9 6 } & { - 0 . 1 6 8 4 6 5 } & { 1 } & { 0 } \\ { 0 . 4 1 3 2 8 9 } & { 0 . 7 7 8 8 1 6 } & { - 0 . 7 0 7 7 2 3 } & { 1 } \end{array} \right] } } \end{array} }$ and $U = \left[ \begin{array} { c c c c } { { 5 . 1 3 1 2 } } & { { 1 . 4 1 4 } } & { { 3 . 1 4 1 } } & { { 0 } } \\ { { 0 } } & { { 5 . 1 9 3 } } & { { - 2 . 1 9 7 } } & { { 5 . 9 2 0 5 6 } } \\ { { 0 } } & { { 0 } } & { { 4 . 2 5 1 9 5 } } & { { 4 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 2 . 6 8 2 8 } } \end{array} \right]$

7. The modified $L U$ algorithm gives the following:

(a) $x _ { 1 } = 1$ , $x _ { 2 } = 2$ , $x _ { 3 } = - 1$   
(b) $x _ { 1 } = 1$ , $x _ { 2 } = 1$ , $x _ { 3 } = 1$   
(c) $x _ { 1 } = 1 . 5$ , $x _ { 2 } = 2$ , $x _ { 3 } = - 1 . 1 9 9 9 9 8$ , $x _ { 4 } = 3$   
(d) $x _ { 1 } = 2 . 9 3 9 8 5 1$ , $x _ { 2 } = 0 . 0 7 0 6 7 7 7 0$ , $x _ { 3 } = 5 . 6 7 7 7 3 5$ , $x _ { 4 } = 4 . 3 7 9 8 1 2$

8. The modified $L U$ algorithm gives the following:

(a) $x _ { 1 } = - 1 2 , x _ { 2 } = - 1 4 , x _ { 3 } = 1 7$ (b) $x _ { 1 } = - 4 9 5 / 2 4 1$ , $x _ { 2 } = 8 4 0 / 2 4 1$ , x3 =56/241 (c) $x _ { 1 } = - 2 9 / 4 7$ , $x _ { 2 } = 5 8 / 4 7$ , $x _ { 3 } = 3 2 / 1 4 1$ , x4 =52/141 (d) $x _ { 1 } = - 0 . 7 0 6 1 2 3$ , $x _ { 2 } = - 0 . 1 8 7 4 1 0$ , $x _ { 3 } = 0 . 5 6 9 1 8 8$ , $x _ { 4 } = 0 . 5 2 8 7 0 4$

9. \*(a) $P ^ { t } L U = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { - { \frac { 1 } { 2 } } } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { 1 } & { - 1 } \\ { 0 } & { 2 } & { 3 } \\ { 0 } & { 0 } & { { \frac { 5 } { 2 } } } \end{array} \right] }$

$$
P ^ { t } L U = [ { \begin{array} { r r r } { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} } [ { \begin{array} { r r r } { 1 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } \end{array} } ] [ { \begin{array} { r r r } { 1 } & { 2 } & { - 1 } \\ { 0 } & { - 5 } & { 6 } \\ { 0 } & { 0 } & { 4 } \end{array} } ]
$$

$$
P ^ { t } L U = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 1 } & { 0 } \\ { 3 } & { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { - 2 } & { 3 } & { 0 } \\ { 0 } & { 5 } & { - 2 } & { 1 } \\ { 0 } & { 0 } & { - 1 } & { - 2 } \\ { 0 } & { 0 } & { 0 } & { 3 } \end{array} \right] }
$$

$$
P ^ { t } L U = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 2 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l l l } { 1 } & { - 2 } & { 3 } & { 0 } \\ { 0 } & { 5 } & { - 3 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } & { - 2 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

$^ { * } 1 0$ . (a) To compute $P ^ { t } L U$ requires ${ \textstyle { \frac { 1 } { 3 } } } n ^ { 3 } - { \textstyle { \frac { 1 } { 3 } } } n$ Multiplications/Divisions and ${ \textstyle { \frac { 1 } { 3 } } } n ^ { 3 } - { \textstyle { \frac { 1 } { 2 } } } n ^ { 2 } + { \textstyle { \frac { 1 } { 6 } } } n$ Additions/Subtractions. (b) If $\ddot { P }$ is obtained from $P$ by a simple row interchange, then $\operatorname* { d e t } \tilde { P } = - \operatorname* { d e t } P$ . Thus, if $\ddot { P }$ is obtained from $P$ by $k$ interchanges, we have $\operatorname* { d e t } \tilde { P } = ( - 1 ) ^ { k } \operatorname* { d e t } P$ . (c) Only $n - 1$ multiplications are needed in addition to the operations in part (a). (d) We have det $A = - 7 4 1$ . Factoring and computing det $A$ requires 75 Multiplications/Divisions and 55 Additions/Subtractions.

\*11. (a) The steps in Algorithm 6.4 give the following:   

<table><tr><td>Multiplications/Divisions</td><td>Additions/Subtractions</td></tr><tr><td>Step 2 n-1 n-1：</td><td>0 n-1</td></tr><tr><td>Step 4</td><td>∑=i-1 i2i-1</td></tr><tr><td>Step 5 £i=2 -n-1 n ∑j=i+1 [2(𝑖-1) +1]</td><td>n-1 Cj=i+12(i-1) In i=2</td></tr><tr><td>Step 6</td><td>n-1 n-1</td></tr><tr><td>Totals</td><td>n-n n²-n²+n</td></tr></table>

(b) The equations are given by

$$
y _ { 1 } = \frac { b _ { 1 } } { l _ { 1 1 } } \quad \mathrm { a n d } \quad y _ { i } = b _ { i } - \sum _ { j = 1 } ^ { i - 1 } \frac { l _ { i j } y _ { j } } { l _ { i i } } , \quad \mathrm { f o r } i = 2 , \dots , n .
$$

If we assume that $l _ { i i } ~ = ~ 1$ , for each $i = 1 , 2 , \dots , n$ , then the number of Multiplications/Divisions is

$$
\sum _ { i = 2 } ^ { n } ( i - 1 ) = { \frac { n ( n - 1 ) } { 2 } } ,
$$

and the number of Additions/Subtractions is the same.

(c)

<table><tr><td></td><td>Multiplications/divisionsAdditions/subtractions</td></tr><tr><td>Factoring into LU</td><td>n n²-n²+n</td></tr><tr><td>Solving Ly = b</td><td>n²-n</td></tr><tr><td>Solving Ux = y</td><td>n²-n n²+n n²-n</td></tr><tr><td>Total</td><td>n³+n²-n n+n²-n</td></tr></table>

(d)

<table><tr><td></td><td>Multiplications/divisions</td><td>Additions/subtractions</td></tr><tr><td>Factoring into LU</td><td>n-n</td><td>n-n²+n</td></tr><tr><td>Solving Ly(k) = b(k)</td><td>(n²-n)m</td><td>(n²-n)m</td></tr><tr><td>Solving Ux(k) = y(k)</td><td>(n²+n）m</td><td>(n²-n)m</td></tr><tr><td>Total</td><td>n³+mn²-n</td><td>n³+(m-)n²-(m-)n</td></tr></table>

# Exercise Set 6.6, page 425

1. (i) The only symmetric matrix is (a). (ii) All are nonsingular. (iii) Matrices (a) and (b) are strictly diagonally dominant. (iv) The only positive definite matrix is (a).

2. (i) Matrices (a) and (c) are symmetric. (ii) Matrices (a), (b), and (c) are nonsingular. (iii) Matrices (a) and (b) are strictly diagonally dominant. (iv) Matrices (b) and (c) are positive definite.

3. The $L D L ^ { t }$ factorization of the matrices $A$ have the following forms.

$$
L = \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { - { \frac { 1 } { 2 } } } & { 1 } & { 0 } \\ { 0 } & { - { \frac { 2 } { 3 } } } & { 1 } \end{array} } \right] , D = \left[ { \begin{array} { c c c } { 2 } & { 0 } & { 0 } \\ { 0 } & { { \frac { 3 } { 2 } } } & { 0 } \\ { 0 } & { 0 } & { { \frac { 4 } { 3 } } } \end{array} } \right]
$$

$$
L = { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { 1 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { - 0 . 4 5 4 5 4 5 4 5 } & { 1 } & { 0 } \\ { 0 . 2 5 } & { 0 . 2 7 2 7 2 7 } & { 0 . 0 7 6 9 2 3 0 7 7 } & { 1 } \end{array} \right] } , \quad D = { \left[ \begin{array} { l l l l } { 4 . 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 . 7 5 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 . 1 8 1 8 1 8 2 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 . 5 3 8 4 6 1 5 } \end{array} \right] }
$$

$$
L = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { 1 } & { 0 } & { 0 } \\ { - 0 . 2 5 } & { - 0 . 2 7 2 7 2 7 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 . 4 4 } & { 1 } \end{array} \right] , \quad D = \left[ \begin{array} { c c c c } { 4 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 . 7 5 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 4 . 5 4 5 4 5 4 5 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 3 . 1 2 } \end{array} \right]
$$

$$
L = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 . 3 3 3 3 3 3 3 } & { 1 } & { 0 } & { 0 } \\ { 0 . 1 6 6 6 6 6 7 } & { 0 . 2 } & { 1 } & { 0 } \\ { - 0 . 1 6 6 6 6 6 7 } & { 0 . 1 } & { - 0 . 2 4 3 2 4 3 2 4 } & { 1 } \end{array} \right] , \quad D = \left[ \begin{array} { c c c c } { 6 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 3 . 3 3 3 3 3 3 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 3 . 7 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 2 . 5 8 1 0 8 1 1 } \end{array} \right]
$$

4. The $L D L ^ { t }$ factorization of the matrices $A$ have the following forms.

$$
L = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { - 0 . 2 5 } & { 1 } & { 0 } \\ { 0 . 2 5 } & { 0 . 0 9 0 9 0 9 } & { 1 } \end{array} \right] , D = \left[ \begin{array} { c c c } { 4 } & { 0 } & { 0 } \\ { 0 } & { 2 . 7 5 } & { 0 } \\ { 0 } & { 0 } & { 1 . 7 2 7 2 7 2 7 3 } \end{array} \right]
$$

$$
L = \left[ { \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 . 5 } & { 1 } & { 0 } \\ { 0 . 5 } & { 0 . 2 } & { 1 } \end{array} } \right] , \quad D = \left[ { \begin{array} { l l l } { 4 } & { 0 } & { 0 } \\ { 0 } & { 5 } & { 0 } \\ { 0 } & { 0 } & { 3 . 6 } \end{array} } \right]
$$

$$
L = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 . 5 } & { - 0 . 3 3 3 3 3 3 } & { 1 } & { 0 } \\ { 0 . 2 5 } & { 0 . 3 3 3 3 3 3 3 } & { 0 . 6 . 0 7 1 4 2 8 6 } & { 1 } \end{array} \right] , \quad D = \left[ \begin{array} { c c c c } { 4 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 3 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 4 . 6 6 6 6 7 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 5 . 6 9 6 4 2 9 } \end{array} \right]
$$

$$
L = \left[ \begin{array} { c c c c } { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { 1 } & { 0 } & { 0 } \\ { 0 . 2 5 } & { - 0 . 9 0 9 0 9 0 9 } & { 1 } & { 0 } \\ { 0 . 2 5 } & { - 0 . 4 5 4 5 4 5 5 } & { 0 . 3 6 8 4 2 1 1 } & { 1 } \end{array} \right] , \quad D = \left[ \begin{array} { c c c c } { 4 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 . 7 5 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 . 7 2 7 2 7 3 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 2 . 9 4 7 3 6 8 } \end{array} \right]
$$

5. Cholesky’s Algorithm gives the following results.

(a) $L = \left[ \begin{array} { c c c } { { 1 . 4 1 4 2 1 3 } } & { { 0 } } & { { 0 } } \\ { { - 0 . 7 0 7 1 0 6 9 } } & { { 1 . 2 2 4 7 4 3 } } & { { 0 } } \\ { { 0 } } & { { - 0 . 8 1 6 4 9 7 2 } } & { { 1 . 1 5 4 6 9 9 } } \end{array} \right]$   
(b) $L = \left[ \begin{array} { c c c c } { { 2 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 . 5 } } & { { 1 . 6 5 8 3 1 1 } } & { { 0 } } & { { 0 } } \\ { { 0 . 5 } } & { { - 0 . 7 5 3 7 7 8 5 } } & { { 1 . 0 8 7 1 1 3 } } & { { 0 } } \\ { { 0 . 5 } } & { { 0 . 4 5 2 2 6 7 1 } } & { { 0 . 0 8 3 6 2 4 4 2 } } & { { 1 . 2 4 0 3 4 6 } } \end{array} \right]$   
(c) $L = \left[ \begin{array} { l l l l } { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 . 5 } & { 1 . 6 5 8 3 1 1 } & { 0 } & { 0 } \\ { - 0 . 5 } & { - 0 . 4 5 2 2 6 7 1 } & { 2 . 1 3 2 0 0 6 } & { 0 } \\ { 0 } & { 0 } & { 0 . 9 3 8 0 8 3 3 } & { 1 . 7 6 6 3 5 1 } \end{array} \right]$ 2.449489 0 0 0   
(d) L = 0.4082483 0.8164966 1.825741 0.3651483 0 1.923538 0 0 0.4082483 0.1825741 0.4678876 1.606574

6. Cholesky’s Algorithm gives the following results.

$$
L = \left[ \begin{array} { c c c } { { 2 } } & { { 0 } } & { { 0 } } \\ { { - 1 / 2 } } & { { \sqrt { 1 1 } / 2 } } & { { 0 } } \\ { { 1 / 2 } } & { { \sqrt { 1 1 } / 2 2 } } & { { \sqrt { 2 0 9 } / 1 1 } } \end{array} \right]
$$

$$
L = { \left[ \begin{array} { l l l } { 2 } & { 0 } & { 0 } \\ { 1 } & { { \sqrt { 5 } } } & { 0 } \\ { 1 } & { { \sqrt { 5 } } / 5 } & { { \sqrt { 9 5 } } / 5 } \end{array} \right] }
$$

$$
L = \left[ \begin{array} { l l l l } { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { \sqrt { 3 } } & { 0 } & { 0 } \\ { 1 } & { - \sqrt { 3 } / 3 } & { \sqrt { 4 2 } / 3 } & { 0 } \\ { 1 / 2 0 } & { \sqrt { 3 } / 3 } & { 1 7 \sqrt { 4 2 } / 8 4 } & { \sqrt { 4 4 6 6 } / 2 8 } \end{array} \right]
$$

$$
L = { \left[ \begin{array} { l l l l } { 2 } & { 0 } & { 0 } & { 0 } \\ { 1 / 2 } & { { \sqrt { 1 1 } } / 2 } & { 0 } & { 0 } \\ { 1 / 2 } & { - { \sqrt { 1 1 } } / 2 2 } & { { \sqrt { 2 0 9 } } / 1 1 } & { 0 } \\ { 1 / 2 } & { - 5 { \sqrt { 1 1 } } / 2 2 } & { 7 { \sqrt { 2 0 9 } } / 2 0 9 } & { 2 { \sqrt { 2 6 6 } } / 1 9 } \end{array} \right] }
$$

7. The modified factorization algorithm gives the following results.

(a) $x _ { 1 } = 1$ , $x _ { 2 } = - 1$ , $x _ { 3 } = 0$ (b) $x _ { 1 } = 0 . 2$ , $x _ { 2 } = - 0 . 2$ , $x _ { 3 } = - 0 . 2$ , $x _ { 4 } = 0 . 2 5$ (c) $x _ { 1 } = 1$ , $x _ { 2 } = 2$ , $x _ { 3 } = - 1$ , $x _ { 4 } = 2$

(d) $x _ { 1 } = - 0 . 8 5 8 6 3 8 7$ , $x _ { 2 } = 2 . 4 1 8 8 4 8$ , $x _ { 3 } = - 0 . 9 5 8 1 1 5 2$ , $x _ { 4 } = - 1 . 2 7 2 2 5 1$

8. The modified factorization algorithm gives the following results.

(a) $x _ { 1 } = - 1 3 / 1 9 , x _ { 2 } = 2 1 / 1 9 , x _ { 3 } = 5 4 / 1 9$ (b) $x _ { 1 } = - 3 / 3 8$ , $x _ { 2 } = 4 / 1 9$ , $x _ { 3 } = - 1 / 1 9$ (c) $x _ { 1 } = - 4 5 2 / 3 1 9$ , $x _ { 2 } = 3 7 3 / 3 1 9$ , $x _ { 3 } = 7 6 3 / 3 1 9$ , $x _ { 4 } = - 3 5 6 / 3 1 9$ (d) $x _ { 1 } = 5 / 2 8$ , $x _ { 2 } = 5 / 7$ , $x _ { 3 } = 1 / 4$ , $x _ { 4 } = 9 / 2 8$

9. The modified Cholesky’s algorithm gives the following results.

(a) $x _ { 1 } = 1 , x _ { 2 } = - 1 , x _ { 3 } = 0$   
(b) $x _ { 1 } = 0 . 2 , x _ { 2 } = - 0 . 2 , x _ { 3 } = - 0 . 2 , x _ { 4 } = 0 . 2 5$   
(c) $x _ { 1 } = 1 , x _ { 2 } = 2 , x _ { 3 } = - 1 , x _ { 4 } = : 2$   
(d) $x _ { 1 } = - 0 . 8 5 8 6 \div 3 8 7 4 , x _ { 2 } = 2 . 4 1 8 8 4 8 \div 2 , x _ { 3 } = - 0 . 9 5 8 1 1 5 1 8 , x _ { 4 } = - 1 . 2 7 2 2 5$

10. (a) $x _ { 1 } = - 0 . 6 8 4 2 1 0 5 2 6 5 , x _ { 2 } = 1 . 1 0 5 2 6 3 1 5 8 , x _ { 3 } = 2 . 8 4 2 1 0 5 2 6 3$ (b) $x _ { 1 } = - 0 . 0 7 8 9 4 7 3 6 8 9 0 , x _ { 2 } = 0 . 2 1 0 5 2 6 3 1 5 8 , x _ { 3 } = - 0 . 0 5 2 6 3 1 5 7 8 9 5$ 5 (c) $\mathfrak { c } _ { 1 } = - 1 . 4 1 6 9 2 7 9 0 0 , x _ { 2 } = 1 . 1 6 9 2 7 8 9 9 7 , x _ { 3 } = 2 . 3$ $x _ { 2 } = 1 . 1 6 9 2 7 8 9 9 7 , x _ { 3 } = 2 . 3 9 1 8 4 9 5 3 0 , x _ { 4 } = - 1 . 1$ 15987461 (d) $x _ { 1 } = 0 . 1 7 8 5 7 1 4 2 8 6 , x _ { 2 } = 0 . 7 1 4 2 8 5 7 1 4 2 , x _ { 3 } = 0 . 2 5 , x _ { 4 } = 0 . 3 2 1 4 2 8 5 7 1 4 2 , x _ { 5 } = 0 . 2 4 2 , x _ { 6 } = 0 . 2 5 , x _ { 7 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 9 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 . 2 5 , x _ { 8 } = 0 .$

11. The Crout Factorization Algorithm gives the following results.

$^ *$ (a) $x _ { 1 } = 0 . 5$ , $x _ { 2 } = 0 . 5$ , $x _ { 3 } = 1$   
(b) $x _ { 1 } = - 0 . 9 9 9 9 9 9 5$ , $x _ { 2 } = 1 . 9 9 9 9 9 9 9$ , $x _ { 3 } = 1$   
(c) $x _ { 1 } = 1$ , $x _ { 2 } = - 1$ , $x _ { 3 } = 0$   
(d) $x _ { 1 } = - 0 . 0 9 3 5 7 7 9 8$ , $x _ { 2 } = 1 . 5 8 7 1 5 6$ , $x _ { 3 } = - 1 . 1 6 7 4 3 1$ , $x _ { 4 } = 0 . 5 4 1 2 8 4 4$

12. The Crout Factorization Algorithm gives the following results.

(a) $x _ { 1 } = 3 . 6 0 0 0 0 0 0 0 0$ , $x _ { 2 } = - 4 . 2 0 0 0 0 0 0 0 0$ , $x _ { 3 } = 2 . 8 0 0 0 0 0 0 0 0$   
(b) $x _ { 1 } = 3 . 9 4 4 4 4 4 4 4 4$ , $x _ { 2 } = 2 . 8 8 8 8 8 8 8 9$ , $x _ { 3 } = - 0 . 7 2 2 2 2 2 2 2 2 2$   
(c) $x _ { 1 } = 2 . 3 8 0 9 5 2 3 8 1$ , $x _ { 2 } = 1 . 7 6 1 9 0 4 7 6 2$ , $x _ { 3 } = 1 . 9 0 4 7 6 1 9 0 5$ , $x _ { 4 } = 2 . 0 4 7 6 1 9 0 4 8$   
(d) $x _ { 1 } ~ = ~ 0 . 6 6 6 6 6 6 6 6 7$ , $x _ { 2 } ~ = ~ 0 . 3 3 3 3 3 3 3 3 3 4$ , $x _ { 3 } ~ = ~ - 0 . 6 6 6 6 6 6 6 6 6 6$ , $x _ { 4 } ~ = ~ - 1 . 0 0 0 0 0 0 0 0 0$ , $x _ { 5 } = 0 . 0 0 0 0 0 0 0 0$

13. We have $x _ { i } = 1$ , for each $i = 1 , \ldots , 1 0$ .

14. The modified $L D L ^ { t }$ factorization gives the following results.

(a)

$$
L = \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } \\ { 2 } & { 1 } & { 1 } \end{array} } \right] , \qquad D = \left[ { \begin{array} { c c c } { 3 } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 2 } \end{array} } \right]
$$

$$
L = \left[ { \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { - 2 } & { 1 } & { 0 } \\ { 3 } & { - 1 } & { 1 } \end{array} } \right] , \qquad D = \left[ { \begin{array} { l l l } { 3 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} } \right]
$$

$$
L = \left[ \begin{array} { c c c c } { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { - 2 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 2 } } & { { 1 } } & { { 0 } } \\ { { - 1 } } & { { 1 } } & { { 4 } } & { { 1 } } \end{array} \right] , \qquad D = \left[ \begin{array} { c c c c } { { - 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { - 4 } } \end{array} \right]
$$

$$
L = \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } & { 0 } \\ { 2 } & { 0 } & { 1 } & { 0 } \\ { - 2 } & { 1 } & { - 1 } & { 1 } \end{array} \right] , \qquad D = \left[ \begin{array} { l l l l } { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 3 } \end{array} \right]
$$

15. Only the matrix in (d) is positive definite.

16. When $\begin{array} { r } { \alpha > { \frac { 8 } { 7 } } } \end{array}$ the matrix is positive definite.

$^ *$ 17. When $\textstyle - 2 < \alpha < { \frac { 3 } { 2 } }$ the matrix is positive definite.

18. When $0 < \beta < \frac { \perp } { 2 }$ and $\beta + 2 < | \alpha | < 3$ the matrix is strictly diagonally dominant.

$^ { * } 1 9$ . When $0 < \beta < 1$ and $3 < \alpha < 5 - \beta$ the matrix is strictly diagonally dominant.

$^ { * } 2 0$ . (a) Yes. (b) $\begin{array} { r l } & { \mathrm { N o t ~ n e c e s s a r i l y . ~ C o n s i d e r } \left[ \begin{array} { l l } { 2 } & { - 1 } \\ { 3 } & { 4 } \end{array} \right] . } \\ & { \mathrm { N o t ~ n e c e s s a r i l y . ~ C o n s i d e r } \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 2 } \end{array} \right] \quad \mathrm { a n d } \quad \left[ \begin{array} { l l } { - 2 } & { 1 } \\ { 1 } & { - 2 } \end{array} \right] . } \\ & { \mathrm { N o t ~ n e c e s s a r i l y . ~ C o n s i d e r } \left[ \begin{array} { l l } { 2 } & { - 1 } \\ { 3 } & { 4 } \end{array} \right] . } \\ & { \mathrm { N o t ~ n e c e s s a r i l y . ~ C o n s i d e r } \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 2 } \end{array} \right] \quad \mathrm { a n d } \quad \left[ \begin{array} { l l } { 2 } & { - 1 } \\ { - 1 } & { 2 } \end{array} \right] . } \end{array}$ (c) (d) (e)

21. (a) No; for example, consider $\left[ { \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} } \right]$ . (b) Yes, since $A = A ^ { t }$ . (c) Yes, since $\mathbf { x } ^ { t } ( A + B ) \mathbf { x } = \mathbf { x } ^ { t } A \mathbf { x } + \mathbf { x } ^ { t } B \mathbf { x }$ . (d) Yes, since $\mathbf { x } ^ { t } A ^ { 2 } \mathbf { x } = \mathbf { x } ^ { t } A ^ { t } A \mathbf { x } = ( A \mathbf { x } ) ^ { t } ( A \mathbf { x } ) \geq 0$ , and because $A$ is nonsingular, equality holds only if $\mathbf { x } = \mathbf { 0 }$ . (e) No; for example, consider $A = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] }$ and $B = { \left[ \begin{array} { l l } { 1 0 } & { ~ 0 } \\ { 0 } & { 1 0 } \end{array} \right] }$ .

\*22. (a) When $\alpha = 2$ the matrix is singular. (b) The matrix $A$ cannot be strictly diagonally dominant regardless of $\alpha$ . (c) The matrix is symmetric for all values of $\alpha$ . (d) The matrix is positive definite when $\alpha > 2$ .

23. (a) Since $\operatorname* { d e t } A = 3 \alpha - 2 \beta$ , the matrix $A$ is singular if and only if $\alpha = 2 \beta / 3$ . (b) The matrix is strictly diagonally dominant when $| \alpha | > 1$ and $| \beta | < 1$ . (c) The matrix is symmetric when $\beta = 1$ . (d) The matrix is positive definite when $\alpha > \frac { 2 } { 3 }$ and $\beta = 1$ .

24. Yes, since $A ^ { t } B ^ { t } = ( B A ) ^ { t } = ( A B ) ^ { t } = B ^ { t } A ^ { t }$ .

25. One example is $A = \left[ \begin{array} { l l } { 1 . 0 } & { 0 . 2 } \\ { 0 . 1 } & { 1 . 0 } \end{array} \right]$ .

26. Partition $A ^ { ( k ) }$ into the form

$$
\begin{array} { r } { A ^ { ( k ) } = \left[ \begin{array} { c c c c c c c c } { a _ { 1 1 } ^ { ( 1 ) } } & { a _ { 1 2 } ^ { ( 1 ) } } & { \ldots } & { a _ { 1 , k } ^ { ( 1 ) } } & { a _ { 1 , k + 1 } ^ { ( 1 ) } } & { \ldots } & { a _ { l , n } ^ { ( 1 ) } } \\ { 0 } & { a _ { 2 2 } ^ { ( 2 ) } } & { \ldots } & { a _ { 2 k } ^ { ( 2 ) } } & { a _ { 2 k + 1 } ^ { ( 2 ) } } & { \ldots } & { a _ { 2 n } ^ { ( 2 ) } } \\ { \vdots } & { \ddots } & { \ddots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { \ldots } & { 0 } & { a _ { k , k } ^ { ( k ) } } & { a _ { k , k + 1 } ^ { ( k ) } } & { \ldots } & { a _ { k , n } ^ { ( k ) } } \\ & & & & & & { a _ { k + 1 , k } ^ { ( k ) } } & { \ldots } & { a _ { k + 1 , n } ^ { ( k ) } } \\ { 0 } & { \ldots } & { 0 } & { a _ { k + 1 , k } ^ { ( k ) } } & { a _ { k + 1 , k + 1 } ^ { ( k ) } } & { \ldots } & { a _ { k + 1 , n } ^ { ( k ) } } \\ { \vdots } & { \ddots } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { \ldots } & { 0 } & { a _ { n , k } ^ { ( k ) } } & { a _ { n , k + 1 } ^ { ( k ) } } & { \ldots } & { a _ { n , n } ^ { ( k ) } } \end{array} \right] = \left[ \begin{array} { c c } { A _ { 1 1 } ^ { ( k ) } } & { A _ { 1 2 } ^ { ( k ) } } \\ { A _ { 2 1 } ^ { ( k ) } } & { A _ { 2 2 } ^ { ( k ) } } \end{array} \right] . } \end{array}
$$

The multiplier matrix $M ^ { ( k - 1 ) }$ and $A ^ { ( k - 1 ) }$ can be similarly partitioned into

$$
\begin{array} { r } { \mathbb { M } ^ { ( k - 1 ) } = \left[ \begin{array} { l l l l l l l l l } { 1 } & { 0 } & { \cdots } & { \cdots } & { 0 } & { 0 } & { \cdots } & { \cdots } & { 0 } \\ { 0 } & { \ddots } & { \ddots } & { } & { } & { \vdots } & { \vdots } & { } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { } & { } & { \vdots } & { \vdots } & { } & { \vdots } \\ { 0 } & { \cdots } & { 0 } & { 1 } & { 0 } & { \vdots } & { } & { \vdots } & { } \\ { 0 } & { \cdots } & { 0 } & { - m _ { k , k - 1 } } & { 1 } & { 0 } & { \cdots } & { \cdots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { - m _ { k + 1 , k - 1 } } & { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { - m _ { k + 1 , k - 1 } } & { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { 0 } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { - m _ { n , k - 1 } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] = \left[ \begin{array} { l } { M _ { 1 1 } ^ { ( k - 1 ) } } \\ { M _ { 2 1 } ^ { ( k - 1 ) } } \\ { M _ { 2 1 } ^ { ( k - 1 ) } } \end{array} \right] , } \end{array}
$$

where $M _ { 1 1 } ^ { ( k - 1 ) }$ is a $k \times k$ lower triangular matrix, $O$ is a $k \times ( n - k )$ block of zeros, $M _ { 2 1 } ^ { ( k - 1 ) }$ is $( n - k ) \times k$ matrix, $I$ identity matrix, and

$$
A ^ { ( k - 1 ) } = \left[ \begin{array} { l l } { A _ { 1 1 } ^ { ( k - 1 ) } } & { A _ { 1 2 } ^ { ( k - 1 ) } } \\ { A _ { 2 1 } ^ { ( k - 1 ) } } & { A _ { 2 2 } ^ { ( k - 1 ) } } \end{array} \right] .
$$

Here A(k−11 is $k \times k$ , $A _ { 1 2 } ^ { ( k - 1 ) }$ is $k \times ( n - k )$ , $A _ { 2 1 } ^ { ( k - 1 ) }$ is $( n - k ) \times k$ , and $A _ { 2 2 } ^ { ( k - 1 ) }$ is $( n - k ) \times ( n - k )$ . The formation of ${ A } _ { 1 1 } ^ { ( k ) }$ can be obtained from the partitioned product of $M ^ { ( k - 1 ) }$ and $A ^ { ( k - 1 ) }$ and is given by

$$
A _ { 1 1 } ^ { ( k ) } = M _ { 1 1 } ^ { ( k - 1 ) } A _ { 1 1 } ^ { ( k - 1 ) } + 0 \cdot A _ { 2 1 } ^ { ( k - 1 ) } = M _ { 1 1 } ^ { ( k - 1 ) } A _ { 1 1 } ^ { ( k - 1 ) } .
$$

In a similar manner, each of $M ^ { ( k - 2 ) } , \ldots , M ^ { ( 1 ) }$ and $A ^ { ( k - 2 ) } , \ldots , A ^ { ( 1 ) }$ can be partitioned to obtain

$$
A _ { 1 1 } ^ { ( k ) } = M _ { 1 1 } ^ { ( k - 1 ) } A _ { 1 1 } ^ { ( k - 1 ) } = M _ { 1 1 } ^ { ( k - 1 ) } M _ { 1 1 } ^ { ( k - 2 ) } A _ { 1 1 } ^ { ( k - 2 ) } = \ldots = M _ { 1 1 } ^ { ( k - 1 ) } M _ { 1 1 } ^ { ( k - 2 ) } \ldots M _ { 1 1 } ^ { ( 1 ) } A _ { 1 1 } ^ { ( 1 ) } ,
$$

where $A _ { 1 1 } ^ { ( 1 ) } = A _ { 1 1 }$ is the $k \times k$ leading principal submatrix of $A$ . Assume all leading principal submatrices of $A$ are nonsingular. Then $a _ { 1 1 } \neq 0$ , and the elimination process can be started. For the inductive hypothesis, assume that $k - 1$ elimination steps can be performed without row interchanges. It follows that $a _ { 1 1 } ^ { ( 1 ) } , \ldots , a _ { k - 1 , k - 1 } ^ { ( k - 1 ) }$ are all nonzero and the above equation holds. Taking determinants produces

$$
a _ { 1 1 } ^ { ( 1 ) } a _ { 2 2 } ^ { ( 2 ) } \ldots a _ { k - 1 , k - 1 } ^ { ( k - 1 ) } a _ { k , k } ^ { ( k ) } = \operatorname* { d e t } A _ { 1 1 } ^ { ( k ) } = \operatorname* { d e t } M _ { 1 1 } ^ { ( k - 1 ) } \operatorname* { d e t } M _ { 1 1 } ^ { ( k - 2 ) } \ldots \operatorname* { d e t } M _ { 1 1 } ^ { ( 1 ) } \operatorname* { d e t } A _ { 1 1 } \neq 0 .
$$

Hence, $a _ { k , k } ^ { ( k ) } \neq 0$ and the process can continue. By mathematical induction all pivot elements $a _ { 1 1 } ^ { ( 1 ) } , \ldots , a _ { n , n } ^ { ( n ) }$ are nonzero and Gaussian elimination can be performed without row interchanges.

Conversely, suppose Gaussian elifollows that all the pivot elements $a _ { 1 1 } ^ { ( 1 ) } , \ldots , a _ { n , n } ^ { ( n ) }$ be performed without row interchanges. It are nonzero. Thus,

$$
\operatorname* { d e t } A _ { 1 1 } = a _ { 1 1 } ^ { ( 1 ) } a _ { 2 2 } ^ { ( 2 ) } \cdot . . a _ { k , k } ^ { ( k ) } \neq 0 ,
$$

and the $k \times k$ principal leading submatrix is nonsingular, for each $k = 1 , 2 , \ldots , n$ .

\*27. The Crout Factorization Algorithm can be rewritten as follows:

STEP 1 Set $l _ { 1 } = a _ { 1 } ; u _ { 1 } = c _ { 1 } / l _ { 1 }$ .   
STEP 2 For $i = 2 , \ldots , n - 1$ set $l _ { i } = a _ { i } - b _ { i } u _ { i - 1 } ; u _ { i } = c _ { i } / l _ { i }$ .   
STEP 3 Set ln = an − bnun 1.   
STEP 4 Set $z _ { 1 } = d _ { 1 } / l _ { 1 }$ .   
STEP 5 For $i = 2 , \ldots , n$ set $z _ { i } = ( d _ { i } - b _ { i } z _ { i - 1 } ) / l _ { i }$ .   
STEP 6 Set $x _ { n } = z _ { n }$ .   
STEP 7 For i = n − 1, . . . , 1 set xi = zi − uixi+1.   
STEP 8 OUTPUT $( x _ { 1 } , \ldots , x _ { n } )$ ;   
STOP.

\*28. First, $\left| l _ { 1 1 } \right| = \left| a _ { 1 1 } \right| > 0$ and $\begin{array} { r } { | u _ { 1 2 } | = \frac { | a _ { 1 2 } | } { | l _ { 1 1 } | } < 1 } \end{array}$ . In general, assume $| l _ { j j } | > 0$ and $| u _ { j , j + 1 } | < 1$ , for $j = 1 , \ldots , i - 1$ . Then

$$
\left| l _ { i i } \right| = \left| a _ { i i } - l _ { i , i - 1 } u _ { i - 1 , i } \right| = \left| a _ { i i } - a _ { i , i - 1 } u _ { i - 1 , i } \right| \geq \left| a _ { i i } \right| - \left| a _ { i , i - 1 } u _ { i - 1 , i } \right| > \left| a _ { i i } \right| - \left| a _ { i , i - 1 } \right| > 0 ,
$$

and

$$
\left| u _ { i , i + 1 } \right| = \frac { \left| a _ { i , i + 1 } \right| } { \left| l _ { i i } \right| } < \frac { \left| a _ { i , i + 1 } \right| } { \left| a _ { i i } \right| - \left| a _ { i , i - 1 } \right| } \leq 1 ,
$$

for $i = 2 , \ldots , n - 1$ . Further,

$$
\left| l _ { n n } \right| = \left| a _ { n n } - l _ { n , n - 1 } u _ { n - 1 , n } \right| = \left| a _ { n n } - a _ { n , n - 1 } u _ { n - 1 , n } \right| \geq \left| a _ { n n } \right| - \left| a _ { n , n - 1 } \right| > 0 .
$$

So

$$
\operatorname* { d e t } A = \operatorname* { d e t } L \cdot \operatorname* { d e t } U = l _ { 1 1 } \cdot l _ { 2 2 } \ldots l _ { n n } \cdot 1 > 0 .
$$

$$
i _ { 1 } = 0 . 6 7 8 5 0 4 7 , \quad i _ { 2 } = 0 . 4 2 1 4 9 5 3 , \quad i _ { 3 } = 0 . 2 5 7 0 0 9 3 , \quad i _ { 4 } = 0 . 1 5 4 2 0 5 6 , \quad i _ { 5 } = 0 . 1 0 2 8 0 3 7
$$

30. The Crout Factorization Algorithm requires $5 n - 4$ Multiplications/Divisions and $3 n - 3$ Additions/Subtractions.

31. (a) Mating male $i$ with female $j$ produces offspring with the same wing characteristics as mating male $j$ with female $i$ . (b) No. Consider, for example, $\mathbf { x } = ( 1 , 0 , - 1 ) ^ { t }$ .

\*32. (a)

$$
D ^ { 1 / 2 } D ^ { 1 / 2 } = \left[ \begin{array} { c c c c c } { \sqrt { d _ { 1 1 } } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \sqrt { d _ { 2 2 } } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { } \\ { 0 } & { \cdots } & { 0 } & { \sqrt { d _ { n n } } } \end{array} \right] \cdot \left[ \begin{array} { c c c c c } { \sqrt { d _ { 1 1 } } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { \sqrt { d _ { 2 2 } } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { \sqrt { d _ { n n } } } \end{array} \right] = \left[ \begin{array} { c c c c c } { d _ { 1 1 } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { d _ { 2 2 } } & { \ddots } & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { d _ { n n } } \end{array} \right] .
$$

(b) We have

$$
\left( \hat { L } D ^ { 1 / 2 } \right) \left( \hat { L } D ^ { 1 / 2 } \right) ^ { t } = \hat { L } D ^ { 1 / 2 } \left( D ^ { 1 / 2 } \right) ^ { t } \hat { L } ^ { t } = \hat { L } D ^ { 1 / 2 } D ^ { 1 / 2 } \hat { L } ^ { t } = \hat { L } D \hat { L } ^ { t } = A .
$$

Since $L L ^ { t } = A$ , we have $\hat { L } D ^ { 1 / 2 } = L$

# Iterative Techniques in Matrix Algebra

Exercise Set 7.1, page 441

1. (a) We have $| | \mathbf { x } | | _ { \infty } = 4$ and $| | \mathbf { x } | | _ { 2 } = 5 . 2 2 0 1 5 3$ . (b) We have $| | \mathbf { x } | | _ { \infty } = 4$ and $| | \mathbf { x } | | _ { 2 } = 5 . 4 7 7 2 2 6$ . (c) We have $| | \mathbf { x } | | _ { \infty } = 2 ^ { k }$ and $| | \mathbf { x } | | _ { 2 } = ( 1 + 4 ^ { k } ) ^ { 1 / 2 }$ . (d) We have $| | \mathbf { x } | | _ { \infty } = 4 / ( k + 1 )$ and $| | \mathbf { x } | | _ { 2 } = ( 1 6 / ( k + 1 ) ^ { 2 } + 4 / k ^ { 4 } + k ^ { 4 } e ^ { - 2 k } ) ^ { 1 / 2 } .$

2. $^ { * } ( \mathrm { a } )$ Since $\begin{array} { r } { \| \mathbf { x } \| _ { 1 } = \sum _ { i = 1 } ^ { n } | x _ { i } | \geq 0 } \end{array}$ with equality only if $x _ { i } = 0$ for all $i$ , properties $( i )$ and $( i i )$ in Definition 7.1 hold. Also,

$$
\| \alpha \mathbf { x } \| _ { 1 } = \sum _ { i = 1 } ^ { n } | \alpha x _ { i } | = \sum _ { i = 1 } ^ { n } | \alpha \| x _ { i } | = | \alpha | \sum _ { i = 1 } ^ { n } | x _ { i } | = | \alpha | \| \mathbf { x } \| _ { 1 } ,
$$

so property $( i i i )$ holds.

Finally,

$$
\| \mathbf { x } + \mathbf { y } \| _ { 1 } = \sum _ { i = 1 } ^ { n } | x _ { i } + y _ { i } | \leq \sum _ { i = 1 } ^ { n } ( | x _ { i } | + | y _ { i } | ) = \sum _ { i = 1 } ^ { n } | x _ { i } | + \sum _ { i = 1 } ^ { n } | y _ { i } | = \| \mathbf { x } \| _ { 1 } + \| \mathbf { y } \| _ { 1 } ,
$$

so property ( $_ { \mathit { l v } }$ ) also holds.

(b) (1a) 8.5 (1b) $1 0 \quad \mathrm { ~ ( 1 c ) ~ } \ : \ : \left| \sin k \right| + | \cos k | + e ^ { k } \quad \mathrm { ~ ( 1 d ) ~ } \ : \ : 4 / ( k + 1 ) + 2 / k ^ { 2 } + k ^ { 2 } e ^ { - k }$ (c) We have

$$
\begin{array} { l } { \displaystyle \| \mathbf { x } \| _ { 1 } ^ { 2 } = \left( \displaystyle \sum _ { i = 1 } ^ { n } | x _ { i } | \right) ^ { 2 } = \left( | x _ { 1 } | + | x _ { 2 } | + \cdot \cdot \cdot + | x _ { n } | \right) ^ { 2 } } \\ { \displaystyle \geq | x _ { 1 } | ^ { 2 } + | x _ { 2 } | ^ { 2 } + \cdot \cdot \cdot + | x _ { n } | ^ { 2 } = \displaystyle \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { 2 } = \| \mathbf { x } \| _ { 2 } ^ { 2 } . } \end{array}
$$

Thus, $\| \mathbf { x } \| _ { 1 } \geq \| \mathbf { x } \| _ { 2 }$ .


<!-- chunk 0004: pages 211-280 -->
3. (a) We have $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } \mathbf { x } ^ { ( k ) } = ( 0 , 0 , 0 ) ^ { t } } \end{array}$ . (b) We have $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } \mathbf { x } ^ { ( k ) } = ( 0 , 1 , 3 ) ^ { t } } \end{array}$ . (c) We have $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } \mathbf { x } ^ { ( k ) } = ( 0 , 0 , \frac { 1 } { 2 } ) ^ { t } } \end{array}$ . (d) We have $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } \mathbf { x } ^ { ( k ) } = ( 1 , - 1 , 1 ) ^ { t } } \end{array}$ .

4. The $l _ { \infty }$ norms are as follows:

(a) 25 (b) 16 (c) 4 (d) 12

5. (a) We have $| | \mathbf { x } - \hat { \mathbf { x } } | | _ { \infty } = 8 . 5 7 \times 1 0 ^ { - 4 }$ and $| | A \hat { \mathbf { x } } - \mathbf { b } | | _ { \infty } = 2 . 0 6 \times 1 0 ^ { - 4 }$ .

(b) We have $| | \mathbf { x } - \hat { \mathbf { x } } | | _ { \infty } = 0 . 9 0$ and $| | A { \hat { \mathbf { x } } } - \mathbf { b } | | _ { \infty } = 0 . 2 7$ .   
(c) We have $| | \mathbf { x } - \hat { \mathbf { x } } | | _ { \infty } = 0 . 5$ and $| | A \hat { \mathbf { x } } - \mathbf { b } | | _ { \infty } = 0 . 3$ .   
(d) We have $| | \mathbf { x } - { \hat { \mathbf { x } } } | | _ { \infty } = 6 . 5 5 \times 1 0 ^ { - 2 }$ , and $| | A { \hat { \mathbf { x } } } - \mathbf { b } | | _ { \infty } = 0 . 3 2$ .

6. The $l _ { \infty }$ norms are as follows:

(a) 16 (b) 25 (c) 4 \*(d) 12 $^ { * } 7$ . Let $A = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] }$ and $B = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] }$ . Then $\| A B \| _ { \otimes } = 2$ , but $\left\| A \right\| _ { \bigotimes } \cdot \left\| B \right\| _ { \bigotimes } = 1$

8. Showing properties (i) – (iv) of Definition 7.8 is similar to the proof in Exercise 2a. To show property (v),

$$
\begin{array} { r l } & { \| A B \| _ { \mathbb { D } } = \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { j = 1 } ^ { n } \left| \sum _ { k = 1 } ^ { n } a _ { i k } b _ { k j } \right| \leq \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \sum _ { k = 1 } ^ { n } | a _ { i k } | | b _ { k j } | } \\ & { \qquad = \displaystyle \sum _ { i = 1 } ^ { n } \left\{ \sum _ { k = 1 } ^ { n } \left| a _ { i k } \right| \sum _ { j = 1 } ^ { n } | b _ { k j } | \right\} \leq \displaystyle \sum _ { i = 1 } ^ { n } \left( \sum _ { k = 1 } ^ { n } | a _ { i k } | \right) \left( \displaystyle \sum _ { k = 1 } ^ { n } \sum _ { j = 1 } ^ { n } | b _ { k j } | \right) } \\ & { \qquad = \displaystyle \left( \sum _ { i = 1 } ^ { n } \sum _ { k = 1 } ^ { n } | a _ { i k } | \right) \| B \| _ { \mathbb { D } } = \| A \| _ { \mathbb { D } } \| B \| _ { \mathbb { D } } . } \end{array}
$$

The norms of the matrices in Exercise 4 are (4a) 26, (4b) 26, (4c) 10, and (4d) 28.

9. (a) Showing properties ( $i )$ - $( i v )$ of Definition 7.8 is straight-forward. Property (v) is shown as

follows:

$$
\begin{array} { r l r } { \| A B \| _ { F } ^ { 2 } = } & { \left( \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { j = 1 } ^ { n } \left| \displaystyle \sum _ { k = 1 } ^ { n } a _ { i k } b _ { k j } \right| ^ { 2 } \right) } \\ & { \leq } & { \left( \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { j = 1 } ^ { n } \left( \displaystyle \sum _ { k = 1 } ^ { n } \left| a _ { i k } \right| ^ { 2 } \displaystyle \sum _ { k = 1 } ^ { n } | b _ { k j } | ^ { 2 } \right) \right) \quad \mathrm { ~ b y ~ T h e o r e m ~ 7 . 3 ~ } } \\ & { = \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { k = 1 } ^ { n } \left[ | a _ { i k } | ^ { 2 } \left( \displaystyle \sum _ { j = 1 } ^ { n } \displaystyle \sum _ { k = 1 } ^ { n } | b _ { k j } | ^ { 2 } \right) \right] } \\ & { = \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { k = 1 } ^ { n } | a _ { i k } | ^ { 2 } \| B \| _ { F } ^ { 2 } = \| B \| _ { F } ^ { 2 } \displaystyle \sum _ { i = 1 } ^ { n } | a _ { i k } | ^ { 2 } = \| B \| _ { F } ^ { 2 } \| A \| _ { F } ^ { 2 } = \| A \| _ { F } ^ { 2 } \| B \| _ { F } ^ { 2 } . } \end{array}
$$

(b) We have

(4a) $\begin{array} { l } { \| A \| _ { F } = \sqrt { 3 2 6 } } \\ { \| A \| _ { F } = \sqrt { 3 2 6 } } \\ { \| A \| _ { F } = 4 } \\ { \| A \| _ { F } = \sqrt { 1 4 8 } . } \end{array}$   
(4b)   
(4c)   
(4d)

(c) We have

$$
\begin{array} { r l } & { \| A \| _ { 2 } ^ { 2 } = \displaystyle \operatorname* { m a x } _ { \| { \bf x } \| _ { 2 } = 1 } \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } \right) ^ { 2 } \leq \displaystyle \operatorname* { m a x } _ { \| { \bf x } \| _ { 2 } = 1 } \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | | x _ { j } | \right) ^ { 2 } } \\ & { \qquad \leq \displaystyle \operatorname* { m a x } _ { \| { \bf x } \| _ { 2 } = 1 } \sum _ { i = 1 } ^ { n } \left[ \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \left( \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \right] ^ { 2 } = \displaystyle \operatorname* { m a x } _ { \| { \bf x } \| _ { 2 } = 1 } \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) \left( \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { 2 } \right) } \\ & { \qquad = \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } = \| A \| _ { F } ^ { 2 } } \end{array}
$$

Let $j$ be fixed and define

$$
x _ { k } = { \left\{ \begin{array} { l l } { 0 , } & { { \mathrm { i f ~ } } k \neq j } \\ { 1 , } & { { \mathrm { i f ~ } } k = j . } \end{array} \right. }
$$

Then $A \mathbf { x } = ( a _ { 1 j } , a _ { 2 j } , \dotsc , a _ { n j } ) ^ { t }$ , so

$$
\| A \| _ { 2 } ^ { 2 } \geq \| A \mathbf { x } \| _ { 2 } ^ { 2 } \geq \sum _ { i = 1 } ^ { n } | a _ { i j } | ^ { 2 } .
$$

Thus

$$
\| A \| _ { F } ^ { 2 } = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } = \sum _ { j = 1 } ^ { n } \sum _ { i = 1 } ^ { n } | a _ { i j } | ^ { 2 } \leq \sum _ { j = 1 } ^ { n } \| A \| _ { 2 } ^ { 2 } = n \| A \| _ { 2 } ^ { 2 } .
$$

Hence, $\| A \| _ { 2 } \leq \| A \| _ { F } \leq { \sqrt { n } } \| A \| _ { 2 }$ .

10. We have

$$
\| A \mathbf { x } \| _ { 2 } ^ { 2 } = \sum _ { i = 1 } ^ { n } \left| \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } \right| ^ { 2 } \leq \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | | x _ { j } | \right) ^ { 2 } .
$$

Using the Cauchy–Buniakowsky–Schwarz inequality gives

$$
\| A \mathbf { x } \| _ { 2 } ^ { 2 } \leq \sum _ { i = 1 } ^ { n } \left( \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \left( \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \right) ^ { 2 } = \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) \| \mathbf { x } \| _ { 2 } ^ { 2 } = \| A \| _ { F } ^ { 2 } \| \mathbf { x } \| _ { 2 } ^ { 2 } .
$$

Thus, $\| A \mathbf { x } \| _ { 2 } \leq \| A \| _ { F } \| \mathbf { x } \| _ { 2 }$ .

$^ { * } 1 1$ . That $\| \mathbf { x } \| \geq 0$ follows easily. That $\| \mathbf { x } \| = 0$ if and only if $\mathbf x = \mathbf 0$ follows from the definition of positive definite. In addition,

$$
\| { \boldsymbol { \alpha } } \mathbf { x } \| = \left[ \left( \alpha \mathbf { x } ^ { t } \right) { \boldsymbol { S } } ( { \boldsymbol { \alpha } } \mathbf { x } ) \right] ^ { \frac { 1 } { 2 } } = \left[ \alpha ^ { 2 } \mathbf { x } ^ { t } { \boldsymbol { S } } \mathbf { x } \right] ^ { \frac { 1 } { 2 } } = | { \boldsymbol { \alpha } } | \left( \mathbf { x } ^ { t } { \boldsymbol { S } } \mathbf { x } \right) ^ { \frac { 1 } { 2 } } = | { \boldsymbol { \alpha } } | \| \mathbf { x } \| .
$$

From Cholesky’s factorization, let $S = L L ^ { t }$ . Then

$$
\begin{array} { r l } & { \mathbf { x } ^ { t } S \mathbf { y } = \mathbf { x } ^ { t } L L ^ { t } \mathbf { y } = \left( L ^ { t } \mathbf { x } \right) ^ { t } \left( L ^ { t } \mathbf { y } \right) } \\ & { \qquad \leq \left[ \left( L ^ { t } \mathbf { x } \right) ^ { t } \left( L ^ { t } \mathbf { x } \right) \right] ^ { 1 / 2 } \left[ \left( L ^ { t } \mathbf { y } \right) ^ { t } \left( L ^ { t } \mathbf { y } \right) \right] ^ { 1 / 2 } } \\ & { \qquad = \left( \mathbf { x } ^ { t } L L ^ { t } \mathbf { x } \right) ^ { 1 / 2 } \left( \mathbf { y } ^ { t } L L ^ { t } \mathbf { y } \right) ^ { 1 / 2 } = \left( \mathbf { x } ^ { t } S \mathbf { x } \right) ^ { 1 / 2 } \left( \mathbf { y } ^ { t } S \mathbf { y } \right) ^ { 1 / 2 } . } \end{array}
$$

Thus

$$
\begin{array} { r l } & { \| \mathbf { x } + \mathbf { y } \| ^ { 2 } = \left[ \left( \mathbf { x } + \mathbf { y } \right) ^ { t } S \left( \mathbf { x } + \mathbf { y } \right) \right] = \left[ \mathbf { x } ^ { t } S \mathbf { x } + \mathbf { y } ^ { t } S \mathbf { x } + \mathbf { x } ^ { t } S \mathbf { y } + \mathbf { y } ^ { t } S \mathbf { y } \right] } \\ & { \qquad \leq \mathbf { x } ^ { t } S \mathbf { x } + 2 \left( \mathbf { x } ^ { t } S \mathbf { x } \right) ^ { 1 / 2 } \left( \mathbf { y } ^ { t } S \mathbf { y } \right) ^ { 1 / 2 } + \left( \mathbf { y } ^ { t } S \mathbf { y } \right) ^ { 1 / 2 } } \\ & { \qquad = \mathbf { x } ^ { t } S \mathbf { x } + 2 \| \mathbf { x } \| \| \mathbf { y } \| + \mathbf { y } ^ { t } S \mathbf { y } = \left( \| \mathbf { x } \| + \| \mathbf { y } \| \right) ^ { 2 } . } \end{array}
$$

This demonstrates properties $( i ) \mathrm { ~ - ~ } ( i v )$ of Definition 7.1.

12. Since $\| \mathbf { x } \| ^ { \prime } = 0$ implies $\| S \mathbf { x } \| = 0$ , we have $S x = \mathbf { 0 }$ . Since $S$ is nonsingular, $\mathbf x = \mathbf 0$ . Also,

$$
\| \mathbf { x } + \mathbf { y } \| ^ { \prime } = \| S ( \mathbf { x } + \mathbf { y } ) \| = \| S \mathbf { x } + S \mathbf { y } \| \leq \| S \mathbf { x } \| + \| S \mathbf { y } \| = \| \mathbf { x } \| ^ { \prime } + \| \mathbf { y } \| ^ { \prime }
$$

and

$$
\| \alpha \mathbf { x } \| ^ { \prime } = \| S ( \alpha \mathbf { x } ) \| = | \alpha | \ \| S \mathbf { x } \| = | \alpha | \ \| \mathbf { x } \| ^ { \prime } .
$$

$^ *$ 13. It is not difficult to show that $( i )$ holds. If $\| A \| = 0$ , then $\| A \mathbf { x } \| = 0$ for all vectors $\mathbf { x }$ with $\| \mathbf { x } \| = 1$ . Using $\mathbf { x } = ( 1 , 0 , \ldots , 0 ) ^ { t }$ , $\mathbf { x } = ( 0 , 1 , 0 , \ldots , 0 ) ^ { t } , . . .$ , and $\mathbf { x } = ( 0 , \ldots , 0 , 1 ) ^ { t }$ successively implies that each column of $A$ is zero. Thus, $\| A \| = 0$ if and only if $A = 0$ . Moreover,

$$
\begin{array} { r l r } & { } & { \| \alpha A \| = \underset { \| { \bf x } \| = 1 } { \operatorname* { m a x } } \| ( \alpha A { \bf x } ) \| = | \alpha | \underset { \| { \bf x } \| = 1 } { \operatorname* { m a x } } \| A { \bf x } \| = | \alpha | \cdot \| A \| , } \\ & { } & { \| A + B \| = \underset { \| { \bf x } \| = 1 } { \operatorname* { m a x } } \| ( A + B ) { \bf x } \| \le \underset { \| { \bf x } \| = 1 } { \operatorname* { m a x } } ( \| A { \bf x } \| + \| B { \bf x } \| ) , ~ } \end{array}
$$

so

$$
| | A + B | | \leq \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } | | A \mathbf { x } | | + \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } | | B \mathbf { x } | | = \| A \| + \| B \|
$$

and

$$
\| A B \| = \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| ( A B ) \mathbf { x } \| = \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| A ( B \mathbf { x } ) \| .
$$

Thus

$$
| | A B | | \leq \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| A \| \ \| B \mathbf { x } \| = \| A \| \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| B \mathbf { x } \| = \| A \| \ \| B \| .
$$

14. (a) We have

$$
\begin{array} { l } { \displaystyle \sum _ { i = 1 } ^ { \frac { n } { 2 } } \left( \frac { x _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } } - \frac { y _ { i } } { \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } \right) ^ { 2 } = \sum _ { i = 1 } ^ { n } \frac { x _ { i } ^ { 2 } } { \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } } - 2 \sum _ { i = 1 } ^ { n } \frac { x _ { i } y _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } \\ { + \displaystyle \sum _ { i = 1 } ^ { n } \frac { y _ { i } ^ { 2 } } { \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } } } \\ { = 1 - 2 \sum _ { i = 1 } ^ { n } \frac { x _ { i } y _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } + 1 . } \end{array}
$$

Thus

$$
{ \frac { \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } = 1 - { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } \left( { \frac { x _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } - { \frac { y _ { i } } { \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } \right) ^ { 2 } .
$$

(b) Since

$$
{ \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } \left( { \frac { x _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } - { \frac { y _ { i } } { \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } \right) ^ { 2 } \geq 0 ,
$$

we have

$$
\frac { \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } \leq 1
$$

and

$$
\sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \leq \left( \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { i = 1 } ^ { n } y _ { i } ^ { 2 } \right) ^ { 1 / 2 } .
$$

15. Define $\mathbf { z } = ( z _ { 1 } , z _ { 2 } , \ldots , z _ { n } ) ^ { t }$ by $z _ { i } ~ = ~ x _ { i }$ when $y _ { i } \geq 0$ and $z _ { i } = - x _ { i }$ when $y _ { i } < 0$ . Since the Cauchy-Buniakowsky-Schwarz Inequality holds for $\mathbf { z }$ and $\mathbf { y }$ we have

$$
\sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \leq \sum _ { i = 1 } ^ { n } | x _ { i } y _ { i } | = \sum _ { i = 1 } ^ { n } z _ { i } y _ { i } \leq \sum _ { i = 1 } ^ { n } \{ z _ { i } ^ { 2 } \} ^ { 1 / 2 } \sum _ { i = 1 } ^ { n } \{ y _ { i } ^ { 2 } \} ^ { 1 / 2 } = \sum _ { i = 1 } ^ { n } \{ x _ { i } ^ { 2 } \} ^ { 1 / 2 } \sum _ { i = 1 } ^ { n } \{ y _ { i } ^ { 2 } \} ^ { 1 / 2 } .
$$

# Exercise Set 7.2, page 449

1. (a) The eigenvalue $\lambda _ { 1 } = 3$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , - 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = 1$ has the eigenvector $\mathbf { x } _ { 2 } = ( 1 , 1 ) ^ { t }$ . (b) alue has $\textstyle \lambda _ { 1 } = { \frac { 1 + { \sqrt { 5 } } } { 2 } }$ has ctor $\mathbf { x } = \left( 1 , ( 1 + \sqrt { 5 } ) / 2 \right) ^ { t }$ , and the eigenvalue λ2 = 1− √5 $\mathbf { x } = { \left( 1 , { \left( 1 - { \sqrt { 5 } } \right) } / 2 \right) } ^ { t }$ (c) The eigenvalue $\lambda _ { 1 } = \textstyle { \frac { 1 } { 2 } }$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = - \frac { 1 } { 2 }$ has the eigenvector $\mathbf { x } _ { 2 } = ( 1 , - 1 ) ^ { t }$ . $^ { * } ( \mathrm { d } )$ The eigenvalue $\lambda _ { 1 } = 1$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , - 1 , 0 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = \lambda _ { 3 } =$ 3 has the eigenvectors $\mathbf { x } _ { 2 } = ( 1 , 1 , 0 ) ^ { t }$ and $\mathbf { x } _ { 3 } = ( 0 , 0 , 1 ) ^ { t }$ . (e) The eigenvalue $\lambda _ { 1 } = 7$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , 4 , 4 ) ^ { t }$ , the eigenvalue $\lambda _ { 2 } = - 1$ has the eigenvector $\mathbf { x } _ { 2 } = ( 1 , 0 , 0 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = 3$ has the eigenvector $\mathbf { x } _ { 3 } = ( 1 , 2 , 0 ) ^ { t }$ . (f) The eigenvalue $\lambda _ { 1 } = \lambda _ { 2 } = 1$ has the eigenvectors $\mathbf { x } _ { 1 } = ( - 1 , 0 , 1 ) ^ { t }$ and $\mathbf { x } _ { 2 } = ( - 1 , 1 , 0 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = 5$ has the eigenvector $\mathbf { x } = ( 1 , 2 , 1 ) ^ { t }$ .

2. (a) The eigenvalue $\lambda _ { 1 } = 0$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , - 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = - 1$ has the eigenvector $\mathbf { x } _ { 2 } = ( 1 , - 2 ) ^ { t }$ . (b) The eigenvalue $\lambda _ { 1 } ~ = ~ - 1 / 3$ has the eigenvector $\mathbf { x } _ { 1 } ~ = ~ ( - 3 / 2 , 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = - 1 / 2$ has the eigenvector $\mathbf { x } _ { 2 } = ( - 2 , 1 ) ^ { t }$ . (c) The eigenvalue $\lambda _ { 1 } = - 1$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , - 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = 4$ has the eigenvector $\mathbf { x } _ { 2 } = ( 4 , 1 ) ^ { t }$ . (d) The eigenvalue $\lambda _ { 1 } = 3$ has the eigenvector $\mathbf { x } _ { 1 } = ( - 1 , 1 , 2 ) ^ { t }$ , the eigenvalue $\lambda _ { 2 } = 4$ has the eigenvector $\mathbf { x } _ { 2 } = ( 0 , 1 , 2 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = - 2$ has the eigenvector $\mathbf { x } = ( - 3 , 8 , 1 ) ^ { t }$ . (e) The eigenvalue $\lambda _ { 1 } = \lambda _ { 2 } = 1 / 2$ has the eigenvector $\mathbf { x } _ { 1 } = ( 0 , 5 , 1 2 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = - 1 / 3$ has the eigenvector $\mathbf { x } _ { 3 } = ( 0 , 0 , 1 ) ^ { t }$ . (f) The eigenvalue $\lambda _ { 1 } = 2 + 2 i$ has the eigenvector $\mathbf { x } _ { 1 } = ( 0 , - 2 i , 1 ) ^ { t }$ , the eigenvalue $\lambda _ { 2 } =$ $2 - 2 i$ has the eigenvector $\mathbf { x } _ { 2 } = ( 0 , 2 i , 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = 2$ has the eigenvector $\mathbf { x } _ { 3 } = ( 1 , 0 , 0 ) ^ { t }$ .

3. (a) The eigenvalue $\lambda _ { 1 } = 2 + \sqrt { 2 } i$ has the eigenvector $( { \sqrt { 2 } } i , - 1 ) ^ { t }$ and the eigenvalue $\lambda _ { 2 } =$ $2 - \sqrt { 2 } i$ has the eigenvector $( \sqrt { 2 } i , 1 ) ^ { t }$ . \*(b) The eigenvalue $\begin{array} { r } { \lambda _ { 1 } = \frac { 1 } { 2 } ( 3 + \sqrt { 7 } i ) } \end{array}$ has the eigenvector $( 1 - { \sqrt { 7 } } i , 2 ) ^ { t }$ and the eigenvalue $\begin{array} { r } { \lambda _ { 2 } = \frac { 1 } { 2 } ( 3 - \sqrt { 7 } i } \end{array}$ has the eigenvector $( 1 + { \sqrt { 7 } } i , 2 ) ^ { t }$ .

4. (a) The eigenvalue $\lambda _ { 1 } = 1 + { \sqrt { 3 } } i$ has the eigenvector $( 2 \sqrt { 3 } i , - \sqrt { 3 } i , - 3 ) ^ { t }$ and the eigenvalue $\lambda _ { 2 } = 1 - \sqrt { 3 } i$ has the eigenvector $( 2 { \sqrt { 3 } } i , - { \sqrt { 3 } } i , 3 ) ^ { t }$ . (b) The eigenvalue $\lambda _ { 1 } = 1 { + } \sqrt { 2 } i$ has the eigenvector $( 3 , 1 - \sqrt { 2 } i , - 1 - 2 \sqrt { 2 } i ) ^ { t }$ and the eigenvalue $\lambda _ { 2 } = 1 - \sqrt { 2 } i$ has the eigenvector $( 3 , 1 + { \sqrt { 2 } } i , - 1 + 2 { \sqrt { 2 } } i ) ^ { t }$ .

5. The spectral radii for the matrices in Exercise $^ { 1 }$ are;

(a) 3 $( \mathrm { b ) ~ { \frac { 1 + { \sqrt { 5 } } } { 2 } } ~ \quad ( c ) ~ { \frac { 1 } { 2 } } ~ \quad ~ \ast ( \mathrm { d } ) ~ { 3 } }$ (e) 7 (f) 5

6. The spectral radii for the matrices in Exercise 2 are:

(a) 1 (b) $\frac { 1 } { 2 }$ (c) 4 (d) 4 (e) $\frac { 1 } { 2 }$ (f ) 2 √2

$^ { * } 7$ . Only the matrix in $1 ( \mathrm { c } )$ is convergent.

8. Only the matrices in $2 ( \mathrm { b } )$ and $2 ( \mathrm { e } )$ are convergent.

9. The $l _ { 2 }$ norms for the matrices in Exercise 1 are:

(a) 3 (b) 1.618034 (c) 0.5 (d) 3 (e) 8.224257 (f) 5.203527

10. The $l _ { 2 }$ norms for the matrices in Exercise 1 are:

(a) 3.162278 (b) 1.458020 (c) 5.036796 (d) 5.601152 (e) 2.896954 (f) 4.701562

11. Since

$$
A _ { 1 } ^ { k } = [ \frac { 1 } { 2 ^ { k } - 1 } \quad 2 ^ { - k } ] , \quad \mathrm { ~ w e ~ h a v e ~ } \quad \operatorname* { l i m } _ { k  \infty } A _ { 1 } ^ { k } = [ \frac { 1 } { 2 } \quad 0 ] .
$$

Also,

$$
A _ { 2 } ^ { k } = [ { \frac { 2 ^ { - k } } { 2 ^ { k - 1 } } } \quad \quad 0 \atop { 2 ^ { - k } } ] , \quad { \mathrm { ~ s o ~ } } \quad \operatorname* { l i m } _ { k  \infty } A _ { 2 } ^ { k } = [ { \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} } ] .
$$

$^ { * } 1 2$ . Suppose the $\lambda$ is an eigenvalue of $A$ with corresponding eigenvector $\mathbf { x }$ . Then $A \mathbf { x } \ = \ \lambda \mathbf { x }$ , $A ^ { 2 } \mathbf { x } = A ( \lambda \mathbf { x } ) = \lambda A \mathbf { x } = \lambda ^ { 2 } \mathbf { x }$ , and in general, $A ^ { m } { \bf x } = \lambda ^ { m } { \bf x }$ , for any positive integer $m$ . As a consequence,

$$
\mathbf { 0 } = A ^ { m } \mathbf { x } = \lambda ^ { m } \mathbf { x } \quad { \mathrm { w h i c h ~ i m p l i e s ~ t h a t ~ } } \lambda ^ { m } = 0 .
$$

Hence $\lambda = 0$ .

13. Let $A$ be an $n \times n$ matrix. Expanding across the first row gives the characteristic polynomial

$$
p ( \lambda ) = \operatorname * { d e t } ( A - \lambda I ) = ( a _ { 1 1 } - \lambda ) M _ { 1 1 } + \sum _ { j = 2 } ^ { n } ( - 1 ) ^ { j + 1 } a _ { 1 j } M _ { 1 j } .
$$

The determinants $M _ { 1 j }$ are of the form

$$
M _ { 1 j } = \operatorname* { d e t } \left[ \begin{array} { c c c c c c c c } { a _ { 2 1 } } & { a _ { 2 2 } - \lambda } & { \cdots } & { a _ { 2 , j - 1 } } & { a _ { 2 , j + 1 } } & { \cdots } & { a _ { 2 n } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { \cdots } & { a _ { 3 , j - 1 } } & { a _ { 3 , j + 1 } } & { \cdots } & { a _ { 3 n } } \\ { \vdots } & { \vdots } & & & { \vdots } & & & { \vdots } \\ { a _ { j - 1 , 1 } } & { a _ { j - 1 , 2 } } & { \cdots } & { a _ { j - 1 , j - 1 } - \lambda } & { a _ { j - 1 , j + 1 } } & { \cdots } & { a _ { j - 1 , n } } \\ { a _ { j , 1 } } & { a _ { j , 2 } } & { \cdots } & { a _ { j , j - 1 } } & { a _ { j , j + 1 } } & { \cdots } & { a _ { j , n } } \\ { a _ { j + 1 , 1 } } & { a _ { j + 1 , 2 } } & { \cdots } & { a _ { j + 1 , j - 1 } } & { a _ { j + 1 , j + 1 } - \lambda } & { \cdots } & { a _ { j + 1 , n } } \\ { \vdots } & { \vdots } & & & { \vdots } & { \vdots } & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n , j - 1 } } & { a _ { n , j + 1 } } & { \cdots } & { a _ { n n } - \lambda } \\ { a _ { n 1 } } & & & & & & {  } \end{array} \right] ,
$$

for $j = 2 , \dots , n$ . Note that each $M _ { 1 j }$ has $n - 2$ entries of the form $a _ { i i } - \lambda$ . Thus,

$$
p ( \lambda ) = \operatorname* { d e t } ( A - \lambda I ) = ( a _ { 1 1 } - \lambda ) M _ { 1 1 } + \{ { \mathrm { t e r m s ~ o f ~ d e g r e e ~ } } n - 2 { \mathrm { ~ o r ~ l e s s } } \} .
$$

Since

$$
M _ { 1 1 } = \operatorname* { d e t } { \left[ \begin{array} { l l l l l l } { a _ { 2 2 } - \lambda } & { a _ { 2 3 } } & { \cdots } & { \cdots } & { a _ { 2 n } } \\ { a _ { 3 2 } } & { a _ { 3 3 } - \lambda } & { \ddots } & & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & & { \ddots } & { \ddots } & { a _ { n - 1 , n } } \\ { a _ { n 2 } } & { \ldots } & { \ldots } & { a _ { n , n - 1 } } & { a _ { n n } - \lambda } \end{array} \right] }
$$

is of the same form as $\operatorname* { d e t } ( A - \lambda I )$ , the same argument can be repeatedly applied to determine

$$
p ( \lambda ) = ( a _ { 1 1 } - \lambda ) { \left( a _ { 2 2 } - \lambda \right) } \cdot \cdot { \left( a _ { n n } - \lambda \right) } + \{ { \mathrm { t e r m s ~ o f ~ d e g r e e ~ } } n - 2 { \mathrm { ~ o r ~ l e s s ~ i n ~ } } \lambda \} .
$$

Thus, $p ( \lambda )$ is a polynomial of degree $n$

$^ *$ 14. (a) $P ( \lambda ) = ( \lambda _ { 1 } - \lambda ) \ldots ( \lambda _ { n } - \lambda ) = \operatorname* { d e t } ( A - \lambda I ) , { \mathrm { ~ s o ~ } } P ( 0 ) = \lambda _ { 1 } \cdots \lambda _ { n } = \operatorname* { d e t } A .$ (b) A singular if and only if $\operatorname* { d e t } A = 0$ , which is equivalent to at least one of $\lambda _ { i }$ being $0$ .

15. (a) $\operatorname* { d e t } ( A - \lambda I ) = \operatorname* { d e t } ( ( A - \lambda I ) ^ { t } ) = \operatorname* { d e t } ( A ^ { t } - \lambda I )$ (b) If $A \mathbf { x } = \lambda \mathbf { x }$ , then $A ^ { 2 } \mathbf { x } = \lambda A \mathbf { x } = \lambda ^ { 2 } \mathbf { x }$ , and by induction, $A ^ { k } \mathbf { x } = \lambda ^ { k } \mathbf { x }$ . (c) If $A \mathbf { x } = \lambda \mathbf { x }$ and $A ^ { - 1 }$ exists, then $\mathbf { x } = \lambda A ^ { - 1 } \mathbf { x }$ . By Exercise 14 (b), $\lambda \neq 0$ , so $\textstyle { \frac { 1 } { \lambda } } \mathbf { x } = A ^ { - 1 } \mathbf { x }$ . (d) Since $\begin{array} { r } { A ^ { - 1 } \mathbf { x } = \frac { 1 } { \lambda } \mathbf { x } } \end{array}$ , we have $\begin{array} { r } { ( A ^ { - 1 } ) ^ { 2 } \mathbf { x } = \frac { 1 } { \lambda } A ^ { - 1 } \mathbf { x } = \frac { 1 } { \lambda ^ { 2 } } \mathbf { x } } \end{array}$ . Mathematical induction gives

$$
( A ^ { - 1 } ) ^ { k } \mathbf { x } = { \frac { 1 } { \lambda ^ { k } } } \mathbf { x } .
$$

(e) If $A \mathbf { x } = \lambda \mathbf { x }$ , then

$$
q ( A ) \mathbf { x } = q _ { 0 } \mathbf { x } + q _ { 1 } A \mathbf { x } + \ldots + q _ { k } A ^ { k } \mathbf { x } = q _ { 0 } \mathbf { x } + q _ { 1 } \lambda \mathbf { x } + \ldots + q _ { k } \lambda ^ { k } \mathbf { x } = q ( \lambda ) \mathbf { x } .
$$

(f) Let $A - \alpha I$ be nonsingular. Since $A \mathbf { x } = \lambda \mathbf { x }$ ,

$$
( A - \alpha I ) \mathbf { x } = A \mathbf { x } - \alpha I \mathbf { x } = \lambda \mathbf { x } - \alpha \mathbf { x } = ( \lambda - \alpha ) \mathbf { x } .
$$

Thus,

$$
{ \frac { 1 } { \lambda - \alpha } } \mathbf { x } = ( A - \alpha I ) ^ { - 1 } \mathbf { x } .
$$

16. Since $A ^ { t } A = A ^ { 2 }$ and $A \mathbf { x } = \lambda \mathbf { x }$ , we have $A ^ { 2 } \mathbf { x } = \lambda ^ { 2 } \mathbf { x }$ . Thus

$$
\rho \left( A ^ { t } A \right) = \rho \left( A ^ { 2 } \right) = \left[ \rho ( A ) \right] ^ { 2 } \quad { \mathrm { a n d } } \quad \| A \| _ { 2 } = \left[ \rho \left( A ^ { t } A \right) \right] ^ { \frac { 1 } { 2 } } = \rho ( A ) .
$$

17. (a) We have the real eigenvalue $\lambda = 1$ with the eigenvector $\mathbf { x } = ( 6 , 3 , 1 ) ^ { t }$ . (b) Choose any multiple of the vector $( 6 , 3 , 1 ) ^ { t }$ .

18. For

$$
A = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } B = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] } ,
$$

we have $\rho ( A ) = \rho ( B ) = 1$ and $\rho ( A + B ) = 3$ .

19. Let $A \mathbf { x } = \lambda \mathbf { x }$ . Then $\left| \lambda \right| \ \left\| \mathbf { x } \right\| = \left\| A \mathbf { x } \right\| \leq \left\| A \right\| \ \left\| \mathbf { x } \right\|$ , which implies $| \lambda | \leq \| A \|$ . Also, $( 1 / \lambda ) \mathbf { x } =$ $A ^ { - 1 } \mathbf { x }$ so $1 / | \lambda | \leq \| A ^ { - 1 } \|$ and $\| A ^ { - 1 } \| ^ { - 1 } \leq | \lambda |$ .

# Exercise Set 7.3, page 459

1. Two iterations of Jacobi’s method gives the following results.

\*(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 4 2 8 5 7 1 , - 0 . 3 5 7 1 4 2 9 , 0 . 4 2 8 5 7 1 4 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 7 , 0 . 9 1 , 0 . 7 4 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 6 5 , 1 . 6 5 , - 0 . 4 , - 2 . 4 7 5 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 3 2 5 , - 1 . 6 , 1 . 6 , 1 . 6 7 5 , 2 . 4 2 5 ) ^ { t }$

2. Two iterations of Jacobi’s method gives the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 2 5 0 0 0 0 0 , - 1 . 3 3 3 3 3 3 3 , 0 . 2 0 0 0 0 0 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 0 0 0 0 0 0 0 0 , 1 . 0 0 0 0 0 0 0 , - 1 . 3 3 3 3 3 3 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 5 2 0 8 3 3 3 , - 0 . 0 4 1 6 6 6 6 7 , - 0 . 2 1 6 6 6 6 7 , 0 . 4 1 6 6 6$ 667) $t$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 6 8 7 5 , 1 . 1 2 5 , 0 . 6 8 7 5 , 1 . 3 7 5 , 0 . 5 6 2 5 , 1 . 3 7 5 ) ^ { t }$

3. Two iterations of the Gauss-Seidel method give the following results.

\*(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 1 1 1 1 1 1 , - 0 . 2 2 2 2 2 2 2 , 0 . 6 1 9 0 4 7 6 ) ^ { i }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 7 9 , 0 . 9 4 9 5 , 0 . 7 8 9 9 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 5 , 2 . 6 4 , - 0 . 3 3 6 8 7 5 , - 2 . 2 6 7 3 7 5 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 1 8 9 0 6 3 , - 1 . 5 2 1 3 5 4 , 1 . 8 6 2 3 9 6 , 1 . 8 8 2 5 2 6 , 2 . 2 5 5 6 4 5 ) ^ { t }$

4. Two iterations of the Gauss-Seidel method give the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 2 5 0 0 0 0 0 0 0 0 , - 0 . 9 1 6 6 6 6 6 6 6 7 , 0 . 0 6 6 6 6 6 6 6 6 6 6 6 6 ) ^ { \mathrm { {  u } } }$ t (b) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 6 6 6 6 6 6 6 6 6 7 , 1 . 3 3 3 3 3 3 3 3 4 , - 0 . 8 8 8 8 8 8 8 8 9 4 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 6 2 5 , 0 , - 0 . 2 2 5 , 0 . 6 1 6 6 6 6 7 ) ^ { t }$ (d) $\mathbf { x } ^ { ( z ) } = ( 0 . 6 8 7 5 , 1 . 5 4 6 8 7 5 , 0 . 7 9 2 9 6 8 8 , 1 . 7 1 8 7 5 , 0 . 7 2 2 6 5 6 3 , 1 . 8 7 8 9 0 6 ) ^ { t }$

5. Jacobi’s Algorithm gives the following results.

\*(a) ${ \bf x } ^ { ( 9 ) } = ( 0 . 0 3 5 1 0 0 7 9 , - 0 . 2 3 6 6 3 7 5 1 , 0 . 6 5 8 1 2 7 3 2 )$ t (b) $\mathbf { x } ^ { ( 6 ) } = ( 0 . 9 9 5 7 2 5 0 , 0 . 9 5 7 7 7 5 0 , 0 . 7 9 1 4 5 0 0 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 1 ) } = ( - 0 . 7 9 7 1 0 5 8 1 , 2 . 7 9 5 1 7 0 6 7 , - 0 . 2 5 9 3 9 5 7 8 , - 2 . 2 5 1 7 9 2 9 9$ )t (d) $\mathbf { x } ^ { ( 1 2 ) } = ( 0 . 7 8 7 0 8 8 3 , - 1 . 0 0 3 0 3 6 , 1 . 8 6 6 0 4 8 , 1 . 9 1 2 4 4 9 , 1 . 9 8 5 7 0 7 ) ^ { t }$

6. Jacobi’s Algorithm gives the following results.

(a) $\mathbf { x } ^ { ( 1 0 ) } = ( 1 . 4 4 7 6 4 2 3 8 4 , - 0 . 8 3 5 5 6 4 7 8 8 2 , - 0 . 0 4 5 0 2 2 6 6 1 8 ) ^ { t }$   
(b) $\mathbf { x } ^ { ( 2 1 ) } = ( - 1 . 4 5 4 8 5 7 9 5 , 1 . 4 5 4 8 5 7 9 5 , - 0 . 7 2 7 0 4 3 9 6 ) ^ { t }$   
(c) $\mathbf { x } ^ { ( 1 2 ) } = ( - 0 . 7 5 2 0 5 5 9 9 , 0 . 0 4 0 2 7 0 2 8 , - 0 . 2 8 0 2 5 9 5 7 , 0 . 6 9 0 0 8 5 3 6 ) ^ { t }$   
(d) $\mathbf { x } ^ { ( 9 ) } = ( 0 . 3 5 7 0 5 5 6 6 , 1 . 4 2 8 5 2 8 8 3 , 0 . 3 5 7 0 5 5 6 6 , 1 . 5 7 1 4 1 1 1 3 , 0 . 2 8 5 5 2 2 4 6 , 1 . 5 7 1 4 1 1 1 1 3 , 0 . 2 7 8 7 5 0 9 , 0 . 1 7 7 1 4 1 1 1 1 3 )$ 3)t

7. The Gauss-Seidel Algorithm gives the following results.

\*(a) $\mathbf { x } ^ { ( 6 ) } = ( 0 . 0 3 5 3 5 1 0 7 , - 0 . 2 3 6 7 8 8 6 , 0 . 6 5 7 7 5 9 0 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 4 ) } = ( 0 . 9 9 5 7 4 7 5 , 0 . 9 5 7 8 7 3 8 , 0 . 7 9 1 5 7 4 8 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 7 9 6 9 1 4 7 6 , 2 . 7 9 4 6 1 8 2 7 , - 0 . 2 5 9 1 8 0 8 1 , - 2 . 2 5 1 8 3 6 1 6 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 7 ) } = ( 0 . 7 8 6 6 8 2 5 , - 1 . 0 0 2 7 1 9 , 1 . 8 6 6 2 8 3 , 1 . 9 1 2 5 6 2 , 1 . 9 8 9 7 9 0 ) ^ { t }$

8. The Gauss-Seidel Algorithm gives the following results.

(a) $\mathbf { x } ^ { ( 6 ) } = ( 1 . 4 4 7 8 1 6 3 5 0 , - 0 . 8 3 5 8 1 7 3 0 3 7 , - 0 . 0 4 4 7 9 9 6 1 8 6 ) ^ { i }$ $t$   
(b) $\mathbf { x } ^ { ( 8 ) } = ( - 1 . 4 5 4 8 0 4 2 0 , 1 . 4 5 4 4 1 3 1 6 , - 0 . 7 2 7 2 0 6 5 8 ) ^ { t }$   
(c) $\mathbf { \boldsymbol { x } } ^ { ( 8 ) } = ( - 0 . 7 5 3 1 7 6 3 , 0 . 0 4 1 0 1 0 4 9 , - 0 . 2 8 0 7 0 4 7 , 0 . 6 9 1 6 3 0 5 ) ^ { \circ }$ t   
(d) x(6) = (0.35713196, 1.42856598, 0.35714149, 1.57140350, 0.28570175, 1.57142544)t

9. (a)

$$
T _ { j } = \left[ \begin{array} { c c c } { { 0 } } & { { \frac { 1 } { 2 } } } & { { - \frac { 1 } { 2 } } } \\ { { - 1 } } & { { 0 } } & { { - 1 } } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { 0 } } \end{array} \right] \quad \mathrm { a n d } \quad \operatorname* { d e t } ( \lambda I - T _ { j } ) = \lambda ^ { 3 } + \frac { 5 } { 4 } x .
$$

Thus, the eigenvalues of $T _ { j }$ are $0$ and $\pm \frac { \sqrt { 5 } } { 2 } i$ , so $\rho ( T _ { j } ) = \frac { \sqrt { 5 } } { 2 } > 1$ .

(b) x(25) = (−20.827873, 2.0000000, −22.827873)t

(c)

$$
T _ { g } = \left[ \begin{array} { c c c } { { 0 } } & { { { \frac { 1 } { 2 } } } } & { { - { \frac { 1 } { 2 } } } } \\ { { 0 } } & { { { - \frac { 1 } { 2 } } } } & { { - { \frac { 1 } { 2 } } } } \\ { { 0 } } & { { 0 } } & { { - { \frac { 1 } { 2 } } } } \end{array} \right] \quad \mathrm { a n d } \quad \operatorname* { d e t } ( \lambda I - T _ { g } ) = \lambda \left( \lambda + \frac 1 2 \right) ^ { 2 } .
$$

Thus, the eigenvalues of $T _ { g }$ are 0, $- \frac 1 2$ , and $- \frac 1 2$ ; and $\rho ( T _ { g } ) = \frac { 1 } { 2 }$

(d) $\mathbf { x } ^ { ( 2 3 ) } = ( 1 . 0 0 0 0 0 2 3 , 1 . 9 9 9 9 9 7 5 , - 1 . 0 0 0 0 0 0 1 ) ^ { t }$ is within $1 0 ^ { - 5 }$ in the ${ \mathit { l } } _ { \infty }$ norm.

10. (a) $T _ { j } = \left[ { \begin{array} { c c c } { 0 } & { - 2 } & { 2 } \\ { - 1 } & { 0 } & { - 1 } \\ { - 2 } & { - 2 } & { 0 } \end{array} } \right]$ and $\operatorname* { d e t } ( \lambda I - T _ { j } ) = \lambda ^ { 3 }$ , so $\rho ( T _ { j } ) = 0$ . (b) $\mathbf { x } ^ { ( 4 ) } = ( 1 . 0 0 0 0 0 0 0 0 0 , 2 . 0 0 0 0 0 0 0 0 , - 1 . 0 0 0 0 0 0 0 0 ) ^ { t }$ is within $1 0 ^ { - 5 }$ in the $l _ { \infty }$ norm. (c) $T _ { g } = { \frac { \left[ 0 \mathrm { ~ ~ - 2 ~ ~ ~ } 2 \right] } { \left[ 0 \mathrm { ~ ~ ~ } 2 \right] } } \mathrm { ~ ~ a n d ~ } \operatorname* { d e t } ( \lambda I - T _ { g } ) = \lambda ( \lambda - 2 ) ^ { 2 } , \mathrm { ~ s ~ }$ o $\rho ( T _ { g } ) = 2$ .

$$
\mathbf { x } ^ { ( 2 5 ) } = \left( 1 . 3 0 \times 1 0 ^ { 9 } , - 1 . 3 2 5 \times 1 0 ^ { 9 } , 3 . 3 5 5 \times 1 0 ^ { 7 } \right) ^ { t }
$$

11. (a) $A$ is not strictly diagonally dominant.

(b)

$$
T _ { g } = \left[ { 0 \atop 0 } \ { 0 \atop 0 } \ { 0 . 7 5 } \right] \quad { \mathrm { a n d } } \quad \rho ( T _ { g } ) = 0 . 6 2 5 .
$$

Since $T _ { g }$ is convergent, the Gauss-Seidel method will converge.

(c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , $\mathbf { x } ^ { ( 1 3 ) } = ( 0 . 8 9 7 5 1 3 1 0 , - 0 . 8 0 1 8 6 5 1 8 , 0 . 7 0 1 5 5 4 3 1 ) ^ { t }$

(d) $\rho ( T _ { g } ) = 1 . 3 7 5$ . Since $T _ { g }$ is not convergent, the Gauss-Seidel method will not converge

12. (a) $A$ is not strictly diagonally dominant.

(b) We have

$$
T _ { j } = \left[ \begin{array} { c c c } { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 . 5 } } & { { 0 } } & { { 0 . 2 5 } } \\ { { - 1 } } & { { 0 . 5 } } & { { 0 } } \end{array} \right] \quad \mathrm { a n d } \quad \rho ( T _ { j } ) = 0 . 9 7 2 1 0 5 2 1 .
$$

Since $T _ { j }$ is convergent, the Jacobi method will converge.

(c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , $\mathbf { x } ^ { ( 1 8 7 ) } = ( 0 . 9 0 2 2 2 6 5 5 , - 0 . 7 9 5 9 5 2 4 2 , 0 . 6 9 2 8 1 3 1 6 ) ^ { t }$

(d) $\rho ( T _ { j } ) = 1 . 3 9 3 3 1 7 7 9 3 7 1$ . Since $T _ { j }$ is not convergent, the Jacobi method will not converge.

13. (a) Subtract ${ \bf x } = T { \bf x } + { \bf c }$ from $\mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c }$ to obtain $\mathbf { x } ^ { ( k ) } - \mathbf { x } = T ( \mathbf { x } ^ { ( k - 1 ) } - \mathbf { x } )$ . Thus,

$$
\| \mathbf { x } ^ { ( k ) } - \mathbf { x } \| \leq \| T \| \| \mathbf { x } ^ { ( k - 1 ) } - \mathbf { x } \| .
$$

Inductively, we have

$$
\| \mathbf { x } ^ { ( k ) } - \mathbf { x } \| \leq \| T \| ^ { k } \| \mathbf { x } ^ { ( 0 ) } - \mathbf { x } \| .
$$

The remainder of the proof is similar to the proof of Corollary 2.5.

(b) The last column has no entry when $| | T | | _ { \infty } = 1$ .

<table><tr><td></td><td>=x(2）- x|∞</td><td>|T|o</td><td>|T12 T|²x(0）- x| |/x(1）-x(|∞ 1-|IT|</td></tr><tr><td>1 (a)</td><td>0.22932</td><td>0.857143</td><td>0.48335</td></tr><tr><td>1 (b)</td><td>0.051579</td><td>0.3 0.089621</td><td>2.9388 0.11571</td></tr><tr><td>1 (c)</td><td>1.1453</td><td>0.9</td><td>2.2642 20.25</td></tr><tr><td>1 (d)</td><td>0.27511</td><td>1</td><td>0.75342</td></tr><tr><td>1(e)</td><td>0.59743</td><td>1</td><td>1.9897</td></tr><tr><td>1 (f)</td><td>0.875</td><td>0.75</td><td>1.125</td></tr></table>

\*14. The matrix $T _ { j } = \left( t _ { i k } \right)$ has entries given by

Since $A$ is strictly diagonally dominant, $\| T _ { j } \| _ { \infty } = \underset { 1 \leq i \leq n } { \operatorname* { m a x } } \sum _ { \stackrel { k = 1 } { k \neq i } } ^ { n } \left| \frac { a _ { i k } } { a _ { i i } } \right| < 1$ .

<table><tr><td></td><td>Jacobi 33 iterations</td><td>Gauss-Seidel 8 iterations</td><td></td><td>Jacobi 33 iterations</td><td>Gauss-Seidel 8 iterations</td></tr><tr><td>X1</td><td>1.53873501</td><td>1.53873270</td><td>X41</td><td>0.02185033</td><td>0.02184781</td></tr><tr><td>x2</td><td>0.73142167</td><td>0.73141966</td><td>X42</td><td>0.02133203</td><td>0.02132965</td></tr><tr><td>x3</td><td>0.10797136</td><td>0.10796931</td><td>X43</td><td>0.02083782</td><td>0.02083545</td></tr><tr><td>X4</td><td>0.17328530</td><td>0.17328340</td><td>X44</td><td>0.02036585</td><td>0.02036360</td></tr><tr><td>X5</td><td>0.04055865</td><td>0.04055595</td><td>X45</td><td>0.01991483</td><td>0.01991261</td></tr><tr><td>X6</td><td>0.08525019</td><td>0.08524787</td><td>X46</td><td>0.01948325</td><td>0.01948113</td></tr><tr><td>X7</td><td>0.16645040</td><td>0.16644711</td><td>X47</td><td>0.01907002</td><td>0.01906793</td></tr><tr><td>x8</td><td>0.12198156</td><td>0.12197878</td><td>X48</td><td>0.01867387</td><td>0.01867187</td></tr><tr><td>x9</td><td>0.10125265</td><td>0.10124911</td><td>X49</td><td>0.01829386</td><td>0.01829190</td></tr><tr><td>X10</td><td>0.09045966</td><td>0.09045662</td><td>x50</td><td>0.71792896</td><td>0.01792707</td></tr><tr><td>X11</td><td>0.07203172</td><td>0.07202785</td><td>X51</td><td>0.01757833</td><td>0.01757648</td></tr><tr><td>X12</td><td>0.07026597</td><td>0.07026266</td><td>X52</td><td>0.01724113</td><td>0.01723933</td></tr><tr><td>X13</td><td>0.06875835</td><td>0.06875421</td><td>X53</td><td>0.01691660</td><td>0.01691487</td></tr><tr><td>X14</td><td>0.06324659</td><td>0.06324307</td><td>X54</td><td>0.01660406</td><td>0.01660237</td></tr><tr><td>X15</td><td>0.05971510</td><td>0.05971083</td><td>X55</td><td>0.01630279</td><td>0.01630127</td></tr><tr><td>X16</td><td>0.05571199</td><td>0.05570834</td><td>X56</td><td>0.01601230</td><td>0.01601082</td></tr><tr><td>X17</td><td>0.05187851</td><td>0.05187416</td><td>X57</td><td>0.01573198</td><td>0.01573087</td></tr><tr><td>X18</td><td>0.04924911</td><td>0.04924537</td><td>X58</td><td>0.01546129</td><td>0.01546020</td></tr><tr><td>X19</td><td>0.04678213</td><td>0.04677776</td><td>X59</td><td>0.01519990</td><td>0.01519909</td></tr><tr><td>X20</td><td>0.04448679</td><td>0.04448303</td><td>X60</td><td>0.01494704</td><td>0.01494626</td></tr><tr><td>X21</td><td>0.04246924</td><td>0.04246493</td><td>X61</td><td>0.01470181</td><td>0.01470085</td></tr><tr><td>X22</td><td>0.04053818</td><td>0.04053444</td><td>X62</td><td>0.01446510</td><td>0.01446417</td></tr><tr><td>X23</td><td>0.03877273</td><td>0.03876852</td><td>X63</td><td>0.01423556</td><td>0.01423437</td></tr><tr><td>X24</td><td>0.03718190</td><td>0.03717822</td><td>X64</td><td>0.01401350</td><td>0.01401233</td></tr><tr><td>X25</td><td>0.03570858</td><td>0.03570451</td><td>X65</td><td>0.01380328</td><td>0.01380234</td></tr><tr><td>X26</td><td>0.03435107</td><td>0.03434748</td><td>X66</td><td>0.01359448</td><td>0.01359356</td></tr><tr><td>X27</td><td>0.03309542</td><td>0.03309152</td><td>X67</td><td>0.01338495</td><td>0.01338434</td></tr><tr><td>X28</td><td>0.03192212</td><td>0.03191866</td><td>X68</td><td>0.01318840</td><td>0.01318780</td></tr><tr><td>X29</td><td>0.03083007</td><td>0.03082637</td><td>X69</td><td>0.01297174</td><td>0.01297109</td></tr><tr><td>X30</td><td>0.02980997</td><td>0.02980666</td><td>X70</td><td>0.01278663</td><td>0.01278598</td></tr><tr><td>X31</td><td>0.02885510</td><td>0.02885160</td><td>X71</td><td>0.01270328</td><td>0.01270263</td></tr><tr><td>x32</td><td>0.02795937</td><td>0.02795621</td><td>72</td><td>0.01252719</td><td>0.01252656</td></tr><tr><td>X33</td><td>0.02711787</td><td>0.02711458</td><td>X73</td><td>0.01237700</td><td>0.01237656</td></tr><tr><td>x34</td><td>0.02632478</td><td>0.02632179</td><td>X74</td><td>0.01221009</td><td>0.01220965</td></tr><tr><td>X35</td><td>0.02557705</td><td>0.02557397</td><td>75</td><td>0.01129043</td><td>0.01129009</td></tr><tr><td>X36</td><td>0.02487017</td><td>0.02486733</td><td>X76</td><td>0.01114138</td><td>0.01114104</td></tr><tr><td>X37</td><td>0.02420147</td><td>0.02419858</td><td>77</td><td>0.01217337</td><td>0.01217312</td></tr><tr><td>x38</td><td>0.02356750</td><td>0.02356482</td><td>X78</td><td>0.01201771</td><td>0.01201746</td></tr><tr><td>X39</td><td>0.02296603</td><td>0.02296333</td><td>X79</td><td>0.01542910</td><td>0.01542896</td></tr><tr><td>X40</td><td>0.02239424</td><td>0.02239171</td><td>X80</td><td>0.01523810</td><td>0.01523796</td></tr></table>

16. (a) We have $P _ { 0 } = 1$ , so the equation $P _ { 1 } = { \textstyle \frac { 1 } { 2 } } P _ { 0 } + { \textstyle \frac { 1 } { 2 } } P _ { 2 }$ gives $\begin{array} { r } { P _ { 1 } - \frac { 1 } { 2 } P _ { 2 } = \frac { 1 } { 2 } } \end{array}$ . Since $P _ { i } =$ $\textstyle { \frac { 1 } { 2 } } P _ { i - 1 } + { \frac { 1 } { 2 } } P _ { i + 1 }$ , we have $\begin{array} { r } { - \frac { 1 } { 2 } P _ { i - 1 } + P _ { i } - \frac { 1 } { 2 } \mathbf { \bar { \mathit { P } } } _ { i + 1 } = \bar { \mathbf { \mathit { 0 } } } } \end{array}$ , for $i = 2 , \ldots , n - 2$ 2 . Finally, since $P _ { n } = 0$ 2 and $P _ { n - 1 } = { \textstyle { \frac { 1 } { 2 } } } P _ { n - 2 } + { \textstyle { \frac { 1 } { 2 } } } P _ { n }$ 2, we have $- { \textstyle \frac { 1 } { 2 } } P _ { n - 2 } + P _ { n - 1 } = 0$ . This gives the linear system.

(b) The solution vector is $( 0 . 8 9 9 9 6 4 3 1 , 0 . 7 9 9 9 3 5 4 4 , 0 . 6 9 9 9 1 5 4 9 , 0 . 5 9 9 9 0 5 5 2 , 0 . 4 9 9 9 0 5 5 2$ , 0.39991454, 0.29993086, 0.19995223, 0.09997611)t, using 86 iterations with a tolerance $1 . 0 0 \times 1 0 ^ { - 5 }$ in $l _ { \infty }$ with the Gauss-Seidel method.

The solution vector $\mathrm { 1 S \ ( 0 . 9 6 \dot { 2 } S \times 9 / ( 4 , 0 . 9 2 5 9 9 5 ) 2 7 , 0 . 8 8 9 2 \dot { 2 } ) 0 4 2 , 0 . 8 5 2 8 9 8 9 } / , \ 0 . 8 1 6 \times 5 4 2 7 0 9 2$ , $) , \langle | { \mathrm { S } } { \mathrm { 1 } } 3 5 0 0 \rangle / 2 , \{ \mathrm { 0 } . { \cdot } { \mathrm { ( 4 6 2 8 3 4 0 , 0 ) } } { \mathrm { , ~ 0 } } { \mathrm { . ~ ( 1 . 8 4 / 9 8 , 0 . 6 / 8 0 5 9 / 9 , 0 . 6 2 4 9 / 4 2 1 , 0 . 6 1 2 0 4 2 0 0 , 0 . 5 8 1 1 0 9 5 ) } }$ , $9 . 9 5 0 9 4 1 8 0 1 , 0 . 5 3 2 5 0 9 0 9 4 0 1 1 , 0 . 4 9 2 1 0 9 9 9 1 0 0 , 0 . 4 0 9 3 ( 2 9 9 4 9 , 0 . 4 3 0 0 \ ( \mathrm { ~ 1 ~ } 0 . 9 ) , 0 . 4 1 0 0 \ ( 9 4 4 , 0 . 3 8 5 0 2 ( 0 . 1 0 ) )$ , 0.36156768, 0.33850391, 0.31643400, 0.29535198, 0.27524791, 0.25610805, 0.23791514, 0.22064859, 0.20428475, 0.18879715, 0.17415669, 0.16033195, 0.14728936, 0.13499341, 0.12340690, 0.11249111, 0.10220596, 0.09251023, 0.08336165, 0.07471709, 0.06653267, 0.05876386, 0.05136562, 0.04429243, 0.03749843, 0.03093747, 0.02456315, 0.01832893, 0.01218814, 0.00609407)t, using 231 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 3 }$ in ${ \mathit { l } } _ { \infty }$ with the Gauss-Seidel method.

The solution vector is $( 0 . 9 6 3 0 5 8 5 4 , 0 . 9 2 6 2 7 4 9 4 , 0 . 8 8 9 7 2 6 1 3 , 0 . 8 5 3 4 8 7 0 6 , 0 . 8 1 7 6 3 0 ^ { \circ } 2 6 0 9 8 8 9 8 8 0 ^ { \circ } )$ , 0.78222543, 0.74733909, 0.71303418, $\mathrm { 0 . 6 \mathord { \left/ { \vphantom { 0 . 6 \mathrm { 0 . 6 9 3 6 9 8 3 } } } \right. \kern - delimiterspace } 0 . 6 \mathrm { 0 . 6 4 6 4 0 1 0 1 , 0 . 6 1 4 1 / \mathrm { 8 4 1 } } , 0 . \mathrm { . 0 8 2 / 4 8 1 6 } }$ , $0 . 3 9 3 2 1 3 1 ( 8 , 0 . 3 2 2 4 2 0 0 1 2 , 0 . 4 9 3 9 0 1 2 8 ( , 0 . 4 0 5 ) ( 1 9 9 3 0 ) , 0 . 4 3 8 ( 0 8 3 2 , 0 . 4 1 2 ( 9 1 0 1 , 0 . 3 8 ( 8 0 8 0 8 )$ , $0 . 3 0 0 3 8 1 1 9 0 , 0 . 3 4 0 8 1 1 4 , 0 . 3 1 8 8 8 1 0 4 2 , 0 . 2 9 9 ( \mathrm { \it ~ ( 9 4 0 8 ) . 0 2 ~ ( 1 ~ 0 . 0 6 8 ) . 0 2 0 8 ( \mathrm { \it ~ 1 3 3 3 8 , 0 . 2 4 0 0 2 0 1 4 } ) }$ , 0.22346997, 0.20724328, 0.19191807, 0.17747025, 0.16387393, 0.15110162, 0.13912457, 0.12791297, 0.11743622, 0.10766312, 0.09856216, 0.09010163, 0.08224988, 0.07497547, 0.06824731, 0.06203481, 0.05630801, 0.05103770, 0.04619548, 0.04175387, 0.03768638, 0.03396754, 0.03057293, 0.02747926, 0.02466435, 0.02210715, 0.01978772, 0.01768725, $0 . 0 1 5 7 8 8 0 6 , 0 . 0 1 4 0 7 3 5 0 , 0 . 0 1 2 5 2 8 0 3 , 0 . 0 1 1 1 3 7 1 0 , 0 . 0 0 9 8 8 ^ { \prime } 1 8 , 0 . 0 0 8 7 6 5 6 8 , 0 . 0 0 7 7 6 0 9 9 2 , 0 . 0 0 9 8 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime }$ $0 . 0 0 6 8 6 2 1 0 , 0 . 0 0 6 0 5 9 2 6 , 0 . 0 0 5 3 4 3 2 1 , 0 . 0 0 4 7 0 5 5 2 , 0 . 0 0 4 1 3 8 4 4 , 0 . 0 0 3 6 3 4 9 0 , 0 . 0 0 3 1 8 8 4 2 ,$ $0 . 1 0 0 2 d ( 9 3 \bot \mathrm { Z } , \mathrm  0 . 1 0 0 2 4 4 3 6 3 , 0 . 0 0 2 1 . 3 9 0 9 , 0 . 0 0 1 8 0 3 6 0 8 , 0 . 0 0 1 6 0 2 3 0 2 , 0 . 0 0 1 4 1 3 1 , 0 . 0 0 1 2 2 8 3 1 , 0 . 0 0 0 2 6 2 2 6 3 6 0 8 , 0 . 0 0 0 2 2 6 1 2 8 0 2 , 0 . 0 0 0 2 2 6 2 8 2 8 2 8 0 2 8 , 0 . 0 0 0 2 2 2 6 2 8 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0$ , $9 . 0 0 1 1 0 6 6 3 5 0 , 0 . 0 0 0 9 2 4 4 / \ , 0 . 0 0 0 8 0 0 4 / \ , 0 . 0 0 0 0 6 9 2 2 1 , 0 . 0 0 0 0 3 9 7 8 1 , 0 . 0 0 0 0 3 1 3 6 0 0 , 0 . 0 0 0 0 4 4 4 0 9$ , $0 . 0 0 0 3 8 \mathrm { { L } 9 7 } , 0 . 0 0 0 0 3 3 2 8 0 6 6 , 0 . 0 0 0 0 0 2 8 \mathrm { { L } 3 2 } , 0 . 0 0 0 0 2 4 0 8 2 , 0 . 0 0 0 0 2 0 5 7 5 , 0 . 0 0 0 1 7 5 3 9 , 0 . 0 0 0 1 4 9 0 9 .$ 0.00012629, 0.00010648, 0.00008920, 0.00007405, 0.00006067, 0.00004871, 0.00003787, $0 . 0 0 0 0 2 7 8 6 , 0 . 0 0 0 0 1 8 3 9 , 0 . 0 0 0 0 0 9 1 9 ) ^ { u }$ , using 233 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 3 }$ in $l _ { \infty }$ norm with the Gauss-Seidel method.

(c) The equations are $P _ { i } = \alpha P _ { i - 1 } + ( 1 - \alpha ) P _ { i + 1 }$ , for $i = 1 , 2 , \ldots , n - 1$ , and the linear system becomes

$$
{ \left[ \begin{array} { l l l l l } { 1 } & { \alpha - 1 } & { 0 } & { \cdots } & { 0 } \\ { - \alpha } & { 1 } & { \alpha - 1 } & { \ddots } & { \vdots } \\ { 0 } & { - \alpha } & { \ddots } & { \ddots } & { 0 } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \alpha - 1 } \\ { 0 } & { \cdots } & { 0 } & { - \alpha } & { 1 } \end{array} \right] } \quad { \left[ \begin{array} { l } { P _ { 1 } } \\ { P _ { 2 } } \\ { \vdots } \\ { \vdots } \\ { P _ { n - 1 } } \end{array} \right] } = { \left[ \begin{array} { l } { \alpha } \\ { 0 } \\ { \vdots } \\ { \vdots } \\ { 0 } \end{array} \right] }
$$

(d) The solution vector is (0.49947985, 0.24922901, 0.12411164, 0.06155895, 0.03028662, 0.01465286, 0.00683728, 0.00293009, 0.00097670)t, using 35 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 5 }$ in ${ \mathit { l } } _ { \infty }$ norm with the Gauss-Seidel method. The solution vector is $( 4 . 9 9 9 5 3 2 8 \times 1 0 ^ { - 1 } , 2 . 4 9 9 3 9 6 7 \times 1 0 ^ { - 1 } , 1 . 2 4 9 4$ $1 . 2 4 9 4 2 1 5 \times 1 0 ^ { - 1 }$ , $6 . 2 4 5 1 1 7 2 \times 1 0 ^ { - 2 } .$ $, 3 . 1 2 1 1 7 1 9 \times 1 0 ^ { - 2 } , 1 . 5 5 9 6 4 4 8 \times 1 0 ^ { - 2 } , 7 . 7 9 1 9 7 5 7 \times 1 0 ^ { - 3 } , 3 . 8 9 1 9 1 9 3 \times 1 0 ^ { - 3 } , 2 . 7 9 1 4 9 5 7 \times 1 0 ^ { - 2 }$

$1 . 9 4 3 3 5 5 6 \times 1 0 ^ { - 3 } , 9 . 7 0 0 3 6 7 3 \times 1 0 ^ { - 4 } , 4 . 8 3 9 9 8 7 6 \times 1 0 ^ { - 4 } , 2 . 4 1 3 7 4 1 5 \times 1 0 ^ { - 4 } , 1 . 2 0 3 0 8 3 2 \times 1 0 ^ { - 4 } ,$ $5 . 9 9 2 7 3 2 1 \times 1 0 ^ { - 5 } , 2 . 9 8 2 9 2 6 0 \times 1 0 ^ { - 5 } , 1 . 4 8 3 5 8 0 3 \times 1 0 ^ { - 5 } , 7 . 3 7 2 1 1 4 0 \times 1 0 ^ { - 6 } , 3 . 6 5 9 7 0 3 7 \times 1 0 ^ { - 6 } . 9 9 9 6 0 0 0 0 0 0 0 0 0 0 0 ,$ $1 . 8 1 4 8 1 6 7 \times 1 0 ^ { - 6 }$ $\mathrm { , 8 . 9 8 9 0 2 2 9 \times 1 0 ^ { - 7 } , 4 . 4 4 6 7 7 5 2 \times 1 0 ^ { - 7 } , }$ $7 7 5 2 \times 1 0 ^ { - 7 } , 2 . 1 9 6 8 0 4 8 \times 1 0 ^ { - 7 } , 1 . 0 8 3 7 0 9 3 \times 1 0 ^ { - \cdot }$ 7, $3 7 9 1 6 5 \times 1 0 ^ { - \circ } , 2 . 6 2 5 0 1 7 7 \times 1 0 ^ { - \circ } , 1 . 2 8 8 7 2 3 3 2 \times 1 0 ^ { - \circ } , 6 . 3 1 5 6 9 5 3 \times 1 0 ^ { - \circ } , 3 . 0 8 9 4 8 2 9 \times 1 0 ^ { - \circ } ,$ 1.5084 $2 7 7 \times 1 0 ^ { - 9 } , 7 . 3 5 0 3 8 7 6 \times 1 0 ^ { - 1 0 } , 3 . 5 7 4 5 2 3 2 \times 1 0 ^ { - 1 0 }$ $7 6 \times 1 0 ^ { - 1 0 } , 3 . 5 7 4 5 2 3 2 \times 1 0 ^ { - 1 0 } , 1 . 7 3 4 7 0 3 5 \times 1 0 ^ { - 1 0 } ,$ $\mathrm { 3 2 } \times 1 0 ^ { - 1 0 } , \mathrm { 1 . 7 3 4 7 0 3 5 } \times 1 0 ^ { - 1 0 } , \mathrm { 8 . 4 0 0 6 1 0 5 } \times 1 0 ^ { - 1 1 } ,$ $4 . 0 5 9 3 4 7 0 { \times } 1 0 ^ { - 1 1 }$ $4 7 0 \times 1 0 ^ { - 1 1 } , 1 . 9 5 7 2 4 1 8 \times 1 0 ^ { - 1 1 } , 9 . 4 1 5 8 7 9 8 \times 1 0 ^ { - 1 1 }$ $1 1 8 \times 1 0 ^ { - 1 1 } , 9 . 4 1 5 8 7 9 8 \times 1 0 ^ { - 1 2 } , 4 . 5 1 9 5 1 9 7 \times 1 0 ^ { - 1 2 }$ $9 8 \times 1 0 ^ { - 1 2 } , 4 . 5 1 9 5 1 9 7 \times 1 0 ^ { - 1 2 } , 2 . 1 6 4 3 4 6 5 \times 1 0 ^ { - 1 2 }$ , $1 . 0 3 4 0 7 7 0 \times 1 0 ^ { - 1 2 } , 4 . 9 2 8 9 7 5 7 \times 1 0 ^ { - 1 3 } , 2 . 3 4 3 7 6 7$ $7 { \times } 1 0 ^ { - 1 3 } , 2 . 3 4 3 7 6 7 7 { \times } 1 0 ^ { - 1 3 } , 1 . 1 1 1 6 6 4 4 { \times } 1 0 ^ { - 1 3 } ,$ 5.2577488 10−14, $2 . 4 7 7 6 5 0 9 \times 1 0 ^ { - 1 4 } , 1 . 1 6 0 8 1 9 0 \times 1 0 ^ { - 1 4 } , 5 . 3 7 6 7 4 5 8 \times 1 0 ^ { - 1 5 } , 2 . 4 2 4 9 9 7 7 \times 1 0 ^ { - 1 5 } , 1 . 0 1 9 2 4 8 9 \times 1 0 ^ { - 1 5 } .$ $3 . 3 9 7 4 9 6 5 \times 1 0 ^ { - 1 6 } ) ^ { t }$ , using 40 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 5 }$ in $l _ { \infty }$ norm with the Gauss-Seidel method. The solution $\mathrm { \ v e c t o r ~ i s ~ ( 4 . 9 9 9 5 3 2 8 \times 1 0 ^ { - 1 } , 2 . 4 9 9 3 9 6 7 \times 1 0 ^ { - 1 } , 1 . 2 4 9 4 2 1 5 \times 1 0 ^ { - 1 } , }$ $6 . 2 4 5 1 1 7 2 \times 1 0 ^ { - 2 } , 3 . 1 2 1 1 7 1 9 \times 1 0 ^ { - 2 } , 1 . 5 5 9 6 4 4 8 \times 1 0 ^ { - 2 } , 7 . 7 9 1 9 7 5 7 \times 1 0 ^ { - 3 } , 3 . 8 9 1 9 1 9 3 9 8 8 8 7 8 8 7 8 7 8 7 8 7 8 8 7 8$ 3, $1 . 9 4 3 3 5 5 6 \times 1 0 ^ { - 3 }$ $, 9 . 7 0 0 3 6 7 3 \times 1 0 ^ { - 4 } , 4 . 8 3 9 9 8 7 6 \times 1 0 ^ { - 4 } , 2 . 4 1 3 7 4 1 5 \times 1 0 ^ { - 4 } , 1 . 2 0 3 0 8 3 2 \times 1 0 ^ { - 4 }$ , $5 . 9 9 2 7 3 2 1 \times 1 0 ^ { - 5 }$ $\times 1 0 ~ ^ { \circ } , 2 . 9 8 \angle 9 2 0 0 \times 1 0 ~ ^ { \circ } , 1 . 4 8 . 3 0 8 0 3 \times 1 0 ~ ^ { \circ } , ( . 3 ( \bar { \cal Z } 1 1 4 0 \times 1 0 ~ ^ { \circ } , 3 . 0 3 9 ( 0 3 i \times 1 0 ~ ^ { \circ }$ , $1 . 8 1 4 8 1 6 7 \times 1 0 ^ { - 6 }$ , $8 . 9 8 9 0 2 2 9 \times 1 0 ^ { - 7 } , 4 . 4 4 6 7 7 5 2 \times 1 0 ^ { - 7 } , 2 . 1 9 6 8 0 4 8 \times$ $7 7 5 2 \times 1 0 ^ { - 7 } , 2 . 1 9 6 8 0 4 8 \times 1 0 ^ { - 7 } , 1 . 0 8 3 7 0 9 3 \times 1 0 ^ { - 1 }$ 7, $5 . 3 3 7 9 1 6 5 \times 1 0 ^ { - 8 }$ , $2 . 6 2 5 0 1 7 7 \times 1 0 ^ { - 8 } , 1 . 2 8 8 7 2 3 2 \times 1 0 ^ { - 8 } , 6 . 3 1 5 6 9 5 3 \times$ $7 2 3 2 \times 1 0 ^ { - 8 } , 6 . 3 1 5 6 9 5 3 \times 1 0 ^ { - 9 } , 3 . 0 8 9 4 8 2 9 \times 1 0 ^ { - 9 }$ 9, $\in \Omega \odot 4 . 9 7 7 \ddots 1 \Omega - 9 ^ { ' } 7 \phantom { ' } \supset \Omega \odot 9 . 9 7 \phantom { ' } \rho \sim \cdot 1 \ : \Omega - 1 0 ^ { - 1 } \phantom { ' } 0 \succeq \succeq 7 . 4 \succeq \sigma \odot 9 . \hdots 1 \Omega - 1 0 ^ { - 1 } 1 \phantom { ' } 1 \quad \tau \circ 4 . 7 \ 0 \Omega \succeq \zeta \hdots 1 \Omega - 1 0 ^ { - 1 } \phantom { ' } 0 \phantom { ' } \odot 4 . 0 0 \sigma + \Omega \in \Omega \times \hdots 1 \Omega - 1 1$ $1 . 5 0 8 4 2 7 7 \times 1 0 ^ { - 9 }$ $7 7 \times 1 0 ^ { - 9 } , 7 . 3 5 0 3 8 7 6 \times 1 0 ^ { - 1 0 } , 3 . 5 7 4 5 2 3 2 \times 1 0 ^ { - 1 0 }$ $7 6 \times 1 0 ^ { - 1 0 } , 3 . 5 7 4 5 2 3 2 \times 1 0 ^ { - 1 0 } , 1 . 7 3 4 7 0 3 5 \times 1 0 ^ { - 1 0 } ,$ $\mathrm { 5 2 } \times 1 0 ^ { - 1 0 } , \mathrm { 1 . 7 3 4 7 0 3 5 } \times \mathrm { 1 0 ^ { - 1 0 } , 8 . 4 0 0 6 1 0 6 } \times \mathrm { 1 0 ^ { - 1 1 } } .$ $4 . 0 5 9 3 4 7 2 \times 1 0 ^ { - 1 1 } , 1 . 9 5 7 2 4 2 1 \times 1 0 ^ { - 1 1 } , 9 . 4 1 5 8 8 4 8 \times 1 0 ^ { - 1 2 } , 4 . 5 1 9 5 2 7 5 \times 1 0 ^ { - 1 2 } , 2 . 1 9 5 2 6 2 1 \times 1 0 ^ { - 1 2 } , 2 . 2 7 6 2 6 2 1 \times 1 0 ^ { - 1 2 } , 2 . 2 7 6 2 2 6 2 1$ $, 4 . 5 1 9 5 2 7 5 \times 1 0 ^ { - 1 2 } , 2 . 1 6 4 3 5 8 1 \times 1 0 ^ { - 1 2 }$ , $0 3 4 0 9 4 0 \times 1 0 ^ { - 1 2 } , 4 . 9 2 9 2 1 6 7 \times 1 0 ^ { - 1 9 } , 2 . 3 4 4 1 0 2 5 \times 1 0 ^ { - 1 9 } , 1 . 1 1 2 1 1 8 9 \times 1 0 ^ { - 1 9 } , 5 . 2 6 3 7 8 7 7 \times 1 0 ^ { - 1 9 } , 9 . 9 9 9 8 8 8 8 , 1 . 2 7 6 7 8 7 8$ 2.4855 $1 1 6 \times 1 0 ^ { - 1 4 } , 1 . 1 7 0 8 5 3 2 \times 1 0 ^ { - 1 4 } , 5 . 5 0 2 4 7 8 9 \times 1 0 ^ { - 1 }$ $2 \times 1 0 ^ { - 1 4 } , 5 . 5 0 2 4 7 8 9 \times 1 0 ^ { - 1 5 } , 2 . 5 7 9 7 9 1 5 \times 1 0 ^ { - 1 5 } ,$ $\mathrm { 8 9 \times 1 0 ^ { - 1 5 } , 2 . 5 7 9 7 9 1 5 \times 1 0 ^ { - 1 5 } , 1 . 2 0 6 6 5 4 9 \times 1 0 ^ { - 1 5 } }$ , $5 . 6 3 0 6 2 4 1 \times 1 0 ^ { - 1 6 } , 2 . 6 2 1 2 5 0 5 \times 1 0 ^ { - 1 6 } , 1 . 2 1 7 4 2 8$ $\mathrm { \dot { 0 } 5 } \times 1 0 ^ { - 1 6 } , 1 . 2 1 7 4 2 8 1 \times 1 0 ^ { - 1 6 } , 5 . 6 4 1 1 2 4 9 \times 1 0 ^ { - 1 7 }$ $\mathbf { 8 1 } \times 1 0 ^ { - 1 6 } , 5 . 6 4 1 1 2 4 9 \times 1 0 ^ { - 1 7 } , 2 . 6 0 7 8 4 1 5 \times 1 0 ^ { - 1 7 }$ , $1 . 2 0 2 8 0 6 3 \times 1 0 ^ { - 1 4 } , 5 . 5 3 4 9 7 4 3 \times 1 0 ^ { - 1 8 } , 2 . 5 4 1 2 5 2 2 \times 1 0 ^ { - 1 8 } , 1 . 1 6 4 1 2 4 3 \times 1 0 ^ { - 1 8 } , 5 . 5 3 4 2 5 6 0 , 0 . 1 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 2 . 2 2 6 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 2 . 2 2 6 2 2 6 2 \times 1 0 ^ { - 1 8 } , 0 . 1 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 0 . 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 0 . 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 0 . 2 2 6 2 8$ $( 2 2 \times 1 0 ^ { - 1 8 } , 1 . 1 6 4 1 2 4 3 \times 1 0 ^ { - 1 8 } , 5 . 3 2 0 8 1 2 0 \times 1 0 ^ { - 1 9 }$ , $2 . 4 2 6 5 6 0 9 \times 1 0 ^ { - 1 9 } , 1 . 1 0 4 1 9 8 8 \times 1 0 ^ { - 1 9 } , 5 . 0 1 3 6 5 4 8 \times 1 0 ^ { - 2 0 } , 2 . 2 7 1 5 4 3 6 \times 1 0 ^ { - 2 0 } , 1 . 0 2 6 9 6 5 5 \times 1 0 ^ { - 2 0 } ,$ $4 . 6 3 3 0 5 5 2 { \times } 1 0 ^ { - 2 1 } , 2 . 0 8 5 7 6 2 3 { \times } 1 0 ^ { - 2 1 } , 9 . 3 7 0 3 7 1$ $\}$ $1 5 \times 1 0 ^ { - 2 2 } , 4 . 2 0 0 9 9 7 8 \times 1 0 ^ { - 2 2 } , 1 . 8 7 9 5 8 0 0 \times 1 0 ^ { - 2 2 }$ , 8.3924 $9 3 3 \times 1 0 ^ { - 2 3 } , 3 . 7 3 9 8 3 2 0 \times 1 0 ^ { - 2 3 } , 1 . 6 6 3 2 3 3 5 \times 1 0 ^ { - 2 }$ $3 2 0 \times 1 0 ^ { - 2 3 } , 1 . 6 6 3 2 3 3 5 \times 1 0 ^ { - 2 3 } , 7 . 3 8 2 5 0 0 9 \times 1 0 ^ { - 2 4 }$ $3 5 \times 1 0 ^ { - 2 3 } , 7 . 3 8 2 5 0 0 9 \times 1 0 ^ { - 2 4 } , 3 . 2 7 0 4 8 4 0 \times 1 0 ^ { - 2 4 }$ , $1 . 4 4 6 0 6 5 2 { \times } 1 0 ^ { - 2 4 } , 6 . 3 8 1 7 5 3 7 { \times } 1 0 ^ { - 2 5 } , 2 . 8 1 1 1 0 8$ $A A \in \cap \theta C 5 < 9 < 1 0 - 2 4 < 6 . 9 8 1 7 5 < 2 7 < 1 0 - 2 5 < 2 8 1 1 1 0 8 1 < 1 0 ^ { - 2 5 } 1 9 3 5 0 7 7 2 0 < 1 0 ^ { - 2 5 } < 4 9 . 4 2 0 6 A < 1 0 ^ { - 2 6 }$ $7 \times 1 0 ^ { - 2 5 } , 2 . 8 1 1 1 0 8 1 \times 1 0 ^ { - 2 5 } , 1 . 2 3 5 9 7 3 9 \times 1 0 ^ { - 2 5 } ,$ $5 . 4 2 4 3 0 6 4 \times 1 0 ^ { - 2 6 }$ $2 . 3 7 6 2 4 4 3 \times 1 0 ^ { - 2 6 } , 1 . 0 3 9 1 0 3 1 \times 1 0 ^ { - 2 6 } , 4 . 5 3 5 8 1 7 9 \times 1 0 ^ { - 2 \prime } , 1 . 9 7 6 4 7 1 4 \times 1 0 ^ { - 2 \prime } , 8 . 9 7 6 2 4 1 8 \times 1 0 ^ { - 2 \prime } , 9 . 9 7 6 2 4 1 8 \times 1 0 ^ { - 2 \prime } , 9 . 9 7 6 2 4 1 8 \times 1 0 ^ { - 2 \prime } , 1 . 9 7 6 2 4 1 8 \times 1 0 ^ { - 3 \prime } .$ $8 . 5 9 7 4 9 5 6 \times 1 0 ^ { - 2 8 }$ , $3 . 7 3 3 4 3 2 6 \times 1 0 ^ { - 2 8 } , 1 . 6 1 8 4 8 2 3 \times 1 0 ^ { - 2 8 } , 7 . 0 0 4 5 3 1 9 \times 1 0 ^ { - 2 9 } , 3 . 0 2 6 4 2 5 5 \times 1 0 ^ { - 2 9 } , 1 . 0 2 6 8 4 8 2 5 2 6 \times 1 0 ^ { - 2 9 } , 2 . 0 2 6 8 4 8 2 5 8 8 8 1 9 \times 1 0 ^ { - 2 9 } , 2 . 0 2 6 8 4 8 2 5 8 8 1 9 \times 1 0 ^ { - 2 9 } , 3 . 0 2 8 4 8 2 4 9 6 2 5 8 8 1 9 \times 1 0 ^ { - 2 9 } , 2 . 0 2 8 4 8 2 4 9 6 2 5 8 1 9 \times 1 0 ^ { - 2 9 } , 3 . 0 2 8 4 8 2 4 8 2 8 8 8 1 9 8 2 8 8 1$ $1 . 3 0 5 4 7 5 3 \times 1 0 ^ { - 2 9 }$ , $5 . 6 2 2 1 5 7 7 \times 1 0 ^ { - 3 0 }$ $5 7 7 \times 1 0 ^ { - 3 0 } , 2 . 4 1 7 3 5 7 3 \times 1 0 ^ { - 3 0 } , 1 . 0 3 7 7 4 1 4 \times 1 0 ^ { - 3 6 }$ $5 7 3 \times 1 0 ^ { - 3 0 } , 1 . 0 3 7 7 4 1 4 \times 1 0 ^ { - 3 0 } , 4 . 4 4 7 8 7 2 6 \times 1 0 ^ { - 3 1 }$ $\cdot 1 4 \times 1 0 ^ { - 3 0 } , 4 . 4 4 7 8 7 2 6 \times 1 0 ^ { - 3 1 } , 1 . 9 0 3 3 7 5 1 \times 1 0 ^ { - 3 1 }$ , 8. $. 1 3 1 2 4 5 3 \times 1 0 ^ { - 3 2 } , 3 . 4 6 6 0 5 1 3 \times 1 0 ^ { - 3 2 } , 1 . 4 7 1 2 6 6 5 \times 1 0 ^ { - 3 2 } , 6 . 1 7 0 7 3 2 5 \times 1 0 ^ { - 3 3 } , 2 . 4 7 9 0 8 1 2 \times 1 0 ^ { - 3 3 } , 2 . 7 9 0 7 2 6 8 1 2 \times 1 0 ^ { - 3 3 }$ $8 . 2 6 3 6 0 3 9 \times 1 0 ^ { - 3 4 } ) ^ { t }$ , using 40 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 5 }$ in $l _ { \infty }$ norm with the Gauss-Seidel method.

17. (a) Since $A$ is a positive definite, $a _ { i i } > 0$ for $1 \leq i \leq n$ and $A$ is symmetric. Thus, $A$ can be written as $A = D - L - L ^ { t }$ , where $D$ is diagonal with $d _ { i i } > 0$ and $L$ is lower triangular. The diagonal of the lower triangular matrix $D - L$ has the positive entries $d _ { 1 1 } = a _ { 1 1 }$ , $d _ { 2 2 } = a _ { 2 2 } , \cdots$ , $d _ { n n } = a _ { n n }$ , so $( D - L ) ^ { - 1 }$ exists.

(b) Since $A$ is symmetric,

$$
P ^ { t } = \left( A - T _ { g } ^ { t } A T _ { g } \right) ^ { t } = A ^ { t } - T _ { g } ^ { t } A ^ { t } T _ { g } = A - T _ { g } ^ { t } A T _ { g } = P .
$$

Thus, $P$ is symmetric.

(c) $T _ { g } = ( D - L ) ^ { - 1 } L ^ { t }$ , so

$$
( D - L ) T _ { g } = L ^ { t } = D - L - D + L + L ^ { t } = ( D - L ) - ( D - L - L ^ { t } ) = ( D - L ) - A .
$$

Since $( D - L ) ^ { - 1 }$ exists, we have $T _ { g } = I - ( D - L ) ^ { - 1 } A$ .

(d) Since $Q = ( D - L ) ^ { - 1 } A$ , we have $T _ { g } = I - Q$ . Note that $Q ^ { - 1 }$ exists. By the definition of $P$ we have

$$
\begin{array} { r l } & { P = A - T _ { g } ^ { t } A T _ { g } = A - \left[ I - \left( D - L \right) ^ { - 1 } A \right] ^ { t } A \left[ I - \left( D - L \right) ^ { - 1 } A \right] } \\ & { \quad = A - \left[ I - Q \right] ^ { t } A [ I - Q ] = A - \left( I - Q ^ { t } \right) A ( I - Q ) } \\ & { \quad = A - \left( A - Q ^ { t } A \right) \left( I - Q \right) = A - \left( A - Q ^ { t } A - A Q + Q ^ { t } A Q \right) } \\ & { \quad = Q ^ { t } A + A Q - Q ^ { t } A Q = Q ^ { t } \left[ A + \left( Q ^ { t } \right) ^ { - 1 } A Q - A Q \right] } \\ & { \quad = Q ^ { t } \left[ A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A \right] Q . } \end{array}
$$

(e) Since

$$
\boldsymbol { A } \boldsymbol { Q } ^ { - 1 } = \boldsymbol { A } \left[ \boldsymbol { A } ^ { - 1 } ( \boldsymbol { D } - \boldsymbol { L } ) \right] = \boldsymbol { D } - \boldsymbol { L } \quad \mathrm { a n d } \quad \left( \boldsymbol { Q } ^ { t } \right) ^ { - 1 } \boldsymbol { A } = \boldsymbol { D } - \boldsymbol { L } ^ { t } ,
$$

we have

$$
A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A = D - L + D - L ^ { t } - \left( D - L - L ^ { t } \right) = D .
$$

Thus,

$$
P = Q ^ { t } \left[ A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A \right] Q = Q ^ { t } D Q .
$$

So for $\mathbf { x } \in \mathbb { R } ^ { n }$ , we have ${ \bf x } ^ { t } P { \bf x } = { \bf x } ^ { t } Q ^ { t } D Q { \bf x } = ( Q { \bf x } ) ^ { t } D ( Q { \bf x } )$ .

Since $D$ is a positive diagonal matrix, $( Q { \bf x } ) ^ { t } D ( Q { \bf x } ) \ge 0$ unless $Q \mathbf { x } = \mathbf { 0 }$ . However, $Q$ is nonsingular, so $Q \mathbf { x } = \mathbf { 0 }$ if and only if $\mathbf x = \mathbf 0$ . Thus, $P$ is positive definite.

(f) Let $\lambda$ be an eigenvalue of $T _ { g }$ with the eigenvector $\mathbf { x } \neq \mathbf { 0 }$ . Since $\mathbf { x } ^ { t } P \mathbf { x } > 0$ ,

$$
\mathbf { x } ^ { t } \left[ A - T _ { g } ^ { t } A T _ { g } \right] \mathbf { x } > 0
$$

and

$$
\mathbf { x } ^ { t } A \mathbf { x } - \mathbf { x } ^ { t } T _ { g } ^ { t } A T _ { g } \mathbf { x } > 0 .
$$

Since $T _ { g } \mathbf { x } = \lambda \mathbf { x }$ , we have $\mathbf { x } ^ { t } T _ { g } ^ { t } = \lambda \mathbf { x } ^ { t }$ so

$$
\left( 1 - \lambda ^ { 2 } \right) \mathbf { x } ^ { t } A x = \mathbf { x } ^ { t } A \mathbf { x } - \lambda ^ { 2 } \mathbf { x } ^ { t } A x > 0 .
$$

Since $A$ is positive definite, $1 - \lambda ^ { 2 } > 0$ , and $\lambda ^ { 2 } < 1$ . Thus $| \lambda | < 1$

(g) For any eigenvalue $\lambda$ of $T _ { g }$ , we have $| \lambda | < 1$ . This implies $\rho ( T _ { g } ) < 1$ and $T _ { g }$ is convergent.

# Exercise Set 7.4, page 467

1. Two iterations of the SOR method with $\omega = 1 . 1$ give the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 0 5 4 1 0 0 7 9 , - 0 . 2 1 1 5 4 3 5 , 0 . 6 4 7 7 1 5 9 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 8 7 6 7 9 0 , 0 . 9 7 8 4 9 3 5 , 0 . 7 8 9 9 3 2 8 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 7 1 8 8 5 , 2 . 8 1 8 8 2 2 , - 0 . 2 8 0 9 7 2 6 , - 2 . 2 3 5 4 2 2 ) ^ { i }$ t

$$
\mathbf { x } ^ { ( 2 ) } = ( 1 . 0 7 9 6 7 5 , - 1 . 2 6 0 6 5 4 , 2 . 0 4 2 4 8 9 , 1 . 9 9 5 3 7 3 , 2 . 0 4 9 5 3 6 ) ^ { t }
$$

2. Two iterations of the SOR method with $\omega = 1 . 1$ give the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 5 1 2 7 7 5 0 0 0 , - 0 . 8 2 9 8 4 9 1 6 6 7 , - 0 . 0 8 4 3 3 7 3 6 6 7 ) ^ { t }$   
(b) $\mathfrak { c } ^ { ( 2 ) } = ( - 1 . 5 8 5 2 3 7 5 0 , 1 . 3 7 8 8 5 6 8 8 , - 0 . 7 0 3 9 2 1 2 8 \mathrm { . }$ 12)t   
(c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 6 6 0 4 9 0 2 , 0 . 0 3 7 0 0 7 4 9 , - 0 . 2 4 9 3 5 1 3 , 0 . 6 5 6 1 1 3 9 ) ^ { t }$   
(d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 3 7 8 1 2 5 0 0 0 0 , 1 . 4 4 5 4 6 8 7 5 0 , 0 . 3 5 9 6 9 1 4 0 6 2 , 1 . 4 5 8 5 3 1 2 5 0 , 0 . 3 0 7 1 9 2 1 8 7 6 0 0 0 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 . 0 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 . 0 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 . 0 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 . 0 , 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 .$ 5, 1.572124727)t

3. Two iterations of the SOR method with $\omega = 1 . 3$ give the following results.

\*(a) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 1 0 4 0 1 0 3 , - 0 . 1 3 3 1 8 1 4 , 0 . 6 7 7 4 9 9 7 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 5 7 0 7 3 , 0 . 9 9 0 3 8 7 5 , 0 . 7 2 0 6 5 6 9 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 2 3 6 9 5 , 3 . 2 2 8 7 5 2 , - 0 . 1 5 2 3 8 8 8 , - 2 . 0 4 1 2 6 6 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 7 0 6 4 2 5 8 , - 0 . 4 1 0 3 8 7 6 , 2 . 4 1 7 0 6 3 , 2 . 2 5 1 9 5 5 , 1 . 0 6 1 5 0 7 ) ^ { t }$

4. Two iterations of the SOR method with $\omega = 1 . 3$ give the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 4 5 5 7 8 3 3 3 4 , - 0 . 7 7 2 1 4 9 4 4 4 2 , - 0 . 0 8 0 5 3 9 6 2 2 8 ) ^ { t }$   
(b) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 4 2 0 7 3 7 5 0 , 1 . 5 9 5 7 5 8 1 2 5 , - 0 . 8 5 9 7 9 2 7 8 1 2 ) ^ { t }$   
(c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 7 2 6 8 8 9 3 , 0 . 1 2 5 1 4 8 3 , - 0 . 2 9 2 3 3 7 1 , 0 . 7 0 3 7 0 1 8 ) ^ { t }$   
(d) $\mathbf { x } ^ { \left. \varepsilon \right. } = ( 0 . 5 2 8 1 2 5 0 0 0 0 , 1 . 4 8 0 7 8 1 2 5 0 , 0 . 3 2 2 8 1 6 4 0 6 , 1 . 3 5 9 7 1 8 7 5 0 , 0 . 4 2 8 8 1 7 1 8 7 5 , 1 . 5 0 5 9 4 9 9 6 1 ) ^ { \varepsilon }$

5. The SOR Algorithm with $\omega = 1 . 2$ gives the following results.

\*(a) $\mathbf { x } ^ { ( 1 1 ) } = ( 0 . 0 3 5 4 4 3 5 6 , - 0 . 2 3 7 1 8 3 3 3 , 0 . 6 5 7 8 8 3 1 7 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 7 ) } = ( 0 . 9 9 5 8 3 4 1 , 0 . 9 5 7 9 0 4 1 , 0 . 7 9 1 5 7 5 6 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 8 ) } = ( - 0 . 7 9 7 6 0 0 9 , 2 . 7 9 5 2 8 8 , - 0 . 2 5 8 8 2 9 3 , - 2 . 2 5 1 7 6 8 ) ^ { t }$ (d) $\mathfrak { c } ^ { ( \mathrm { 1 0 } ) } = ( 0 . 7 8 6 6 3 1 0 , - 1 . 0 0 2 8 0 7 , 1 . 8 6 6 5 3 0 , 1 . 9 1 2 6$ 45, 1.989792) $t$

6. The SOR Algorithm with $\omega = 1 . 2$ gives the following results.

(a) $\mathbf { x } ^ { ( 8 ) } = ( 1 . 4 4 7 5 0 3 8 1 4 , - 0 . 8 3 5 9 2 9 7 6 2 4 , - 0 . 0 4 4 5 5 1 6 5 3 2 ) ^ { t }$   
(b) $\mathbf { x } ^ { ( 6 ) } = ( - 1 . 4 5 4 5 8 2 8 5 0 , 1 . 4 5 4 4 9 8 8 6 3 , - 0 . 7 2 7 3 3 0 2 7 1 4 ) ^ { t }$   
(c) $\mathbf { x } ^ { ( 0 ) } = ( - 0 . 7 5 3 0 8 9 7 1 , 0 . 0 4 1 1 7 2 8 1 , - 0 . 2 8 0 7 4 8 1 7 , 0 . 6 9 1 6 3 5 0 6 ) ^ { u }$   
(d) $\mathbf { x } ^ { ( 7 ) } = ( 0 . 3 5 7 1 2 8 4 9 4 5 , 1 . 4 2 8 5 8 2 2 4 0 , 0 . 3 5 7 1 4 8 9 7 3 1 , 1 . 5 7 1 4 4 0 1 1 6 , 0 . 2 8 5 7 5 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 )$ 000650, 1.571445036)t

7. The tridiagonal matrices are in parts (b) and (c). \*(9b): For $\omega = 1 . 0 1 2 8 2 3$ we have $\mathbf { x } ^ { ( 4 ) } = ( 0 . 9 9 5 7 8 4 6 , 0 . 9 5 7 8 9 3 5 , 0 . 7 9 1 5 7 8 8 ) ^ { t }$ . (9c): For $\omega = 1 . 1 5 3 4 9 9$ we have $\mathbf { x } ^ { ( 7 ) } = ( - 0 . 7 9 7 7 6 5 1 , 2 . 7 9 5 3 4 3 , - 0 . 2 5 8 8 0 2 1 , - 2 . 2 5 1 7 6 0 ) ^ { t }$ .

8. The tridiagonal matrix is in part (d). (10d): For $\omega = 1 . 0 3 3 3 7 0 4 5 3$ we have

x(5) = (0.3571407017, 1.428570817, 0.357142771, 1.571421010, 0.2857118407, 1.571428256)t.

9. Let $\lambda _ { 1 } , . . . , \lambda _ { n }$ be the eigenvalues of $T _ { \omega }$ . Then

$$
\begin{array} { l } { \displaystyle \prod _ { i = 1 } ^ { n } \lambda _ { i } = \operatorname* { d e t } T _ { \omega } = \operatorname* { d e t } \bigg ( ( D - \omega L ) ^ { - 1 } [ ( 1 - \omega ) D + \omega U ] \bigg ) } \\ { = \operatorname* { d e t } ( D - \omega L ) ^ { - 1 } \operatorname* { d e t } ( ( 1 - \omega ) D + \omega U ) = \operatorname* { d e t } \big ( D ^ { - 1 } \big ) \operatorname* { d e t } ( ( 1 - \omega ) D ) } \\ { = \bigg ( \displaystyle \frac { 1 } { \big ( a _ { 1 1 } a _ { 2 2 } \ldots a _ { n n } \big ) } \bigg ) \bigg ( ( 1 - \omega ) ^ { n } a _ { 1 1 } a _ { 2 2 } \ldots a _ { n n } \bigg ) \bigg ) = ( 1 - \omega ) ^ { n } . } \end{array}
$$

Thus

$$
\rho ( T _ { \omega } ) = \underset { 1 \leq i \leq n } { \operatorname* { m a x } } | \lambda _ { i } | \geq | \omega - 1 | ,
$$

and $| \omega - 1 | < 1$ if and only if $0 < \omega < 2$ .

10. (a) The system was reordered so that the diagonal of the matrix had nonzero entries.

(b) (i) The solution vector using 30 iterations is

$( 0 . 0 0 3 6 \dot { 2 } , - 6 \dot { 3 } 3 9 . 7 4 4 6 \dot { 3 } 8 , - 3 6 6 0 . 2 5 \dot { 3 } 2 7 \dot { 2 } , - 8 9 6 5 . 7 5 5 8 0 8 , 6 \dot { 3 } \dot { 3 } 9 . 7 4 4 6 \dot { 3 } 8 , 1 0 0 0 0$ , − 7320.508959, 6339.746729)t.

(ii) The solution vector using 57 iterations is

(−0.002651, − 6339.744637, −3660.255362, −8965.752851, 6339.748259, 10000, − 7320.506544, 6339.748258)t.

(iii) Method does not converge using $\omega = 1 . 2 5$ . However, using $\omega = 1 . 1$ and using 132 iterations gives the solution vector

(0.0045175, − 6339.744528, −3660.253009, $-$ 8965.756179, 6339.743756, 10000, $- 7 3 2 0 . 5 0 9 5 4 7 , 6 3 3 9 . 7 4 7 5 4 4 ) ^ { \iota }$ .

11. The results that follow include approximations from the Jacobi and Gauss-Seidel methods for comparison.   

<table><tr><td></td><td>Jacobi 33</td><td>Gauss-Seidel 8 iterations</td><td>SOR (ω = 1.2) 13</td><td></td><td>Jacobi</td><td>Gauss-Seidel</td><td>SOR (ω = 1.2)</td></tr><tr><td></td><td>iterations</td><td></td><td>iterations</td><td></td><td>iterations</td><td>iterations</td><td>iterations</td></tr><tr><td>X1</td><td>1.53873501</td><td>1.53873270</td><td>1.53873549</td><td>X41</td><td>0.02185033</td><td>0.02184781</td><td>0.02184855</td></tr><tr><td>x2</td><td>0.73142167</td><td>0.73141966</td><td>0.73142226</td><td>X42</td><td>0.02133203</td><td>0.02132965</td><td>0.02133038</td></tr><tr><td>x3</td><td>0.10797136</td><td>0.10796931</td><td>0.10797063</td><td>X43</td><td>0.02083782</td><td>0.02083545</td><td>0.02083615</td></tr><tr><td>X4</td><td>0.17328530</td><td>0.17328340</td><td>0.17328480</td><td>X44</td><td>0.02036585</td><td>0.02036360</td><td>0.02036429</td></tr><tr><td>X5</td><td>0.04055865</td><td>0.04055595</td><td>0.04055737</td><td>X45</td><td>0.01991483</td><td>0.01991261</td><td>0.01991324</td></tr><tr><td>X6</td><td>0.08525019</td><td>0.08524787</td><td>0.08524925</td><td>X46</td><td>0.01948325</td><td>0.01948113</td><td>0.01948175</td></tr><tr><td>X7</td><td>0.16645040</td><td>0.16644711 0.12197878</td><td>0.16644868 0.12198026</td><td>X47</td><td>0.01907002</td><td>0.01906793</td><td>0.01906846</td></tr><tr><td>x8</td><td>0.12198156</td><td></td><td></td><td>X48</td><td>0.01867387</td><td>0.01867187</td><td>0.01867239</td></tr><tr><td>x9</td><td>0.10125265</td><td>0.10124911</td><td>0.10125043</td><td>X49</td><td>0.01829386</td><td>0.01829190</td><td>0.01829233</td></tr><tr><td>X10</td><td>0.09045966</td><td>0.09045662</td><td>0.09045793 0.07202912</td><td>X50</td><td>0.71792896</td><td>0.01792707</td><td>0.01792749</td></tr><tr><td>X11</td><td>0.07203172</td><td>0.07202785</td><td>0.07026392</td><td>X51</td><td>0.01757833</td><td>0.01757648</td><td>0.01757683</td></tr><tr><td>X12</td><td>0.07026597</td><td>0.07026266</td><td>0.06875546</td><td>X52</td><td>0.01724113</td><td>0.01723933</td><td>0.01723968</td></tr><tr><td>X13</td><td>0.06875835</td><td>0.06875421 0.06324307</td><td>0.06324429</td><td>X53</td><td>0.01691660</td><td>0.01691487</td><td>0.01691517</td></tr><tr><td>X14</td><td>0.06324659</td><td>0.05971083</td><td>0.05971200</td><td>X54</td><td>0.01660406</td><td>0.01660237</td><td>0.01660267</td></tr><tr><td>X15</td><td>0.05971510</td><td>0.05570834</td><td>0.05570949</td><td>X55</td><td>0.01630279</td><td>0.01630127</td><td>0.01630146</td></tr><tr><td>X16</td><td>0.05571199 0.05187851</td><td>0.05187416</td><td>0.05187529</td><td>X56</td><td>0.01601230 0.01573198</td><td>0.01601082</td><td>0.01601101</td></tr><tr><td>X17</td><td>0.04924911</td><td>0.04924537</td><td>0.04924648</td><td>X57</td><td></td><td>0.01573087</td><td>0.01573077</td></tr><tr><td>X18</td><td>0.04678213</td><td>0.04677776</td><td>0.04677885</td><td>X58</td><td>0.01546129</td><td>0.01546020</td><td>0.01546010</td></tr><tr><td>X19</td><td>0.04448679</td><td>0.04448303</td><td>0.04448409</td><td>X59</td><td>0.01519990</td><td>0.01519909</td><td>0.01519878</td></tr><tr><td>x20</td><td>0.04246924</td><td>0.04246493</td><td>0.04246597</td><td>X60</td><td>0.01494704</td><td>0.01494626</td><td>0.01494595</td></tr><tr><td>X21</td><td>0.04053818</td><td>0.04053444</td><td>0.04053546</td><td>X61</td><td>0.01470181</td><td>0.01470085</td><td>0.01470077</td></tr><tr><td>X22</td><td></td><td>0.03876852</td><td>0.03876952</td><td>X62</td><td>0.01446510</td><td>0.01446417</td><td>0.01446409</td></tr><tr><td>X23</td><td>0.03877273 0.03718190</td><td>0.03717822</td><td>0.03717920</td><td>X63</td><td>0.01423556</td><td>0.01423437</td><td>0.01423461</td></tr><tr><td>X24</td><td></td><td>0.03570451</td><td>0.03570548</td><td>X64</td><td>0.01401350</td><td>0.01401233</td><td>0.01401256</td></tr><tr><td>X25</td><td>0.03570858 0.03435107</td><td>0.03434748</td><td>0.03434844</td><td>X65</td><td>0.01380328</td><td>0.01380234</td><td>0.01380242</td></tr><tr><td>X26</td><td>0.03309542</td><td>0.03309152</td><td>0.03309246</td><td>X66</td><td>0.01359448</td><td>0.01359356</td><td>0.01359363</td></tr><tr><td>X27</td><td>0.03192212</td><td>0.03191866</td><td>0.03191958</td><td>X67</td><td>0.01338495</td><td>0.01338434</td><td>0.01338418</td></tr><tr><td>X28</td><td></td><td>0.03082637</td><td>0.03082727</td><td>X68</td><td>0.01318840</td><td>0.01318780</td><td>0.01318765</td></tr><tr><td>X29</td><td>0.03083007 0.02980997</td><td>0.02980666</td><td>0.02980755</td><td>X69</td><td>0.01297174</td><td>0.01297109 0.01278598</td><td>0.01297107</td></tr><tr><td>X30</td><td>0.02885510</td><td>0.02885160</td><td>0.02885248</td><td>x70</td><td>0.01278663</td><td>0.01270263</td><td>0.01278597</td></tr><tr><td>X31</td><td>0.02795937</td><td>0.02795621</td><td>0.02795707</td><td>X71</td><td>0.01270328</td><td></td><td>0.01270271</td></tr><tr><td>X32</td><td>0.02711787</td><td>0.02711458</td><td>0.02711543</td><td>X72</td><td>0.01252719</td><td>0.01252656</td><td>0.01252663</td></tr><tr><td>X33</td><td></td><td></td><td></td><td>X73</td><td>0.01237700</td><td>0.01237656</td><td>0.01237654</td></tr><tr><td>X34</td><td>0.02632478</td><td>0.02632179</td><td>0.02632262</td><td>X74</td><td>0.01221009</td><td>0.01220965</td><td>0.01220963</td></tr><tr><td>X35</td><td>0.02557705</td><td>0.02557397</td><td>0.02557479</td><td>X75</td><td>0.01129043</td><td>0.01129009</td><td>0.01129008</td></tr><tr><td>X36</td><td>0.02487017</td><td>0.02486733</td><td>0.02486814</td><td>X76</td><td>0.01114138</td><td>0.01114104</td><td>0.01114102</td></tr><tr><td>X37</td><td>0.02420147</td><td>0.02419858</td><td>0.02419938</td><td>X77</td><td>0.01217337</td><td>0.01217312</td><td>0.01217313</td></tr><tr><td>x38</td><td>0.02356750</td><td>0.02356482</td><td>0.02356560</td><td>X78</td><td>0.01201771</td><td>0.01201746</td><td>0.01201746</td></tr><tr><td>X39</td><td>0.02296603</td><td>0.02296333</td><td>0.02296410</td><td>x79</td><td>0.01542910</td><td>0.01542896</td><td>0.01542896</td></tr><tr><td>X40</td><td>0.02239424</td><td>0.02239171</td><td>0.02239247</td><td>x80</td><td>0.01523810</td><td>0.01523796</td><td>0.01523796</td></tr></table>

12. For $0 < \omega < 2$ , let $T _ { \omega } = ( D - \omega L ) ^ { - 1 } \left[ ( 1 - \omega ) D + \omega L ^ { t } \right] .$ . Let $P = A - T _ { \omega } ^ { t } A T _ { \omega }$ and note that $P$ is symmetric.

As in Exercise 17 of Section 7.3, we derive a new representation for $T _ { \omega }$ :

$$
( D - \omega L ) T _ { \omega } = ( 1 - \omega ) D + \omega L ^ { t } = ( D - \omega L ) - \omega A , \mathrm { s o } T _ { \omega } = I - \omega ( D - \omega L ) ^ { - 1 } A .
$$

Let

$$
\begin{array} { r } { Q = \omega ( D - \omega L ) ^ { - 1 } A \quad \mathrm { a n d } \quad Q ^ { t } = \omega A \left[ ( D - \omega L ) ^ { - 1 } \right] ^ { t } . } \end{array}
$$

We again have

$$
P = Q ^ { t } \left[ A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A \right] Q .
$$

But

$$
A Q ^ { - 1 } = \frac { 1 } { \omega } ( D - \omega L ) \quad \mathrm { a n d } \quad \left( Q ^ { t } \right) ^ { - 1 } A = \frac { 1 } { \omega } \left( D - \omega L ^ { t } \right)
$$

so

$$
\begin{array} { c } { \displaystyle { A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A = \frac 1 \omega \left[ D - \omega L + D - \omega L ^ { t } \right] - A } } \\ { \displaystyle { = \frac 2 \omega D - D + D - L - L ^ { t } - A } } \\ { \displaystyle { = \left( \frac 2 \omega - 1 \right) D . } } \end{array}
$$

Thus $P = \left( { \frac { 2 } { \omega } } - 1 \right) Q ^ { t } D Q$ . Since $0 < \omega < 2$ , we have $\frac { \ d ^ { 2 } } { \ d \omega } - 1 > 0$ and $P$ is positive definite.

The proof follows Exercise 17 with $T _ { g }$ replaced by $T _ { \omega }$ . Hence, $T _ { \omega }$ is convergent.

# Exercise Set 7.5, page 482

1. The $l _ { \infty }$ condition numbers are:

(a) 50 (b) 241.37 (c) 600,002 (d) 339,866

2. The $l _ { \infty }$ condition numbers are:

(a) 12.24012756 (b) 12.24012756 (c) 12 \*(d) 198.17

3. We have

<table><tr><td></td><td>=x-xα</td><td>K(A)/b- Ax∞/A</td></tr><tr><td>(a)</td><td>8.571429 × 10-4</td><td>1.238095 × 10-2</td></tr><tr><td>(b)</td><td>0.1</td><td>3.832060</td></tr><tr><td>(c）</td><td>0.04</td><td>0.8</td></tr><tr><td>(d）</td><td>20</td><td>1.152440 × 105</td></tr></table>

4. We have

<table><tr><td></td><td>x-x|α</td><td>K(A)|b- Ax|∞/A∞</td></tr><tr><td>(a)</td><td>20</td><td>65.03241</td></tr><tr><td>(b)</td><td>0.02</td><td>720.5764</td></tr><tr><td>（c）</td><td>0.1</td><td>3.727412 × 10-1</td></tr><tr><td>*（d)</td><td>6.551700 × 10-2</td><td>9.059201</td></tr></table>

5. Gaussian elimination and iterative refinement give the following results.

(a) (i) $( - 1 0 . 0 , 1 . 0 1 ) ^ { t }$ , (ii) $( 1 0 . 0 , 1 . 0 0 ) ^ { t }$   
(b) (i) $( 1 2 . 0 , 0 . 4 9 9 , - 1 . 9 8 ) ^ { t }$ , (ii) $( 1 . 0 0 , 0 . 5 0 0 , - 1 . 0 0 ) ^ { t }$   
(c) (i) $( 0 . 1 8 5 , 0 . 0 1 0 3 , - 0 . 0 2 0 0 , - 1 . 1 2 ) ^ { t }$ , (ii) $( 0 . 1 7 7 , 0 . 0 1 2 7 , - 0 . 0 2 0 7 , - 1 . 1 8 ) ^ { \tau }$   
(d) (i) $( 0 . 7 9 9 , - 3 . 1 2 , 0 . 1 5 1 , 4 . 5 6 ) ^ { t }$ , (ii) $( 0 . 7 5 8 , - 3 . 0 0 , 0 . 1 5 9 , 4 . 3 0 ) ^ { t }$

6. Gaussian elimination and iterative refinement give the following results.

$$
\begin{array} { r l } & { ( 1 2 . 0 0 , 0 . 9 9 9 0 ) ^ { t } , ( 1 0 . 0 0 , 1 . 0 0 0 ) ^ { t } } \\ & { ( 1 . 2 0 0 , 0 . 5 0 0 2 , - 1 . 3 8 0 ) ^ { t } , ( 1 . 0 0 0 , 0 . 5 0 0 0 , - 0 . 9 9 9 8 ) ^ { t } } \\ & { ( 0 . 1 7 5 6 , 0 . 0 1 3 0 5 , - 0 . 0 2 0 7 5 , - 1 . 1 9 2 ) ^ { t } , ( 0 . 1 7 6 8 , 0 . 0 1 2 6 9 , - 0 . 0 2 0 6 5 , - 1 . 1 8 2 ) ^ { t } } \\ & { ( 0 . 7 9 6 3 , - 3 . 1 5 2 , 0 . 1 7 0 5 , 4 . 6 1 5 ) ^ { t } , ( 0 . 7 8 8 9 , - 3 . 1 2 8 , 0 . 1 6 7 8 , 4 . 5 6 1 ) ^ { t } } \end{array}
$$

7. The matrix is ill-conditioned since $K _ { \infty } = 6 0 0 0 2$ . We have $\tilde { \mathbf { x } } = ( - 1 . 0 0 0 0 , 2 . 0 0 0 0 ) ^ { t }$ .

8. The matrix $A$ is ill-conditioned since $K _ { \infty } ( A ) = 6 0 0 , 0 0 2$ and $\hat { \mathbf { x } } = ( 1 . 8 1 8 1 9 2 , 0 . 5 9 0 9 0 9 1 ) ^ { \iota }$

$^ { * } 9$ . For any vector $\mathbf { x }$ , we have

$$
\left\| \mathbf { x } \right\| = \left\| A ^ { - 1 } A \mathbf { x } \right\| \leq \left\| A ^ { - 1 } \right\| \left\| A \mathbf { x } \right\| , \ \mathrm { s o } \ \left\| A \mathbf { x } \right\| \geq { \frac { \left\| \mathbf { x } \right\| } { \left\| A ^ { - 1 } \right\| } } .
$$

Let $\mathbf { x } \neq \mathbf { 0 }$ be such that $\| \mathbf { x } \| = 1$ and $B \mathbf { x } = \mathbf { 0 }$ . Then

$$
\left\| ( A - B ) \mathbf { x } \right\| = \left\| A \mathbf { x } \right\| \geq { \frac { \left\| \mathbf { x } \right\| } { \left\| A ^ { - 1 } \right\| } } { \mathrm { a n d } } { \frac { \left\| ( A - B ) \mathbf { x } \right\| } { \left\| A \right\| } } \geq { \frac { 1 } { \left\| A ^ { - 1 } \right\| \left\| A \right\| } } = { \frac { 1 } { K ( A ) } } .
$$

Since $\| \mathbf { x } \| = 1$ ,

$$
\left\| ( A - B ) \mathbf { x } \right\| \leq \left\| A - B \right\| \left\| \mathbf { x } \right\| = \left\| A - B \right\| { \mathrm { ~ a n d ~ } } { \frac { \| A - B \| } { \left\| A \right\| } } \geq { \frac { 1 } { K ( A ) } } .
$$

10. The approximate condition numbers are as follows:

$^ { * } ( \mathrm { a } )$ With $B = { \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 1 } & { 2 } \end{array} \right] }$ , we have $K _ { \infty } ( A ) \geq 3 0 \small { , } 0 0 0$ (b) With $B = \left[ \begin{array} { l l } { 4 . 0 } & { 1 . 6 } \\ { 7 . 0 } & { 2 . 8 } \end{array} \right]$ , we have $K _ { \infty } ( A ) \geq { \frac { 9 7 } { 3 } }$ .

11. (a) $K _ { \infty } \left( H ^ { ( 4 ) } \right) = 2 8 , 3 7 5$ (b) $K _ { \infty } \left( H ^ { ( 5 ) } \right) = 9 4 3 , 6 5 6$ (c) actual solution $\mathbf { x } = ( - 1 2 4 , 1 5 6 0 , - 3 9 6 0 , 2 6 6 0 ) ^ { t }$ ; approximate solution $\tilde { \mathbf { x } } = ( - 1 2 4 . 2 , ~ 1 5 6 3 . 8 , - 3 9 7 1 . 8 , 2 6 6 8 . 8 ) ^ { t }$ ; $\| \mathbf { x } - \tilde { \mathbf { x } } \| _ { \infty } = 1 1 . 8$ ; and $\frac { \| \mathbf { x } - \tilde { \mathbf { x } } \| _ { \infty } } { \| \mathbf { x } \| _ { \infty } } = 0 . 0 2 9 8 0$ $\frac { K _ { \infty } ( A ) } { 1 - K _ { \infty } ( A ) \left( \frac { \| \delta A \| _ { \infty } } { \| A \| _ { \infty } } \right) } \left[ \frac { \| \delta b \| _ { \infty } } { \| b \| _ { \infty } } + \frac { \| \delta A \| _ { \infty } } { \| A \| _ { \infty } } \right] = \frac { 2 8 3 7 5 } { 1 - 2 8 3 7 5 \left( \frac { 6 . 6 \times 1 0 ^ { - 6 } } { 2 . 0 8 3 } \right) } \left[ 0 + \frac { 6 . { \overline { { 6 } } } \times 1 0 ^ { - 6 } } { 2 . 0 8 { \overline { { 3 } } } } \right]$

12. For the $3 \times 3$ Hilbert matrix $H$ , we have

$$
\hat { H } ^ { - 1 } = \left[ \begin{array} { c c c } { 8 . 9 6 8 } & { - 3 5 . 7 7 } & { 2 9 . 7 7 } \\ { - 3 5 . 7 7 } & { 1 9 0 . 6 } & { - 1 7 8 . 6 } \\ { 2 9 . 7 7 } & { - 1 7 8 . 6 } & { 1 7 8 . 6 } \end{array} \right] , \qquad \hat { H } = \left[ \begin{array} { c c c } { 0 . 9 7 9 9 } & { 0 . 4 8 7 0 } & { 0 . 3 2 3 8 } \\ { 0 . 4 8 6 0 } & { 0 . 3 2 4 6 } & { 0 . 2 4 3 4 } \\ { 0 . 3 2 3 2 } & { 0 . 2 4 3 3 } & { 0 . 1 9 4 9 } \end{array} \right] ,
$$

and $\| H - \hat { H } \| _ { \infty } = 0 . 0 4 2 6 0$ .

# Exercise Set 7.6, page 492

1. (a) (0.18, 0.13)t (b) (0.19, 0.10)t (c) Gaussian elimination gives the best answer since $\mathbf { v } ^ { ( 2 ) } = ( 0 , 0 ) ^ { t }$ in the conjugate gradient method. (d) $( 0 . 1 3 , 0 . 2 1 ) ^ { t }$ . There is no improvement, although $\mathbf { v } ^ { ( 2 ) } \neq \mathbf { 0 }$ .

2. (a) (1.0, 1.0)t (b) (1.0, 1.0)t (c) Both answers are the same. However, more operations are required in the conjugate gradient method. (d) $( 1 . 1 , 1 . 0 ) ^ { t }$ . The answer is not as good due to rounding error.

3. (a) $( 1 . 0 0 , - 1 . 0 0 , 1 . 0 0 ) ^ { t }$ (b) (0.827, 0.0453, −0.0357)t (c) Partial pivoting and scaled partial pivoting also give $( 1 . 0 0 , - 1 . 0 0 , 1 . 0 0 ) ^ { t }$ . (d) $( 0 . 7 7 6 , 0 . 2 3 8 , - 0 . 1 8 5 ) ^ { t } .$

The residual from (3b) is $( - 0 . 0 0 0 4 , - 0 . 0 0 3 8 , 0 . 0 0 3 7 ) ^ { t }$ , and the residual from part (3d) is (0.0022, −0.0038,0.0024)t. There does not appear to be much improvement, if any. Rounding error is more prevalent because of the increase in the number of matrix multiplications.

4. (a) $( 0 . 9 9 9 9 9 9 9 9 9 9 7 , - 1 , 1 ) ^ { t }$ (b) $( 0 . 9 9 9 9 9 9 9 1 9 5 9 , - 1 . 0 0 0 0 6 6 4 1 9 , 0 . 9 9 9 9 9 9 6 6 9 3 ) ^ { u }$ ; The residual is $\left( 0 . 1 1 2 3 6 \times 1 0 ^ { - 5 } , 0 . 6 2 4 2 \times 1 0 ^ { - 6 } , 0 . 4 3 8 7 \times 1 0 ^ { - 6 } \right) ^ { \tau }$ (c) Partial pivoting gives the same answer as in part (a). (d) (1.000000364, −0.999999391, 1.000000888)t.

The residual is $\left( - 0 . 1 0 0 0 1 \times 1 0 ^ { - 5 } , - 0 . 6 3 0 8 7 \times 1 0 ^ { - 6 } , - 0 . 4 6 9 1 \times 1 0 ^ { - 6 } \right) ^ { t } .$ .

There does not seem to be an improvement in this preconditioning method.

5. Two steps of the Conjugate Gradient method with $C = C ^ { - 1 } = I$ give the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 5 3 5 9 3 3 4 5 6 , - 0 . 1 6 9 7 9 3 2 1 1 7 , 0 . 5 9 0 1 1 7 2 0 9 1 ) ^ { t }$ and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 0 . 2 2 1$ .   
\*(b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 9 9 3 1 2 9 5 1 0 , 0 . 9 6 4 2 7 3 4 4 5 6 , 0 . 7 7 8 4 2 6 6 5 7 5 ) ^ { t } \hat { \varepsilon }$ nd $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 0 . 1 4 4$ .   
(c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 7 2 9 0 9 5 4 1 1 4 , 2 . 5 1 5 7 8 2 4 5 2 , - 0 . 6 7 8 8 9 0 4 0 5 8 , - 2 . 3 3 1 9 4 3 9 8 2 ) ^ { t } :$ and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 2 . 2$ .   
(d) $\mathbf { x } ^ { ( 2 ) } = \left( - 0 . 7 0 7 1 1 0 8 9 0 1 , - 0 . 0 9 5 4 7 4 8 8 8 1 , - 0 . 3 4 4 1 0 7 4 0 9 3 , 0 . 5 2 5 6 0 9 1 4 9 7 \right)$ t and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } =$ 0.39.   
(e) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 3 3 5 9 6 8 3 8 1 , 0 . 9 3 6 7 5 8 8 9 3 5 , 1 . 3 3 9 9 2 0 9 4 9 , 1 . 7 4 3 0 8 3 0 0 4 , 1 . 7 4 3 0 8 3 0 0 4 ) ^ { t } \mathfrak { s o l t a r s o f f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f }$ nd $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } =$ 1.3.   
(f) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 0 2 2 3 7 5 6 7 1 , 1 . 6 8 6 4 5 1 8 9 3 , 1 . 0 2 2 3 7 5 6 7 1 , 2 . 0 6 0 9 1 9 5 6 8 , 0 . 8 3 1 0 9 9 1 8 )$ 7764, 2.060919568)t and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 1 . 1 3$ .

6. Two steps of the Conjugate Gradient method with $C ^ { - 1 } = D ^ { - 1 / 2 }$ give the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 0 1 2 8 1 3 2 9 3 , - 0 . 2 0 9 5 5 0 7 3 5 2 , 0 . 0 7 0 1 2 1 7 8 9 1 ) ^ { t }$ and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 0 . 1 4 5$   
\*(b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 9 9 3 1 2 9 5 1 0 , 0 . 9 6 4 2 7 3 4 4 5 5 , 0 . 7 7 8 4 2 6 6 5 7 7 ) ^ { t } { \mathrm { a n d } } \left\| \mathbf { r } ^ { ( 2 ) } \right\| _ { \infty }$ $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 0 . 1 4 4$   
(c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 3 3 6 5 8 0 2 6 2 5 , 2 . 1 2 9 6 9 3 1 8 9 , - 0 . 7 6 0 0 3 9 5 5 8 0 , 2 . 7 0 3 1 9 6 8 1 4 ) ^ { t } \sin ^ { 2 } { \delta }$ nd $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 2 . 3 5$   
(d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 9 2 7 7 2 1 5 6 4 , - 0 . 3 7 9 1 9 6 8 2 3 3 , - 0 . 0 2 6 4 9 9 4 3 8 2 7 , 0 . 0 1 9 7 7 2 7 2 8 3 ) ^ { \circ }$ t and $\left\| \mathbf { r } ^ { ( 2 ) } \right\| _ { \infty } =$ 0.146   
(e) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 4 4 1 4 2 4 8 5 7 6 , 0 . 8 0 8 9 2 7 6 5 0 0 , 1 . 4 6 3 7 6 0 2 0 0 , 1 . 7 3 0 5 3 7 7 2 1 , 1 . 8 9 5 8 0 8 6 0 0 ) ^ { t } { \mathrm { a n d } }$ $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } =$ 1.06   
(f) x(2) = (1.022375670, 1.686451892, 1.022375670, 2.060919568, 0.8310997753, 2.060919568)t and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 1 . 1 3$

7. The Conjugate Gradient method with $C = C ^ { - 1 } = I$ gives the following:

(a) $\mathfrak { c } ^ { ( 3 ) } = ( 0 . 0 6 1 8 5 5 6 7 0 1 3 , - 0 . 1 9 5 8 7 6 2 8 8 7 , 0 . 6 1 8 5 5$ 67010)t and $\| \mathbf { r } ^ { ( 3 ) } \| _ { \infty } = 0 . 4 \times 1 0 ^ { - 9 }$ .   
\*(b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 9 9 5 7 8 9 4 7 3 8 , 0 . 9 5 7 8 9 4 7 3 6 9 , 0 . 7 9 1 5 7 8 9 4 7 4 ) ^ { t }$ and $\| \mathbf { r } ^ { ( 3 ) } \| _ { \infty } = 0 . 1 \times 1 0 ^ { - 9 }$ .   
(c) $\mathbf { x } ^ { ( 4 ) } = ( - 0 . 7 9 7 6 4 7 0 5 7 9 , 2 . 7 9 5 2 9 4 1 2 0 , - 0 . 2 5 8 8 2 3 5 3 0 5 , - 2 . 2 5 1 7 6 4 7 0 6 ) ^ { t } \mathrm { a }$ nd $\| \mathbf { r } ^ { ( 4 ) } \| _ { \infty } = 0 . 3 9 \times$ $1 0 ^ { - 7 }$ .   
(d) $\mathbf { x } ^ { ( 4 ) } \ = \ ( - 0 . 7 5 3 4 2 4 6 5 7 5 , 0 . 0 4 1 0 9 5 8 9 0 3 9 , - 0 . 2 8 0 8 2 1 9 1 7 9 , 0 . 6 9 1 7 8 0 8 2 1 9 ) ^ { t }$ and $\| \mathbf { r } ^ { ( 4 ) } \| _ { \infty } =$ 0.11  10−9.   
(e) $\mathbf { x } ^ { ( 5 ) } = ( 0 . 4 5 1 6 1 2 9 0 3 2 , 0 . 7 0 9 6 7 7 4 1 9 7 , 1 . 6 7 7 4 1 9 3 5 5 , 1 . 7 4 1 9 3 5 4 8 3 , 1 . 8 0 6 4 5 1 6 1 3 ) ^ { t } \mathrm { a n d } \mathbf { x } ^ { ( 5 ) }$ nd $\| \mathbf { r } ^ { ( 5 ) } \| _ { \infty } =$ $0 . 2 \times 1 0 ^ { - 9 }$ .

(f) $\mathbf { x } ^ { ( 4 ) } = ( 1 . 0 0 0 0 0 0 0 0 0 0 0 , 2 . 0 0 0 0 0 0 0 0 0 0 , 1 . 0 0 0 0 0 0 0 0 0 0 , 2 . 0 0 0 0 0 0 0 0 0 0 , 0 . 9 9 9 9 9 9 9$ 9997, 2.000000000)t and $\| \mathbf { r } ^ { ( 4 ) } \| _ { \infty } = 0 . 4 4 \times 1 0 ^ { - 9 }$ .

8. The Conjugate Gradient method with $C ^ { - 1 } = D ^ { - 1 / 2 }$ gives the following:

(a) x(3) = (0.06185567019, −0.1958762885, 0.6185567006)t and $\left\| \mathbf { r } ^ { ( 3 ) } \right\| _ { \infty } = 0 . 1 2 \times 1 0 ^ { - 8 }$   
\*(b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 9 9 5 7 8 9 4 7 3 9 , 0 . 9 5 7 8 9 4 7 3 6 8 , 0 . 7 9 1 5 7 8 9 4 7 5 ) ^ { t }$ and $\left\| \mathbf { r } ^ { ( 3 ) } \right\| _ { \infty } = 0 . 1 9 \times 1 0 ^ { - 8 }$   
(c) x(4) = (−0.7976470596, 2.795294118, −0.2588235287, −2.251764706)t and $\left\| \mathbf { r } ^ { ( 4 ) } \right\| _ { \infty } = 0 . 7 \times$ $1 0 ^ { - 8 }$   
(d) $\mathbf { x } ^ { ( 4 ) } = ( 0 . 6 1 6 4 3 8 3 5 6 0 , - 0 . 3 9 7 2 6 0 2 7 4 2 , 0 . 0 4 7 9 4 5 2 0 5 5 0 , - 0 . 0 2 0 5 4 7 9 4 5 2 5 ) ^ { t }$ and $\left\| \mathbf { r } ^ { ( 4 ) } \right\| _ { \infty } =$ 0.76 × 10−9   
(e) x(5) = (0.4516129026, 0.7096774190, 1.677419356, 1.741935484, 1.806451615)t and $\left\| \mathbf { r } ^ { ( 5 ) } \right\| _ { \infty } =$ $0 . 6 1 \times 1 0 ^ { - 1 0 }$   
(f) $\mathfrak { c } ^ { ( 4 ) } = ( 0 . 9 9 9 9 9 9 9 9 9 2 , 1 . 9 9 9 9 9 9 9 9 9 9 , 0 . 9 9 9 9 9 9 9 9 9 9 \mathfrak { c }$ 92, 2.000000000, 0.9999999989, 2.000000000)t and $\left\| \mathbf { r } ^ { ( 4 ) } \right\| _ { \infty } = 0 . 1 1 \times 1 0 ^ { - 9 }$

9. Approximations to within $1 0 ^ { - 5 }$ in the $l _ { i n f t y }$ are shown in the tables.

<table><tr><td>(a)</td><td>Jacobi 49 iterations</td><td>Gauss-Seidel 28 iterations</td><td>SOR (ω = 1.3) 13 iterations</td><td>Conjugate Gradient 9 iterations</td></tr><tr><td>x1</td><td>0.93406183</td><td>0.93406917</td><td>0.93407584</td><td>0.93407713</td></tr><tr><td>x2</td><td>0.97473885</td><td>0.97475285</td><td>0.97476180</td><td>0.97476363</td></tr><tr><td>x3</td><td>1.10688692</td><td>1.10690302</td><td>1.10691093</td><td>1.10691243</td></tr><tr><td>X4</td><td>1.42346150</td><td>1.42347226</td><td>1.42347591</td><td>1.42347699</td></tr><tr><td>X5</td><td>0.85931331</td><td>0.85932730</td><td>0.85933633</td><td>0.85933790</td></tr><tr><td>X6</td><td>0.80688119</td><td>0.80690725</td><td>0.80691961</td><td>0.80692197</td></tr><tr><td>X7</td><td>0.85367746</td><td>0.85370564</td><td>0.85371536</td><td>0.85372011</td></tr><tr><td>x8</td><td>1.10688692</td><td>1.10690579</td><td>1.10691075</td><td>1.10691250</td></tr><tr><td>xg</td><td>0.87672774</td><td>0.87674384</td><td>0.87675177</td><td>0.87675250</td></tr><tr><td>X10</td><td>0.80424512</td><td>0.80427330</td><td>0.80428301</td><td>0.80428524</td></tr><tr><td>X11</td><td>0.80688119</td><td>0.80691173</td><td>0.80691989</td><td>0.80692252</td></tr><tr><td>X12</td><td>0.97473885</td><td>0.97475850</td><td>0.97476265</td><td>0.97476392</td></tr><tr><td>X13</td><td>0.93003466</td><td>0.93004542</td><td>0.93004899</td><td>0.93004987</td></tr><tr><td>X14</td><td>0.87672774</td><td>0.87674661</td><td>0.87675155</td><td>0.87675298</td></tr><tr><td>X15</td><td>0.85931331</td><td>0.85933296</td><td>0.85933709</td><td>0.85933979</td></tr><tr><td>X16</td><td>0.93406183</td><td>0.93407462</td><td>0.93407672</td><td>0.93407768</td></tr><tr><td>(b)</td><td>Jacobi 60 iterations</td><td>Gauss-Seidel 35 iterations</td><td>SOR (ω = 1.2) 23 iterations</td><td>Conjugate Gradient 11 iterations</td></tr><tr><td>x1</td><td>0.39668038</td><td>0.39668651</td><td>0.39668915</td><td>0.39669775</td></tr><tr><td>x2</td><td>0.07175540</td><td>0.07176830</td><td>0.07177348</td><td>0.07178516</td></tr><tr><td>x3</td><td>-0.23080396</td><td>-0.23078609</td><td>-0.23077981</td><td>-0.23076923</td></tr><tr><td>X4</td><td>0.24549277</td><td>0.24550989</td><td>0.24551535</td><td>0.24552253</td></tr><tr><td>x5</td><td>0.83405412</td><td>0.83406516</td><td>0.83406823</td><td>0.83407148</td></tr><tr><td>X6</td><td>0.51497606</td><td>0.51498897</td><td>0.51499414</td><td>0.51500583</td></tr><tr><td>X7</td><td>0.12116003</td><td>0.12118683</td><td>0.12119625</td><td>0.12121212</td></tr><tr><td>x8</td><td>-0.24044414</td><td>-0.24040991</td><td>-0.24039898</td><td>-0.24038462</td></tr><tr><td>x9</td><td>0.37873579</td><td>0.37876891</td><td>0.37877812</td><td>0.37878788</td></tr><tr><td>X10</td><td>1.09073364</td><td>1.09075392</td><td>1.09075899</td><td>1.09076341</td></tr><tr><td>X11</td><td>0.54207872</td><td>0.54209658</td><td>0.54210286</td><td>0.54211344</td></tr><tr><td>X12</td><td>0.13838259</td><td>0.13841682</td><td>0.13842774</td><td>0.13844211</td></tr><tr><td>X13</td><td>-0.23083868</td><td>-0.23079452</td><td>-0.23078224</td><td>-0.23076923</td></tr><tr><td></td><td>0.41919067</td><td>0.41923122</td><td>0.41924136</td><td></td></tr><tr><td>X14</td><td>1.15015953</td><td></td><td>1.15019025</td><td>0.41925019</td></tr><tr><td>X15</td><td></td><td>1.15018477</td><td></td><td>1.15019425</td></tr><tr><td>X16</td><td>0.51497606 0.12116003</td><td>0.51499318</td><td>0.51499864</td><td>0.51500583</td></tr><tr><td>X17</td><td>-0.24044414</td><td>0.12119315</td><td>0.12120236</td><td>0.12121212</td></tr><tr><td>X18</td><td></td><td>-0.24040359</td><td>-0.24039345</td><td>-0.24038462</td></tr><tr><td>X19</td><td>0.37873579</td><td>0.37877365</td><td>0.37878188</td><td>0.37878788</td></tr><tr><td>X20</td><td>1.09073364</td><td>1.09075629</td><td>1.09076069</td><td>1.09076341</td></tr><tr><td>X21</td><td>0.39668038</td><td>0.39669142</td><td>0.39669449</td><td>0.39669775</td></tr><tr><td>X22</td><td>0.07175540</td><td>0.07177567</td><td>0.07178074</td><td>0.07178516</td></tr><tr><td>X23</td><td>-0.23080396</td><td>-0.23077872</td><td>-0.23077323 0.24551982</td><td>-0.23076923</td></tr><tr><td>X24</td><td>0.24549277</td><td>0.24551542</td><td></td><td>0.24552253</td></tr><tr><td>X25</td><td>0.83405412</td><td>0.83406793</td><td>0.83407025</td><td>0.83407148</td></tr><tr><td>(c）</td><td>Jacobi 15</td><td>Gauss-Seidel 9</td><td>SOR (ω = 1.1) 8</td><td>Conjugate Gradient 8</td></tr><tr><td></td><td>iterations</td><td>iterations</td><td>iterations</td><td>iterations</td></tr><tr><td>X1</td><td>-3.07611424</td><td>-3.07611739</td><td>-3.07611796</td><td>-3.07611794</td></tr><tr><td>X2</td><td>-1.65223176</td><td>-1.65223563</td><td>-1.65223579</td><td>-1.65223582</td></tr><tr><td>X3</td><td>-0.53282391</td><td>-0.53282528</td><td>-0.53282531</td><td>-0.53282528</td></tr><tr><td>X4</td><td>-0.04471548</td><td>-0.04471608</td><td>-0.04471609</td><td>-0.04471604</td></tr><tr><td>x5</td><td>0.17509673</td><td>0.17509661</td><td>0.17509661</td><td>0.17509661</td></tr><tr><td>X6</td><td>0.29568226</td><td>0.29568223</td><td>0.29568223</td><td>0.29568218</td></tr><tr><td>X7</td><td>0.37309012</td><td>0.37309011</td><td>0.37309011</td><td>0.37309011</td></tr><tr><td>X8</td><td>0.42757934</td><td>0.42757934</td><td>0.42757934</td><td>0.42757927</td></tr><tr><td>xg</td><td>0.46817927</td><td>0.46817927</td><td>0.46817927</td><td>0.46817927</td></tr><tr><td>X10</td><td>0.49964748</td><td>0.49964748</td><td>0.49964748</td><td>0.49964748</td></tr><tr><td>X11</td><td>0.52477026</td><td>0.52477026</td><td>0.52477026</td><td>0.52477027</td></tr><tr><td>X12</td><td>0.54529835</td><td>0.54529835</td><td>0.54529835</td><td>0.54529836</td></tr><tr><td>X13</td><td>0.56239007</td><td>0.56239007</td><td>0.56239007</td><td>0.56239009</td></tr><tr><td>X14</td><td>0.57684345</td><td>0.57684345</td><td>0.57684345</td><td>0.57684347</td></tr><tr><td>X15</td><td>0.58922662</td><td>0.58922662</td><td>0.58922662</td><td>0.58922664</td></tr><tr><td>X16</td><td>0.59995522</td><td>0.59995522</td><td>0.59995522</td><td>0.59995523</td></tr><tr><td>X17</td><td>0.60934045 0.61761997</td><td>0.60934045</td><td>0.60934045</td><td>0.60934045</td></tr><tr><td>X18</td><td></td><td>0.61761997</td><td>0.61761997</td><td>0.61761998</td></tr><tr><td>X19</td><td>0.62497846</td><td>0.62497846</td><td>0.62497846</td><td>0.62497847</td></tr><tr><td>X20</td><td>0.63156161 0.63748588</td><td>0.63156161</td><td>0.63156161</td><td>0.63156161</td></tr><tr><td>X21</td><td></td><td>0.63748588</td><td>0.63748588</td><td>0.63748588</td></tr><tr><td>X22</td><td>0.64284553</td><td>0.64284553</td><td>0.64284553</td><td>0.64284553</td></tr><tr><td>X23</td><td>0.64771764</td><td>0.64771764</td><td>0.64771764</td><td>0.64771764</td></tr><tr><td>X24</td><td>0.65216585</td><td>0.65216585</td><td>0.65216585</td><td>0.65216585</td></tr><tr><td>X25</td><td>0.65624320</td><td>0.65624320</td><td>0.65624320</td><td>0.65624320</td></tr><tr><td>X26</td><td>0.65999423</td><td>0.65999423</td><td>0.65999423</td><td>0.65999422</td></tr><tr><td>X27</td><td>0.66345660</td><td>0.66345660</td><td>0.66345660</td><td>0.66345660</td></tr><tr><td>X28</td><td>0.66666242</td><td>0.66666242</td><td>0.66666242</td><td>0.66666242</td></tr><tr><td>X29</td><td>0.66963919</td><td>0.66963919</td><td>0.66963919</td><td>0.66963919</td></tr><tr><td>x30</td><td>0.67241061</td><td>0.67241061</td><td>0.67241061</td><td>0.67241060</td></tr><tr><td>x31</td><td>0.67499722</td><td>0.67499722</td><td>0.67499722</td><td>0.67499721</td></tr><tr><td>X32</td><td>0.67741692</td><td>0.67741692</td><td>0.67741691</td><td>0.67741691</td></tr><tr><td>X33</td><td>0.67968535</td><td>0.67968535</td><td>0.67968535</td><td>0.67968535</td></tr><tr><td>X34</td><td>0.68181628</td><td>0.68181628</td><td>0.68181628</td><td>0.68181628</td></tr><tr><td>X35</td><td>0.68382184</td><td>0.68382184</td><td>0.68382184</td><td>0.68382184</td></tr><tr><td>X36</td><td>0.68571278</td><td>0.68571278</td><td>0.68571278</td><td>0.68571278</td></tr><tr><td>X37</td><td>0.68749864</td><td>0.68749864</td><td>0.68749864</td><td>0.68749864</td></tr><tr><td>x38</td><td>0.68918652</td><td>0.68918652</td><td>0.68918652</td><td>0.68918652</td></tr><tr><td>X39</td><td>0.69067718</td><td>0.69067718</td><td>0.69067718</td><td>0.69067717</td></tr><tr><td>X40</td><td>0.68363346</td><td>0.68363346</td><td>0.68363346</td><td>0.68363349</td></tr></table>

10. $n = 1 0$ : The solution vector is (0.90909091, 0.81818182, 0.72727273, 0.63636364, 0.54545455, 0.45454545, 0.36363636, 0.27272727, 0.18181818, 0.09090909)t, using 10 iterations with $\left\| \mathbf { r } ^ { ( 1 0 ) } \right\| _ { \infty } = 0$ .

$n = 5 0$ : The solution vector is

(0.98039216, 0.96078432, 0.94117648, 0.92156863, 0.90196079, 0.88235295, 0.86274511, 0.84313727, 0.82352943, 0.80392158, 0.78431374, 0.76470590, 0.74509806, 0.72549021, 0.70588237, 0.68627453, $0 . 6 6 6 6 6 6 6 6 8 8 , \ 0 . 6 4 7 0 5 8 8 4 , \ 0 . 6 5 2 7 4 5 1 0 1 0 , \ 0 . 6 0 7 8 4 3 1 5 , \ 0 . 5 8 8 2 3 5 3 3 1 , \ 0 . 5 6 8 6 2 7 4 7 , \ 0 . 5 4 9 0 1 9 6 2 , \ 0 . 5 2 9 9 2$ 41178, 0.50980394, 0.49019609, 0.47058825, 0.45098041, 0.43137256, 0.41176472, 0.39215688, 0.37254903, 0.35294119, 0.33333335, 0.31372550, 0.29411766, 0.27450981, 0.25490197, 0.23529413, 0.21568628, 0.19607844, 0.17647060, 0.15686275, 0.13725491, 0.11764706, 0.09803922, 0.07843138, 0.05882353, 0.03921569, 0.01960784)t, using 50 iterations with a tolerance $1 . 0 0 \times 1 0 ^ { - 3 }$ in $l _ { \infty }$ and $\| \mathbf { r } ^ { ( 5 0 ) } \| _ { \infty } = 0$ .

$n = 1 0 0$ : The solution vector is

(0.99009901, 0.98019803, 0.97029704, 0.96039606, 0.95049507, 0.94059409, 0.93069310, 0.92079212,   
0.91089113, 0.90099014, 0.89108916, 0.88118817, 0.87128718, 0.86138620, 0.85148521, 0.84158422,   
0.83168323, 0.82178225, 0.81188126, 0.80198027, 0.79207928, 0.78217830, 0.77227731, 0.76237632,   
0.75247533, 0.74257434, 0.73267335, 0.72277237, 0.71287138, 0.70297039, 0.69306940, 0.68316841,   
0.67326742, 0.66336643, 0.65346544, 0.64356445, 0.63366347, 0.62376248, 0.61386149, 0.60396050,   
0.59405951, 0.58415852, 0.57425753, 0.56435654, 0.55445555, 0.54455456, 0.53465357, 0.52475258,   
0.51485159, 0.50495059, 0.49504960, 0.48514861, 0.47524762, 0.46534663, 0.45544564, 0.44554465,   
0.43564366, 0.42574267, 0.41584168, 0.40594068, 0.39603969, 0.38613870, 0.37623771, 0.36633672,   
0.3 $) 6 4 3 5 7 ( 3 , 0 . 3 4 6 5 3 4 / ( 4 , 0 . 3 3 6 6 3 3 / ( 4 , 0 . 3 3 2 6 / 3 2 7 ( 3 ) , 0 . 3 1 6 8 3 1 / ( 6 , 0 . 3 3 0 6 9 3 3 0 / ( , 0 . 2 9 ( 0 2 9 / 8 ) , 0 . 2 8 ( 1 . 2 8 ( 9 ) 9 ) )$   
0.2 $/ ( 2 2 2 / ( 9 , 0 . 2 2 6 / 3 2 6 8 0 , 0 . 2 5 ) / 4 2 5 8 8 1 , 0 . 2 4 / 3 2 4 8 2 , 0 . 2 3 / 6 2 3 8 3 , 0 . 2 2 / ( 7 2 2 8 3 , 0 . 2 1 / 8 2 1 8 4 , 0 . 2 0 / 9 2 0 8 3 ) ,$   
0.1 $)  \mathrm { S G I . S N S 6 , ~ 0 . 1 . N S K . I . N S S 6 , ~ 0 . 1 \cdot ( N Z 2 1 ^ { \prime } ( 8 ^ { \prime } , 0 . 1 6 8 3 4 1 6 8 8 , 0 . 1 5 3 8 4 1 5 8 5 9 , 0 . 1 4 8 5 1 . 4 8 5 ) . 1 4 8 5 9 , 0 . 1 . 3 3 8 6 1 3 9 0 , 0 . 1 . 2 8 ( 1 . 2 9 1 1 , 0 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 . 0 5 ) }$   
0.11881192, 0.10891092, 0.09900993, 0.08910894, 0.07920794, 0.06930695, 0.05940596, 0.04950497,   
0.03960397, 0.02970298, 0.01980199, 0.00990099)t,

using 100 iterations with a tolerance $1 . 0 0 \times 1 0 ^ { - 3 }$ in ${ \mathit { l } } _ { \infty }$ and $\left\| \mathbf { r } ^ { ( 1 0 0 ) } \right\| _ { \infty } = 0$

11. The Conjugate Gradient method gives the results in the following tables.

(a)

<table><tr><td>Solution</td><td>Residual</td></tr><tr><td>2.55613420</td><td>0.00668246</td></tr><tr><td>4.09171393</td><td>-0.00533953</td></tr><tr><td>4.60840390</td><td>-0.01739814</td></tr><tr><td>3.64309950</td><td>-0.03171624</td></tr><tr><td>5.13950533</td><td>0.01308093</td></tr><tr><td>7.19697808</td><td>-0.02081095</td></tr><tr><td>7.68140405</td><td>-0.04593118</td></tr><tr><td>5.93227784</td><td>0.01692180</td></tr><tr><td>5.81798997</td><td>0.04414047</td></tr><tr><td>5.85447806</td><td>0.03319707</td></tr><tr><td>5.94202521</td><td>-0.00099947</td></tr><tr><td>4.42152959</td><td>-0.00072826</td></tr><tr><td></td><td></td></tr><tr><td>3.32211695</td><td>0.02363822</td></tr><tr><td>4.49411604</td><td>0.00982052</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td>4.80968966</td><td>0.00846967</td></tr><tr><td></td><td></td></tr><tr><td>3.81108707</td><td>-0.01312902</td></tr></table>

This converges in 6 iterations with tolerance $5 . 0 0 \times 1 0 ^ { - 2 }$ in the ${ \mathit { l } } _ { \infty }$ norm and $\| \mathbf { r } ^ { ( 6 ) } \| _ { \infty } =$ 0.046.

(b)

<table><tr><td>Solution</td><td>Residual</td></tr><tr><td>2.55613420</td><td>0.00668246</td></tr><tr><td>4.09171393</td><td>-0.00533953</td></tr><tr><td>4.60840390</td><td>-0.01739814</td></tr><tr><td>3.64309950</td><td>-0.03171624</td></tr><tr><td>5.13950533</td><td>0.01308093</td></tr><tr><td>7.19697808</td><td>-0.02081095</td></tr><tr><td>7.68140405</td><td>-0.04593118</td></tr><tr><td>5.93227784</td><td>0.01692180</td></tr><tr><td>5.81798996</td><td>0.04414047</td></tr><tr><td>5.85447805</td><td>0.03319706</td></tr><tr><td>5.94202521</td><td>-0.00099947</td></tr><tr><td>4.42152959</td><td>-0.00072826</td></tr><tr><td>3.32211694</td><td>0.02363822</td></tr><tr><td></td><td></td></tr><tr><td>4.49411603</td><td>0.00982052</td></tr><tr><td>4.80968966</td><td>0.00846967</td></tr><tr><td></td><td></td></tr><tr><td>3.81108707</td><td>-0.01312902</td></tr></table>

This converges in 6 iterations with tolerance $5 . 0 0 \times 1 0 ^ { - 2 }$ in the ${ \mathit { l } } _ { \infty }$ norm and $\| \mathbf { r } ^ { ( 6 ) } \| _ { \infty } =$ 0.046.

(c) All tolerances lead to the same convergence specifications.

$^ { \ast } 1 2$ . With $\langle \mathbf { x } , \mathbf { y } \rangle = \mathbf { x } ^ { t } \mathbf { y }$ , we have

$$
\langle \mathbf { x } , \mathbf { y } \rangle = \mathbf { x } ^ { t } \mathbf { y } = \mathbf { y } ^ { t } \mathbf { x } = \langle \mathbf { y } , \mathbf { x } \rangle ;
$$

$$
\langle c \mathbf { x } , \mathbf { y } \rangle = ( c \mathbf { x } ) ^ { t } \mathbf { y } = c \mathbf { x } ^ { t } \mathbf { y } = c \langle \mathbf { x } , \mathbf { y } \rangle = \mathbf { x } ^ { t } c \mathbf { y } = \langle \mathbf { x } , c \mathbf { y } \rangle ;
$$

$$
\langle \mathbf { x } + \mathbf { z } , \mathbf { y } \rangle = ( \mathbf { x } + \mathbf { z } ) ^ { t } \mathbf { y } = \left( \mathbf { x } ^ { t } + \mathbf { z } ^ { t } \right) \mathbf { y } = \mathbf { x } ^ { t } \mathbf { y } + \mathbf { z } ^ { t } \mathbf { y } = \langle \mathbf { x } , \mathbf { y } \rangle + \langle \mathbf { z } , \mathbf { y } \rangle ;
$$

$$
\langle \mathbf { x } , \mathbf { x } \rangle = \mathbf { x } ^ { t } \mathbf { x } = \| \mathbf { x } \| _ { 2 } ^ { 2 } \geq 0 .
$$

We show (v) as follows:

If $\langle \mathbf { x } , \mathbf { x } \rangle = \| \mathbf { x } \| _ { 2 } ^ { 2 } = 0$ , then $\mathbf x = \mathbf 0$ by the properties of norms. If $\mathbf x = \mathbf 0$ , then $0 = \mathbf { x } ^ { t } \mathbf { x } = \langle \mathbf { x } , \mathbf { x } \rangle$ .

13. (a) Let $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ be a set of nonzero $A$ -orthogonal vectors for the symmetric positive definite matrix $A$ . Then $\langle \mathbf { v } ^ { ( i ) } , A \mathbf { v } ^ { ( j ) } \rangle = 0$ , if $i \neq j$ . Suppose

$$
c _ { 1 } \mathbf { v } ^ { ( 1 ) } + c _ { 2 } \mathbf { v } ^ { ( 2 ) } + \cdot \cdot \cdot + c _ { n } \mathbf { v } ^ { ( n ) } = \mathbf { 0 } ,
$$

where not all $c _ { i }$ are zero. Suppose $k$ is the smallest integer for which $c _ { k } \neq 0$ . Then

$$
c _ { k } \mathbf { v } ^ { ( k ) } + c _ { k + 1 } \mathbf { v } ^ { ( k + 1 ) } + \cdot \cdot \cdot + c _ { n } \mathbf { v } ^ { ( n ) } = \mathbf { 0 } .
$$

We solve for $\mathbf { v } ^ { ( k ) }$ to obtain

$$
\mathbf { v } ^ { ( k ) } = - { \frac { c _ { k + 1 } } { c _ { k } } } \mathbf { v } ^ { ( k + 1 ) } - \cdot \cdot \cdot - { \frac { c _ { n } } { c _ { k } } } \mathbf { v } ^ { ( n ) } .
$$

Multiplying by $A$ gives

$$
A \mathbf { v } ^ { ( k ) } = - { \frac { c _ { k + 1 } } { c _ { k } } } A \mathbf { v } ^ { ( k + 1 ) } - \cdot \cdot \cdot - { \frac { c _ { n } } { c _ { k } } } A \mathbf { v } ^ { ( n ) } ,
$$

so

$$
\begin{array} { r c l } { ( { \mathbf v } ^ { ( k ) } ) ^ { t } A { \mathbf v } ^ { ( k ) } } & { = } & { - \frac { c _ { k + 1 } } { c _ { k } } ( { \mathbf v } ^ { ( k ) } ) ^ { t } A { \mathbf v } ^ { ( k + 1 ) } - \cdot \cdot \cdot - \frac { c _ { n } } { c _ { k } } ( { \mathbf v } ^ { ( k ) t } ) A { \mathbf v } ^ { ( n ) } } \\ & { = } & { - \frac { c _ { k + 1 } } { c _ { k } } \langle { \mathbf v } ^ { ( k ) } , A { \mathbf v } ^ { ( k + 1 ) } \rangle - \cdot \cdot \cdot - \frac { c _ { n } } { c _ { k } } \langle { \mathbf v } ^ { ( k ) } , A { \mathbf v } ^ { ( n ) } \rangle } \\ & { = } & { - \frac { c _ { k + 1 } } { c _ { k } } \cdot 0 - \cdot \cdot \cdot - \frac { c _ { n } } { c _ { k } } \cdot 0 = 0 . } \end{array}
$$

Since $A$ is positive definite, $\mathbf { v } ^ { ( k ) } = \mathbf { 0 }$ , which is a contradiction. Thus, all the $c _ { i }$ must be zero, and $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ is linearly independent.

(b) Let $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ be a set of nonzero $A$ -orthogonal vectors for the symmetric positive definite matrix $A$ , and let $\mathbf { z }$ be orthogonal to $\mathbf { v } ^ { ( i ) }$ , for each $i = 1 , \ldots , n$ . From part (a), the set $\{ \mathbf { v } ^ { ( 1 ) } , \ldots \mathbf { v } ^ { ( n ) } \}$ is linearly independent, so there is a collection of constants $\beta _ { 1 } , \ldots , \beta _ { n }$ with

$$
\mathbf { z } = \sum _ { i = 1 } ^ { n } \beta _ { i } \mathbf { v } ^ { ( i ) } .
$$

Hence,

$$
\langle \mathbf { z } , \mathbf { z } \rangle = \mathbf { z } ^ { t } \mathbf { z } = \sum _ { i = 1 } ^ { n } \beta _ { i } \mathbf { z } ^ { t } \mathbf { v } ^ { ( i ) } = \sum _ { i = 1 } ^ { n } \beta _ { i } \cdot 0 = 0 ,
$$

and Theorem 7.30, part (e), implies that $\mathbf { z } = \mathbf { 0 }$ .

\*14. To prove Theorem 7.33 by mathematical induction:

(a) First note that we have

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } + t _ { 1 } \mathbf { v } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } + \frac { \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. } { \left. \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 1 ) } \right. } \mathbf { v } ^ { ( 1 ) } .
$$

Thus

$$
A \mathbf { x } ^ { ( 1 ) } = A \mathbf { x } ^ { ( 0 ) } + \frac { \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. } { \left. \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 1 ) } \right. } A \mathbf { v } ^ { ( 1 ) }
$$

and

$$
{ \bf b } - A { \bf x } ^ { ( 1 ) } = { \bf b } - A { \bf x } ^ { ( 0 ) } - \frac { \left. { \bf v } ^ { ( 1 ) } , { \bf r } ^ { ( 0 ) } \right. } { \left. { \bf v } ^ { ( 1 ) } , A { \bf v } ^ { ( 1 ) } \right. } A { \bf v } ^ { ( 1 ) } .
$$

Hence,

$$
\mathbf { r } ^ { ( 1 ) } = \mathbf { r } ^ { ( 0 ) } - \frac { \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. } { \left. \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 1 ) } \right. } A \mathbf { v } ^ { ( 1 ) } .
$$

Taking the inner product with $\mathbf { v } ^ { ( 1 ) }$ gives

$$
\begin{array} { r l } & { \left. \mathbf { r } ^ { ( 1 ) } , \mathbf { v } ^ { ( 1 ) } \right. = \left. \mathbf { r } ^ { ( 0 ) } , \mathbf { v } ^ { ( 1 ) } \right. - \frac { \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. } { \left. \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 1 ) } \right. } \left. A \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 1 ) } \right. } \\ & { \qquad = \left. \mathbf { r } ^ { ( 0 ) } , \mathbf { v } ^ { ( 1 ) } \right. - \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. = 0 . } \end{array}
$$

This establishes the base step.

(b) For the inductive hypothesis we assume that $\left. \mathbf { r } ^ { ( k ) } , \mathbf { v } ^ { ( j ) } \right. = 0$ , for all $k \ \leq \ l$ and $j ~ =$ $1 , 2 , \ldots , k$ . We must then show

$$
\left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( j ) } \right. = 0 , \quad \mathrm { f o r } \quad j = 1 , 2 , \ldots , l + 1 .
$$

We do this in two parts.

First, for $j = 1 , 2 , \dots , l$ , we will show that $\left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( j ) } \right. = 0$ . We have

$$
\begin{array} { r l } & { \mathbf { x } ^ { ( l + 1 ) } = \mathbf { x } ^ { ( l ) } + t _ { l + 1 } \mathbf { v } ^ { ( l + 1 ) } } \\ & { \quad \quad = \mathbf { x } ^ { ( l ) } + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } \mathbf { v } ^ { ( l + 1 ) } , } \end{array}
$$

so

$$
A \mathbf { x } ^ { ( l + 1 ) } = A \mathbf { x } ^ { ( l ) } + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } A \mathbf { v } ^ { ( l + 1 ) } .
$$

Subtracting $\mathbf { b }$ from both sides gives

$$
- \mathbf { r } ^ { ( l + 1 ) } = - \mathbf { r } ^ { ( l ) } + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } A \mathbf { v } ^ { ( l + 1 ) } .
$$

Taking the inner product of both sides of (2) with $\mathbf { v } ^ { ( i ) }$ gives

$$
- \left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( i ) } \right. = - \left. \mathbf { r } ^ { ( l ) } , \mathbf { v } ^ { ( i ) } \right. + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } \left. A \mathbf { v } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( i ) } \right. .
$$

The first term on the right-hand side of (3) is $0$ by the inductive hypothesis, and the factor $\left. A \mathbf { v } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( i ) } \right.$ is $0$ because of $A$ -orthogonality. Thus, $\left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( i ) } \right. = 0$ , for $1 , 2 , \ldots , l$ .

(c) For the second part we take the inner product of both sides of (2) with $\mathbf { v } ^ { ( l + 1 ) }$ to obtain

$$
- \left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( l + 1 ) } \right. = - \left. \mathbf { r } ^ { ( l ) } , \mathbf { v } ^ { ( l + 1 ) } \right. + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } \left. A \mathbf { v } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( l + 1 ) } \right. .
$$

Thus,

$$
- \left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( l + 1 ) } \right. = - \left. \mathbf { r } ^ { ( l ) } , \mathbf { v } ^ { ( l + 1 ) } \right. + \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. = 0 .
$$

This completes the proof by induction.

15. If $A$ is a positive definite matrix whose eigenvalues are $0 < \lambda _ { 1 } \leq \cdot \cdot \cdot \leq \lambda _ { n }$ , then $| | { \cal { A } } | | _ { 2 } = \lambda _ { n }$ and $| | A ^ { - 1 } | | _ { 2 } = 1 / \lambda _ { 1 }$ , so $K _ { 2 } ( A ) = \lambda _ { n } / \lambda _ { 1 }$ .

For the matrix $A$ in Example 3 we have

$$
K _ { 2 } ( A ) = { \frac { \lambda _ { 5 } } { \lambda _ { 1 } } } = { \frac { 7 0 0 . 0 3 1 } { 0 . 0 5 7 0 7 3 7 } } = 1 2 2 6 5 . 2 ,
$$

and the matrix $A H$ has

$$
K _ { 2 } ( A H ) = { \frac { \lambda _ { 5 } } { \lambda _ { 1 } } } = { \frac { 1 . 8 8 0 5 2 } { 0 . 1 5 6 3 7 0 } } = 1 2 . 0 2 6 1 .
$$

Maple gives ConditionNumber $\mathbf { \sigma } \cdot ( A , 2 ) = 1 2 2 6 5 . 1 5 9 1 4$ and ConditionNumber $\cdot ( A H , 2 ) = 1 2 . 0 2 5 9 8 1 2 4$

# Approximation Theory

# Exercise Set 8.1, page 506

$^ { * } 1$ . The linear least-squares polynomial is $1 . 7 0 7 8 4 x + 0 . 8 9 9 6 8$ .   
$^ { * 2 }$ . The least-squares polynomial of degree two is $P _ { 2 } ( x ) = 0 . 4 0 6 6 6 6 7 + 1 . 1 5 4 8 4 8 x + 0 . 0 3 4 8 4 8 4 8 x ^ { . }$ 2, with $E = 1 . 7 0 3 5$ .   
3. The least-squares polynomials with their errors are, respectively, $0 . 6 \dot { 2 } 0 8 9 5 0 + 1 . 2 1 9 6 \dot { 2 } 1 x$ , with $E = 2 . 7 1 9 \times 1 0 ^ { - 5 }$ ; $0 . 5 9 6 5 8 0 7 + 1 . 2 5 3 2 9 3 x - 0 . 0 1 0 8 5 3 4 3 x ^ { 2 }$ , with $E = 1 . 8 0 1 \times 1 0 ^ { - 5 }$ ; and 0.629019 $3 + 1 . 1 8 5 0 1 0 x + 0 . 0 3 5 3 3 2 5 2 x ^ { 2 } - 0 . 0 1 0 0 4 7 2 3 x ^ { 3 }$ , with $E = 1 . 7 4 1 \times 1 0 ^ { - 5 }$ .   
4. The least-squares polynomials with their errors are, respectively, $P _ { 1 } ( x ) = 0 . 9 2 9 5 1 4 0 + 0 . 5 2 8 1 0 2 1 x$ , with $2 . 4 5 7 \times 1 0 ^ { - 2 }$ ; $P _ { 2 } ( x ) = 1 . 0 1 1 3 4 1 - 0 . 3 2 5 6 9 8 8 x + 1 . 1 4 7 3 3 0 x ^ { 2 }$ , with $9 . 4 5 3 \times 1 0 ^ { - 4 }$ ; $P _ { 3 } ( x ) = 1 . 0 0 0 4 4 0 - 0 . 0 0 1 5 4 0 9 8 6 x - 0 . 0 1 1 5 0 5 6 7 5 x ^ { 2 } + 1 . 0 2 1 0 2 3 x ^ { 3 }$ with $1 . 1 1 2 \times 1 0 ^ { - 4 }$ .   
5. (a) The linear least-squares polynomial is $7 2 . 0 8 4 5 x - 1 9 4 . 1 3 8$ , with error 329. (b) The least-squares polynomial of degree two is $6 . 6 1 8 2 1 x ^ { 2 } - 1 . 1 4 3 5 2 x + 1 . 2 3 5 5 6$ , with error $1 . 4 4 \times 1 0 ^ { - 3 }$ . (c) The least-squares polynomial of degree three is $- 0 . 0 1 3 6 7 4 2 x ^ { 3 } + 6 . 8 4 5 5 7 x ^ { 2 } - 2 . 3 7 9 1 9 x +$ 3.42904, with error $5 . 2 7 \times 1 0 ^ { - 4 }$ . (d) The least-squares approximation of the form $b e ^ { a x }$ is $2 4 . 2 5 8 8 e ^ { 0 . 3 7 2 3 8 2 x }$ , with error 418. (e) The least-squares approximation of the form $b x ^ { a }$ is $6 . 2 3 9 0 3 x ^ { 2 . 0 1 9 5 4 }$ , with error 0.00703.   
6. (a) The linear least-squares polynomial is $P _ { 1 } ( x ) = 1 . 6 6 5 5 4 0 x - 0 . 5 1 2 4 5 6 8$ , with error 0.33559. (b) The least-squares polynomial of degree two is $P _ { 2 } ( x ) = 1 . 1 2 9 4 2 4 x ^ { 2 } - 0 . 3 1 1 4 0 3 5 x + 0 . 0 8 5 1 4 3 9 3$ with error $2 . 4 1 9 9 \times 1 0 ^ { - 3 }$ . (c) The least-squares polynomial of degree three is $P _ { 3 } ( x ) = 0 . 2 6 6 2 0 8 1 x ^ { 3 } + 0 . 4 0 2 9 3 2 2 x ^ { 2 } +$ $0 . 2 4 8 3 8 5 7 x - 0 . 0 1 8 4 0 1 4 0$ , with error $5 . 0 7 4 7 \times 1 0 ^ { - 6 }$ . (d) The least-squares approximation of the form $b e ^ { a x }$ is $f ( x ) = 0 . 0 4 5 7 0 7 4 8 e ^ { 2 . 7 0 7 2 9 5 x }$ , with error 1.0750. (e) The least-squares approximation of the form $b x ^ { a }$ is $f ( x ) = 0 . 9 5 0 1 5 6 5 x ^ { 1 . 8 / 2 0 0 9 }$ , with error 0.054477.

. (a) $k = 0 . 8 9 9 6 , \ E ( k ) = 0 . 2 9 5$ (b) $k = 0 . 9 0 5 2$ , $E ( k ) = 0 . 1 2 8$ Part (b) fits the total experimental data best.

$^ { * } 8$ . $P _ { 1 } ( x ) = 0 . 2 2 3 3 5 x - 0 . 8 0 2 8 3$ . For minimal $A$ , 406; for minimal $D$ , 272. The prediction for an $A$ is certainly unreasonable.

9. The least squares line for the point average is 0.101 (ACT score) + 0.487.

10. The percent occurrence is $- 0 . 0 0 2 2 5 5 0 x$ (average weight) $+ 1 3 . 1 4 6$ .

11. The linear least-squares polynomial gives $y \approx 0 . 1 7 9 5 2 x + 8 . 2 0 8 4$ .

12. The linear least-squares polynomial is $1 . 6 0 0 3 9 3 x + 2 5 . 9 2 1 7 5$

13. (a) $\ln R = \ln 1 . 3 0 4 + 0 . 5 7 5 6 \ln W$ (b) $E = 2 5 . 2 5$ (c) $\begin{array} { r l } & { \ln R = \ln 1 . 0 5 1 + 0 . 7 0 0 6 \ln W + 0 . 0 6 6 9 5 ( \ln W ) ^ { 2 } } \\ & { E = \sum _ { i = 1 } ^ { 3 7 } \Big ( R _ { i } - b W _ { i } ^ { a } e ^ { c ( \ln W _ { i } ) ^ { 2 } } \Big ) ^ { 2 } = 2 0 . 3 0 } \end{array}$ (d)

\*14. For each i = 1, . . . , n + 1 and j = 1, . . . , n + 1, aij = aji = Pmk=1 xi+jk , so $A = \left( a _ { i j } \right)$ is symmetric. Suppose $A$ is singular and $\mathbf c \neq \mathbf 0$ satisfies $\mathbf { c } ^ { t } A \mathbf { c } = \mathbf { 0 }$ . Then

$$
0 = \sum _ { i = 1 } ^ { n + 1 } \sum _ { j = 1 } ^ { n + 1 } a _ { i j } c _ { i } c _ { j } = \sum _ { i = 1 } ^ { n + 1 } \sum _ { j = 1 } ^ { n + 1 } \left( \sum _ { k = 1 } ^ { m } x _ { k } ^ { i + j - 2 } \right) c _ { i } c _ { j } = \sum _ { k = 1 } ^ { m } \left[ \sum _ { i = 1 } ^ { n + 1 } \sum _ { j = 1 } ^ { n + 1 } c _ { i } c _ { j } x _ { k } ^ { i + j - 2 } \right] ,
$$

so

$$
\sum _ { k = 1 } ^ { m } \left( \sum _ { i = 1 } ^ { n + 1 } c _ { i } x _ { k } ^ { i - 1 } \right) ^ { 2 } = 0 .
$$

Define $P ( x ) = c _ { 1 } + c _ { 2 } x + . . . + c _ { n + 1 } x ^ { n }$ . Then $\begin{array} { r } { \sum _ { k = 1 } ^ { m } \left[ P ( x _ { k } ) \right] ^ { 2 } = 0 } \end{array}$ and $P ( x )$ has roots $x _ { 1 } , \ldots , x _ { m }$ Since the roots are distinct and $m > n$ , $P ( x )$ must be the zero polynomial. Thus, $c _ { 1 } = c _ { 2 } =$ $\ldots = c _ { n + 1 } = 0$ , and $A$ must be nonsingular.

# Exercise Set 8.2, page 518

1. The linear least-squares approximations are:

(a) $P _ { 1 } ( x ) = 1 . 8 3 3 3 3 3 + 4 x$ $^ *$ (b) $P _ { 1 } ( x ) = - 1 . 6 0 0 0 0 3 + 3 . 6 0 0 0 0 3 x$ (c) $P _ { 1 } ( x ) = 1 . 1 4 0 9 8 1 - 0 . 2 9 5 8 3 7 5 x$ (d) $P _ { 1 } ( x ) = 0 . 1 9 4 5 2 6 7 + 3 . 0 0 0 0 0 1 x$ (e) $P _ { 1 } ( x ) = 0 . 6 1 0 9 2 4 5 + 0 . 0 9 1 6 7 1 0 5 x$ (f) $P _ { 1 } ( x ) = - 1 . 8 6 1 4 5 5 + 1 . 6 6 6 6 6 7 x$

2. The linear least-squares approximations on $[ - 1 , 1 ]$ are:

(a) $P _ { 1 } ( x ) = 3 . 3 3 3 3 3 3 - 2 x$ (b) $P _ { 1 } ( x ) = 0 . 6 0 0 0 0 2 5 x$ (c) $P _ { 1 } ( x ) = 0 . 5 4 9 3 0 6 3 - 0 . 2 9 5 8 3 7 5 x$ (d) $P _ { 1 } ( x ) = 1 . 1 7 5 2 0 1 + 1 . 1 0 3 6 3 9 x$ (e) $P _ { 1 } ( x ) = 0 . 4 2 0 7 3 5 5 + 0 . 4 3 5 3 9 7 5 x$ (f) $P _ { 1 } ( x ) = 0 . 6 4 7 9 1 8 4 + 0 . 5 2 8 1 2 2 6 x$

3. The least squares approximations of degree two are:

(a) $P _ { 2 } ( x ) = 2 + 3 x + x ^ { 2 } \equiv f ( x )$ \*(b) $P _ { 2 } ( x ) = 0 . 4 0 0 0 1 6 3 - 2 . 4 0 0 0 5 4 x + 3 . 0 0 0 0 2 8 x ^ { 2 }$ (c) $P _ { 2 } ( x ) = 1 . 7 2 3 5 5 1 - 0 . 9 3 1 3 6 8 2 x + 0 . 1 5 8 8 8 2 7 x ^ { 2 }$ 2 (d) $P _ { 2 } ( x ) = 1 . 1 6 7 1 7 9 + 0 . 0 8 2 0 4 4 4 2 x + 1 . 4 5 8 9 7 9 x$ 2 (e) $P _ { 2 } ( x ) = 0 . 4 8 8 0 0 5 8 + 0 . 8 2 9 1 8 3 0 x - 0 . 7 3 7 5 1 1 9 x ^ { 2 }$ (f) $P _ { 2 } ( x ) = - 0 . 9 0 8 9 5 2 3 + 0 . 6 2 7 5 7 2 3 x + 0 . 2 5 9 7 7 3 6 x ^ { 2 }$ 2

4. The least squares approximation of degree two on $[ - 1 , 1 ]$ are:

(a) $P _ { 2 } ( x ) = 3 - 2 x + 1 . 0 0 0 0 9 x ^ { 2 }$ (b) $P _ { 2 } ( x ) = 0 . 6 0 0 0 0 2 5 x$ (c) $^ { D } _ { 2 } ( x ) = 0 . 4 9 6 3 4 5 4 - 0 . 2 9 5 8 3 7 5 x + 0 . 1 5 8 8 8 2 7 x ^ { 2 }$ 2 (d) $^ { D } _ { 2 } ( x ) = 0 . 9 9 6 2 9 1 8 + 1 . 1 0 3 6 3 9 x + 0 . 5 3 6 7 2 8 2 x ^ { 2 }$ (e) $P _ { 2 } ( x ) = 0 . 4 9 8 2 7 9 8 + 0 . 4 3 5 3 9 7 5 x - 0 . 2 3 2 6 3 3 0 x ^ { 2 }$ 2 (f) $P _ { 2 } ( x ) = 0 . 6 9 4 7 8 9 8 + 0 . 5 2 8 1 2 2 6 x - 0 . 1 4 0 6 1 4 1 x ^ { \mathrm { i } }$ 2

5. The errors $E$ for the least squares approximations in Exercise 3 are:

(a) $0 . 3 4 2 7 \times 1 0 ^ { - 9 }$ \*(b) 0.0457142(c) 0.000358354(d) 0.0106445(e) 0.0000134621(f) 0.0000967795

6. The errors for the approximations in Exercise 4 are:

(a) 0   
(b) 0.0457206   
(c) 0.00035851   
(d) 0.0014082   
(e) 0.00575753   
(f) 0.00011949

7. The Gram-Schmidt process produces the following collections of polynomials:

$$
\begin{array} { l l l l } { { \phi _ { 0 } ( x ) = 1 , \phi _ { 1 } ( x ) = x - 0 . 5 , } } & { { \phi _ { 2 } ( x ) = x ^ { 2 } - x + \frac { 1 } { 6 } , } } & { { \mathrm { a n d } } } & { { \phi _ { 3 } ( x ) = x ^ { 3 } - 1 . 5 x ^ { 2 } + 0 . 6 x - 0 . 0 5 , } } \\ { { \phi _ { 0 } ( x ) = 1 , \phi _ { 1 } ( x ) = x - 1 , } } & { { \phi _ { 2 } ( x ) = x ^ { 2 } - 2 x + \frac { 2 } { 3 } , } } & { { \mathrm { a n d } } } & { { \phi _ { 3 } ( x ) = x ^ { 3 } - 3 x ^ { 2 } + \frac { 1 2 } { 5 } x - \frac { 2 } { 5 } x + \frac { 1 } { 6 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 2 } , } } \\ { { \phi _ { 0 } ( x ) = 1 , \phi _ { 1 } ( x ) = x - 2 , } } & { { \phi _ { 2 } ( x ) = x ^ { 2 } - 4 x + \frac { 1 1 } { 3 } , } } & { { \mathrm { a n d } } } & { { \phi _ { 3 } ( x ) = x ^ { 3 } - 6 x ^ { 2 } + 1 1 . 4 x - 6 . 8 5 . } } \end{array}
$$

8. The Gram-Schmidt process produces the following collections of polynomials.

(a) $3 . 8 3 3 3 3 3 \phi _ { 0 } ( x ) + 4 . 0 0 0 0 0 0 \phi _ { 1 } ( x )$ (b) $2 \phi _ { 0 } ( x ) + 3 . 6 \phi _ { 1 } ( x )$ (c) $0 . 5 4 9 3 0 6 1 \phi _ { 0 } ( x ) - 0 . 2 9 5 8 3 6 9 \phi _ { 1 } ( x )$ (d) $3 . 1 9 4 5 2 8 \phi _ { 0 } ( x ) + 3 \phi _ { 1 } ( x )$ (e) $0 . 6 5 6 7 6 0 0 \phi _ { 0 } ( x ) + 0 . 0 9 1 6 7 1 0 5 \phi _ { 1 } ( x )$ (f) $1 . 4 7 1 8 7 8 \phi _ { 0 } ( x ) + 1 . 6 6 6 6 6 7 \phi _ { 1 } ( x )$

9. The least-squares polynomials of degree three are:

(a) $P _ { 3 } ( x ) = 3 . 8 3 3 3 3 4 \phi _ { 0 } ( x ) + 4 . 0 0 0 0 0 0 \phi _ { 1 } ( x ) + 0 . 9 9 9 9 9 8 \phi _ { 2 } ( x )$ \*(b) $P _ { 3 } ( x ) = 2 \phi _ { 0 } ( x ) + 3 . 6 \phi _ { 1 } ( x ) + 3 \phi _ { 2 } ( x ) + \phi _ { 3 } ( x )$ (c) $P _ { 3 } ( x ) = 0 . 5 4 9 3 0 6 1 \phi _ { 0 } ( x ) - 0 . 2 9 5 8 3 6 9 \phi _ { 1 } ( x ) + 0 . 1 5 8 8 7 8 5 \phi _ { 2 } ( x ) - 0 . 0 8 5 2 4 4 7 0 \phi _ { 3 } ( x )$ (d) $P _ { 3 } ( x ) = 3 . 1 9 4 5 2 8 \phi _ { 0 } ( x ) + 3 \phi _ { 1 } ( x ) + 1 . 4 5 8 9 6 0 \phi _ { 2 } ( x ) + 0 . 4 7 8 7 9 5 9 \phi _ { 3 } ( x )$ (e) $P _ { 3 } ( x ) = 0 . 6 5 6 7 6 0 0 \phi _ { 0 } ( x ) + 0 . 0 9 1 6 7 1 0 5 \phi _ { 1 } ( x ) - 0 . 7 3 7 5 1 1 8 \phi _ { 2 } ( x ) - 0 . 1 8 7 6 9 5 2 \phi _ { 3 } ( x )$ ) (f) $P _ { 3 } ( x ) = 1 . 4 7 1 8 7 8 \phi _ { 0 } ( x ) + 1 . 6 6 6 6 7 \phi _ { 1 } ( x ) + 0 . 2 5 9 7 7 0 5 \phi _ { 2 } ( x ) - 0 . 0 4 5 5 9 6 1 1 \phi _ { 3 } ( x )$

10. The least-squares polynomials of degree two are:

(a) $P _ { 2 } ( x ) = 3 . 8 3 3 3 3 3 \phi _ { 0 } ( x ) + 4 \phi _ { 1 } ( x ) + 0 . 9 9 9 9 9 9 8 \phi _ { 2 } ( x )$ (b) $P _ { 2 } ( x ) = 2 \phi _ { 0 } ( x ) + 3 . 6 \phi _ { 1 } ( x ) + 3 \phi _ { 2 } ( x )$ (c) $P _ { 2 } ( x ) = 0 . 5 4 9 3 0 6 1 \phi _ { 0 } ( x ) - 0 . 2 9 5 8 3 6 9 \phi _ { 1 } ( x ) + 0 . 1 5 8 8 7 8 5 \phi _ { 2 } ( x )$ (d) $P _ { 2 } ( x ) = 3 . 1 9 4 5 2 8 \phi _ { 0 } ( x ) + 3 \phi _ { 1 } ( x ) + 1 . 4 5 8 9 6 0 \phi _ { 2 } ( x )$ (e) $P _ { 2 } ( x ) = 0 . 6 5 6 7 6 0 0 \phi _ { 0 } ( x ) + 0 . 0 9 1 6 7 1 0 5 \phi _ { 1 } ( x ) - 0 . 7 3 7 5 1 2 1 8 \phi _ { 2 } ( x )$ ) (f) $P _ { 2 } ( x ) = 1 . 4 7 1 8 7 8 \phi _ { 0 } ( x ) + 1 . 6 6 6 6 6 7 \phi _ { 1 } ( x ) + 0 . 2 5 9 7 7 0 5 \phi _ { 2 } ( x )$

11. The Laguerre polynomials are $L _ { 1 } ( x ) = x - 1$ , $L _ { 2 } ( x ) = x ^ { 2 } - 4 x + 2$ and $L _ { 3 } ( x ) = x ^ { 3 } - 9 x ^ { 2 } + 1 8 x - 6$ .

12. The least-squares polynomials of degrees one, two, and three are:

(a) $2 L _ { 0 } ( x ) + 4 L _ { 1 } ( x ) + L _ { 2 } ( x )$ (b) $\begin{array} { r } { \frac { 1 } { 2 } L _ { 0 } ( x ) - \frac { 1 } { 4 } L _ { 1 } ( x ) + \frac { 1 } { 1 6 } L _ { 2 } ( x ) - \frac { 1 } { 9 6 } L _ { 3 } ( x ) } \end{array}$ (c) $6 L _ { 0 } ( x ) + 1 8 L _ { 1 } ( x ) + 9 L _ { 2 } ( x ) + L _ { 3 } ( x )$ (d) $\textstyle { \frac { 1 } { 3 } } L _ { 0 } ( x ) - { \frac { 2 } { 9 } } L _ { 1 } ( x ) + { \frac { 2 } { 2 7 } } L _ { 2 } ( x ) - { \frac { 4 } { 2 4 3 } } L _ { 3 } ( x )$

\*13. Let $i = 0 , 1 , \ldots , n$ $\{ \phi _ { 0 } ( x ) , \phi _ { 1 } ( x ) , \ldots , \phi _ { n } ( x ) \}$ , let $\begin{array} { r } { \phi _ { i } ( x ) \ : = \ : \sum _ { k = 0 } ^ { n } b _ { k i } x ^ { k } } \end{array}$ be a linearly independent set of polynomials in . Let $\begin{array} { r } { Q ( x ) \ = \ \sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } \ \in \ \prod _ { n } } \end{array}$ n. We want to find $\prod _ { n }$ . For each constants $c _ { 0 } , \ldots , c _ { n }$ so that

$$
Q ( x ) = \sum _ { i = 0 } ^ { n } c _ { i } \phi _ { i } ( x ) .
$$

This equation becomes

$$
\sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } = \sum _ { i = 0 } ^ { n } c _ { i } \left( \sum _ { k = 0 } ^ { n } b _ { k i } x ^ { k } \right) 
$$

so we have both

$$
\sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } = \sum _ { k = 0 } ^ { n } \left( \sum _ { i = 0 } ^ { n } c _ { i } b _ { k i } \right) x ^ { k } , \quad { \mathrm { a n d } } \quad \sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } = \sum _ { k = 0 } ^ { n } \left( \sum _ { i = 0 } ^ { n } b _ { k i } c _ { i } \right) x ^ { k } .
$$

But $\{ 1 , x , \ldots , x ^ { n } \}$ is linearly independent, so, for each $k = 0 , \ldots , n$ , we have

$$
\sum _ { i = 0 } ^ { n } b _ { k i } c _ { i } = a _ { k } ,
$$

which expands to the linear system

$$
{ \left[ \begin{array} { l l l l } { b _ { 0 1 } } & { b _ { 0 2 } } & { \cdots } & { b _ { 0 n } } \\ { b _ { 1 1 } } & { b _ { 1 2 } } & { \cdots } & { b _ { 1 n } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { b _ { n 1 } } & { b _ { n 2 } } & { \cdots } & { b _ { n n } } \\ { } & { } & { } & { } \end{array} \right] } \quad { \left[ \begin{array} { l } { c _ { 0 } } \\ { c _ { 1 } } \\ { \vdots } \\ { c _ { n } } \end{array} \right] } = { \left[ \begin{array} { l } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { n } } \end{array} \right] } .
$$

This linear system must have a unique solution $\{ c _ { 0 } , c _ { 1 } , \ldots , c _ { n } \}$ , or else there is a nontrivial set of constants $\{ c _ { 0 } ^ { \prime } , c _ { 1 } ^ { \prime } , \ldots , c _ { n } ^ { \prime } \}$ , for which

$$
{ \begin{array} { r l } { \left[ b _ { 0 1 } \quad \cdot \cdot \cdot \right]} & { b _ { 0 n } } \\ { \vdots } & { \vdots } \\ { b _ { n 1 } \quad \cdot \cdot \cdot } & { b _ { n n } } \end{array}  } &  { \Bigg [ } { \begin{array} { l } { c _ { 0 } ^ { \prime } } \\ { \vdots } \\ { c _ { n } ^ { \prime } } \end{array} } { \Bigg ] } = { \Bigg [ } { \begin{array} { l } { 0 } \\ { \vdots } \\ { 0 } \end{array} } { \Bigg ] } ~ .
$$

Thus

$$
c _ { 0 } ^ { \prime } \phi _ { 0 } ( x ) + c _ { 1 } ^ { \prime } \phi _ { 1 } ( x ) + \ldots + c _ { n } ^ { \prime } \phi _ { n } ( x ) = \sum _ { k = 0 } ^ { n } 0 x ^ { k } = 0 ,
$$

which contradicts the linear independence of the set $\{ \phi _ { 0 } , . . . , \phi _ { n } \}$ . Thus, there is a unique set of constants $\{ c _ { 0 } , \ldots , c _ { n } \}$ , for which

$$
Q ( x ) = c _ { 0 } \phi _ { 0 } ( x ) + c _ { 1 } \phi _ { 1 } ( x ) + . . . + c _ { n } \phi _ { n } ( x ) .
$$

$^ { * } 1 4$ . If $\textstyle \sum _ { i = 0 } ^ { n } c _ { i } \phi _ { i } ( x ) = 0$ , for all $a \leq x \leq b$ , then

$$
\int _ { a } ^ { b } \left( \sum _ { i = 0 } ^ { n } c _ { i } \phi _ { i } ( x ) \right) \phi _ { j } ( x ) w ( x ) d x = 0 , \quad { \mathrm { f o r ~ e a c h ~ } } j = 0 , 1 , \dots , n .
$$

Thus, $c _ { j } = 0$ , for each $j = 0 , 1 , \dotsc , n$ .

15. The normal equations are

$$
\sum _ { k = 0 } ^ { n } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x = \int _ { a } ^ { b } x ^ { j } f ( x ) d x , \quad { \mathrm { f o r ~ e a c h } } \ j = 0 , 1 , \dots , n .
$$

Let

$$
b _ { j k } = \int _ { a } ^ { b } x ^ { j + k } d x , \quad { \mathrm { f o r ~ e a c h } } \ j = 0 , \dots , n , \quad { \mathrm { a n d } } \quad k = 0 , \dots , n ,
$$

and let $B = \left( b _ { j k } \right)$ . Further, let

$$
\mathbf { a } = ( a _ { 0 } , \ldots , a _ { n } ) ^ { t } \quad { \mathrm { a n d } } \quad \mathbf { g } = \left( \int _ { a } ^ { b } f ( x ) d x , \ldots , \int _ { a } ^ { b } x ^ { n } f ( x ) d x \right) ^ { t } .
$$

Then the normal equations produce the linear system $B \mathbf { a } = \mathbf { g }$ .

To show that the normal equations have a unique solution, it suffices to show that if $f \equiv 0$ then $\mathbf { a } = \mathbf { 0 }$ . If $f \equiv 0$ , then

$$
\sum _ { k = 0 } ^ { n } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x = 0 , \quad \mathrm { f o r } j = 0 , \dots , n , \quad \mathrm { a n d } \quad \sum _ { k = 0 } ^ { n } a _ { j } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x = 0 , \quad \mathrm { f o r } j = 0 , \dots , n
$$

and summing over $j$ gives

$$
\sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { n } a _ { j } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x = 0 .
$$

Thus

$$
\int _ { a } ^ { b } \sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { n } a _ { j } x ^ { j } a _ { k } x ^ { k } d x = 0 \quad { \mathrm { a n d } } \quad \int _ { a } ^ { b } { \biggl ( } \sum _ { j = 0 } ^ { n } a _ { j } x ^ { j } { \biggr ) } ^ { 2 } d x = 0 .
$$

Define $P ( x ) = a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n }$ . Then $\begin{array} { r } { \int _ { a } ^ { b } \left[ P ( x ) \right] ^ { 2 } d x = 0 } \end{array}$ and $P ( x ) \equiv 0$ . This implies that $a _ { 0 } = a _ { 1 } = \cdot \cdot \cdot = a _ { n } = 0$ , so $\mathbf { a } = \mathbf { 0 }$ . Hence, the matrix $B$ is nonsingular, and the normal equations have a unique solution.

# Exercise Set 8.3, page 527

1. The interpolating polynomials of degree two are:

\*(a) $^ { D } _ { 2 } ( x ) = 2 . 3 7 7 4 4 3 + 1 . 5 9 0 5 3 4 ( x - 0 . 8 6 6 0 2 5 4 ) +$ $3 4 ( x - 0 . 8 6 6 0 2 5 4 ) + 0 . 5 3 2 0 4 1 8 ( x - 0 . 8 6 6 0 2 5 4 ) ;$ x (b) $P _ { 2 } ( x ) = 0 . 7 6 1 7 6 0 0 + 0 . 8 7 9 6 0 4 7 ( x - 0 . 8 6 6 0 2 5 4 )$ (c) $P _ { 2 } ( x ) = 1 . 0 5 2 9 2 6 + 0 . 4 1 5 4 3 7 0 ( x - 0 . 8 6 6 0 2 5 4 ) - 0 . 1 3 8 4 2 6 2 x ( x - 0 . 8 6 6 0 2 5 4 )$ (d) $P _ { 2 } ( x ) = 0 . 5 6 2 5 + 0 . 6 4 9 5 1 9 ( x - 0 . 8 6 6 0 2 5 4 ) + 0 . 7 5 x ( x - 0 . 8 6 6 0 2 5 4 )$

2. The interpolating polynomials of degree three are:

(a) $P _ { 3 } ( x ) = 2 . 5 1 9 0 4 4 + 1 . 9 4 5 3 7 7 ( x - 0 . 9 2 3 8 7 9 5 ) + 0 . 7 0 4 7 4 2 0 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 )$ $+ 0 . 1 7 5 1 7 5 7 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 ) ( x + 0 . 3 8 2 6 8 3 4 )$

(b) $P _ { 3 } ( x ) = 0 . 7 9 7 9 4 5 9 + 0 . 7 8 4 4 3 8 0 ( x - 0 . 9 2 3 8 7 9 5 ) - 0 . 1 4 6 4 3 9 4 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 )$ $- 0 . 1 5 8 5 0 4 9 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 ) ( x + 0 . 3 8 2 6 8 3 4 )$ (c) $P _ { 3 } ( x ) = 1 . 0 7 2 9 1 1 + 0 . 3 7 8 2 0 6 7 ( x - 0 . 9 2 3 8 7 9 5 ) - 0 . 0 9 7 9 9 2 1 3 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 )$ $+ 0 . 0 4 9 0 9 0 7 3 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 ) ( x + 0 . 3 8 2 6 8 3 4 )$ (d) $P _ { 3 } ( x ) = 0 . 7 2 8 5 5 3 3 + 1 . 3 0 6 5 6 3 ( x - 0 . 9 2 3 8 7 9 5 ) + 0 . 9 9 9 9 9 9 9 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 ) ^ { 2 }$ )

3. Bounds for the maximum errors of polynomials in Exercise 1 are:

\*(a) 0.1132617 (b) 0.04166667 (c) 0.08333333 (d) 1.000000

4. Bounds for the maximum errors of polynomials in Exercise 3 are:

(a) 0.01415772 (b) 0.004382661 (c) 0.03125000 (d) 0.1250000

5. The zeros of $\ddot { T } _ { 3 }$ produce the following interpolating polynomials of degree two.

(a) $^ { D } _ { 2 } ( x ) = 0 . 3 4 8 9 1 5 3 - 0 . 1 7 4 4 5 7 6 ( x - 2 . 8 6 6 0 2 5 ) -$ $\cdot - 2 . 8 6 6 0 2 5 ) + 0 . 1 5 3 8 4 6 2 ( x - 2 . 8 6 6 0 2 5 ) ( x - 2 )$ (b) $P _ { 2 } ( x ) = 0 . 1 5 4 7 3 7 5 - 0 . 2 4 6 1 1 5 2 ( x - 1 . 8 6 6 0 2 5 ) + 0 . 1 9 5 7 2 7 3 ( x - 1 . 8 6 6 0 2 5 ) ( x - 1 )$ (c) $P _ { 2 } ( x ) = 0 . 6 1 6 6 2 0 0 - 0 . 2 3 7 0 8 6 9 ( x - 0 . 9 3 3 0 1 2 7 ) - 0 . 7 4 2 7 7 3 2 ( x - 0 . 9 3 3 0 1 2 7 ) ( x - 0 . 9 3 3 0 1 2 7 ) .$ 0.5) (d) $P _ { 2 } ( x ) = 3 . 0 1 7 7 1 2 5 + 1 . 8 8 3 8 0 0 ( x - 2 . 8 6 6 0 2 5 ) + 0 . 2 5 8 4 6 2 5 ( x - 2 . 8 6 6 0 2 5 ) ( x - 2 )$

6. The polynomial

$$
P ( x ) = { \frac { 1 } { 3 8 4 0 } } + { \frac { 3 7 9 } { 3 8 4 } } x + { \frac { 6 3 7 } { 6 4 0 } } x ^ { 2 } + { \frac { 5 3 } { 9 6 } } x ^ { 3 } + { \frac { 4 3 } { 2 4 0 } } x ^ { 4 }
$$

approximates $x e ^ { x }$ , with error at most 0.00718.

7. The cubic polynomial ${ \frac { 3 8 3 } { 3 8 4 } } x - { \frac { 5 } { 3 2 } } x ^ { 3 }$ approximates $\sin x$ with error at most $7 . 1 9 \times 1 0 ^ { - 4 }$ .

$^ { * } 8$ . If $i > j$ , then

$$
{ \frac { 1 } { 2 } } ( T _ { i + j } ( x ) + T _ { i - j } ( x ) ) = { \frac { 1 } { 2 } } \left( \cos ( i + j ) \theta + \cos ( i - j ) \theta \right) = \cos i \theta \cos j \theta = T _ { i } ( x ) T _ { j } ( x ) .
$$

$^ { * } 9$ . The change of variable $x = \cos \theta$ produces

$$
\int _ { - 1 } ^ { 1 } { \frac { T _ { n } ^ { 2 } ( x ) } { \sqrt { 1 - x ^ { 2 } } } } \ d x = \int _ { - 1 } ^ { 1 } { \frac { [ \cos ( n \operatorname { a r c c o s } x ) ] ^ { 2 } } { \sqrt { 1 - x ^ { 2 } } } } \ d x = \int _ { 0 } ^ { \pi } ( \cos ( n \theta ) ) ^ { 2 } \ d x = { \frac { \pi } { 2 } } .
$$

10. The zeros of $T _ { n } ( x )$ are ${ \overline { { x } } } _ { n } = \cos \left( { \frac { 2 k - 1 } { 2 n } } \pi \right)$ for $k = 1 , 2 , \ldots , n$

The cosine function is strictly decreasing from $0$ to $\pi$ , with values decreasing from $\cos 0 = 1$ to $\cos \pi = - 1$ . So

$$
- 1 = \cos ( \pi ) < \cos \left( { \frac { 2 n - 1 } { 2 n } } \pi \right) = { \overline { { x } } } _ { n } < { \overline { { x } } } _ { n - 1 } < \cdot \cdot \cdot < { \overline { { x } } } _ { 1 } = \cos \left( { \frac { \pi } { 2 n } } \right) < \cos ( 1 ) = 1
$$

Hence the zeros are distinct and lie in $( - 1 , 1 )$

11. The zeros of $T _ { n } ^ { \prime } ( x )$ are ${ \overline { { x ^ { \prime } } } } _ { n } = \cos \left( { \frac { k \pi } { n } } \right)$ for $k = 1 , 2 , \ldots , n - 1$

The cosine function is strictly decreasing from $0$ to $\pi$ , with values decreasing from $\cos 0 = 1$ to $\cos \pi = - 1$ . So

$$
- 1 = \cos ( \pi ) < \cos \left( { \frac { ( n - 1 ) \pi } { n } } \right) = { \overline { { x ^ { \prime } } } } _ { n - 1 } < { \overline { { x ^ { \prime } } } } _ { n - 2 } < \cdot \cdot \cdot < { \overline { { x ^ { \prime } } } } _ { 1 } = \cos \left( { \frac { \pi } { n } } \right) < \cos ( 1 ) = 1
$$

Hence the zeros are distinct and lie in $( - 1 , 1 )$

# Exercise Set 8.4, page 537

$^ { * } 1$ . The Pad´e approximations of degree two for $f ( x ) = e ^ { 2 x }$ are:

$$
\begin{array} { l l l } { n } & { = } & { 2 , m = 0 : r _ { 2 , 0 } ( x ) = 1 + 2 x + 2 x ^ { 2 } } \\ { n } & { = } & { 1 , m = 1 : r _ { 1 , 1 } ( x ) = ( 1 + x ) / ( 1 - x ) } \\ { n } & { = } & { 0 , m = 2 : r _ { 0 , 2 } ( x ) = ( 1 - 2 x + 2 x ^ { 2 } ) ^ { - 1 } } \end{array}
$$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r2,0(xi)</td><td>r1,1(xi)</td><td>r0,2(xi)</td></tr><tr><td>1</td><td>0.2</td><td>1.4918</td><td>1.4800</td><td>1.5000</td><td>1.4706</td></tr><tr><td>2</td><td>0.4</td><td>2.2255</td><td>2.1200</td><td>2.3333</td><td>1.9231</td></tr><tr><td>3</td><td>0.6</td><td>3.3201</td><td>2.9200</td><td>4.0000</td><td>1.9231</td></tr><tr><td>4</td><td>0.8</td><td>4.9530</td><td>3.8800</td><td>9.0000</td><td>1.4706</td></tr><tr><td>5</td><td>1.0</td><td>7.3891</td><td>5.0000</td><td>undefined</td><td>1.0000</td></tr></table>

2. The Pad´e approximations of degree three for $f ( x ) = x \ln ( x + 1 )$ are:

$$
\begin{array} { l } { m = 0 , n = 3 ; ~ x ^ { 2 } - \displaystyle \frac { 1 } { 2 } x ^ { 3 } } \\ { m = 1 , n = 2 ; ~ \displaystyle \frac { x ^ { 2 } } { 1 + \frac { 1 } { 2 } x } } \end{array}
$$

$m = 1$ , $n = 2$ ; $m = 2$ , $n = 1$ ; and $m = 3$ , $n = 0$ : $\frac { x ^ { 2 } } { 1 + { \frac { 1 } { 2 } } x }$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r3.0(xi)</td><td>r2,1(xi)</td></tr><tr><td>1</td><td>0.2</td><td>0.03646431</td><td>0.03600000</td><td>0.03636364</td></tr><tr><td>2</td><td>0.4</td><td>0.13458889</td><td>0.12800000</td><td>0.13333333</td></tr><tr><td>3</td><td>0.6</td><td>0.28200218</td><td>0.25200000</td><td>0.27692308</td></tr><tr><td>4</td><td>0.8</td><td>0.47022933</td><td>0.38400000</td><td>0.45714286</td></tr><tr><td>5</td><td>1.0</td><td>0.69314718</td><td>0.50000000</td><td>0.66666666</td></tr></table>

3. The Pad´e approximation of degree five for $f ( x ) = e ^ { x }$ with $n = 2$ and $m = 3$ is:

$$
r _ { 2 , 3 } ( x ) = ( 1 + \frac { 2 } { 5 } x + \frac { 1 } { 2 0 } x ^ { 2 } ) / ( 1 - \frac { 3 } { 5 } x + \frac { 3 } { 2 0 } x ^ { 2 } - \frac { 1 } { 6 0 } x ^ { 3 } )
$$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r2.3(xi)</td></tr><tr><td>1</td><td>0.2</td><td>1.22140276</td><td>1.22140277</td></tr><tr><td>2</td><td>0.4</td><td>1.49182470</td><td>1.49182561</td></tr><tr><td>3</td><td>0.6</td><td>1.82211880</td><td>1.82213210</td></tr><tr><td>4</td><td>0.8</td><td>2.22554093</td><td>2.22563652</td></tr><tr><td>5</td><td>1.0</td><td>2.71828183</td><td>2.71875000</td></tr></table>

4. The Pad´e approximations of degree five for $f ( x ) = e ^ { x }$ with $n = 3$ and $m = 2$ is:

$$
r _ { 3 , 2 } ( x ) = \left( 1 + \frac { 3 } { 5 } x + \frac { 3 } { 2 0 } x ^ { 2 } + \frac { 1 } { 6 0 } x ^ { 3 } \right) / \left( 1 - \frac { 2 } { 5 } x + \frac { 1 } { 2 0 } x ^ { 2 } \right)
$$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r3.2(xi)</td></tr><tr><td>1</td><td>0.2</td><td>1.22140276</td><td>1.22140275</td></tr><tr><td>2</td><td>0.4</td><td>1.49182470</td><td>1.49182390</td></tr><tr><td>3</td><td>0.6</td><td>1.82211880</td><td>1.82210797</td></tr><tr><td>4</td><td>0.8</td><td>2.22554093</td><td>2.22546816</td></tr><tr><td>5</td><td>1.0</td><td>2.71828183</td><td>2.71794872</td></tr></table>

5. The Pad´e approximations of degree six for $f ( x ) = \sin { x }$ with $m = n = 3$ is:

$$
r _ { 3 , 3 } ( x ) = ( x - \frac { 7 } { 6 0 } x ^ { 3 } ) / ( 1 + \frac { 1 } { 2 0 } x ^ { 2 } )
$$

<table><tr><td>i</td><td>xi</td><td>f(xi)</td><td>Maclaurin polynomial of degree 6</td><td>r3,3(xi)</td></tr><tr><td>0</td><td>0.0</td><td>0.00000000</td><td>0.00000000</td><td>0.00000000</td></tr><tr><td>1</td><td>0.1</td><td>0.09983342</td><td>0.09966675</td><td>0.09938640</td></tr><tr><td>2</td><td>0.2</td><td>0.19866933</td><td>0.19733600</td><td>0.19709571</td></tr><tr><td>3</td><td>0.3</td><td>0.29552021</td><td>0.29102025</td><td>0.29246305</td></tr><tr><td>4</td><td>0.4</td><td>0.38941834</td><td>0.37875200</td><td>0.38483660</td></tr><tr><td>5</td><td>0.5</td><td>0.47942554</td><td>0.45859375</td><td>0.47357724</td></tr></table>

6. The Pad´e approximations of degree six for $f ( x ) = \sin { x }$ are as follows.

(a) Wit $\mathrm { ~ h ~ } n = 2 \mathrm { ~ a n d ~ } m = 4 : \mathrm { ~ } r _ { 2 , 4 } ( x ) = x / \left( 1 + \frac { 1 } { 6 } x ^ { 2 } + \frac { 7 } { 3 6 0 } x ^ { 4 } \right)$ (b) With $n = 4$ $4 { \mathrm { ~ a n d ~ } } m = 2 ! \ r _ { 4 , 2 } ( x ) = \left( x - { \frac { 7 } { 6 0 } } x ^ { 3 } \right) / \left( 1 + { \frac { 1 } { 2 0 } } x ^ { 2 } \right)$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r2.4（xi)</td><td>T4,2(xi)</td></tr><tr><td>0</td><td>0.0</td><td>0.00000000</td><td>0.00000000</td><td>0.00000000</td></tr><tr><td>1</td><td>0.1</td><td>0.09983342</td><td>0.09983342</td><td>0.09938640</td></tr><tr><td>2</td><td>0.2</td><td>0.19866933</td><td>0.19866936</td><td>0.19709571</td></tr><tr><td>3</td><td>0.3</td><td>0.29552021</td><td>0.29552065</td><td>0.29246305</td></tr><tr><td>4</td><td>0.4</td><td>0.38941834</td><td>0.38942158</td><td>0.38483660</td></tr><tr><td>5</td><td>0.5</td><td>0.47942554</td><td>0.47944065</td><td>0.47357724</td></tr></table>

7. The Pad´e approximations of degree five are:

(a) $r _ { 0 , 5 } ( x ) = ( 1 + x + \frac { 1 } { 2 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 3 } + \frac { 1 } { 2 4 } x ^ { 4 } + \frac { 1 } { 1 2 0 } x ^ { 5 } ) ^ { - 1 }$ (b) $r _ { 1 , 4 } ( x ) = ( 1 - \frac { 1 } { 5 } x ) / ( 1 + \frac { 4 } { 5 } x + \frac { 3 } { 1 0 } x ^ { 2 } + \frac { 1 } { 1 5 } x ^ { 3 } + \frac { 1 } { 1 2 0 } x ^ { 4 } )$ (c) $r _ { 3 , 2 } ( x ) = ( 1 - \frac { 3 } { 5 } x + \frac { 3 } { 2 0 } x ^ { 2 } - \frac { 1 } { 6 0 } x ^ { 3 } ) / ( 1 + \frac { 2 } { 5 } x + \frac { 1 } { 2 0 } x ^ { 2 } )$ (d) $r _ { 4 , 1 } ( x ) = ( 1 - \frac { 4 } { 5 } x + \frac { 3 } { 1 0 } x ^ { 2 } - \frac { 1 } { 1 5 } x ^ { 3 } + \frac { 1 } { 1 2 0 } x ^ { 4 } ) / ( 1 + \frac { 1 } { 5 } x )$

<table><tr><td>i</td><td>xi</td><td>f(xi)</td><td>r0.5(xi)</td><td>r1,4(xi)</td><td>r2,3(xi)</td><td>T4,1(xi)</td></tr><tr><td>1</td><td>0.2</td><td>0.81873075</td><td>0.81873081</td><td>0.81873074</td><td>0.81873075</td><td>0.81873077</td></tr><tr><td>2</td><td>0.4</td><td>0.67032005</td><td>0.67032276</td><td>0.67031942</td><td>0.67031963</td><td>0.67032099</td></tr><tr><td>3</td><td>0.6</td><td>0.54881164</td><td>0.54883296</td><td>0.54880635</td><td>0.54880763</td><td>0.54882143</td></tr><tr><td>4</td><td>0.8</td><td>0.44932896</td><td>0.44941181</td><td>0.44930678</td><td>0.44930966</td><td>0.44937931</td></tr><tr><td>5</td><td>1.0</td><td>0.36787944</td><td>0.36809816</td><td>0.36781609</td><td>0.36781609</td><td>0.36805556</td></tr></table>

8. The continued fraction forms of the rational functions are shown.

$$
\begin{array} { c } { { * ( \mathrm { a } ) ~ 1 + \frac { 4 } { x - \frac { 5 } { 4 } + \frac { 2 1 } { x + \frac { 1 } { 4 } } } } } \\ { { ( \mathrm { b } ) ~ \frac { 2 } { x - \frac { 1 } { 4 } + \displaystyle \frac { \frac { 2 3 } { 8 } } { x - \frac { 6 3 } { 9 2 } - \frac { \frac { 4 0 6 } { 5 2 9 } } { x + \frac { 3 3 } { 2 3 } } } } } } \end{array}
$$

9. For $f ( x ) = e ^ { x }$ we have the following approximations.

$r _ { T _ { 2 , 0 } } ( x ) = ( 1 . 2 6 6 0 6 6 T _ { 0 } ( x ) - 1 . 1 3 0 3 1 8 T _ { 1 } ( x ) + 0 . 2 7 1 4 9 5 3 T _ { 2 } ( x ) ) / T _ { 0 } ( x )$ $r _ { T _ { 1 , 1 } } ( x ) = ( 0 . 9 9 4 5 7 0 5 T _ { 0 } ( x ) - 0 . 4 5 6 9 0 4 6 T _ { 1 } ( x ) ) / ( T _ { 0 } ( x ) + 0 . 4 8 0 3 8 7 4 5 T _ { 1 } ( x )$ x)) $r _ { T _ { 0 , 2 } } ( x ) = 0 . 7 9 4 0 2 2 0 T _ { 0 } ( x ) / ( T _ { 0 } ( x ) + 0 . 8 7 7 8 5 7 5 T _ { 1 } ( x ) + 0 . 1 7 7 4 2 6 6 T _ { 2 } ( x ) )$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>TT2.0(xi)</td><td>rT1,1(xi)</td><td>TT0，2(xi)</td></tr><tr><td>1</td><td>0.25</td><td>0.77880078</td><td>0.74592811</td><td>0.78595377</td><td>0.74610974</td></tr><tr><td>2</td><td>0.50</td><td>0.60653066</td><td>0.56515935</td><td>0.61774075</td><td>0.58807059</td></tr><tr><td>3</td><td>1.00</td><td>0.36787944</td><td>0.40724330</td><td>0.36319269</td><td>0.38633199</td></tr></table>

10. For $f ( x ) = \cos x$ we have the following approximations.

$m = 3$ , $n = 0$ and $m = 2 , n = 1$ :

$$
\frac { \cup . \ i \cup \cup \cup \bigcirc \cup . 0 1 0 ( . 4 ) } { T _ { 0 } ( x ) + 0 . 3 0 0 3 2 3 8 T _ { 2 } ( x ) }
$$

$m = 1$ , $n = 2$ and $m = 0 , n = 3$ :

$$
\frac { 0 . 7 6 5 1 9 7 5 T _ { 0 } ( x ) - 0 . 2 2 9 8 0 7 0 T _ { 2 } ( x ) } { T _ { 0 } ( x ) }
$$

This gives

<table><tr><td>C</td><td>f(x)</td><td>rT0,3(x） and rT1,2(x)</td><td>TT2,1（x） and rT3,0(x)</td></tr><tr><td>0.78539816</td><td>0.70710678</td><td>0.68276861</td><td>0.71149148</td></tr><tr><td>1.04719755</td><td>0.50000000</td><td>0.53792021</td><td>0.49098135</td></tr></table>

11. For $f ( x ) = \sin { x }$ we have the following approximations.

$$
r _ { T _ { 2 , 2 } } ( x ) = \frac { 0 . 9 1 7 4 7 T _ { 1 } ( x ) } { T _ { 0 } ( x ) + 0 . 0 8 8 9 1 4 T _ { 2 } ( x ) }
$$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>TT2,2(xi)</td></tr><tr><td>0</td><td>0.00</td><td>0.00000000</td><td>0.00000000</td></tr><tr><td>1</td><td>0.10</td><td>0.09983342</td><td>0.09093843</td></tr><tr><td>2</td><td>0.20</td><td>0.19866933</td><td>0.18028797</td></tr><tr><td>3</td><td>0.30</td><td>0.29552021</td><td>0.26808992</td></tr><tr><td>4</td><td>0.40</td><td>0.38941834</td><td>0.35438412</td></tr></table>

12. For $f ( x ) = e ^ { x }$ we have the following degree five approximations. When $m = 5 , n = 0$ :

When $m = 4 , n = 1$ :

When $m = 3 , n = 2$ :

When $m = 2 , n = 3$ :

When $m = 1 , n = 4$ :

$m = 0 , n = 5$ :

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>TTo,5(xi)</td><td>rT1,4(xi)</td><td>TT2,3(xi)</td><td>TT3,2(xi)</td><td>TT4,1(xi)</td><td>TT5,0(xi)</td></tr><tr><td>1</td><td>0.2</td><td>1.22140276</td><td>1.22137251</td><td>1.22142042</td><td>1.22140929</td><td>1.22141264</td><td>1.29573091</td><td>1.22142198</td></tr><tr><td>2</td><td>0.4</td><td>1.49182470</td><td>1.49190745</td><td>1.49184755</td><td>1.49184841</td><td>1.49183231</td><td>1.54914242</td><td>1.49179061</td></tr><tr><td>3</td><td>0.6</td><td>1.82211880</td><td>1.82224269</td><td>1.82211712</td><td>1.82213166</td><td>1.82211572</td><td>1.84678705</td><td>1.82208177</td></tr><tr><td>4</td><td>0.8</td><td>2.22554093</td><td>2.22539680</td><td>2.22551178</td><td>2.22550877</td><td>2.22553290</td><td>2.19970546</td><td>2.22557527</td></tr><tr><td>5</td><td>1.0</td><td>2.71828183</td><td>2.71856417</td><td>2.71831087</td><td>2.71832589</td><td>2.71828966</td><td>2.62151591</td><td>2.71823332</td></tr></table>

13. (a) $e ^ { x } = e ^ { M \ln \sqrt { 1 0 } + s } = e ^ { M \ln \sqrt { 1 0 } } e ^ { s } = e ^ { \ln 1 0 \frac { M } { 2 } } e ^ { s } = 1 0 ^ { \frac { M } { 2 } } e ^ { s }$ (b) $e ^ { s } \approx \left( 1 + { \frac { 1 } { 2 } } s + { \frac { 1 } { 1 0 } } s ^ { 2 } + { \frac { 1 } { 1 2 0 } } s ^ { 3 } \right) / \left( 1 - { \frac { 1 } { 2 } } s + { \frac { 1 } { 1 0 } } s ^ { 2 } - { \frac { 1 } { 1 2 0 } } s ^ { 3 } \right)$ , with $| \mathrm { e r r o r } | \le 3 . 7 5 \times 1 0 ^ { - 7 }$ . (c) S $\mathrm { * } ~ M = \mathrm { r o u n d } ( 0 . 8 6 8 5 8 8 9 6 3 8 x ) , ~ s = x - M / ( 0 . 8 6 8 5 8 8 9 6 3 8 )$ , and $\hat { f } = \left( 1 + \frac { 1 } { 2 } s + \frac { 1 } { 1 0 } s ^ { 2 } + \frac { 1 } { 1 2 0 } s ^ { 3 } \right) / \left( 1 - \frac { 1 } { 2 } s + \frac { 1 } { 1 0 } s ^ { 2 } - \frac { 1 } { 1 2 0 } s ^ { 3 } \right) .$ Then $f = ( 3 . 1 6 2 2 7 7 6 6 ) ^ { M } \hat { f }$ .

$^ { * } 1 4$ . (a) Since

$$
\sin | x | = \sin ( M \pi + s ) = \sin M \pi \cos s + \cos M \pi \sin s = ( - 1 ) ^ { M } \sin s ,
$$

we have

$$
\sin x = { \mathrm { ~ s i g n ~ } } x \sin | x | = \operatorname { s i g n } { \big ( } x { \big ) } ( - 1 ) ^ { M } \sin s .
$$

(b) We have

$$
\sin x \approx \left( s - { \frac { 3 1 } { 2 9 4 } } s ^ { 3 } \right) \left/ \left( 1 + { \frac { 3 } { 4 9 } } s ^ { 2 } + { \frac { 1 1 } { 5 8 8 0 } } s ^ { 3 } \right) , \right.
$$

with $| \mathrm { e r r o r } | \le 2 . 8 4 \times 1 0 ^ { - 4 }$ .

(c) Set $M = \operatorname { R o u n d } ( | x | / \pi )$ , $s = | x | - M \pi$ , and $f _ { 1 } = \left( s - \frac { 3 1 } { 2 9 4 } s ^ { 3 } \right) \bigg / \left( 1 + \frac { 3 } { 4 9 } s ^ { 2 } + \frac { 1 1 } { 5 8 8 0 } s ^ { 4 } \right) .$ Then $f = ( - 1 ) ^ { M } f _ { 1 } \cdot x / | x |$ is the approximation.

(d) Set $y = x + { \frac { \pi } { 2 } }$ , and repeat part (c) with $y$ in place of $x$

# Exercise Set 8.5, page 546

$$
S _ { 2 } ( x ) = \frac { \pi ^ { 2 } } { 3 } - 4 \cos x + \cos 2 x
$$

2. $S _ { 3 } ( x ) = 2 \sin x - \sin 2 x$

3. $\begin{array} { r l r } { S _ { 3 } ( x ) } & { = } & { 3 . 6 7 6 0 7 8 - 3 . 6 7 6 0 7 8 \cos x + 1 . 4 7 0 4 3 1 \cos 2 x - 0 . 7 3 5 2 1 5 6 \cos 3 x + 3 . 6 7 6 0 7 8 \sin 3 x } \end{array}$ x − $2 . 9 4 0 8 6 2 \sin { 2 x }$

4. The general trigonometric least-squares polynomial is

$$
\begin{array} { l } { { \displaystyle S _ { n } ( x ) = \frac { e ^ { \pi } - e ^ { - \pi } } { 2 \pi } + \frac { ( - 1 ) ^ { n } e ^ { \pi } + ( - 1 ) ^ { n + 1 } e ^ { - \pi } } { \pi ( n ^ { 2 } + 1 ) } \cos n x } } \\ { { \displaystyle \qquad + \frac { 1 } { \pi } \sum _ { k = 1 } ^ { n - 1 } \left[ \frac { ( - 1 ) ^ { k } e ^ { \pi } + ( - 1 ) ^ { k + 1 } e ^ { - \pi } } { k ^ { 2 } + 1 } \right] ( \cos k x - k \sin k x ) . } } \end{array}
$$

$$
S _ { n } ( x ) = { \frac { 1 } { 2 } } + { \frac { 1 } { \pi } } \sum _ { k = 1 } ^ { n - 1 } { \frac { 1 - ( - 1 ) ^ { k } } { k } } \sin k x 
$$

6. The general trigonometric least-squares polynomial is

$$
S _ { n } ( x ) = \sum _ { k = 1 } ^ { n - 1 } { \frac { 2 } { k \pi } } \left( 1 - ( - 1 ) ^ { k } \right) \sin k x .
$$

7. The trigonometric least-squares polynomials are:

\*(a) $S _ { 2 } ( x ) = \cos { 2 x }$   
(b) $S _ { 2 } ( x ) = 0$   
(c) $S _ { 3 } ( x ) = 1 . 5 6 6 4 5 3 + 0 . 5 8 8 6 8 1 5 \cos x - 0 . 2 7 0 0 6 4 2 \cos 2 x + 0 . 2 1 7 5 6 7 9 \cos 3 x + 0 . 8 3 4 1 6 4 0 \sin x - 0 . 0 0 0 0 0 1 1 \sin 2 x \cos 3 x$ $0 . 3 0 9 7 8 6 6 \sin { 2 x }$   
(d) $S _ { 3 } ( x ) = - 2 . 0 4 6 3 2 6 + 3 . 8 8 3 8 7 2 \cos x - 2 . 3 2 0 4 8 2 \cos 2 x + 0 . 7 3 1 0 8 1 8 \cos 3 x$

8. \*(a) $E ( S _ { 2 } ) = 0$ (b) $E ( S _ { 2 } ) = 4$ (c) $E ( S _ { 3 } ) = 0 . 8 2 5 9 8 1 4$ (d) $E ( S _ { 3 } ) = 1 . 9 3 6 6 6 8$

9. The trigonometric least-squares polynomial is

$S _ { 3 } ( x ) = - 0 . 4 9 6 8 9 2 9 + 0 . 2 3 9 1 9 6 5 \cos x + 1 . 5 1 5 3 9 3 \cos 2 x + 0 . 2 3 9 1 9 6 5 \cos 3 x - 1 . 1 5 0 6 4 9 \sin x ,$

with error $E ( S _ { 3 } ) = 7 . 2 7 1 1 9 7$ .

\*10. The trigonometric least-squares polynomial is

with error 107.913.

The approximation in Exercise 10 is better because, in this case,

$$
\sum _ { j = 0 } ^ { 1 0 } \left( f ( \xi _ { j } ) - S _ { 3 } ( \xi _ { j } ) \right) ^ { 2 } = 3 9 7 . 3 6 7 8 ,
$$

whereas the approximation in Exercise 9 has

$$
\sum _ { j = 0 } ^ { 1 0 } ( f ( \xi _ { j } ) - S _ { 3 } ( \xi _ { j } ) ) ^ { 2 } = 5 6 9 . 3 5 8 9 .
$$

11. The trigonometric least-squares polynomials and their errors are

(a)

with $E ( S _ { 3 } ) = 2 1 0 . 9 0 4 5 3$ .

(b)

with $E ( S _ { 4 } ) = 1 6 9 . 4 9 4 3$ .

12. (a) The trigonometric least-squares polynomial is

(b) $\int _ { 0 } ^ { 1 } S _ { 4 } ( x ) d x = 0 . 2 7 7 2 1 4 8 6$ (c) $\int _ { 0 } ^ { 1 } x ^ { 2 } \sin x d x = 0 . 2 2 3 2 4 4 3$

13. Let $f ( - x ) = - f ( x )$ . The integral $\textstyle \int _ { - a } ^ { 0 } f ( x ) d x$ under the change of variable $t = - x$ transforms to

$$
- \int _ { a } ^ { 0 } f ( - t ) \ d t = \int _ { 0 } ^ { a } f ( - t ) \ d t = - \int _ { 0 } ^ { a } f ( t ) \ d t = - \int _ { 0 } ^ { a } f ( x ) \ d x .
$$

Thus,

$$
\int _ { - a } ^ { a } f ( x ) \ d x = \int _ { - a } ^ { 0 } f ( x ) \ d x + \int _ { 0 } ^ { a } f ( x ) \ d x = - \int _ { 0 } ^ { a } f ( x ) \ d x + \int _ { 0 } ^ { a } f ( x ) \ d x = 0 .
$$

14. Let $f ( - x ) = f ( x )$ . The integral $\textstyle \int _ { - a } ^ { 0 } f ( x ) d x$ under the change of variable $t = - x$ transforms to

$$
- \int _ { a } ^ { 0 } f ( - t ) \ d t = \int _ { 0 } ^ { a } f ( - t ) \ d t = \int _ { 0 } ^ { a } f ( t ) \ d t = \int _ { 0 } ^ { a } f ( x ) \ d x .
$$

Thus

$$
\int _ { - a } ^ { a } f ( x ) \ d x = \int _ { - a } ^ { 0 } f ( x ) \ d x + \int _ { 0 } ^ { a } f ( x ) \ d x = \int _ { 0 } ^ { a } f ( x ) \ d x + \int _ { 0 } ^ { a } f ( x ) \ d x = 2 \int _ { 0 } ^ { a } f ( x ) \ d x .
$$

$^ \mathrm { * _ { 1 5 } }$ . The following integrations establish the orthogonality.

$$
\begin{array} { r l } & { \displaystyle \int _ { - \infty } ^ { \infty } \{ \theta _ { 0 } ( x ) ^ { 2 } \log ( x ) \} ^ { 2 } d x = \frac { 1 } { 2 } \int _ { - \infty } ^ { \infty } d x = \pi , } \\ & { \displaystyle \int _ { - \infty } ^ { \infty } ( \psi _ { 0 } ( x ) ^ { 2 } ) d x = \int _ { - \infty } ^ { \infty } ( \cos k x ) ^ { 2 } d x = \int _ { - \infty } ^ { x } [ \frac { 1 } { 2 } + \frac { 1 } { 2 } \cos 2 k x ] d x = x + [ \frac { 1 } { 4 k } \sin 2 k x ] _ { - \infty } ^ { \infty } = x , } \\ & { \displaystyle \int _ { - \infty } ^ { x } [ \theta _ { 0 } ( x ) ( x ) ^ { 2 } + d x = \int _ { - \infty } ^ { x } ( \sin k x ) ^ { 2 } d x = \int _ { - \infty } ^ { x } [ \frac { 1 } { 2 } - \frac { 1 } { 2 } \cos 2 k x ] d x = \pi - [ \frac { 1 } { 4 k } \sin ^ { 2 } 2 k x ] _ { - \infty } ^ { \infty } = x ^ { \infty } } \\ & { \displaystyle \int _ { - \infty } ^ { x } \psi _ { 0 } ( x ) \partial _ { 0 } ( x ) d x = \frac { 1 } { 2 } \int _ { - \infty } ^ { x } \cos k x \mathrm { d } x = [ \frac { 1 } { 2 k } \sin k x ] _ { - \infty } ^ { \infty } = 0 , } \\ & { \displaystyle \int _ { - \infty } ^ { x } \psi _ { 0 } ( x ) \partial _ { 0 } ( x ) d x = \frac { 1 } { 2 } \int _ { - \infty } ^ { x } \sin k x \mathrm { d } x = [ \frac { - 1 } { 2 k } \cos k x ] _ { - \infty } ^ { \infty } = - \frac { 1 } { 2 k } \frac { 1 } { \cos k x } \cos ( - k x ) \mathrm { d } - 0 , } \\ & { \displaystyle \int _ { - \infty } ^ { x } \psi _ { 0 } ( x ) \partial _ { 0 } ( x ) d x = \int _ { - \infty } ^ { x } \cos k x \cos j x d x = \int _ { - \infty } ^ { x } [ \cos k x ] _ { - \infty } ^ { \infty } = x - j k x \mathrm { d } j x = 0 , } \\ &  \displaystyle \int _ { - \infty } ^ { x } \psi _ { 0 } ( x ) \partial _ { 0 } ( x ) d x = \int _ { - \infty } ^ { x } \cos k x \cos j x \end{array}
$$

and

$$
\int _ { - \pi } ^ { \pi } \phi _ { k } ( x ) \phi _ { n + j } ( x ) d x = \int _ { - \pi } ^ { \pi } \cos k x \sin j x d x = { \frac { 1 } { 2 } } \int _ { - \pi } ^ { \pi } [ \sin ( k + j ) x - \sin ( k - j ) x ] d x = 0 .
$$

16. The Fourier Series for $f ( x ) = \left| x \right|$ is

$$
S ( x ) = { \frac { \pi } { 2 } } + { \frac { 2 } { \pi } } \sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } - 1 } { k ^ { 2 } } } \cos k x .
$$

Assuming $f ( 0 ) = S ( 0 )$ gives

$$
0 = S ( 0 ) = \frac { \pi } { 2 } + \frac { 2 } { \pi } \sum _ { k = 1 } ^ { \infty } \frac { ( - 1 ) ^ { k } - 1 } { k ^ { 2 } } ,
$$

but

$$
\sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } - 1 } { k ^ { 2 } } } = - { \frac { 2 } { 1 ^ { 2 } } } + { \frac { 0 } { 2 ^ { 2 } } } - { \frac { 2 } { 3 ^ { 2 } } } + { \frac { 0 } { 4 ^ { 2 } } } + \cdots = - \sum _ { k = 0 } ^ { \infty } { \frac { 2 } { ( 2 k + 1 ) ^ { 2 } } } .
$$

Thus

$$
0 = \frac { \pi } { 2 } - \frac { 2 } { \pi } \sum _ { k = 0 } ^ { \infty } \frac { 2 } { ( 2 k + 1 ) ^ { 2 } } ,
$$

from which

$$
\sum _ { k = 0 } ^ { \infty } { \frac { 1 } { ( 2 k + 1 ) ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 8 } }
$$

follows.

17. The steps are nearly identical to those for determining the constants $b _ { k }$ except for the additional constant term $a _ { 0 }$ in the cosine series. In this case

$$
\frac { \partial E } { \partial a _ { 0 } } = 2 \sum _ { j = 0 } ^ { 2 m - 1 } [ y _ { j } - S _ { n } ( x _ { j } ) ] ( - 1 / 2 ) = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } - \sum _ { j = 0 } ^ { 2 m - 1 } \left( \frac { a _ { 0 } } { 2 } + a _ { n } \cos n x _ { j } + \sum _ { k = 1 } ^ { n - 1 } ( a _ { k } \cos k x _ { j } + b _ { k } \sin k x _ { k } ) \right) ,
$$

The orthogonality implies that only the constant term remains in the second sum. So

$$
0 = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } - { \frac { a _ { 0 } } { 2 } } ( 2 m ) \quad { \mathrm { w h i c h ~ i m p l i e s ~ t h a t } } \quad a _ { 0 } = { \frac { 1 } { m } } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } .
$$

# Exercise Set 8.6, page 557

1. The trigonometric interpolating polynomials are:

\*(a) $S _ { 2 } ( x ) = - 1 2 . 3 3 7 0 1 + 4 . 9 3 4 8 0 2 \cos x - 2 . 4 6 7 4 0 1 \cos 2 x + 4 . 9 3 4 8 0 2 \sin x$ (b) $S _ { 2 } ( x ) = - 6 . 1 6 8 5 0 3 + 9 . 8 6 9 6 0 4 \cos x - 3 . 7 0 1 1 0 2 \cos 2 x + 4 . 9 3 4 8 0 2 \sin x$ (c) $S _ { 2 } ( x ) = 1 . 5 7 0 7 9 6 - 1 . 5 7 0 7 9 6 \cos x$   
(d) $S _ { 2 } ( x ) = - 0 . 5 - 0 . 5 \cos 2 x + \sin x$

2. Parts (a) and (b) give the same answer: The trigonometric interpolating polynomial is

$\mathfrak { I } _ { 4 } ( x ) = \mathrm { ~ - ~ } 4 . 6 2 6 3 7 7 + 6 . 6 7 9 5 1 8 \cos x - 3 . 7 0 1 1 0$ $. 6 7 9 5 1 8 \cos x - 3 . 7 0 1 1 0 2 \cos 2 x + 3 . 1 9 0 0 8 6 \cos ^ { \circ } { \cos ^ { \circ } }$ $0 1 1 0 2 \cos 2 x + 3 . 1 9 0 0 8 6 \cos 3 x - 1 . 5 4 2 1 2 6 \cos 4 ;$ x + 5. $9 5 6 6 8 3 3 \sin x - 2 . 4 6 7 4 0 1 \sin 2 x + 1 . 0 2 2 0 3 1 \sin 3 x$ .

3. The Fast Fourier Transform Algorithm gives the following trigonometric interpolating polynomials.

(a) $S _ { 4 } ( x ) = - 1 1 . 1 0 3 3 1 + 2 . 4 6 7 4 0 1 \cos x - 2 . 4 6 7 4 0 1 \cos 2 x + 2 . 4 6 7 4 0 1 \cos 3 x - 1 . 2 3 3 7 0 1 \cos 4 x + 2 . 1 4 6 7 2 \cos 3 x$ 5.9568 $\mathtt { 3 \sin { x } - 2 . 4 6 7 4 0 1 \sin { 2 x } + 1 . 0 2 2 0 3 0 \sin { 3 x } }$

(b) $S _ { 4 } ( x ) = 1 . 5 7 0 7 9 6 - 1 . 3 4 0 7 5 9 \cos x - 0 . 2 3 0 0 3 7 8 \cos 3 x$ (c) $S _ { 4 } ( x ) = - 0 . 1 2 6 4 2 6 4 + 0 . 2 6 0 2 7 2 4 \cos x - 0 . 3 0 1 1 1 4 0 \cos 2 x + 1 . 1 2 1 3 7 2 \cos 3 x + 0 . 0 4 5 8 9 6 4 8 \cos 2 x$ 4x− 0.1022190 $\sin x + 0 . 2 7 5 4 0 6 2 \sin 2 x - 2 . 0 5 2 9 5 5 \sin 3 x$

(d) $S _ { 4 } ( x ) = - 0 . 1 5 2 6 8 1 9 + 0 . 0 4 7 5 4 2 7 8 \cos x + 0 . 6 8 6 2 1 1 4 \cos 2 x - 1 . 2 1 6 9 1 3 \cos 3 x + 1 . 1 7 6 1 4 3 \cos 4 x - 0 . 0 0 0 0 1 1 1 \sin 6 x$ 0.817938 $\sin x + 0 . 1 8 0 2 4 5 0 \sin 2 x + 0 . 2 7 5 3 4 0 2 \sin 3 x$

$^ { * } 4$ . (a) The trigonometric interpolating polynomial is

$S _ { 4 } ( x ) = 0 . 1 7 3 5 5 0 0 - 0 . 0 2 4 7 5 4 9 8 \cos ( 2 x - 1 ) \pi - 0 . 0 6 9 7 5 7 0 \cos 2 ( 2 x - 1 ) \pi$ $+ 0 . 0 8 4 6 8 3 1 7 \cos 3 ( 2 x - 1 ) \pi - 0 . 0 4 3 8 6 4 7 9 \cos 4 ( 2 x - 1 ) \pi$ + 0.2268260 sin(2x − 1)π $- 0 . 1 0 2 1 6 4 0 \sin 2 ( 2 x - 1 ) \pi + 0 . 0 4 2 8 4 6 4 8 \sin 3 ( 2 x - 1 ) \pi$ .

(b) 0.1735500   
(c) 0.2232443

5. The trigonometric polynomials give the following integral approximations.

<table><tr><td>Approximation</td><td>Actual</td></tr><tr><td>(a) -69.76415</td><td>-62.01255</td></tr><tr><td>(b) 9.869602</td><td>9.869604</td></tr><tr><td>（c） -0.7943605</td><td>-0.2739383</td></tr><tr><td>(d) -0.9593287</td><td>-0.9557781</td></tr></table>

6. The $b _ { k }$ terms are all zero. The $a _ { k }$ terms are

$a _ { 0 } = - 4 . 0 1 2 8 7 5 8 6$ , $a _ { 1 } = 3 . 8 0 2 7 6 9 0 3$ , $a _ { 2 } = - 2 . 2 3 5 1 9 8 7 0$ , $a _ { 3 } = 0 . 6 3 8 1 0 4 0 3$ , $a _ { 4 } = - 0 . 3 1 5 5 0 8 2 1$ , $a _ { 5 } = 0 . 1 9 4 0 8 1 4 5$ , $a _ { 6 } = - 0 . 1 3 4 6 4 4 9 1$ , $a _ { 7 } = 0 . 1 0 1 0 0 5 9 3$ , $a _ { 8 } = - 0 . 0 8 0 1 5 7 0 8$ , $a _ { 9 } = 0 . 0 6 6 4 3 5 9 8$ , $a _ { 1 0 } = - 0 . 0 5 7 0 4 3 5 3$ , $a _ { 1 1 } = 0 . 0 5 0 4 6 6 7 5$ , $a _ { 1 2 } = - 0 . 0 4 5 8 3 4 3 1$ , $a _ { 1 3 } = 0 . 0 4 2 6 2 3 1 8$ , $a _ { 1 4 } = - 0 . 0 4 0 5 1 3 9 5$ , $a _ { 1 5 } = 0 . 0 3 9 3 1 5 8 4$ , and $a _ { 1 6 } = - 0 . 0 3 8 9 2 7 1 3$ .

7. The $b _ { j }$ terms are all zero. The $a _ { j }$ terms are as follows:

$^ { * } 8$ . Since $( \cos x ) ^ { 2 } = { \frac { 1 } { 2 } } + { \frac { 1 } { 2 } } \cos 2 x$

$$
\sum _ { j = 0 } ^ { 2 m - 1 } ( \cos m x _ { j } ) ^ { 2 } = \frac { 1 } { 2 } \sum _ { j = 0 } ^ { 2 m - 1 } 1 + \frac { 1 } { 2 } \sum _ { j = 0 } ^ { 2 m - 1 } \cos 2 m x _ { j } = m + \frac { 1 } { 2 } \sum _ { j = 0 } ^ { 2 m - 1 } \cos 2 m x _ { j } .
$$

However,

$$
\cos 2 m x _ { j } = \cos 2 m \left( - \pi + { \frac { j } { m } } \pi \right) = \cos ( 2 j \pi - 2 m \pi ) = \cos ( 2 j - 2 m ) \pi = ( - 1 ) ^ { 2 j - 2 m } = 1 .
$$

Thus

$$
\sum _ { j = 0 } ^ { 2 m - 1 } ( \cos m x _ { j } ) ^ { 2 } = m + \frac { 1 } { 2 } \sum _ { j = 0 } ^ { 2 m - 1 } 1 = m + m = 2 m .
$$

\*9. From Eq. (8.28),

$$
c _ { k } = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } e ^ { \frac { \pi i j k } { m } } = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } ( \zeta ) ^ { j k } = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } \left( \zeta ^ { k } \right) ^ { j } .
$$

Thus

$$
\begin{array} { r } { c _ { k } = \left( 1 , \zeta ^ { k } , \zeta ^ { 2 k } , \dots , \zeta ^ { \left( 2 m - 1 \right) k } \right) ^ { t } \left[ \begin{array} { c } { y _ { 0 } } \\ { y _ { 1 } } \\ { \vdots } \\ { y _ { 2 m - 1 } } \end{array} \right] , } \end{array}
$$

and the result follows.

10. We have $\mathbf { c } = A \mathbf { d }$ , $\mathbf { d } = B \mathbf { e }$ , $\mathbf { e } = C \mathbf { f }$ , and $\mathbf { f } = D \mathbf { y }$ , where

$$
\begin{array} { r } { A = \left[ \begin{array} { c c c c c c c c c c } { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 1 } \\ { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } \end{array} \right] , \quad B = \left[ \begin{array} { c c c c c c c c c c } { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - i } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { - i } & { - i } \\ { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } \end{array} \right] , } \end{array}
$$

$$
C = \left[ \begin{array} { c c c c c c c c c } { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - i } & { - i } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \frac { - i + 1 } { \sqrt { 2 } } } & { \frac { - i + 1 } { \sqrt { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \frac { - i - 1 } { \sqrt { 2 } } } & { \frac { - i - 1 } { \sqrt { 2 } } } \\ { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } \end{array} \right] ,
$$

and

$$
D = \left[ \begin{array} { c c c c c c c c } { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { i } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { i } & { 0 } \\ { 0 } & { \frac { i - 1 } { \sqrt { 2 } } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \frac { i - 1 } { \sqrt { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \frac { - ( i + 1 ) } { \sqrt { 2 } } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \frac { ( i + 1 ) } { \sqrt { 2 } } } \end{array} \right] .
$$

Note that $\mathbf { c } = A B C D \mathbf { y }$ , which would give Eq. (8.28) if expanded.

# Approximating Eigenvalues

# Exercise Set 9.1, page 568

1. \*(a) The eigenvalues and associated eigenvectors are $\lambda _ { 1 } = 2 , \mathbf { v } ^ { ( 1 ) } = ( 1 , 0 , 0 ) ^ { t }$ ; $\lambda _ { 2 } = 1 , \mathbf { v } ^ { ( 2 ) } =$ $( 0 , 2 , 1 ) ^ { t }$ ; and $\lambda _ { 3 } = - 1 , \mathbf { v } ^ { ( 3 ) } = ( - 1 , 1 , 1 ) ^ { t }$ . The set is linearly independent. (b) The eigenvalues and associated eigenvectors are $\lambda _ { 1 } = 2 , \mathbf { v } ^ { ( 1 ) } = ( 0 , 1 , 0 ) ^ { t }$ ; $\lambda _ { 2 } = 3 , { \bf v } ^ { ( 2 ) } =$ $( 1 , 0 , 1 ) ^ { t }$ ; and $\lambda _ { 3 } = 1 , \mathbf { v } ^ { ( 3 ) } = ( 1 , 0 , - 1 ) ^ { t }$ . The set is linearly independent. (c) The eigenvalues and associated eigenvectors are $\lambda _ { \underline { { { 1 } } } } = 1 , { \bf v } ^ { ( 1 ) } = ( 0 , - 1 , 1 ) ^ { t } ; \lambda _ { 2 } = 1 +$ $\sqrt { 2 } , \mathbf { v } ^ { ( 2 ) } = ( \sqrt { 2 } , 1 , 1 ) ^ { t }$ ; and $\lambda _ { 3 } = 1 - \sqrt { 2 } , \mathbf { v } ^ { ( 3 ) } = ( - \sqrt { 2 } , 1 , 1 ) ^ { t } .$ . The set is linearly independent. (d) The eigenvalues and associated eigenvectors are $\lambda _ { 1 } = \lambda _ { 2 } = 2$ with $\mathbf { v } ^ { ( 1 ) } = ( 1 , 0 , 0 ) ^ { t }$ and $\lambda _ { 3 } = 3$ with $\mathbf { v } ^ { ( 3 ) } = ( 0 , 1 , 1 ) ^ { t }$ . There are not three linearly independent eigenvectors.   
2. (a) Eigenvalue $\lambda _ { 1 } ~ = ~ 1$ has multiplicity 3 and eigenvectors $\mathbf { v } ^ { ( 1 ) } = ( - 1 , 1 , 0 ) ^ { t }$ and ${ \bf v } ^ { ( 2 ) } =$ $( 1 , 0 , 1 ) ^ { t }$ . There are not three linearly independent eigenvectors. (b) Eigenvalue $\lambda _ { 1 } ~ = ~ 3$ has multiplicity 2 and eigenvectors $\mathbf { v } ^ { ( 1 ) } = ( - 1 , 1 , 0 ) ^ { t }$ and ${ \bf v } ^ { ( 2 ) } =$ $( - 1 , 0 , 1 ) ^ { t }$ . Eigenvalue $\lambda _ { 2 } = 0$ has eigenvector $\mathbf { v } ^ { ( 3 ) } = ( 1 , 1 , 1 ) ^ { t }$ . There are three linearly independent eigenvectors. (c) Eigenvalue $\lambda _ { 1 } = 4$ has eigenvector $\mathbf { v } ^ { ( 1 ) } = ( 1 , 1 , 1 ) ^ { t }$ . Eigenvalue $\lambda _ { 2 } = 1$ has multiplicity 2 and eigenvectors $\mathbf { v } ^ { ( 2 ) } = ( - 1 , 1 , 0 ) ^ { t }$ and $\mathbf { v } ^ { ( 3 ) } = ( - 1 , 0 , 1 ) ^ { t }$ . There are three linearly independent eigenvectors. (d) Eigenvalue $\lambda _ { 1 } ~ = ~ 2$ has multiplicity 2 and eigenvectors $\mathbf { v } ^ { ( 1 ) } \ = \ ( 1 , 0 , 0 ) ^ { t }$ and ${ \bf v } ^ { ( 2 ) } =$ $( 0 , - 1 , 1 ) ^ { t }$ . Eigenvalue $\lambda _ { 2 } = 3$ has eigenvector $\mathbf { v } ^ { ( 3 ) } = ( 1 , 1 , 0 ) ^ { t }$ . There are three linearly independent eigenvectors.

3. The eigenvalues are within the Gerˇsgorin circles that are shown.

(a) The three eigenvalues are within $\{ \lambda | | \left| \lambda \right| \leq 2 \} \cup \{ \lambda | | \left| \lambda - 2 \right| \leq 2 \}$ so $\rho ( A ) \leq 4$ .

![](images/415498a97e541154ddd14dfc43d29df2c69db064ad3e92eb960de4b75e491f13.jpg)

(b) The three eigenvalues are within $\{ \lambda | \ | \lambda - 4 | \le 2 \}$ so $\rho ( A ) \leq 6$ .

![](images/907031ba5cffdcdc4b7883def90c31e9d2e9c20dca03c3149205f596e6acbf4e.jpg)

(c) The three real eigenvalues satisfy $0 \leq \lambda \leq 6$ so $\rho ( A ) \leq 6$ .

![](images/4ffebbe294c13765f19e65b4dcaeade775bc19663ac74ef7e81152475f28cd49.jpg)

(d) The three real eigenvalues satisfy $1 . 2 5 \le \lambda \le 8 . 2 5$ so $1 . 2 5 \le \rho ( A ) \le 8 . 2 5$ .

![](images/af7bccc30961bb6ae1bbd1d10dadf4b06f8c6b6357a3da4d17769fa7afdea554.jpg)

4. The eigenvalues are within the Gerˇsgorin circles that are shown.

(a) The four real eigenvalues satisfy $- 8 \leq \lambda \leq 1$ , so $\rho ( A ) \leq 8$ .

![](images/0d401b2afa4916b2feed4fb937c30fcebf6644711317ec4f6324368f82d78bc9.jpg)

\*(b) The real eigenvalues satisfy $- 2 \leq \lambda \leq 6$ , so $\rho ( A ) \leq 6$ .

![](images/a52aaf2d0d16b06eca369418f7f46901196a7b0057f13f7f3130a3f09fa460fd.jpg)

(c) The four real eigenvalues satisfy $- 2 \leq \lambda \leq 6$ , so $\rho ( A ) \leq 6$ .

![](images/8c86f9040b68cb6a2203b1d5045b4ba04914a262a5dfaf0b0a1faea0f6160af7.jpg)

(d) The real eigenvalues satisfy either $1 \leq \lambda \leq 5$ or $6 \leq \lambda \leq 1 2$ , so $1 \leq \rho ( A ) \leq 1 2$

![](images/a44e99803ea9627d1ca8aa03aaa855641f45b12be0de117eb561e70a6bc8c5c0.jpg)

5. All the matrices except (d) have 3 linearly independent eigenvectors. The matrix in part (d) has only 2 linearly independent eigenvectors. One choice for $P$ is each case is

\*(a)

$$
\left[ { \begin{array} { r r r } { - 1 } & { 0 } & { 1 } \\ { 1 } & { 2 } & { 0 } \\ { 1 } & { 1 } & { 0 } \end{array} } \right] ,
$$

$$
\left[ { \begin{array} { r r r } { 0 } & { - 1 } & { 1 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \end{array} } \right] ,
$$

(c)

$$
\left[ { \begin{array} { r r r } { 0 } & { { \sqrt { 2 } } } & { - { \sqrt { 2 } } } \\ { - 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { 1 } \end{array} } \right] ,
$$

6. (a) This matrix is not factorable because it does not have 3 linearly independent eigenvectors. (b)

$$
P = \left[ { \begin{array} { c c c } { 1 } & { 1 } & { 1 } \\ { 1 } & { 0 } & { - 1 } \\ { 1 } & { - 1 } & { 0 } \end{array} } \right] , \quad P ^ { - 1 } = { \frac { 1 } { 3 } } \left[ { \begin{array} { c c c } { 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { - 2 } \\ { 1 } & { - 2 } & { 1 } \end{array} } \right] , \quad { \mathrm { a n d } } \quad D = P = \left[ { \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { 3 } & { 0 } \\ { 0 } & { 0 } & { 3 } \end{array} } \right] .
$$

(c)

$$
P = \left[ \begin{array} { c c c } { 1 } & { 1 } & { 1 } \\ { 0 } & { - 1 } & { 1 } \\ { - 1 } & { 0 } & { 1 } \end{array} \right] , \quad P ^ { - 1 } = \frac { 1 } { 3 } \left[ \begin{array} { c c c } { 1 } & { 1 } & { - 2 } \\ { 1 } & { - 2 } & { 1 } \\ { 1 } & { 1 } & { 1 } \end{array} \right] , \quad \mathrm { a n d } \quad D = P = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 4 } \end{array} \right] .
$$

(d)

$$
P = \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { - 1 } & { 0 } \end{array} } \right] , \quad P ^ { - 1 } = \left[ { \begin{array} { c c c } { 1 } & { - 1 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 1 } \end{array} } \right] , \quad \mathrm { a n d } \quad D = P = \left[ { \begin{array} { c c c } { 2 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 3 } \end{array} } \right] .
$$

7. The vectors are linearly dependent because $- 2 v _ { 1 } + 7 v _ { 2 } - 3 v _ { 3 } = 0$ .

$^ { * } 8$ . The vectors are linearly independent if and only if the matrix formed by having these vectors as columns (or rows) is nonsingular, which is true if and only if the determinant of this matrix is nonzero. Since

$$
\operatorname* { d e t } { \left[ \begin{array} { l l l } { 0 } & { 0 } & { - 2 } \\ { 1 } & { 2 } & { ~ 0 } \\ { 1 } & { 1 } & { ~ 1 } \end{array} \right] } = 2 ,
$$

the vectors are linearly independent.

9. If $c _ { 1 } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + c _ { k } \mathbf { v } _ { k } = \mathbf { 0 }$ , then for any $j$ , with $1 \le j \le k$ , we have $c _ { 1 } \mathbf { v } _ { j } ^ { t } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + c _ { k } \mathbf { v } _ { j } ^ { t } \mathbf { v } _ { k } = \mathbf { 0 }$ . But orthogonality gives $c _ { i } \mathbf { v } _ { j } ^ { t } \mathbf { v } _ { i } = 0$ , for $i \neq j$ , so $c _ { j } \mathbf { v } _ { j } ^ { t } \mathbf { v } _ { j } = 0$ and since $\mathbf { v } _ { j } ^ { t } \mathbf { v } _ { j } \neq 0$ , we must have $c _ { j } = 0$ .

$^ { * } 1 0$ . There must be a largest subset $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { j } \right\}$ , with $j ~ \leq ~ k$ that is linearly independent because the set with the nonzero vector $\{ { \bf x } _ { 1 } \}$ is linearly independent. Suppose that we have this largest linearly independent set and that $j < k$ . Then $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { j } , \mathbf { x } _ { j + 1 } \right\}$ is linearly dependent and there is a set of constants $\{ c _ { 1 } , c _ { 2 } , \ldots , c _ { j } \}$ , not all zero, with

$$
\mathbf { x } _ { j + 1 } = c _ { 1 } \mathbf { x } _ { 1 } + c _ { 2 } \mathbf { x } _ { 2 } + \cdot \cdot \cdot + c _ { j } \mathbf { x } _ { j } .
$$

Because these are all eigenvectors, $A { \bf x } _ { i } = \lambda _ { i } { \bf x } _ { i }$ for each $i = 1 , 2 , \ldots j + 1$ , so

$$
A \mathbf { x } _ { j + 1 } = \lambda _ { j + 1 } \mathbf { x } _ { j + 1 } = c _ { 1 } \lambda _ { 1 } \mathbf { x } _ { 1 } + c _ { 2 } \lambda _ { 2 } \mathbf { x } _ { 2 } + \cdot \cdot \cdot + c _ { j } \lambda _ { j } \mathbf { x } _ { j } .
$$

But we also have

$$
\lambda _ { j + 1 } \mathbf { x } _ { j + 1 } = c _ { 1 } \lambda _ { j + 1 } \mathbf { x } _ { 1 } + c _ { 2 } \lambda _ { j + 1 } \mathbf { x } _ { 2 } + \cdot \cdot \cdot + c _ { j } \lambda _ { j + 1 } \mathbf { x } _ { j } ,
$$

and subtracting these equations gives

$$
\mathbf { \Gamma } _ { + 1 } ) \mathbf { x } _ { 1 } + c _ { 2 } ( \lambda _ { 2 } - \lambda _ { j + 1 } ) \mathbf { x } _ { 2 } + \cdots c _ { j } ( \lambda _ { j } - \lambda _ { j + 1 } ) \mathbf { x } _ { j }
$$

But the set $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { j } \right\}$ was assumed to be linearly independent, so we must have

$$
0 = c _ { 1 } ( \lambda _ { 1 } - \lambda _ { j + 1 } ) = c _ { 2 } ( \lambda _ { 2 } - \lambda _ { j + 1 } ) = \cdots = c _ { j } ( \lambda _ { j } - \lambda _ { j + 1 } ) .
$$

Since eigenvalues are all distinct, this implies that $0 = c _ { 1 } = c _ { 2 } = \cdot \cdot \cdot = c _ { j }$ . This contradicts the original statement that $\mathbf { x } _ { j + 1 }$ could be written as a combination of the vectors $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { j }$ . The only assumption that was made was that $j < k$ , and this statement must be false. As a consequence, the entire set $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { k } \right\}$ must be linearly independent.

11. Since $\{ { \bf v } _ { i } \} _ { i = 1 } ^ { n }$ is linearly independent in $\mathbb { R } ^ { n }$ , there exist numbers $c _ { 1 } , \ldots , c _ { n }$ with

$$
\mathbf { x } = c _ { 1 } \mathbf { v } _ { 1 } + \cdots + c _ { n } \mathbf { v } _ { n } .
$$

Hence, for any $k$ , with $1 \leq k \leq n$ ,

$$
\mathbf { v } _ { k } ^ { t } \mathbf { x } = c _ { 1 } \mathbf { v } _ { k } ^ { t } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + c _ { n } \mathbf { v } _ { k } ^ { t } \mathbf { v } _ { n } = c _ { k } \mathbf { v } _ { k } ^ { t } \mathbf { v } _ { k } = c _ { k } .
$$

$^ { \ast } 1 2$ . Not necessarily. Consider the vectors $\mathbf { x } _ { 1 } = ( 1 , 0 ) ^ { t }$ , $\mathbf { x } _ { 2 } = ( 0 , 1 ) ^ { t }$ , and $\mathbf { x } _ { 3 } = ( 1 , 1 ) ^ { t }$ .

13. (a) (i) $\begin{array} { r } { | \mathbf { 0 } = c _ { 1 } ( 1 , 1 ) ^ { t } + c _ { 2 } ( - 2 , 1 ) ^ { t } \operatorname { i m p l i e s } \operatorname { t h a t } \left[ \begin{array} { l l } { 1 } & { - 2 } \\ { 1 } & { 1 } \end{array} \right] \left[ \begin{array} { l } { c _ { 1 } } \\ { c _ { 2 } } \end{array} \right] = \left[ \begin{array} { l } { 0 } \\ { 0 } \end{array} \right] . \operatorname { B u t } \operatorname* { d e t } \left[ \begin{array} { l l } { 1 } & { - 2 } \\ { 1 } & { 1 } \end{array} \right] = \left[ \begin{array} { l } { 0 } \\ { 1 } & { - 2 } \end{array} \right] . } \end{array}$ $3 \neq 0$ so by Theorem 6.7 we have $c _ { 1 } = c _ { 2 } = 0$ . (ii) $\{ ( 1 , 1 ) ^ { t } , ( - 3 / 2 , 3 / 2 ) ^ { t } \}$ . (iii) $\{ ( { \sqrt { 2 } } / 2 , { \sqrt { 2 } } / 2 ) ^ { t } , ( - { \sqrt { 2 } } / 2 , { \sqrt { 2 } } / 2 ) ^ { t } \} .$ .

(b) (i) The determinant of this matrix is $- 2 \neq 0$ , so $\{ ( 1 , 1 , 0 ) ^ { t } , ( 1 , 0 , 1 ) ^ { t } , ( 0 , 1 , 1 ) ^ { t } \}$ is a linearly independent set. (ii) (iii) $\begin{array} { r l } & { \{ ( 1 , 1 , 0 ) ^ { t } , ( 1 / 2 , - 1 / 2 , 1 ) ^ { t } , ( - 2 / 3 , 2 / 3 , 2 / 3 ) ^ { t } \} } \\ & { \{ ( \sqrt { 2 } / 2 , \sqrt { 2 } / 2 , 0 ) ^ { t } , ( \sqrt { 6 } / 6 , - \sqrt { 6 } / 6 , \sqrt { 6 } / 3 ) ^ { t } , ( - \sqrt { 3 } / 3 , \sqrt { 3 } / 3 , \sqrt { 3 } / 3 ) ^ { t } \} } \end{array}$

(c) (i) If $\mathbf { 0 } = c _ { 1 } ( 1 , 1 , 1 , 1 ) ^ { t } + c _ { 2 } ( 0 , 2 , 2 , 2 ) ^ { t } + c _ { 3 } ( 1 , 0 , 0 , 1 ) ^ { \textnormal { \scriptsize } }$ t, then we have $( E _ { 1 } ) : c _ { 1 } + c _ { 3 } = 0 , \quad ( E _ { 2 } ) : c _ { 1 } + 2 c _ { 2 } = 0 , \quad ( E _ { 3 } ) : c _ { 1 } + 2 c _ { 2 } = 0 , \quad ( E _ { 4 } ) : c _ { 1 } + 2 c _ { 2 } + c _ { 3 } = 0 .$ Subtracting ( $E _ { 3 }$ ) from ( $E _ { 4 }$ ) implies that $c _ { 3 } = 0$ . Hence, from ( $E _ { 1 }$ ) we have $c _ { 1 } = 0$ , and from ( $E _ { 2 }$ ) we have $c _ { 2 } = 0$ . The vectors are linearly independent. (ii) $\{ ( 1 , 1 , 1 , 1 ) ^ { t } , ( - 3 / 2 , 1 / 2 , 1 / 2 , 1 / 2 ) ^ { t } , ( 0 , - 1 / 3 , - 1$ 1/3, 2/3)t} (iii) $\{ ( 1 / 2 , 1 / 2 , 1 / 2 , 1 / 2 ) ^ { t } , ( - \sqrt { 3 } / 2 , \sqrt { 3 } / 6 , \sqrt { 3 } / 6 , \sqrt { 3 } / 6 ) ^ { t } , ( 0 , - \sqrt { 6 } / 6 , - \sqrt { 6 } / 6 , \sqrt { 6 } / 3 ) ^ { t } \}$

(d) (i) If $A$ is the matrix whose columns are the vectors $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \mathbf { v } _ { 3 } , \mathbf { v } _ { 4 } , \mathbf { v } _ { 5 }$ , then $\operatorname* { d e t } A = 6 0 \neq 0$ , so the vectors are linearly independent. (iii) (ii) $\begin{array} { r l } & { ( 2 , 2 , 3 , 2 , 3 ) ^ { t } , ( 2 , - 1 , 0 , - 1 , 0 ) ^ { t } , ( 0 , 0 , 1 , 0 , - 1 ) ^ { t } , ( 1 , 2 , - 1 , 0 , - 1 ) ^ { t } , ( - 2 / 7 , 3 / 7 , 2 / 7 , - 1 , 2 / 7 ) ^ { t } \} } \\ & { \{ ( \sqrt { 3 0 } / 1 5 , \sqrt { 3 0 } / 1 5 , \sqrt { 3 0 } / 1 0 , \sqrt { 3 0 } / 1 5 , \sqrt { 3 0 } / 1 0 ) ^ { t } , ( \sqrt { 6 } / 3 , - \sqrt { 6 } / 6 , 0 , - \sqrt { 6 } / 6 , 0 ) ^ { t } , } \\ & { \sqrt { 2 } / 2 , 0 , - \sqrt { 2 } / 2 ) ^ { t } , ( \sqrt { 7 } / 7 , 2 \sqrt { 7 } / 7 , - \sqrt { 7 } / 7 , 0 , - \sqrt { 7 } / 7 ) ^ { t } , } \\ & { 7 0 / 3 5 , 3 \sqrt { 7 0 } / 7 0 , \sqrt { 7 0 } / 3 5 , - \sqrt { 7 0 } / 1 0 , \sqrt { 7 0 } / 3 5 ) ^ { t } \} } \end{array}$

14. To show linear independence we will show that the matrix whose columns are the given vectors has a nonzero determinant. In case there are fewer vectors than the dimension of the space we can add a vector or vectors to complete the matrix. If the larger set is linearly independent, the original set will also be linearly independent.

(a) (i) The matrix has determinant 7. (ii) The set $\left\{ ( 2 , - 1 ) ^ { t } , { \frac { 1 } { 5 } } ( 1 , 2 ) ^ { t } \right\}$ is orthogonal. (iii) The set $\left\{ { \frac { \sqrt { 5 } } { 5 } } ( 2 , - 1 ) ^ { t } , { \frac { \sqrt { 5 } } { 5 } } ( 1 , 2 ) ^ { t } \right\}$ is orthonormal.

(b) (i) The matrix has determinant $- 2$ . (iii) The set (ii) The set $\begin{array} { r l } & { \left\{ ( 2 , - 1 , 1 ) ^ { t } , \frac { 1 } { 2 } ( 0 , 1 , 1 ) ^ { t } , \frac { 2 } { 3 } ( 1 , 1 , - 1 ) ^ { t } \right\} \mathrm { i s ~ o r t h o g o n a l } . } \\ & { \left\{ \frac { \sqrt { 6 } } { 6 } ( 2 , 1 - , 1 ) ^ { t } , \frac { \sqrt { 2 } } { 2 } ( 0 , 1 , 1 ) ^ { t } , \frac { \sqrt { 3 } } { 3 } ( 1 , 1 , - 1 ) ^ { t } \right\} \mathrm { i s ~ o r t h o n o r m a l } . } \end{array}$ (c) (i) The matrix with the vector $( 0 , 0 , 0 , 1 ) ^ { t }$ added in the last column has determinant 1. (iii) The set (ii) The set $\begin{array} { r l } & { \left\{ ( 1 , 1 , 1 , 1 ) ^ { t } , \frac { 1 } { 4 } ( - 3 , 1 , 1 , 1 ) ^ { t } , \frac { 1 } { 3 } ( 0 , - 2 , 1 , 1 ) ^ { t } \right\} \mathrm { i s ~ o r t h o g o n a l } . } \\ & { \left\{ \frac { 1 } { 2 } ( 1 , 1 , 1 , 1 ) ^ { t } , \frac { \sqrt { 3 } } { 6 } ( 3 , - 1 , - 1 , - 1 ) ^ { t } , \frac { \sqrt { 6 } } { 6 } ( 0 , - 2 , 1 , 1 ) ^ { t } \right\} \mathrm { i s ~ o r t h o n o r m a l } . } \end{array}$ (d) (i) The matrix with the vector $( 0 , 0 , 1 , 0 , 0 ) ^ { t }$ added in the last column has determinant 12. (ii) The set $\left\{ ( 2 , 2 , 0 , 2 , 1 ) ^ { t } , \frac { 3 } { 1 3 } ( - 5 , 8 , 0 , - 5 , 4 ) ^ { t } , \frac { 1 } { 1 0 } ( - 5 , 2 , 0 , 5 , - 4 ) ^ { t } , \frac { 4 } { 7 } ( - 1 , - 1 , 0 , 1 , 2 ) ^ { t } \right\} ^ { - 1 } ,$ is orthogonal. (iii) The set $\left\{ \frac { \sqrt { 1 3 } } { 1 3 } ( 2 , 2 , 0 , 2 , 1 ) ^ { t } , \frac { 1 3 \sqrt { 1 3 0 } } { 1 6 9 0 } ( 5 , - 8 , 0 , 5 , - 4 ) ^ { t } , \frac { \sqrt { 7 0 } } { 7 0 } ( 5 , - 2 , 0 , - 5 , 4 ) ^ { t } , - \frac { \sqrt { 7 } } { 7 } ( 1 , 1 , 0 , - 1 , - 2 ) ^ { t } \right\}$

is orthonormal.

$^ \ast 1 5$ . If $A$ is a strictly diagonally dominant matrix, then in each row, the sum of the magnitudes of the off-diagonal entries in the row are less than the magnitude of the diagonal entry in that row. By Gerˇsgorin Circle Theorem this implies that for each row the magnitude of the center of the Gerˇsgorin circle for that row exceeds the radius so the circle does not contain the origin. Hence 0 cannot be in any Gerˇsgorin circle and consequently cannot be an eigenvalue of $A$ . This implies that $A$ in nonsingular.

$^ *$ 16. Let $( X ) _ { k } = \left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { k } \right\}$ and define the set $( V ) _ { k } = \left\{ \mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \ldots , \mathbf { v } _ { k } \right\}$ in the Gram-Schmidt manner as

$$
\mathbf { v } _ { 1 } = \mathbf { x } _ { 1 } , \quad { \mathrm { a n d } } \quad \mathbf { v } _ { k } = \mathbf { x } _ { k } - \sum _ { i = 1 } ^ { k - 1 } \left( { \frac { \mathbf { v } _ { i } ^ { t } \mathbf { x } _ { k } } { \mathbf { v } _ { i } ^ { t } \mathbf { v } _ { i } } } \right) \mathbf { v } _ { i } .
$$

for each $k > 1$ . We will use Mathematical Induction to show that $( V ) _ { k }$ is orthogonal for every integer $k$ .

First note that since

$$
\mathbf { v } _ { 1 } = \mathbf { x } _ { 1 } , \quad { \mathrm { a n d } } \quad \mathbf { v } _ { 2 } = \mathbf { x } _ { 2 } - \left( { \frac { \mathbf { v } _ { 1 } ^ { t } \mathbf { x } _ { 2 } } { \mathbf { v } _ { 1 } ^ { t } \mathbf { v } _ { 1 } } } \right) \mathbf { v } _ { 1 } ,
$$

we have

$$
\mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { v } _ { 2 } = \mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { x } _ { 2 } - \left( { \frac { \mathbf { v } _ { 1 } ^ { t } \mathbf { x } _ { 2 } } { \mathbf { v } _ { 1 } ^ { t } \mathbf { v } _ { 1 } } } \right) \mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { v } _ { 1 } = \mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { x } _ { 2 } - \mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { x } _ { 2 } = 0 ,
$$

so $( V ) _ { 2 }$ is an orthogonal set.

Now assume that $( V ) _ { j }$ is orthogonal for some positive integer $j$ , and consider $( V ) _ { j + 1 }$ . Since $( V ) _ { j }$ is orthogonal the set $( V ) _ { j + 1 }$ will be orthogonal if and only if $\mathbf { v } _ { s } ^ { t } \cdot \mathbf { v } _ { j + 1 } = 0$ for each $s = 1 , 2 , \dots j$ .

For each $s = 1 , 2 , . . . j$ we have

$$
\begin{array} { l } { { \displaystyle { \bf v } _ { s } ^ { t } \cdot { \bf v } _ { j + 1 } ^ { t } = { \bf v } _ { s } ^ { t } \cdot { \bf x } _ { j + 1 } - \sum _ { i = 1 } ^ { j } \left( \frac { { \bf v } _ { i } ^ { t } { \bf x } _ { j + 1 } } { { \bf v } _ { i } ^ { t } { \bf v } _ { i } } \right) ( { \bf v } _ { s } ^ { t } \cdot { \bf v } _ { i } ) } \ ~ } \\ { { \displaystyle ~ = { \bf v } _ { s } ^ { t } \cdot { \bf x } _ { j + 1 } - \left( \frac { { \bf v } _ { s } ^ { t } { \bf x } _ { j + 1 } } { { \bf v } _ { s } ^ { t } { \bf v } _ { s } } \right) ( { \bf v } _ { s } ^ { t } \cdot { \bf v } _ { s } ) = { \bf v } _ { s } ^ { t } \cdot { \bf x } _ { j + 1 } - { \bf v } _ { s } ^ { t } \cdot { \bf x } _ { j + 1 } ^ { t } = 0 } . } \end{array}
$$

So $( V ) _ { j }$ being orthogonal implies that $( V ) _ { j + 1 }$ is also orthogonal. Mathematical Induction implies that $( V ) _ { j }$ is true for all positive integers $j$ .

17. (a) Let $\mu$ be an eigenvalue of $A$ . Since $A$ is symmetric, $\mu$ is real and Theorem 9.13 gives $0 \leq \mu \leq 4$ . The eigenvalues of $A - 4 I$ are of the form $\mu - 4$ . Thus,

$$
\rho ( A - 4 I ) = \operatorname* { m a x } \lvert \mu - 4 \rvert = \operatorname* { m a x } ( 4 - \mu ) = 4 - \operatorname* { m i n } \mu = 4 - \lambda = \lvert \lambda - 4 \rvert .
$$

(b) The eigenvalues of $A - 4 I$ are $- 3 . 6 1 8 0 3 4$ , $- 2 . 6 1 8 0 3 4$ , −1.381966, and $- 0 . 3 8 1 9 6 6$ , so $\rho ( A - 4 I ) = 3 . 6 1 8 0 3 4$ and $\lambda = 0 . 3 8 1 9 6 6$ . An eigenvector is $( 0 . 6 1 8 0 3 4 , 1 , 1 , 0 . 6 1 8 0 3 4 ) ^ { t }$ .

(c) As in part (a), $0 \le \mu \le 6$ , so $\lvert \lambda - 6 \rvert = \rho ( B - 6 I )$ .

(d) The eigenvalues of $B - 6 I$ are $- 5 . 2 3 6 0 6 7 3$ , $^ { - 4 }$ , $- 2$ , and $- 0 . 7 6 3 9 3 2 0 2$ , so $\rho ( B - 6 I ) =$ 5.2360673 and $\lambda = 0 . 7 6 3 9 3 2 7$ . An eigenvector is $( 0 . 6 1 8 0 3 3 9 5 , 1 , 1 , 0 . 6 1 8 0 3 9 5 ) ^ { \iota }$ t.

# Exercise Set 9.2, page 573

1. In each instance we will compare the characteristic polynomial of $A$ ( $C ( A )$ ) to that of $B$ . They must agree if the matrices are to be similar.

$$
\begin{array} { r l } & { p ( A ) = x ^ { 2 } - 4 x + 3 \neq x ^ { 2 } - 2 x - 3 = p ( B ) . } \\ & { p ( A ) = x ^ { 2 } - 5 x + 6 \neq x ^ { 2 } - 6 x + 6 = p ( B ) . } \\ & { p ( A ) = x ^ { 3 } - 4 x ^ { 2 } + 5 x - 2 \neq x ^ { 3 } - 4 x ^ { 2 } + 5 x - 6 = p ( B ) . } \\ & { p ( A ) = x ^ { 3 } - 5 x ^ { 2 } + 1 2 x - 1 1 \neq x ^ { 3 } - 4 x ^ { 2 } + 4 x + 1 1 = p ( B ) . } \end{array}
$$

2. For a pair of matrices to be similar the determinants and characteristic polynomials must be the same.

(a) $\operatorname* { d e t } ( A ) = 3 \neq 2 = \operatorname* { d e t } ( B )$

(b) $\operatorname* { d e t } ( A ) = - 4 = \operatorname* { d e t } ( B )$ , but $p ( A ) = \lambda ^ { 2 } + \lambda - 4 \neq \lambda ^ { 2 } - \lambda - 4 = p ( B )$ . (c) (d) $\begin{array} { l } { \operatorname* { d e t } ( A ) = 1 \neq - 8 = \operatorname* { d e t } ( B ) } \\ { \operatorname* { d e t } ( A ) = - 2 4 \neq 0 = \operatorname* { d e t } ( B ) } \end{array}$

3. In each case we have $A ^ { 3 } = ( P D P ^ { ( - 1 ) } ) ( P D P ^ { ( - 1 ) } ) ( P D P ^ { ( - 1 ) } ) = P D ^ { 3 } P ^ { ( - 1 ) } .$

$$
\begin{array} { r l } { ( 8 ) \left[ \begin{array} { c c } { \frac { 2 6 } { 6 } } & { - \frac { 1 4 } { 1 5 } } \\ { - \frac { 2 1 } { 5 } } & { \frac { 1 } { 5 } } \end{array} \right] } & { } \\ { ( 6 ) \left[ \begin{array} { c c } { 1 } & { 9 } \\ { 0 } & { - 8 } \end{array} \right] } & { } \\ { ( \mathrm { c } ) \left[ \begin{array} { c c } { \frac { 8 } { 9 } } & { - \frac { 8 } { 8 } } \\ { \frac { 4 } { 5 } } & { - \frac { 3 } { 5 } } & { \frac { 2 } { 5 } } \\ { - \frac { 2 } { 5 } } & { \frac { 4 } { 5 } } & { - \frac { 6 } { 5 } } \end{array} \right] } & { } \\ { ( \mathrm { d } ) \left[ \begin{array} { c c } { 8 } & { 0 } \\ { 0 } & { 8 } \end{array} \right] } & { } \\ { ( \mathrm { d } ) \left[ \begin{array} { c c } { 0 } & { 8 } \\ { 0 } & { 0 } \end{array} \right] } & { } \end{array}
$$

4. (a) The technique is described in part (b). The result is

$$
\left[ { \begin{array} { c c } { 1 0 } & { - 6 } \\ { - 9 } & { 7 } \end{array} } \right] .
$$

\*(b) It would be easy to simply use $A ^ { 3 }$ from Exercise 3(b) and multiply by $A$ . However, we don’t explicitly have $A$ . Alternatively,

$$
A ^ { 4 } = P D ^ { 4 } P ^ { - 1 } = \left[ \begin{array} { c c } { { - 1 } } & { { 2 } } \\ { { 1 } } & { { 0 } } \end{array} \right] \left[ \begin{array} { c c } { { 1 6 } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right] \left[ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { { \frac { 1 } { 2 } } } } & { { { \frac { 1 } { 2 } } } } \end{array} \right] = \left[ \begin{array} { c c } { { 1 } } & { { - 1 5 } } \\ { { 0 } } & { { 1 6 } } \end{array} \right] .
$$

(c) The technique is described in part (b). The result is

$$
A ^ { 4 } = \frac 1 5 \left[ \begin{array} { l l l } { 7 } & { - 4 } & { 1 } \\ { 4 } & { - 3 } & { 2 } \\ { 2 } & { - 4 } & { 6 } \end{array} \right] .
$$

(d) The technique is described in part (b). The result is

$$
A ^ { 4 } = \left[ { \begin{array} { c c c } { 1 6 } & { 0 } & { 0 } \\ { 0 } & { 1 6 } & { 0 } \\ { 0 } & { 0 } & { 1 6 } \end{array} } \right] .
$$

5. They are all diagonalizable with $P$ and $D$ as follows.

$$
{ \begin{array} { r } { P = { \left[ \begin{array} { l l } { - 1 } & { { \frac { 1 } { 4 } } } \\ { 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l } { 5 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] } } \\ { P = { \left[ \begin{array} { l l } { 1 } & { - 1 } \\ { 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 3 } \end{array} \right] } } \end{array} }
$$

$$
{ \begin{array} { r l } & { P = { \left[ \begin{array} { l l l } { 1 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 1 } & { 1 } & { 0 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l l } { 3 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } } \\ & { P = { \left[ \begin{array} { l l l } { { \sqrt { 2 } } } & { - { \sqrt { 2 } } } & { 0 } \\ { 1 } & { 1 } & { - 1 } \\ { 1 } & { 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l l } { 1 + { \sqrt { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 1 - { \sqrt { 2 } } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } } \end{array} }
$$

$$
P = \left[ \begin{array} { c c } { { - 1 } } & { { 1 } } \\ { { 1 } } & { { 1 } } \end{array} \right] \mathrm { ~ a n d ~ } D = \left[ \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { 3 } } \end{array} \right]
$$

$$
P = { \left[ \begin{array} { l l l } { 1 } & { - 1 } & { - 1 } \\ { 1 } & { 0 } & { 1 } \\ { 1 } & { 1 } & { 0 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l l } { 4 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

$$
P = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 1 } \\ { - 1 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l l } { 2 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 3 } \end{array} \right] }
$$

7. Only the matrices in parts (a) and (c) are positive definite.

$$
Q = \left[ { \begin{array} { r r } { - { \frac { \sqrt { 2 } } { 2 } } } & { { \frac { \sqrt { 2 } } { 2 } } } \\ { { \frac { \sqrt { 2 } } { 2 } } } & { { \frac { \sqrt { 2 } } { 2 } } } \end{array} } \right] { \mathrm { ~ a n d ~ } } D = \left[ { \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 3 } \end{array} } \right]
$$

$$
* ( { \bf c } ) ~ Q = \left[ \begin{array} { r r r } { { \frac { \sqrt { 2 } } { 2 } } } & { { 0 } } & { { \frac { \sqrt { 2 } } { 2 } } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { - \frac { \sqrt { 2 } } { 2 } } } & { { 0 } } & { { \frac { \sqrt { 2 } } { 2 } } } \end{array} \right] \mathrm { ~ a n d ~ } D = \left[ \begin{array} { r r r } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 2 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 3 } } \end{array} \right]
$$

8. The matrix will be positive definite if and only if the all the principle leading submatrices have a positive determinant. Let $A _ { n }$ denote the $n \times n$ principle leading submatrix of $A$ .

(a) $\operatorname* { d e t } ( A _ { 1 } ) = 4 \quad \operatorname* { d e t } ( A _ { 2 } ) = 1 2 , \quad \mathrm { a n d } \quad \operatorname* { d e t } ( A ) = 4 4$ , so $A$ is positive definite. A factorization $D = Q ^ { t } A Q$ has

$$
Q = \left[ \begin{array} { c c c } { 0 } & { \frac { \sqrt { 2 } } { 2 } } & { - \frac { \sqrt { 2 } } { 2 } } \\ { \frac { \sqrt { 5 } } { 4 } } & { \frac { \sqrt { 1 0 } } { 5 } } & { \frac { \sqrt { 1 0 } } { 5 } } \\ { - \frac { \sqrt { 5 } } { 2 } } & { \frac { \sqrt { 1 0 } } { 1 0 } } & { \frac { \sqrt { 1 0 } } { 1 0 } } \end{array} \right] \quad \mathrm { a n d } \quad D = \left[ \begin{array} { c c c } { 4 } & { 0 } & { 0 } \\ { 0 } & { 4 + \sqrt { 5 } } & { 0 } \\ { 0 } & { 0 } & { 4 - \sqrt { 5 } } \end{array} \right]
$$

(b) $\operatorname* { d e t } ( A ) = 0$ so $A$ is not positive definite.

(c) $\operatorname* { d e t } ( A ) = - 5$ so $A$ is not positive definite.

(d) $\operatorname * { l e t } ( A _ { 1 } ) = 8 \quad \operatorname * { d e t } ( A _ { 2 } ) = 4 8 , \quad \operatorname * { d e t } ( A _ { 3 } ) = 3 5 2 .$ , and $\operatorname* { d e t } ( A ) = 2 7 3 6$ , so $A$ is positive definite. A factorization $D = Q ^ { t } A Q$ has, approximately,

$$
\left[ { \begin{array} { r r r r } { - 0 . 6 0 0 5 } & { - 0 . 6 0 0 5 } & { - 0 . 4 4 9 6 } & { - 0 . 2 7 7 0 } \\ { - 0 . 7 0 7 1 } & { 0 . 7 0 7 1 } & { 0 } & { 0 } \\ { 0 . 2 8 4 4 } & { 0 . 2 8 4 4 } & { - 0 . 8 9 0 6 } & { 0 . 2 1 2 2 } \\ { - 0 . 2 4 1 9 } & { - 0 . 2 4 1 9 } & { 0 . 0 6 8 8 } & { 0 . 9 3 7 1 } \end{array} } \right] \quad { \mathrm { a n d } } \quad D = \left[ { \begin{array} { r r r r } { 1 3 . 9 5 8 7 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 4 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 6 . 4 8 4 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 7 . 5 5 7 2 } \end{array} } \right]
$$

9. In each case the matrix fails to have 3 linearly independent eigenvectors.

(a) $\operatorname* { d e t } ( A ) = 1 2$ , so $A$ is nonsingular.   
(b) $\operatorname* { d e t } ( A ) = - 1$ , so $A$ is nonsingular.   
\*(c) $\operatorname* { d e t } ( A ) = 1 2$ , so $A$ is nonsingular.   
(d) $\operatorname* { d e t } ( A ) = 1$ , so $A$ is nonsingular.

10. $^ *$ (a) The matrix is clearly singular because it has a row (and a column) all of whose entries are $0$ . However, the eigenvalues of $A$ , which are $\lambda _ { 1 } = 0$ , $\lambda _ { 2 } = 1$ , and $\lambda _ { 3 } = 3$ are distinct so the corresponding eigenvectors, $\mathbf { x } _ { 1 } = ( 0 , 0 , 1 ) ^ { t }$ , $\mathbf { x } _ { 1 } = ( 1 , 1 , 0 ) ^ { t }$ , and $\mathbf { x } _ { 3 } = ( 1 , - 1 , ) ^ { t }$ , can be used to form the columns of the matrix $P$ with $A = P D P ^ { - 1 }$ . The matrix $D$ is the diagonal matrix with diagonal entries in the order $0$ , $^ { 1 }$ , and 3.

(b) The eigenvalues of $A$ are $\lambda _ { 1 } ~ = ~ 0$ , $\lambda _ { 2 } ~ = ~ 3$ , and $\lambda _ { 3 } ~ = ~ 3$ , so $A$ is singular. However, there are three linearly independent eigenvectors of $A$ . The eigenvector $\mathbf { x } _ { 1 } = ( 1 , 1 , 1 ) ^ { t }$ , corresponding to $\lambda _ { 1 } = 0$ , and the eigenvectors $\mathbf { x } _ { 2 } ~ = ~ ( 1 , 0 , - 1 ) ^ { t }$ and $\mathbf { x } _ { 3 } ~ = ~ ( 1 , - 1 , 0 ) ^ { t }$ , corresponding to $\lambda _ { 2 } = \lambda _ { 3 } = 3$ . These eigenvectors can be used to form the columns of the matrix $P$ with $A = P D P ^ { - 1 }$ . The matrix $D$ is the diagonal matrix with diagonal entries in the order 0, 3, and 3.

11. (a) The eigenvalues and associated eigenvectors are $\lambda _ { 1 } = 5 . 3 0 7 8 5 7 5 6 3$ , (0.59020967, 0.51643129, 0.62044441)t; $\lambda _ { 2 } = - 0 . 4 2 1 3 1 1 2 9 9 3$ , $( 0 . 7 7 2 6 4 2 3 4 , - 0 . 1 3 8 7 6 2 7 8 , - 0 . 6 1 9 4 9 0 6 9 ) ^ { u }$ ; $\lambda _ { 3 } = - 0 . 1 3 6 5 4 6 2 6 4 7$ , $( 0 . 2 3 3 8 2 9 7 8 , - 0 . 8 4 5 0 1 1 0 2 , 0 . 4 8 0 9 1 5 8 1 ) ^ { \iota } .$ . (b) $A$ is not positive definite because $\lambda _ { 2 } < 0$ and $\lambda _ { 3 } < 0$ .

12. Since $B$ is nonsingular, $B ^ { - 1 }$ exists and

$$
A B = I \cdot ( A B ) = ( B ^ { - 1 } B ) ( A B ) = B ^ { - 1 } ( B A ) B .
$$

So $A B$ is similar to $B A$ .

13. Because $A$ is similar to $B$ and $B$ is similar to $C$ there exist invertible matrices $S$ and $T$ with $A = S ^ { - 1 } B S$ and $B = T ^ { - 1 } C T$ Hence $A$ is similar to $C$ because

$$
A = S ^ { - 1 } B S = S ^ { - 1 } ( T ^ { - 1 } C T ) S = ( S ^ { - 1 } T ^ { - 1 } ) C ( T S ) = ( T S ) ^ { - 1 } C ( T S ) .
$$

14. Suppose that $A = P B P ^ { - 1 }$ .

(a) We have

$$
{ \begin{array} { r l } & { \operatorname* { d e t } ( A ) = \operatorname* { d e t } ( P B P ^ { - 1 } ) = \operatorname* { d e t } ( P ) \operatorname* { d e t } ( B ) \operatorname* { d e t } ( P ^ { - 1 } ) } \\ & { \qquad = \operatorname* { d e t } ( P ) \operatorname* { d e t } ( P ^ { - 1 } ) \operatorname* { d e t } ( B ) = \operatorname* { d e t } ( P P ^ { - 1 } ) \operatorname* { d e t } ( B ) = \operatorname* { d e t } ( I ) \operatorname* { d e t } ( B ) = \operatorname* { d e t } ( B ) . } \end{array} }
$$

(b) We have

$$
\begin{array} { l } { p ( A ) = \operatorname* { d e t } ( A - \lambda I ) = \operatorname* { d e t } ( P B P ^ { - 1 } - \lambda P \cdot I \cdot P ^ { - 1 } ) } \\ { \quad = \operatorname* { d e t } ( P ) \operatorname* { d e t } ( B - \lambda I ) \operatorname* { d e t } ( P ^ { - 1 } ) = \operatorname* { d e t } ( B - \lambda I ) = p ( B ) . } \end{array}
$$

(c) The characteristic polynomials of $A$ and $B$ agree, so $A$ and $B$ have the same eigenvalues. The matrix $A$ is singular if and only if $0$ is an eigenvalue of $A$ , which is true if and only if $0$ is an eigenvalue of $B$ . So $A$ is nonsingular if and ony if $B$ is nonsingular.

(d) We have

$$
A ^ { - 1 } = ( P B P ^ { - 1 } ) ^ { - 1 } = ( P ^ { - 1 } ) ^ { - 1 } B ^ { - 1 } P ^ { - 1 } = P B ^ { - 1 } P ^ { - 1 } .
$$

So $A ^ { - 1 }$ is similar to $B ^ { - 1 }$ .

(e) We have

$$
A ^ { t } = ( P B P ^ { - 1 } ) ^ { t } = ( P ^ { - 1 } ) ^ { t } B ^ { t } P ^ { t } = ( P ^ { t } ) ^ { - 1 } B ^ { t } P ^ { t } .
$$

Since $P$ is invertible if and only if $P ^ { t }$ is invertible, $A ^ { t }$ is similar to $B ^ { t }$ .

15. The matrix $A$ has an eigenvalue of multiplicity $1$ at $\lambda _ { 1 } = 3$ with eigenvector $\mathbf { s } _ { 1 } = ( 0 , 1 , 1 ) ^ { t }$ , and an eigenvalue of multiplicity 2 at $\lambda _ { 2 } = 2$ with linearly independent eigenvectors ${ \bf s } _ { 2 } = ( 1 , 1 , 0 ) ^ { t }$ and $\mathbf { s } _ { 3 } = ( - 2 , 0 , 1 ) ^ { t }$ . Let

$$
S _ { 1 } = \{ \mathbf { s } _ { 1 } , \mathbf { s } _ { 2 } , \mathbf { s } _ { 3 } \} , \quad S _ { 2 } = \{ \mathbf { s } _ { 2 } , \mathbf { s } _ { 1 } , \mathbf { s } _ { 3 } \} , \quad \mathrm { a n d } \quad S _ { 3 } = \{ \mathbf { s } _ { 2 } , \mathbf { s } _ { 3 } , \mathbf { s } _ { 1 } \} .
$$

Then

$$
A = S _ { 1 } ^ { - 1 } D _ { 1 } S _ { 1 } = S _ { 2 } ^ { - 1 } D _ { 2 } S _ { 2 } = S _ { 3 } ^ { - 1 } D _ { 3 } S _ { 3 } ,
$$

so $A$ is similar to $D _ { 1 }$ , $D _ { 2 }$ , and $D _ { 3 }$ .

\*16. (i) Let the columns of $Q$ be denoted by the vectors ${ \bf q } _ { 1 } , { \bf q } _ { 2 } , \ldots , { \bf q } _ { n }$ , which are also the rows of $Q ^ { t }$ . Because $Q$ is orthogonal, $( { \bf q } _ { i } ) ^ { t } \cdot { \bf q } _ { j }$ is zero when $i \neq j$ and $^ { 1 }$ when $i = j$ . But the $_ { i j }$ - entry of $Q ^ { t } Q$ is $( { \bf q } _ { i } ) ^ { t } \cdot { \bf q } _ { j }$ for each $i$ and $j$ so $Q ^ { t } Q = I$ . Hence $Q ^ { t } = Q ^ { - 1 }$ .

(ii) From part (i) we have $Q ^ { t } Q = I$ , so

$$
( Q \mathbf { x } ) ^ { t } ( Q \mathbf { y } ) = ( \mathbf { x } ^ { t } Q ^ { t } ) ( Q \mathbf { y } ) = \mathbf { x } ^ { t } ( Q ^ { t } Q ) \mathbf { y } = \mathbf { x } ^ { t } ( I ) \mathbf { y } = \mathbf { x } ^ { t } \mathbf { y } .
$$

(iii) This follows from part (ii) with $\mathbf { x }$ replacing $\mathbf { y }$ , since then

$$
| | Q \mathbf { x } | | _ { 2 } ^ { 2 } = ( Q \mathbf { x } ) ^ { t } ( Q \mathbf { x } ) = \mathbf { x } ^ { t } \mathbf { x } = | | \mathbf { x } | | _ { 2 } ^ { 2 } .
$$

17. The matrix $A$ has an eigenvalue of multiplicity $^ { 1 }$ at $\lambda _ { 1 } = 3$ , and an eigenvalue of multiplicity 2 at $\lambda _ { 2 } = 2$ . However, $\lambda _ { 2 } = 2$ has only one linearly independent unit eigenvector, so by Theorem 9.13, $A$ is not similar to a diagonal matrix.

$^ { * } 1 8$ . Let the columns of $Q$ be denoted by the vectors ${ \bf q } _ { 1 } , { \bf q } _ { 2 } , \ldots , { \bf q } _ { n }$ , which are also the rows of $Q ^ { t } = Q ^ { - 1 }$ . Then $Q ^ { t } Q = I$ is equivalent to having $( { \bf q } _ { i } ) ^ { t } \cdot { \bf q } _ { j } = 0$ when $i \neq j$ and $( { \bf q } _ { i } ) ^ { t } \cdot { \bf q } _ { i } = 1$ , for each $i = 1 , 2 , \ldots , n$ and $j = 1 , 2 , \dots , n$ . But this is precisely what is required for the columns of $Q$ to form an orthonormal set. Hence $Q$ is an orthogonal matrix.

19. The proof of Theorem 9.13 follows by considering the form the diagonal matrix must assume. The matrix $A$ is similar to a diagonal matrix $D$ if and only if an invertible matrix $S$ exists with $D = S ^ { - 1 } A S$ , which is equivalent to $A S = S D$ , with $S$ invertible. Suppose that we have $A S = S D$ with the columns of $S$ denoted $\mathbf { s } _ { 1 } , \mathbf { s } _ { 2 } , \ldots , \mathbf { s } _ { n }$ and the diagonal elements of $D$ denoted $d _ { 1 } , d _ { 2 } , \ldots , d _ { n }$ . Then $A \mathbf { s } _ { i } = d _ { i } \mathbf { s } _ { i }$ for each $i = 1 , 2 , \ldots , n$ . Hence each $d _ { i }$ is an eigenvalue of $A$ with corresponding eigenvector ${ \bf s } _ { i }$ . The matrix $S$ is invertible, and consequently $A$ is similar to $D$ , if and only if there are $n$ linearly independent eigenvectors that can be placed in the columns of $S$ .

# Exercise Set 9.3, page 590

1. The approximate eigenvalues and approximate eigenvectors are:

\*(a) $\mu ^ { ( 3 ) } = 3 . 6 6 6 6 6 7$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 9 7 7 2 7 2 7 , 0 . 9 3 1 8 1 8 2 , 1 ) ^ { t }$ (b) $\mu ^ { ( 3 ) } = 2 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , 1 , 0 . 5 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 5 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 2 5 7 8 9 4 7 , 1 , - 0 . 2 8 4 2 1 0 5 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 5 . 0 3 8 4 6 2$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , 0 . 2 2 1 3 7 4 1 , 0 . 3 8 9 3 1 3 0 , 0 . 4 0 4 5 8 0 2 ) ^ { t }$

2. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 3 ) } = 6 . 0 5 0 8 4 7 5$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , 0 . 5 7 1 4 2 8 5 7 , 0 . 7 7 5 9 1 0 3 6 ) ^ { t }$ (b) $\mu ^ { ( 3 ) } = 5 . 5 2 6 3 1 5 8$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 1 7 1 1 7 1 1 7 , 0 . 4 5 9 4 5 9 4 6 , 1 , 0 . 9 4 5 9 4 6 0 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 7 . 5 3 1 0 7 3$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 6 8 8 6 7 2 2 , - 0 . 6 7 0 6 6 7 7 , - 0 . 9 2 1 9 8 0 5 , 1 ) ^ { i }$ t (d) $\mu ^ { ( 3 ) } = 4 . 1 0 6 0 6 1$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 1 2 5 4 6 1 3 , 0 . 0 8 4 8 7 0 8 5 , 0 . 0 0 9 2 2 5 0 9 , 1 ) ^ { t }$

3. The approximate eigenvalues and approximate eigenvectors are:

\*(a) $\mu ^ { ( 3 ) } = 1 . 0 2 7 7 3 0$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 1 8 8 9 0 8 2 , 1 , - 0 . 7 8 3 3 6 2 2 ) ^ { i }$ t (b) $\mu ^ { ( 3 ) } = - 0 . 4 1 6 6 6 6 7$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , - 0 . 7 5 , - 0 . 6 6 6 6 6 7 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 1 7 . 6 4 4 9 3$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 3 8 0 5 7 9 4 , - 0 . 0 9 0 7 9 1 3 2 , 1 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 1 . 3 7 8 6 8 4$ $\mathrm { 4 , ~ \ \mathbf { x } ^ { ( 3 ) } = ( - 0 . 3 6 9 0 2 7 7 , - 0 . 2 5 2 2 8 8 0 , 0 . 2 0 7 7 4 3 8 , 1 ) ^ { t } }$

4. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 3 ) } = 5 . 9 1 8 2 3 2 9$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , 0 . 5 5 2 6 3 3 6 4 , 0 . 8 1 2 9 6 5 6 1 ) ^ { t }$ (b) $\mu ^ { ( 3 ) } = 2 . 6 4 5 8 4 3 6$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 6 0 8 4 6 0 4 0 , 1 , - 0 . 3 2 6 7 7 4 8 8 8 , 0 . 0 3 7 3 8 3 1 8 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 3 . 9 9 6 0 7 3$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 9 9 9 1 4 2 9 , 0 . 9 9 3 2 0 1 4 , 1 , 0 . 9 9 3 9 8 2 5 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 4 . 1 0 5 2 9 3$ $^ { 1 9 3 , } \quad \mathbf { x } ^ { ( 3 ) } = ( 0 . 0 6 2 8 1 4 1 9 , 0 . 0 8 7 0 4 0 8 9 , 0 . 0 1 8 2 5 2 1 3 , 1 ) ^ { t }$

5. The approximate eigenvalues and approximate eigenvectors are:

\*(a) $\mu ^ { ( 3 ) } = 3 . 9 5 9 5 3 8$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 8 1 6 1 2 4 , 0 . 5 5 4 5 6 0 6 , 0 . 5 9 5 1 3 8 3 ) ^ { i }$ t (b) $\mu ^ { ( 3 ) } = 2 . 0 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 6 6 6 6 6 6 7 , - 0 . 6 6 6 6 6 6 7 , - 0 . 3 3 3 3 3 3 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 7 . 1 8 9 5 6 7$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 9 9 5 3 0 8 , 0 . 7 3 6 7 4 7 2 , 0 . 3 1 2 6 7 6 2 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 6 . 0 3 7 0 3 7$ $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 0 7 3 7 1 4 , 0 . 4 8 7 8 5 7 1 , - 0 . 6 6 3 4 8 5 7 , - 0 . 2 5 3 6 8 5 7 ) ^ { t }$

6. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 3 ) } = 3 . 8 4 8 4 1 6 3$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 2 9 8 4 1 3 1 9 , - 0 . 4 6 8 9 3 5 0 1 , 0 . 8 3 1 2 9 3 9 ) ^ { t }$ (b) $\mu ^ { ( 3 ) } = 4 . 6 9 0 5 6 6 0$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 9 5 5 5 7 2 6 6 , - 0 . 2 9 1 2 2 2 1 4 , 0 . 0 4 5 5 0 3 4 6 ) ^ { i }$ t (c) $\mu ^ { ( 3 ) } = 5 . 1 4 2 5 6 2$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 8 3 7 3 0 5 1 , 0 . 3 7 0 1 7 7 0 , 0 . 1 9 3 9 0 2 2 , 0 . 3 5 2 5 4 9 5 ) ^ { t }$ (d) ${ \bf \tau } ^ { ( 3 ) } = 8 . 5 9 3 1 4 2 , \quad { \bf x } ^ { ( 3 ) } = ( - 0 . 4 1 3 4 7 6 2 , 0 . 4 0 2 6 6 6 4 , 0 . 5 5 3 5 5 3 6 , - 0 . 6 0 0 3 9 6 2 ) ^ { t }$

7. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 9 ) } = 3 . 9 9 9 9 0 8 , \quad \mathbf { x } ^ { ( 9 ) } = ( 0 . 9 9 9 9 9 4 3 , 0 . 9 9 9 9 8 2 8 , 1 ) ^ { t }$ (b) $\mu ^ { ( 1 3 ) } = 2 . 4 1 4 2 1 4$ , $\mathbf { x } ^ { ( 1 3 ) } = ( 1 , 0 . 7 0 7 1 4 2 9 , 0 . 7 0 7 0 7 0 7 ) ^ { t }$ (c) $\mu ^ { ( 9 ) } = 5 . 1 2 4 7 4 9$ , $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 2 4 2 4 4 7 6 , 1 , - 0 . 3 1 9 9 7 3 3 ) ^ { t }$ (d) $\mu ^ { ( 2 4 ) } = 5 . 2 3 5 8 6 1$ , $\mathbf { x } ^ { ( 2 4 ) } = ( 1 , 0 . 6 1 7 8 3 6 1 , 0 . 1 1 8 1 6 6 7 , 0 . 4 9 9 9 2 2 0 ) ^ { t }$

8. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 1 2 ) } = 5 . 9 1 9 3 4 7 6$ , $\mathbf { x } ^ { ( 1 2 ) } = ( 1 , 0 . 5 5 4 7 8 8 4 5 , 0 . 8 0 9 9 5 8 1 6 ) ^ { t }$ (b) $\mu ^ { ( 1 4 ) } = 5 . 6 6 5 8 9 7 2$ , $\mathbf { x } ^ { ( 1 4 ) } = ( 0 . 0 5 5 2 0 4 4 4 , 0 . 2 5 7 4 9 7 2 8 , 1 , 0 . 8 8 8 6 1 7 2 6$ )t (c) $\mathbf { \boldsymbol { \tau } } ^ { \prime } ) = 8 . 9 9 9 6 6 7 , \quad \mathbf { \boldsymbol { x } } ^ { ( 1 7 ) } = ( 0 . 9 9 9 9 0 8 5 , - 0 . 9 9 9 9 0 7 8 , - 0 . 9 9 9 9 9 9 3 , 1 ) ^ { t }$ (d) The method did not converge in 25 iterations. However, $\lambda _ { 1 } \approx \mu ^ { ( 3 6 3 ) } = 4 . 1 0 5 3 0 9$ , $\mathrm { t h e n } \mathbf { x } ^ { ( 3 6 3 ) } = ( 0 . 0 6 2 8 6 2 9 9 , 0 . 0 8 7 0 2 7 5 4 , 0 . 0 1 8 2 4 6 8 0 , 1 ) ^ { t }$ and $\lambda _ { 2 } \approx \mu ^ { ( 1 5 ) } = - 4 . 0 2 4 3 0 8$

9. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 9 ) } = 1 . 0 0 0 0 1 5 2 3$ with $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 1 9 9 9 9 3 9 1 , 1 , - 0 . 7 9 9 9 9 0 8 7 ) ^ { t }$   
(b) $\mu ^ { ( 1 2 ) } = - 0 . 4 1 4 2 1 3 5 6$ with $\mathbf { x } ^ { ( 1 2 ) } = ( 1 , - 0 . 7 0 7 0 9 1 8 4 , - 0 . 7 0 7 1 2 1 7 2 0 ^ { t }$   
(c) The method did not converge in 25 iterations. However, convergence occurred with $\mu ^ { ( 4 2 ) } = 1 . 6 3 6 6 3 6 4 2$ with $\mathbf { x } ^ { ( 4 2 ) } = ( - 0 . 5 7 0 6 8 1 5 1 , 0 . 3 6 3 3 6 5 8 , 1 ) ^ { t }$   
(d) $\mu ^ { ( 9 ) } = 1 . 3 8 1 9 5 9 2 9$ with $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 3 8 1 9 4 0 0 3 , - 0 . 2 3 6 1 0 0 6 8 , 0 . 2 3 6 0 1 9 0 9 , 1 ) ^ { t }$

10. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 7 ) } = 5 . 9 1 9 6 6 8 8$ , $\mathbf { x } ^ { ( 7 ) } = ( 1 , 0 . 5 5 4 8 4 7 7 6 , 0 . 8 0 9 9 7 3 3 0 ) ^ { t }$ (b) $\mu ^ { ( 6 ) } = 2 . 6 4 5 9 3 1 2$ , $\mathbf { x } ^ { ( 6 ) } = ( 0 . 6 0 7 5 6 1 9 1 , 1 , - 0 . 3 2 5 0 6 9 3 0 , 0 . 0 3 8 3 6 9 2 6 ) ^ { t }$ (c) $\mu ^ { ( 6 ) } = 3 . 9 9 9 9 9 7$ , $\mathbf { x } ^ { ( 6 ) } = ( 0 . 9 9 9 9 9 3 9 , 0 . 9 9 9 9 9 9 9 , 0 . 9 9 9 9 9 4 0 , 1 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 4 . 1 0 5 2 9 3$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 0 6 2 8 1 4 1 9 , 0 . 0 8 7 0 4 0 8 9 , 0 . 0 1 8 2 5 2 1 3 , 1 ) ^ { t }$

11. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 8 ) } = 4 . 0 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 8 ) } = ( 0 . 5 7 7 3 5 4 7 , 0 . 5 7 7 3 2 8 2 , 0 . 5 7 7 3 6 7 9 ) ^ { t }$ (b) $\mu ^ { ( 1 3 ) } = 2 . 4 1 4 2 1 4$ , $\mathbf { x } ^ { ( 1 3 ) } = ( - 0 . 7 0 7 1 0 6 8 , - 0 . 5 0 0 0 2 5 5 , - 0 . 4 9 9 9 7 4 5 ) ^ { t }$ (c) $\mu ^ { ( 1 6 ) } = 7 . 2 2 3 6 6 3$ , $\mathbf { x } ^ { ( 1 6 ) } = ( 0 . 6 2 4 7 8 4 5 , 0 . 7 2 0 4 2 7 1 , 0 . 3 0 1 0 4 6 6 ) ^ { t }$ (d) $\mu ^ { ( 2 0 ) } = 7 . 0 8 6 1 3 0$ $8 6 1 3 0 , \quad \mathbf { x } ^ { ( 2 0 ) } = ( 0 . 3 3 2 5 9 9 9 , 0 . 2 6 7 1 8 6 2 , - 0 . 7 5 9 0 1 0 8 , - 0 . 4 9 1 8 2 4 6 ) ^ { t }$

12. The approximate eigenvalues and approximate eigenvectors are:

(a) The method did not converge in 25 iterations. Dominant eigenvalues are $\sqrt { 1 5 }$ and $- { \sqrt { 1 5 } }$ . (b) $\mu ^ { ( 1 6 ) } = 4 . 8 3 4 7 7 8 0$ , $\mathbf { x } ^ { ( 1 6 ) } = ( - 0 . 9 2 9 0 4 8 7 0 , - 0 . 3 6 7 7 8 3 6 1 , 0 . 0 4 0 0 4 6 6 2 ) ^ { t }$ (c) $\mu ^ { ( 2 1 ) } = 5 . 2 3 6 0 6 8$ , $\mathbf { x } ^ { ( 2 1 ) } = ( 0 . 7 7 9 5 5 3 9 , 0 . 4 8 1 5 9 9 6 , 0 . 0 9 2 1 4 2 1 4 , 0 . 3 8 9 7 0 1 6 )$ )t (d) $\mu ^ { ( 1 6 ) } = 9 . 0 0 0 0 0 0 0 , \quad \mathbf { x } ^ { ( 1 6 ) } = ( - 0 . 4 9 9 9 5 9 2 , 0 . 4 9 9 9 5 8 4 , 0 . 5 0 0 0 4 0 8 , - 0 . 5 0 0 0 4 1 6 ) ^ { \mathrm { t } }$

13. The approximate eigenvalues and approximate eigenvectors are:

(a) $\lambda _ { 2 } { \approx } \mu ^ { ( 1 ) } = 1 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 1 ) } = ( - 2 . 9 9 9 9 0 8 , 2 . 9 9 9 9 0 8 , 0 ) ^ { t }$ (b) $\lambda _ { 2 } { \approx } \mu ^ { ( 1 ) } = 1 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 1 ) } = ( 0 , - 1 . 4 1 4 2 1 4 , 1 . 4 1 4 2 1 4 ) ^ { t }$ (c) $\lambda _ { 2 } { \approx } \mu ^ { ( 6 ) } = 1 . 6 3 6 7 3 4$ , $\mathbf { x } ^ { ( 6 ) } = ( 1 . 7 8 3 2 1 8 , - 1 . 1 3 5 3 5 0 , - 3 . 1 2 4 7 3 3 ) ^ { t }$ t

$$
\lambda _ { 2 } \approx \mu ^ { ( 1 0 ) } = 3 . 6 1 8 1 7 7 , \quad \mathbf { x } ^ { ( 1 0 ) } = ( 0 . 7 2 3 6 3 9 0 , - 1 . 1 7 0 5 7 3 , 1 . 1 7 0 6 7 5 , - 0 . 2 7 6 3 3 7 4 ) ^ { t }
$$

14. The approximate eigenvalues and approximate eigenvectors are:

(a) The method did not converge in 25 iterations. The remaining eigenvalues are complex numbers.   
(b) $\mu ^ { ( 9 ) } = 2 . 6 4 5 9 0 9 5 , \quad \mathbf { x } ^ { ( 9 ) } = ( - 1 . 6 9 3 0 9 5 3 , - 2 . 7 8 6 7 3 8 3 , 0 . 9 0 5 8 2 5 3 3 , - 0 . 1 0 6 9 2 8 4 2 ) ^ { t }$   
(c) $\lambda _ { 2 } \approx \mu ^ { ( 2 1 ) } = 5 . 0 0 0 0 5 1 , \quad \mathbf { x } ^ { ( 2 1 ) } = ( 1 . 9 9 9 3 3 8 , - 1 . 9 9 9 6 0 3 , 1 . 9 9 9 6 0 3 , - 2 . 0 0 0 1 9 8 ) ^ { t }$   
(d) $\mathbf { x } ^ { ( 1 5 ) } = ( - 8 . 1 5 1 9 6 5 , 2 . 1 0 0 6 9 9 , 0 . 7 5 1 9 0 8 0 , - 0 . 3 5 5 4 9 4 1 ) ^ { t }$ .

15. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 8 ) } = 4 . 0 0 0 0 0 1 , \quad \mathbf { x } ^ { ( 8 ) } = ( 0 . 9 9 9 9 7 7 3 , 0 . 9 9 9 9 3 1 3 4 , 1 ) ^ { t }$ (b) The method fails because of division by zero. (c) $\mu ^ { ( 7 ) } = 5 . 1 2 4 8 9 0$ , $\mathbf { x } ^ { ( 7 ) } = ( - 0 . 2 4 2 5 9 3 8 , 1 , - 0 . 3 1 9 6 3 5 1 ) ^ { t }$ (d) $\mu ^ { ( 1 5 ) } = 5 . 2 3 6 1 1 2 , \quad \mathbf { x } ^ { ( 1 5 ) } = ( 1 , 0 . 6 1 2 5 3 6 9 , 0 . 1 2 1 7 2 1 6 , 0 . 4 9 7 8 3 1 8 ) ^ { t }$

16. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 9 ) } = 5 . 9 1 9 7 1 4 1 0$ , $\mathbf { x } ^ { ( 9 ) } = ( 1 , 0 . 5 5 4 7 8 8 4 5 , 0 . 8 0 9 9 5 8 1 6 ) ^ { t }$ (b) $\mathbf { \xi } = 5 . 6 6 5 8 1 2 1 1 , \quad \mathbf { x } ^ { ( 1 1 ) } = ( 0 . 0 5 5 2 0 4 4 , 0 . 2 5 7 4 9 9 2 8 , 1 , 0 . 8 8 8 6 1 7 2 8 )$ t (c) $\mu ^ { ( 1 0 ) } = 8 . 9 9 9 8 9 0$ , $\mathbf { x } ^ { ( 1 0 ) } = ( 0 . 9 9 4 4 1 3 7 , - 0 . 9 9 4 2 1 4 8 , - 0 . 9 9 9 7 9 9 1 , 1$ )t (d) $\mu ^ { ( 1 1 ) } = 4 . 1 0 5 3 1 7 , \quad \mathbf { x } ^ { ( 1 1 ) } = ( 0 . 1 1 7 1 6 5 4 0 , 0 . 0 7 2 8 5 3 9 9 5 , 0 . 0 1 3 1 6 6 5 5 , 1 ) ^ { t }$

17. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 2 ) } = 1 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 5 4 2 3 7 3 , - 0 . 7 7 1 5 8 2 8 , 0 . 6 1 7 1 4 7 4 ) ^ { t }$ (b) $\mu ^ { ( 1 3 ) } = 1 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 1 3 ) } = ( 0 . 0 0 0 0 7 4 3 2 , - 0 . 7 0 7 0 7 2 3 , 0 . 7 0 7 1 4 1 3 ) ^ { t }$ (c) $\mu ^ { ( 1 4 ) } = 4 . 9 6 1 6 9 9$ , $\mathbf { x } ^ { ( 1 4 ) } = ( - 0 . 4 8 1 4 4 7 2 , 0 . 0 5 1 8 0 4 7 3 , 0 . 8 7 4 9 4 2 8 ) ^ { t }$ (d) $\mu ^ { ( 1 7 ) } = 4 . 4 2 8 0 0 7 $ , $\mathbf { x } ^ { ( 1 7 ) } = ( 0 . 7 1 9 4 2 3 0 , 0 . 4 2 3 1 9 0 8 , 0 . 1 1 5 3 5 8 9 , 0 . 5 3 8 5 4 6 6 ) ^ { t }$

18. The Power method was applied to the matrices in Exercise 1 using $\mathbf { x } ^ { ( 0 ) }$ as given with $T O L =$ $1 0 ^ { - 4 }$ . The following table summarizes the results. (Note: The results are very sensitive to roundoff error.)

<table><tr><td></td><td>入1</td><td>Number of iterations</td><td>入2</td><td>Eigenvector</td></tr><tr><td>(1a)</td><td>3.999908</td><td>2</td><td>1.000037</td><td>(-0.1999411,1, -0.799911)t</td></tr><tr><td>(16)</td><td>2.414213562</td><td>15</td><td>1.000003</td><td>(0.00004881, -0.9999485,1)t</td></tr><tr><td>(1c)</td><td>5.12488541</td><td>5</td><td>1.636636</td><td>(-0.5706569,0.3633325,1)t</td></tr><tr><td>(1d</td><td>5.23606796</td><td>13</td><td>3.617997</td><td>(-0.6180177,1, -0.9999990,0.2360394)t</td></tr></table>

19. (a) We have $| \lambda | \le 6$ for all eigenvalues $\lambda$ . (b) The approximate eigenvalue is $\mu ^ { ( 1 3 3 ) } = 0 . 6 9 7 6 6 8 5 4$ , with the approximate eigenvector $\mathbf { x } ^ { ( 1 3 3 ) } = ( 1 , 0 . 7 1 6 6 7 2 7 , 0 . 2 5 6 8 0 9 9 , 0 . 0 4 6 0 1 2 1 7 ) ^ { i }$ . (c) The characteristic polynomial is

$$
P ( \lambda ) = \lambda ^ { 4 } - \frac { 1 } { 4 } \lambda - \frac { 1 } { 1 6 } ,
$$

and the eigenvalues are

λ1 = 0.6976684972, λ2 = 0.2301775942+0.56965884i, $\begin{array} { r } { , \quad \lambda _ { 3 } = - 0 . 2 3 0 1 7 7 5 9 4 2 - 0 . 5 6 9 6 5 8 8 4 i } \end{array}$ ,

and

$$
\lambda _ { 4 } = - 0 . 2 3 7 3 1 3 3 0 8 .
$$

(d) The beetle population should approach zero since $A$ is convergent.

$^ *$ 20. Since

$$
\mathbf { x } ^ { t } = \frac { 1 } { \lambda _ { 1 } v _ { i } ^ { ( 1 ) } } ( a _ { i 1 } , a _ { i 2 } , \ldots , a _ { i n } ) ,
$$

the $i$ th row of $B$ is

$$
\left( a _ { i 1 } , a _ { i 2 } , \dots , a _ { i n } \right) - \frac { \lambda _ { 1 } } { \lambda _ { 1 } v _ { i } ^ { ( 1 ) } } \left( v _ { i } ^ { ( 1 ) } a _ { i 1 } , v _ { i } ^ { ( 1 ) } a _ { i 2 } , \dots , v _ { i } ^ { ( 1 ) } a _ { i n } \right) = \mathbf { 0 } .
$$

21. Using the Inverse Power method with $\mathbf { x } ^ { ( 0 ) } = ( 1 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 1 ) ^ { t }$ and $q = 0$ gives the following results:

(a) $\mu ^ { ( 4 9 ) } = 1 . 0 2 0 1 9 2 6$ , so $\rho ( A ^ { - 1 } ) \approx 1 / \mu ^ { ( 4 9 ) } = 0 . 9 8 0 2 0 7 1$ (b) $\mu ^ { ( 3 0 ) } = 1 . 0 4 0 4 5 6 8$ , so $\rho ( A ^ { - 1 } ) \approx 1 / \mu ^ { ( 3 0 ) } = 0 . 9 6 1 1 1 6 3$ (c) $\mu ^ { ( 2 2 ) } = 1 . 0 6 0 6 9 7 4$ , so $\rho ( A ^ { - 1 } ) \approx 1 / \mu ^ { ( 2 2 ) } = 0 . 9 4 2 7 7 6 0$ The method appears to be stable for all $\alpha$ in $[ \frac { 1 } { 4 } , \frac { 3 } { 4 } ]$ .

22. (a) $\rho \left( A ^ { - 1 } \right) = 0 . 9 8 0 1 4 8 5$ (b) $\rho \left( A ^ { - 1 } \right) = 0 . 9 6 1 0 6 9 9$ (c) $\rho \left( A ^ { - 1 } \right) = 0 . 9 4 2 7 1 9 8$ The method appears to be stable for $\alpha > 0$ .

23. Forming $A ^ { - 1 } B$ and using the Power method with $\mathbf { x } ^ { ( 0 ) } = ( 1 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 1 ) ^ { t }$ gives the following results:

(a) The spectral radius is approximately $\mu ^ { ( 4 6 ) } = 0 . 9 8 0 0 0 2 1$ .   
(b) The spectral radius is approximately $\mu ^ { ( 2 5 ) } = 0 . 9 6 0 3 5 4 3$ .   
(c) The spectral radius is approximately $\mu ^ { ( 1 8 ) } = 0 . 9 4 1 0 7 5 4$ .

24. (a) $\lambda _ { 1 } = - 6$ , $\lambda _ { 2 } = - 5$ , $\lambda _ { 3 } = - 2$ , the system is stable. (b) $\lambda _ { 1 } = - 2$ , $\lambda _ { 2 } = - 1 . 1 0 6 7 7 1 1$ , $\lambda _ { 3 } = - 3 . 9 4 6 6 4 + 0 . 8 2 9 7 0 i$ , $\lambda _ { 4 } = - 3 . 9 4 6 6 4 - 0 . 8 2 9 7 0 i$ , the system is stable.

# Exercise Set 9.4, page 600

1. Householder’s method produces the following tridiagonal matrices.

12.00000 10.77033 0.0   
\*(a) 10.77033 3.862069 5.344828 0.0 5.344828 7.137931 2.0000000 1.414214 0.0   
(b) 1.414214 1.000000 0.0 0.0 0.0 3.0 1.0000000 1.414214 0.0   
(c) 1.414214 1.000000 0.0 0.0 0.0 1.000000 4.750000 2.263846 0.0   
(d) 2.263846 4.475610 1.219512 0.0 1.219512 5.024390

2. Householder’s method produces the following tridiagonal matrices.

3. Householder’s method produces the following tridiagonal matrices.

2.0000000 2.8284271 1.4142136 (a) 2.8284271 1.0000000 2.0000000 0.0000000 2.0000000 3.0000000

−1.0000000 3.0655513 0.0000000   
(b) 3.6055513 0.23076923 3.1538462 0.0000000 0.15384615 2.2307692 5.0000000 4.9497475 1.4320780 1.5649769 1.4142136 2.0000000 2.4855515 1.8226448   
(c) 0.0000000 5.4313902 1.4237288 2.6486542 0.0000000 0.0000000 1.5939865 5.4237288 4.0000000 1.7320508 0.0000000 0.0000000 1.7320508 2.3333333 0.23570226 0.40824829   
(d) 0.0000000 0.47140452 4.6666667 0.57735027 0.0000000 0.0000000 0.0000000 5.0000000

# Exercise Set 9.5, page 611

1. Two iterations of the QR Algorithm without shifting produce the following matrices.

3.142857 0.559397 0.0   
(a) A(3) 0.559397 2.248447 0.187848 0.0 0.187848 0.608696 4.549020 1.206958 0.0   
(b) A(3) 1.206958 3.519688 0.000725 0.0 0.000725 −0.068708 4.592920 0.472934 0.0   
(c) A(3) 0.472934 3.108760 0.232083 0.0 0.232083 1.298319 3.071429 0.855352 0.0 0.0   
(d) A(3) = 0.855352 3.314192 1.161046 0.0 0.0 1.1610446 3.331770 0.268898 0.0 0.0 0.268898 0.282609  3.607843 0.612882 0.0 0.0   
(e) A(3) 0.612882 1.395227 1.111027 0.0 0.0 1.111027 3.133919 0.346353 0.0 0.0 0.346353 0.869151 1.013260 0.279065 0.0 0.0   
(f) A(3) 0.279065 0.696255 0.107448 0.0 0.0 0.107448 0.843061 0.310832 0.0 0.0 0.310832 0.317424

2. Two iterations of the QR Algorithm without shifting produce the following matrices.

$$
{ \begin{array} { r l } { A ^ { ( 3 ) } = { \Biggl [ \begin{array} { l l l } { 2 . 6 3 3 3 3 3 3 3 } & { - 1 . 1 6 8 5 6 9 8 8 } & { 0 } \\ { - 1 . 1 6 8 5 6 9 8 8 } & { 0 . 9 3 7 8 6 2 7 6 } & { - 2 . 5 7 5 9 4 4 9 8 { \Biggr ] } } \\ { 0 } & { - 2 . 5 7 5 9 4 4 9 8 } & { 0 . 4 2 8 8 0 3 9 1 } \end{array} } } \\ { A ^ { ( 3 ) } = { \Biggl [ \begin{array} { l l l } { 4 . 6 0 1 3 0 7 1 9 } & { 1 . 3 8 5 4 5 1 3 4 } & { 0 } \\ { 1 . 3 8 5 4 5 1 3 4 } & { 4 . 1 6 5 3 2 3 1 3 } & { 0 . 2 4 2 8 0 0 1 1 } \\ { 0 } & { 0 . 2 4 2 8 0 0 1 1 } & { 1 . 2 3 3 3 6 9 6 8 { \Biggr ] } } \end{array} } } \end{array} }
$$

<table><tr><td rowspan="7">A(3）</td><td>6.28571429</td><td>1.16057692</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1.16057692</td><td>5.26984127</td><td>1.49897084</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1.49897084</td><td>4.80808081</td><td>1.50776756</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1.50776756</td><td>3.07260525</td><td>0.23213209</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0.23213209</td><td>0.56375839</td></tr><tr><td>5.58655992</td><td>-0.60565234</td><td>0</td><td>0</td><td>0</td></tr><tr><td>-0.60565234</td><td>3.92585374</td><td>0.02385124</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0.02385124</td><td>3.03035281</td><td>-1.22483017</td><td>0</td></tr><tr><td>0</td><td>0</td><td>-1.22483017</td><td>2.29033145</td><td>0.73675527</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0.73675527</td><td>1.66690207</td></tr></table>

3. The matrices in Exercise 1 have the following eigenvalues, accurate to within $1 0 ^ { - 5 }$ .

\*(a) 3.414214, 2.000000, 0.58578644  
(b) −0.06870782, 5.346462, 2.722246  
(c) 1.267949, 4.732051, 3.000000  
(d) 4.745281, 3.177283, 1.822717, 0.2547188  
(e) 3.438803, 0.8275517, −1.488068, −3.778287  
(f) 0.9948440, 1.189091, 0.5238224, 0.1922421

4. The matrices have the following eigenvalues, accurate to within $1 0 ^ { - 5 }$ .

(a) 3.9115033, 2.1294613, −2.0409646 (b) 1.2087122, 5.7912878, 3.0000000 (c) $\mathrm { 5 . 0 0 0 0 0 0 0 0 , 2 . 0 0 0 0 0 0 0 0 , 4 . 0 0 0 0 0 0 0 0 , 7 . 4 6 4 1 0 1 6 , 0 . 5 3 5 8 9 8 4 }$ (d) 4.0274350, 2.0707128, 3.7275564, 5.7839956, 0.8903002

5. The matrices in Exercise 1 have the following eigenvectors, accurate to within $1 0 ^ { - 5 }$ .

(a) $( - 0 . 7 0 7 1 0 6 7 , 1 , - 0 . 7 0 7 1 0 6 7 ) ^ { t }$ , $( 1 , 0 , - 1 ) ^ { t }$ , $( 0 . 7 0 7 1 0 6 8 , 1 , 0 . 7 0 7 1 0 6 8 ) ^ { t }$   
(b) $( 0 . 1 7 4 1 2 9 9 , - 0 . 5 3 4 3 5 3 9 , 1 ) ^ { t }$ , $( 0 . 4 2 6 1 7 3 5 , 1 , 0 . 4 6 0 1 4 4 3 ) ^ { t }$ , $( 1 , - 0 . 2 7 7 7 5 4 4 , - 0 . 3 2 2 5 4 9 1 ) ^ { \iota }$   
(c) $( 0 . 2 6 7 9 4 9 2 , 0 . 7 3 2 0 5 0 8 , 1 ) ^ { t }$ , $( 1 , - 0 . 7 3 2 0 5 0 8 , 0 . 2 6 7 9 4 9 2 ) ^ { t }$ , $( 1 , 1 , - 1 ) ^ { t }$   
(d) $( - 0 . 0 8 0 2 9 4 4 7 , - 0 . 3 0 0 7 2 5 4 , 0 . 7 4 5 2 8 1 2 , 1 ) ^ { u }$ , $( 0 . 4 5 9 2 8 8 0 , 1 , - 0 . 7 1 7 9 9 4 9 , 0 . 8 7 2 7 1 1 8 ) ^ { \iota }$ , ( $0 . 8 7 2 7 1 1 8 , 0 . 7 1 7 9 9 4 9 , 1 , - 0 . 4 5 9 2 8 8 0 ) ^ { t } \ ($ $( 1 , - 0 . 7 4 5 2 8 1 2 , - 0 . 3 0 0 7 2 5 4 , 0 . 0 8 0 2 9 4 4 7 ) ^ { v }$   
(e) $( - 0 . 0 1 2 8 9 8 6 1 , - 0 . 0 7 0 1 5 2 9 9 , 0 . 4 3 8 8 0 2 6 , 1 ) ^ { \tau }$ , $( - 0 . 1 0 1 8 0 6 0 , - 0 . 2 8 7 8 6 1 8 , 1 , - 0 . 4 6 0 3 1 0 2 ) ^ { u }$ , $( 1 , 0 . 5 1 1 9 3 2 2 , 0 . 2 2 5 9 9 3 2 , - 0 . 0 5 0 3 5 4 2 3 ) ^ { v }$ $( - 0 . 5 6 2 3 3 9 1 , 1 , 0 . 2 1 5 9 4 7 4 , - 0 . 0 3 1 8 5 8 7 1 ) ^ { \tau }$   
(f) $( - 0 . 1 5 2 0 1 5 0 , - 0 . 3 0 0 8 9 5 0 , - 0 . 0 5 1 5 5 9 5 6 , 1 ) ^ { u }$ , $( 0 . 3 6 2 7 9 6 6 , 1 , 0 . 7 4 5 9 8 0 7 , 0 . 3 9 4 5 0 8 1 ) ^ { u }$ , $( 1 , 0 . 0 9 5 2 8 9 6 2 , - 0 . 6 9 0 7 9 2 1 , 0 . 1 4 5 0 7 0 3 ) ^ { t } , ( 0 . 8 0 2 9 4 0 3 , - 0 . 9 8 8 4 4 4 8 , 1 , - 0 . 1 2 3 7 9 9 5 ) ^ { t }$

6. (a) The inverse power method using $\mathbf { x } ^ { ( 0 ) } \ = \ ( 1 , 1 , 1 ) ^ { t }$ gives the following eigenvalues and eigenvectors.

$\lambda _ { 1 } = 3 . 9 1 1 5 0 3 3 1$ , $\mathbf { x } ^ { ( 9 ) } = ( 0 . 3 4 1 3 2 5 4 6 , - 0 . 5 1 8 1 9 8 9 1 , 1 ) ^ { t }$ $\lambda _ { 2 } = 2 . 1 2 9 4 6 1 2 8$ , $\mathbf { x } ^ { ( 5 ) } = ( 1 , - 0 . 1 7 8 1 9 4 1 4 , - 0 . 2 1 6 8 3 2 1 9 ) ^ { t }$ $\lambda _ { 3 } = - 2 . 0 4 0 9 6 4 5 9$ , $\mathbf { x } ^ { ( 6 ) } = ( 0 . 2 7 0 5 3 4 1 1 , 1 , 0 . 2 1 2 9 2 9 4 0 ) ^ { t }$ (b) The inverse power method using $\mathbf { x } ^ { ( 0 ) } \ = \ ( 1 , 1 , 1 ) ^ { t }$ gives the following eigenvalues and eigenvectors.

(c) The inverse power method using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives the following eigenvalues and eigenvectors.

(d) The inverse power method using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives the following eigenvalues and eigenvectors.

$\lambda _ { 1 } = 4 . 0 2 7 4 3 4 9 6$ , $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 5 0 0 9 0 0 8 , - 0 . 4 8 7 1 5 8 6 , - 0 . 1 3 5 3 4 3 3 4 , 1 , 0 . 9 7 3 2 9 7 6 2 ) ^ { t }$ $\lambda _ { 2 } = 2 . 0 7 0 7 1 2 8$ , $\mathfrak { c } ^ { ( z ) } = ( - 0 . 0 1 1 1 5 3 0 0 , - 0 . 0 3 2 6 7 0 3 5 , 0 . 3 4 1 0 6 3 2 7 , - 0 . 9 2 9 2 8 7 2 0 , 1 )$ )t $\lambda _ { 3 } = 3 . 7 2 7 5 5 6 4 2$ , $\mathbf { x } ^ { ( 2 ) } = ( 0 . 7 8 5 8 8 9 4 6 , 1 , 0 . 0 6 7 2 2 9 4 4 , 0 . 0 4 1 5 6 9 7 5 , 0 . 0 5 7 1 3 6 1 1 ) ^ { t }$ $\lambda _ { 4 } = 5 . 7 8 3 9 9 5 5 7$ , x $\mathbf { \dot { \hat { \rho } } ^ { ( 2 ) } } = ( 1 , - 0 . 7 8 3 9 9 5 5 7 , - 0 . 0 3 3 2 3 4 1 6 , 0 . 0 0 5 4 8 2 3$ 8, 0.00196925)t $\lambda _ { 5 } = 0 . 8 9 0 3 0 0 2 5$ , $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 0 1 4 4 5 6 3 2 , - 0 . 0 5 9 4 1 1 1 2 , 1 , 0 . 2 4 4 5 4 5$ 382, 0.11591404)t \*7. (a) First note that for any vector $\mathbf { x } = ( x _ { 1 } , x _ { 2 } ) ^ { t }$ we have

and that

$$
\begin{array} { r l } & { v _ { 1 } \cos \theta - x _ { 2 } \sin \theta ) ^ { 2 } + ( x _ { 1 } \sin \theta + x _ { 2 } \cos \theta ) ^ { 2 } = x _ { 1 } ^ { 2 } ( ( \cos \theta ) ^ { 2 } + ( \sin \theta ) ^ { 2 } ) + x _ { 2 } ^ { 2 } ( ( - \sin \theta ) ^ { 2 } + ( \cos \theta ) ^ { 2 } ) } \\ & { \qquad = x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } . } \end{array}
$$

So the $l _ { 2 }$ norms are the same.

Now let ${ \bf z } = ( z _ { 1 } , z _ { 2 } ) ^ { t }$ represent the vector that has the same magnitude as $\mathbf { x }$ but has been rotated by the angle $\theta$ . Let $\phi$ be the angle from the $x$ -axis to the point $( x _ { 1 } , x _ { 2 } )$ and let $r = \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } = | | \mathbf { x } | | _ { 2 }$ . Then

$$
x _ { 1 } = r \cos \phi \quad { \mathrm { a n d } } \quad x _ { 2 } = r \sin \phi .
$$

In a similar manner,

$$
\begin{array} { r } { z _ { 1 } = r \cos ( \phi + \theta ) = r \cos \phi \cos \theta - r \sin \phi \sin \theta = x _ { 1 } \cos \theta - x _ { 2 } \sin \theta } \\ { z _ { 2 } = r \sin ( \phi + \theta ) = r \cos \phi \sin \theta + r \sin \phi \cos \theta = x _ { 1 } \sin \theta + x _ { 2 } \cos \theta } \end{array}
$$

So the unique vector $\mathbf { z }$ that has the same $l _ { 2 }$ norm as $\mathbf { x }$ and is rotated by an angle of $\theta$ is given by multiplying $\mathbf { x }$ by the rotation matrix.

(b) Consider the the vector $\mathbf { x } = ( 1 , 1 ) ^ { t }$ , which has ${ \mathit { l } } _ { \infty }$ norm 1. If $\theta = \pi / 4$ , then

$$
\left[ { \begin{array} { r r } { \cos \theta } & { - \sin \theta } \\ { \sin \theta } & { \cos \theta } \end{array} } \right] \left[ { \begin{array} { r } { 1 } \\ { 1 } \end{array} } \right] = \left[ { \begin{array} { r r } { { \frac { \sqrt { 2 } } { 2 } } } & { - { \frac { \sqrt { 2 } } { 2 } } } \\ { { \frac { \sqrt { 2 } } { 2 } } } & { { \frac { \sqrt { 2 } } { 2 } } } \end{array} } \right] \left[ { \begin{array} { r } { 1 } \\ { 1 } \end{array} } \right] = \left[ { \begin{array} { r } { 0 } \\ { \sqrt { 2 } } \end{array} } \right] ,
$$

which has ${ \mathit { l } } _ { \infty }$ norm $\sqrt { 2 }$ .

$^ { * } 8$ . Let $P = ( p _ { i j } )$ be a rotation matrix with nonzero entries $p _ { j j } = p _ { i i } = \cos \theta$ , $p _ { i j } = - p _ { j i } = \sin { \theta }$ , and $p _ { k k } = 1$ , if $k \neq i$ and $k \neq j$ . For any $n \times n$ matrix $A$ ,

$$
( A P ) _ { r s } = \sum _ { k = 1 } ^ { n } a _ { r k } p _ { k s } .
$$

If $s \neq i , j$ , then $p _ { k s } = 0$ unless $k = s$ . Thus, $( A P ) _ { r s } = a _ { r s }$ . If $s = j$ , then

$$
( A P ) _ { r j } = a _ { r j } p _ { j j } + a _ { r i } p _ { i j } = a _ { r j } \cos \theta + a _ { r i } \sin \theta .
$$

If $s = i$ , then

$$
( A P ) _ { r i } = a _ { r j } p _ { j i } + a _ { r i } p _ { i i } = - a _ { r j } \sin \theta + a _ { r i } \cos { \theta }
$$

Similarly, $\textstyle ( P A ) _ { r s } = \sum _ { k = 1 } ^ { n } p _ { r k } a _ { k s }$ . If $r \neq i , j$ , then $p _ { r k } = 0$ unless $r = k$ . Thus, $( P A ) _ { r s } = a _ { r s }$ If $r = i$ , then

$$
P A ) _ { i s } = p _ { i j } a _ { j s } + p _ { i i } a _ { i s } = a _ { j s } \sin \theta + a _ { i s } \cos \theta .
$$

If $r = j$ , then

$$
( P A ) _ { j s } = p _ { j j } a _ { j s } + p _ { j i } a _ { i s } = a _ { j s } \cos \theta - a _ { i s } \sin \theta .
$$

9. Let is upper triangular and is upper Hessenberg. Then n Sinc $C = R Q$ , where n upper $R$ iangular matrix, $Q$ f . Thus $\begin{array} { r } { c _ { i j } = \sum _ { k = 1 } ^ { n } r _ { i k } q _ { k j } } \end{array}$ uif $R$ enberg m. Hence, $q _ { k j } = 0$ $k > j + 1$ $r _ { i k } = 0$ . Thus,  means $k < i$ $\begin{array} { r } { c _ { i j } = \sum _ { k = i } ^ { j + 1 } r _ { i k } q _ { k j } } \end{array}$ $\begin{array} { r } { c _ { i j } = \sum _ { k = i } ^ { n } r _ { i k } q _ { k j } } \end{array}$ =i . The sum will be zeror Hessenberg matrix. $i > j + 1$ $c _ { i j } = 0$ $i \geq j + 2$ $C$

10. (a) We have

$$
\begin{array} { c c } { { { \cal P } _ { 2 } ^ { e } { \cal P } _ { 3 } ^ { e } = } } & { { { \bf \pi } ^ { \nu } \cdot { \bf \Lambda } ^ { 0 } } } & { { { \bf 0 } } } \\ { { { \cal P } _ { 2 } ^ { e } { \cal P } _ { 3 } ^ { e } = } } & { { { \bf \pi } ^ { \nu } \cdot { \bf \Lambda } ^ { 0 } } } & { { { \bf 0 } } } & { { \cdots \ { \bf 0 } ^ { \nu } } } \\ { { { \bf 0 } } } & { { { \bf 0 } } } & { { { \bf 1 } } } & { { { \bf 0 } } } & { { \cdots \ { \bf 0 } ^ { \nu } } } \\ { { \vdots \ \quad \quad \vdots \quad } } & { { \vdots \ \ddots \ } } & { { \ddots \ \ddots } } & { { \vdots \ } } \\ { { \vdots \quad \quad \vdots \quad } } & { { \ddots \quad } } & { { \ddots \quad \ddots } } & { { { \bf \Lambda } _ { 0 } } } \\ { { { \bf 0 } } } & { { { \bf 0 } } } & { { \cdots \ } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf 0 } } } \\ { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { e } { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { \cdots \ { \bf \Lambda } ^ { 0 } } } \\ { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } \\ { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 1 } } } & { { \ddots \quad \ddots } } \\ { { \vdots \quad \quad } } & { { \vdots \quad \vdots \quad } } & { { \ddots \quad \ddots } } & { { \vdots \ } } \\ { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } \end{array}
$$

(b) Let $Q _ { k } \ = \ P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { k } ^ { t }$ be an upper triangular matrix except for the entries $( Q _ { k } ) _ { 2 , 1 }$ , matrix $( Q _ { k } ) _ { 3 , 2 }$ , . . . , $( P _ { k + 1 } ) ^ { t }$ $( Q _ { k } ) _ { k , k - 1 }$ −can only change columns , which may be nonzero. Since multiplying $k$ and $k + 1$ in forming $Q _ { k + 1 } = P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { k } ^ { t } P _ { k + 1 } ^ { t }$ $Q _ { k }$ by the rotation , we only need to consider the entries $( Q _ { k + 1 } ) _ { i , k }$ and $( Q _ { k + 1 } ) _ { i , k + 1 }$ , for $i = k { + } 2 , \ldots , n$ . First, we have

$$
( Q _ { k + 1 } ) _ { i , k } = \sum _ { j = 1 } ^ { n } ( Q _ { k } ) _ { i , j } \left( P _ { k + 1 } ^ { t } \right) _ { j , k } = ( Q _ { k } ) _ { i , k } c _ { k + 1 } + ( Q _ { k } ) _ { i , k - 1 } s _ { k + 1 } .
$$

However, $( Q _ { k } ) _ { i , k } = 0$ for $i > k$ and $( Q _ { k } ) _ { i , k + 1 } = 0$ , for $i > k + 1$ . Thus, $( Q _ { k + 1 } ) _ { i , k } = 0$ , for $i \geq k + 2$ . Further,

$$
( Q _ { k + 1 } ) _ { i , k + 1 } = - ( Q _ { k } ) _ { i , k } s _ { k + 1 } + ( Q _ { k } ) _ { i , k + 1 } c _ { k + 1 } = 0 ,
$$

for $i \geq k + 2$ . Thus, $Q _ { k + 1 } = P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { k + 1 } ^ { t }$ is upper triangular except for the entries in positions $( 2 , 1 )$ , $( 3 , 2 )$ , $\cdot \cdot \cdot$ , $( k , k - 1 ) , ( k + 1 , k )$ , which may be nonzero.

(c) From parts (a) and (b) and mathematical induction, it follows that the matrix $P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdots P _ { n } ^ { t }$ is upper triangular except that the entries in positions $( 2 , 1 )$ , $( 3 , 2 )$ , $\cdot \cdot \cdot$ , $( n , n - 1 )$ may be nonzero. Thus, the entries in positions $( i , j )$ , for $i \geq j + 2$ are zero, which means that $P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdots P _ { n } ^ { t }$ is an upper Hessenberg matrix.

Note: There is no material deleted here. Exercise 11 is placed on a separate page so that the alignment of the steps in the algorithm are easier to see.


<!-- chunk 0005: pages 281-347 -->
\*11. The following algorithm implements Jacobi’s method for symmetric matrices.

INPUT: dimension $n$ , matrix $A = \left( a _ { i j } \right)$ , tolerance $T O L$ , maximum number of iterations $N$ .

$$
\begin{array} { r l } & { b = | a _ { i i } - a _ { j j } | ; } \\ & { c = 2 a _ { i j } \ \mathrm { s i g n } ( a _ { i i } - a _ { j j } ) ; } \\ & { \mathrm { C O = 0 . 5 } \left( 1 + b / \left( c ^ { 2 } + b ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \right) ^ { \frac { 1 } { 2 } } ; } \\ & { \mathrm { S I = 0 . 5 } c / \left( C O \left( c ^ { 2 } + b ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \right) . } \end{array}
$$

STEP 11 If $k 1 > N$ then OUTPUT (’Maximum number of iterations exceeded’); STOP.

12. Jacobi’s method produces the following eigenvalues, accurate to within the tolerance:

(a) 3.414214, 0.5857864, 2.0000000; 3 iterations (b) 2.722246, 5.346462, −0.06870782; 3 iterations (c) 4.732051, 3, 1.267949; 3 iterations (d) 0.2547188, 1.822717, 3.177283, 4.745281; 3 iterations (e) −1.488068, $-$ 3.778287, 0.8275517, 3.438803; 3 iterations (f) 0.1922421, 1.189091, 0.5238224, 0.9948440; 3 iterations

13. (a) To within $1 0 ^ { - 5 }$ , the eigenvalues are 2.618034, 3.618034, 1.381966, and 0.3819660. (b) In terms of $p$ and $\rho$ the eigenvalues are $- 6 5 . 4 5 0 8 5 p / \rho , - 9 0 . 4 5 0 8 5 p / \rho , - 3 4 . 5 4 9 1 5 p / \rho$ , and $- 9 . 5 4 9 1 5 0 p / \rho$ .

14. (a) When $\alpha = 1 / 4$ , we have 0.97972997, 0.92060076, 0.82741863, 0.70771852, 0.57114328, 0.42886719, 0.29232093, 0.17255567, 0.07939063, and 0.02025441. (b) When $\alpha = 1 / 2$ , we have 0.95945994, 0.84120152, 0.65483725, 0.41543703, 0.14228657, −0.14226561, −0.41535813, −0.65488866, $^ -$ 0.84121873, and −0.95949118. (c) When $\alpha = 3 / 4$ , we have 0.93918991, 0.76180227, 0.48225588, 0.12315555, −0.28657015, 0.71339842, 1.12303720, 1.48233299, 1.76182810, and 1.93923676. The method appears to be stable for $\alpha \leq \textstyle { \frac { 1 } { 2 } }$ .

15. The actual eigenvalues are as follows:

(a) When $\alpha ~ = ~ \textstyle { \frac { 1 } { 4 } }$ we have 0.97974649, 0.92062677, 0.82743037, 0.70770751, 0.57115742, 0.42884258, 0.29229249, 0.17256963, 0.07937323, and 0.02025351.   
(b) When $\alpha ~ = ~ \frac { 1 } { 2 }$ we have 0.95949297, 0.84125353, 0.65486073, 0.41541501, 0.14231484, −0.14231484, −0.41541501, −0.65486073, $-$ 0.84125353, and −0.95949297.   
(c) When $\alpha \ : = \ : \frac { 3 } { 4 }$ we have 0.93923946, 0.76188030, 0.48229110, 0.12312252, −0.28652774, −0.71347226, −1.12312252, −1.48229110, $^ -$ 1.76188030, and −1.93923946. The method appears to be stable for $\alpha \leq \textstyle { \frac { 1 } { 2 } }$ .

# Exercise Set 9.6, page 625

1. (a) $s _ { 1 } = 1 + { \sqrt { 2 } }$ , $s _ { 2 } = - 1 + { \sqrt { 2 } }$ \*(b) $s _ { 1 } = \sqrt { 4 + \sqrt { 1 0 } }$ , $s _ { 2 } = \sqrt { 4 - \sqrt { 1 0 } }$ (c) $s _ { 1 } = \sqrt { 1 0 }$ , $s _ { 2 } = 2$ (d) $s _ { 1 } = \sqrt { 7 } , s _ { 2 } = 1 , s _ { 3 } = 1$

2. (a) $s _ { 1 } = { \sqrt { 2 } } , s _ { 2 } = { \sqrt { 2 } }$ (b) $s _ { 1 } = 2$ , $s _ { 2 } = 1$ , $s _ { 3 } = 1$ (c) $s _ { 1 } = \sqrt { 5 }$ , $s _ { 2 } = \sqrt { 3 }$ (d) $s _ { 1 } = \sqrt { 5 }$ , s2 = √2, $s _ { 3 } = 1$

3. (a)

$$
U = \left[ \begin{array} { c c } { { - 0 . 9 2 3 8 8 0 } } & { { - 0 . 3 8 2 6 8 3 } } \\ { { - 0 . 3 8 2 6 8 3 1 } } & { { 0 . 9 2 3 8 8 0 } } \end{array} \right] , \quad S = \left[ \begin{array} { c c } { { 2 . 4 1 4 2 1 4 } } & { { 0 } } \\ { { 0 } } & { { 0 . 4 1 4 2 1 4 } } \end{array} \right] ,
$$

$$
V ^ { t } = \left[ \begin{array} { r r } { { - 0 . 9 2 3 8 8 0 } } & { { - 0 . 3 8 2 6 8 3 } } \\ { { - 0 . 3 8 2 6 8 3 } } & { { 0 . 9 2 3 8 8 0 } } \end{array} \right]
$$

\*(b)

$$
U = \left[ \begin{array} { c c c } { { - 0 . 8 2 4 7 3 6 } } & { { 0 . 3 9 1 3 3 6 } } & { { 0 . 4 0 8 2 4 8 } } \\ { { - 0 . 5 2 1 6 0 9 } } & { { - 0 . 2 4 7 5 0 2 } } & { { - 0 . 8 1 6 4 9 7 } } \\ { { - 0 . 2 1 8 4 8 2 } } & { { - 0 . 8 8 6 3 4 0 } } & { { 0 . 4 0 8 2 4 8 } } \end{array} \right] , \quad S = \left[ \begin{array} { c c } { { 2 . 6 7 6 2 4 3 } } & { { 0 } } \\ { { 0 } } & { { 0 . 9 1 5 2 7 2 } } \\ { { 0 } } & { { 0 } } \end{array} \right] .
$$

(c)

$$
V ^ { t } = \left[ \begin{array} { r r } { { - 1 } } & { { 0 } } \\ { { 0 } } & { { - 1 } } \end{array} \right]
$$

(d)

$$
U = \left[ \begin{array} { r r r r r } { { - 0 . 4 3 6 4 3 6 } } & { { 0 . 7 0 7 1 0 7 } } & { { 0 . 4 0 8 2 4 8 } } & { { - 0 . 3 7 7 9 6 4 } } \\ { { 0 . 4 3 6 4 3 6 } } & { { 0 . 7 0 7 1 0 7 } } & { { - 0 . 4 0 8 2 4 8 } } & { { 0 . 3 7 7 9 6 4 } } \\ { { - 0 . 4 3 6 4 3 6 } } & { { 0 } } & { { - 0 . 8 1 6 4 9 7 } } & { { - 0 . 3 7 7 9 6 4 } } \\ { { - 0 . 6 5 4 6 5 4 } } & { { 0 } } & { { 0 } } & { { 0 . 7 5 5 9 2 9 } } \end{array} \right] , \quad S = \left[ \begin{array} { r r r r } { { 2 . 6 4 5 7 5 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right] ,
$$

4. (a)

$$
U = \left[ \begin{array} { c c } { { - 0 . 7 0 7 1 0 7 } } & { { 0 . 7 0 7 1 0 7 } } \\ { { 0 . 7 0 7 1 0 7 } } & { { 0 . 7 0 7 1 0 7 } } \end{array} \right] , \quad S = \left[ \begin{array} { c c } { { 1 . 4 1 4 2 1 4 } } & { { 0 } } \\ { { 0 } } & { { 1 . 4 1 4 2 1 4 } } \end{array} \right] ,
$$

$$
V ^ { t } = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] }
$$

(b)

$$
U = \left[ \begin{array} { c c c } { { - 0 . 5 7 7 3 5 0 } } & { { 0 . 4 0 8 2 4 8 } } & { { 0 . 7 0 7 1 0 7 } } \\ { { - 0 . 5 7 7 3 5 0 } } & { { 0 . 4 0 8 2 4 8 } } & { { - 0 . 7 0 7 1 0 7 } } \\ { { - 0 . 5 7 7 3 5 0 } } & { { - 0 . 8 1 6 4 9 7 } } & { { 0 } } \end{array} \right] , \quad S = \left[ \begin{array} { c c c } { { 2 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right] ,
$$

(c)

5. For the matrix $A$ in Example 2 we have

$$
A ^ { t } A = { \left[ \begin{array} { l l l l l } { 1 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 1 } & { 1 } & { 1 } \\ { 1 } & { 0 } & { 1 } & { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 0 } \\ { 1 } & { 1 } & { 0 } \end{array} \right] } = { \left[ \begin{array} { l l l } { 2 } & { 1 } & { 1 } \\ { 1 } & { 4 } & { 1 } \\ { 1 } & { 1 } & { 2 } \end{array} \right] }
$$

So $\begin{array} { l } { { A ^ { t } A ( 1 , 2 , 1 ) ^ { t } = ( 5 , 1 0 , 5 ) ^ { t } = 5 ( 1 , 2 , 1 ) ^ { t } , A ^ { t } A ( 1 , - 1 , 1 ) ^ { t } = ( 2 , - 2 , 2 ) ^ { t } = 2 ( 1 , - 1 , 1 ) ^ { t } , } } \\ { { A ( - 1 , 0 , 1 ) ^ { t } = ( - 1 , 0 , 1 ) ^ { t } . } } \end{array}$ , and $^ { * } 6$ . The rank of $a$ is the number of linearly independent rows in $A$ , and the rank of $A ^ { t }$ is the number of linearly independent row of $A ^ { t }$ , which corresponds to the number of linearly independent columns of $A$ . By Theorem 9.25 the number of linearly independent rows of a matrix is the same as the number of independent columns, so the rank of $A$ is the same as the rank of $A ^ { t }$ .

$^ { * } 7$ . Let $A$ be an $m \times n$ matrix. Theorem 9.25 implies that $\operatorname { R a n k } ( A ) = \operatorname { R a n k } ( A ^ { t } )$ , so $\operatorname { N u l l i t y } ( A ) =$ $n { \mathrm { - R a n k } } ( A )$ and N $\mathrm { { l l i t y } } ( A ^ { t } ) = m { \mathrm { { - R a n k } } } ( A ^ { t } ) = m { \mathrm { { - R a n k } } } ( A )$ . Hence $\mathrm { N u l l i t y } ( A ) = \mathrm { N u l l i t y } ( A ^ { t } )$ if and only if $n = m$ .

$^ { * } 8$ . The matrices $S$ and $S ^ { t }$ have nonzero values only on their diagonals, and the nonzero eigenvalues of $A ^ { t } A$ and $A A ^ { t }$ are the same, so the singular values of $A ^ { t }$ are on the diagonal of $S ^ { t }$ in decreasing order. In addition, the matrices $U$ and $V$ are both orthogonal, so a Singular Value Decomposition of $A ^ { t }$ is given by

$$
A ^ { t } = ( U S V ^ { t } ) ^ { t } = ( V ^ { t } ) ^ { t } S ^ { t } U ^ { t } = V S ^ { t } U ^ { t }
$$

9. $\mathrm { R a n k } ( S )$ is the number of nonzero entries on the diagonal of $S$ . This corresponds to the number of nonzero eigenvalues (counting multiplicities) of $A ^ { t } A$ . So $\operatorname { R a n k } ( S ) = \operatorname { R a n k } ( A ^ { t } A )$ , and by part (ii) of Theorem 9.26 this is the same as $\operatorname { R a n k } ( A )$ .

10. From Exercise 9 we know that $\operatorname { R a n k } ( A ) = \operatorname { R a n k } ( S )$ . Since $A$ and $S$ are both $m \times n$ ,

$$
\operatorname { R a n k } ( A ) + \operatorname { N u l l i t y } ( A ) = n = \operatorname { R a n k } ( S ) + \operatorname { N u l l i t y } ( S ) ,
$$

which implies that $\mathrm { N u l l i t y } ( A ) = \mathrm { N u l l i t y } ( S )$ .

$^ *$ 11. The matrices $U$ and $V$ are orthogonal, so they are nonsingular with $U ^ { - 1 } = U ^ { t }$ and $V ^ { - 1 } = V ^ { t }$ . Since

$$
\operatorname* { d e t } A = \operatorname* { d e t } U \cdot \operatorname* { d e t } S \cdot \operatorname* { d e t } V ^ { t } ,
$$

with $\operatorname* { d e t } U$ and $\operatorname* { d e t } V ^ { t }$ both nonzero, $\operatorname* { d e t } A = 0$ if and only if $\operatorname* { d e t } S = 0$ . Hence $A$ in nonsingular if and only if $S$ is nonsingular.

When $A ^ { - 1 }$ exists we have the Singular Value Decomposition of $A ^ { - 1 }$ given by

$$
A ^ { - 1 } = \left( U S V ^ { t } \right) ^ { - 1 } = ( V ^ { t } ) ^ { - 1 } S ^ { - 1 } U ^ { - 1 } = \left( V ^ { - 1 } \right) ^ { - 1 } S ^ { - 1 } U ^ { t } = V S ^ { - 1 } U ^ { t } .
$$

12. If $A$ is $m \times n$ , then $A ^ { t }$ is $n \times m$ , $A A ^ { t }$ is $n \times n$ , and $A ^ { t } A$ is $m \times m$ . So

$$
n = \operatorname { R a n k } ( A ) + \operatorname { N u l l i t y } ( A ) = \operatorname { R a n k } ( A A ^ { t } ) + \operatorname { N u l l i t y } ( A A ^ { t } ) \quad { \mathrm { a n d } } \quad m = \operatorname { R a n k } ( A ^ { t } A ) + \operatorname { N u l l i t y } ( A ^ { t } A )
$$

Since $\operatorname { R a n k } ( A ^ { t } A ) = \operatorname { R a n k } ( A ) = \operatorname { R a n k } ( A A ^ { t } )$ we have

$$
\mathrm { N u l l i t y } ( A ) = \mathrm { N u l l i t y } ( A ^ { t } A ) = \mathrm { N u l l i t y } ( A A ^ { t } ) \quad { \mathrm { i f ~ a n d ~ o n l y ~ i f } } \quad m = n .
$$

13. Yes. By Theorem 9.25 we have $\operatorname { R a n k } ( A ^ { t } A ) = \operatorname { R a n k } ( ( A ^ { t } A ) ^ { t } ) = \operatorname { R a n k } ( A A ^ { t } )$ . Applying part (iii) of Theorem 9.26 gives $\operatorname { R a n k } ( A A ^ { t } ) = \operatorname { R a n k } ( A ^ { t } A ) = \operatorname { R a n k } ( A )$ .

14. Because $P$ is orthogonal, we have $P ^ { - 1 } = P ^ { t }$ , so $( P A ) ^ { t } ( P A ) = A ^ { t } ( P ^ { t } P ) A = A ^ { t } A$ . The singular values of $A$ are the eigenvalues of $A ^ { t } A$ , which must agree with those of $( P A ) ^ { t } ( P A )$ . Hence the singular values of $A$ and $P A$ are the same.

$^ *$ 15. The condition number is defined on page 470 as

$$
K _ { 2 } ( A ) = | | A | | _ { 2 } | | A ^ { - 1 } | | _ { 2 } .
$$

By Theorem 7.15 on page 447, we have $\lvert \lvert A \rvert \rvert _ { 2 } ^ { 2 } = \rho ( A ^ { t } A )$ , which is the largest eigenvalue of $A ^ { t } A$ , that is, $s _ { 1 } ^ { 2 }$ .

In addition, Exercise 15 on page 450 states that the eigenvalues of the inverse of a nonsingular matrix are the reciprocals of the eigenvalues of the matrix, so

$$
| | A ^ { - 1 } | | _ { 2 } ^ { 2 } = \rho ( ( A ^ { - 1 } ) ^ { t } A ^ { - 1 } ) = \rho ( ( A ^ { t } ) ^ { - 1 } A ^ { - 1 } ) = \rho ( ( A A ^ { t } ) ^ { - 1 } )
$$

is the largest eigenvalue of $( A A ^ { t } ) ^ { - 1 }$ . This is the reciprocal of the smallest eigenvalue $A A ^ { t }$ . By Theorem 9.26, the nonzero eigenvalues of $A ^ { t } A$ and $A A ^ { t }$ are the same, so this value is $1 / s _ { n } ^ { 2 }$ . As a consequence,

$$
K _ { 2 } ( A ) = | | A | | _ { 2 } | | A ^ { - 1 } | | _ { 2 } = { \frac { s _ { 1 } } { s _ { n } } } .
$$

16. For 1(a)the $l _ { 2 }$ condition number is ${ \frac { 1 + { \sqrt { 2 } } } { - 1 + { \sqrt { 2 } } } } = 3 + 2 { \sqrt { 2 } }$ , and for $1 ( \mathrm { d } )$ it is $\sqrt { 7 }$ . For $2 ( \mathrm { a } )$ the $l _ { 2 }$ condition number is $1$ , and for $2 ( \mathrm { b } )$ it is 2.

17. (a) Use the tabulated values to construct

$$
\mathbf { b } = { \left[ \begin{array} { l } { y _ { 0 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \\ { y _ { 5 } } \end{array} \right] } = { \left[ \begin{array} { l } { 1 . 3 } \\ { 3 . 5 } \\ { 4 . 2 } \\ { 5 . 0 } \\ { 7 . 0 } \end{array} \right] } , \quad { \mathrm { a n d } } \quad A = { \left[ \begin{array} { l l } { 1 } & { x _ { 0 } } \\ { 1 } & { x _ { 1 } } \\ { 1 } & { x _ { 2 } } \\ { 1 } & { x _ { 3 } } \\ { 1 } & { x _ { 4 } } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 1 . 0 } \\ { 1 } & { 2 . 0 } \\ { 1 } & { 3 . 0 } \\ { 1 } & { 4 . 0 } \\ { 1 } & { 5 . 0 } \end{array} \right] } .
$$

The matrix $A$ has the singular value decomposition $A = U S V ^ { t }$ , where

$$
\boldsymbol { S } = \left[ \begin{array} { c c } { 7 . 6 9 1 2 1 3 } & { 0 } \\ { 0 } & { 0 . 9 1 9 3 7 0 } \\ { 0 } & { 0 } \\ { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] , \quad \boldsymbol { V } ^ { t } = \left[ \begin{array} { c c } { 0 . 2 6 6 9 3 4 } & { 0 . 9 6 3 7 1 5 } \\ { 0 . 9 6 3 7 1 5 } & { - 0 . 2 6 6 9 3 4 } \end{array} \right]
$$

and

So

$$
\mathbf { c } = U ^ { t } \mathbf { b } = \left[ \begin{array} { c } { 1 0 . 2 3 9 1 6 0 } \\ { - 0 . 0 2 4 1 9 6 } \\ { 0 . 2 1 9 0 1 3 } \\ { - 0 . 0 7 6 6 2 1 } \\ { 0 . 8 2 7 7 4 3 } \end{array} \right] ,
$$

and the components of $\mathbf { z }$ are

$$
z _ { 1 } = { \frac { c _ { 1 } } { s _ { 1 } } } = { \frac { 1 0 . 2 3 9 1 6 0 } { 7 . 6 9 1 2 1 3 } } = 1 . 3 3 , \quad { \mathrm { a n d } } \quad z _ { 2 } = { \frac { c _ { 2 } } { s _ { 2 } } } = { \frac { - 0 . 0 2 4 1 9 6 } { 0 . 9 1 9 3 7 0 } } = - 0 . 0 2 6 ,
$$

This gives the least squares coefficients in $P _ { 1 } ( x ) = a _ { 0 } + a _ { 1 } x$ a s

$$
\left[ \begin{array} { l } { a _ { 0 } } \\ { a _ { 1 } } \end{array} \right] = \mathbf { x } = V \mathbf { z } = \left[ \begin{array} { l } { 0 . 3 3 } \\ { 1 . 2 9 } \end{array} \right] ,
$$

that is, $P _ { 1 } ( x ) = 0 . 3 3 + 1 . 2 9 x$ .

(b) We have the same vector $\mathbf { b }$ as in part(a) but the matrix $a$ is now

$$
A = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 1 } & { 2 } & { 4 } \\ { 1 } & { 3 } & { 9 } \\ { 1 } & { 4 } & { 1 6 } \\ { 1 } & { 5 } & { 2 5 } \end{array} \right] } ~ .
$$

and

We now find the vector $\mathbf { c } = U ^ { t } \mathbf { b }$ , construct $\mathbf { z }$ by dividing the components of the vector $\mathbf { c }$ by the three singular values. Then the coefficients of the least squares polynomial are given by the components of the vector $V \mathbf { z }$ . This produces

$$
P _ { 2 } ( x ) = 0 . 1 8 + 1 . 4 1 8 5 7 1 x - 0 . 0 2 1 4 2 8 6 x ^ { 2 } .
$$

\*18. (a) Use the tabulated values to construct

$$
\mathbf { b } = { \left[ \begin{array} { l } { y _ { 0 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \\ { y _ { 5 } } \end{array} \right] } = { \left[ \begin{array} { l } { 1 . 8 4 } \\ { 1 . 9 6 } \\ { 2 . 2 1 } \\ { 2 . 4 5 } \\ { 2 . 9 4 } \\ { 3 . 1 8 } \end{array} \right] } , \quad { \mathrm { a n d } } \quad A = { \left[ \begin{array} { l l l } { 1 } & { x _ { 0 } } & { x _ { 0 } ^ { 2 } } \\ { 1 } & { x _ { 1 } } & { x _ { 1 } ^ { 2 } } \\ { 1 } & { x _ { 2 } } & { x _ { 2 } ^ { 2 } } \\ { 1 } & { x _ { 3 } } & { x _ { 3 } ^ { 2 } } \\ { 1 } & { x _ { 4 } } & { x _ { 4 } ^ { 2 } } \\ { 1 } & { x _ { 5 } } & { x _ { 5 } ^ { 2 } } \end{array} \right] } = { \left[ \begin{array} { l l l } { 1 } & { 1 . 0 } & { 1 . 0 } \\ { 1 } & { 1 . 1 } & { 1 . 2 1 } \\ { 1 } & { 1 . 3 } & { 1 . 6 9 } \\ { 1 } & { 1 . 5 } & { 2 . 2 5 } \\ { 1 } & { 1 . 9 } & { 3 . 6 1 } \\ { 1 } & { 2 . 1 } & { 4 . 4 1 } \end{array} \right] } .
$$

The matrix $A$ has the singular value decomposition $A = U S V ^ { t }$ , where

So

and the components of $\mathbf { z }$ are

$$
z _ { 1 } = \frac { c _ { 1 } } { s _ { 1 } } = \frac { - 5 . 9 5 5 0 0 9 } { 7 . 8 4 4 1 2 7 } = - 0 . 7 5 9 1 6 8 , z _ { 2 } = \frac { c _ { 2 } } { s _ { 2 } } = \frac { - 1 . 1 8 5 5 9 1 } { 1 . 2 2 3 7 9 0 } = - 0 . 9 6 8 7 8 6 ,
$$

and

$$
z _ { 3 } = { \frac { c _ { 3 } } { s _ { 3 } } } = { \frac { - 0 . 0 4 4 9 8 5 } { 0 . 0 7 0 0 9 4 } } = - 0 . 6 4 1 7 8 4 .
$$

This gives the least squares coefficients in $P _ { 2 } ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 }$ a s

$$
\left[ \begin{array} { r } { a _ { 0 } } \\ { a _ { 1 } } \\ { a _ { 2 } } \end{array} \right] = \mathbf { x } = V \mathbf { z } = \left[ \begin{array} { r } { 0 . 5 9 6 5 8 1 } \\ { 1 . 2 5 3 2 9 3 } \\ { - 0 . 0 1 0 8 5 3 } \end{array} \right] .
$$

The least squares error using these values uses the last three components of $\mathbf { c }$ , and is

$$
| | A \mathbf { x } - \mathbf { b } | | _ { 2 } = { \sqrt { c _ { 4 } ^ { 2 } + c _ { 5 } ^ { 2 } + c _ { 6 } ^ { 2 } } } = { \sqrt { ( - 0 . 0 0 3 7 3 2 ) ^ { 2 } + ( - 0 . 0 0 0 4 9 3 ) ^ { 2 } + ( - 0 . 0 0 1 9 6 3 ) ^ { 2 } } } = 0 . 0 0 4 2 4 4 .
$$

(b) Use the tabulated values to construct

$$
\mathbf { b } = { \left[ \begin{array} { l } { y _ { 0 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \\ { y _ { 5 } } \end{array} \right] } = { \left[ \begin{array} { l } { 1 . 8 4 } \\ { 1 . 9 6 } \\ { 2 . 2 1 } \\ { 2 . 4 5 } \\ { 2 . 9 4 } \\ { 3 . 1 8 } \end{array} \right] } , \quad { \mathrm { a n d } } \quad A = { \left[ \begin{array} { l l l l } { 1 } & { x _ { 0 } } & { x _ { 0 } ^ { 2 } } & { x _ { 0 } ^ { 3 } } \\ { 1 } & { x _ { 1 } } & { x _ { 1 } ^ { 2 } } & { x _ { 1 } ^ { 3 } } \\ { 1 } & { x _ { 2 } } & { x _ { 2 } ^ { 2 } } & { x _ { 2 } ^ { 3 } } \\ { 1 } & { x _ { 3 } } & { x _ { 3 } ^ { 2 } } & { x _ { 3 } ^ { 3 } } \\ { 1 } & { x _ { 4 } } & { x _ { 4 } ^ { 2 } } & { x _ { 4 } ^ { 3 } } \\ { 1 } & { x _ { 5 } } & { x _ { 5 } ^ { 2 } } & { x _ { 5 } ^ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l l l l } { 1 } & { 1 . 0 } & { 1 . 0 } & { 1 . 0 } \\ { 1 } & { 1 . 1 } & { 1 . 2 1 } & { 1 . 3 3 1 } \\ { 1 } & { 1 . 3 } & { 1 . 6 9 } & { 2 . 1 9 7 } \\ { 1 } & { 1 . 5 } & { 2 . 2 5 } & { 3 . 3 7 5 } \\ { 1 } & { 1 . 9 } & { 3 . 6 1 } & { 6 . 8 5 9 } \\ { 1 } & { 2 . 1 } & { 4 . 4 1 } & { 9 . 2 6 1 } \end{array} \right] } .
$$

The matrix $A$ has the singular value decomposition $A = U S V ^ { t }$ , where

and

So

$$
\mathbf { c } = U ^ { t } \mathbf { b } = \left[ \begin{array} { c } { - 5 . 6 3 2 3 0 9 } \\ { - 2 . 2 6 8 3 7 6 } \\ { 0 . 0 3 6 2 4 1 } \\ { 0 . 0 0 5 7 1 7 } \\ { - 0 . 0 0 0 8 4 5 } \\ { - 0 . 0 0 4 0 8 6 } \end{array} \right] ,
$$

and the components of $\mathbf { z }$ are

$$
\begin{array} { l } { { z _ { 1 } = \displaystyle \frac { c _ { 1 } } { s _ { 1 } } = \displaystyle \frac { - 5 . 6 3 2 3 0 9 } { 1 4 . 5 0 6 8 0 8 } = - 0 . 3 8 8 2 5 3 , \quad z _ { 2 } = \displaystyle \frac { c _ { 2 } } { s _ { 2 } } = \displaystyle \frac { - 2 . 2 6 8 3 7 6 } { 2 . 0 8 4 9 0 9 } = - 1 . 0 8 7 9 9 8 , } } \\ { { z _ { 3 } = \displaystyle \frac { c _ { 3 } } { s _ { 3 } } = \displaystyle \frac { 0 . 0 3 6 2 4 1 } { 0 . 1 9 8 7 6 0 } = 0 . 1 8 2 3 3 6 , \quad \mathrm { a n d } \quad z _ { 4 } = \displaystyle \frac { c _ { 4 } } { s _ { 4 } } = \displaystyle \frac { 0 . 0 0 5 7 1 7 } { 0 . 8 6 8 3 2 8 } = 0 . 6 5 8 4 3 . } } \end{array}
$$

This gives the least squares coefficients in $P _ { 2 } ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + a _ { 3 } x ^ { 3 }$ as

$$
\left[ \begin{array} { r } { a _ { 0 } } \\ { a _ { 1 } } \\ { a _ { 2 } } \\ { a _ { 3 } } \end{array} \right] = \mathbf { x } = V \mathbf { z } = \left[ \begin{array} { r } { 0 . 6 2 9 0 1 9 } \\ { 1 . 1 8 5 0 1 0 } \\ { 0 . 0 3 5 3 3 3 } \\ { - 0 . 0 1 0 0 4 7 } \end{array} \right] .
$$

The least squares error using these values uses the last two components of $\mathbf { c }$ , and is

$$
| | A \mathbf { x } - \mathbf { b } | | _ { 2 } = { \sqrt { c _ { 5 } ^ { 2 } + c _ { 6 } ^ { 2 } } } = { \sqrt { ( - 0 . 0 0 0 8 4 5 ) ^ { 2 } + ( - 0 . 0 0 4 0 8 6 ) ^ { 2 } } } = 0 . 0 0 4 1 7 2 .
$$

# Numerical Solutions of Nonlinear Systems of Equations

Exercise Set 10.1, page 636

1. Use Theorem 10.5

\*2. One example is $\mathbf { F } ( x _ { 1 } , x _ { 2 } ) = { \bigg ( } 1 , { \frac { 1 } { ( x _ { 1 } - 1 ) ^ { 2 } + x _ { 2 } ^ { 2 } } } { \bigg ) } ^ { t } .$

3. Use Theorem 10.5 for each of the partial derivatives.

\*4. The solutions are near (−1.5, 10.5) and $( 2 , 1 1 )$ .

(a) The graphs are shown in the figure below.

![](images/e14debc4b243f75339d1e84fe814e6198f97b344b27bdbfa25b51e14310963d1.jpg)

(b) Use

$$
\mathbf { G } _ { 1 } ( \mathbf { x } ) = \left( - 0 . 5 + { \sqrt { 2 x _ { 2 } - 1 7 . 7 5 } } , 6 + { \sqrt { 2 5 - ( x _ { 1 } - 1 ) ^ { 2 } } } \right) ^ { t }
$$

and

$$
\mathbf { G } _ { 2 } ( \mathbf { x } ) = \left( - 0 . 5 - \sqrt { 2 x _ { 2 } - 1 7 . 7 5 } , 6 + \sqrt { 2 5 - ( x _ { 1 } - 1 ) ^ { 2 } } \right) ^ { t } .
$$

For ${ \bf G } _ { 1 } ( { \bf x } )$ with $\mathbf { x } ^ { ( 0 ) } = ( 2 , 1 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( 1 . 5 4 6 9 4 6 6 , 1 0 . 9 6 9 9 9 4 ) ^ { t }$ , and for ${ \bf G } _ { 2 } ( { \bf x } )$ with $\mathbf { x } ^ { ( 0 ) } = ( - 1 . 5 , 1 0 . 5 )$ , we have $\mathbf { x } ^ { ( 3 4 ) } = ( - 2 . 0 0 0 0 0 3 , 9 . 9 9 9 9 9 6 ) ^ { t }$ .

$^ { * } 5$ . (a) Continuity properties can be easily shown. Moreover,

$$
\frac { 8 } { 1 0 } \leq \frac { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + 8 } { 1 0 } \leq 1 . 2 5
$$

and

$$
\frac { 8 } { 1 0 } \leq \frac { x _ { 1 } x _ { 2 } ^ { 2 } + x _ { 1 } + 8 } { 1 0 } \leq 1 . 2 8 7 5 ,
$$

so $\mathbf { G } ( \mathbf { x } ) \in D$ , whenever $\mathbf { x } \in D$ .

Further,

$$
\frac { \partial g _ { 1 } } { \partial x _ { 1 } } = \frac { 2 x _ { 1 } } { 1 0 } \quad \mathrm { ~ s o ~ } \left| \frac { \partial g _ { 1 } ( \mathbf { x } ) } { \partial x _ { 1 } } \right| \leq \frac { 3 } { 1 0 } , \quad \frac { \partial g _ { 1 } } { \partial x _ { 2 } } = \frac { 2 x _ { 2 } } { 1 0 } \quad \mathrm { ~ s o ~ } \left| \frac { \partial g _ { 2 } ( \mathbf { x } ) } { \partial x _ { 2 } } \right| \leq \frac { 3 } { 1 0 } ,
$$

$$
\frac { \partial g _ { 2 } } { \partial x _ { 1 } } = \frac { x _ { 2 } ^ { 2 } + 1 } { 1 0 } \quad \mathrm { ~ s o ~ } \left| \frac { \partial g _ { 2 } ( \mathbf { x } ) } { \partial x _ { 1 } } \right| \leq \frac { 3 . 2 5 } { 1 0 } , \quad \mathrm { ~ a n d ~ } \ \frac { \partial g _ { 2 } } { \partial x _ { 2 } } = \frac { 2 x _ { 1 } x _ { 2 } } { 1 0 } \quad \mathrm { ~ s o ~ } \left| \frac { \partial g _ { 2 } ( \mathbf { x } ) } { \partial x _ { 2 } } \right| \leq \frac { 4 . 5 } { 1 0 } .
$$

Since

$$
\left| \frac { \partial g _ { i } ( \mathbf { x } ) } { \partial x _ { j } } \right| \leq 0 . 4 5 = \frac { 0 . 9 } { 2 } ,
$$

for $i , j = 1 , 2$ , all hypothesis of Theorem 10.6 have been satisfied, and $\mathbf { G }$ has a unique fixed point in $D$ .

(b) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ and tolerance $1 0 ^ { - 5 }$ , we have $\mathbf { x } ^ { ( 1 3 ) } = ( 0 . 9 9 9 9 9 7 3 , 0 . 9 9 9 9 9 7 3 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ and tolerance $1 0 ^ { - 5 }$ , we have $\mathbf { x } ^ { ( 1 1 ) } = ( 0 . 9 9 9 9 9 8 4 , 0 . 9 9 9 9 9 9 1 ) ^ { t }$ .

6. (a) $\mathbf { G } = \left( x _ { 2 } / { \sqrt { 5 } } , 0 . 2 5 ( \sin x _ { 1 } + \cos x _ { 2 } ) \right) ^ { t }$ and $D = \{ ( x _ { 1 } , x _ { 2 } ) \mid 0 \leq x _ { 1 } , x _ { 1 } \leq 1 \}$ . (b) With $\begin{array} { r } { { \bf x } ^ { ( 0 ) } = \left( \frac { 1 } { 2 } , \frac { 1 } { 2 } \right) ^ { t } } \end{array}$ , we have $\mathbf { x } ^ { ( 1 0 ) } = ( 0 . 1 2 1 2 4 4 0 , 0 . 2 7 1 1 0 6 5 ) ^ { t }$ t. (c) With $\begin{array} { r } { { \bf x } ^ { ( 0 ) } = \left( \frac { 1 } { 2 } , \frac { 1 } { 2 } \right) ^ { t } } \end{array}$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 0 . 1 2 1 2 4 2 1 , 0 . 2 7 1 1 0 5 2 ) ^ { t }$ .

7. (a) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 5 . 0 0 0 0 0 0 0 0 , 0 . 0 0 0 0 0 0 0 , - 0 . 5 2 3 5 9 8 8 ) ^ { t }$ . (b) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( 1 . 0 3 6 4 0 1 1 , 1 . 0 8 5 7 0 7 2 , 0 . 9 3 1 1 9 1 1 3 ) ^ { t }$ . (c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 . 5 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 0 . 0 0 0 0 0 0 0 0 0 , 0 . 0 9 9 9 9 9 9 9 , 1 . 0 0 0 0 0 0 0 ) ^ { t }$ . (d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 0 . 4 9 8 1 4 4 7 1 , - 0 . 1 9 9 6 0 6 0 0 , - 0 . 5 2 8 8 2 5 9 5 ) ^ { i }$ t.

8. (a) With

$$
\mathbf { G } ( \mathbf { x } ) = \left( \sqrt { x _ { 1 } - x _ { 2 } ^ { 2 } } , \sqrt { x _ { 1 } ^ { 2 } - x _ { 2 } } \right) ^ { t } \quad \mathrm { a n d } \quad \mathbf { x } ^ { ( 0 ) } = ( 0 . 7 , 0 . 4 ) ^ { t } ,
$$

we have $\mathbf { x } ^ { ( 1 4 ) } = ( 0 . 7 7 1 8 4 6 4 7 , 0 . 4 1 9 6 5 1 3 1 )$ t.

(b) With

$$
\mathbf G ( \mathbf x ) = \left( x / \sqrt { 3 } , \sqrt { \left( 1 + x _ { 1 } ^ { 3 } \right) / ( 3 x _ { 1 } ) } \right) ^ { t } \quad \mathrm { a n d } \quad \mathbf x ^ { ( 0 ) } = ( 0 . 4 , 0 . 7 ) ^ { t } ,
$$

we have $\mathbf { x } ^ { ( 2 0 ) } = ( 0 . 4 9 9 9 9 8 0 , 0 . 8 6 6 0 2 2 1 ) ^ { t }$ t.

(c) With

$$
\mathbf { G } ( \mathbf { x } ) = \left( \sqrt { 3 7 - x _ { 2 } } , \sqrt { x _ { 1 } - 5 } , 3 - x _ { 1 } - x _ { 2 } \right) ^ { t } \quad \mathrm { a n d } \quad \mathbf { x } ^ { ( 0 ) } = ( 5 , 1 , - 1 ) ^ { t } ,
$$

we have $\mathbf { x } ^ { ( 1 0 ) } = ( 6 . 0 0 0 0 0 0 2 , 1 . 0 0 0 0 0 0 0 , - 3 . 9 9 9 9 9 7 1 ) ^ { t }$ .

(d) With

$$
\mathbf { G } ( \mathbf { x } ) = \left( \sqrt { 2 x _ { 3 } + x _ { 2 } - 2 x _ { 2 } ^ { 2 } } , \sqrt { \left( 1 0 x _ { 3 } + x _ { 1 } ^ { 2 } \right) / 8 } , x _ { 1 } ^ { 2 } / ( 7 x _ { 2 } ) \right) ^ { t } \quad \mathrm { a n d } \quad \mathbf { x } ^ { ( 0 ) } = ( 0 . 5 , 0 . 5 , 0 ) ^ { t } ,
$$

we have $\mathbf { x } ^ { ( 6 0 ) } = ( 0 . 5 2 9 1 5 4 8 , 0 . 4 0 0 0 0 1 8 , 0 . 0 9 9 9 9 8 5 3 ) ^ { t }$ .

9. (a) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 0 0 0 0 0 0 0 , 0 , - 0 . 5 2 3 5 9 8 8 ) ^ { t }$ . (b) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 4 ) } = ( 1 . 0 3 6 4 0 0 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { t } .$ (c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 3 ) } = ( 0 , 0 . 1 0 0 0 0 0 0 0 , 1 . 0 0 0 0 0 0 0 ) ^ { t }$ . (d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 4 ) } = ( 0 . 4 9 8 1 4 4 7 , - 0 . 1 9 9 6 0 5 9 , - 0 . 5 2 8 8 2 6 0 ) ^ { t }$ .

10. (a) Using $\mathbf { G } _ { 1 } ( \mathbf { x } ) = ( \sqrt { x _ { 1 } - { x _ { 2 } } ^ { 2 } } , \sqrt { { x _ { 1 } } ^ { 2 } } - x _ { 2 } ) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 0 . 7 , 0 . 4 ) ^ { t }$ as in Exercise 8(a) gives a square root of a negative number as the first iteration. Thus, the method fails. (b) Using $\mathbf { G } _ { 1 } ( \mathbf { x } ) = \left( x / \sqrt { 3 } , \sqrt { ( 1 + { x _ { 1 } } ^ { 3 } ) / ( 3 x _ { 1 } ) } \right) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 0 . 4 , 0 . 7 ) ^ { t }$ as in Exercise 8(b) gives $\mathbf { x } ^ { ( 1 0 ) } = ( 0 . 4 9 9 9 9 8 0 7 , 0 . 8 6 6 0 2 6 5 2 ) ^ { t }$ . The convergence is accelerated for this problem. (c) Using $\mathbf { G } _ { 1 } ( \mathbf { x } ) = ( \sqrt { 3 7 - x _ { 2 } } , \sqrt { x _ { 1 } - 5 } , 3 - x _ { 1 } - x _ { 2 } ) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 5 , 1 , - 1 ) ^ { t }$ as in Exercise 8(c) gives $\mathbf { x } ^ { ( 1 ) } = ( 6 , 1 , - 4 ) ^ { t }$ . The convergence very much accelerated for this problem. (d) Using $\mathbf { G } _ { 1 } ( \mathbf { x } ) = ( \sqrt { 2 x _ { 3 } + x _ { 2 } - { 2 x _ { 2 } } ^ { 2 } } , \sqrt { ( { 1 0 x _ { 3 } + x _ { 1 } } ^ { 2 } ) / 8 } , { x _ { 1 } } ^ { 2 } / ( 2 x _ { 2 } ) ) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 0 . 5 , 0 . 5 , 0 ) ^ { t }$ as in Exercise $8 ( \mathrm { d } )$ leads to division by zero as the first iteration. Thus, the method fails.

11. A stable solution occurs when $x _ { 1 } = 8 0 0 0$ and $x _ { 2 } = 4 0 0 0$ .

$^ { * } 1 2$ . Let $\mathbf { F } ( \mathbf { x } ) = ( f _ { 1 } ( \mathbf { x } ) , . . . , f _ { n } ( \mathbf { x } ) ) ^ { t }$ . Suppose $\mathbf { F }$ is continuous at $\mathbf { x _ { 0 } }$ . By Definition 10.3,

$$
\operatorname * { l i m } _ { \mathbf { x } \to \mathbf { x _ { 0 } } } f _ { i } ( \mathbf { x } ) = f _ { i } ( \mathbf { x } _ { 0 } ) , \quad \mathrm { f o r ~ e a c h } \ i = 1 , . . . , n .
$$

Given $\epsilon > 0$ , there exists $\delta _ { i } > 0$ such that

$$
| f _ { i } ( { \bf x } ) - f _ { i } ( { \bf x } _ { 0 } ) | < \epsilon ,
$$

whenever $0 < | | { \bf x } - { \bf x } _ { 0 } | | < \delta _ { i }$ and $\mathbf { x } \in D$ .

Let $\delta = \operatorname* { m i n } _ { 1 \leq i \leq n } \delta _ { i }$ . If $0 < | | \mathbf { x } - \mathbf { x } _ { 0 } | | < \delta$ , then $0 < | | { \bf x } - { \bf x } _ { 0 } | | < \delta _ { i }$ and $| f _ { i } ( { \bf x } ) - f _ { i } ( { \bf x } _ { 0 } ) | < \epsilon$ , for each $i = 1 , . . . , n$ , whenever $\mathbf { x } \in D$ . This implies that

$$
| | \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } _ { 0 } ) | | _ { \infty } < \epsilon ,
$$

whenever $| | \mathbf { x } - \mathbf { x } _ { 0 } | | < \delta$ and $\mathbf { x } \in D$ . By the equivalence of vector norms, the result holds for all vector norms by suitably adjusting $\delta$ .

For the converse, let $\epsilon > 0$ be given. Then there is a $\delta > 0$ such that

$$
| | \mathbf { F } ( \mathbf { x } ) - \mathbf { F } ( \mathbf { x } _ { 0 } ) | | < \epsilon ,
$$

whenever $\mathbf { x } \in D$ and $| | \mathbf { x } - \mathbf { x } _ { 0 } | | < \delta$ . By the equivalence of vector norms, a number $\delta ^ { \prime } > 0$ can be found with

$$
| | f _ { i } ( \mathbf { x } ) - f _ { i } ( \mathbf { x } _ { 0 } ) | | < \epsilon .
$$

whenever $\mathbf { x } \in D$ and $\| \mathbf { x } - \mathbf { x } _ { 0 } \| < \delta ^ { \prime }$ .

Thus, $\begin{array} { r } { \operatorname* { l i m } _ { \mathbf { x } \to \mathbf { x } _ { 0 } } f _ { i } ( \mathbf { x } ) = f _ { i } ( \mathbf { x } _ { 0 } ) } \end{array}$ , for $i = 1 , . . . , n$ . Since $\mathbf { F } ( \mathbf { x } _ { \mathrm { 0 } } )$ is defined, the conditions in Definition 10.3 hold, and $\mathbf { F }$ is continuous at $\mathbf { x } _ { \mathrm { 0 } }$ .

13. When $A = O$ , the zero matrix, the result follows immediately, because in this case $\mathbf { F } ( \mathbf { x } ) -$ $\mathbf { F } ( \mathbf { x } _ { \mathrm { 0 } } ) = \mathbf { 0 }$ for all $\mathbf { x }$ and $\mathbf { x } _ { \mathrm { 0 } }$ in $\mathbb { R } ^ { n }$ .

Suppose $A \neq O$ . Let $\mathbf { x } _ { \mathrm { 0 } }$ in $\mathbb { R } ^ { n }$ be arbitrary and $\varepsilon > 0$ . Choose $\delta = \varepsilon / | | A | |$ and $\mathbf { x } _ { 0 } - \mathbf { x } < \delta$ . Then

$$
| | F ( \mathbf { x } ) - F ( \mathbf { x } _ { 0 } ) | | = | | A \mathbf { x } - A \mathbf { x } _ { 0 } | | = | | A ( \mathbf { x } - \mathbf { x } _ { 0 } ) | | .
$$

so

$$
| | F ( \mathbf { x } ) - F ( \mathbf { x } _ { 0 } ) | | = | | A ( \mathbf { x } - \mathbf { x } _ { 0 } ) | | \leq | | A | | \cdot | | \mathbf { x } - \mathbf { x } _ { 0 } | | < | | A | | \cdot { \frac { \varepsilon } { | | A | | } } = \varepsilon .
$$

This, by Exercise 12, implies that $\mathbf { F }$ is continuous on $\mathbb { R } ^ { n }$ .

# Exercise Set 10.2, page 644

1. Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 4 9 5 8 9 3 6 , 1 . 9 8 3 4 2 3 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 5 1 3 1 6 1 6 , - 0 . 0 1 8 3 7 6 2 2 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 2 3 . 9 4 2 6 2 6 , 7 . 6 0 8 6 7 9 7 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 1 ) }$ cannot be computed since $J ( 0 )$ is singular.

2. Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 0 0 1 6 6 7 , 0 . 2 5 0 8 0 3 6 , - 0 . 5 1 7 3 8 7 4 ) ^ { t }$ \*(b) $\mathbf { x } ^ { ( 2 ) } = ( 4 . 3 5 0 8 7 7 , 1 8 . 4 9 1 2 3 , - 1 9 . 8 4 2 1 1 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 0 3 6 6 8 7 0 8 , 1 . 0 8 5 9 2 3 8 4 , 0 . 9 2 9 7 7 9 3 2 )$ t (d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 4 0 7 1 6 6 8 7 , 1 . 3 0 9 4 4 3 7 7 , - 0 . 8 5 8 9 5 4 7 7 ) ^ { t }$ t

3. Graphing in Maple gives the following:

(a) $( 0 . 5 , 0 . 2 ) ^ { t }$ and (1.1, 6.1)t   
(b) $( - 0 . 3 5 , 0 . 0 5 ) ^ { t } , ( 0 . 2 , - 0 . 4 5 ) ^ { t } , ( 0 . 4 , - 0 . 5 ) ^ { t }$ and $( 1 , - 0 . 3 ) ^ { t }$   
\*(c) $( - 1 , 3 . 5 ) ^ { t }$ , $( 2 . 5 , 4 ) ^ { t }$   
(d) (0.11, 0.27)t

4. Graphing in Maple gives the following:

$$
\begin{array} { r l } & { ( 0 . 5 , 0 . 5 , - 0 . 5 ) ^ { t } } \\ & { ( 7 , - 1 , - 2 ) ^ { t } } \\ & { ( 1 , 1 , 1 ) ^ { t } } \\ & { ( 1 , - 1 , 1 ) ^ { t } \mathrm { ~ a n d ~ } ( 1 , 1 , - 1 ) ^ { t } } \end{array}
$$

5. Newton’s method gives the following:

$$
\mathbf { W i t h { x } } ^ { ( 0 ) } = ( 0 . 5 , 2 ) ^ { t } , { \mathbf { x } } ^ { ( 3 ) } = ( 0 . 5 , 2 ) ^ { t } \mathbf { W i t h { x } } ^ { ( 0 ) } = ( 1 . 1 , 6 . 1 ) , { \mathbf { x } } ^ { ( 3 ) } = ( 1 . 0 9 6 7 1 9 7 , 6 . 0 4 0 9 3 2 9 ) ^ { t }
$$

(b) With $\mathbf { x } ^ { ( 0 ) } = ( - 0 . 3 5 , 0 . 0 5 ) ^ { t } , \mathbf { x } ^ { ( 3 ) } = ( - 0 . 3 7 3 6 9 8 2 2 , 0 . 0 5 6 2 6 6 4 9 0 ^ { t } \mathrm { W i t h } \mathbf { x } ^ { ( 0 ) } = ( 0 . 2 , - 0 . 4 5 ) ^ { t } , \mathbf { x } ^ { ( 3 ) } = ( 0 . 3 , - 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 . 4 , 0 , 0 . 4 , 0 . 4 , 0 , 0 . 4 , 0 . 4 , 0 , 0 . 4 , 0 , 0 . 4 , 0 , 0 . 4 , 0 , 0 , 0 . 4 , 0 , 0 , 0 . 4 , 0 , 0 , 0 . 4 , 1 . 5 , 0 , 0 , 0 , 0 , 0 . 4 , 1 . 5 , 0 , 0 , 0 , 0 , 1 . 5 , 0 , 0 , 0 , 1 . 5 , 0 , 0 , 1 .$ ( $0 . 1 4 7 8 3 9 2 4 , - 0 . 4 3 6 1 7 7 6 2 ) ^ { t }$ With $\mathbf { x } ^ { ( 0 ) } = ( 0 . 4 , - 0 . 5 ) ^ { t } , \mathbf { x } ^ { ( 3 ) } = ( 0 . 4 0 8 0 9 5 6 6 , - 0 . 4 9 2$ 62939)t With $\mathbf { x } ^ { ( 0 ) } = ( 1 , - 0 . 3 ) ^ { t } , \mathbf { x } ^ { ( 4 ) } = ( 1 . 0 3 3 0 7 1 5 , - 0 . 2 7 9 9 6 1 8 4 ) ^ { t }$   
\*(c) With $\mathbf { x } ^ { ( 0 ) } = ( - 1 , 3 . 5 ) ^ { t }$ , $\mathbf { x } ^ { ( 1 ) } = ( - 1 , 3 . 5 ) ^ { t }$ and $\mathbf { x } ^ { ( 0 ) } = ( 2 . 5 , 4 ) ^ { t }$ , $\mathbf { x } ^ { ( 3 ) } = ( 2 . 5 4 6 9 4 7 , 3 . 9 8 4 9 9 8 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ , $\mathbf { x } ^ { ( 6 ) } = ( 0 . 1 2 1 2 4 1 9 , 0 . 2 7 1 1 0 5 1 ) ^ { t }$ .

6. Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 1 2 ) } = ( 0 . 4 9 9 9 9 9 5 3 , 0 . 0 0 3 1 9 9 0 6 , - 0 . 5 2 3 5 1 8 8 6 ) ^ { t }$   
(b) $\mathfrak { c } ^ { ( 4 ) } = ( 6 . 1 7 1 0 7 4 6 2 , - 1 . 0 8 2 1 6 2 0 1 , - 2 . 0 8 8 9 1 2 5 1 )$ t   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 . 0 3 6 4 0 1 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } ~ = ~ ( 1 , - 1 , 1 ) ^ { t }$ , $\mathbf { x } ^ { ( 5 ) } \ = \ ( 0 . 9 , - 1 , 0 . 5 ) ^ { t }$ ; and with $\mathbf { x } ^ { ( 0 ) } ~ = ~ ( 1 , - 1 , 1 ) ^ { t }$ , $\mathbf { x } ^ { ( 5 ) } =$ $( 0 . 5 , 1 , - 0 . 5 ) ^ { t }$ .

7. Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 5 ) } = ( 0 . 5 0 0 0 0 0 0 0 , 0 . 8 6 6 0 2 5 4 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 6 ) } = ( 1 . 7 7 2 4 5 4 , 1 . 7 7 2 4 5 4 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 5 ) } = ( - 1 . 4 5 6 0 4 3 , - 1 . 6 6 4 2 3 0 , 0 . 4 2 2 4 9 3 4 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 4 ) } = ( 0 . 4 9 8 1 4 4 7 , - 0 . 1 9 9 6 0 5 9 , - 0 . 5 2 8 8 2 6 0 ) ^ { t }$

8. (a) Suppose $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ) ^ { t }$ is a solution to

$$
\begin{array} { c } { { 4 x _ { 1 } - x _ { 2 } + x _ { 3 } = x _ { 1 } x _ { 4 } , } } \\ { { { } } } \\ { { - x _ { 1 } + 3 x _ { 2 } - 2 x _ { 3 } = x _ { 2 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } - 2 x _ { 2 } + 3 x _ { 3 } = x _ { 3 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } = 1 . } } \end{array}
$$

Multiplying the first three equations by $^ { - 1 }$ and factoring gives

$$
\begin{array} { c } { { 4 ( - x _ { 1 } ) - ( - x _ { 2 } ) + ( - x _ { 3 } ) = ( - x _ { 1 } ) x _ { 4 } , } } \\ { { - ( - x _ { 1 } ) + 3 ( - x _ { 2 } ) - 2 ( - x _ { 3 } ) = ( - x _ { 2 } ) x _ { 4 } , } } \\ { { ( - x _ { 1 } ) - 2 ( - x _ { 2 } ) + 3 ( - x _ { 3 } ) = ( - x _ { 3 } ) x _ { 4 } , } } \\ { { ( - x _ { 1 } ) ^ { 2 } + ( - x _ { 2 } ) ^ { 2 } + ( - x _ { 3 } ) ^ { 2 } = 1 . } } \end{array}
$$

Thus, $( - x _ { 1 } , - x _ { 2 } , - x _ { 3 } , x _ { 4 } ) ^ { t }$ is also a solution.

(b) Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives $\mathbf { x } ^ { ( 5 ) } = ( 0 , 0 . 7 0 7 1 0 6 7 8 , 0 . 7 0 7 1 0 6 7 8 , 1 ) ^ { t }$ . Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 0 , 0 , 0 ) ^ { t }$ gives $\mathbf { x } ^ { ( 6 ) } = ( 0 . 8 1 6 4 9 6 5 8 , 0 . 4 0 8 2 4 8 2 9 , - 0 . 4 0 8 2 4 8 2 9 , 3 ) ^ { t }$ . Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , - 1 , 1 , - 1 ) ^ { t }$ gives x $\mathbf { \Phi } _ { \mathrm { * } } ^ { ( \mathsf { 0 } ) } = ( 0 . 5 7 7 3 5 0 2 7 , - 0 . 5 7 7 3 5 0 2 7 , 0 . 5 7 7 3 5 0 2 7 , 6 )$ t. The other three solutions follow easily from part (a).

9. With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 - 1 ) ^ { t }$ and $T O L = 1 0 ^ { - 6 }$ , we have $\mathbf { x } ^ { ( 2 0 ) } = ( 0 . 5 , 9 . 5 \times 1 0 ^ { - 7 } , - 0 . 5 2 3 5 9 8 8 ) ^ { t }$ .

10. Since $f _ { j } ( x _ { 1 } , \ldots , x _ { n } ) = a _ { j 1 } x _ { 1 } + a _ { j 2 } x _ { 2 } + \ldots + a _ { j n } x _ { n } - b _ { j }$ , we have ${ \frac { \dot { o } f _ { j } } { \partial x _ { 1 } } } = a _ { j i }$ . Hence,

$$
J ( \mathbf { x } ) = { \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \dots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \dots } & { a _ { 2 n } } \\ { \vdots } & { } & { } & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \dots } & { a _ { n n } } \end{array} \right] } = A .
$$

Further,

$$
\mathbf { F } \left( \mathbf { x } ^ { ( 0 ) } \right) = { \left[ \begin{array} { l l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { \dots } & { a _ { 1 n } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { \dots } & { a _ { 2 n } } \\ { \vdots } & & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \dots } & { a _ { n n } } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } ^ { ( 0 ) } } \\ { x _ { 2 } ^ { ( 0 ) } } \\ { \vdots } \\ { x _ { n } ^ { ( 0 ) } } \end{array} \right] } - { \left[ \begin{array} { l } { b _ { 1 } } \\ { b _ { 2 } } \\ { \vdots } \\ { b _ { n } } \end{array} \right] } = J \left( \mathbf { x } ^ { ( 0 ) } \right) \mathbf { x } ^ { ( 0 ) } - \mathbf { b } .
$$

Thus, given $\mathbf { x } ^ { ( 0 ) }$ , we have

$$
\begin{array} { r l } & { \mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } \left( J \left( \mathbf { x } ^ { ( 0 ) } \right) \mathbf { x } ^ { ( 0 ) } - \mathbf { b } \right) } \\ & { \qquad = \mathbf { x } ^ { ( 0 ) } - J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } J \left( \mathbf { x } ^ { ( 0 ) } \right) \mathbf { x } ^ { ( 0 ) } + J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } \mathbf { b } = J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } \mathbf { b } = A ^ { - 1 } \mathbf { b } . } \end{array}
$$

So given any $\mathbf { x } ^ { ( 0 ) }$ , the solution to the linear system is $\mathbf { x } ^ { ( 1 ) }$ .

11. When the dimension $n$ is $1$ , $\mathbf { F } ( \mathbf { x } )$ is a one-component function $f ( \mathbf { x } ) = f _ { 1 } ( \mathbf { x } )$ , and the vector $\mathbf { x }$ has only one component $x _ { 1 } = x$ . In this case, the Jacobian matrix $J ( \mathbf { x } )$ reduces to the $1 \times 1$ matrix $[ \partial f _ { 1 } / \partial x _ { 1 } ( { \bf x } ) ] = f ^ { \prime } ( { \bf x } ) = f ^ { \prime } ( x )$ . Thus, the vector equation

$$
\mathbf { x } ^ { ( k ) } = \mathbf { x } ^ { ( k - 1 ) } - J ( \mathbf { x } ^ { ( k - 1 ) } ) ^ { - 1 } \mathbf { F } ( \mathbf { x } ^ { ( k - 1 ) } )
$$

becomes the scalar equation

$$
x _ { k } = x _ { k - 1 } - f ( x _ { k - 1 } ) ^ { - 1 } f ( x _ { k - 1 } ) = x _ { k - 1 } - { \frac { f ( x _ { k - 1 } ) } { f ^ { \prime } ( x _ { k - 1 } ) } } .
$$

$^ { \ast } 1 2$ . The constants required for the pressure equation are in part (a). The approximate radius is in part (b).

(a) $k _ { 1 } = 8 . 7 7 1 2 5 , k _ { 2 } = 0 . 2 5 9 6 9 0 , k _ { 3 } = - 1 . 3 7 2 1 7$

(b) Solving the equation

$$
{ \frac { 5 0 0 } { \pi r ^ { 2 } } } = k _ { 1 } e ^ { k _ { 2 } r } + k _ { 3 } r
$$

numerically, gives $r = \mathrm { 3 . 1 8 5 1 7 }$ .

13. With $\theta _ { i } ^ { ( 0 ) } = 1$ , for each $i = 1 , 2 , \ldots , 2 0$ , the following results are obtained.

<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td></td><td>0.14062</td><td>0.19954</td><td>0.24522</td><td>0.28413</td><td>0.31878</td><td>0.35045</td></tr></table>

<table><tr><td>i</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td></td><td>0.37990</td><td>0.40763</td><td>0.43398</td><td>0.45920</td><td>0.48348</td><td>0.50697</td><td>0.52980</td></tr></table>

<table><tr><td>i</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr><tr><td></td><td>0.55205</td><td>0.57382</td><td>0.59516</td><td>0.61615</td><td>0.63683</td><td>0.65726</td><td>0.67746</td></tr></table>

14. (a) We have

$$
{ \frac { \partial E } { \partial a } } = 2 \sum _ { i = 1 } ^ { n } \left( w _ { i } y _ { i } - { \frac { a } { ( x _ { i } - b ) ^ { c } } } \right) \left( { \frac { 1 } { ( x _ { i } - b ) ^ { c } } } \right) = 0 ,
$$

$$
\frac { \partial E } { \partial b } = 2 \sum _ { i = 1 } ^ { n } \left( w _ { i } y _ { i } - \frac { a } { ( x _ { i } - b ) ^ { c } } \right) \left( \frac { - a c } { ( x _ { i } - b ) ^ { c + 1 } } \right) = 0 ,
$$

and

$$
{ \frac { \partial E } { \partial c } } = 2 \sum _ { i = 1 } ^ { n } \left( w _ { i } y _ { i } - { \frac { a } { ( x _ { i } - b ) ^ { c } } } \right) \ln ( x _ { i } - b ) \left( { \frac { - a } { ( x _ { i } - b ) ^ { c } } } \right) = 0 .
$$

Solving for $a$ in the first equation and substituting into the second and third equations gives the linear system.

(b) With $\mathbf { x } ^ { ( 0 ) } = ( 2 6 . 8 , 8 . 3 ) ^ { t } = ( b _ { 0 } , c _ { 0 } ) ^ { t }$ , we have $\mathbf { x } ^ { ( 7 ) } = ( 2 6 . 7 7 0 2 1 , 8 . 4 5 1 8 3 1 ) ^ { t }$ . Thus, $a =$ $2 . 2 1 7 9 5 2 \times 1 0 ^ { 6 }$ , $b = 2 6 . 7 7 0 2 1$ , $c = 8 . 4 5 1 8 3 1$ , and

$$
\sum _ { i = 1 } ^ { n } \left( w _ { i } y _ { i } - { \frac { a } { ( x _ { i } - b ) ^ { c } } } \right) ^ { 2 } = 0 . 7 8 2 1 1 3 9 .
$$

# Exercise Set 10.3, page 652

1. Broyden’s method gives the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 4 7 7 7 9 2 0 , 1 . 9 2 7 5 5 7 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 3 2 5 0 0 7 0 , - 0 . 1 3 8 6 9 6 7 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 2 2 9 3 7 2 , 0 . 8 2 4 3 4 9 1 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 7 7 9 5 0 0 , 1 . 7 4 3 3 9 6 ) ^ { t }$

2. Broyden’s method gives the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 0 0 2 3 1 2 3 , - 1 . 0 8 0 2 9 9 0 9 , - 0 . 5 2 3 8 2 3 9 4 ) ^ { t }$ . \*(b) $\mathbf { x } ^ { ( 2 ) } = ( - 6 7 . 0 0 5 8 2 8 , 3 8 . 3 1 4 9 3 5 , 3 1 . 6 9 0 8 9 3 ) ^ { t }$ . (c) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 4 0 3 6 0 2 4 2 , - 1 . 6 7 9 8 7 5 2 4 , 0 . 4 5 8 1 6 5 0 9 ) ^ { t }$ (d) $\mathfrak { c } ^ { ( 2 ) } = ( 0 . 4 9 8 4 0 5 8 0 , - 0 . 1 9 9 8 4 2 0 9 , - 0 . 5 2 8 5 1 3 5 3 )$ t

3. Broyden’s method gives the following:

(a) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 8 ) } = ( 0 . 5 , 2 ) ^ { t }$ .   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 3 7 3 6 9 8 2 , 0 . 0 5 6 2 6 6 4 9 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( 0 . 5 , 0 . 8 6 6 0 2 5 4 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 2 , 2 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 8 ) } = ( 1 . 7 7 2 4 5 4 , 1 . 7 7 2 4 5 4 ) ^ { t }$ .

4. Broyden’s method gives the following:

(a) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathfrak { c } ^ { ( 1 8 ) } = ( 0 . 4 9 9 9 9 9 5 3 , 0 . 0 0 3 1 9 9 0 4 , - 0 . 5 2 3 5 1 8 8 6 ) ^ { t }$ .   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 2 , 1 , - 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 0 ) } = ( 6 . 0 0 0 0 0 0 0 0 0 0 0 , 1 . 0 0 0 0 0 0 0 0 0 0 , - 4 . 0 0 0 0 0 0 0 0 0 0 ) ^ { \circ }$ t.   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( - 1 , - 2 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( - 1 . 4 5 6 0 4 3 , - 1 . 6 6 4 2 3 1 , 0 . 4 2 2 4 9 3 4 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 5 ) } = ( 0 . 4 9 8 1 4 4 7 , - 0 . 1 9 9 6 0 5 9 , - 0 . 5 2 8 8 2 6 0 ) ^ { t }$ .

5. Broyden’s method gives the following:

(a) With $\mathbf { x } ^ { ( 0 ) } = ( 2 . 5 , 4 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 3 ) } = ( 2 . 5 4 6 9 4 7 , 3 . 9 8 4 9 9 8 ) ^ { t }$   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 4 ) } = ( 0 . 1 2 1 2 4 1 9 , 0 . 2 7 1 1 0 5 2 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 3 ) } = ( 1 . 0 3 6 4 0 1 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , - 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 8 ) } = ( 0 . 9 , - 1 , 0 . 5 ) ^ { t }$ ; and with $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , - 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 8 ) } = ( 0 . 5 , 1 , - 0 . 5 ) ^ { t }$ .

6. (a) Suppose $( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ) ^ { t }$ is a solution to

$$
\begin{array} { c } { { 4 x _ { 1 } - x _ { 2 } + x _ { 3 } = x _ { 1 } x _ { 4 } , } } \\ { { { } } } \\ { { - x _ { 1 } + 3 x _ { 2 } - 2 x _ { 3 } = x _ { 2 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } - 2 x _ { 2 } + 3 x _ { 3 } = x _ { 3 } x _ { 4 } , } } \\ { { { } } } \\ { { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + x _ { 3 } ^ { 2 } = 1 . } } \end{array}
$$

Multiplying the first three equations by $^ { - 1 }$ and factoring gives

$$
\begin{array} { c } { { 4 ( - x _ { 1 } ) - ( - x _ { 2 } ) + ( - x _ { 3 } ) = ( - x _ { 1 } ) x _ { 4 } , } } \\ { { - ( - x _ { 1 } ) + 3 ( - x _ { 2 } ) - 2 ( - x _ { 3 } ) = ( - x _ { 2 } ) x _ { 4 } , } } \\ { { ( - x _ { 1 } ) - 2 ( - x _ { 2 } ) + 3 ( - x _ { 3 } ) = ( - x _ { 3 } ) x _ { 4 } , } } \\ { { ( - x _ { 1 } ) ^ { 2 } + ( - x _ { 2 } ) ^ { 2 } + ( - x _ { 3 } ) ^ { 2 } = 1 . } } \end{array}
$$

Thus, $( - x _ { 1 } , - x _ { 2 } , - x _ { 3 } , - x _ { 4 } ) ^ { t }$ is also a solution.

(b) Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives $\mathbf { x } ^ { ( 6 ) } = ( 0 , 0 . 7 0 7 1 0 6 7 8 , 0 . 7 0 7 1 0 6 7 8 , 1 ) ^ { t }$ . Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 0 , 0 , 0 ) ^ { t }$ gives $\mathfrak { c } ^ { ( \mathrm { ~ 1 5 } ) } = ( 0 . 8 1 6 4 9 6 5 9 , 0 . 4 0 8 2 4 8 2 1 , - 0 . 4 0 8 2 4 8 3 7 , 3 ) ^ { t } .$ Using $\mathbf { x } ^ { ( 0 ) } = ( 1 , - 1 , 1 , - 1 ) ^ { t }$ gives $\mathbf { x } ^ { ( 1 1 ) } = ( 0 . 5 7 7 3 5 0 3 4 , - 0 . 5 7 7 3 5 0 2 3 , 0 . 5 7 7 3 5 0 2 5 , 6 ) ^ { i }$ t. The other three solutions follow easily from part (a).

7. With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 - 1 ) ^ { t }$ , Broyden’s method gives $\mathbf { x } ^ { ( 5 6 ) } = ( 0 . 5 0 0 0 5 9 1 , 0 . 0 1 0 5 7 2 3 5 , - 0 . 5 2 2 4 8 1 8 ) ^ { t }$ $^ { * } 8$ . If $\mathbf { z } ^ { t } \mathbf { y } = 0$ , then ${ \bf z } = { \bf z } _ { 1 } + { \bf z } _ { 2 }$ , where $\mathbf { z } _ { 1 } = \mathbf { 0 }$ and $\mathbf { z } _ { 2 } = \mathbf { z }$ . Otherwise, let

$$
\mathbf { z } _ { 1 } = \frac { \mathbf { y } ^ { t } \mathbf { z } } { \| \mathbf { y } \| _ { 2 } ^ { 2 } } \mathbf { y }
$$

be parallel to $\mathbf { y }$ and let ${ \bf z } _ { 2 } = { \bf z } - { \bf z } _ { 1 }$ . Then

$$
\mathbf { z } _ { 2 } ^ { t } \mathbf { y } = \mathbf { z } ^ { t } \mathbf { y } - \mathbf { z } _ { 1 } ^ { t } \mathbf { y } = \mathbf { z } ^ { t } \mathbf { y } - \left[ \frac { \mathbf { y } ^ { t } \mathbf { z } } { \mathbf { y } ^ { t } \mathbf { y } } \mathbf { y } \right] ^ { t } \mathbf { y } = \mathbf { z } ^ { t } \mathbf { y } - \frac { \mathbf { z } ^ { t } \mathbf { y } } { \mathbf { y } ^ { t } \mathbf { y } } \mathbf { y } ^ { t } \mathbf { y } = 0 .
$$

$^ { * } 9$ . Let $\lambda$ be an eigenvalue of $M = \left( I + \mathbf { u v } ^ { t } \right)$ with eigenvector $\mathbf { x } \neq \mathbf { 0 }$ . Then

$$
\lambda \mathbf { x } = M \mathbf { x } = \left( I + \mathbf { u } \mathbf { v } ^ { t } \right) \mathbf { x } = \mathbf { x } + \left( \mathbf { v } ^ { t } \mathbf { x } \right) \mathbf { u } .
$$

Thus, $( \lambda - 1 ) \mathbf { x } = ( \mathbf { v } ^ { t } \mathbf { x } ) \mathbf { u }$ . If $\lambda = 1$ , then $\mathbf { v } ^ { t } \mathbf { x } = 0$ . So $\lambda = 1$ is an eigenvalue of $M$ with multiplicity $n - 1$ and eigenvectors $\mathbf { x } ^ { ( 1 ) } , \ldots , \mathbf { x } ^ { ( n - 1 ) }$ where $\mathbf { v } ^ { t } \mathbf { x } ^ { ( j ) } = 0$ , for $j = 1 , \ldots , n - 1$ .

Assuming $\lambda \neq 1$ implies $\mathbf { x }$ and $\mathbf { u }$ are parallel, so for some number $\alpha$ , we have $\mathbf { x } = \alpha \mathbf { u }$ . Then

$$
( \lambda - 1 ) \alpha \mathbf { u } = \left( \mathbf { v } ^ { t } ( \alpha \mathbf { u } ) \right) \mathbf { u } \quad { \mathrm { a n d } } \quad \alpha ( \lambda - 1 ) \mathbf { u } = \alpha \left( \mathbf { v } ^ { t } \mathbf { u } \right) \mathbf { u } ,
$$

which implies that

$$
\lambda - 1 = { \bf v } ^ { t } { \bf u } \quad \mathrm { o r } \quad \lambda = 1 + { \bf v } ^ { t } { \bf u } .
$$

Hence, $M$ has eigenvalues $\lambda _ { i }$ , $1 \leq i \leq n$ where $\lambda _ { i } = 1$ , for $i = 1 , \ldots , n - 1$ and $\lambda _ { n } = 1 + \mathbf { v } ^ { t } \mathbf { u }$ .   
Since $\begin{array} { r } { \operatorname* { d e t } M = \prod _ { i = 1 } ^ { n } \lambda _ { i } } \end{array}$ , we have $\operatorname* { d e t } M = 1 + \mathbf { v } ^ { t } \mathbf { u }$ .

$^ { * } 1 0$ . (a) Since $A ^ { - 1 }$ exists we can write $\operatorname* { d e t } \left( A + \mathbf { x } \mathbf { y } ^ { t } \right) = \operatorname* { d e t } \left( A + A A ^ { - 1 } \mathbf { x } \mathbf { y } ^ { t } \right) = \operatorname* { d e t } A \left( I + A ^ { - 1 } \mathbf { x } \mathbf { y } ^ { t } \right) = \operatorname* { d e t } A \operatorname* { d e t } \left( I + A ^ { - 1 } \mathbf { x } \mathbf { y } ^ { t } \right) .$ But $A ^ { - 1 }$ exists so $\operatorname* { d e t } A \neq 0$ . By Exercise 9, $\operatorname* { d e t } \left( I + A ^ { - 1 } \mathbf { x } \mathbf { y } ^ { t } \right) = 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x }$ . So $\left( A + \mathbf { x } \mathbf { y } ^ { t } \right) ^ { - 1 }$ exists if and only if $\mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } \neq - 1$ .

(b) Assume $\mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } \neq - 1$ so that $\left( A + \mathbf { x } \mathbf { y } ^ { t } \right) ^ { - 1 }$ exists. Therefore,

$$
\begin{array} { r l } & { A ^ { - 1 } - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } \bigg ] \left( A + \mathbf { x y } ^ { t } \right) = A ^ { - 1 } A - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } A } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } + A ^ { - 1 } \mathbf { x y } ^ { t } - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } \mathbf { x y } ^ { t } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } } \\ & { \qquad = I - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } + A ^ { - 1 } \mathbf { x y } ^ { t } - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } \mathbf { x y } ^ { t } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } } \\ & { \qquad = I - \cfrac { A ^ { - 1 } \mathbf { x y } ^ { t } - A ^ { - 1 } \mathbf { x y } ^ { t } - \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } A ^ { - 1 } \mathbf { x y } ^ { t } + A ^ { - 1 } \mathbf { x y } ^ { t } A ^ { - 1 } \mathbf { x y } } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } } \\ & { \qquad = I + \frac { \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } A ^ { - 1 } \mathbf { x y } ^ { t } - \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } \left( A ^ { - 1 } \mathbf { x y } ^ { t } \right) } { 1 + \mathbf { y } ^ { t } A ^ { - 1 } \mathbf { x } } = I . } \end{array}
$$

11. With $\mathbf { x } ^ { ( 0 ) } = ( 0 . 7 5 , 1 . 2 5 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 4 ) } = ( 0 . 7 5 0 1 9 4 8 , 1 . 1 8 4 7 1 2 ) ^ { t }$ . Thus, $a = 0 . 7 5 0 1 9 4 8 , b =$ 1.184712, and the error is 19.796.

# Exercise Set 10.4, page 659

1. The Steepest Descent method gives the following:

\*(a) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 1 ) } = ( 0 . 4 9 4 3 5 4 1 , 1 . 9 4 8 0 4 0 ) ^ { t }$ .   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 ) } = ( 0 . 5 0 6 8 0 3 0 4 , 0 . 9 1 7 8 0 0 5 1 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 2 , 2 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 ) } = ( 1 . 7 3 6 0 8 3 , 1 . 8 0 4 4 2 8 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 3 6 1 0 0 9 2 , 0 . 0 5 7 8 8 3 6 8 ) ^ { t }$ .

2. The Steepest Descent method gives the following:

(a) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 4 ) } = ( 1 . 0 4 3 6 0 5 , 1 . 0 6 4 0 5 8 , 0 . 9 2 4 6 1 1 8 ) ^ { t }$ .   
(b) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 9 ) } = ( 0 . 4 9 3 2 7 3 9 , 0 . 9 8 6 3 8 8 8 , - 0 . 5 1 7 5 9 6 4 ) ^ { t }$ .   
(c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 1 ) } = ( - 1 . 6 0 8 2 9 6 , - 1 . 1 9 2 7 5 0 , 0 . 7 2 0 5 6 4 2 ) ^ { t }$ .   
(d) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , we have $\mathbf { x } ^ { ( 1 ) } = ( 0 , 0 . 0 0 9 8 9 0 5 6 , 0 . 9 8 9 0 5 5 6 ) ^ { t }$ .

3. The Steepest Descent method with Newton’s method gives the following:

\*(a) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 , 2 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 , 0 . 8 6 6 0 2 5 4 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 4 ) } = ( 1 . 7 7 2 4 5 4 , 1 . 7 7 2 4 5 4 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 3 7 3 6 9 8 2 , 0 . 0 5 6 2 6 6 4 9 ) ^ { t }$

4. The Steepest Descent method with Newton’s method gives the following:

(a) $\mathbf { x } ^ { ( 3 ) } = ( 1 . 0 3 6 4 0 0 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 , 1 , - 0 . 5 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 5 ) } = ( - 1 . 4 5 6 0 4 3 , - 1 . 6 6 4 2 3 0 , 0 . 4 2 2 4 9 3 4 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 6 ) } = ( 0 . 0 0 0 0 0 0 0 0 , 0 . 1 0 0 0 0 0 0 1 , 1 . 0 0 0 0 0 0 0 ) ^ { t }$

5 . The Steepest Descent method gives the following:

(a) $\mathbf { x } ^ { ( 3 ) } = ( 1 . 0 3 6 4 0 0 , 1 . 0 8 5 7 0 7 , 0 . 9 3 1 1 9 1 4 ) ^ { i }$ t (b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 , 1 , - 0 . 5 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 5 ) } = ( - 1 . 4 5 6 0 4 3 , - 1 . 6 6 4 2 3 0 , 0 . 4 2 2 4 9 3 4 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 6 ) } = ( 0 . 0 0 0 0 0 0 0 0 , 0 . 1 0 0 0 0 0 0 1 , 1 . 0 0 0 0 0 0 0 ) ^ { t }$

$^ { * } 6$ . (a) We have $\alpha _ { 1 } = 0$ , $g _ { 1 } = g ( x _ { 1 } , . . . , x _ { n } ) = g \left( \mathbf { x } ^ { ( 0 ) } \right) = h ( \alpha _ { 1 } )$ , $\begin{array} { r } { g _ { 3 } = g \left( \mathbf { x } ^ { ( 0 ) } - \alpha _ { 3 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right) = } \end{array}$ $h \big ( \alpha _ { 3 } \big )$ , $g _ { 2 } = g \left( \mathbf { x } ^ { ( 0 ) } - \alpha _ { 2 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right) = h ( \alpha _ { 2 } )$ ,

$$
\begin{array} { r l } & { h _ { 1 } = \displaystyle \frac { \left( g _ { 2 } - g _ { 1 } \right) } { \left( \alpha _ { 2 } - \alpha _ { 1 } \right) } = g \left[ \mathbf { x } ^ { ( 0 ) } - \alpha _ { 1 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) , \mathbf { x } ^ { ( 0 ) } - \alpha _ { 2 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right] = h [ \alpha _ { 1 } , \alpha _ { 2 } ] , } \\ & { h _ { 2 } = \displaystyle \frac { \left( g _ { 3 } - g _ { 2 } \right) } { \left( \alpha _ { 3 } - \alpha _ { 2 } \right) } = g \left[ \mathbf { x } ^ { ( 0 ) } - \alpha _ { 2 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) , \mathbf { x } ^ { ( 0 ) } - \alpha _ { 3 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right] = h [ \alpha _ { 2 } , \alpha _ { 3 } ] , } \\ & { h _ { 3 } = \displaystyle \frac { \left( h _ { 2 } - h _ { 1 } \right) } { \left( \alpha _ { 3 } - \alpha _ { 1 } \right) } } \\ & { \quad = g \left[ \mathbf { x } ^ { ( 0 ) } - \alpha _ { 1 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) , \mathbf { x } ^ { ( 0 ) } - \alpha _ { 2 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) , \mathbf { x } ^ { ( 0 ) } - \alpha _ { 3 } \nabla g \left( \mathbf { x } ^ { ( 0 ) } \right) \right] = h [ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } ] . } \end{array}
$$

The Newton divided-difference form of the second interpolating polynomial is

$$
\begin{array} { l } { { P ( \alpha ) = h [ \alpha _ { 1 } ] + h [ \alpha _ { 1 } , \alpha _ { 2 } ] ( \alpha - \alpha _ { 1 } ) + h [ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } ] ( \alpha - \alpha _ { 1 } ) ( \alpha - \alpha _ { 2 } ) } } \\ { { \qquad = g _ { 1 } + h _ { 1 } ( \alpha - \alpha _ { 1 } ) + h _ { 3 } ( \alpha - \alpha _ { 1 } ) ( \alpha - \alpha _ { 2 } ) } } \\ { { \qquad = g _ { 1 } + h _ { 1 } \alpha + h _ { 3 } \alpha ( \alpha - \alpha _ { 2 } ) . } } \end{array}
$$

(b) $P ^ { \prime } ( \alpha ) = h _ { 1 } - \alpha _ { 2 } h _ { 3 } + 2 h _ { 3 } \alpha$ , so $P ^ { \prime } ( \alpha ) = 0$ when $\alpha = 0 . 5 ( \alpha _ { 2 } - h _ { 1 } / h _ { 3 } )$ .

# Exercise Set 10.5, page 666

1. The Continuation method and Eulers method gives:

(a) (3, −2.25)t (b) (0.42105263, 2.6184211)t (c) (2.173110, −1.3627731)t

2. The Continuation method and Eulers method gives:

(a) (2.3039880, −2.0010995)t (b) (0.59709702, 2.2579684)t (c) (2.1094460, −1.3345633)t

3. Using the Continuation method and Eulers method gives:

\*(a) (0.44006047, 1.8279835)t (b) $( - 0 . 4 1 3 4 2 6 1 3 , 0 . 0 9 6 6 9 4 6 8 ) ^ { \tau }$ (c) $( 0 . 4 9 8 5 8 9 0 9 , 0 . 2 4 9 9 9 0 9 1 , - 0 . 5 2 0 6 7 9 7 8 ) ^ { v }$ (d) $( 6 . 1 9 3 5 4 8 4 , 1 8 . 5 3 2 2 5 8 , - 2 1 . 7 2 5 8 0 6 ) ^ { u }$

4. (a) ( $- 1 5 . 7 8 4 3 2 7 2 4 , 5 . 2 9 9 7 4 5 8 9 ) ^ { t }$ is not comparable using $\mathbf { x } ( 0 ) \ : = \ : ( 0 , 0 ) ^ { t }$ as starting value. Using the starting values as in 10.2 Exercise $5 ( \mathrm { c } )$ gives: $\mathbf { x } ( 0 ) = ( - 1 , 3 . 5 ) ^ { t }$ leads to $( - 1 , 3 . 5 ) ^ { t }$ , and $\mathbf { x } ( 0 ) = ( 2 . 5 , 4 ) ^ { t }$ leads to (2.54694647, 3.9849976) $t$ (b) $( 0 . 1 2 1 2 4 1 9 5 , 0 . 2 7 1 1 0 5 1 6 ) ^ { t }$ using $\mathbf { x } ( 0 ) = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ is comparable to Newton’s method. Using $\mathbf { x } ( 0 ) = ( 0 , 0 ) ^ { t }$ leads to an error in the program. (c) $( 1 . 0 3 6 4 5 8 8 0 , 1 . 0 8 5 7 2 5 0 2 , 0 . 9 3 1 3 6 7 1 4 ) ^ { t }$ is comparable to Newton’s method. (d) Using $\mathbf { x } ( 0 ) = ( 0 , 0 , 0 ) ^ { t }$ does not allow computation of $\mathbf { x } ( 1 )$ . Using $\mathbf { x } ( 0 ) = ( 1 , - 1 , 1 ) ^ { t }$ gives $( 0 . 9 0 0 1 6 0 7 4 , - 1 . 0 0 2 3 8 0 0 8 , 0 . 4 9 6 6 1 0 9 3 ) ^ { u }$ which is nearly comparable to Newton’s method.

5. The Continuation method and the RungeKutta method of order four gives:

(a) With $\mathbf { x } ( 0 ) = ( - 1 , 3 . 5 ) ^ { t }$ the result is $( - 1 , 3 . 5 ) ^ { t }$ . \* With $\mathbf { x } ( 0 ) = ( 2 . 5 , 4 ) ^ { t }$ the result is (2.54694647, 3.98499746)t.   
(b) With $\mathbf { x } ( 0 ) = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ the result is $( 0 . 1 2 1 2 4 1 9 5 , 0 . 2 7 1 1 0 5 1 6 ) ^ { t }$ .   
(c) With $\mathbf { x } ( 0 ) = ( 1 , 1 , 1 ) ^ { t }$ the result is $( 1 . 0 3 6 4 0 0 4 7 , 1 . 0 8 5 7 0 6 5 5 , 0 . 9 3 1 1 9 1 4 4 ) ^ { \iota } .$ .

(d) With $\mathbf { x } ( 0 ) = ( 1 , - 1 , 1 ) ^ { t }$ the result is $( 0 . 9 0 0 1 6 0 7 4 , - 1 . 0 0 2 3 8 0 0 8 , 0 . 4 9 6 6 1 0 9 3 7 ) ^ { \tau } .$ With $\mathbf { x } ( 0 ) = ( 1 , 1 , - 1 ) ^ { t }$ the result is $( 0 . 5 0 1 0 4 0 3 5 , 1 . 0 0 2 3 8 0 0 8 , - 0 . 4 9 6 6 1 0 9 3 ) ^ { v }$ .

6. The Continuation method and the RungeKutta method of order four gives:

(a) $\left( 0 . 4 9 9 5 0 4 5 1 , 0 . 8 6 6 3 5 6 9 1 \right)$ t. This result is comparable since it required only 4 matrix inversions to obtain an answer almost as accurate as in Section 10.2 Exercise 3a with 5 iterations.   
(b) (1.7730066, 1.7703057)t. This result is comparable since it required only 4 matrix inversions to obtain an answer almost as accurate as in Section 10.2 Exercise 3b with 6 iterations.   
(c) $( - 1 . 4 5 6 9 2 1 7 , - 1 . 6 6 4 5 2 9 2 , 0 . 4 2 1 3 8 6 1 6 ) ^ { v }$ . This result is comparable to the result obtained in Section 10.2 Exercise 3c since it required only 4 matrix inversions as compared to 5 iterations of Newton’s method.   
(d) $( 0 . 4 9 8 1 3 3 6 4 , - 0 . 1 9 9 5 7 9 1 7 , - 0 . 5 2 8 8 2 7 7 3 ) ^ { \tau }$ . This result is comparable to the result obtained in Section 10.2 Exercise 3d.

7. The Continuation method and the RungeKutta method of order four gives:

(a) With $\mathbf { x } ( 0 ) = ( - 1 , 3 . 5 ) ^ { t }$ the result is $( - 1 , 3 . 5 ) ^ { t }$ . With $\mathbf { x } ( 0 ) = ( 2 . 5 , 4 ) ^ { t }$ the result is $( 2 . 5 4 6 9 4 6 5 , 3 . 9 8 4 9 9 7 5 ) ^ { t }$ .   
(b) With $\mathbf { x } ( 0 ) = ( 0 . 1 1 , 0 . 2 7 ) ^ { t }$ the result is $( 0 . 1 2 1 2 4 1 9 1 , 0 . 2 7 1 1 0 5 1 6 ) ^ { t }$ .   
(c) With $\mathbf { x } ( 0 ) = ( 1 , 1 , 1 ) ^ { t }$ the result is $( 1 . 0 3 6 4 0 0 4 7 , 1 . 0 8 5 7 0 6 5 5 , 0 . 9 3 1 1 9 1 4 4 ) ^ { \upsilon }$ .   
(d) With $\mathbf { x } ( 0 ) = ( 1 , - 1 , 1 ) ^ { t }$ the result is $( 0 . 9 0 0 1 5 9 6 4 , - 1 . 0 0 0 2 1 8 2 6 , 0 . 4 9 9 6 8 9 4 4 ) ^ { \iota }$ . With $\mathbf { x } ( 0 ) = ( 1 , 1 , - 1 ) ^ { t }$ the result is $( 0 . 5 0 0 9 6 5 3 , 1 . 0 0 0 2 1 8 2 6 , - 0 . 4 9 9 6 8 9 4 4 ) ^ { u }$ .

8. Using $\mathbf { x } ( 0 ) = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives

$$
\mathbf { x } ( 1 ) = \left( 1 0 ^ { - 1 0 } , 0 . 7 0 4 7 6 1 9 0 4 9 , 0 . 7 0 4 7 6 1 9 0 4 9 , 1 \right) ^ { t } .
$$

Using $\mathbf { x } ( 0 ) = ( 1 , 0 , 0 , 0 ) ^ { t }$ gives

x(1) = (0.8171787148, 0.4035113851, −0.4035113850, 2.993229684)t.

Using $\mathbf { x } ( 0 ) = ( 1 , - 1 , 1 , - 1 ) ^ { t }$ gives

$$
\mathbf { x } ( 1 ) = ( 0 . 5 7 6 9 8 4 1 3 8 7 , - 0 . 5 7 6 9 8 4 1 2 3 9 , 0 . 5 7 6 9 8 4 1 2 4 6 , 6 . 0 1 9 6 0 3 1 6 2 ) ^ { t }
$$

The other three solutions follow easily from Exercise 6(a) of Section 10.2.

9. The Continuation method and the RungeKutta method of order four gives the approximate solution, (0.50024553, 0.078230039, −0.52156996)t

$^ { * } 1 0$ . The system of differential equations to solve by Euler’s method is

$$
\begin{array} { r } { \mathbf { x } ^ { \prime } ( \lambda ) = - [ J ( \mathbf { x } ( \lambda ) ) ] ^ { - 1 } F ( \mathbf { x } ( 0 ) ) . } \end{array}
$$

With $N = 1$ , we have $h = 1$ and

$$
\mathbf { x } ( 1 ) = \mathbf { x } ( 0 ) + h [ - J ( \mathbf { x } ( 0 ) ) ] ^ { - 1 } F ( \mathbf { x } ( 0 ) ) = \mathbf { x } ( 0 ) - h J ( \mathbf { x } ( 0 ) ) ^ { - 1 } F ( \mathbf { x } ( 0 ) ) = \mathbf { x } ( 0 ) - J ( \mathbf { x } ( 0 ) ) ^ { - 1 } F ( \mathbf { x } ( 0 ) )
$$

However, Newton’s method gives

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - J \left( \mathbf { x } ^ { ( 0 ) } \right) ^ { - 1 } F \left( \mathbf { x } ^ { ( 0 ) } \right) .
$$

Since $\mathbf { x } ( 0 ) = \mathbf { x } ^ { ( 0 ) }$ , we have $\mathbf { x } ( 1 ) = \mathbf { x } ^ { ( 1 ) }$ .

11. For each $\lambda$ , we have

$$
0 = G ( \lambda , { \bf x } ( \lambda ) ) = F ( { \bf x } ( \lambda ) ) - e ^ { - \lambda } F ( { \bf x } ( 0 ) ) ,
$$

so

$$
0 = \frac { \partial F ( \mathbf { x } ( \lambda ) ) } { \partial \mathbf { x } } \frac { d \mathbf { x } } { d \lambda } + e ^ { - \lambda } F ( \mathbf { x } ( 0 ) ) = J ( \mathbf { x } ( \lambda ) ) \mathbf { x } ^ { \prime } ( \lambda ) + e ^ { - \lambda } F ( \mathbf { x } ( 0 ) )
$$

and

$$
J ( { \bf x } ( \lambda ) ) { \bf x } ^ { \prime } ( \lambda ) = - e ^ { - \lambda } F ( { \bf x } ( 0 ) ) = - F ( { \bf x } ( 0 ) ) .
$$

Thus

$$
\begin{array} { r } { \mathbf { x } ^ { \prime } ( \lambda ) = - J ( \mathbf { x } ( \lambda ) ) ^ { - 1 } F ( \mathbf { x } ( 0 ) ) . } \end{array}
$$

With $N = 1$ , we have $h = 1$ so that

$$
\mathbf { x } ( 1 ) = \mathbf { x } ( 0 ) - J ( \mathbf { x } ( 0 ) ) ^ { - 1 } F ( \mathbf { x } ( 0 ) ) .
$$

However, Newton’s method gives

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } - J ( \mathbf { x } ^ { ( 0 ) } ) ^ { - 1 } F ( \mathbf { x } ^ { ( 0 ) } ) .
$$

Since $\mathbf { x } ( 0 ) = \mathbf { x } ^ { ( 0 ) }$ , we have $\mathbf { x } ( 1 ) = \mathbf { x } ^ { ( 1 ) }$

12. (a) The CMRK4 algorithm with $N = 1$ requires the solution of 4 linear systems, which is almost as much work as required for 4 iterations of Newton’s method. Exercises 5, 6, and 8 yield appropriate comparisons. In only 5a, 5b, and 5c was CMRK4 competitive with Newton’s method. This suggests that CMRK4 with $N = 1$ is not as good as Newton’s Method. (b) Generally, the CMRK4 algorithm would yield good initial approximations for Newton’s method. This is well illustrated in Exercises 4b, 4c, 4d, 5, 6, and 8. (c) The CMRK4 algorithm with $N = 2$ requires the solution of 8 linear systems, which is almost as much work as required for 8 iterations of Newton’s method. Exercises 7 and 9 yield appropriate comparisons. Newton’s method outperformed CMRK4 in Exercise 7. The CMRK4 algorithm worked well in Exercise 9 which had the singular Jacobian. The results here suggest that CMRK4 with $N = 2$ is not as good as Newton’s method. (d) Since the CMRK4 algorithm with $N = 1$ generally yields good initial approximations for Newton’s method, we would not need to use the CMRK4 algorithm with $N = 2$ for this purpose.

# Boundary-Value Problems for Ordinary Differential Equations

Exercise Set 11.1, page 677

1. The Linear Shooting Algorithm gives the results in the following tables.

\*(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.5</td><td>0.82432432</td><td>0.82402714</td></tr></table>

(b)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.25</td><td>0.3937095</td><td>0.3936767</td></tr><tr><td>2</td><td>0.50</td><td>0.8240948</td><td>0.8240271</td></tr><tr><td>3</td><td>0.75</td><td>1.337160</td><td>1.337086</td></tr></table>

2. The Linear Shooting Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.78539816</td><td>-0.28245222</td><td>-0.28284271</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>π/8</td><td>-0.31541496</td><td>-0.31543220</td></tr><tr><td>2</td><td>π/4</td><td>-0.2828507</td><td>-0.282842712</td></tr><tr><td>3</td><td>3π/8</td><td>-0.20718437</td><td>-0.20719298</td></tr></table>

3. The Linear Shooting Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>Ci</td><td>W1i</td><td>y(xi）</td></tr><tr><td>3</td><td>0.3</td><td>0.7833204</td><td>0.7831923</td></tr><tr><td>6</td><td>0.6</td><td>0.6023521</td><td>0.6022801</td></tr><tr><td>9</td><td>0.9</td><td>0.8568906</td><td>0.8568760</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>5</td><td>1.25</td><td>0.1676179</td><td>0.1676243</td></tr><tr><td>10</td><td>1.50</td><td>0.4581901</td><td>0.4581935</td></tr><tr><td>15</td><td>1.75</td><td>0.6077718</td><td>0.6077740</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>0.3</td><td>-0.5185754</td><td>-0.5185728</td></tr><tr><td>6</td><td>0.6</td><td>-0.2195271</td><td>-0.2195247</td></tr><tr><td>9</td><td>0.9</td><td>-0.0406577</td><td>-0.0406570</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>1.3</td><td>0.0655336</td><td>0.06553420</td></tr><tr><td>6</td><td>1.6</td><td>0.0774590</td><td>0.07745947</td></tr><tr><td>9</td><td>1.9</td><td>0.0305619</td><td>0.03056208</td></tr></table>

4. The Linear Shooting Algorithm gives the results in the following tables.

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>W2i</td></tr><tr><td>1</td><td>0.15707963</td><td>1.05248506</td><td>0.25267869</td></tr><tr><td>2</td><td>0.31415927</td><td>1.07905470</td><td>0.08492370</td></tr><tr><td>3</td><td>0.47123890</td><td>1.07905469</td><td>-0.08492234</td></tr><tr><td>4</td><td>0.62831853</td><td>1.05248505</td><td>-0.25267729</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>W2i</td></tr><tr><td>1</td><td>0.15707963</td><td>-0.06061198</td><td>-0.29443007</td></tr><tr><td>2</td><td>0.31415927</td><td>-0.09117479</td><td>-0.09251254</td></tr><tr><td>3</td><td>0.47123890</td><td>-0.08959214</td><td>0.11091096</td></tr><tr><td>4</td><td>0.62831853</td><td>-0.05748564</td><td>0.29239128</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>W2i</td></tr><tr><td>5</td><td>1.25000000</td><td>0.64314227</td><td>0.28800448</td></tr><tr><td>10</td><td>1.50000000</td><td>0.68324209</td><td>0.07407700</td></tr><tr><td>15</td><td>1.75000000</td><td>0.69226853</td><td>0.01166358</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>W2i</td></tr><tr><td>3</td><td>0.60000000</td><td>-0.71219638</td><td>-1.82098025</td></tr><tr><td>5</td><td>1.00000000</td><td>-1.64068454</td><td>-2.81187530</td></tr><tr><td>8</td><td>1.60000000</td><td>-3.52051591</td><td>-2.83551329</td></tr></table>

\*5. The Linear Shooting Algorithm with $h = 0 . 0 5$ gives the following results.

<table><tr><td colspan="2"></td></tr><tr><td>i</td><td>Xi W1i</td></tr><tr><td>6 0.3</td><td>0.04990547</td></tr><tr><td>10 0.5</td><td>0.00673795</td></tr><tr><td>16 0.8</td><td>0.00033755</td></tr></table>

The Linear Shooting Algorithm with $h = 0 . 1$ gives the following results.

<table><tr><td>i Xi</td><td>W1i</td></tr><tr><td>3 0.3</td><td>0.05273437</td></tr><tr><td>5</td><td>0.5 0.00741571</td></tr><tr><td>8 0.8</td><td>0.00038976</td></tr></table>

$^ { * } 6$ . For Eq. (11.3), let $u _ { 1 } ( x ) = y$ and $u _ { 2 } ( x ) = y ^ { \prime }$ . Then

$$
u _ { 1 } ^ { \prime } ( x ) = u _ { 2 } ( x ) , \quad a \leq x \leq b , \quad u _ { 1 } ( a ) = \alpha
$$

and

$$
u _ { 2 } ^ { \prime } ( x ) = p ( x ) u _ { 2 } ( x ) + q ( x ) u _ { 1 } ( x ) + r ( x ) , \quad a \leq x \leq b , \quad u _ { 2 } ( a ) = 0 .
$$

For Eq. (11.4), let $v _ { 1 } ( x ) = y$ and $v _ { 2 } ( x ) = y ^ { \prime }$ . Then

$$
v _ { 1 } ^ { \prime } ( x ) = v _ { 2 } ( x ) , \quad a \leq x \leq b , \quad v _ { 1 } ( a ) = 0
$$

and

$$
v _ { 2 } ^ { \prime } ( x ) = p ( x ) v _ { 2 } ( x ) + q ( x ) v _ { 1 } ( x ) , \quad a \leq x \leq b , \quad v _ { 2 } ( a ) = 1 .
$$

Using the notation $u _ { 1 , i } = u _ { 1 } ( x _ { i } )$ , $u _ { 2 , i } = u _ { 2 } ( x _ { i } )$ , $v _ { 1 , i } = v _ { 1 } ( x _ { i } )$ and $v _ { 2 , i } = v _ { 2 } ( x _ { i } )$ leads to the equations in Step 4 of Algorithm 11.1.

7. (a) The approximate potential is $u ( 3 ) \approx 3 6 . 6 6 7 0 2$ using $h = 0 . 1$ . (b) The actual potential is $u ( 3 ) = 3 6 . 6 6 6 6 7$ .

$^ { * } 8$ . Since $y _ { 2 } ( a ) = 0$ and $y _ { 2 } ( b ) = 0$ , the boundary value problem

$$
y ^ { \prime \prime } = p ( x ) y ^ { \prime } + q ( x ) y , \quad a \leq x \leq b , \quad y ( a ) = 0 , \quad y ( b ) = 0
$$

has $y = 0$ as a unique solution, so $y _ { 2 } \equiv 0$ .

9. (a) There are no solutions if $b$ is an integer multiple of $\pi$ and $B \neq 0$ . (b) A unique solution exists whenever $b$ is not an integer multiple of $\pi$ . (c) There is an infinite number of solutions if $b$ is an multiple integer of $\boldsymbol { \mathscr { u } }$ and $B = 0$ .

$^ *$ 10. The unique solution is $y ( x ) = B \left( e ^ { x } - e ^ { - x } \right) / \left( e ^ { b } - e ^ { - b } \right)$ . For Exercise 9, we have $q ( x ) < 0$ , so Corollary 11.2 does not apply.

# Exercise Set 11.2, page 684

$^ { * } 1$ . The Nonlinear Shooting Algorithm gives $w _ { 1 } = 0 . 4 0 5 5 0 5 \approx \ln 1 . 5 = 0 . 4 0 5 4 6 5$ . 2. The Nonlinear Shooting Algorithm with $h = 0 . 2 5$ requires 4 iterations and gives:

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>-0.75</td><td>0.44444651</td><td>0.44444444</td></tr><tr><td>2</td><td>-0.5</td><td>0.40000229</td><td>0.4</td></tr><tr><td>3</td><td>-0.25</td><td>0.36363809</td><td>0.36363636</td></tr></table>

3. The Nonlinear Shooting Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>1.1</td><td>0.09530982</td><td>0.09531018</td></tr><tr><td>2</td><td>1.2</td><td>0.18232094</td><td>0.18232156</td></tr><tr><td>3</td><td>1.3</td><td>0.26236347</td><td>0.26236426</td></tr><tr><td>4</td><td>1.4</td><td>0.33647129</td><td>0.33647224</td></tr><tr><td>5</td><td>1.5</td><td>0.40546403</td><td>0.40546511</td></tr><tr><td>6</td><td>1.6</td><td>0.47000243</td><td>0.47000363</td></tr><tr><td>7</td><td>1.7</td><td>0.53062693</td><td>0.53062825</td></tr><tr><td>8</td><td>1.8</td><td>0.58778522</td><td>0.58778666</td></tr><tr><td>9</td><td>1.9</td><td>0.64185232</td><td>0.64185389</td></tr><tr><td>10</td><td>2.0</td><td>0.69314549</td><td>0.69314718</td></tr></table>

Convergence in 4 iterations gives $t = 1 . 0 0 0 0 0 1 7$

(b)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.15707963</td><td>1.16934027</td><td>1.16933413</td></tr><tr><td>2</td><td>0.31415927</td><td>1.36209813</td><td>1.36208552</td></tr><tr><td>3</td><td>0.47123890</td><td>1.57460167</td><td>1.57458304</td></tr><tr><td>4</td><td>0.62831853</td><td>1.80002060</td><td>1.79999746</td></tr><tr><td>5</td><td>0.78539816</td><td>2.02814008</td><td>2.02811498</td></tr><tr><td>6</td><td>0.94247780</td><td>2.24572329</td><td>2.24569937</td></tr><tr><td>7</td><td>1.09955743</td><td>2.43760187</td><td>2.43758190</td></tr><tr><td>8</td><td>1.25663706</td><td>2.58845757</td><td>2.58844295</td></tr><tr><td>9</td><td>1.41371669</td><td>2.68503045</td><td>2.68502044</td></tr><tr><td>10</td><td>1.57079633</td><td>2.71829004</td><td>2.71828183</td></tr></table>

Convergence requires 4 iterations and gives $t = 1 . 0 0 0 0 3 0 1$ .

(c)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.83775804</td><td>0.86205941</td><td>0.86205848</td></tr><tr><td>2</td><td>0.89011792</td><td>0.88156057</td><td>0.88155882</td></tr><tr><td>3</td><td>0.94247780</td><td>0.89945618</td><td>0.89945372</td></tr><tr><td>4</td><td>0.99483767</td><td>0.91579268</td><td>0.91578959</td></tr><tr><td>5</td><td>1.04719755</td><td>0.93060849</td><td>0.93060486</td></tr></table>

Convergence requires 3 iterations and gives $t = 0 . 4 2 0 4 6 7 2 5$ .

(d)

<table><tr><td>i</td><td>Xi</td><td>W1i</td></tr><tr><td>1</td><td>0.15707963</td><td>2.15645346 2.15643446</td></tr><tr><td>2</td><td>0.31415927</td><td>2.30905208 2.30901699</td></tr><tr><td>3</td><td>0.47123890</td><td>2.45403919 2.45399050</td></tr><tr><td>4</td><td>0.62831853</td><td>2.58784539 2.58778525</td></tr><tr><td>5</td><td>0.78539816</td><td>2.70717651 2.70710678</td></tr><tr><td>6</td><td>0.94247780</td><td>2.80909468 2.80901699</td></tr><tr><td>7</td><td>1.09955743</td><td>2.89109072 2.89100652</td></tr><tr><td>8</td><td>1.25663706</td><td>2.95114591 2.95105652</td></tr><tr><td>9</td><td>1.41371669</td><td>2.98778172 2.98768834</td></tr><tr><td>10</td><td>1.57079633</td><td>3.00009624 3.00000000</td></tr><tr><td>11</td><td>1.72787596</td><td>2.98778634 2.98768834</td></tr><tr><td>12</td><td>1.88495559</td><td>2.95115520 2.95105652</td></tr><tr><td>13</td><td>2.04203522</td><td>2.89110479 2.89100652</td></tr><tr><td>14</td><td>2.19911486</td><td>2.80911373 2.80901699</td></tr><tr><td>15</td><td>2.35619449</td><td>2.70720082 2.70710678</td></tr><tr><td>16</td><td>2.51327412</td><td>2.58787536 2.58778525</td></tr><tr><td>17</td><td>2.67035376</td><td>2.45407537 2.45399050</td></tr><tr><td>18</td><td>2.82743339</td><td>2.30909523 2.30901699</td></tr><tr><td>19</td><td>2.98451302</td><td>2.15650454 2.15643446</td></tr><tr><td>20</td><td>3.14159265</td><td>2.00006028 2.00000000</td></tr></table>

Convergence requires 8 iterations and gives $t = 1 . 0 0 0 1 2 5 3$ .

4. The Nonlinear Shooting Algorithm gives the results in the following tables.

\*(a) 4 iterations are required, giving:

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>1.3</td><td>0.4347835</td><td>0.4347826</td></tr><tr><td>6</td><td>1.6</td><td>0.3846170</td><td>0.3846154</td></tr><tr><td>9</td><td>1.9</td><td>0.3448300</td><td>0.3448276</td></tr></table>

(b) 6 iterations are required, giving:

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi</td></tr><tr><td>3</td><td>1.3</td><td>2.069249</td><td>2.069231</td></tr><tr><td>6</td><td>1.6</td><td>2.225013</td><td>2.225000</td></tr><tr><td>9</td><td>1.9</td><td>2.426317</td><td>2.426316</td></tr></table>

(c) 3 iterations are required, giving:

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>2.3</td><td>1.2676912</td><td>1.2676917</td></tr><tr><td>6</td><td>2.6</td><td>1.3401256</td><td>1.3401268</td></tr><tr><td>9</td><td>2.9</td><td>1.4095359</td><td>1.4095383</td></tr></table>

(d) To apply the algorithm we need to redefine the initial value of $T K$ to be 2. Then 7 iterations are required, giving:

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi）</td></tr><tr><td>5</td><td>1.25</td><td>0.4358290</td><td>0.4358272</td></tr><tr><td>10</td><td>1.50</td><td>1.3684496</td><td>1.3684447</td></tr><tr><td>15</td><td>1.75</td><td>2.9992010</td><td>2.9991909</td></tr></table>

5. \*(a) Modify Algorithm 11.2 as follows:

STEP 1 Set $h = ( b - a ) / N$ ; $k = 2$ ; $T K 1 = ( \beta - \alpha ) / ( b - a ) .$ .   
STEP 2 Set $w _ { 1 , 0 } = \alpha$ ; $w _ { 2 , 0 } = T K 1$ .   
STEP 3 For $i = 1 , \ldots , N$ do Steps 4 and 5.

STEP 4 Set $x = a + ( i - 1 ) h$ . STEP 5 Set

$$
\begin{array} { r l } & { k _ { 1 , 1 } = h w _ { 2 , i - 1 } ; } \\ & { k _ { 1 , 2 } = h f ( x , w _ { 1 , i - 1 } , w _ { 2 , i - 1 } ) ; } \\ & { k _ { 2 , 1 } = h ( w _ { 2 , i - 1 } + k _ { 1 , 2 } / 2 ) ; } \\ & { k _ { 2 , 2 } = h f ( x + h / 2 , w _ { 1 , i - 1 } + k _ { 1 , 1 } / 2 , w _ { 2 , i - 1 } + k _ { 1 , 2 } / 2 ) ; } \\ & { k _ { 3 , 1 } = h ( w _ { 2 , i - 1 } + k _ { 2 , 2 } / 2 ) ; } \\ & { k _ { 3 , 2 } = h f ( x + h / 2 , w _ { 1 , i - 1 } + k _ { 2 , 1 } / 2 , w _ { 2 , i - 1 } + k _ { 2 , 2 } / 2 ) ; } \\ & { k _ { 4 , 1 } = h ( w _ { 2 , i - 1 } + k _ { 3 , 2 } / 2 ) ; } \\ & { k _ { 4 , 2 } = h f ( x + h / 2 , w _ { 1 , i - 1 } + k _ { 3 , 1 } , w _ { 2 , i - 1 } + k _ { 3 , 2 } ) ; } \\ & { w _ { 1 , i } = w _ { 1 , i - 1 } + \big ( k _ { 1 , 1 } + 2 k _ { 2 , 1 } + 2 k _ { 3 , 1 } + k _ { 4 , 1 } \big ) / 6 ; } \\ & { w _ { 2 , i } = w _ { 2 , i - 1 } + \big ( k _ { 1 , 2 } + 2 k _ { 2 , 2 } + 2 k _ { 3 , 2 } + k _ { 4 , 2 } \big ) / 6 . } \end{array}
$$

STEP 6 Set $T K 2 = T K 1 + ( \beta - w _ { 1 , N } ) / ( b - a )$ .   
STEP 7 While $k \leq M )$ do Steps 8–15.   
STEP 8 Set $w _ { 2 , 0 } = T \kappa 2$ ; HOLD = w1,N.   
STEP 9 For i = 1, . . . , N do Steps 10 and 11. STEP 10 (Same as STEP 4 ) STEP 11 (Same as STEP 5 )   
STEP 12 If $| w _ { 1 , N } - \beta | \leq T O L$ then do Steps 13 and 14. STEP 13 For $i = 0 , \ldots , N$ set $x = a + i h$ ; $\operatorname { O U T P U T } ( x , w _ { 1 , i } , w _ { 2 , i } )$ . STEP 14 STOP.   
STEP 15 Set $\begin{array} { r l } & { T K = T K 2 - ( w _ { 1 , N } - \beta ) ( T K 2 - T K 1 ) / ( w _ { 1 . N } - H O L D ) ; } \\ & { T K 1 = T K 2 ; } \\ & { T K 2 = T K ; } \\ & { k = k + 1 . } \end{array}$

STEP 16 OUTPUT(’Maximum number of iterations exceeded.’); STOP.

(b) For 3(a), 3 iterations give:

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>1.2</td><td>0.45453896</td><td>0.45454545</td></tr><tr><td>2</td><td>1.4</td><td>0.41665348</td><td>0.41666667</td></tr><tr><td>3</td><td>1.6</td><td>0.38459538</td><td>0.38461538</td></tr><tr><td>4</td><td>1.8</td><td>0.35711592</td><td>0.35714286</td></tr></table>

For 3(c), 3 iterations give:

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>2.2</td><td>1.24299575</td><td>1.24300281</td></tr><tr><td>2</td><td>2.4</td><td>1.29211897</td><td>1.29213540</td></tr><tr><td>3</td><td>2.6</td><td>1.34009800</td><td>1.34012683</td></tr><tr><td>4</td><td>2.8</td><td>1.38671706</td><td>1.38676227</td></tr></table>

# Exercise Set 11.3, page 689

$^ { * } 1$ . The Linear Finite-Difference Algorithm gives following results.

(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi）</td></tr><tr><td>1</td><td>0.5</td><td>0.83333333</td><td>0.82402714</td></tr></table>

(b)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.25</td><td>0.39512472</td><td>0.39367669</td></tr><tr><td>2</td><td>0.5</td><td>0.82653061</td><td>0.82402714</td></tr><tr><td>3</td><td>0.75</td><td>1.33956916</td><td>1.33708613</td></tr></table>

(c) Extrapolation gives

$$
y \left( { \frac { 1 } { 2 } } \right) \approx { \frac { 4 ( 0 . 8 2 6 5 3 0 6 1 ) - 0 . 8 3 3 3 3 3 3 3 } { 3 } } = 0 . 8 2 4 2 6 3 0 4
$$

2. The Linear Finite-Difference Algorithm gives following results.

(a)

<table><tr><td>i</td><td>Ci</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>T/4</td><td>-0.28287080</td><td>-0.282842712</td></tr><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>π/8</td><td>-0.31568540</td><td>-0.31543220</td></tr><tr><td>2</td><td>π/4</td><td>-0.28290585</td><td>-0.282842712</td></tr><tr><td>3</td><td>3π/8</td><td>-0.20699563</td><td>-0.20719298</td></tr></table>

(c) Extrapolation gives

$$
y \left( { \frac { \pi } { 4 } } \right) \approx { \frac { 4 ( - 0 . 2 8 2 9 0 5 8 5 ) - ( - 0 . 2 8 2 8 7 0 8 0 ) } { 3 } } = - 0 . 2 8 2 9 1 7 5 3 3
$$

3. The Linear Finite-Difference Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>2</td><td>0.2</td><td>1.018096</td><td>1.0221404</td></tr><tr><td>5</td><td>0.5</td><td>0.5942743</td><td>0.59713617</td></tr><tr><td>7</td><td>0.7</td><td>0.6514520</td><td>0.65290384</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>5</td><td>1.25</td><td>0.16797186</td><td>0.16762427</td></tr><tr><td>10</td><td>1.50</td><td>0.45842388</td><td>0.45819349</td></tr><tr><td>15</td><td>1.75</td><td>0.60787334</td><td>0.60777401</td></tr></table>

<table><tr><td>i</td><td>Ci</td><td>W1i</td><td>y(xi）</td></tr><tr><td>3</td><td>0.3</td><td>-0.5183084</td><td>-0.5185728</td></tr><tr><td>6</td><td>0.6</td><td>-0.2192657</td><td>-0.2195247</td></tr><tr><td>9</td><td>0.9</td><td>-0.0405748</td><td>-0.04065697</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi）</td></tr><tr><td>3</td><td>1.3</td><td>0.0654387</td><td>0.0655342</td></tr><tr><td>6</td><td>1.6</td><td>0.0773936</td><td>0.0774595</td></tr><tr><td>9</td><td>1.9</td><td>0.0305465</td><td>0.0305621</td></tr></table>

4. The Linear Finite-Difference Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>1</td><td>0.15707963</td><td>1.05260081</td><td>1.05248562</td></tr><tr><td>2</td><td>0.31415927</td><td>1.07922974</td><td>1.07905555</td></tr><tr><td>3</td><td>0.47123890</td><td>1.07922974</td><td>1.07905555</td></tr><tr><td>4</td><td>0.62831853</td><td>1.05260081</td><td>1.05248562</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>0.15707963</td><td>-0.06141845</td><td>-0.06062540</td></tr><tr><td>2</td><td>0.31415927</td><td>-0.09240491</td><td>-0.09119581</td></tr><tr><td>3</td><td>0.47123890</td><td>-0.09080499</td><td>-0.08961338</td></tr><tr><td>4</td><td>0.62831853</td><td>-0.05825827</td><td>-0.05749950</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>5</td><td>1.25</td><td>0.64328225</td><td>0.64314355</td></tr><tr><td>10</td><td>1.50</td><td>0.68332838</td><td>0.68324289</td></tr><tr><td>15</td><td>1.75</td><td>0.69230217</td><td>0.69226885</td></tr><tr><td>3</td><td>0.6</td><td>-0.70664241</td><td>-0.71228492</td></tr><tr><td>5</td><td>1.0</td><td>-1.63674050</td><td>-1.64085909</td></tr><tr><td>8</td><td>1.6</td><td>-3.52936107</td><td>-3.52075148</td></tr></table>

$^ { * } 5$ . The Linear Finite-Difference Algorithm gives the results in the following tables.

<table><tr><td>i</td><td>xXi</td><td>wi(h = 0.1)</td><td>i</td><td>Mi</td><td>wi(h = 0.05)</td></tr><tr><td>3</td><td>0.3</td><td>0.05572807</td><td>6</td><td>0.3</td><td>0.05132396</td></tr><tr><td>6</td><td>0.6</td><td>0.00310518</td><td>12</td><td>0.6</td><td>0.00263406</td></tr><tr><td>9</td><td>0.9</td><td>0.00016516</td><td>18</td><td>0.9</td><td>0.00013340</td></tr></table>

6. The Linear Finite-Difference Algorithm with the extrapolation in Example 2 gives:

(a)

<table><tr><td>Xi</td><td>Wi(h = 0.1)</td><td>Wi(h = 0.05)</td><td>Wi(h = 0.025)</td><td>Ext1i</td><td>Ext2i</td><td>Ext3i</td></tr><tr><td>0.2</td><td>1.01809654</td><td>1.02113909</td><td>1.02189067</td><td>1.02215327</td><td>1.02214120</td><td>1.02214039</td></tr><tr><td>0.4</td><td>0.64736665</td><td>0.65004438</td><td>0.65070691</td><td>0.65093696</td><td>0.65092775</td><td>0.65092714</td></tr><tr><td>0.6</td><td>0.60014996</td><td>0.60175137</td><td>0.60214815</td><td>0.60228517</td><td>0.60228041</td><td>0.60228009</td></tr><tr><td>0.8</td><td>0.73896130</td><td>0.73961176</td><td>0.73977312</td><td>0.73982858</td><td>0.73982691</td><td>0.73982680</td></tr></table>

(b)

<table><tr><td>xi</td><td>Wi(h = 0.05)</td><td>Wi(h = 0.025)</td><td>Wi(h = 0.0125)</td><td>Ext1i</td><td>Ext2i</td><td>Ext3i</td></tr><tr><td>1.2</td><td>0.07795820</td><td>0.07769625</td><td>0.07763091</td><td>0.07760893</td><td>0.07760913</td><td>0.07760914</td></tr><tr><td>1.4</td><td>0.36654278</td><td>0.36632776</td><td>0.36627411</td><td>0.36625609</td><td>0.36625623</td><td>0.36625624</td></tr><tr><td>1.6</td><td>0.52914512</td><td>0.52901406</td><td>0.52898134</td><td>0.52897037</td><td>0.52897043</td><td>0.52897044</td></tr><tr><td>1.8</td><td>0.62871452</td><td>0.62865682</td><td>0.62864241</td><td>0.62863759</td><td>0.62863761</td><td>0.62863761</td></tr></table>

7. (a) The approximate deflections are shown in the following table.

<table><tr><td>i</td><td>Xi</td><td>W1i</td></tr><tr><td>5</td><td>30</td><td>0.0102808</td></tr><tr><td>10</td><td>60</td><td>0.0144277</td></tr><tr><td>15</td><td>90</td><td>0.0102808</td></tr></table>

(b) Yes, the maximum error on the interval is within 0.2 in.   
(c) Yes, the maximum deflection occurs at $x = 6 0$ . The exact solution is within tolerance, but the approximation is not.

8. The approximate deflection at 1-in. intervals is give in the following table.

<table><tr><td>i Wi</td><td></td></tr><tr><td>Xi</td><td></td></tr><tr><td>10 20</td><td>10.0 0.1098549 20.0 0.1761424</td></tr><tr><td>25</td><td>25.0 0.1849608</td></tr><tr><td>30</td><td>30.0 0.1761424</td></tr><tr><td>40</td><td>40.0 0.1098549</td></tr></table>

$^ { * } 9$ . First we have

$$
\left| { \frac { h } { 2 } } p ( x _ { i } ) \right| \leq { \frac { h L } { 2 } } < 1 ,
$$

so

$$
\Bigg | - 1 - \frac { h } { 2 } p ( x _ { i } ) \Bigg | = 1 + \frac { h } { 2 } p ( x _ { i } ) \quad \mathrm { a n d } \quad \Bigg | - 1 + \frac { h } { 2 } p ( x _ { i } ) \Bigg | = 1 - \frac { h } { 2 } p ( x _ { i } ) .
$$

Therefore,

$$
\left| - 1 - { \frac { h } { 2 } } p ( x _ { i } ) \right| + \left| - 1 + { \frac { h } { 2 } } p ( x _ { i } ) \right| = 2 \leq 2 + h ^ { 2 } q ( x _ { i } ) ,
$$

for $2 \leq i \leq N - 1$ .

Since

$$
\left| - 1 + \frac { h } { 2 } p ( x _ { 1 } ) \right| < 2 \leq 2 + h ^ { 2 } q ( x _ { 1 } ) \quad \mathrm { ~ a n d ~ } \ \left| - 1 - \frac { h } { 2 } p ( x _ { N } ) \right| < 2 \leq 2 + h ^ { 2 } q ( x _ { N } ) ,
$$

Theorem 6.31 implies that the linear system (11.19) has a unique solution.

$^ { * } 1 0$ . Let $q ( x ) \geq w > 0$ on $[ a , b ]$ . Then using the sixth Taylor polynomial gives

$$
{ \frac { y ( x _ { i + 1 } ) - y ( x _ { i - 1 } ) } { 2 h } } = y ^ { \prime } ( x _ { i } ) + { \frac { h ^ { 2 } } { 6 } } y ^ { \prime \prime \prime } ( x _ { i } ) + { \frac { h ^ { 4 } } { 1 2 0 } } y ^ { ( 5 ) } ( x _ { i } ) + O \left( h ^ { 5 } \right)
$$

and

$$
{ \frac { y ( x _ { i + 1 } ) - 2 y ( x _ { i } ) + y ( x _ { i - 1 } ) } { h ^ { 2 } } } = y ^ { \prime \prime } ( x _ { i } ) + { \frac { h ^ { 2 } } { 1 2 } } y ^ { ( 4 ) } ( x _ { i } ) + O \left( h ^ { 4 } \right) .
$$

Thus

$$
\big ( 2 + h ^ { 2 } q ( x _ { i } ) \big ) y ( x _ { i } ) - \bigg ( 1 - \frac { h } { 2 } p ( x _ { i } ) \bigg ) y ( x _ { i + 1 } ) - \bigg ( 1 + \frac { h } { 2 } p ( x _ { i } ) \bigg ) y ( x _ { i - 1 } ) + h ^ { 2 } r ( x _ { i } )
$$

$$
= p ( x _ { i } ) \frac { h ^ { 4 } } { 6 } y ^ { \prime \prime \prime } ( x _ { i } ) - \frac { h ^ { 4 } } { 1 2 } y ^ { ( 4 ) } ( x _ { i } ) + ] O \left( h ^ { 6 } \right) .
$$

Subtracting $h ^ { 2 }$ times Equation (11.18) gives

$$
\begin{array} { l } { { \displaystyle \left( 2 + h ^ { 2 } q ( x _ { i } ) \right) ( y ( x _ { i } ) - w _ { i } ) = \left( 1 - \frac { h } { 2 } p ( x _ { i } ) \right) ( y ( x _ { i + 1 } ) - w _ { i + 1 } ) } } \\ { { \displaystyle \qquad + \left( 1 + \frac { h } { 2 } p ( x _ { i } ) \right) ( y ( x _ { i - 1 } ) - w _ { i - 1 } ) } } \\ { { \displaystyle \qquad + \left[ \frac { p ( x _ { i } ) } { 6 } y ^ { \prime \prime \prime } ( x _ { i } ) - \frac { 1 } { 1 2 } y ^ { ( 4 ) } ( x _ { i } ) \right] h ^ { 4 } + { \cal O } \left( h ^ { 6 } \right) . } } \end{array}
$$

Let $E = \textstyle \operatorname* { m a x } _ { 0 \leq i \leq N + 1 } | y ( x _ { i } ) - w _ { i } |$ . Then since $\begin{array} { r } { \Big | \frac { h } { 2 } p ( x _ { i } ) \Big | < 1 } \end{array}$

$$
\left( 2 + h ^ { 2 } q ( x _ { i } ) \right) \left( y ( x _ { i } ) - w _ { i } \right) \leq 2 E + h ^ { 4 } \biggl | \frac { p ( x _ { i } ) } { 6 } y ^ { \prime \prime \prime } ( x _ { i } ) - \frac { 1 } { 1 2 } y ^ { ( 4 ) } ( x _ { i } ) \biggr | + O \left( h ^ { 6 } \right) .
$$

Let $K _ { 1 } = \operatorname* { m a x } _ { a \leq x \leq b } | y ^ { \prime \prime \prime } ( x ) |$ and $K _ { 2 } = \mathrm { m a x } _ { a \leq x \leq b } \left| y ^ { ( 4 ) } ( x ) \right| .$ If $q ( x _ { i } ) \geq w$ , then

$$
\left( 2 + h ^ { 2 } w \right) E \leq 2 E + h ^ { 4 } \biggl [ \frac { L K _ { 1 } } { 6 } + \frac { K _ { 2 } } { 1 2 } \biggr ] + O \left( h ^ { 6 } \right)
$$

and

$$
E \leq h ^ { 2 } \left[ \frac { 2 L K _ { 1 } + K _ { 2 } } { 1 2 w } \right] + O \left( h ^ { 4 } \right) .
$$

# Exercise Set 11.4, page 696

$^ { * } 1$ . The Nonlinear Finite-Difference method gives the following results.

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>1.5</td><td>0.4067967</td><td>0.4054651</td></tr></table>

2. The Nonlinear Finite-Difference method gives the following results.   

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>-0.75</td><td>0.44458639</td><td>0.44444444</td></tr><tr><td>2</td><td>-0.5</td><td>0.40015723</td><td>0.4</td></tr><tr><td>3</td><td>-0.25</td><td>0.36373152</td><td>0.36363636</td></tr></table>

3. The Nonlinear Finite-Difference Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>2</td><td>1.20000000</td><td>0.18220299</td><td>0.18232156</td></tr><tr><td>4</td><td>1.40000000</td><td>0.33632929</td><td>0.33647224</td></tr><tr><td>6</td><td>1.60000000</td><td>0.46988413</td><td>0.47000363</td></tr><tr><td>8</td><td>1.80000000</td><td>0.58771808</td><td>0.58778666</td></tr></table>

Convergence in 3 iterations.

(b)

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>2</td><td>0.31415927</td><td>1.36244080</td><td>1.36208552</td></tr><tr><td>4</td><td>0.62831853</td><td>1.80138559</td><td>1.79999746</td></tr><tr><td>6</td><td>0.94247780</td><td>2.24819259</td><td>2.24569937</td></tr><tr><td>8</td><td>1.25663706</td><td>2.59083695</td><td>2.58844295</td></tr></table>

Convergence in 3 iterations.

(c)

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y(xi)</td></tr><tr><td>1</td><td>0.83775804</td><td>0.86205907</td><td>0.86205848</td></tr><tr><td>2</td><td>0.89011792</td><td>0.88155964</td><td>0.88155882</td></tr><tr><td>3</td><td>0.94247780</td><td>0.89945447</td><td>0.89945372</td></tr><tr><td>4</td><td>0.99483767</td><td>0.91579005</td><td>0.91578959</td></tr></table>

Convergence in 2 iterations.

<table><tr><td>i</td><td>Xi</td><td>Wi</td><td>y（xi)</td></tr><tr><td>4</td><td>0.62831853</td><td>2.28968807</td><td>2.58778525</td></tr><tr><td>8</td><td>1.25663706</td><td>2.41412603</td><td>2.95105652</td></tr><tr><td>12</td><td>1.88495559</td><td>2.41412603</td><td>2.95105652</td></tr><tr><td>16</td><td>2.51327412</td><td>2.28968807</td><td>2.58778525</td></tr></table>

Convergence in 4 iterations.

4. The Nonlinear Finite-Difference Algorithm gives the results in the following tables.

\*(a)

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>1.3</td><td>0.4347972</td><td>0.4347826</td></tr><tr><td>6</td><td>1.6</td><td>0.3846286</td><td>0.3846154</td></tr><tr><td>9</td><td>1.9</td><td>0.3448316</td><td>0.3448276</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>1.3</td><td>2.0694081</td><td>2.0692308</td></tr><tr><td>6</td><td>1.6</td><td>2.2250937</td><td>2.2250000</td></tr><tr><td>9</td><td>1.9</td><td>2.4263387</td><td>2.4263158</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>W1i</td><td>y(xi)</td></tr><tr><td>3</td><td>2.3</td><td>1.2677078</td><td>1.2676917</td></tr><tr><td>6</td><td>2.6</td><td>1.3401418</td><td>1.3401268</td></tr><tr><td>9</td><td>2.9</td><td>1.4095432</td><td>1.4095383</td></tr><tr><td>5</td><td>1.25</td><td>0.4345979</td><td>0.4358273</td></tr><tr><td>10</td><td>1.50</td><td>1.3662119</td><td>1.3684447</td></tr><tr><td>15</td><td>1.75</td><td>2.9969339</td><td>2.9991909</td></tr></table>

5. (b) For ( $^ *$ 4a) the complete results are:

For (4c) we have:   

<table><tr><td>Xi</td><td>Wi(h = 0.2)</td><td>Wi(h = 0.1)</td><td>Wi(h = 0.05)</td></tr><tr><td>1.00</td><td>0.5000000000</td><td>0.5000000000</td><td>0.5000000000</td></tr><tr><td>1.05</td><td></td><td></td><td>0.4878058215</td></tr><tr><td>1.10</td><td></td><td>0.4761972439</td><td>0.4761921720</td></tr><tr><td>1.15</td><td></td><td></td><td>0.4651185619</td></tr><tr><td>1.20</td><td>0.4545886201</td><td>0.4545563382</td><td>0.4545481813</td></tr><tr><td>1.25</td><td></td><td></td><td>0.4444474908</td></tr><tr><td>1.30</td><td></td><td>0.4347956122</td><td>0.4347858663</td></tr><tr><td>1.35</td><td></td><td></td><td>0.4255352892</td></tr><tr><td>1.40</td><td>0.4167206681</td><td>0.4166802725</td><td>0.4166700749</td></tr><tr><td>1.45</td><td></td><td></td><td>0.4081666349</td></tr><tr><td>1.50</td><td></td><td>0.4000130439</td><td>0.4000032672</td></tr><tr><td>1.55</td><td></td><td></td><td>0.3921599714</td></tr><tr><td>1.60</td><td>0.3846613728</td><td>0.3846269650</td><td>0.3846182851</td></tr><tr><td>1.65</td><td></td><td></td><td>0.3773611389</td></tr><tr><td>1.70</td><td></td><td>0.3703797826</td><td>0.3703727277</td></tr><tr><td>1.75</td><td></td><td></td><td>0.3636383953</td></tr><tr><td>1.80</td><td>0.3571694307</td><td>0.3571495457</td><td>0.3571445322</td></tr><tr><td>1.85</td><td></td><td></td><td>0.3508784839</td></tr><tr><td>1.90</td><td></td><td>0.3448311085</td><td>0.3448284683</td></tr><tr><td>1.95</td><td></td><td></td><td>0.3389835019</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>2.00</td><td>0.3333333333</td><td>0.3333333333</td><td>0.3333333333</td></tr></table>

<table><tr><td>Xi</td><td>Wi(h = 0.2)</td><td>Wi(h = 0.1)</td><td>Wi(h = 0.05)</td><td>EXT1,i</td><td>EXT2,i</td><td>EXT3,i</td></tr><tr><td>1.2</td><td>2.0340273</td><td>2.0335158</td><td>2.0333796</td><td>2.0333453</td><td>2.0333342</td><td>2.0333334</td></tr><tr><td>1.4</td><td>2.1148732</td><td>2.1144386</td><td>2.1143243</td><td>2.1142937</td><td>2.1142863</td><td>2.1142858</td></tr><tr><td>1.6</td><td>2.2253630</td><td>2.2250937</td><td>2.2250236</td><td>2.2250039</td><td>2.2250003</td><td>2.2250000</td></tr><tr><td>1.8</td><td>2.3557284</td><td>2.3556001</td><td>2.3555668</td><td>2.3555573</td><td>2.3555556</td><td>2.3355556</td></tr></table>

6. The approximate deflections using the Nonlinear Finite Difference Algorithm are shown in the following table.

<table><tr><td>i</td><td>Xi</td></tr><tr><td>5</td><td>30 0.01028080</td></tr><tr><td>10</td><td>60 0.01442767</td></tr><tr><td>15</td><td>90 0.01028080</td></tr></table>

The results from Exercise 7 in Section 11.3 are:

<table><tr><td>i</td><td>Ci W1i</td></tr><tr><td>5 30</td><td>0.0102808</td></tr><tr><td>10</td><td>60 0.0144277</td></tr><tr><td>15</td><td>90 0.0102808</td></tr></table>

Since the results are the same we can conclude that adding the nonlinear term to the differential equation makes no difference.

$^ { * } 7$ . The Jacobian matrix $J = \left( a _ { i , j } \right)$ is tridiagonal with entries given in (11.21). So

$$
\begin{array} { r l } & { \quad \alpha _ { 1 , 1 } = 2 + \hbar ^ { 2 } f _ { 9 } \left( x _ { 1 1 } , w _ { 1 1 } , \frac { 1 } { 2 h } ( w _ { 2 } - \alpha ) \right) , } \\ & { \quad \alpha _ { 1 , 2 } = - 1 + \frac { b } { 2 } f _ { 9 } \left( x _ { 1 1 } , w _ { 1 1 } , \frac { 1 } { 2 h } ( w _ { 2 } - \alpha ) \right) , } \\ & { \quad \alpha _ { i , i - 1 } = - 1 - \frac { b } { 2 } f _ { 9 } \left( x _ { i } , w _ { i } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) , \quad \textrm { f o r } 2 \le i \le N - 1 } \\ & { \quad \alpha _ { i , i } = 2 + \hbar ^ { 2 } f _ { 9 } \left( x _ { i } , w _ { i + 1 } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) , \quad \textrm { f o r } 2 \le i \le N - 1 } \\ & { \quad \alpha _ { i , i + 1 } = - 1 + \frac { b } { 2 } f _ { 9 } \left( x _ { i } , w _ { i } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) , \quad \textrm { f o r } 2 \le i \le N - 1 } \\ & { \quad \alpha _ { N , N - 1 } = - 1 - \frac { b } { 2 } f _ { 9 } \left( x _ { N } , w _ { N } , \frac { 1 } { 2 h } ( \delta - w _ { N - 1 } ) \right) , } \\ & { \quad \alpha _ { N , N - 1 } = 2 + \hbar ^ { 2 } f _ { 9 } \left( x _ { N } , w _ { N } , \frac { 1 } { 2 h } ( \delta - w _ { N - 1 } ) \right) . } \end{array}
$$

Thus, $| a _ { i , i } | \geq 2 + h ^ { 2 } \delta$ , for $i = 1 , \ldots , N$ . Since $| f _ { y ^ { \prime } } ( x , y , y ^ { \prime } ) | \leq L$ and $h < 2 / L$ ,

$$
\left| \frac { h } { 2 } f _ { y ^ { \prime } } ( x , y , y ^ { \prime } ) \right| \leq \frac { h L } { 2 } < 1 .
$$

So

$$
\begin{array} { r l } & { \quad | a _ { 1 , 2 } | = \displaystyle { \bigg | - 1 + \frac { h } { 2 } f _ { y ^ { \prime } } \left( x _ { 1 } , w _ { 1 } , \frac { 1 } { 2 h } ( w _ { 2 } - \alpha ) \right) \bigg | < 2 < | a _ { 1 , 1 } | } , } \\ & { \quad | a _ { i , i - 1 } | + | a _ { i , i + 1 } | = - a _ { i , i - 1 } - a _ { i , i + 1 } } \\ & { \qquad = 1 + \displaystyle { \frac { h } { 2 } f _ { y ^ { \prime } } \left( x _ { i } , w _ { i } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) + 1 - \frac { h } { 2 } f _ { y ^ { \prime } } \left( x _ { i } , w _ { i } , \frac { 1 } { 2 h } ( w _ { i + 1 } - w _ { i - 1 } ) \right) } } \\ & { \qquad = 2 \le | a _ { i , i } | , } \end{array}
$$

and

$$
\left| a _ { N , N - 1 } \right| = - \ a _ { N , N - 1 } = 1 + { \frac { h } { 2 } } f _ { y ^ { \prime } } \left( x _ { N } , w _ { N } , { \frac { 1 } { 2 h } } ( \beta - w _ { N - 1 } ) \right) < 2 < | a _ { N , N } | .
$$

By Theorem 6.31, the matrix $J$ is nonsingular.

# Exercise Set 11.5, page 710

\*1. The Piecewise Linear Algorithm gives

$$
\phi ( x ) = - 0 . 0 7 7 1 3 2 7 4 \phi _ { 1 } ( x ) - 0 . 0 7 4 4 2 6 7 8 \phi _ { 2 } ( x ) .
$$

The actual values are

$$
y ( x _ { 1 } ) = - 0 . 0 7 9 8 8 5 4 5 \quad \mathrm { a n d } \quad y ( x _ { 2 } ) = - 0 . 0 7 7 1 2 9 0 3 .
$$

2. The Piecewise Linear Algorithm gives

$$
\phi ( x ) = - 0 . 2 5 5 2 6 2 9 \phi _ { 1 } ( x ) - 0 . 1 6 3 3 5 6 5 \phi _ { 2 } ( x ) .
$$

The actual values are

$$
y ( x _ { 1 } ) = - 0 . 2 4 \quad { \mathrm { a n d } } \quad y ( x _ { 2 } ) = - 0 . 1 6 .
$$

3. The Piecewise Linear Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>xi</td><td>（xi）</td><td>y(xi)</td></tr><tr><td>3</td><td>0.3</td><td>-0.212333</td><td>-0.21</td></tr><tr><td>6</td><td>0.6</td><td>-0.241333</td><td>-0.24</td></tr><tr><td>9</td><td>0.9</td><td>-0.090333</td><td>-0.09</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi)</td><td>y(xi)</td></tr><tr><td>3</td><td>0.3</td><td>0.1815138</td><td>0.1814273</td></tr><tr><td>6</td><td>0.6</td><td>0.1805502</td><td>0.1804753</td></tr><tr><td>9</td><td>0.9</td><td>0.05936468</td><td>0.05934303</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi）</td><td>y(xi）</td></tr><tr><td>5</td><td>0.25</td><td>-0.3585989</td><td>-0.3585641</td></tr><tr><td>10</td><td>0.50</td><td>-0.5348383</td><td>-0.5347803</td></tr><tr><td>15</td><td>0.75</td><td>-0.4510165</td><td>-0.4509614</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi）</td><td>y(xi）</td></tr><tr><td>5</td><td>0.25</td><td>-0.1846134</td><td>-0.1845204</td></tr><tr><td>10</td><td>0.50</td><td>-0.2737099</td><td>-0.2735857</td></tr><tr><td>15</td><td>0.75</td><td>-0.2285169</td><td>-0.2284204</td></tr></table>

4. The Cubic Spline Algorithm gives the results in the following tables. \*(a)

<table><tr><td>i</td><td>Xi</td><td>（xi)</td><td>Yi</td></tr><tr><td>1</td><td>0.25</td><td>-0.0712415</td><td>-0.0712308</td></tr><tr><td>2</td><td>0.5</td><td>-0.0944237</td><td>-0.0944091</td></tr><tr><td>3</td><td>0.75</td><td>-0.0681742</td><td>-0.0681651</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>（xi)</td><td>yi</td></tr><tr><td>1</td><td>0.25</td><td>-0.1875</td><td>-0.1875</td></tr><tr><td>2</td><td>0.5</td><td>-0.25</td><td>-0.25</td></tr><tr><td>3</td><td>0.75</td><td>-0.1875</td><td>-0.1875</td></tr></table>

5. The Cubic Spline Algorithm gives the results in the following tables.

(a)

<table><tr><td>i</td><td>xi</td><td>（xi）</td><td>y(xi）</td></tr><tr><td>3</td><td>0.3</td><td>-0.2100000</td><td>-0.21</td></tr><tr><td>6</td><td>0.6</td><td>-0.2400000</td><td>-0.24</td></tr><tr><td>9</td><td>0.9</td><td>-0.0900000</td><td>-0.09</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi）</td><td>y(xi</td></tr><tr><td>3</td><td>0.3</td><td>0.1814269</td><td>0.1814273</td></tr><tr><td>6</td><td>0.6</td><td>0.1804753</td><td>0.1804754</td></tr><tr><td>9</td><td>0.9</td><td>0.05934321</td><td>0.05934303</td></tr></table>

<table><tr><td>i</td><td>Xi</td><td>（xi）</td><td>y(xi)</td></tr><tr><td>5</td><td>0.25</td><td>-0.3585639</td><td>-0.3585641</td></tr><tr><td>10</td><td>0.50</td><td>-0.5347779</td><td>-0.5347803</td></tr><tr><td>15</td><td>0.75</td><td>-0.4509109</td><td>-0.4509614</td></tr></table>

<table><tr><td>i</td><td>xi</td><td>（xi） y(xi)</td></tr><tr><td>5</td><td>0.25</td><td>-0.1845191 -0.1845204</td></tr><tr><td>10</td><td>0.50</td><td>-0.2735833 -0.2735857</td></tr><tr><td>15</td><td>0.75</td><td>-0.2284186 -0.2284204</td></tr></table>

$^ { * } 6$ . With $z ( x ) = y ( x ) - \beta x - \alpha ( 1 - x )$ , we have

$$
z ( 0 ) = y ( 0 ) - \alpha = \alpha - \alpha = 0 \quad { \mathrm { a n d } } \quad z ( 1 ) = y ( 1 ) - \beta = \beta - \beta = 0 .
$$

Further, $z ^ { \prime } ( x ) = y ^ { \prime } ( x ) - \beta + \alpha$ . Thus

$$
y ( x ) = z ( x ) + \beta x + \alpha ( 1 - x ) \quad { \mathrm { a n d } } \quad y ^ { \prime } ( x ) = z ^ { \prime } ( x ) + \beta - \alpha .
$$

Substituting for $y$ and $y ^ { \prime }$ in the differential equation gives

$$
- \frac { d } { d x } ( p ( x ) z ^ { \prime } + p ( x ) ( \beta - \alpha ) ) + q ( x ) ( z + \beta x + \alpha ( 1 - x ) ) = f ( x ) .
$$

Simplifying gives the differential equation

$$
- \frac { d } { d x } ( p ( x ) z ^ { \prime } ) + q ( x ) z = f ( x ) + ( \beta - \alpha ) p ^ { \prime } ( x ) - [ \beta x + \alpha ( 1 - x ) ] q ( x ) .
$$

7. Exercise 6 and the Piecewise Linear Algorithm give:

<table><tr><td>i</td><td>Xi</td><td>（xi)</td><td>y（(xi）</td></tr><tr><td>3</td><td>0.3</td><td>1.0408182</td><td>1.0408182</td></tr><tr><td>6</td><td>0.6</td><td>1.1065307</td><td>1.1065306</td></tr><tr><td>9</td><td>0.9</td><td>1.3065697</td><td>1.3065697</td></tr></table>

8. The Cubic Spline Algorithm gives the results in the following table.

<table><tr><td>i(x) Xi</td><td></td><td>y(xi)</td></tr><tr><td>0.3</td><td>1.0408183</td><td>1.0408182</td></tr><tr><td>0.5</td><td>1.1065307</td><td>1.1065301</td></tr><tr><td>0.9</td><td>1.3065697</td><td>1.3065697</td></tr></table>

$^ { * } 9$ . A change in variable $w = ( x - a ) / ( b - a )$ gives the boundary value problem

$$
- \frac { d } { d w } ( p ( ( b - a ) w + a ) y ^ { \prime } ) + ( b - a ) ^ { 2 } q ( ( b - a ) w + a ) y = ( b - a ) ^ { 2 } f ( ( b - a ) w + a ) ,
$$

where $0 < w < 1$ , $y ( 0 ) = \alpha$ , and $y ( 1 ) = \beta$ . Then Exercise 6 can be used.

\*10. If $\sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x ) = 0$ , for $0 \leq x \leq 1$ , then for any $j$ , we have $\sum _ { i = 1 } ^ { n } c _ { i } \phi _ { i } ( x _ { j } ) = 0 ,$

But

$$
\phi _ { i } ( x _ { j } ) = { \left\{ \begin{array} { l l } { 0 } & { i \neq j , } \\ { 1 } & { i = j , } \end{array} \right. }
$$

so $c _ { j } \phi _ { j } ( x _ { j } ) = c _ { j } = 0$ . Hence the functions are linearly independent.

11. Suppose $\begin{array} { r } { \phi ( x ) = \sum _ { i = 0 } ^ { n + 1 } c _ { i } \phi _ { i } ( x ) = 0 } \end{array}$ , for all $x$ in $\lfloor 0 , 1 \rfloor$ . At the nodes $x _ { i } , i = 0 , \ldots , n + 1$ , we have

$$
\begin{array} { r l } & { \phi _ { 0 } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 / 4 , } & { \mathrm { i f ~ } i = 1 } \\ { 0 , } & { \mathrm { o t h e r w i s e : } } \end{array} \right. } \\ & { ~ \phi _ { 1 } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f ~ } i = 1 } \\ { 1 / 4 , } & { \mathrm { i f ~ } i = 2 } \\ { 0 , } & { \mathrm { o t h e r w i s e : } } \end{array} \right. } \\ & { ~ \phi _ { n } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f ~ } i = n } \\ { 1 / 4 , } & { \mathrm { i f ~ } i = n } \\ { 0 , } & { \mathrm { o t h e r w i s e : } } \end{array} \right. } \\ & { ~ \phi _ { n + 1 } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 / 4 , } & { \mathrm { i f ~ } i = n } \\ { 0 , } & { \mathrm { o t h e r w i s e : } } \end{array} \right. } \\ & { ~ \phi _ { n + 1 } ( x _ { i } ) = \left\{ \begin{array} { l l } { 1 / 4 , } & { \mathrm { i f ~ } i = n } \\ { 0 , } & { \mathrm { i f ~ } i = n } \end{array} \right. } \end{array}
$$

and for $j = \mathopen { } \mathclose \bgroup  , \aftergroup \egroup 3 , \ldots , n - 1$ ,

$$
\phi _ { j } ( x _ { i } ) = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } i = j } \\ { 1 / 4 , } & { { \mathrm { i f ~ } } i = j - 1 { \mathrm { ~ o r ~ } } i = j + 1 } \\ { 0 , } & { { \mathrm { o t h e r w i s e . } } } \end{array} \right. }
$$

Thus

$$
\begin{array} { l } { \displaystyle 0 = \phi ( { x } _ { 1 } ) = \frac { 1 } { 4 } c _ { 0 } + c _ { 1 } + \frac { 1 } { 4 } c _ { 2 } } \\ { \displaystyle 0 = \phi ( { x } _ { 2 } ) = \frac { 1 } { 4 } c _ { 1 } + c _ { 2 } + \frac { 1 } { 4 } c _ { 3 } } \\ { \displaystyle \phantom { \frac { 1 } { 4 } c _ { 0 } + \phi ( { x } _ { 1 } ) } \vdots \qquad } \\ { \displaystyle 0 = \phi ( { x } _ { n - 1 } ) = \frac { 1 } { 4 } c _ { n - 2 } + c _ { n - 1 } + \frac { 1 } { 4 } c _ { n } } \\ { \displaystyle 0 = \phi ( { x } _ { n } ) = \frac { 1 } { 4 } c _ { n - 1 } + c _ { n } + \frac { 1 } { 4 } c _ { n + 1 } . } \end{array}
$$

Since $\phi ^ { \prime } ( 0 ) = \phi ^ { \prime } ( 1 ) = 0$ , we have

$$
0 = \frac { 3 } { h } c _ { 0 } + \frac { 1 . 5 } { h } c _ { 1 } , \quad \mathrm { s o } \quad 0 = 3 c _ { 0 } + 1 . 5 c _ { 1 }
$$

and

$$
0 = - \frac { 1 . 5 } { h } c _ { n } - \frac { 3 } { h } c _ { n + 1 } , \quad \mathrm { s o } \quad 0 = 1 . 5 c _ { n } + 3 c _ { n + 1 } .
$$

Thus,

$$
\left[ \begin{array} { c c c c c c c c c c c } { 3 } & { 1 . 5 } & { 0 } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { 0 } \\ { 0 . 2 5 } & { 1 } & { 0 . 2 5 } & { \ddots } & & & & & { \vdots } \\ { 0 } & { 0 . 2 5 } & { 1 } & { 0 . 2 5 } & { \ddots } & & & & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & & & { \vdots } \\ { \vdots } & & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & & & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & & & { \ddots } & { 0 . 2 5 } & { 1 } & { 0 . 2 5 } & { 0 } \\ { \vdots } & & & & { \ddots } & { 0 . 2 5 } & { 1 } & { 0 . 2 5 } \\ { \vdots } & & & & { \ddots } & { 0 . 2 5 } & { 1 } & { 0 . 2 5 } \\ { 0 } & { \cdots } & { \cdots } & { \cdots } & { \cdots } & { 0 } & { 1 . 5 } & { 3 } \end{array} \right] \left[ \begin{array} { c } { c _ { 0 } } \\ { c _ { 1 } } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { \vdots } \\ { c _ { n - 1 } } \\ { c _ { n + 1 } } \end{array} \right] = \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { \vdots } \\ { \vdots } \\ { 0 } \\ { 0 } \\ { 0 } \end{array} \right] ,
$$

which can be written as the linear system $A \mathbf { c } \ = \ \mathbf { 0 }$ . The matrix $A$ is strictly diagonally dominant and, hence, nonsingular. So the only solution to the linear system is $\mathbf c = \mathbf 0$ , and $\left\{ \phi _ { 0 } , \phi _ { 1 } , \ldots , \phi _ { n } , \phi _ { n + 1 } \right\}$ is linearly independent.

$^ { \ast } 1 2$ . Let $\mathbf { c } = ( c _ { 1 } , \ldots , c _ { n } ) ^ { t }$ be any vector and let $\begin{array} { r } { \phi ( x ) = \sum _ { j = 1 } ^ { n } c _ { j } \phi _ { j } ( x ) } \end{array}$ . Then

$$
\begin{array} { l } { { \displaystyle c ^ { t } A \mathbf { c } = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } a _ { i j } c _ { i } c _ { j } = \sum _ { i = 1 } ^ { n } \sum _ { j = i - 1 } ^ { i + 1 } a _ { i j } c _ { i } c _ { i } } } \\ { { \displaystyle \ - \sum _ { i = 1 } ^ { n } \left[ \int _ { 0 } ^ { 1 } \left\{ p ( x ) c _ { i } \phi _ { i } ^ { \prime } ( x ) c _ { i - 1 } \phi _ { i - 1 } ^ { \prime } ( x ) + q ( x ) c _ { i } \phi _ { i } ( x ) c _ { i - 1 } \phi _ { i - 1 } ( x ) \right\} d x \right. } } \\ { { \displaystyle \left. \ + \int _ { 0 } ^ { 1 } \left\{ p ( x ) c _ { i } ^ { 2 } [ \phi _ { i } ^ { \prime } ( x ) ] ^ { 2 } + q ( x ) c _ { i } ^ { 2 } [ \phi _ { i } ^ { \prime } ( x ) ] ^ { 2 } \right\} d x } \ ~ } \\ { { \displaystyle \ + \int _ { 0 } ^ { 1 } \left\{ p ( x ) c _ { i } \phi _ { i } ^ { \prime } ( x ) c _ { i + 1 } \phi _ { i + 1 } ^ { \prime } ( x ) + q ( x ) c _ { i } \phi _ { i } ( x ) c _ { i + 1 } \phi _ { i + 1 } ( x ) \right\} d x \right] } } \\ { { \displaystyle \ - \int _ { 0 } ^ { 1 } \left\{ p ( x ) [ \phi ^ { \prime } ( x ) ] ^ { 2 } + q ( x ) [ \phi ( x ) ] ^ { 2 } \right\} d x } . } \end{array}
$$

So $\mathbf { c } ^ { t } A \mathbf { c } \geq 0$ with equality only if $\mathbf c = \mathbf 0$ . Since $A$ is also symmetric, $A$ is positive definite.

$^ \mathrm { * _ { 1 3 } }$ . For $\mathbf { c } = ( c _ { 0 } , c _ { 1 } , \hdots , c _ { n + 1 } ) ^ { t }$ and $\begin{array} { r } { \phi ( x ) = \sum _ { i = 0 } ^ { n + 1 } c _ { i } \phi _ { i } ( x ) } \end{array}$ , we have

$$
\mathbf { c } ^ { t } A \mathbf { c } = \int _ { 0 } ^ { 1 } p ( x ) [ \phi ^ { \prime } ( x ) ] ^ { 2 } + q ( x ) [ \phi ( x ) ] ^ { 2 } d x .
$$

But $p ( x ) > 0$ and $q ( x ) [ \phi ( x ) ] ^ { 2 } \geq 0$ , so $\mathbf { c } ^ { t } A \mathbf { c } \geq 0$ , and it can be $0$ , for $\mathbf x \neq 0$ , only if $\phi ^ { \prime } ( x ) \equiv 0$ on $[ 0 , 1 ]$ . However, $\{ \phi _ { 0 } ^ { \prime } , \phi _ { 1 } ^ { \prime } , . . . , \phi _ { n + 1 } ^ { \prime } \}$ is linearly independent, so $\phi ^ { \prime } ( x ) \neq 0$ on $[ 0 , 1 ]$ and $\mathbf { c } ^ { t } A \mathbf { c } = 0$ if and only if $\mathbf c = \mathbf 0$ .

# Numerical Solutions to Partial Differential Equations

Exercise Set 12.1, page 723

$^ { * } 1$ . The Poisson Equation Finite-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>1</td><td>1</td><td>0.5</td><td>0.5</td><td>0.0</td><td>0</td></tr><tr><td>1</td><td>2</td><td>0.5</td><td>1.0</td><td>0.25</td><td>0.25</td></tr><tr><td>1</td><td>3</td><td>0.5</td><td>1.5</td><td>1.0</td><td>1</td></tr></table>

2. The Poisson Equation Finite-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td><td>u(xi,yi)</td></tr><tr><td>1</td><td>1</td><td>1.33333333</td><td>0.33333333</td><td>0.6348043</td><td>0.6359888</td></tr><tr><td>1</td><td>2</td><td>1.33333333</td><td>0.66666667</td><td>0.7985001</td><td>0.7985077</td></tr><tr><td>2</td><td>1</td><td>1.66666667</td><td>0.33333333</td><td>1.0599924</td><td>1.0687200</td></tr><tr><td>2</td><td>2</td><td>1.66666667</td><td>0.66666667</td><td>1.1698208</td><td>1.1700713</td></tr></table>

3. The Poisson Equation Finite-Difference Algorithm gives the following results.

(a) 30 iterations required:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>2</td><td>2</td><td>0.4</td><td>0.4</td><td>0.1599988</td><td>0.16</td></tr><tr><td>2</td><td>4</td><td>0.4</td><td>0.8</td><td>0.3199988</td><td>0.32</td></tr><tr><td>4</td><td>2</td><td>0.8</td><td>0.4</td><td>0.3199995</td><td>0.32</td></tr><tr><td>4</td><td>4</td><td>0.8</td><td>0.8</td><td>0.6399996</td><td>0.64</td></tr></table>

(b) 29 iterations required:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>2</td><td>1</td><td>1.256637</td><td>0.3141593</td><td>0.2951855</td><td>0.2938926</td></tr><tr><td>2</td><td>3</td><td>1.256637</td><td>0.9424778</td><td>0.1830822</td><td>0.1816356</td></tr><tr><td>4</td><td>1</td><td>2.513274</td><td>0.3141593</td><td>-0.7721948</td><td>-0.7694209</td></tr><tr><td>4</td><td>3</td><td>2.513274</td><td>0.9424778</td><td>-0.4785169</td><td>-0.4755283</td></tr></table>

(c) 126 iterations required:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>4</td><td>3</td><td>0.8</td><td>0.3</td><td>1.2714468</td><td>1.2712492</td></tr><tr><td>4</td><td>7</td><td>0.8</td><td>0.7</td><td>1.7509414</td><td>1.7506725</td></tr><tr><td>8</td><td>3</td><td>1.6</td><td>0.3</td><td>1.6167917</td><td>1.6160744</td></tr><tr><td>8</td><td>7</td><td>1.6</td><td>0.7</td><td>3.0659184</td><td>3.0648542</td></tr></table>

(d) 127 iterations required:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td><td>u(xi,yj)</td></tr><tr><td>2</td><td>2</td><td>1.2</td><td>1.2</td><td>0.5251533</td><td>0.5250861</td></tr><tr><td>4</td><td>4</td><td>1.4</td><td>1.4</td><td>1.3190830</td><td>1.3189712</td></tr><tr><td>6</td><td>6</td><td>1.6</td><td>1.6</td><td>2.4065150</td><td>2.4064186</td></tr><tr><td>8</td><td>8</td><td>1.8</td><td>1.8</td><td>3.8088995</td><td>3.8088576</td></tr></table>

4. The Poisson Equation Finite-Difference Algorithm with extrapolation gives the following results.   

<table><tr><td>xi</td><td>yj</td><td>Wij(h = 0.2)</td><td>Wij(h = 0.1)</td><td>Wij(h = 0.05)</td><td>Ext1i,j</td><td>Ext2i,j</td><td>Ext3i,j</td></tr><tr><td>0.4</td><td>0.4</td><td>0.15999914</td><td>0.15999579</td><td>0.15998414</td><td>0.159994673</td><td>0.15998026</td><td>0.15997930</td></tr><tr><td>0.4</td><td>0.8</td><td>0.31999888</td><td>0.31999384</td><td>0.31997558</td><td>0.319992160</td><td>0.31996949</td><td>0.31996798</td></tr><tr><td>0.8</td><td>0.4</td><td>0.31999952</td><td>0.31999588</td><td>0.31997997</td><td>0.319994667</td><td>0.31997467</td><td>0.31997333</td></tr><tr><td>0.8</td><td>0.8</td><td>0.63999955</td><td>0.63999689</td><td>0.63998633</td><td>0.639996003</td><td>0.63998281</td><td>0.63998193</td></tr></table>

\*5. To incorporate the SOR method, make the following changes to Algorithm 12.1:

$$
\begin{array} { r l r } { S T E P \ 1 } & { \mathrm { S e t ~ } h = ( b - a ) / n ; } \\ & { } & { k = ( d - c ) / m ; } \\ & { } & { \omega = 4 / \left( 2 + \sqrt { 4 - ( \cos \pi / m ) ^ { 2 } - ( \cos \pi / n ) ^ { 2 } } \right) ; } \\ & { } & { \omega _ { 0 } = 1 - w ; } \end{array}
$$

In each of Steps 7, 8, 9, 11, 12, 13, 14, 15, and 16 after

insert

$$
\begin{array} { r l } & { \mathrm { s e t } ~ E = w _ { \alpha , \beta } - z ; } \\ & { ~ \mathrm { i f } ~ ( | E | > \mathrm { N O R M } ) \mathrm { ~ t h e n ~ s e t ~ N O R M } = | E | ; } \\ & { \mathrm { s e t } ~ w _ { \alpha , \beta } = \omega _ { 0 } E + z . } \end{array}
$$

where $\alpha$ and $\beta$ depend on which step is being changed.

6. Using $T O L = 1 0 ^ { - 6 }$ , the results are the same for both methods. The number of iterations required are listed for each method.

(a) SOR 14 iterations, Gauss–Seidel 30 iterations, $\omega = 1 . 2 5 9 6 1 6$   

<table><tr><td colspan="6"></td></tr><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td></tr><tr><td>1</td><td>1</td><td>0.2</td><td>0.2</td><td>0.03999975</td></tr><tr><td>2</td><td>2</td><td>0.4</td><td>0.4</td><td>0.15999994</td></tr><tr><td>3</td><td>3</td><td>0.6</td><td>0.6</td><td>0.35999994</td></tr><tr><td>4</td><td>4</td><td>0.8</td><td>0.8</td><td>0.63999998</td></tr></table>

(b) SOR 14 iterations, Gauss–Seidel 29 iterations, $\omega = 1 . 2 5 9 6 1 6$   

<table><tr><td>i</td><td>j</td><td>Ci</td><td>yj</td><td>Wij</td></tr><tr><td>2</td><td>1</td><td>1.256637</td><td>0.3141593</td><td>0.29518499</td></tr><tr><td>2</td><td>3</td><td>1.256637</td><td>0.9424778</td><td>0.18308118</td></tr><tr><td>4</td><td>1</td><td>2.513274</td><td>0.3141593</td><td>-0.77219505</td></tr><tr><td>4</td><td>3</td><td>2.513274</td><td>0.9424778</td><td>-0.47851735</td></tr></table>

(c) SOR 30 iterations, Gauss–Seidel 126 iterations, $\omega = 1 . 5 2 7 8 6 4$   

<table><tr><td></td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td></tr><tr><td>1</td><td>1</td><td>0.2</td><td>0.1</td><td>1.0202140</td></tr><tr><td>2</td><td>2</td><td>0.4</td><td>0.2</td><td>1.0833400</td></tr><tr><td>3</td><td>3</td><td>0.6</td><td>0.3</td><td>1.1973456</td></tr><tr><td>4</td><td>4</td><td>0.8</td><td>0.4</td><td>1.3773776</td></tr><tr><td>5</td><td>5</td><td>1.0</td><td>0.5</td><td>1.6491565</td></tr><tr><td>6</td><td>6</td><td>1.2</td><td>0.6</td><td>2.0550775</td></tr><tr><td>7</td><td>7</td><td>1.4</td><td>0.7</td><td>2.6653128</td></tr><tr><td>8</td><td>8</td><td>1.6</td><td>0.8</td><td>3.5975766</td></tr><tr><td>9</td><td>9</td><td>1.8</td><td>0.9</td><td>5.0537432</td></tr></table>

(d) SOR 30 iterations, Gauss–Seidel 127 iterations, $\omega = 1 . 5 2 7 8 6 4$   

<table><tr><td></td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td></tr><tr><td>2</td><td>2</td><td>1.2</td><td>1.2</td><td>0.52515626</td></tr><tr><td>4</td><td>4</td><td>1.4</td><td>1.4</td><td>1.3190907</td></tr><tr><td>6</td><td>6</td><td>1.6</td><td>1.6</td><td>2.4065227</td></tr><tr><td>8</td><td>8</td><td>1.8</td><td>1.8</td><td>3.8089025</td></tr></table>

7. The approximate potential at some typical points gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wi,j</td></tr><tr><td>1</td><td>4</td><td>0.1</td><td>0.4</td><td>88</td></tr><tr><td>2</td><td>1</td><td>0.2</td><td>0.1</td><td>66</td></tr><tr><td>4</td><td></td><td>0.4</td><td>0.2</td><td>66</td></tr></table>

8. Approximations for the temperature are given in the following table. Convergence was obtained with 293 iterations using the tolerance $1 0 ^ { - 6 }$ .

<table><tr><td>i</td><td>j</td><td>Xi</td><td>yj</td><td>Wij</td></tr><tr><td>5</td><td>9</td><td>2.0</td><td>3.0</td><td>5.959624</td></tr><tr><td>8</td><td>3</td><td>3.2</td><td>1.0</td><td>7.916551</td></tr><tr><td>10</td><td>9</td><td>4.0</td><td>3.0</td><td>4.679948</td></tr><tr><td>12</td><td>12</td><td>4.8</td><td>4.0</td><td>2.060342</td></tr></table>

# Exercise Set 12.2, page 736

1. The Heat Equation Backward-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi，tj)</td></tr><tr><td>1</td><td>1</td><td>0.5</td><td>0.05</td><td>0.632952</td><td>0.652037</td></tr><tr><td>2</td><td>1</td><td>1.0</td><td>0.05</td><td>0.895129</td><td>0.883937</td></tr><tr><td>3</td><td>1</td><td>1.5</td><td>0.05</td><td>0.632952</td><td>0.625037</td></tr><tr><td>1</td><td>2</td><td>0.5</td><td>0.1</td><td>0.566574</td><td>0.552493</td></tr><tr><td>2</td><td>2</td><td>1.0</td><td>0.1</td><td>0.801256</td><td>0.781344</td></tr><tr><td>3</td><td>2</td><td>1.5</td><td>0.1</td><td>0.566574</td><td>0.552493</td></tr></table>

\*2. The Heat Equation Backward-Difference Algorithm gives the following results.   

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>1</td><td>1</td><td>1/3</td><td>0.05</td><td>1.59728</td><td>1.53102</td></tr><tr><td>2</td><td>1</td><td>2/3</td><td>0.05</td><td>-1.59728</td><td>-1.53102</td></tr><tr><td>1</td><td>2</td><td>1/3</td><td>0.1</td><td>1.47300</td><td>1.35333</td></tr><tr><td>2</td><td>2</td><td>2/3</td><td>0.1</td><td>-1.47300</td><td>-1.35333</td></tr></table>

3. The Crank-Nicolson Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>1</td><td>1</td><td>0.5</td><td>0.05</td><td>0.628848</td><td>0.652037</td></tr><tr><td>2</td><td>1</td><td>1.0</td><td>0.05</td><td>0.889326</td><td>0.883937</td></tr><tr><td>3</td><td>1</td><td>1.5</td><td>0.05</td><td>0.628848</td><td>0.625037</td></tr><tr><td>1</td><td>2</td><td>0.5</td><td>0.1</td><td>0.559251</td><td>0.552493</td></tr><tr><td>2</td><td>2</td><td>1.0</td><td>0.1</td><td>0.790901</td><td>0.781344</td></tr><tr><td>3</td><td>2</td><td>1.5</td><td>0.1</td><td>0.559252</td><td>0.552493</td></tr></table>

\*4. The Crank-Nicolson Algorithm gives the following results.

For $h = 0 . 4$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>1</td><td>1</td><td>1/3</td><td>0.05</td><td>1.59728</td><td>1.53102</td></tr><tr><td>2</td><td>1</td><td>2/3</td><td>0.05</td><td>-1.59728</td><td>-1.53102</td></tr><tr><td>1</td><td>2</td><td>1/3</td><td>0.1</td><td>1.47300</td><td>1.35333</td></tr><tr><td>2</td><td>2</td><td>2/3</td><td>0.1</td><td>-1.47300</td><td>-1.35333</td></tr></table>

5. The Forward-Difference Algorithm gives the following results.

(a) For $h = 0 . 4$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>5</td><td>0.8</td><td>0.5</td><td>3.035630</td><td>0</td></tr><tr><td>3</td><td>5</td><td>1.2</td><td>0.5</td><td>-3.035630</td><td>0</td></tr><tr><td>4</td><td>5</td><td>1.6</td><td>0.5</td><td>1.876122</td><td>0</td></tr></table>

For $h = 0 . 4$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>10</td><td>0.8</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td>3</td><td>10</td><td>1.2</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td>4</td><td>10</td><td>1.6</td><td>0.5</td><td>0</td><td>0</td></tr></table>

(b) For $h = \frac { \pi } { 1 0 }$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>J</td><td>xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.94247780</td><td>0.5</td><td>0.4864823</td><td>0.4906936</td></tr><tr><td>6</td><td>10</td><td>1.88495559</td><td>0.5</td><td>0.5728943</td><td>0.5768449</td></tr><tr><td>9</td><td>10</td><td>2.82743339</td><td>0.5</td><td>0.1858197</td><td>0.1874283</td></tr></table>

6. The Forward-Difference Algorithm gives the following results.

(a) For $h = 0 . 2$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi，tj)</td></tr><tr><td>4</td><td>10</td><td>0.8</td><td>0.4</td><td>1.166149</td><td>1.169362</td></tr><tr><td>8</td><td>10</td><td>1.6</td><td>0.4</td><td>1.252413</td><td>1.254556</td></tr><tr><td>12</td><td>10</td><td>2.4</td><td>0.4</td><td>0.4681813</td><td>0.4665473</td></tr><tr><td>16</td><td>10</td><td>3.2</td><td>0.4</td><td>-0.1027637</td><td>-0.1056622</td></tr></table>

(b) For $h = 0 . 1$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.3</td><td>0.4</td><td>0.5397009</td><td>0.5423003</td></tr><tr><td>6</td><td>10</td><td>0.6</td><td>0.4</td><td>0.6344565</td><td>0.6375122</td></tr><tr><td>9</td><td>10</td><td>0.9</td><td>0.4</td><td>0.2061474</td><td>0.2071403</td></tr></table>

7. The Backward-Difference Algorithm gives:

(a) For $h = 0 . 4$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>5</td><td>0.8</td><td>0.5</td><td>-0.00258</td><td>0</td></tr><tr><td>3</td><td>5</td><td>1.2</td><td>0.5</td><td>0.00258</td><td>0</td></tr><tr><td>4</td><td>5</td><td>1.6</td><td>0.5</td><td>-0.00159</td><td>0</td></tr></table>

For $h = 0 . 4$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>10</td><td>0.8</td><td>0.5</td><td>-4.93 × 10-4</td><td>0</td></tr><tr><td>3</td><td>10</td><td>1.2</td><td>0.5</td><td>4.93 ×10-4</td><td>0</td></tr><tr><td>4</td><td>10</td><td>1.6</td><td>0.5</td><td>-3.05 ×10-4</td><td>0</td></tr></table>

(b) For $\begin{array} { r } { h = \frac { \pi } { 1 0 } } \end{array}$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.94247780</td><td>0.5</td><td>0.4986092</td><td>0.4906936</td></tr><tr><td>6</td><td>10</td><td>1.88495559</td><td>0.5</td><td>0.5861503</td><td>0.5768449</td></tr><tr><td>9</td><td>10</td><td>2.82743339</td><td>0.5</td><td>0.1904518</td><td>0.1874283</td></tr></table>

8. (a) For $h = 0 . 2$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>4</td><td>10</td><td>0.8</td><td>0.4</td><td>1.176752</td><td>1.169362</td></tr><tr><td>8</td><td>10</td><td>1.6</td><td>0.4</td><td>1.259495</td><td>1.254556</td></tr><tr><td>12</td><td>10</td><td>2.4</td><td>0.4</td><td>0.4628134</td><td>0.4665473</td></tr><tr><td>16</td><td>10</td><td>3.2</td><td>0.4</td><td>-0.1123064</td><td>-0.1056622</td></tr></table>

(b) For $h = 0 . 1$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.3</td><td>0.4</td><td>0.5482691</td><td>0.5423003</td></tr><tr><td>6</td><td>10</td><td>0.6</td><td>0.4</td><td>0.6445290</td><td>0.6375123</td></tr><tr><td>9</td><td>10</td><td>0.9</td><td>0.4</td><td>0.2094202</td><td>0.2071403</td></tr></table>

9. The Crank-Nicolson Algorithm gives the following results.

(a) For $h = 0 . 4$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>5</td><td>0.8</td><td>0.5</td><td>8.2 ×10-7</td><td>0</td></tr><tr><td>3</td><td>5</td><td>1.2</td><td>0.5</td><td>-8.2 × 10-7</td><td>0</td></tr><tr><td>4</td><td>5</td><td>1.6</td><td>0.5</td><td>5.1 ×10-7</td><td>0</td></tr></table>

For $h = 0 . 4$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>10</td><td>0.8</td><td>0.5</td><td>-2.6 × 10-6</td><td>0</td></tr><tr><td>3</td><td>10</td><td>1.2</td><td>0.5</td><td>2.6×10-6</td><td>0</td></tr><tr><td>4</td><td>10</td><td>1.6</td><td>0.5</td><td>-1.6 × 10-6</td><td>0</td></tr></table>

(b) For $\begin{array} { r } { h = \frac { \pi } { 1 0 } } \end{array}$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.94247780</td><td>0.5</td><td>0.4926589</td><td>0.4906936</td></tr><tr><td>6</td><td>10</td><td>1.88495559</td><td>0.5</td><td>0.5791553</td><td>0.5768449</td></tr><tr><td>9</td><td>10</td><td>2.82743339</td><td>0.5</td><td>0.1881790</td><td>0.1874283</td></tr></table>

10. The Crank-Nicolson Algorithm gives the following results.

(a) For $h = 0 . 2$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>4</td><td>10</td><td>0.8</td><td>0.4</td><td>1.171532</td><td>1.169362</td></tr><tr><td>8</td><td>10</td><td>1.6</td><td>0.4</td><td>1.256005</td><td>1.254556</td></tr><tr><td>12</td><td>10</td><td>2.4</td><td>0.4</td><td>0.4654499</td><td>0.4665473</td></tr><tr><td>16</td><td>10</td><td>3.2</td><td>0.4</td><td>-0.1076139</td><td>-0.1056622</td></tr></table>

(b) For $h = 0 . 1$ and $k = 0 . 0 4$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wi,j</td><td>u(xi,tj)</td></tr><tr><td>3</td><td>10</td><td>0.3</td><td>0.4</td><td>0.5440532</td><td>0.5423003</td></tr><tr><td>6</td><td>10</td><td>0.6</td><td>0.4</td><td>0.6395728</td><td>0.6375122</td></tr><tr><td>9</td><td>10</td><td>0.9</td><td>0.4</td><td>0.2078098</td><td>0.2071403</td></tr></table>

11. Using Richardson’s method gives:

(a) Using $h = 0 . 4$ and $k = 0 . 1$ leads to meaningless results. Using $h = 0 . 4$ and $k = 0 . 0 5$ again gives meaningless answers. Letting $h = 0 . 4$ and $k = 0 . 0 0 5$ produces the following:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>1</td><td>100</td><td>0.4</td><td>0.5</td><td>-165.405</td></tr><tr><td>2</td><td>100</td><td>0.8</td><td>0.5</td><td>267.613</td></tr><tr><td>3</td><td>100</td><td>1.2</td><td>0.5</td><td>-267.613</td></tr><tr><td>4</td><td>100</td><td>1.6</td><td>0.5</td><td>165.405</td></tr></table>

(b)

The instability of Richardson’s method gives very poor results.   

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>w(xij)</td></tr><tr><td>3</td><td>10</td><td>0.9424778</td><td>0.5</td><td>0.46783396</td></tr><tr><td>6</td><td>10</td><td>1.8849556</td><td>0.5</td><td>0.54995267</td></tr><tr><td>9</td><td>10</td><td>2.8274334</td><td>0.5</td><td>0.17871220</td></tr></table>

12. Using Richardson’s method gives:

(a) For $h = 0 . 2$ and $k = 0 . 0 4$

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>w(xi)</td></tr><tr><td>4</td><td>10</td><td>0.8</td><td>0.4</td><td>1.1406275</td></tr><tr><td>8</td><td>10</td><td>1.6</td><td>0.4</td><td>1.2315952</td></tr><tr><td>12</td><td>10</td><td>2.4</td><td>0.4</td><td>0.47267557</td></tr><tr><td>16</td><td>10</td><td>3.2</td><td>0.4</td><td>-0.08733023</td></tr></table>

(b) For $h = 0 . 1$ and $k = 0 . 0 4$

<table><tr><td>i</td><td>j</td><td>xi</td><td>tj</td><td>w(xij)</td></tr><tr><td>2</td><td>10</td><td>0.2</td><td>0.4</td><td>0.37945980</td></tr><tr><td>4</td><td>10</td><td>0.4</td><td>0.4</td><td>0.61397885</td></tr><tr><td>6</td><td>10</td><td>0.6</td><td>0.4</td><td>0.61397885</td></tr><tr><td>8</td><td>10</td><td>0.8</td><td>0.4</td><td>0.37945980</td></tr></table>

$^ *$ 13. We have

$$
a _ { 1 1 } v _ { 1 } ^ { ( i ) } + a _ { 1 2 } v _ { 2 } ^ { ( i ) } = ( 1 - 2 \lambda ) \sin \frac { i \pi } { m } + \lambda \sin \frac { 2 \pi i } { m }
$$

and

$$
\begin{array} { l } { { \mu _ { i } v _ { 1 } ^ { ( i ) } = \left[ 1 - 4 \lambda \left( \sin { \frac { i \pi } { 2 m } } \right) ^ { 2 } \right] \sin { \frac { i \pi } { m } } = \left[ 1 - 4 \lambda \left( \sin { \frac { i \pi } { 2 m } } \right) ^ { 2 } \right] \left( 2 \sin { \frac { i \pi } { 2 m } } \cos { \frac { i \pi } { 2 m } } \right) } } \\ { { \phantom { \mu _ { i } v _ { 1 } ^ { ( i ) } = } = 2 \sin { \frac { i \pi } { 2 m } } \cos { \frac { i \pi } { 2 m } } - 8 \lambda \left( \sin { \frac { i \pi } { 2 m } } \right) ^ { 3 } \cos { \frac { i \pi } { 2 m } } . } } \end{array}
$$

However,

$$
\begin{array} { c } { { \displaystyle \left( 1 - 2 \lambda \right) \sin \displaystyle \frac { i \pi } { m } + \lambda \sin \displaystyle \frac { 2 \pi i } { m } = 2 ( 1 - 2 \lambda ) \sin \displaystyle \frac { i \pi } { 2 m } \cos \displaystyle \frac { i \pi } { 2 m } + 2 \lambda \sin \displaystyle \frac { i \pi } { m } \cos \displaystyle \frac { i \pi } { m } } } \\ { { = 2 ( 1 - 2 \lambda ) \sin \displaystyle \frac { i \pi } { 2 m } \cos \displaystyle \frac { i \pi } { 2 m } } } \\ { { + 2 \lambda \displaystyle \left[ 2 \sin \displaystyle \frac { i \pi } { 2 m } \cos \displaystyle \frac { i \pi } { 2 m } \right] \left[ 1 - 2 \left( \sin \displaystyle \frac { i \pi } { 2 m } \right) ^ { 2 } \right] } } \\ { { = 2 \sin \displaystyle \frac { i \pi } { 2 m } \cos \displaystyle \frac { i \pi } { 2 m } - 8 \lambda \cos \displaystyle \frac { i \pi } { 2 m } \left[ \sin \displaystyle \frac { i \pi } { 2 m } \right] ^ { 3 } . } } \end{array}
$$

Thus

$$
a _ { 1 1 } v _ { 1 } ^ { ( i ) } + a _ { 1 2 } v _ { 2 } ^ { ( i ) } = \mu _ { i } v _ { 1 } ^ { ( i ) } .
$$

Further,

$$
\begin{array} { r l } & { a _ { j , j - 1 } v _ { j - 1 } ^ { ( i ) } + a _ { j , j } v _ { j } ^ { ( i ) } + a _ { j , j + 1 } v _ { j + 1 } ^ { ( i ) } = \lambda \sin \frac { i ( j - 1 ) \pi } { m } + ( 1 - 2 \lambda ) \sin \frac { i j \pi } { m } + \lambda \sin \frac { i ( j + 1 ) \pi } { m } } \\ & { \phantom { a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a } } \\ & { \phantom { a a a a a a a a a a a a a a a a a a a a a a a a a a a } = \lambda \biggl ( \sin \frac { i j \pi } { m } \cos \frac { i \pi } { m } - \sin \frac { i \pi } { m } \cos \frac { i j \pi } { m } \biggr ) + ( 1 - 2 \lambda ) \sin \frac { i j \pi } { m } } \\ & { \phantom { a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a } } \\ & { \phantom { a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a } + \lambda \biggl ( \sin \frac { i j \pi } { m } - 2 \lambda \sin \frac { i j \pi } { m } + 2 \lambda \biggr ) } \\ & { = \sin \frac { i j \pi } { m } - 2 \lambda \sin \frac { i j \pi } { m } + 2 \lambda \sin \frac { i \pi } { m } \biggr ( \cos \frac { i \pi } { m } - 1 \biggr ) } \end{array}
$$

and

$$
\begin{array} { l } { { \mu _ { i } v _ { j } ^ { ( i ) } = \left[ 1 - 4 \lambda \left( \sin { \displaystyle \frac { i \pi } { 2 m } } \right) ^ { 2 } \right] \sin \displaystyle \frac { i j \pi } { m } = \left[ 1 - 4 \lambda \left( \displaystyle \frac { 1 } { 2 } - \displaystyle \frac { 1 } { 2 } \cos { \displaystyle \frac { i \pi } { m } } \right) \right] \sin \displaystyle \frac { i j \pi } { m } } } \\ { { = \left[ 1 + 2 \lambda \left( \cos { \displaystyle \frac { i \pi } { m } } - 1 \right) \right] \sin \displaystyle \frac { i j \pi } { m } , } } \end{array}
$$

so

$$
a _ { j , j - 1 } v _ { j - 1 } ^ { ( i ) } + a _ { j , j } v _ { j } ^ { ( i ) } + a _ { j , j + 1 } v _ { j } ^ { ( i ) } = \mu _ { i } v _ { j } ^ { ( i ) } .
$$

Similarly,

$$
a _ { m - 2 , m - 1 } v _ { m - 2 } ^ { ( i ) } + a _ { m - 1 , m - 1 } v _ { m - 1 } ^ { ( i ) } = \mu _ { i } v _ { m - 1 } ^ { ( i ) } ,
$$

so $A \mathbf { v } ^ { ( i ) } = \mu _ { i } \mathbf { v } ^ { ( i ) }$ .

$^ { * } 1 4$ . We have

$$
\begin{array} { l } { { a _ { 1 1 } v _ { 1 } ^ { ( i ) } + a _ { 1 2 } v _ { 2 } ^ { ( i ) } = \left( 1 + 2 \lambda \right) \sin { \displaystyle \frac { i \pi } { m } } - \lambda \sin { \displaystyle \frac { 2 \pi i } { m } } = \left( 1 + 2 \lambda \right) \sin { \displaystyle \frac { i \pi } { m } } - 2 \lambda \sin { \displaystyle \frac { i \pi } { m } } \cos { \displaystyle \frac { i \pi } { m } } } } \\ { { = \sin { \displaystyle \frac { i \pi } { m } } \left[ 1 + 2 \lambda \left( 1 - \cos { \displaystyle \frac { i \pi } { m } } \right) \right] } } \end{array}
$$

and

$$
\mu _ { i } v _ { 1 } ^ { ( i ) } = \left[ 1 + 4 \lambda \left( \sin \frac { i \pi } { 2 m } \right) ^ { 2 } \right] \sin \frac { i \pi } { m } = \left[ 1 + 2 \lambda \left( 1 - \cos \frac { i \pi } { m } \right) \right] \sin \frac { i \pi } { m } = a _ { 1 1 } v _ { 1 } ^ { ( i ) } + a _ { 1 2 } v _ { 2 } ^ { ( i ) } .
$$

In general,

$$
\begin{array} { l } { { a _ { j , j - 1 } v _ { j - 1 } ^ { ( i ) } + a _ { j , j } v _ { j } ^ { ( i ) } + a _ { j , j + 1 } v _ { j + 1 } ^ { ( i ) } = - \lambda \sin \displaystyle \frac { i ( j - 1 ) \pi } { m } + ( 1 + 2 \lambda ) \sin \displaystyle \frac { i j \pi } { m } - \lambda \sin \displaystyle \frac { i ( j + 1 ) \pi } { m } } } \\ { { \displaystyle \qquad = - \lambda \left( \sin \displaystyle \frac { i j \pi } { m } \cos \displaystyle \frac { i \pi } { m } - \sin \displaystyle \frac { i \pi } { m } \cos \displaystyle \frac { i j \pi } { m } \right) + ( 1 + 2 \lambda ) \sin \displaystyle \frac { i j \pi } { m } } } \\ { { \displaystyle \qquad - \lambda \left( \sin \displaystyle \frac { i j \pi } { m } \cos \displaystyle \frac { i \pi } { m } + \sin \displaystyle \frac { i \pi } { m } \cos \displaystyle \frac { i j \pi } { m } \right) } } \\ { { \displaystyle \qquad = - 2 \lambda \sin \displaystyle \frac { i j \pi } { m } \cos \displaystyle \frac { i \pi } { m } + ( 1 + 2 \lambda ) \sin \displaystyle \frac { i j \pi } { m } } } \\ { { \displaystyle \qquad = \left[ 1 + 2 \lambda \left( 1 - \cos \displaystyle \frac { i \pi } { m } \right) \right] \sin \displaystyle \frac { i j \pi } { m } = \mu _ { i } v _ { j } ^ { ( i ) } . } } \end{array}
$$

Similarly,

$$
a _ { m - 2 , m - 1 } v _ { m - 2 } ^ { ( i ) } + a _ { m - 1 , m - 1 } v _ { m - 1 } ^ { ( i ) } = \mu _ { i } v _ { m - 1 } ^ { ( i ) } .
$$

Thus, $A \mathbf { v } ^ { ( i ) } = \mu _ { i } \mathbf { v } ^ { ( i ) }$ . Since $A$ is symmetric with positive eigenvalues, $A$ is positive definite. Further,

$$
\sum _ { j = 1 , j \neq i } ^ { n } \left| a _ { i j } \right| = 2 \lambda < 1 + 2 \lambda = | a _ { i i } | , \quad { \mathrm { f o r } } 1 \leq i \leq n ,
$$

so $A$ is diagonally dominant.

$^ \mathrm { * _ { 1 5 } }$ . To modify Algorithm 12.2, change the following:

Step 7 Set

$$
\begin{array} { r l } & { t = j k ; } \\ & { w _ { 0 } = \phi ( t ) ; } \\ & { z _ { 1 } = ( w _ { 1 } + \lambda w _ { 0 } ) / l _ { 1 } . } \\ & { w _ { m } = \psi ( t ) . } \end{array}
$$

Step $^ { 8 }$ For $i = 2 , \ldots , m - 2$ set

$$
z _ { i } = ( w _ { i } + \lambda z _ { i - 1 } ) / l _ { i } ;
$$

Set

$$
z _ { m - 1 } = ( w _ { m - 1 } + \lambda w _ { m } + \lambda z _ { m - 2 } ) / l _ { m - 1 } .
$$

Step 11 OUTPUT $\mathbf { \rho } ( t )$ ;

To modify Algorithm 12.3, change the following:

Step 1 Set

Step 7 Set

$$
\begin{array} { r l } & { t = j k ; } \\ & { z _ { 1 } = \left[ ( 1 - \lambda ) w _ { 1 } + \frac { \lambda } { 2 } w _ { 2 } + \frac { \lambda } { 2 } \displaybreaks _ { 0 } + \frac { \lambda } { 2 } \phi ( t ) \right] / l _ { 1 } ; } \\ & { w _ { 0 } = \phi ( t ) . } \end{array}
$$

Step $^ { 8 }$ For $i = 2 , \ldots , m - 2$ set

$$
z _ { i } = \left[ ( 1 - \lambda ) w _ { i } + { \textstyle \frac { \lambda } { 2 } } ( w _ { i + 1 } + w _ { i - 1 } + z _ { i - 1 } ) \right] / l _ { i } ;
$$

Set

$$
\begin{array} { r l } & { z _ { m - 1 } = \left[ ( 1 - \lambda ) w _ { m - 1 } + \frac { \lambda } { 2 } ( w _ { m } + w _ { m - 2 } + z _ { m - 2 } + \psi ( t ) ) \right] / l _ { m - 1 } ; } \\ & { w _ { m } = \psi ( t ) . } \end{array}
$$

Step 11 OUTPUT $( t )$ ;

16. The modifications of Algorithms 12.2 and 12.3 give the following results:

(a) For modified Algorithm 12.2 we have

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>3</td><td>25</td><td>0.3</td><td>0.25</td><td>0.2883460</td></tr><tr><td>5</td><td>25</td><td>0.5</td><td>0.25</td><td>0.3468410</td></tr><tr><td>8</td><td>25</td><td>0.8</td><td>0.25</td><td>0.2169217</td></tr></table>

(b) For modified Algorithm 12.3 we have

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>3</td><td>25</td><td>0.3</td><td>0.25</td><td>0.2798737</td></tr><tr><td>5</td><td>25</td><td>0.5</td><td>0.25</td><td>0.3363686</td></tr><tr><td>8</td><td>25</td><td>0.8</td><td>0.25</td><td>0.2107662</td></tr></table>

17. To modify Algorithm 12.2, change the following:

STEP 7 Set

$$
\begin{array} { r l } & { t = j k ; } \\ & { w _ { 0 } = \phi ( t ) ; } \\ & { z _ { 1 } = ( w _ { 1 } + \lambda w _ { 0 } ) / l _ { 1 } . } \\ & { w _ { m } = \psi ( t ) . } \end{array}
$$

STEP $\boldsymbol { \vartheta }$ For $i = 2 , \ldots , m - 2$ set

$$
z _ { i } = ( w _ { i } + \lambda z _ { i - 1 } ) / l _ { i } ;
$$

$$
z _ { m - 1 } = ( w _ { m - 1 } + \lambda w _ { m } + \lambda z _ { m - 2 } ) / l _ { m - 1 } .
$$

STEP 11 OUTPUT $\mathbf { \rho } ( t )$

To modify Algorithm 12.3, change the following:

STEP 1 Set

STEP 7 Set

$$
\begin{array} { r l } & { h = l / m ; } \\ & { k = T / N ; } \\ & { \lambda = \alpha ^ { 2 } k / h ^ { 2 } ; } \\ & { w _ { m } = \psi ( 0 ) ; } \\ & { w _ { 0 } = \phi ( 0 ) . } \\ & { t = j k ; } \\ & { z _ { 1 } = \left[ ( 1 - \lambda ) w _ { 1 } + \frac { \lambda } { 2 } w _ { 2 } + \frac { \lambda } { 2 } _ { 0 } + \frac { \lambda } { 2 } \phi ( t ) \right] / l _ { 1 } ; } \\ & { w _ { 0 } = \phi ( t ) . } \end{array}
$$

STEP $\boldsymbol { \vartheta }$ For $i = 2 , \ldots , m - 2$ set

$$
z _ { i } = \left[ ( 1 - \lambda ) w _ { i } + { \textstyle \frac { \lambda } { 2 } } ( w _ { i + 1 } + w _ { i - 1 } + z _ { i - 1 } ) \right] / l _ { i } ;
$$

Set

$$
\begin{array} { r l } & { z _ { m - 1 } = \left[ ( 1 - \lambda ) w _ { m - 1 } + \frac { \lambda } { 2 } ( w _ { m } + w _ { m - 2 } + z _ { m - 2 } + \psi ( t ) ) \right] / l _ { m - 1 } ; } \\ & { w _ { m } = \psi ( t ) . } \end{array}
$$

STEP 11 OUTPUT $( t )$ ;

18. The approximations to the temperature distributions using Algorithms 12.2 and 12.3 are given in the following table:

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij(Algorithm 12.3)</td><td>Wij (Algorithm 12.2)</td></tr><tr><td>3</td><td>10</td><td>0.3</td><td>0.225</td><td>1.223279</td><td>1.207730</td></tr><tr><td>6</td><td>10</td><td>0.75</td><td>0.225</td><td>1.862358</td><td>1.836564</td></tr><tr><td>10</td><td>10</td><td>1.35</td><td>0.225</td><td>0.701087</td><td>0.692834</td></tr></table>

19. (a) The approximate temperature at some typical points is given in the table.

<table><tr><td>i</td><td>j</td><td>ri</td><td>tj</td><td>Wi,j</td></tr><tr><td>1</td><td>20</td><td>0.6</td><td>10</td><td>137.6753</td></tr><tr><td>2</td><td>20</td><td>0.7</td><td>10</td><td>245.9678</td></tr><tr><td>3</td><td>20</td><td>0.8</td><td>10</td><td>340.2862</td></tr><tr><td>4</td><td>20</td><td>0.9</td><td>10</td><td>424.1537</td></tr></table>

(b) The strain is approximately $I = 1 2 4 2 . 5 3 7$ .

# Exercise Set 12.3, page 744

$^ { * } 1$ . The Wave Equation Finite-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>4</td><td>0.25</td><td>1.0</td><td>-0.7071068</td><td>-0.7071068</td></tr><tr><td>3</td><td>4</td><td>0.50</td><td>1.0</td><td>-1.0000000</td><td>-1.0000000</td></tr><tr><td>4</td><td>4</td><td>0.75</td><td>1.0</td><td>-0.7071068</td><td>-0.7071068</td></tr></table>

2. The Wave Equation Finite-Difference Algorithm gives the following results.   

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,ti)</td></tr><tr><td>2</td><td>4</td><td>0.125</td><td>0.5</td><td>0.48428862</td><td>0.47942554</td></tr><tr><td>3</td><td>4</td><td>0.250</td><td>0.5</td><td>0.00000000</td><td>0</td></tr><tr><td>4</td><td>4</td><td>0.375</td><td>0.5</td><td>-0.48428862</td><td>0.47942554</td></tr></table>

3. The Wave Equation Finite-Difference Algorithm with $h = \frac { \pi } { 1 0 }$ and $k = 0 . 0 5$ gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>10</td><td>π/5</td><td>0.5</td><td>0.5163933</td><td>0.5158301</td></tr><tr><td>5</td><td>10</td><td>π/2</td><td>0.5</td><td>0.8785407</td><td>0.8775826</td></tr><tr><td>8</td><td>10</td><td>4π/5</td><td>0.5</td><td>0.5163933</td><td>0.5158301</td></tr></table>

The Wave Equation Finite-Difference Algorithm with $h = \frac { \pi } { 2 0 }$ and $k = 0 . 1$ gives the following results.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>4</td><td>5</td><td>π/5</td><td>0.5</td><td>0.5159163</td></tr><tr><td>10</td><td>5</td><td>π/2</td><td>0.5</td><td>0.8777292</td></tr><tr><td>16</td><td>5</td><td>4π/5</td><td>0.5</td><td>0.5159163</td></tr></table>

The Wave Equation Finite-Difference Algorithm with $h = \frac { \pi } { 2 0 }$ and $k = 0 . 0 5$ gives the following results.

<table><tr><td>i</td><td>j</td><td>Ci</td><td>tj</td><td>Wij</td></tr><tr><td>4</td><td>10</td><td>π/5</td><td>0.5</td><td>0.5159602</td></tr><tr><td>10</td><td>10</td><td>π/2</td><td>0.5</td><td>0.8778039</td></tr><tr><td>16</td><td>10</td><td>4π/5</td><td>0.5</td><td>0.5159602</td></tr></table>

4. The Wave Equation Finite-Difference Algorithm gives the following results.   

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>2</td><td>10</td><td>0.62831853</td><td>0.5</td><td>0.5233857</td></tr><tr><td>5</td><td>10</td><td>1.57079633</td><td>0.5</td><td>0.8904370</td></tr><tr><td>8</td><td>10</td><td>2.51327412</td><td>0.5</td><td>0.5233857</td></tr></table>

For $h = 0 . 0 5$ and $k = 0 . 1$ :

<table><tr><td>i</td><td>j</td><td>xi</td><td>tj</td><td>Wij</td></tr><tr><td>4</td><td>5</td><td>0.62831853</td><td>0.5</td><td>0.53000146</td></tr><tr><td>10</td><td>5</td><td>1.57079633</td><td>0.5</td><td>0.90169234</td></tr><tr><td>16</td><td>5</td><td>2.51327412</td><td>0.5</td><td>0.53000146</td></tr></table>

For $h = 0 . 0 5$ and $k = 0 . 0 5$ :

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Wij</td></tr><tr><td>4</td><td>10</td><td>0.62831853</td><td>0.5</td><td>0.52299419</td></tr><tr><td>10</td><td>10</td><td>1.57079633</td><td>0.5</td><td>0.88977086</td></tr><tr><td>16</td><td>10</td><td>2.51327412</td><td>0.5</td><td>0.52299419</td></tr></table>

5. The Wave Equation Finite-Difference Algorithm gives the following results.

<table><tr><td>i</td><td>j</td><td>xi</td><td>tj</td><td>Wij</td><td>u(xi,tj)</td></tr><tr><td>2</td><td>3</td><td>0.2</td><td>0.3</td><td>0.6729902</td><td>0.61061587</td></tr><tr><td>5</td><td>3</td><td>0.5</td><td>0.3</td><td>0</td><td>0</td></tr><tr><td>8</td><td>3</td><td>0.8</td><td>0.3</td><td>-0.6729902</td><td>-0.61061587</td></tr></table>

6. Algorithm 12.4 gives the following results:

<table><tr><td>i</td><td>j</td><td>xi</td><td>tj</td><td>Wij</td></tr><tr><td>2</td><td>5</td><td>0.2</td><td>0.5</td><td>-1</td></tr><tr><td>5</td><td>5</td><td>0.5</td><td>0.5</td><td>0</td></tr><tr><td>8</td><td>5</td><td>0.8</td><td>0.5</td><td>1</td></tr></table>

7. (a) The air pressure for the open pipe is $p ( 0 . 5 , 0 . 5 ) \approx 0 . 9$ and $p ( 0 . 5 , 1 . 0 ) \approx 2 . 7$ . (b) The air pressure for the closed pipe is $p ( 0 . 5 , 0 . 5 ) \approx 0 . 9$ and $p ( 0 . 5 , 1 . 0 ) \approx 0 . 9 1 8 7 9 2 7$

\*8. Approximate voltages and currents are given in the following table.

<table><tr><td>i</td><td>j</td><td>Xi</td><td>tj</td><td>Voltage</td><td>Current</td></tr><tr><td>5</td><td>2</td><td>50</td><td>0.2</td><td>77.769</td><td>3.88845</td></tr><tr><td>12</td><td>2</td><td>120</td><td>0.2</td><td>104.60</td><td>-1.69931</td></tr><tr><td>18</td><td>2</td><td>180</td><td>0.2</td><td>33.986</td><td>-5.22995</td></tr><tr><td>5</td><td>5</td><td>50</td><td>0.5</td><td>77.702</td><td>3.88510</td></tr><tr><td>12</td><td>5</td><td>120</td><td>0.5</td><td>104.51</td><td>-1.69785</td></tr><tr><td>18</td><td>5</td><td>180</td><td>0.5</td><td>33.957</td><td>-5.22453</td></tr></table>

# Exercise Set 12.4, page 758

$^ * 1$ . With $E _ { 1 } = ( 0 . 2 5 , 0 . 7 5 )$ , $E _ { 2 } = ( 0 , 1 )$ , $E _ { 3 } = ( 0 . 5 , 0 . 5 )$ , and $E _ { 4 } = ( 0 , 0 . 5 )$ , the basis functions are

$$
\begin{array} { r c l } { \phi _ { 1 } ( x , y ) } & { = } & { \left\{ \begin{array} { l l } { 4 x } & { \mathrm { o n ~ } T _ { 1 } } \\ { - 2 + 4 y } & { \mathrm { o n ~ } T _ { 2 } , } \end{array} \right. } \\ { \phi _ { 2 } ( x , y ) } & { = } & { \left\{ \begin{array} { l l } { - 1 - 2 x + 2 y } & { \mathrm { o n ~ } T _ { 1 } } \\ { 0 } & { \mathrm { o n ~ } T _ { 2 } , } \end{array} \right. } \\ { \phi _ { 3 } ( x , y ) } & { = } & { \left\{ \begin{array} { l l } { 0 } & { \mathrm { o n ~ } T _ { 1 } } \\ { 1 + 2 x - 2 y } & { \mathrm { o n ~ } T _ { 2 } , } \end{array} \right. } \\ { \phi _ { 4 } ( x , y ) } & { = } & { \left\{ \begin{array} { l l } { 2 - 2 x - 2 y } & { \mathrm { o n ~ } T _ { 1 } } \\ { 2 - 2 x - 2 y } & { \mathrm { o n ~ } T _ { 2 } , } \end{array} \right. } \end{array}
$$

and $\gamma _ { 1 } = 0 . 3 2 3 8 2 5$ , $\gamma _ { 2 } = 0$ , $\gamma _ { 3 } = 1 . 0 0 0 0$ , and $\gamma _ { 4 } = 0$ .

2. With $E _ { 1 } ~ = ~ ( 0 . 2 5 , 0 . 7 5 )$ , $E _ { 2 } ~ = ~ ( 0 , 1 )$ , $E _ { 3 } ~ = ~ ( 0 . 5 , 0 . 5 )$ , $E _ { 4 } ~ = ~ ( 0 , 0 . 5 )$ , $E _ { 5 } ~ = ~ ( 0 , 0 . 7 5 )$ , and $E _ { 6 } = ( 0 . 2 5 , 0 . 5 )$ , the following results are obtained:

<table><tr><td>i</td><td>j</td><td>蜀</td><td>福</td><td>S</td><td></td><td>node</td></tr><tr><td>1</td><td>1</td><td>0</td><td>4</td><td></td><td>0</td><td>1</td></tr><tr><td>1</td><td>2</td><td>一 -3</td><td></td><td>0</td><td>4</td><td>2</td></tr><tr><td>1</td><td>3</td><td>4</td><td></td><td>-4</td><td>-4</td><td>5</td></tr><tr><td>2</td><td>1</td><td>-2</td><td></td><td>0</td><td>4</td><td>1</td></tr><tr><td>2</td><td>2</td><td>-1</td><td></td><td>4</td><td>0</td><td>3</td></tr><tr><td>2</td><td>3</td><td>4</td><td>-4</td><td></td><td>-4</td><td>6</td></tr><tr><td>3</td><td>1</td><td>0</td><td>4</td><td></td><td>0</td><td>1</td></tr><tr><td>3</td><td>2</td><td>3</td><td>0</td><td></td><td>-4</td><td>4</td></tr><tr><td>3</td><td>3</td><td>一 -2</td><td>-4</td><td></td><td>4</td><td>5</td></tr><tr><td>4</td><td>1</td><td>一 -2</td><td></td><td>0</td><td>4</td><td>1</td></tr><tr><td>4</td><td>2</td><td>1</td><td></td><td></td><td>0</td><td>4</td></tr><tr><td>4</td><td>3</td><td>2</td><td></td><td>4</td><td>-4</td><td>6</td></tr></table>

So $\gamma _ { 1 } = 0 . 3 2 3 8 2 5 5$ , $\gamma _ { 2 } = 0$ , $\gamma _ { 3 } = 1 . 0$ , $\gamma _ { 4 } = 0$ , $\gamma _ { 5 } = 0$ , and $\gamma _ { 6 } = 0 . 5$ .

3. The Finite-Element Algorithm with $K = 8 , N = 8 , M = 3 2 , n = 9 , m = 2 5$ , and $N L = 0$ gives the following results, where the labeling is as shown in the diagram.

![](images/cfea5d3e7412aa6ae2d2e015ab75c164394bf683fe8f4a29552d3046bc76b073.jpg)

With the labeling shown in the figure:

$\gamma _ { 1 } = 0 . 5 1 1 0 2 3$ , $\gamma _ { 2 } = 0 . 7 2 0 4 7 6$ , $\gamma _ { 3 } = 0 . 5 0 7 8 9 9$ , $\gamma _ { 4 } = 0 . 7 2 0 4 7 6$ ,   
$\gamma _ { 5 } = 1 . 0 1 8 8 5$ , $\gamma _ { 6 } = 0 . 7 2 0 4 7 6$ , $\gamma _ { 7 } = 0 . 5 0 7 8 9 6$ , $\gamma _ { 8 } = 0 . 7 2 0 4 7 6$ ,   
$\gamma _ { 9 } = 0 . 5 1 1 0 2 3 \mathrm { a n d } \gamma _ { i } = 0 , \mathrm { f o r } 1 0 \leq i \leq 2 5 $   
$u ( 0 . 1 2 5 , 0 . 1 2 5 ) \approx 0 . 6 1 4 1 8 7$ , $u ( 0 . 1 2 5 , 0 . 2 5 ) \approx 0 . 6 9 0 3 4 3 , u ( 0 . 2 5 , 0 . 1 2 5 ) \approx 0 . 6 9 0 3 4 3$ , and $u ( 0 . 2 5 , 0 . 2 5 ) \approx$   
0.720476

4. The Finite-Element Algorithm with $K = 8$ , $N = 2 2$ , $M = 3 2$ , $n = 2 5$ , $m = 2 5$ , and $N L = 1 6$ gives the results shown below, where the labeling is as shown in the figure for Exercise 3:

$\gamma _ { 1 } = - 0 . 4 8 9 6 9 5$ , $\gamma _ { 2 } = 0 . 0 1 6 3 2 5 0$ , $\gamma _ { 3 } = 0 . 5 2 4 2 4 3$ , $\gamma _ { 4 } = 0 . 0 1 6 3 2 5 0$ ,   
$\gamma _ { 5 } = 0 . 0 0 8 6 8 5 1 8$ , $\gamma _ { 6 } = 0 . 0 1 6 3 2 5 0$ , $\gamma _ { 7 } = 0 . 5 2 4 2 4 3$ , $\gamma _ { 8 } = 0 . 0 1 6 3 2 5 0$ ,   
$\gamma _ { 9 } = - 0 . 4 8 9 6 9 5$ , $\gamma _ { 1 0 } = - 1 . 0 6 9 1 3$ , $\gamma _ { 1 1 } = - 0 . 6 8 4 3 0 8$ , $\gamma _ { 1 2 } = 0 . 0 5 8 1 5 8 3$ ,   
$\gamma _ { 1 3 } = 0 . 7 5 2 8 7 1$ , $\gamma _ { 1 4 } = 0 . 9 6 \dot { 2 } 8 0 1$ , $\gamma _ { 1 5 } = - 0 . 6 8 4 3 0 8$ , $\gamma _ { 1 6 } = 0 . 7 5 2 8 7 1$ ,   
$\gamma _ { 1 7 } = 0 . 0 5 8 1 5 8 3$ , $\gamma _ { 1 8 } = 0 . 0 5 8 1 5 8 3$ , $\gamma _ { 1 9 } = 0 . 7 5 2 8 7 1$ , $\gamma _ { 2 0 } = - 0 . 6 8 4 3 0 8$ ,   
$\gamma _ { 2 1 } = 0 . 9 6 2 8 0 1$ , $\gamma _ { 2 2 } = 0 . 7 5 2 8 7 1$ , $\gamma _ { 2 3 } = 0 . 0 5 8 1 5 8 3$ , $\gamma _ { 2 4 } = - 0 . 6 8 4 3 0 8$ ,   
and $\gamma _ { 2 5 } = - 1 . 0 6 9 1 3$ .   
$u ( 0 . 1 2 5 , 0 . 1 2 5 ) \approx 0 . 2 7 0 2 8 4$ , $u ( 0 . 1 2 5 , 0 . 2 5 ) \approx - 0 . 2 3 8 5 9 5$ , $u ( 0 . 2 5 , 0 . 1 2 5 ) \approx - 0 . 2 3 8 5 9 5$ , and $u ( 0 . 2 5 , 0 . 2 5 ) \approx 0 . 0 1 6 3 2 5 0$

$^ { * } 5$ . The Finite-Element Algorithm with $K = 0 , N = 1 2 , M = 3 2 , n = 2 0 , m = 2 7$ , and $N L = 1 4$ gives the following results, where the labeling is as shown in the diagram.

![](images/c86ee0a0da42a53813869b66754c05b870f97d11c64d3ec45f22b472f0fc8061.jpg)

$u ( 1 , 0 ) \approx 2 2 . 9 2 8 2 4$ , $u ( 4 , 0 ) \approx 2 2 . 8 4 6 6 3$ , and $u \left( { \frac { 5 } { 2 } } , { \frac { \sqrt { 3 } } { 2 } } \right) \approx 1 8 . 8 5 8 9 5$ .
