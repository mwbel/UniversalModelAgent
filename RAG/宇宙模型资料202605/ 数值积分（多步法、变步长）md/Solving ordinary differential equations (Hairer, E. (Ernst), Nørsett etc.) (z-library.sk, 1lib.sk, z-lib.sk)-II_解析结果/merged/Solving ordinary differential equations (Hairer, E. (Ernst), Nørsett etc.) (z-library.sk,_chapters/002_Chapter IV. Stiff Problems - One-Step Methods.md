# Chapter IV. Stiff Problems - One-Step Methods

IV.1 Examples of Stiff Equations ... 2

Chemical Reaction Systems .... 3   
Electrical Circuits 4   
Diffusion 6   
A “Stiff" Beam 8   
High Oscillations 11   
Exercises ， 11

# IV.2Stability Analysis for Explicit RK Methods ... 15

Stability Analysis for Euler's Method. 15   
Explicit Runge-Kutta Methods 16   
Extrapolation Methods 18   
Analysis of the Examples of IV.1 18   
Automatic Stiffness Detection 21   
Step-Control Stability 24   
A PI Step Size Control 28   
Stabilized Explicit Runge-Kutta Methods 31   
Exercises 37

# IV.3 Stability Function of Implicit RK-Methods ... 40

The Stability Function 40   
$A$ -Stability   
$L$ -Stability and $A ( \alpha )$ -Stability 44   
Numerical Results 46   
Stability Functions of Order $\geq s$ 47   
Padé Approximations to the Exponential Function 48   
Exercises 49

IV.4 Order Stars.... 51

Introduction 51   
Order and Stability for Rational Approximations 56   
Stability of Padé Approximations 58   
Comparing Stability Domains. 58   
Rational Approximations with Real Poles 61   
The Real-Pole Sandwich... 62   
Multiple Real-Pole Approximations 67   
Exercises 70

# IV.5 Construction of Implicit Runge-Kutta Methods .... 71

Gauss Methods 71   
Radau IA and Radau IIA Methods 72   
Lobatto IIIA, IIB and IIIC Methods 75   
The W -Transformation 77   
Construction of Implicit Runge-Kutta Methods . 83   
Stability Function 84   
Positive Functions 86   
Exercises ... 89

# IV.6Diagonally Implicit RK Methods .. 91

Order Conditions 91   
Stiffly Accurate SDIRK Methods 92   
The Stability Function .. 96   
Multiple Real-Pole Approximations with $R ( \infty ) { = } 0$ 98   
Choice of Method 99   
Exercises.. 100

IV.7 Rosenbrock-Type Methods... 102

Derivation of the Method 102   
Order Conditions... 104   
The Stability Function 108   
Construction of Methods of Order 4 108   
Higher Order Methods 111   
Implementation of Rosenbrock-Type Methods 111   
The“Hump” 113   
Methods with Inexact Jacobian (W -Methods) 114   
Exercises 117

# IV.8 Implementation of Implicit Runge-Kutta Methods ... 118

Reformulation of the Nonlinear System 118   
Simplified Newton Iterations 119   
The Linear System 121   
Step Size Selection 123   
Implicit Differential Equations 127   
An SDIRK-Code 128   
SIRK-Methods 128   
Exercises 130

IV.9 Extrapolation Methods ... 131

Extrapolation of Symmetric Methods 131   
Smoothing... 133   
The Linearly Implicit Mid-Point Rule 134   
Implicit and Linearly Implicit Euler Method 138   
Implementation 139   
Exercises.. 142

IV.10 Numerical Experiments ... 143

The Codes Used 143   
Twelve Test Problems 144   
Results and Discussion 152   
Partitioning and Projection Methods 160   
Exercises .. 165

# IV.11 Contractivity for Linear Problems .... 167

Euclidean Norms (Theorem of von Neumann) 168   
Error Growth Function for Linear Problems 169   
Small Nonlinear Perturbations 172   
Contractivity in $\| \cdot \| _ { \infty }$ and $\Vert \cdot \Vert _ { 1 }$ 175   
Study of the Threshold Factor 176   
Absolutely Monotonic Functions 178   
Exercises 179

# [V.12 B-Stability and Contractivity.... 180

One-Sided Lipschitz Condition 180   
$B$ -Stability and Algebraic Stability 181   
Some Algebraically Stable IRK Methods 183   
$A N$ -Stability ... 184   
Reducible Runge-Kutta Methods 187   
The Equivalence Theorem for $S$ -Irreducible Methods 188   
Error Growth Function 193   
Computation of $\varphi _ { B } ( x )$ 195   
Exercises ... 199

# [V.13 Positive Quadrature Formulas and B-Stable RK-Methods .. 201

Quadrature Formulas and Related Continued Fractions.. 201   
Number of Positive Weights... 203   
Characterization of Positive Quadrature Formulas 205   
Necessary Conditions for Algebraic Stability 206   
Characterization of Algebraically Stable Methods 209   
The “Equivalence”of $A$ - and $B$ -Stability 211   
Exercises 213

# [V.14 Existence and Uniqueness of IRK Solutions ... 215

Existence.. 215   
A Counterexample 217   
Influence of Perturbations and Uniqueness 218   
Computation of $\alpha _ { 0 } ( A ^ { - 1 } )$ 220   
Methods with Singular $A$ 222   
Lobatto IIC Methods 223   
Exercises. 223

IV.15 B-Convergence .. 225

The Order Reduction Phenomenon 225   
The Local Error ... 228   
Error Propagation.. 229   
$B$ -Convergence for Variable Step Sizes 230   
$B$ -Convergence Implies Algebraic Stability 232   
The Trapezoidal Rule.. 234   
Order Reduction for Rosenbrock Methods 236   
Exercises 237
