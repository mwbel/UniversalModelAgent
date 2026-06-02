# Chapter II. Runge-Kutta and Extrapolation Methods

I1.1. The First Runge-Kutta Methods 130   
General formulation of Runge-Kutta methods 132   
Discussion of methods of order 4 133

Contents ix

"Optimal" formulas 137   
Numerical example 139   
Exercises 140

I.2. Order Conditions for RK Methods 142

The derivatives of the true solution 144   
Conditions for order 3 144   
Trees and elementary differentials 144   
The Taylor expansion of the true solution 146   
Faa di Bruno's formula 148   
The derivatives of the numerical solution 150   
The order conditions 153   
Exercises 154

# [I.3. Error Estimation and Convergence for RK Methods 156

Rigorous error bounds 156   
The principal error term 158   
Estimation of the global error 159   
Exercises 163

# II.4. Practical Error Estimation and Step Size Selection 165

Richardson extrapolation 165   
Automatic step size control 166   
Embedded RK formulas 167   
The formula of Dormand and Prince 171   
Numerical study of the step-control mechanism 172   
Numerical comparison of 4th-order methods 174   
Exercises.... 174

I1.5. Further Questions of Practical Computation 176

Dense output 176   
Continuous embedded formulas 179   
Implicit output 180   
Discontinuous equations 180   
Starting step-size 182   
Numerical computation of derivatives with respect to initial values   
and parameters 183   
Exercises 184

# I1.6. Explicit RK-Methods of Higher Order 185

The Butcher barriers 6 stage, 5th order processes 8 # n 185 186   
7 stage, 6th order processes 188   
Further Butcher barriers 189   
A 10-th order formula 189   
Embedded formulas of high order 193   
A numerical example 196   
Exercises 196

II.7. Implicit Runge-Kutta Methods 199

Introduction .·· . 199   
Existence of numerical solution 201   
The methods of Kuntzmann and Butcher of order 2s 203   
IRK methods based on Lobatto quadrature 204   
IRK as collocation methods 206   
Exercises 209

I1.8. Asymptotic Expansion of the Global Error 211

The local error 211   
The global error 211   
Examples 213   
Variable h 213   
Negative h 214   
Properties of the adjoint method 215   
Symmetric methods 216   
Exercises 217

I1.9. Extrapolation Methods 219

Definition of the method 219   
The Aitken-Neville algorithm 221   
Rational extrapolation 221   
A numerical example 222   
Extrapolation with symmetric methods 223   
The Gragg or GBS method 224   
The smoothing step 225   
Numerical algorithm and example 226   
Asymptotic expansion for odd indices 226   
Existence of explicit RK methods of arbitrary order 228   
Order and step size control 228   
Numerical study of the combined step size and order control 231   
Exercises 232

II.10. Numerical Comparisons 236

Numerical resuits 238   
A discontinuous ex ample 239   
Conclusion 241

II.11. Composition of B-Series 242

Composition of RK methods 242   
B-series 243   
Order conditions for RK methods 247   
Butcher's "effective order" 247   
Exercises 248

I1.12. Higher Derivative Methods 250

Collocation methods 251   
Obreschkoff methods 253   
Fehlberg methods 254   
General theory of order conditions 256   
Exercises 258

# I1.13. Numerical Methods for Second Order Differential Equations.... 260

=

Thederieveof theexact soluton 262   
The derivatives of the numerical solution 265   
The order conditions 267   
On the construction of Nystrom methods 268   
Global convergence 270   
Implementation of Nystrom methods 271   
An extrapolation method for $y ^ { \prime \prime } { = } f \left( x \ , y \right)$ 271   
Numerical comparisons 273   
Higher order systems 274   
Exercises 275   
I1.14. P-Series for Partitioned Ordinary Differential Equations 276   
Derivatives of the exact solution, P-trees 277   
P-series 280   
RK-methods violating (1.9) 282   
Fehlberg methods 283   
Nystrom methods 283   
Exercises.. 285   
II.15. Delay Differential Equations 286   
Existence 286   
Constant step size methods for constant delay 288   
Variable step size methods. 289   
Characteristic values of exponential solutions 290   
Stability....... 291   
An example from population dynamics 292   
Infectious disease modellng 294   
An example from enzyme kinetics 295   
A mathematical model in immunology 297   
Integro-differential equations 299   
Exercises 300
