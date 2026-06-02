Chapter 17, which discusses ordinary differential equations, has some even more complicated examples that combine inheritance and templating. We defer further discussion to there.

# CITED REFERENCES AND FURTHER READING:

Stroustrup, B. 1997, The $C { + } { + }$ Programming Language, 3rd ed. (Reading, MA: Addison-Wesley).[1] Lippman, S.B., Lajoie, J., and Moo, B.E. 2005, $C { + } { + }$ Primer, 4th ed. (Boston: Addison-Wesley).[2] Keogh, J., and Giannini, M. 2004, OOP Demystified (Emeryville, CA: McGraw-Hill/Osborne).[3] Cline, M., Lomow, G., and Girou, M. 1999, $C { + } { + }$ FAQs, 2nd ed. (Boston: Addison-Wesley).[4]

# 1.4 Vector and Matrix Objects

The $\mathrm { C } { + + }$ Standard Library [1] includes a perfectly good vector<> template class. About the only criticism that one can make of it is that it is so feature-rich that some compiler vendors neglect to squeeze the last little bit of performance out of its most elementary operations, for example returning an element by its subscript. That performance is extremely important in scientific applications; its occasional absence in $\mathrm { C } { + } { + }$ compilers is a main reason that many scientists still (as we write) program in C, or even in Fortran!

Also included in the $\mathrm { C } { + + }$ Standard Library is the class valarray<>. At one time, this was supposed to be a vector-like class that was optimized for numerical computation, including some features associated with matrices and multidimensional arrays. However, as reported by one participant,

The valarray classes were not designed very well. In fact, nobody tried to determine whether the final specification worked. This happened because nobody felt “responsible” for these classes. The people who introduced valarrays to the $\mathrm { C } { + + }$ standard library left the committee a long time before the standard was finished. [1]

The result of this history is that $\mathrm { C } { + } { + }$ , at least now, has a good (but not always reliably optimized) class for vectors and no dependable class at all for matrices or higher-dimensional arrays. What to do? We will adopt a strategy that emphasizes flexibility and assumes only a minimal set of properties for vectors and matrices. We will then provide our own, basic, classes for vectors and matrices. For most compilers, these are at least as efficient as vector $\vartriangle { \mathsf { { C } } } \ v { \mathbf { \{ \Lambda } } $ and other vector and matrix classes in common use. But if, for you, they’re not, then it is easy to change to a different set of classes, as we will explain.

# 1.4.1 Typedefs

Flexibility is achieved by having several layers of typedef type-indirection, resolved at compile time so that there is no run-time performance penalty. The first level of type-indirection, not just for vectors and matrices but for virtually all variables, is that we use user-defined type names instead of $\mathrm { C } { + } { + }$ fundamental types. These are defined in $\mathtt { n r 3 . h }$ . If you ever encounter a compiler with peculiar builtin types, these definitions are the “hook” for making any necessary changes. The complete list of such definitions is

<table><tr><td>NR Type</td><td>Usual Definition</td><td>Intent</td></tr><tr><td>Char</td><td>char</td><td rowspan="6">8-bit signed integer 8-bit unsigned integer 32-bit signed integer</td></tr><tr><td>Uchar</td><td>unsigned char</td></tr><tr><td>Int int</td><td></td></tr><tr><td>Uint unsigned int</td><td>32-bit unsigned integer</td></tr><tr><td>Llong</td><td>long long int 64-bit signed integer</td></tr><tr><td>Ullong</td><td>unsigned long long int 64-bit unsigned integer</td></tr><tr><td>Doub</td><td>double</td><td>64-bit floating point</td></tr><tr><td>Ldoub</td><td>long double</td><td>[reserved for future use]</td></tr><tr><td>Complex</td><td>complex&lt;double&gt;</td><td>2 × 64-bit floating complex</td></tr><tr><td>Bool</td><td>bool</td><td>true or false</td></tr></table>

An example of when you might need to change the typedefs in nr3.h is if your compiler’s int is not 32 bits, or if it doesn’t recognize the type long long int.

You might need to substitute vendor-specific types like (in the case of Microsoft) __int32 and $\_ { - } \mathtt { i n t } 6 4$ .

The second level of type-indirection returns us to the discussion of vectors and matrices. The vector and matrix types that appear in Numerical Recipes source code are as follows. Vectors: VecInt, VecUint, VecChar, VecUchar, VecCharp, VecLlong, VecUllong, VecDoub, VecDoubp, VecComplex, and VecBool. Matrices: MatInt, MatUint, MatChar, MatUchar, MatLlong, MatUllong, MatDoub, MatComplex, and MatBool. These should all be understandable, semantically, as vectors and matrices whose elements are the corresponding user-defined types, above. Those ending in a “p” have elements that are pointers, e.g., VecCharp is a vector of pointers to char, that is, char\*. If you are wondering why the above list is not combinatorially complete, it is because we don’t happen to use all possible combinations of Vec, Mat, fundamental type, and pointer in this book. You can add further analogous types as you need them.

Wait, there’s more! For every vector and matrix type above, we also define types with the same names plus one of the suffixes “_I”, “_O”, and “_IO”, for example VecDoub_IO. We use these suffixed types for specifying argument types in function definitions. The meaning, respectively, is that the argument is “input”, “output”, or “both input and output”. The $_ - \ I$ types are automatically defined to be const. We discuss this further in $\ S 1 . 5 . 2$ under the topic of const correctness.

It may seem capricious for us to define such a long list of types when a much smaller number of templated types would do. The rationale is flexibility: You have a hook into redefining each and every one of the types individually, according to your needs for program efficiency, local coding standards, const-correctness, or whatever. In fact, in $\mathtt { n r 3 . h }$ , all these types are typedef’d to one vector and one matrix class, along the following lines:

typedef NRvector<Int> VecInt, VecInt_O, VecInt_IO;   
typedef const NRvector<Int> VecInt_I;   
typedef NRvector<Doub> VecDoub, VecDoub_O, VecDoub_IO;   
typedef const NRvector<Doub> VecDoub_I;   
typedef NRmatrix<Int> MatInt, MatInt_O, MatInt_IO;   
typedef const NRmatrix<Int> MatInt_I;   
typedef NRmatrix<Doub> MatDoub, MatDoub_O, MatDoub_IO;   
typedef const NRmatrix<Doub> MatDoub_I;

So (flexibility, again) you can change the definition of one particular type, like VecDoub, or else you can change the implementation of all vectors by changing the definition of NRvector<>. Or, you can just leave things the way we have them in nr3.h. That ought to work fine in $9 9 . 9 \%$ of all applications.

# 1.4.2 Required Methods for Vector and Matrix Classes

The important thing about the vector and matrix classes is not what names they are typedef’d to, but what methods are assumed for them (and are provided in the NRvector and NRmatrix template classes). For vectors, the assumed methods are a subset of those in the $\mathrm { C } { + } { + }$ Standard Library vector $\cdot >$ class. If $\mathtt { v }$ is a vector of type NRvector ${ \mathrm { - } } \mathrm { T } >$ , then we assume the methods:

$\mathtt { v } ( )$ Constructor, zero-length vector.   
v(Int n) Constructor, vector of length n.   
v(Int n, const T &a) Constructor, initialize all elements to the value a.   
v(Int n, const T \*a) Constructor, initialize elements to values in a C-style array, a[0], a[1], : : :   
v(const NRvector &rhs) Copy constructor.   
v.size() Returns number of elements in v.   
v.resize(Int newn) Resizes v to size newn. We do not assume that contents are preserved.   
v.assign(Int newn, const T &a) Resize v to size newn, and set all elements to the value a.   
v[Int i] Element of v by subscript, either an l-value and an r-value.   
$\qquad \mathtt { v } =$ rhs Assignment operator. Resizes v if necessary and makes it a copy of the vector rhs.   
typedef T value_type; Makes T available externally (useful in templated functions or classes).

As we will discuss later in more detail, you can use any vector class you like with Numerical Recipes, as long as it provides the above basic functionality. For example, a brute force way to use the $\mathrm { C } { + } { + }$ Standard Library vector<> class instead of NRvector is by the preprocessor directive

# #define NRvector vector

(In fact, there is a compiler switch, _USESTDVECTOR_, in the file nr3.h that will do just this.)

The methods for matrices are closely analogous. If vv is a matrix of type NRmatrix<T>, then we assume the methods:

vv() Constructor, zero-length vector.   
vv(Int n, Int m) Constructor, ${ \mathfrak { n } } \times { \mathfrak { m } }$ matrix.   
vv(Int n, Int m, const T &a) Constructor, initialize all elements to the value a.   
vv(Int n, Int m, const T \*a) Constructor, initialize elements by rows to the values in a C-style array.   
vv(const NRmatrix &rhs) Copy constructor.   
vv.nrows() Returns number of rows n.   
vv.ncols() Returns number of columns m.   
vv.resize(Int newn, Int newm) Resizes vv to newn $\times$ newm. We do not assume that contents are preserved.   
vv.assign(Int newn, Int newm, Resizes vv to $\mathtt { n e w n } \times \mathtt { n e w m }$ , const t &a) and sets all elements to the value a.   
vv[Int i] Return a pointer to the first element in row i (not often used by itself).   
v[Int i][Int j] Element of vv by subscript, either an l-value and an r-value.   
vv = rhs Assignment operator. Resizes vv if necessary and makes it a copy of the matrix rhs.   
typedef T value_type; Makes T available externally.

For more precise specifications, see $\ S 1 . 4 . 3$

There is one additional property that we assume of the vector and matrix classes, namely that all of an object’s elements are stored in sequential order. For a vector, this means that its elements can be addressed by pointer arithmetic relative to the first element. For example, if we have

VecDoub a(100);   
Doub $\ast \boldsymbol { \mathrm b } ~ = ~ \& \boldsymbol { \mathrm [ 0 ] }$ ;

then a[i] and b[i] reference the same element, both as an l-value and as an rvalue. This capability is sometimes important for inner-loop efficiency, and it is also useful for interfacing with legacy code that can handle Doub\* arrays, but not VecDoub vectors. Although the original $\mathrm { C } { + + }$ Standard Library did not guarantee this behavior, all known implementations of it do so, and the behavior is now required by an amendment to the standard [2].

For matrices, we analogously assume that storage is by rows within a single sequential block so that, for example,

Int $\scriptstyle \mathtt { n } = 9 7$ , $\mathtt { m } = 1 0 3$ ;  
MatDoub $\mathtt { a } ( \mathtt { n } , \mathtt { m } )$ ;  
Doub \*b $=$ &a[0][0];

implies that a[i][j] and b $[ \mathrm { m } { * \mathrm { i } + \mathrm { j } } ]$ are equivalent.

A few of our routines need the capability of taking as an argument either a vector or else one row of a matrix. For simplicity, we usually code this using overloading, as, e.g.,

void someroutine(Doub \*v, Int m) { Version for a matrix row.   
}   
inline void someroutine(VecDoub &v) { Version for a vector. someroutine(&v[0],v.size());   
}

For a vector v, a call looks like someroutine(v), while for row i of a matrix vv it is someroutine(&vv[i][0],vv.ncols()). While the simpler argument vv[i] would in fact work in our implementation of NRmatrix, it might not work in some other matrix class that guarantees sequential storage but has the return type for a single subscript different from $^ { \mathrm { T } * }$ .

# 1.4.3 Implementations in nr3.h

For reference, here is a complete declaration of NRvector.

template <class T>   
class NRvector {   
private: int nn; Size of array, indices $0 \cdot \cdot \mathtt { n n } ^ { - 1 }$ . T \*v; Pointer to data array.   
public: NRvector(); Default constructor. explicit NRvector(int n); Construct vector of size n. NRvector(int n, const T &a); Initialize to constant value a. NRvector(int n, const T \*a); Initialize to values in C-style array a. NRvector(const NRvector &rhs); Copy constructor. NRvector & operator $\mathop { : = }$ (const NRvector &rhs); Assignment operator. typedef T value_type; Make T available. inline T & operator[](const int i); Return element number i. inline const T & operator[](const int i) const; const version. inline int size() const; Return size of vector. void resize(int newn); Resize, losing contents. void assign(int newn, const T &a); Resize and assign a to every element. \~NRvector(); Destructor.

The implementations are straightforward and can be found in the file $\mathtt { n r 3 . h }$ . The only issues requiring finesse are the consistent treatment of zero-length vectors and the avoidance of unnecessary resize operations.

A complete declaration of NRmatrix is

template <class T>   
class NRmatrix {   
private: int nn; Number of rows and columns. Index int mm; range is 0..nn-1, 0..mm-1. T \*\*v; Storage for data.   
public: NRmatrix(); Default constructor. NRmatrix(int n, int m); Construct ${ \mathfrak { n } } \times { \mathfrak { m } }$ matrix. NRmatrix(int n, int m, const T &a); Initialize to constant value a. NRmatrix(int n, int m, const T \*a); Initialize to values in C-style array a. NRmatrix(const NRmatrix &rhs); Copy constructor. NRmatrix & operator $^ { * = }$ (const NRmatrix &rhs); Assignment operator. typedef T value_type; Make T available. inline T\* operator[](const int i); Subscripting: pointer to row i. inline const $^ { \mathrm { T } * }$ operator[](const int i) const; const version. inline int nrows() const; Return number of rows. inline int ncols() const; Return number of columns. void resize(int newn, int newm); Resize, losing contents. void assign(int newn, int newm, const T &a); Resize and assign a to every element. \~NRmatrix(); Destructor.   
};

A couple of implementation details in NRmatrix are worth commenting on. The private variable $\ast \ast \tau$ points not to the data but rather to an array of pointers to the data rows. Memory allocation of this array is separate from the allocation of space for the actual data. The data space is allocated as a single block, not separately for each row. For matrices of zero size, we have to account for the separate possibilities that there are zero rows, or that there are a finite number of rows, but each with zero columns. So, for example, one of the constructors looks like this:

template <class T>   
NRmatrix<T>::NRmatrix(int n, int m) : nn(n), mm(m), v(n>0 ? new T\*[n] : NULL)   
{ int i,nel=m\*n; if (v) v[0] $=$ nel>0 ? new T[nel] : NULL; for ( $\dot { \bf 1 } = 1$ ;i<n; $\dot { 1 } + + \dot { 1 }$ ) v[i] $=$ v[i-1] + m;   
}

Finally, it matters a lot whether your compiler honors the inline directives in NRvector and NRmatrix above. If it doesn’t, then you may be doing full function calls, saving and restoring context within the processor, every time you address a vector or matrix element. This is tantamount to making $\mathrm { C } { + } { + }$ useless for most numerical computing! Luckily, as we write, the most commonly used compilers are all “honorable” in this respect.

# CITED REFERENCES AND FURTHER READING:

Josuttis, N.M. 1999, The $C { + } { + }$ Standard Library: A Tutorial and Reference (Boston: Addison-Wesley).[1] International Standardization Organization 2003, Technical Corrigendum ISO 14882:2003.[2]

# 1.5 Some Further Conventions and Capabilities

We collect in this section some further explanation of $\mathrm { C } { + } { + }$ language capabilities and how we use them in this book.

# 1.5.1 Error and Exception Handling

We already mentioned that we code error conditions with simple throw statements, like this

# throw("error foo in routine bah");

If you are programming in an environment that has a defined set of error classes, and you want to use them, then you’ll need to change these lines in the routines that you use. Alternatively, without any additional machinery, you can choose between a couple of different, useful behaviors just by making small changes in nr3.h.

By default, nr3.h redefines throw() by a preprocessor macro, #define throw(message) \ {printf("ERROR: %s\n in file %s at line %d\n", \ message,__FILE__,__LINE__); \ exit(1);}

This uses standard ANSI C features, also present in $\mathrm { C } { + } { + }$ , to print the source code file name and line number at which the error occurs. It is inelegant, but perfectly functional.

Somewhat more functional, and definitely more elegant, is to set nr3.h’s compiler switch _USENRERRORCLASS_, which instead substitutes the following code:

struct NRerror { char \*message; char \*file; int line; NRerror(char \*m, char \*f, int l) : message(m), file(f), line(l) {}   
};   
void NRcatch(NRerror err) { printf("ERROR: %s\n in file %s at line %d\n", err.message, err.file, err.line); exit(1);   
}

#define throw(message) throw(NRerror(message,__FILE__,__LINE__));

Now you have a (rudimentary) error class, NRerror, available. You use it by putting a try : : : catch control structure at any desired point (or points) in your code, for example (-2.9),

try Cholesky achol(a);   
}   
catch (NRerror err) { NRcatch(err);   
}

As shown, the use of the NRcatch function above simply mimics the behavior of the previous macro in the global context. But you don’t have to use NRcatch at all: You can substitute any code that you want for the body of the catch statement. If you want to distinguish between different kinds of exceptions that may be thrown, you can use the information returned in err. We’ll let you figure this out yourself. And of course you are welcome to add more complicated error classes to your own copy of $\mathtt { n r 3 . h }$ .

# 1.5.2 Const Correctness

Few topics in discussions about $\mathrm { C } { + } { + }$ evoke more heat than questions about the keyword const. We are firm believers in using const wherever possible, to achieve what is called “const correctness.” Many coding errors are automatically trapped by the compiler if you have qualified identifiers that should not change with const when they are declared. Also, using const makes your code much more readable: When you see const in front of an argument to a function, you know immediately that the function will not modify the object. Conversely, if const is absent, you should be able to count on the object being changed somewhere.

We are such strong const believers that we insert const even where it is theoretically redundant: If an argument is passed by value to a function, then the function makes a copy of it. Even if this copy is modified by the function, the original value is unchanged after the function exits. While this allows you to change, with impunity, the values of arguments that have been passed by value, this usage is error-prone and hard to read. If your intention in passing something by value is that it is an input variable only, then make it clear. So we declare a function $f ( x )$ as, for example,

# Doub f(const Doub x);

If in the function you want to use a local variable that is initialized to ${ \tt x }$ but then gets changed, define a new quantity — don’t use x. If you put const in the declaration, the compiler will not let you get this wrong.

Using const in your function arguments makes your function more general: Calling a function that expects a const argument with a non-const variable involves a “trivial” conversion. But trying to pass a const quantity to a non-const argument is an error.

A final reason for using const is that it allows certain user-defined conversions to be made. As discussed in [1], this can be useful if you want to use Numerical Recipes routines with another matrix/vector class library.

We now need to elaborate on what exactly const does for a nonsimple type such as a class that is an argument of a function. Basically, it guarantees that the object is not modified by the function. In other words, the object’s data members are unchanged. But if a data member is a pointer to some data, and the data itself is not a member variable, then the data can be changed even though the pointer cannot be.

Let’s look at the implications of this for a function f that takes an NRvector<Doub> argument a. To avoid unnecessary copying, we always pass vectors and matrices by reference. Consider the difference between declaring the argument of a function with and without const:

void f(NRvector<Doub> &a) versus void f(const NRvector<Doub> &a)

The const version promises that f does not modify the data members of a. But a statement like

inside the function definition is in principle perfectly OK — you are modifying the data pointed to, not the pointer itself.

“Isn’t there some way to protect the data?” you may ask. Yes, there is: You can declare the return type of the subscript operator, operator[], to be const. This is why there are two versions of operator[] in the NRvector class,

# T & operator[](const int i);const T & operator[](const int i) const;

The first form returns a reference to a modifiable vector element, while the second returns a nonmodifiable vector element (because the return type has a const in front).

But how does the compiler know which version to invoke when you just write a[i]? That is specified by the trailing word const in the second version. It refers not to the returned element, nor to the argument i, but to the object whose operator[] is being invoked, in our example the vector a. Taken together, the two versions say this to the compiler: “If the vector a is const, then transfer that const’ness to the returned element a[i]. If it isn’t, then don’t.”

The remaining question is thus how the compiler determines whether a is const. In our example, where a is a function argument, it is trivial: The argument is either declared as const or else it isn’t. In other contexts, a might be const because you originally declared it as such (and initialized it via constructor arguments), or because it is a const reference data member in some other object, or for some other, more arcane, reason.

As you can see, getting const to protect the data is a little complicated. Judging from the large number of matrix/vector libraries that follow this scheme, many people feel that the payoff is worthwhile. We urge you always to declare as const those objects and variables that are not intended to be modified. You do this both at the time an object is actually created and in the arguments of function declarations and definitions. You won’t regret making a habit of const correctness.

In $\ S 1 . 4$ we defined vector and matrix type names with trailing $_ - \ I$ labels, for example, VecDoub_I and MatInt_I. The _I, which stands for “input to a function,” means that the type is declared as const. (This is already done in the typedef statement; you don’t have to repeat it.) The corresponding labels $_ - 0$ and $_ - \pm 0$ are to remind you when arguments are not just non-const, but will actually be modified by the function in whose argument list they appear.

Having rightly put all this emphasis on const correctness, duty compels us also to recognize the existence of an alternative philosophy, which is to stick with the more rudimentary view “const protects the container, not the contents.” In this case you would want only one form of operator[], namely

# T & operator[](const int i) const;

It would be invoked whether your vector was passed by const reference or not. In both cases element i is returned as potentially modifiable. While we are opposed to this philosophically, it turns out that it does make possible a tricky kind of automatic type conversion that allows you to use your favorite vector and matrix classes instead of NRvector and NRmatrix, even if your classes use a syntax completely different from what we have assumed. For information on this very specialized application, see [1].

# 1.5.3 Abstract Base Class (ABC), or Template?

There is sometimes more than one good way to achieve some end in $\mathrm { C } { + + }$ . Heck, let’s be honest: There is always more than one way. Sometimes the differences amount to small tweaks, but at other times they embody very different views about the language. When we make one such choice, and you prefer another, you are going to be quite annoyed with us. Our defense against this is to avoid foolish consistencies, and to illustrate as many viewpoints as possible.

A good example is the question of when to use an abstract base class (ABC) versus a template, when their capabilities overlap. Suppose we have a function func that can do its (useful) thing on, or using, several different types of objects, call them ObjA, ObjB, and ObjC. Moreover, func doesn’t need to know much about the object it interacts with, only that it has some method tellme.

We could implement this setup as an abstract base class:

Abstract Base Class for objects with tellme.

Derived class.

Derived class.

struct ObjABC { virtual void tellme ${ \mathrm { ~  ~ \omega ~ } } ( \ k ) \ = \ 0$   
};   
struct ObjA : ObjABC { void tellme() {...}   
};   
struct ObjB : ObjABC { void tellme() {...}   
};   
struct ObjC : ObjABC { void tellme() {...}   
};   
void func(ObjABC &x) { ... x.tellme();   
}

Derived class.

References the appropriate tellme.

On the other hand, using a template, we can write code for func without ever seeing (or even knowing the names of) the objects for which it is intended:

template<class T>   
void func(T &x) { ... x.tellme();   
}

That certainly seems easier! Is it better?

Maybe. A disadvantage of templates is that the template must be available to the compiler every time it encounters a call to func. This is because it actually compiles a different version of func for every different type of argument T that it encounters. Unless your code is so large that it cannot easily be compiled as a single unit, however, this is not much of a disadvantage. On the other side, favoring templates, is the fact that virtual functions incur a small run-time penalty when they are called. But this is rarely significant.

The deciding factors in this example relate to software engineering, not performance, and are hidden in the lines with ellipses (...). We haven’t really told you how closely related ObjA, ObjB, and ObjC are. If they are close, then the ABC approach offers possibilities for putting more than just tellme into the base class. Putting things into the base class, whether data or pure virtual methods, lets the compiler enforce consistency across the derived classes. If you later write another derived object ObjD, its consistency will also be enforced. For example, the compiler will require you to implement a method in every derived class corresponding to every pure virtual method in the base class.

By contrast, in the template approach, the only enforced consistency will be that the method tellme exists, and this will only be enforced at the point in the code where func is actually called with an ObjD argument (if such a point exists), not at the point where ObjD is defined. Consistency checking in the template approach is thus somewhat more haphazard.

Laid-back programmers will opt for templates. Up-tight programmers will opt for ABCs. We opt for. . . both, on different occasions. There can also be other reasons, having to do with subtle features of class derivation or of templates, for choosing one approach over the other. We will point these out as we encounter them in later chapters. For example, in Chapter 17 we define an abstract base class called StepperBase for the various “stepper” routines for solving ODEs. The derived classes implement particular stepping algorithms, and they are templated so they can accept function or functor arguments (see $\ S 1 . 3 . 3 )$ .

# 1.5.4 NaN and Floating Point Exceptions

We mentioned in $\ S 1 . 1 . 1$ that the IEEE floating-point standard includes a representation for NaN, meaning “not a number.” NaN is distinct from positive and negative infinity, as well as from every representable number. It can be both a blessing and a curse.

The blessing is that it can be useful to have a value that can be used with meanings like “don’t process me” or “missing data” or “not yet initialized.” To use NaN in this fashion, you need to be able to set variables to it, and you need to be able to test for its having been set.

Setting is easy. The “approved” method is to use numeric_limits. In nr3.h the line

static const Doub NaN $=$ numeric_limits<Doub>::quiet_NaN();

defines a global value NaN, so that you can write things like

$$
\begin{array} { r } { \tt { x } = N a N ; } \end{array}
$$

at will. If you ever encounter a compiler that doesn’t do this right (it’s a pretty obscure corner of the standard library!), then try either

Uint proto_nan[2] $=$ 0xffffffff, 0x7fffffff;   
double NaN $\qquad = ~ *$ ( double\* )proto_nan;

(which assumes little-endian behavior; cf. $\ S 1 . 1 . 1 )$ or the self-explanatory

Doub $\begin{array} { r } { \mathbb { N } { \bf a } \mathbb { N } = { \bf s } { \bf q } { \bf r } { \bf t } \left( - 1 . \right) ; } \end{array}$

which may, however, throw an immediate exception (see below) and thus not work for this purpose. But, one way or another, you can generally figure out how to get a NaN constant into your environment.

Testing also requires a bit of (one-time) experimentation: According to the IEEE standard, $\mathrm { N a N }$ is guaranteed to be the only value that is not equal to itself!

So, the “approved” method of testing whether Doub value x has been set to NaN is

$$
\mathrm { i } \textbf { f } \left( \textbf { x } : = \textbf { x } \right) ~ \{ \dots , \}
$$

(or test for equality to determine that it’s not a NaN). Unfortunately, at time of writing, some otherwise perfectly good compilers don’t do this right. Instead, they provide a macro isnan() that returns true if the argument is NaN, otherwise false. (Check carefully whether the required #include is math.h or float.h — it varies.)

What, then, is the curse of NaN? It is that some compilers, notably Microsoft, have poorly thought-out default behaviors in distinguishing quiet NaNs from signalling NaNs. Both kinds of NaNs are defined in the IEEE floating-point standard. Quiet NaNs are supposed to be for uses like those above: You can set them, test them, and propagate them by assignment, or even through other floating operations. In such uses they are not supposed to signal an exception that causes your program to abort. Signalling NaNs, on the other hand, are, as the name implies, supposed to signal exceptions. Signalling NaNs should be generated by invalid operations, such as the square root or logarithm of a negative number, or pow(0.,0.).

If all NaNs are treated as signalling exceptions, then you can’t make use of them as we have suggested above. That’s annoying, but OK. On the other hand, if all NaNs are treated as quiet (the Microsoft default at time of writing), then you will run long calculations only to find that all the results are NaN — and you have no way of locating the invalid operation that triggered the propagating cascade of (quiet) NaNs. That’s not OK. It makes debugging a nightmare. (You can get the same disease if other floating-point exceptions propagate, for example overflow or division-by-zero.)

Tricks for specific compilers are not within our normal scope. But this one is so essential that we make it an “exception”: If you are living on planet Microsoft, then the lines of code,

int cw $=$ _controlfp(0,0);   
cw $\& = \widetilde $ (EM_INVALID | EM_OVERFLOW | EM_ZERODIVIDE );   
_controlfp(cw,MCW_EM);

at the beginning of your program will turn NaNs from invalid operations, overflows, and divides-by-zero into signalling NaNs, and leave all the other NaNs quiet. There is a compiler switch, _TURNONFPES_ in nr3.h that will do this for you automatically. (Further options are EM_UNDERFLOW, EM_INEXACT, and EM_DENORMAL, but we think these are best left quiet.)

# 1.5.5 Miscellany

- Bounds checking in vectors and matrices, that is, verifying that subscripts are in range, is expensive. It can easily double or triple the access time to subscripted elements. In their default configuration, the NRvector and NRmatrix classes never do bounds checking. However, $\mathtt { n r 3 . h }$ has a compiler switch, _CHECKBOUNDS_, that turns bounds checking on. This is implemented by preprocessor directives for conditional compilation so there is no performance penalty when you leave it turned off. This is ugly, but effective.

The vector $< >$ class in the $\mathrm { C } { + } { + }$ Standard Library takes a different tack. If you access a vector element by the syntax $\tau \left[ \dot { \bf 1 } \right]$ , there is no bounds checking. If you instead use the at() method, as v.at(i), then bounds checking is performed. The obvious weakness of this approach is that you can’t easily change a lengthy program from one method to the other, as you might want to

do when debugging.

- The importance to performance of avoiding unnecessary copying of large objects, such as vectors and matrices, cannot be overemphasized. As already mentioned, they should always be passed by reference in function arguments. But you also need to be careful about, or avoid completely, the use of functions whose return type is a large object. This is true even if the return type is a reference (which is a tricky business anyway). Our experience is that compilers often create temporary objects, using the copy constructor, when the need to do so is obscure or nonexistent. That is why we so frequently write void functions that have an argument of type (e.g.) MatDoub_O for returning the “answer.” (When we do use vector or matrix return types, our excuse is either that the code is pedagogical, or that the overhead is negligible compared to some big calculation that has just been done.)

You can check up on your compiler by instrumenting the vector and matrix classes: Add a static integer variable to the class definition, increment it within the copy constructor and assignment operator, and look at its value before and after operations that (you think) should not require any copies. You might be surprised.

- There are only two routines in Numerical Recipes that use three-dimensional arrays, rlft3 in $\ S 1 2 . 6$ , and solvde in $\ S 1 8 . 3$ . The file nr3.h includes a rudimentary class for three-dimensional arrays, mainly to service these two routines. In many applications, a better way to proceed is to declare a vector of matrices, for example,

vector<MatDoub> threedee(17);   
for (Int i=0;i<17;i++) threedee[i].resize(19,21);

which creates, in effect, a three-dimensional array of size $1 7 \times 1 9 \times 2 1$ . You can address individual components as threedee[i][j][k].

- “Why no namespace?” Industrial-strength programmers will notice that, unlike the second edition, this third edition of Numerical Recipes does not shield its function and class names by a NR:: namespace. Therefore, if you are so bold as to #include every single file in the book, you are dumping on the order of 500 names into the global namespace, definitely a bad idea!

The explanation, quite simply, is that the vast majority of our users are not industrial-strength programmers, and most found the NR:: namespace annoying and confusing. As we emphasized, strongly, in $\ S 1 . 0 . 1$ , NR is not a program library. If you want to create your own personal namespace for NR, please go ahead.

- In the distant past, Numerical Recipes included provisions for unit- or onebased, instead of zero-based, array indices. The last such version was published in 1992. Zero-based arrays have become so universally accepted that we no longer support any other option.

# CITED REFERENCES AND FURTHER READING:

Numerical Recipes Software 2007, “Using Other Vector and Matrix Libraries,” Numerical Recipes Webnote No. 1,at http://www.nr.com/webnotes?1 [1]

# Solution of Linear Algebraic Equations

# 2.0 Introduction

The most basic task in linear algebra, and perhaps in all of scientific computing, is to solve for the unknowns in a set of linear algebraic equations. In general, a set of linear algebraic equations looks like this:

$$
\begin{array} { c } { { a _ { 0 0 } x _ { 0 } + a _ { 0 1 } x _ { 1 } + a _ { 0 2 } x _ { 2 } + \dots + a _ { 0 , N - 1 } x _ { N - 1 } = b _ { 0 } } } \\ { { \ } } \\ { { a _ { 1 0 } x _ { 0 } + a _ { 1 1 } x _ { 1 } + a _ { 1 2 } x _ { 2 } + \dots + a _ { 1 , N - 1 } x _ { N - 1 } = b _ { 1 } } } \\ { { \ } } \\ { { a _ { 2 0 } x _ { 0 } + a _ { 2 1 } x _ { 1 } + a _ { 2 2 } x _ { 2 } + \dots + a _ { 2 , N - 1 } x _ { N - 1 } = b _ { 2 } } } \\ { { \ } } \\ { { \dots } } \\ { { \ } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \\ { { { \cal { I } } } } \end{array}
$$

Here the $N$ unknowns $x _ { j }$ , $j = 0 , 1 , \dotsc , N - 1$ are related by $M$ equations. The coefficients $a _ { i j }$ with $i \ = \ 0 , 1 , \ldots , M - 1$ and $j ~ = ~ 0 , 1 , \ldots , N - 1$ are known numbers, as are the right-hand side quantities $b _ { i }$ , $i = 0 , 1 , \ldots , M - 1$ .

If $N = M$ , then there are as many equations as unknowns, and there is a good chance of solving for a unique solution set of $x _ { j }$ ’s. Otherwise, if $N \neq M$ , things are even more interesting; we’ll have more to say about this below.

If we write the coefficients $a _ { i j }$ as a matrix, and the right-hand sides $b _ { i }$ as a column vector,

$$
\mathbf { A } = \left[ \begin{array} { c c c c } { a _ { 0 0 } } & { a _ { 0 1 } } & { \ldots } & { a _ { 0 , N - 1 } } \\ { a _ { 1 0 } } & { a _ { 1 1 } } & { \ldots } & { a _ { 1 , N - 1 } } \\ { \ldots } & { \ldots } & { } & { } \\ { a _ { M - 1 , 0 } } & { a _ { M - 1 , 1 } } & { \ldots } & { a _ { M - 1 , N - 1 } } \end{array} \right] \qquad \mathbf { b } = \left[ \begin{array} { c } { b _ { 0 } } \\ { b _ { 1 } } \\ { \ldots } \\ { b _ { M - 1 } } \end{array} \right]
$$

then equation (2.0.1) can be written in matrix form as

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

Here, and throughout the book, we use a raised dot to denote matrix multiplication, or the multiplication of a matrix and a vector, or the dot product of two vectors.

This usage is nonstandard, but we think it adds clarity: the dot is, in all of these cases, a contraction operator that represents the sum over a pair of indices, for example

$$
\begin{array} { l c l } { { { \bf C } = { \bf A \cdot B } } } & { { \displaystyle \Longleftrightarrow } } & { { \displaystyle c _ { i k } = \sum _ { j } a _ { i j } b _ { j k } } } \\ { { } } & { { } } & { { } } \\ { { { \bf b } = { \bf A \cdot x } } } & { { \displaystyle \Longleftrightarrow } } & { { \begin{array} { r } { { b _ { i } = \displaystyle \sum _ { j } a _ { i j } x _ { j } } } \\ { { } } \end{array} } } \\ { { \bf d = x \cdot A } } & { { \displaystyle \Longleftrightarrow } } & { { \begin{array} { r } { { d _ { j } = \displaystyle \sum _ { i } x _ { i } a _ { i j } } } \\ { { } } \end{array} } } \\ { { \boldsymbol { q } = { \bf x \cdot y } } } & { { \displaystyle \Longleftrightarrow } } & { { \boldsymbol { q } = \displaystyle \sum _ { i } x _ { i } y _ { i } } } \end{array}
$$

In matrices, by convention, the first index on an element $a _ { i j }$ denotes its row and the second index its column. For most purposes you don’t need to know how a matrix is stored in a computer’s physical memory; you just reference matrix elements by their two-dimensional addresses, e.g., $a _ { 3 4 } = \mathtt { a } [ 3 ]$ [4]. This $\mathrm { C } { + + }$ notation can in fact hide a variety of subtle and versatile physical storage schemes, see $\ S 1 . 4$ and $\ S 1 . 5$ .

# 2.0.1 Nonsingular versus Singular Sets of Equations

You might be wondering why, above, and for the case $M = N$ , we credited only a “good” chance of solving for the unknowns. Analytically, there can fail to be a solution (or a unique solution) if one or more of the $M$ equations is a linear combination of the others, a condition called row degeneracy, or if all equations contain certain variables only in exactly the same linear combination, called column degeneracy. It turns out that, for square matrices, row degeneracy implies column degeneracy, and vice versa. A set of equations that is degenerate is called singular. We will consider singular matrices in some detail in $\ S 2 . 6$ .

Numerically, at least two additional things prevent us from getting a good solution:

- While not exact linear combinations of each other, some of the equations may be so close to linearly dependent that roundoff errors in the machine render them linearly dependent at some stage in the solution process. In this case your numerical procedure will fail, and it can tell you that it has failed. Accumulated roundoff errors in the solution process can swamp the true solution. This problem particularly emerges if $N$ is too large. The numerical procedure does not fail algorithmically. However, it returns a set of $x$ ’s that are wrong, as can be discovered by direct substitution back into the original equations. The closer a set of equations is to being singular, the more likely this is to happen, since increasingly close cancellations will occur during the solution. In fact, the preceding item can be viewed as the special case in which the loss of significance is unfortunately total.

Much of the sophistication of well-written “linear equation-solving packages” is devoted to the detection and/or correction of these two pathologies. It is difficult to give any firm guidelines for when such sophistication is needed, since there is no such thing as a “typical” linear problem. But here is a rough idea: Linear sets with $N$ no larger than 20 or 50 are routine if they are not close to singular; they rarely require more than the most straightforward methods, even in only single (that is, float) precision. With double precision, this number can readily be extended to $N$ as large as perhaps 1000, after which point the limiting factor anyway soon becomes machine time, not accuracy.

Even larger linear sets, $N$ in the thousands or millions, can be solved when the coefficients are sparse (that is, mostly zero), by methods that take advantage of the sparseness. We discuss this further in $\ S 2 . 7$ .

Unfortunately, one seems just as often to encounter linear problems that, by their underlying nature, are close to singular. In this case, you might need to resort to sophisticated methods even for the case of $N = 1 0$ (though rarely for $N = 5$ ). Singular value decomposition (-2.6) is a technique that can sometimes turn singular problems into nonsingular ones, in which case additional sophistication becomes unnecessary.

# 2.0.2 Tasks of Computational Linear Algebra

There is much more to linear algebra than just solving a single set of equations with a single right-hand side. Here, we list the major topics treated in this chapter. (Chapter 11 continues the subject with discussion of eigenvalue/eigenvector problems.)

When $M = N$ :

- Solution of the matrix equation $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ for an unknown vector $\mathbf { X }$ $( \ S 2 . 1 -$ $\ S 2 . 1 0 )$ .   
- Solution of more than one matrix equation $\mathbf { A } \cdot \mathbf { x } _ { j } = \mathbf { b } _ { j }$ , for a set of vectors $\mathbf { X } _ { j }$ , $j = 0 , 1 , \ldots$ , each corresponding to a different, known right-hand side vector $\mathbf { b } _ { j }$ . In this task the key simplification is that the matrix A is held constant, while the right-hand sides, the b’s, are changed $( \ S 2 . 1 - \ S 2 . 1 0 )$ .   
- Calculation of the matrix $\mathbf { A } ^ { - 1 }$ that is the matrix inverse of a square matrix A, i.e., $\mathbf { A } \cdot \mathbf { A } ^ { - 1 } = \mathbf { A } ^ { - 1 } \cdot \mathbf { A } = \mathbf { 1 }$ , where 1 is the identity matrix (all zeros except for ones on the diagonal). This task is equivalent, for an $N \times N$ matrix A, to the previous task with $N$ different $\mathbf { b } _ { j }$ ’s $( j = 0 , 1 , \ldots , N - 1 )$ , namely the unit vectors $( \mathbf { b } _ { j } =$ all zero elements except for 1 in the $j$ th component). The corresponding $\mathbf { X }$ ’s are then the columns of the matrix inverse of A $\ S 2 . 1$ and $\ S 2 . 3 )$ .   
- Calculation of the determinant of a square matrix A (-2.3).

If $M < N$ , or if $M = N$ but the equations are degenerate, then there are effectively fewer equations than unknowns. In this case there can be either no solution, or else more than one solution vector $\mathbf { X }$ . In the latter event, the solution space consists of a particular solution $\mathbf { x } _ { p }$ added to any linear combination of (typically) $N - M$ vectors (which are said to be in the nullspace of the matrix A). The task of finding the solution space of A involves

- Singular value decomposition of a matrix A (-2.6).

If there are more equations than unknowns, $M \ > \ N$ , there is in general no solution vector $\mathbf { X }$ to equation (2.0.1), and the set of equations is said to be overdetermined. It happens frequently, however, that the best “compromise” solution is sought, the one that comes closest to satisfying all equations simultaneously. If closeness is defined in the least-squares sense, i.e., that the sum of the squares of the differences between the left- and right-hand sides of equation (2.0.1) be minimized, then the overdetermined linear problem reduces to a (usually) solvable linear problem, called the

- Linear least-squares problem.

The reduced set of equations to be solved can be written as the $N \times N$ set of equations

$$
( \mathbf { A } ^ { T } \cdot \mathbf { A } ) \cdot \mathbf { x } = ( \mathbf { A } ^ { T } \cdot \mathbf { b } )
$$

where $\mathbf { A } ^ { T }$ denotes the transpose of the matrix A. Equations (2.0.5) are called the normal equations of the linear least-squares problem. There is a close connection between singular value decomposition and the linear least-squares problem, and the latter is also discussed in $\ S 2 . 6$ . You should be warned that direct solution of the normal equations (2.0.5) is not generally the best way to find least-squares solutions.

Some other topics in this chapter include

- Iterative improvement of a solution (-2.5)   
- Various special forms: symmetric positive-definite (-2.9), tridiagonal (-2.4), band-diagonal (-2.4), Toeplitz (-2.8), Vandermonde (-2.8), sparse (-2.7)   
- Strassen’s “fast matrix inversion” (-2.11).

# 2.0.3 Software for Linear Algebra

Going beyond what we can include in this book, several good software packages for linear algebra are available, though not always in $\mathrm { C } { + } { + }$ . LAPACK, a successor to the venerable LINPACK, was developed at Argonne National Laboratories and deserves particular mention because it is published, documented, and available for free use. ScaLAPACK is a version available for parallel architectures. Packages available commercially include those in the IMSL and NAG libraries.

Sophisticated packages are designed with very large linear systems in mind. They therefore go to great effort to minimize not only the number of operations, but also the required storage. Routines for the various tasks are usually provided in several versions, corresponding to several possible simplifications in the form of the input coefficient matrix: symmetric, triangular, banded, positive-definite, etc. If you have a large matrix in one of these forms, you should certainly take advantage of the increased efficiency provided by these different routines, and not just use the form provided for general matrices.

There is also a great watershed dividing routines that are direct (i.e., execute in a predictable number of operations) from routines that are iterative (i.e., attempt to converge to the desired answer in however many steps are necessary). Iterative methods become preferable when the battle against loss of significance is in danger of being lost, either due to large $N$ or because the problem is close to singular. We will treat iterative methods only incompletely in this book, in $\ S 2 . 7$ and in Chapters 19 and 20. These methods are important but mostly beyond our scope. We will, however, discuss in detail a technique that is on the borderline between direct and iterative methods, namely the iterative improvement of a solution that has been obtained by direct methods (-2.5).

# CITED REFERENCES AND FURTHER READING:

Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press).

Gill, P.E., Murray, W., and Wright, M.H. 1991, Numerical Linear Algebra and Optimization, vol. 1 (Redwood City, CA: Addison-Wesley).   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 4.   
Ueberhuber, C.W. 1997, Numerical Computation: Methods, Software, and Analysis, 2 vols. (Berlin: Springer), Chapter 13.   
Coleman, T.F., and Van Loan, C. 1988, Handbook for Matrix Computations (Philadelphia: S.I.A.M.).   
Forsythe, G.E., and Moler, C.B. 1967, Computer Solution of Linear Algebraic Systems (Englewood Cliffs, NJ: Prentice-Hall).   
Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer).   
Westlake, J.R. 1968, A Handbook of Numerical Matrix Inversion and Solution of Linear Equations (New York: Wiley).   
Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), Chapter 2.   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), Chapter 9.

# 2.1 Gauss-Jordan Elimination

Gauss-Jordan elimination is probably the way you learned to solve linear equations in high school. (You may have learned it as “Gaussian elimination,” but, strictly speaking, that term refers to the somewhat different technique discussed in $\ S 2 . 2 .$ ) The basic idea is to add or subtract linear combinations of the given equations until each equation contains only one of the unknowns, thus giving an immediate solution. You might also have learned to use the same technique for calculating the inverse of a matrix.

For solving sets of linear equations, Gauss-Jordan elimination produces both the solution of the equations for one or more right-hand side vectors b, and also the matrix inverse $\mathbf { A } ^ { - 1 }$ . However, its principal deficiencies are (i) that it requires all the right-hand sides to be stored and manipulated at the same time, and (ii) that when the inverse matrix is not desired, Gauss-Jordan is three times slower than the best alternative technique for solving a single linear set (-2.3). The method’s principal strength is that it is as stable as any other direct method, perhaps even a bit more stable when full pivoting is used (see $\ S 2 . 1 . 2 )$ .

For inverting a matrix, Gauss-Jordan elimination is about as efficient as any other direct method. We know of no reason not to use it in this application if you are sure that the matrix inverse is what you really want.

You might wonder about deficiency (i) above: If we are getting the matrix inverse anyway, can’t we later let it multiply a new right-hand side to get an additional solution? This does work, but it gives an answer that is very susceptible to roundoff error and not nearly as good as if the new vector had been included with the set of right-hand side vectors in the first instance.

Thus, Gauss-Jordan elimination should not be your method of first choice for solving linear equations. The decomposition methods in $\ S 2 . 3$ are better. Why do we discuss Gauss-Jordan at all? Because it is straightforward, solid as a rock, and a good place for us to introduce the important concept of pivoting which will also be important for the methods described later. The actual sequence of operations performed in Gauss-Jordan elimination is very closely related to that performed by the routines in the next two sections.

# 2.1.1 Elimination on Column-Augmented Matrices

For clarity, and to avoid writing endless ellipses $( \cdots )$ we will write out equations only for the case of four equations and four unknowns, and with three different righthand side vectors that are known in advance. You can write bigger matrices and extend the equations to the case of $N \times N$ matrices, with $M$ sets of right-hand side vectors, in completely analogous fashion. The routine implemented below in $\ S 2 . 1 . 2$ is, of course, general.

Consider the linear matrix equation

$$
\begin{array} { r } { [ \begin{array} { c c c c } { a _ { 0 0 } } & { a _ { 0 1 } } & { a _ { 0 2 } } & { a _ { 0 3 } } \\ { a _ { 1 0 } } & { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 0 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 0 } } & { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} ] \cdot [ \begin{array} { c } { ( \begin{array} { c } { x _ { 0 0 } } \\ { x _ { 1 0 } } \\ { x _ { 2 1 } } \\ { x _ { 3 0 } } \end{array} ) _ { \perp } } \\ { ( \begin{array} { c } { x _ { 2 1 } } \\ { x _ { 3 1 } } \\ { x _ { 3 2 } } \end{array} ) _ { \perp } } \end{array} ( \begin{array} { c } { x _ { 0 1 } } \\ { x _ { 1 1 } } \\ { x _ { 2 2 } } \\ { x _ { 3 1 } } \\ { x _ { 3 2 } } \end{array} ) _ { \perp } ( \begin{array} { c } { y _ { 0 0 } } \\ { y _ { 1 0 } } \\ { y _ { 2 2 } } \\ { y _ { 3 0 } } \end{array} ) _ { \perp } ( \begin{array} { c c c c } { y _ { 0 1 } } & { y _ { 0 1 } } & { y _ { 0 2 } } & { y _ { 0 3 } } \\ { y _ { 1 1 } } & { y _ { 1 1 } } & { y _ { 1 2 } } & { y _ { 1 3 } } \\ { y _ { 2 0 } } & { y _ { 2 1 } } & { y _ { 2 2 } } & { y _ { 2 3 } } \\ { y _ { 3 0 } } & { y _ { 3 1 } } & { y _ { 3 2 } } & { y _ { 3 3 } } \end{array} ) ] } \\  = [ ( \begin{array} { c }  ( \begin{array} { c } { b _ { 0 0 } } \\ { b _ { 1 0 } } \\ { b _ { 1 0 } } \\ { b _ { 2 0 } } \\ { b _ { 3 0 } } \end{array} ) _ { \perp } ( \begin{array} { c } { b _ { 0 1 } } \\ { b _ { 1 1 } } \\ { b _ { 2 1 } } \\ { b _ { 3 1 } } \end{array} ) _ { \perp } ( \begin{array} { c } { b _ { 0 2 } } \\ { b _ { 1 2 } } \\  \end{array} \end{array} \end{array}
$$

Here the raised dot (	) signifies matrix multiplication, while the operator $\sqcup$ just signifies column augmentation, that is, removing the abutting parentheses and making a wider matrix out of the operands of the $\sqcup$ operator.

It should not take you long to write out equation (2.1.1) and to see that it simply states that $x _ { i j }$ is the $i$ th component $( i = 0 , 1 , 2 , 3 )$ ) of the vector solution of the $j$ th right-hand side $( j = 0 , 1 , 2 )$ , the one whose coefficients are $b _ { i j } , i = 0 , 1 , 2 , 3$ ; and that the matrix of unknown coefficients $y _ { i j }$ is the inverse matrix of $a _ { i j }$ . In other words, the matrix solution of

$$
[ \mathbf { A } ] \cdot [ \mathbf { x _ { 0 } } \sqcup \mathbf { x _ { 1 } } \sqcup \mathbf { x } _ { 2 } \sqcup \mathbf { Y } ] = [ \mathbf { b } _ { 0 } \sqcup \mathbf { b } _ { 1 } \sqcup \mathbf { b } _ { 2 } \sqcup \mathbf { 1 } ]
$$

where $\mathbf { A }$ and $\mathbf { Y }$ are square matrices, the $\mathbf { b } _ { i }$ ’s and $\mathbf { X } _ { i }$ ’s are column vectors, and 1 is the identity matrix, simultaneously solves the linear sets

$$
\mathbf { A } \cdot \mathbf { x } _ { 0 } = \mathbf { b } _ { 0 } \qquad \mathbf { A } \cdot \mathbf { x } _ { 1 } = \mathbf { b } _ { 1 } \qquad \mathbf { A } \cdot \mathbf { x } _ { 2 } = \mathbf { b } _ { 2 }
$$

and

$$
\mathbf { A \cdot Y } = \mathbf { 1 }
$$

Now it is also elementary to verify the following facts about (2.1.1):

- Interchanging any two rows of A and the corresponding rows of the $\mathbf { b }$ ’s and of 1 does not change (or scramble in any way) the solution $\mathbf { X }$ ’s and Y . Rather, it just corresponds to writing the same set of linear equations in a different order. Likewise, the solution set is unchanged and in no way scrambled if we replace any row in A by a linear combination of itself and any other row, as long as we do the same linear combination of the rows of the $\mathbf { b }$ ’s and 1 (which then is no longer the identity matrix, of course).

- Interchanging any two columns of A gives the same solution set only if we simultaneously interchange corresponding rows of the $\mathbf { X }$ ’s and of Y . In other words, this interchange scrambles the order of the rows in the solution. If we do this, we will need to unscramble the solution by restoring the rows to their original order.

Gauss-Jordan elimination uses one or more of the above operations to reduce the matrix A to the identity matrix. When this is accomplished, the right-hand side becomes the solution set, as one sees instantly from (2.1.2).

# 2.1.2 Pivoting

In “Gauss-Jordan elimination with no pivoting,” only the second operation in the above list is used. The zeroth row is divided by the element $a _ { 0 0 }$ (this being a trivial linear combination of the zeroth row with any other row — zero coefficient for the other row). Then the right amount of the zeroth row is subtracted from each other row to make all the remaining $a _ { i 0 }$ ’s zero. The zeroth column of A now agrees with the identity matrix. We move to column 1 and divide row 1 by $a _ { 1 1 }$ , then subtract the right amount of row 1 from rows 0, 2, and 3, so as to make their entries in column 1 zero. Column 1 is now reduced to the identity form. And so on for columns 2 and 3. As we do these operations to A, we of course also do the corresponding operations to the b’s and to 1 (which by now no longer resembles the identity matrix in any way!).

Obviously we will run into trouble if we ever encounter a zero element on the (then current) diagonal when we are going to divide by the diagonal element. (The element that we divide by, incidentally, is called the pivot element or pivot.) Not so obvious, but true, is the fact that Gauss-Jordan elimination with no pivoting (no use of the first or third procedures in the above list) is numerically unstable in the presence of any roundoff error, even when a zero pivot is not encountered. You must never do Gauss-Jordan elimination (or Gaussian elimination; see below) without pivoting!

So what is this magic pivoting? Nothing more than interchanging rows (partial pivoting) or rows and columns (full pivoting), so as to put a particularly desirable element in the diagonal position from which the pivot is about to be selected. Since we don’t want to mess up the part of the identity matrix that we have already built up, we can choose among elements that are both (i) on rows below (or on) the one that is about to be normalized, and also (ii) on columns to the right (or on) the column we are about to eliminate. Partial pivoting is easier than full pivoting, because we don’t have to keep track of the permutation of the solution vector. Partial pivoting makes available as pivots only the elements already in the correct column. It turns out that partial pivoting is “almost” as good as full pivoting, in a sense that can be made mathematically precise, but which need not concern us here (for discussion and references, see [1]). To show you both variants, we do full pivoting in the routine in this section and partial pivoting in $\ S 2 . 3$ .

We have to state how to recognize a particularly desirable pivot when we see one. The answer to this is not completely known theoretically. It is known, both theoretically and in practice, that simply picking the largest (in magnitude) available element as the pivot is a very good choice. A curiosity of this procedure, however, is that the choice of pivot will depend on the original scaling of the equations. If we take the third linear equation in our original set and multiply it by a factor of a million, it is almost guaranteed that it will contribute the first pivot; yet the underlying solution of the equations is not changed by this multiplication! One therefore sometimes sees routines which choose as pivot that element which would have been largest if the original equations had all been scaled to have their largest coefficient normalized to unity. This is called implicit pivoting. There is some extra bookkeeping to keep track of the scale factors by which the rows would have been multiplied. (The routines in $\ S 2 . 3$ include implicit pivoting, but the routine in this section does not.)

Finally, let us consider the storage requirements of the method. With a little reflection you will see that at every stage of the algorithm, either an element of A is predictably a one or zero (if it is already in a part of the matrix that has been reduced to identity form) or else the exactly corresponding element of the matrix that started as 1 is predictably a one or zero (if its mate in A has not been reduced to the identity form). Therefore the matrix 1 does not have to exist as separate storage: The matrix inverse of A is gradually built up in A as the original A is destroyed. Likewise, the solution vectors x can gradually replace the right-hand side vectors $\mathbf { b }$ and share the same storage, since after each column in A is reduced, the corresponding row entry in the b’s is never again used.

Here is a routine that does Gauss-Jordan elimination with full pivoting, replacing its input matrices by the desired answers. Immediately following is an overloaded version for use when there are no right-hand sides, i.e., when you want only the matrix inverse.

# void gaussj(MatDoub_IO &a, MatDoub_IO &b)

Linear equation solution by Gauss-Jordan elimination, equation (2.1.1) above. The input matrix is a[0..n-1][0..n-1]. b[0..n-1][0..m-1] is input containing the m right-hand side vectors. On output, a is replaced by its matrix inverse, and b is replaced by the corresponding set of solution vectors.

Int i,icol,irow,j,k,l,ll, $\mathrm { n } = \mathrm { a }$ .nrows(),m=b.ncols();   
Doub big,dum,pivinv;   
VecInt indxc(n),indxr(n),ipiv(n); These integer arrays are used for bookkeeping on   
for ( $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j++) ipiv[j] ${ = } 0$ ; the pivoting.   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) { This is the main loop over the columns to be big=0.0; reduced. for (j=0;j<n;j++) This is the outer loop of the search for a pivot if (ipiv[j] $\ ! = ~ 1 \cdot$ ) element. for (k=0;k<n;k++) { if (ipiv[k] $\scriptstyle = = 0 .$ ) { if (abs(a[j][k]) $> =$ big) { big=abs(a[j][k]); irow=j; icol=k; } } }

# $^ { + + }$ (ipiv[icol]);

We now have the pivot element, so we interchange rows, if needed, to put the pivot element on the diagonal. The columns are not physically interchanged, only relabeled: indxc[i], the column of the $( \mathrm { i } + 1 ) \mathrm { t h }$ pivot element, is the $( \mathrm { i } + 1 ) \mathrm { t h }$ column that is reduced, while indxr[i] is the row in which that pivot element was originally located. If indxr[i] $\neq$ indxc[i], there is an implied column interchange. With this form of bookkeeping, the solution b’s will end up in the correct order, and the inverse matrix will be scrambled by columns.

if (irow $! =$ icol) { for $\scriptstyle 1 = 0$ ;l<n; $\beth + +$ ) SWAP(a[irow][l],a[icol][l]); for $\scriptstyle \mathbf { 1 } = 0$ ;l<m;l++) SWAP(b[irow][l],b[icol][l]);   
}   
indxr[i] $=$ irow; We are now ready to divide the pivot row by the pivot element, located at irow and icol.   
indxc[i] $=$ icol;   
if (a[icol][icol] $\mathrm { = = } \ 0 . 0$ ) throw("gaussj: Singular Matrix");   
pivinv $= 1$ .0/a[icol][icol];   
a[icol][icol] $^ { = 1 }$ .0;   
for ( $\scriptstyle 1 = 0$ ;l<n; $\beth + +$ ) a[icol][l] $\ast =$ pivinv;   
for ( $\scriptstyle 1 = 0$ ;l<m;l++) b[icol][l] $\ast =$ pivinv;   
for ( $\mathtt { 1 1 } mathtt { = 0 }$ ;ll<n;ll++) Next, we reduce the rows... if (ll ! $! =$ icol) { ...except for the pivot one, of course. dum $_ { 1 } = \mathtt { a }$ [ll][icol]; a[ll][icol] ${ = } 0$ .0; for ( $\scriptstyle 1 = 0$ ;l<n; $^ { 1 + + }$ ) a[ll][l] $- =$ a[icol][l]\*dum; for ( $\scriptstyle 1 = 0$ ;l<m; $^ { 1 + + }$ ) b[ll][l] $- =$ b[icol][l]\*dum; }

This is the end of the main loop over columns of the reduction. It only remains to unscramble the solution in view of the column interchanges. We do this by interchanging pairs of columns in the reverse order that the permutation was built up.

for (l=n-1;l>=0;l--) { if (indxr[l] $! =$ indxc[l]) for ( $\scriptstyle 1 = 0$ ;k<n;k++) SWAP(a[k][indxr[l]],a[k][indxc[l]]);   
} And we are done.

# }

void gaussj(MatDoub_IO &a)   
Overloaded version with no right-hand sides. Replaces a by its inverse.   
{ MatDoub b(a.nrows(),0); Dummy vector with zero columns. gaussj(a,b);   
}

# 2.1.3 Row versus Column Elimination Strategies

The above discussion can be amplified by a modest amount of formalism. Row operations on a matrix A correspond to pre- (that is, left-) multiplication by some simple matrix $\mathbf { R }$ . For example, the matrix $\mathbf { R }$ with components

$$
R _ { i j } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } i = j { \mathrm { ~ a n d ~ } } i \neq 2 , 4 } \\ { 1 } & { { \mathrm { i f ~ } } i = 2 , j = 4 } \\ { 1 } & { { \mathrm { i f ~ } } i = 4 , j = 2 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

effects the interchange of rows 2 and 4. Gauss-Jordan elimination by row operations alone (including the possibility of partial pivoting) consists of a series of such left-multiplications, yielding successively

$$
\begin{array} { c } { \mathbf { A } \cdot \mathbf { x } = \mathbf { b } } \\ { \left( \cdots \mathbf { R } _ { 2 } \cdot \mathbf { R } _ { 1 } \cdot \mathbf { R } _ { 0 } \cdot \mathbf { A } \right) \cdot \mathbf { x } = \cdots \mathbf { R } _ { 2 } \cdot \mathbf { R } _ { 1 } \cdot \mathbf { R } _ { 0 } \cdot \mathbf { b } } \\ { \left( \mathbf { 1 } \right) \cdot \mathbf { x } = \cdots \mathbf { R } _ { 2 } \cdot \mathbf { R } _ { 1 } \cdot \mathbf { R } _ { 0 } \cdot \mathbf { b } } \\ { \mathbf { x } = \cdots \mathbf { R } _ { 2 } \cdot \mathbf { R } _ { 1 } \cdot \mathbf { R } _ { 0 } \cdot \mathbf { b } } \end{array}
$$

The key point is that since the $\mathbf { R }$ ’s build from right to left, the right-hand side is simply transformed at each stage from one vector to another.

Column operations, on the other hand, correspond to post-, or right-, multiplications by simple matrices, call them C. The matrix in equation (2.1.5), if right-multiplied onto a matrix A, will interchange columns 2 and 4 of A. Elimination by column operations involves (conceptually) inserting a column operator, and also its inverse, between the matrix A and the

unknown vector $\mathbf { X }$ :

$$
\begin{array} { r l r } & { } & { \mathbf { A } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { \mathbf { A } \cdot \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { \mathbf { A } \cdot \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 1 } ^ { - 1 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { \mathbf { A } \cdot \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 1 } \cdot \mathbf { C } _ { 1 } ^ { - 1 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { ( \mathbf { A } \cdot \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 1 } \cdot \mathbf { C } _ { 2 } \cdot \dots ) \cdots \mathbf { C } _ { 2 } ^ { - 1 } \cdot \mathbf { C } _ { 1 } ^ { - 1 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \\ & { } & { ( \mathbf { 1 } \cdot \mathbf { \dots } \mathbf { C } _ { 2 } ^ { - 1 } \cdot \mathbf { C } _ { 1 } ^ { - 1 } \cdot \mathbf { C } _ { 0 } ^ { - 1 } \cdot \mathbf { x } = \mathbf { b } } \end{array}
$$

which (peeling off the $\mathbf { C } ^ { - 1 }$ ’s one at a time) implies a solution

$$
\mathbf { x } = \mathbf { C } _ { 0 } \cdot \mathbf { C } _ { 1 } \cdot \mathbf { C } _ { 2 } \cdot \cdot \cdot \mathbf { b }
$$

Notice the essential difference between equation (2.1.8) and equation (2.1.6). In the latter case, the $\mathbf { C }$ ’s must be applied to $\mathbf { b }$ in the reverse order from that in which they become known. That is, they must all be stored along the way. This requirement greatly reduces the usefulness of column operations, generally restricting them to simple permutations, for example in support of full pivoting.

# CITED REFERENCES AND FURTHER READING:

Wilkinson, J.H. 1965, The Algebraic Eigenvalue Problem (New York: Oxford University Press).[1]   
Carnahan, B., Luther, H.A., and Wilkes, J.O. 1969, Applied Numerical Methods (New York: Wiley), Example 5.2, p. 282.   
Bevington, P.R., and Robinson, D.K. 2002, Data Reduction and Error Analysis for the Physical Sciences, 3rd ed. (New York: McGraw-Hill),p. 247.   
Westlake, J.R. 1968, A Handbook of Numerical Matrix Inversion and Solution of Linear Equations (New York: Wiley).   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 9 . 3 – 1$ .

# 2.2 Gaussian Elimination with Backsubstitution

Any discussion of Gaussian elimination with backsubstitution is primarily pedagogical. The method stands between full elimination schemes such as Gauss-Jordan, and triangular decomposition schemes such as will be discussed in the next section. Gaussian elimination reduces a matrix not all the way to the identity matrix, but only halfway, to a matrix whose components on the diagonal and above (say) remain nontrivial. Let us now see what advantages accrue.

Suppose that in doing Gauss-Jordan elimination, as described in $\ S 2 . 1$ , we at each stage subtract away rows only below the then-current pivot element. When $a _ { 1 1 }$ is the pivot element, for example, we divide the row 1 by its value (as before), but now use the pivot row to zero only $a _ { 2 1 }$ and $a _ { 3 1 }$ , not $a _ { 0 1 }$ (see equation 2.1.1). Suppose, also, that we do only partial pivoting, never interchanging columns, so that the order of the unknowns never needs to be modified.


<!-- chunk 0002: pages 71-140 -->
Then, when we have done this for all the pivots, we will be left with a reduced equation that looks like this (in the case of a single right-hand side vector):

$$
\left[ \begin{array} { c c c c } { a _ { 0 0 } ^ { \prime } } & { a _ { 0 1 } ^ { \prime } } & { a _ { 0 2 } ^ { \prime } } & { a _ { 0 3 } ^ { \prime } } \\ { 0 } & { a _ { 1 1 } ^ { \prime } } & { a _ { 1 2 } ^ { \prime } } & { a _ { 1 3 } ^ { \prime } } \\ { 0 } & { 0 } & { a _ { 2 2 } ^ { \prime } } & { a _ { 2 3 } ^ { \prime } } \\ { 0 } & { 0 } & { 0 } & { a _ { 3 3 } ^ { \prime } } \end{array} \right] \cdot \left[ \begin{array} { c } { x _ { 0 } } \\ { x _ { 1 } } \\ { x _ { 2 } } \\ { x _ { 3 } } \end{array} \right] = \left[ \begin{array} { c } { b _ { 0 } ^ { \prime } } \\ { b _ { 1 } ^ { \prime } } \\ { b _ { 2 } ^ { \prime } } \\ { b _ { 3 } ^ { \prime } } \end{array} \right]
$$

Here the primes signify that the $a$ ’s and $b$ ’s do not have their original numerical values, but have been modified by all the row operations in the elimination to this point. The procedure up to this point is termed Gaussian elimination.

# 2.2.1 Backsubstitution

But how do we solve for the $x$ ’s? The last $x$ ( $x _ { 3 }$ in this example) is already isolated, namely

$$
x _ { 3 } = b _ { 3 } ^ { \prime } / a _ { 3 3 } ^ { \prime }
$$

With the last $x$ known we can move to the penultimate $x$ ,

$$
x _ { 2 } = \frac { 1 } { a _ { 2 2 } ^ { \prime } } [ b _ { 2 } ^ { \prime } - x _ { 3 } a _ { 2 3 } ^ { \prime } ]
$$

and then proceed with the $x$ before that one. The typical step is

$$
x _ { i } = \frac { 1 } { a _ { i i } ^ { \prime } } \biggl [ b _ { i } ^ { \prime } - \sum _ { j = i + 1 } ^ { N - 1 } a _ { i j } ^ { \prime } x _ { j } \biggr ]
$$

The procedure defined by equation (2.2.4) is called backsubstitution. The combination of Gaussian elimination and backsubstitution yields a solution to the set of equations.

The advantage of Gaussian elimination and backsubstitution over Gauss-Jordan elimination is simply that the former is faster in raw operations count: The innermost loops of Gauss-Jordan elimination, each containing one subtraction and one multiplication, are executed $N ^ { 3 }$ and $N ^ { 2 } m$ times (where there are $N$ equations and unknowns, and $m$ different right-hand sides). The corresponding loops in Gaussian elimination are executed only ${ \scriptstyle { \frac { 1 } { 3 } } } N ^ { 3 }$ times (only half the matrix is reduced, and the increasing numbers of predictable zeros reduce the count to one-third), and $\scriptstyle { \frac { 1 } { 2 } } N ^ { 2 } m$ times, respectively. Each backsubstitution of a right-hand side is ${ \frac { 1 } { 2 } } N ^ { 2 }$ executions of a similar loop (one multiplication plus one subtraction). For $m \ll N$ (only a few right-hand sides) Gaussian elimination thus has about a factor three advantage over Gauss-Jordan. (We could reduce this advantage to a factor 1.5 by not computing the inverse matrix as part of the Gauss-Jordan scheme.)

For computing the inverse matrix (which we can view as the case of $m = N$ right-hand sides, namely the $N$ unit vectors that are the columns of the identity matrix), Gaussian elimination and backsubstitution at first glance require ${ \scriptstyle { \frac { 1 } { 3 } } } N ^ { 3 }$ (matrix reduction) $+ \textstyle { \frac { 1 } { 2 } } N ^ { 3 }$ (right-hand side manipulations) $+ \textstyle { \frac { 1 } { 2 } } N ^ { 3 }$ ( $N$ backsubstitutions) $\begin{array} { r } { { \bf \Pi } = \frac { 4 } { 3 } N ^ { 3 } } \end{array}$ loop executions, which is more than the $N ^ { 3 }$ for Gauss-Jordan. However, the unit vectors are quite special in containing all zeros except for one element. If this is taken into account, the right-side manipulations can be reduced to only $\scriptstyle { \frac { 1 } { 6 } } N ^ { 3 }$ loop executions, and, for matrix inversion, the two methods have identical efficiencies.

Both Gaussian elimination and Gauss-Jordan elimination share the disadvantage that all right-hand sides must be known in advance. The $L U$ decomposition method in the next section does not share that deficiency, and also has an equally small operations count, both for solution with any number of right-hand sides and for matrix inversion.

# CITED REFERENCES AND FURTHER READING:

Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 9 . 3 – 1$ .   
Isaacson, E., and Keller, H.B. 1966, Analysis of Numerical Methods; reprinted 1994 (New York: Dover), $\ S 2 . 1$ .   
Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), $\ S 2 . 2 . 1$ .   
Westlake, J.R. 1968, A Handbook of Numerical Matrix Inversion and Solution of Linear Equations (New York: Wiley).

# 2.3 LU Decomposition and Its Applications

Suppose we are able to write the matrix A as a product of two matrices,

$$
\mathbf { L } \cdot \mathbf { U } = \mathbf { A }
$$

where $\mathbf { L }$ is lower triangular (has elements only on the diagonal and below) and U is upper triangular (has elements only on the diagonal and above). For the case of a $4 \times 4$ matrix $\mathbf { A }$ , for example, equation (2.3.1) would look like this:

$$
\left[ \begin{array} { c c c c } { \alpha _ { 0 0 } } & { 0 } & { 0 } & { 0 } \\ { \alpha _ { 1 0 } } & { \alpha _ { 1 1 } } & { 0 } & { 0 } \\ { \alpha _ { 2 0 } } & { \alpha _ { 2 1 } } & { \alpha _ { 2 2 } } & { 0 } \\ { \alpha _ { 3 0 } } & { \alpha _ { 3 1 } } & { \alpha _ { 3 2 } } & { \alpha _ { 3 3 } } \end{array} \right] \cdot \left[ \begin{array} { c c c c } { \beta _ { 0 0 } } & { \beta _ { 0 1 } } & { \beta _ { 0 2 } } & { \beta _ { 0 3 } } \\ { 0 } & { \beta _ { 1 1 } } & { \beta _ { 1 2 } } & { \beta _ { 1 3 } } \\ { 0 } & { 0 } & { \beta _ { 2 2 } } & { \beta _ { 2 3 } } \\ { 0 } & { 0 } & { 0 } & { \beta _ { 3 3 } } \end{array} \right] = \left[ \begin{array} { c c c c } { a _ { 0 0 } } & { a _ { 0 1 } } & { a _ { 0 2 } } & { a _ { 0 3 } } \\ { a _ { 1 0 } } & { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 0 } } & { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 3 0 } } & { a _ { 3 1 } } & { a _ { 3 2 } } & { a _ { 3 3 } } \end{array} \right]
$$

We can use a decomposition such as (2.3.1) to solve the linear set

$$
\mathbf { A } \cdot \mathbf { x } = ( \mathbf { L } \cdot \mathbf { U } ) \cdot \mathbf { x } = \mathbf { L } \cdot ( \mathbf { U } \cdot \mathbf { x } ) = \mathbf { b }
$$

by first solving for the vector $\mathbf { y }$ such that

$$
\mathbf { L } \cdot \mathbf { y } = \mathbf { b } 
$$

and then solving

$$
\mathbf { U } \cdot \mathbf { x } = \mathbf { y }
$$

What is the advantage of breaking up one linear set into two successive ones? The advantage is that the solution of a triangular set of equations is quite trivial, as

we have already seen in $\ S 2 . 2$ (equation 2.2.4). Thus, equation (2.3.4) can be solved by forward substitution as follows:

$$
\begin{array} { l } { { \displaystyle y _ { 0 } = \frac { b _ { 0 } } { \alpha _ { 0 0 } } } } \\ { { \displaystyle y _ { i } = \frac { 1 } { \alpha _ { i i } } \biggl [ b _ { i } - \sum _ { j = 0 } ^ { i - 1 } \alpha _ { i j } y _ { j } \biggr ] \qquad i = 1 , 2 , \ldots , N - 1 } } \end{array}
$$

while (2.3.5) can then be solved by backsubstitution exactly as in equations (2.2.2) – (2.2.4),

$$
\begin{array} { l } { { x _ { N - 1 } = \displaystyle \frac { y _ { N - 1 } } { \beta _ { N - 1 , N - 1 } } } } \\ { { x _ { i } = \displaystyle \frac { 1 } { \beta _ { i i } } \biggl [ y _ { i } - \sum _ { j = i + 1 } ^ { N - 1 } \beta _ { i j } x _ { j } \biggr ] \qquad i = N - 2 , N - 3 , \ldots , 0 } } \end{array}
$$

Equations (2.3.6) and (2.3.7) total (for each right-hand side $\mathbf { b }$ ) $N ^ { 2 }$ executions of an inner loop containing one multiply and one add. If we have $N$ right-hand sides that are the unit column vectors (which is the case when we are inverting a matrix), then taking into account the leading zeros reduces the total execution count of (2.3.6) from ${ \scriptstyle { \frac { 1 } { 2 } } } N ^ { 3 }$ to $\scriptstyle { \frac { 1 } { 6 } } N ^ { 3 }$ , while (2.3.7) is unchanged at ${ \scriptstyle { \frac { 1 } { 2 } } } N ^ { 3 }$ .

Notice that, once we have the $L U$ decomposition of A, we can solve with as many right-hand sides as we then care to, one at a time. This is a distinct advantage over the methods of $\ S 2 . 1$ and $\ S 2 . 2$ .

# 2.3.1 Performing the LU Decomposition

How then can we solve for $\mathbf { L }$ and $\mathbf { U }$ , given A? First, we write out the $i , j$ th component of equation (2.3.1) or (2.3.2). That component always is a sum beginning with

$$
\alpha _ { i 0 } \beta _ { 0 j } + \dots = a _ { i j }
$$

The number of terms in the sum depends, however, on whether $i$ or $j$ is the smaller number. We have, in fact, the three cases,

$$
\begin{array} { c c c } { i < j : } & { } & { \alpha _ { i 0 } \beta _ { 0 j } + \alpha _ { i 1 } \beta _ { 1 j } + \cdots + \alpha _ { i i } \beta _ { i j } = a _ { i j } } \\ { i = j : } & { } & { \alpha _ { i 0 } \beta _ { 0 j } + \alpha _ { i 1 } \beta _ { 1 j } + \cdots + \alpha _ { i i } \beta _ { j j } = a _ { i j } } \\ { i > j : } & { } & { \alpha _ { i 0 } \beta _ { 0 j } + \alpha _ { i 1 } \beta _ { 1 j } + \cdots + \alpha _ { i j } \beta _ { j j } = a _ { i j } } \end{array}
$$

Equations $( 2 . 3 . 8 ) - ( 2 . 3 . 1 0 )$ total $N ^ { 2 }$ equations for the $N ^ { 2 } + N$ unknown $\alpha$ ’s and $\beta$ ’s (the diagonal being represented twice). Since the number of unknowns is greater than the number of equations, we are invited to specify $N$ of the unknowns arbitrarily and then try to solve for the others. In fact, as we shall see, it is always possible to take

$$
\alpha _ { i i } \equiv 1 \qquad i = 0 , \ldots , N - 1
$$

A surprising procedure, now, is Crout’s algorithm, which quite trivially solves the set of $N ^ { 2 } + N$ equations (2.3.8) – (2.3.11) for all the $\alpha$ ’s and $\beta$ ’s by just arranging the equations in a certain order! That order is as follows:

- Set $\alpha _ { i i } = 1 , i = 0 , \ldots , N - 1$ (equation 2.3.11).

- For each $j ~ = ~ 0 , 1 , 2 , \dots , N - 1$ do these two procedures: First, for $i \ =$ $0 , 1 , \ldots , j$ , use (2.3.8), (2.3.9), and (2.3.11) to solve for $\beta _ { i j }$ , namely

$$
\beta _ { i j } = a _ { i j } - \sum _ { k = 0 } ^ { i - 1 } \alpha _ { i k } \beta _ { k j }
$$

(When $i = 0$ in 2.3.12 the summation term is taken to mean zero.) Second, for $i = j + 1 , j + 2 , \dots , N - 1$ use (2.3.10) to solve for $\alpha _ { i j }$ , namely

$$
\alpha _ { i j } = \frac { 1 } { \beta _ { j j } } \left( a _ { i j } - \sum _ { k = 0 } ^ { j - 1 } \alpha _ { i k } \beta _ { k j } \right)
$$

Be sure to do both procedures before going on to the next $j$ .

If you work through a few iterations of the above procedure, you will see that the $\alpha$ ’s and $\beta$ ’s that occur on the right-hand side of equations (2.3.12) and (2.3.13) are already determined by the time they are needed. You will also see that every $a _ { i j }$ is used only once and never again. This means that the corresponding $\alpha _ { i j }$ or $\beta _ { i j }$ can be stored in the location that the $a$ used to occupy: the decomposition is “in place.” [The diagonal unity elements $\alpha _ { i i }$ (equation 2.3.11) are not stored at all.] In brief, Crout’s method fills in the combined matrix of $\alpha$ ’s and $\beta$ ’s,

$$
\left[ { \begin{array} { l l l l } { \beta _ { 0 0 } } & { \beta _ { 0 1 } } & { \beta _ { 0 2 } } & { \beta _ { 0 3 } } \\ { \alpha _ { 1 0 } } & { \beta _ { 1 1 } } & { \beta _ { 1 2 } } & { \beta _ { 1 3 } } \\ { \alpha _ { 2 0 } } & { \alpha _ { 2 1 } } & { \beta _ { 2 2 } } & { \beta _ { 2 3 } } \\ { \alpha _ { 3 0 } } & { \alpha _ { 3 1 } } & { \alpha _ { 3 2 } } & { \beta _ { 3 3 } } \end{array} } \right]
$$

by columns from left to right, and within each column from top to bottom (see Figure 2.3.1).

What about pivoting? Pivoting (i.e., selection of a salubrious pivot element for the division in equation 2.3.13) is absolutely essential for the stability of Crout’s method. Only partial pivoting (interchange of rows) can be implemented efficiently. However this is enough to make the method stable. This means, incidentally, that we don’t actually decompose the matrix A into $L U$ form, but rather we decompose a rowwise permutation of A. (If we keep track of what that permutation is, this decomposition is just as useful as the original one would have been.)

Pivoting is slightly subtle in Crout’s algorithm. The key point to notice is that equation (2.3.12) in the case of $i \ : = \ : j$ (its final application) is exactly the same as equation (2.3.13) except for the division in the latter equation; in both cases the upper limit of the sum is $k = j - 1 ( = i - 1 )$ . This means that we don’t have to commit ourselves as to whether the diagonal element $\beta _ { j j }$ is the one that happens to fall on the diagonal in the first instance, or whether one of the (undivided) $\alpha _ { i j }$ ’s below it in the column, $i = j + 1 , \dotsc , N - 1$ , is to be “promoted” to become the diagonal $\beta$ . This can be decided after all the candidates in the column are in hand. As you should be able to guess by now, we will choose the largest one as the diagonal $\beta$ (pivot element), and then do all the divisions by that element en masse. This is Crout’s method with partial pivoting. Our implementation has one additional wrinkle: It initially finds the largest element in each row, and subsequently (when it is looking for the maximal pivot element) scales the comparison as if we had initially scaled all the equations to make their maximum coefficient equal to unity; this is the implicit pivoting mentioned in $\ S 2 . 1$ .

![](images/8d24f701b5de9206402bda68303ba691f102e90b603dad44e498bdc4b9957833.jpg)  
Figure 2.3.1. Crout’s algorithm for $_ { L U }$ decomposition of a matrix. Elements of the original matrix are modified in the order indicated by lowercase letters: a, b, c, etc. Shaded boxes show the previously modified elements that are used in modifying two typical elements, each indicated by an $\mathbf { \ddot { x } } ^ { , , }$ .

The inner loop of the $L U$ decomposition, equations (2.3.12) and (2.3.13), resembles the inner loop of matrix multiplication. There is a triple loop over the indices $i$ , $j$ , and $k$ . There are six permutations of the order in which these loops can be done. The straightforward implementation of Crout’s algorithm corresponds to the $j i k$ permutation, where the order of the indices is the order of the loops from outermost to innermost. On modern processors with a hierarchy of cache memory, and when matrices are stored by rows, the fastest execution time is usually the $k i j$ or $i k j$ ordering. Pivoting is easier with $k i j$ ordering, so that is the implementation we use. This is called “outer product Gaussian elimination” by Golub and Van Loan [1].

$L U$ decomposition is well suited for implementation as an object (a class or struct). The constructor performs the decomposition, and the object itself stores the result. Then, a method for forward- and backsubstitution can be called once, or many times, to solve for one or more right-hand sides. Methods for additional functionality are also easy to include. The object’s declaration looks like this:

# struct LUdcmp

Object for solving linear equations $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ using $_ { L U }$ decomposition, and related functions. {

Int n; MatDoub lu; VecInt indx; Doub d; LUdcmp(MatDoub_I &a); void solve(VecDoub_I &b, VecDoub_O &x); void solve(MatDoub_I &b, MatDoub_O &x); void inverse(MatDoub_O &ainv); Doub det(); void mprove(VecDoub_I &b, VecDoub_IO &x) MatDoub_I &aref; };

Stores the decomposition.   
Stores the permutation.   
Used by det.   
Constructor. Argument is the matrix A.   
Solve for a single right-hand side.   
Solve for multiple right-hand sides.   
Calculate matrix inverse ${ \bf A } ^ { - 1 }$ .   
Return determinant of A.   
Discussed in $\ S 2 . 5$ .   
Used only by mprove.

Here is the implementation of the constructor, whose argument is the input matrix that is to be $L U$ decomposed. The input matrix is not altered; a copy is made, on which outer product Gaussian elimination is then done in-place.

# LUdcmp::LUdcmp(MatDoub_I &a) : n(a.nrows()), lu(a), aref(a), indx(n) {

Given a matrix $\mathbf { a } \left[ 0 \cdot \mathbf { \mathtt { n } } \mathbf { - } 1 \right] \left[ 0 \cdot \mathbf { \mathtt { n } } \mathbf { - } 1 \right]$ , this routine replaces it by the $_ { L U }$ decomposition of a rowwise permutation of itself. a is input. On output, it is arranged as in equation (2.3.14) above; indx $\left[ 0 \ldots \mathbf { n } \mathbf { - } 1 \right]$ is an output vector that records the row permutation effected by the partial pivoting; d is output as $\pm 1$ depending on whether the number of row interchanges was even or odd, respectively. This routine is used in combination with solve to solve linear equations or invert a matrix.

const Doub TINY $\sp { \prime } = 1$ .0e-40; A small number.   
Int i,imax,j,k;   
Doub big,temp;   
VecDoub vv(n); vv stores the implicit scaling of each row.   
$\mathtt { d } \mathtt { = } 1$ .0; No row interchanges yet.   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) { Loop over rows to get the implicit scaling inforbig=0.0; mation. for (j=0;j<n;j++) if ((temp=abs(lu[i][j])) $>$ big) big=temp; if (big $\scriptstyle = = \ 0 . 0 { \mathrm { . } }$ ) throw("Singular matrix in LUdcmp"); No nonzero largest element. vv[i] $= 1$ .0/big; Save the scaling.   
}   
for (k=0;k<n;k++) { This is the outermost kij loop. big=0.0; Initialize for the search for largest pivot element. for (i=k;i<n;i++) { temp=vv[i]\*abs(lu[i][k]); if (temp $>$ big) { Is the figure of merit for the pivot better than big=temp; the best so far? imax=i; } } if (k != imax) { Do we need to interchange rows? for (j=0;j<n;j++) { Yes, do so... temp=lu[imax][j]; lu[imax][j] $=$ lu[k][j]; lu[k][j] $=$ temp; } $\mathrm { ~ d ~ } = \mathrm { ~ - d ~ }$ ; ...and change the parity of d. vv[imax]=vv[k]; Also interchange the scale factor. } indx[k] $=$ imax; if (lu[k][k] $= = \ 0 . 0$ ) lu[k][k] $= ^ { \prime }$ TINY; If the pivot element is zero, the matrix is singular (at least to the precision of the algorithm). For some applications on singular matrices, it is desirable to substitute

TINY for zero.

for ( $\dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi } \dot { \bf \Phi }$ ;i<n;i++) { temp=lu[i][k] $/ { = }$ lu[k][k]; Divide by the pivot element. for (j=k+1;j<n;j++) Innermost loop: reduce remaining submatrix. lu[i][j] $- =$ temp\*lu[k][j]; } }

Once the LUdcmp object is constructed, two functions implementing equations (2.3.6) and (2.3.7) are available for solving linear equations. The first solves a single right-hand side vector $\mathbf { b }$ for a solution vector $\mathbf { X }$ . The second simultaneously solves multiple right-hand vectors, arranged as the columns of a matrix B. In other words, it calculates the matrix $\mathbf { A } ^ { - 1 } \cdot \mathbf { B }$ .

# void LUdcmp::solve(VecDoub_I &b, VecDoub_O $\& \mathbf { x }$ )

Solves the set of n linear equations $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ using the stored $_ { L U }$ decomposition of A. b[0..n-1] is input as the right-hand side vector $\mathbf { b }$ , while $\mathbf { x }$ returns the solution vector $\mathbf { x }$ ; b and x may reference the same vector, in which case the solution overwrites the input. This routine takes into account the possibility that b will begin with many zero elements, so it is efficient for use in matrix inversion.

Int i,ii ${ = } 0$ ,ip,j; Doub sum; if (b.size() $\mathbf { \omega } _ { ! } = \mathbf { \omega } _ { \mathrm { ~ n ~ } }$ || x.size() $\ ! = { \mathrm { ~ \bf ~ n ~ } } ,$ throw("LUdcmp::solve bad sizes"); for ( $\scriptstyle \dot { 1 } = 0$ ;i<n; $\dot { \bar { \lambda } } + +$ ) x[i] $=$ b[i]; for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { When ii is set to a positive value, it will become the ip=indx[i]; index of the first nonvanishing element of b. We now sum=x[ip]; do the forward substitution, equation (2.3.6). The x[ip] $= \tt x$ [i]; only new wrinkle is to unscramble the permutation if (ii $\iota = \ 0$ ) as we go. for (j=ii-1;j<i;j++) sum $- =$ lu[i][j]\*x[j]; else if (sum ! $\downarrow =$ 0.0) A nonzero element was encountered, so from now on we $\dot { 1 } \dot { 2 } = \dot { 1 } + 1$ ; will have to do the sums in the loop above. x[i] $=$ sum; } for (i=n-1;i>=0;i--) { Now we do the backsubstitution, equation (2.3.7). sum $= \mathbf { x }$ [i]; for ( $ \scriptstyle { \dot { \mathcal { I } } } = { \dot { \bar { \mathsf { 1 } } } } + { \bar { \mathsf { 1 } } }$ ;j<n;j++) sum $- =$ lu[i][j]\*x[j]; x[i] $=$ sum/lu[i][i]; Store a component of the solution vector $X$ . } All done! }

# void LUdcmp::solve(MatDoub_I &b, MatDoub_O $\operatorname { \& } \operatorname  \mathrm { . }$ )

Solves m sets of n linear equations $\mathbf { A \cdot X } = \mathbf { B }$ using the stored $_ { L U }$ decomposition of A. The matrix b[0..n-1][0..m-1] inputs the right-hand sides, while $\mathbf { x } \left[ 0 \ldots \mathtt { n - 1 } \right] \left[ 0 \ldots \mathtt { m - 1 } \right]$ returns the solution ${ \bf A } ^ { - 1 }$  B. b and $\mathbf { x }$ may reference the same matrix, in which case the solution overwrites the input.

int i,j, $\mathtt { m } = \mathtt { b }$ .ncols();   
if (b.nrows() $! = \mathrm { ~ n ~ }$ || x.nrows() $\ ! = { \textbf { n } }$ || b.ncols() != x.ncols()) throw("LUdcmp::solve bad sizes");   
VecDoub xx(n);   
for $( \ j = 0$ ;j<m;j $^ { + + }$ ) { Copy and solve each column in turn. for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i $\cdot ^ { + + }$ ) xx[i] $=$ b[i][j]; solve(xx,xx); for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) x[i][j] $=$ xx[i];   
}

The $L U$ decomposition in LUdcmp requires about ${ \scriptstyle { \frac { 1 } { 3 } } } N ^ { 3 }$ executions of the inner loops (each with one multiply and one add). This is thus the operation count for solving one (or a few) right-hand sides, and is a factor of 3 better than the Gauss-Jordan routine gaussj that was given in $\ S 2 . 1$ , and a factor of 1.5 better than a Gauss-Jordan routine (not given) that does not compute the inverse matrix. For inverting a matrix, the total count (including the forward- and backsubstitution as discussed following equation 2.3.7 above) is $\begin{array} { r } { ( \frac { 1 } { 3 } + \frac { 1 } { 6 } + \frac { 1 } { 2 } ) N ^ { 3 } = N ^ { 3 } } \end{array}$ , the same as gaussj.

To summarize, this is the preferred way to solve the linear set of equations $\mathbf { A \cdot x } = \mathbf { b }$ :

const Int $\mathrm { ~ n ~ } = \mathrm { ~ . ~ . ~ }$ MatDoub $\mathtt { a } ( \mathtt { n } , \mathtt { n } )$ ;   
VecDoub b(n),x(n);   
LUdcmp alu(a);   
alu.solve(b,x);

The answer will be given back in x. Your original matrix a and vector b are not altered. If you need to recover the storage in the object alu, then start a temporary scope with “{” before alu is declared, and end that scope with $\mathbf { \ddot { y } } , \mathbf { \vec { \tau } }$ when you want alu to be destroyed.

If you subsequently want to solve a set of equations with the same A but a different right-hand side b, you repeat only

alu.solve(b,x);

# 2.3.2 Inverse of a Matrix

LUdcmp has a member function that gives the inverse of the matrix A. Simply, it creates an identity matrix and then invokes the appropriate solve method.

void LUdcmp::inverse(MatDoub_O &ainv)   
Using the stored $_ { L U }$ decomposition, return in ainv the matrix inverse ${ \bf A } ^ { - 1 }$ . {   
Int i,j;   
ainv.resize(n,n);   
for $\scriptstyle \dot { 1 } = 0$ ;i<n; $\dot { 1 } + +$ ) { for (j=0;j<n;j++) ainv[i][j] = 0.; ainv[i][i] = 1.;   
7   
solve(ainv,ainv);

The matrix ainv will now contain the inverse of the original matrix a. Alternatively, there is nothing wrong with using a Gauss-Jordan routine like gaussj (-2.1) to invert a matrix in place, destroying the original. Both methods have practically the same operations count.

# 2.3.3 Determinant of a Matrix

The determinant of an $L U$ decomposed matrix is just the product of the diagonal elements,

$$
\mathrm { d e t } = \prod _ { j = 0 } ^ { N - 1 } \beta _ { j j }
$$

We don’t, recall, compute the decomposition of the original matrix, but rather a decomposition of a rowwise permutation of it. Luckily, we have kept track of whether the number of row interchanges was even or odd, so we just preface the product by the corresponding sign. (You now finally know the purpose of d in the LUdcmp structure.)

# Doub LUdcmp::det()

Using the stored $_ { L U }$ decomposition, return the determinant of the matrix A.

Doub dd $\qquad = \ \mathrm { ~ d ~ }$ ;   
for (Int i=0;i<n; $\mathbf { i } + + \mathbf { i }$ ) dd \*= lu[i][i];   
return dd;

# }

For a matrix of any substantial size, it is quite likely that the determinant will overflow or underflow your computer’s floating-point dynamic range. In such a case you can easily add another member function that, e.g., divides by powers of ten, to keep track of the scale separately, or, e.g., accumulates the sum of logarithms of the absolute values of the factors and the sign separately.

# 2.3.4 Complex Systems of Equations

If your matrix A is real, but the right-hand side vector is complex, say $\mathbf { b } + i \mathbf { d }$ , then (i) $L U$ decompose A in the usual way, (ii) backsubstitute $\mathbf { b }$ to get the real part of the solution vector, and (iii) backsubstitute $\mathbf { d }$ to get the imaginary part of the solution vector.

If the matrix itself is complex, so that you want to solve the system

$$
( \mathbf { A } + i \mathbf { C } ) \cdot ( \mathbf { x } + i \mathbf { y } ) = ( \mathbf { b } + i \mathbf { d } )
$$

then there are two possible ways to proceed. The best way is to rewrite LUdcmp with complex routines. Complex modulus substitutes for absolute value in the construction of the scaling vector vv and in the search for the largest pivot elements. Everything else goes through in the obvious way, with complex arithmetic used as needed.

A quick-and-dirty way to solve complex systems is to take the real and imaginary parts of (2.3.16), giving

$$
\begin{array} { r } { \mathbf { A \cdot x } - \mathbf { C } \cdot \mathbf { y } = \mathbf { b } } \\ { \mathbf { C } \cdot \mathbf { x } + \mathbf { A } \cdot \mathbf { y } = \mathbf { d } } \end{array}
$$

which can be written as a $2 N \times 2 N$ set of real equations,

$$
\left( { \begin{array} { c c } { \mathbf { A } } & { - \mathbf { C } } \\ { \mathbf { C } } & { \mathbf { A } } \end{array} } \right) \cdot \left( { \begin{array} { l } { \mathbf { x } } \\ { \mathbf { y } } \end{array} } \right) = \left( { \begin{array} { l } { \mathbf { b } } \\ { \mathbf { d } } \end{array} } \right)
$$

and then solved with LUdcmp’s routines in their present forms. This scheme is a factor of 2 inefficient in storage, since $\mathbf { A }$ and $\mathbf { C }$ are stored twice. It is also a factor of 2 inefficient in time, since the complex multiplies in a complexified version of the routines would each use 4 real multiplies, while the solution of a $2 N \times 2 N$ problem involves 8 times the work of an $N \times N$ one. If you can tolerate these factor-of-two inefficiencies, then equation (2.3.18) is an easy way to proceed.

# CITED REFERENCES AND FURTHER READING:

Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), Chapter 4.[1]

Anderson, E., et al. 1999, LAPACK User’s Guide, 3rd ed. (Philadelphia: S.I.A.M.). Online with software at $^ { 2 0 0 7 + }$ , http://www.netlib.org/lapack.   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 3 . 3$ , and p. 50.   
Forsythe, G.E., and Moler, C.B. 1967, Computer Solution of Linear Algebraic Systems (Englewood Cliffs, NJ: Prentice-Hall), Chapters 9, 16, and 18.   
Westlake, J.R. 1968, A Handbook of Numerical Matrix Inversion and Solution of Linear Equations (New York: Wiley).   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 4 . 1$ .   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 9 . 1 1$ .   
Horn, R.A., and Johnson, C.R. 1985, Matrix Analysis (Cambridge: Cambridge University Press).

# 2.4 Tridiagonal and Band-Diagonal Systems of Equations

The special case of a system of linear equations that is tridiagonal, that is, has nonzero elements only on the diagonal plus or minus one column, is one that occurs frequently. Also common are systems that are band-diagonal, with nonzero elements only along a few diagonal lines adjacent to the main diagonal (above and below).

For tridiagonal sets, the procedures of $L U$ decomposition, forward- and backsubstitution each take only $O ( N )$ operations, and the whole solution can be encoded very concisely. The resulting routine tridag is one that we will use in later chapters.

Naturally, one does not reserve storage for the full $N \times N$ matrix, but only for the nonzero components, stored as three vectors. The set of equations to be solved is

$$
\left[ \begin{array} { l l l l l } { b _ { 0 ~ } } & { c _ { 0 ~ } } & { 0 } & { \cdots } & & \\ { a _ { 1 ~ } } & { b _ { 1 ~ } } & { c _ { 1 ~ } } & { \cdots } & & \\ & & { \cdots } & & & \\ & & { \cdots } & { a _ { N - 2 ~ } } & { b _ { N - 2 ~ } } & { c _ { N - 2 } } \\ & & { \cdots } & { 0 } & { a _ { N - 1 } } & { b _ { N - 1 } } \end{array} \right] \cdot \left[ \begin{array} { l } { u _ { 0 ~ } } \\ { u _ { 1 ~ } } \\ { \cdots } \\ { u _ { N - 2 } } \\ { u _ { N - 1 } } \end{array} \right] = \left[ \begin{array} { l } { r _ { 0 ~ } } \\ { r _ { 1 ~ } } \\ { \cdots } \\ { r _ { N - 2 } } \\ { r _ { N - 1 } } \end{array} \right]
$$

Notice that $a _ { 0 }$ and $c _ { N - 1 }$ are undefined and are not referenced by the routine that follows.

void tridag(VecDoub_I &a, VecDoub_I &b, VecDoub_I &c, VecDoub_I &r, VecDoub_O &u) Solves for a vector $\mathbf { u } \left[ 0 \ldots \ldots \right]$ the tridiagonal linear set given by equation (2.4.1). a $\left[ 0 \cdot \cdot \mathbf { n } ^ { - 1 } \right]$ , b[0..n-1], c[0..n-1], and $\mathbf { r } \left[ 0 \ldots \mathbf { n - 1 } \right]$ are input vectors and are not modified.

Int j, $\mathrm { n } = \mathrm { a }$ .size();   
Doub bet;   
VecDoub gam(n); One vector of workspace, gam, is needed.   
if (b[0] $= = \ 0 . 0$ ) throw("Error 1 in tridag");   
If this happens, then you should rewrite your equations as a set of order $N - 1$ , with $u _ { 1 }$   
trivially eliminated.   
u[0] $= \mathbf { r }$ [0]/(bet $\mathtt { \Gamma } = \mathtt { b }$ [0]);   
for $\scriptstyle \dot { \mathcal { I } } = 1$ ;j<n;j++) { Decomposition and forward substitution. gam[j] $= _ { \tt C }$ [j-1]/bet; bet $= \mathrm { b }$ [j]-a[j]\*gam[j]; if (bet $\scriptstyle = = \ 0 . 0$ ) throw("Error 2 in tridag"); u[j] $=$ (r[j]-a[j]\*u[j-1])/bet;   
}   
for ${ \bf \rho } ( { \bf j } = ( { \bf n } - 2 )$ ; $\scriptstyle { \dot { \mathsf { J } } } > = 0$ ;j--) u[j] $-- = \mathrm { g a m [ j + 1 ] * _ { U } }$ [j+1]; Backsubstitution.

There is no pivoting in tridag. It is for this reason that tridag can fail even when the underlying matrix is nonsingular: A zero pivot can be encountered even for a nonsingular matrix. In practice, this is not something to lose sleep about. The kinds of problems that lead to tridiagonal linear sets usually have additional properties which guarantee that the algorithm in tridag will succeed. For example, if

$$
\left| b _ { j } \right| > \left| a _ { j } \right| + \left| c _ { j } \right| \qquad j = 0 , \ldots , N - 1
$$

(called diagonal dominance), then it can be shown that the algorithm cannot encounter a zero pivot.

It is possible to construct special examples in which the lack of pivoting in the algorithm causes numerical instability. In practice, however, such instability is almost never encountered — unlike the general matrix problem where pivoting is essential.

The tridiagonal algorithm is the rare case of an algorithm that, in practice, is more robust than theory says it should be. Of course, should you ever encounter a problem for which tridag fails, you can instead use the more general method for band-diagonal systems, described below (the Bandec object).

Some other matrix forms consisting of tridiagonal with a small number of additional elements (e.g., upper right and lower left corners) also allow rapid solution; see $\ S 2 . 7$ .

# 2.4.1 Parallel Solution of Tridiagonal Systems

It is possible to solve tridiagonal systems doing many of the operations in parallel. We illustrate by the special case with $N = 7$ :

$$
\left[ \begin{array} { l l l l l l l } { b _ { 0 ~ } } & { c _ { 0 ~ } } & & & & & \\ { a _ { 1 ~ } } & { b _ { 1 ~ } } & { c _ { 1 ~ } } & & & & \\ & { a _ { 2 ~ } } & { b _ { 2 ~ } } & { c _ { 2 ~ } } & & & \\ & & { a _ { 3 ~ } } & { b _ { 3 ~ } } & { c _ { 3 ~ } } & & \\ & & & { a _ { 4 ~ } } & { b _ { 4 ~ } } & { c _ { 4 ~ } } & \\ & & & & { a _ { 5 ~ } } & { b _ { 5 ~ } } & { c _ { 5 ~ } } \\ & & & & & & { a _ { 6 ~ } } &  b _ { 6 ~ } \end{array} \right] \cdot \left[ \begin{array} { l } { u _ { 0 ~ } } \\ { u _ { 1 ~ } } \\ { u _ { 2 ~ } } \\ { u _ { 3 ~ } } \\ { u _ { 4 ~ } } \\ { u _ { 5 ~ } } \\ { u _ { 6 ~ } } \end{array} \right] = \left[ \begin{array} { l } { r _ { 0 ~ } } \\ { r _ { 1 ~ } } \\ { r _ { 2 ~ } } \\ { r _ { 3 ~ } } \\ { r _ { 4 ~ } } \\ { r _ { 5 ~ } } \\ { r _ { 6 ~ } } \end{array} \right]
$$

The basic idea is to partition the problem into even and odd elements, recurse to solve the latter, and then solve the former in parallel. Specifically, we first rewrite equation (2.4.3) by permuting its rows and columns,

$$
\left[ \begin{array} { l l l l l l l } { b _ { 0 ~ } } & & & & { c _ { 0 ~ } } & & \\ & { b _ { 2 ~ } } & & & { a _ { 2 ~ } } & { c _ { 2 ~ } } & \\ & & { b _ { 4 ~ } } & & & & { a _ { 4 ~ } } & { c _ { 4 ~ } } \\ { a _ { 1 ~ } } & { c _ { 1 ~ } } & & { b _ { 6 ~ } } & & { b _ { 1 ~ } } & \\ & { a _ { 3 ~ } } & { c _ { 3 ~ } } & & & & { b _ { 3 ~ } } \\ & & & { a _ { 5 ~ } } & { c _ { 5 ~ } } & & & { b _ { 5 } } \end{array} \right] \cdot \left[ \begin{array} { l } { u _ { 0 ~ } } \\ { u _ { 2 ~ } } \\ { u _ { 4 ~ } } \\ { u _ { 6 ~ } } \\ { u _ { 1 ~ } } \\ { u _ { 3 ~ } } \\ { u _ { 5 ~ } } \end{array} \right] = \left[ \begin{array} { l } { r _ { 0 ~ } } \\ { r _ { 2 ~ } } \\ { r _ { 4 ~ } } \\ { r _ { 6 ~ } } \\ { r _ { 1 ~ } } \\ { r _ { 3 ~ } } \\ { r _ { 5 ~ } } \end{array} \right]
$$

Now observe that, by row operations that subtract multiples of the first four rows from each of the last three rows, we can eliminate all nonzero elements in the lower-left quadrant. The price we pay is bringing some new elements into the lower-right quadrant, whose

nonzero elements we now call $x$ ’s, $y$ ’s, and $z$ ’s. We call the modified right-hand sides $q$ . The transformed problem is now

$$
\begin{array} { r } { \left[ \begin{array} { l l l l l l l l } { b _ { 0 } } & & & & { c _ { 0 } } & & & \\ & { b _ { 2 } } & & & & { a _ { 2 } } & { c _ { 2 } } & \\ & & { b _ { 4 } } & & & & & { a _ { 4 } } & { c _ { 4 } } \\ & & & { b _ { 6 } } & & & & { a _ { 6 } } \\ & & & & { y _ { 0 } } & & { z _ { 0 } } & \\ & & & & { x _ { 1 } } & { y _ { 1 } } & { z _ { 1 } } \\ & & & & & & { x _ { 2 } } & { y _ { 2 } } \end{array} \right] \cdot \left[ \begin{array} { l } { u _ { 0 } } \\ { u _ { 2 } } \\ { u _ { 4 } } \\ { u _ { 6 } } \\ { u _ { 1 } } \\ { u _ { 3 } } \\ { u _ { 5 } } \\ { u _ { 5 } } \end{array} \right] = \left[ \begin{array} { l } { r _ { 0 } } \\ { r _ { 2 } } \\ { r _ { 4 } } \\ { r _ { 6 } } \\ { q _ { 0 } } \\ { q _ { 1 } } \\ { q _ { 2 } } \end{array} \right] } \end{array}
$$

Notice that the last three rows form a new, smaller, tridiagonal problem, which we can solve simply by recursing. Once its solution is known, the first four rows can be solved by a simple, parallelizable, substitution. For discussion of this and related methods for parallelizing tridiagonal systems, and references to the literature, see [2].

# 2.4.2 Band-Diagonal Systems

Where tridiagonal systems have nonzero elements only on the diagonal plus or minus one, band-diagonal systems are slightly more general and have (say) $m _ { 1 } \geq 0$ nonzero elements immediately to the left of (below) the diagonal and $m _ { 2 } \geq 0$ nonzero elements immediately to its right (above it). Of course, this is only a useful classification if $m _ { 1 }$ and $m _ { 2 }$ are both $\ll N$ . In that case, the solution of the linear system by $L U$ decomposition can be accomplished much faster, and in much less storage, than for the general $N \times N$ case.

The precise definition of a band-diagonal matrix with elements $a _ { i j }$ is that

$$
a _ { i j } = 0 \quad \mathrm { w h e n } \quad j > i + m _ { 2 } \quad \mathrm { o r } \quad i > j + m _ { 1 }
$$

Band-diagonal matrices are stored and manipulated in a so-called compact form, which results if the matrix is tilted $4 5 ^ { \circ }$ clockwise, so that its nonzero elements lie in a long, narrow matrix with $m _ { 1 } + 1 + m _ { 2 }$ columns and $N$ rows. This is best illustrated by an example: The banddiagonal matrix

$$
\left( \begin{array} { c c c c c c c c } { 3 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 4 } & { 1 } & { 5 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 9 } & { 2 } & { 6 } & { 5 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 3 } & { 5 } & { 8 } & { 9 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 7 } & { 9 } & { 3 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 3 } & { 8 } & { 4 } & { 6 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 2 } & { 4 } & { 4 } \end{array} \right)
$$

which has $N = 7 , m _ { 1 } = 2$ , and $m _ { 2 } = 1$ , is stored compactly as the $7 \times 4$ matrix,

$$
\left( { \begin{array} { c c c c } { x } & { x } & { 3 } & { 1 } \\ { x } & { 4 } & { 1 } & { 5 } \\ { 9 } & { 2 } & { 6 } & { 5 } \\ { 3 } & { 5 } & { 8 } & { 9 } \\ { 7 } & { 9 } & { 3 } & { 2 } \\ { 3 } & { 8 } & { 4 } & { 6 } \\ { 2 } & { 4 } & { 4 } & { x } \end{array} } \right)
$$

Here $x$ denotes elements that are wasted space in the compact format; these will not be referenced by any manipulations and can have arbitrary values. Notice that the diagonal of the original matrix appears in column $m _ { 1 }$ , with subdiagonal elements to its left and superdiagonal elements to its right.

The simplest manipulation of a band-diagonal matrix, stored compactly, is to multiply it by a vector to its right. Although this is algorithmically trivial, you might want to study the following routine as an example of how to pull nonzero elements $a _ { i j }$ out of the compact storage format in an orderly fashion.

void banmul(MatDoub_I &a, const Int m1, const Int m2, VecDoub_I &x, VecDoub_O &b)

Matrix multiply $\mathbf { b } = \mathbf { A } \cdot \mathbf { x }$ , where $\mathbf { A }$ is band-diagonal with m1 rows below the diagonal and $\mathtt { m 2 }$ rows above. The input vector is $\mathbf { x } \left[ 0 \ldots \ldots \right] $ and the output vector is $\mathtt { b } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ . The array $\mathtt { a } [ 0 . . . . 1 . . 1 ] [ 0 . . . . 1 + \mathtt { m } 2 ]$ stores A as follows: The diagonal elements are in $\mathbf { a } \left[ 0 \ldots \mathbf { n - 1 } \right] \left[ \mathbf { m 1 } \right]$ . Subdiagonal elements are in $\mathbf { a } \left[ j \cdot \cdot \cdot \mathbf { n - 1 } \right] \left[ 0 \cdot \cdot \cdot \cdot 1 \right] -$ with $j > 0$ appropriate to the number of elements on each subdiagonal. Superdiagonal elements are in $\mathtt { a } [ 0 \dots j ] [ \mathtt { m } 1 + 1 \dots \mathtt { m } 1 + \mathtt { m } 2 ]$ with $j < \mathtt { n } \mathtt { - } 1$ appropriate to the number of elements on each superdiagonal.

Int i,j,k,tmploop, $\mathtt { n } = \mathtt { a }$ .nrows();   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { $\mathtt { k } = \mathtt { i } - \mathtt { m } 1$ ; tmploop=MIN(m1+m2+1,Int(n-k)); b[i] ${ = } 0$ .0; for (j=MAX(0,-k);j<tmploop; $\mathrm { j } + +$ ) b[i] $+ =$ a[i][j]\*x[j+k];   
}

It is not possible to store the $L U$ decomposition of a band-diagonal matrix A quite as compactly as the compact form of A itself. The decomposition (essentially by Crout’s method; see $\ S 2 . 3 )$ produces additional nonzero “fill-ins.” One straightforward storage scheme is to store the upper triangular factor $( U )$ in a space with the same shape as A, and to store the lower triangular factor $( L )$ in a separate compact matrix of size $N \times m _ { 1 }$ . The diagonal elements of $U$ (whose product, times $\mathsf { d } = \pm 1$ , gives the determinant) are in the first column of $U$ .

Here is an object, analogous to LUdcmp in $\ S 2 . 3$ , for solving band-diagonal linear equations:

# struct Bandec {

Object for solving linear equations $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ for a band-diagonal matrix A, using $_ { L U }$ decomposition.

Int n,m1,m2;   
MatDoub au,al; Upper and lower triangular matrices, stored compactly.   
VecInt indx;   
Doub d;   
Bandec(MatDoub_I &a, const int mm1, const int mm2); Constructor.   
void solve(VecDoub_I &b, VecDoub_O &x); Solve a right-hand side vector.   
Doub det(); Return determinant of A.

The constructor takes as arguments the compactly stored matrix A, and the integers $m _ { 1 }$ and $m _ { 2 }$ . (One could of course define a “band-diagonal matrix object” to encapsulate these quantities, but in this brief treatment we want to keep things simple.)

Bandec::Bandec(MatDoub_I &a, const Int mm1, const Int mm2) : n(a.nrows()), au(a), m1(mm1), m2(mm2), al(n,m1), indx(n)

# banded.h

Constructor. Given an $\mathbf { n } \times \mathbf { n }$ band-diagonal matrix A with m1 subdiagonal rows and m2 superdiagonal rows, compactly stored in the array a[0..n-1][0.. $\mathtt { m 1 + m 2 } ]$ as described in the comment for routine banmul, an $_ { L U }$ decomposition of a rowwise permutation of A is constructed. The upper and lower triangular matrices are stored in au and al, respectively. The stored vector indx[0..n-1] records the row permutation effected by the partial pivoting; d is $\pm 1$ depending on whether the number of row interchanges was even or odd, respectively. {

const Doub TINY $^ { \prime = 1 }$ .0e-40;   
Int i,j,k,l,mm;   
Doub dum;   
$\scriptstyle { \mathtt { m m } } = { \mathtt { m } } 1 + { \mathtt { m } } 2 + 1$ ;   
l=m1;   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<m1;i++) { Rearrange the storage a bit. for (j=m1-i;j<mm;j $^ { + + }$ ) au[i][j-l] $\equiv _ { i }$ au[i][j]; l--; for (j=mm-l-1;j<mm;j++) au[i][j]=0.0;   
}   
d=1.0;   
l=m1;   
for (k=0;k<n;k++) { For each row... dum=au[k][0]; i=k; if (l<n) $\beth + +$ ; for (j ${ \tt = } \tt k { + }$ 1;j<l;j++) { Find the pivot element. if (abs(au[j][0]) $>$ abs(dum)) dum=au[j][0]; i=j; indx[k] $= \dot { 1 } + 1$ ; if (dum $\scriptstyle = = 0 . 0$ ) au[k][0] $=$ TINY; Matrix is algorithmically singular, but proceed anyway with TINY pivot (desirable in some applications). if (i $\mathbf { \updownarrow } = \mathbf { \partial } \mathbf { k } )$ 3 Interchange rows. $\mathrm { ~ d ~ } = \mathrm { ~ - d ~ }$ ; for $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<mm;j++) SWAP(au[k][j],au[i][j]); } for (i=k+1;i<l;i++) { Do the elimination. dum=au[i][0]/au[k][0]; al[k][i-k-1] $=$ dum; for (j $= 1$ ;j<mm;j++) au[i][j-1] $=$ au[i][j]-dum\*au[k][j]; au[i][mm-1] ${ = } 0$ .0; }   
}

Some pivoting is possible within the storage limitations of bandec, and the above routine does take advantage of the opportunity. In general, when TINY is returned as a diagonal element of $U$ , then the original matrix (perhaps as modified by roundoff error) is in fact singular. In this regard, bandec is somewhat more robust than tridag above, which can fail algorithmically even for nonsingular matrices; bandec is thus also useful (with $m _ { 1 } = m _ { 2 } = 1$ ) for some ill-behaved tridiagonal systems.

Once the matrix A has been decomposed, any number of right-hand sides can be solved in turn by repeated calls to the solve method, the forward- and backsubstitution routine analogous to its same-named cousin in $\ S 2 . 3$ .

# void Bandec::solve(VecDoub_I &b, VecDoub_O &x)

Given a right-hand side vector b[0..n-1], solves the band-diagonal linear equations $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ .   
The solution vector $\mathbf { x }$ is returned as $\mathbf { x } \left[ 0 \ldots \ldots \right] $ .   
Int i,j,k,l,mm;   
Doub dum;   
mm=m1+m2+1;   
l=m1;   
for (k=0;k<n;k++) x[k] $=$ b[k];   
for (k=0;k<n;k++) { Forward substitution, unscrambling the permuted rows j=indx[k]-1; as we go. if (j!=k) SWAP(x[k],x[j]); if (l<n) l++; for (j=k+1;j<l;j++) x[j] $- =$ al[k][j-k-1]\*x[k];   
$\beth = 1$ ;   
for (i=n-1;i>=0;i--) { Backsubstitution. dum=x[i]; for (k=1;k<l;k++) dum -= au[i][k]\*x[k+i]; x[i] $=$ dum/au[i][0]; if (l<mm) l++;   
}

And, finally, a method for getting the determinant:

Doub Bandec::det() {   
Using the stored decomposition, return the determinant of the matrix A. Doub dd $\mathit { \Theta } = \mathit { \Theta } \mathtt { d }$ ; for (int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n; $\dot { 1 } + + \dot { 1 }$ ) dd $\ast =$ au[i][0]; return dd;

The routines in Bandec are based on the Handbook routines bandet1 and bansol1 in [1].

# CITED REFERENCES AND FURTHER READING:

Keller, H.B. 1968, Numerical Methods for Two-Point Boundary-Value Problems; reprinted 1991 (New York: Dover), p. 74.   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), Example 5.4.3, p. 166.   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 9 . 1 1$ .   
Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer),Chapter I/6.[1]   
Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), $\ S 4 . 3$ .   
Hockney, R.W., and Jesshope, C.R. 1988, Parallel Computers 2: Architecture, Programming, and Algorithms (Bristol and Philadelphia: Adam Hilger),\$5.4.[2]

# 2.5 Iterative Improvement of a Solution to Linear Equations

Obviously it is not easy to obtain greater precision for the solution of a linear set than the precision of your computer’s floating-point word. Unfortunately, for large sets of linear equations, it is not always easy to obtain precision equal to, or even comparable to, the computer’s limit. In direct methods of solution, roundoff errors accumulate, and they are magnified to the extent that your matrix is close to singular. You can easily lose two or three significant figures for matrices that (you thought) were far from singular.

If this happens to you, there is a neat trick to restore the full machine precision, called iterative improvement of the solution. The theory is straightforward (see Figure 2.5.1): Suppose that a vector $\mathbf { X }$ is the exact solution of the linear set

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

You don’t, however, know $\mathbf { X }$ . You only know some slightly wrong solution $\mathbf { x } + \delta \mathbf { x }$ , where $\&$ is the unknown error. When multiplied by the matrix A, your slightly wrong solution gives a product slightly discrepant from the desired right-hand side $\mathbf { b }$ , namely

$$
\mathbf { A } \cdot ( \mathbf { x } + \delta \mathbf { x } ) = \mathbf { b } + \delta \mathbf { b }
$$

Subtracting (2.5.1) from (2.5.2) gives

$$
\mathbf { A } \cdot \delta \mathbf { x } = \delta \mathbf { b }
$$

![](images/0f6f4d1ab95a051635bd29b6e599c01753fce4bd8d96e942a347a4cf9328acc7.jpg)  
Figure 2.5.1. Iterative improvement of the solution to $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ . The first guess $\mathbf { x } + \delta \mathbf { x }$ is multiplied by $\mathbf { A }$ to produce $\mathbf { b } + \delta \mathbf { b }$ . The known vector $\mathbf { b }$ is subtracted, giving $\delta \mathbf { b }$ . The linear set with this right-hand side is inverted, giving ${ \displaystyle \delta \mathbf { x } }$ . This is subtracted from the first guess giving an improved solution $\mathbf { x }$ .

But (2.5.2) can also be solved, trivially, for $\delta \mathbf { b }$ . Substituting this into (2.5.3) gives

$$
\mathbf { A } \cdot \delta \mathbf { x } = \mathbf { A } \cdot ( \mathbf { x } + \delta \mathbf { x } ) - \mathbf { b }
$$

In this equation, the whole right-hand side is known, since $\mathbf { x } + \delta \mathbf { x }$ is the wrong solution that you want to improve. It is good to calculate the right-hand side in higher precision than the original solution, if you can, since there will be a lot of cancellation in the subtraction of $\mathbf { b }$ . Then, we need only solve (2.5.4) for the error $\displaystyle { \delta \mathbf { x } }$ , and then subtract this from the wrong solution to get an improved solution.

An important extra benefit occurs if we obtained the original solution by $L U$ decomposition. In this case we already have the $L U$ decomposed form of A, and all we need do to solve (2.5.4) is compute the right-hand side, forward- and backsubstitute.

Because so much of the necessary machinery is already in LUdcmp, we implement iterative improvement as a member function of that class. Since iterative improvement requires the matrix A (as well as its $L U$ decomposition), we have, with foresight, caused LUdcmp to save a reference to the matrix a from which it was constructed. If you plan to use iterative improvement, you must not modify a or let it go out of scope. (No other method in LUdcmp makes use of this reference to a.)

# void LUdcmp::mprove(VecDoub_I &b, VecDoub_IO &x)

Improves a solution vector $\mathbf { x } \left[ 0 \ldots \ldots \right] $ of the linear set of equations $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ . The vectors $\mathbf { b } \left[ 0 \ldots \mathbf { n - 1 } \right]$ and $\mathbf { x } \left[ 0 \ldots \ldots \right] $ are input. On output, $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ is modified, to an improved set of values.

Int i,j;   
VecDoub r(n);   
for $\scriptstyle \dot { 1 } = 0$ ;i<n; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \beta } } } .$ ) { Calculate the right-hand side, accumulating Ldoub sdp $=$ -b[i]; the residual in higher precision. for (j ${ = } 0$ ;j<n;j++) sdp $+ =$ (Ldoub)aref[i][j] $^ *$ (Ldoub)x[j]; r[i] $=$ sdp;   
}   
solve(r,r);   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) x[i] -= r[i];

Solve for the error term, and subtract it from the old solution.

# }

Iterative improvement is highly recommended: It is a process of order only $N ^ { 2 }$ operations (multiply vector by matrix, forward- and backsubstitute — see discussion following equation 2.3.7); it never hurts; and it can really give you your money’s worth if it saves an otherwise ruined solution on which you have already spent of order $N ^ { 3 }$ operations.

You can call mprove several times in succession if you want. Unless you are starting quite far from the true solution, one call is generally enough; but a second call to verify convergence can be reassuring.

If you cannot compute the right-hand side in equation (2.5.4) in higher precision, iterative refinement will still often improve the quality of a solution, although not in all cases as much as if higher precision is available. Many textbooks assert the contrary, but you will find the proof in [1].

# 2.5.1 More on Iterative Improvement

It is illuminating (and will be useful later in the book) to give a somewhat more solid analytical foundation for equation (2.5.4), and also to give some additional results. Implicit in the previous discussion was the notion that the solution vector $\mathbf { x } + \delta \mathbf { x }$ has an error term; but we neglected the fact that the $L U$ decomposition of $\mathbf { A }$ is itself not exact.

A different analytical approach starts with some matrix ${ \bf B } _ { 0 }$ that is assumed to be an approximate inverse of the matrix A, so that $\mathbf { B } _ { 0 } \cdot \mathbf { A }$ is approximately the identity matrix 1. Define the residual matrix $\mathbf { R }$ of ${ \bf B } _ { 0 }$ as

$$
\mathbf { R } \equiv \mathbf { 1 } - \mathbf { B } _ { 0 } \cdot \mathbf { A }
$$

which is supposed to be “small” (we will be more precise below). Note that therefore

$$
\mathbf { B } _ { 0 } \cdot \mathbf { A } = \mathbf { 1 } - \mathbf { R }
$$

Next consider the following formal manipulation:

$$
\begin{array} { r l } & { \mathbf { A } ^ { - 1 } = \mathbf { A } ^ { - 1 } \cdot ( \mathbf { B } _ { 0 } ^ { - 1 } \cdot \mathbf { B } _ { 0 } ) = ( \mathbf { A } ^ { - 1 } \cdot \mathbf { B } _ { 0 } ^ { - 1 } ) \cdot \mathbf { B } _ { 0 } = ( \mathbf { B } _ { 0 } \cdot \mathbf { A } ) ^ { - 1 } \cdot \mathbf { B } _ { 0 } } \\ & { \qquad = ( \mathbf { 1 } - \mathbf { R } ) ^ { - 1 } \cdot \mathbf { B } _ { 0 } = ( \mathbf { 1 } + \mathbf { R } + \mathbf { R } ^ { 2 } + \mathbf { R } ^ { 3 } + \cdots ) \cdot \mathbf { B } _ { 0 } } \end{array}
$$

We can define the $n$ th partial sum of the last expression by

$$
\mathbf { B } _ { n } \equiv ( \mathbf { 1 } + \mathbf { R } + \cdots + \mathbf { R } ^ { n } ) \cdot \mathbf { B } _ { 0 }
$$

so that $\mathbf { B } _ { \infty } \to \mathbf { A } ^ { - 1 }$ , if the limit exists.

It now is straightforward to verify that equation (2.5.8) satisfies some interesting recurrence relations. As regards solving $\mathbf { A \cdot x } = \mathbf { b }$ , where $\mathbf { X }$ and $\mathbf { b }$ are vectors, define

$$
{ \bf x } _ { n } \equiv { \bf B } _ { n } \cdot { \bf b }
$$

Then it is easy to show that

$$
\mathbf { x } _ { n + 1 } = \mathbf { x } _ { n } + \mathbf { B } _ { 0 } \cdot ( \mathbf { b } - \mathbf { A } \cdot \mathbf { x } _ { n } )
$$

This is immediately recognizable as equation (2.5.4), with $- \delta \mathbf { x } = \mathbf { x } _ { n + 1 } - \mathbf { x } _ { n }$ , and with ${ \bf B } _ { 0 }$ taking the role of ${ \bf A } ^ { - 1 }$ . We see, therefore, that equation (2.5.4) does not require that the $L U$ decomposition of $\mathbf { A }$ be exact, but only that the implied residual $\mathbf { R }$ be small. In rough terms, if the residual is smaller than the square root of your computer’s roundoff error, then after one application of equation (2.5.10) (that is, going from $\mathbf { x } _ { 0 } \equiv \mathbf { B } _ { 0 } \cdot \mathbf { b }$ to $\mathbf { X } _ { 1 }$ ) the first neglected term, of order $\mathbf { R } ^ { 2 }$ , will be smaller than the roundoff error. Equation (2.5.10), like equation (2.5.4), moreover, can be applied more than once, since it uses only ${ \bf B } _ { 0 }$ , and not any of the higher $\mathbf { B }$ ’s.

A much more surprising recurrence that follows from equation (2.5.8) is one that more than doubles the order $n$ at each stage:

$$
{ \bf B } _ { 2 n + 1 } = 2 { \bf B } _ { n } - { \bf B } _ { n } \cdot { \bf A } \cdot { \bf B } _ { n } \qquad n = 0 , 1 , 3 , 7 , \ldots
$$

Repeated application of equation (2.5.11), from a suitable starting matrix ${ \bf B } _ { 0 }$ , converges quadratically to the unknown inverse matrix ${ \bf A } ^ { - 1 }$ (see $\ S 9 . 4$ for the definition of “quadratically”). Equation (2.5.11) goes by various names, including Schultz’s Method and Hotelling’s Method; see Pan and Reif [2] for references. In fact, equation (2.5.11) is simply the iterative Newton-Raphson method of root finding (-9.4) applied to matrix inversion.

Before you get too excited about equation (2.5.11), however, you should notice that it involves two full matrix multiplications at each iteration. Each matrix multiplication involves $N ^ { 3 }$ adds and multiplies. But we already saw in $\ S 2 . 1 - \ S 2 . 3$ that direct inversion of A requires only $N ^ { 3 }$ adds and $\setminus ^ { 3 }$ multiplies in toto. Equation (2.5.11) is therefore practical only when special circumstances allow it to be evaluated much more rapidly than is the case for general matrices. We will meet such circumstances later, in $\ S 1 3 . 1 0$ .

In the spirit of delayed gratification, let us nevertheless pursue the two related issues: When does the series in equation (2.5.7) converge; and what is a suitable initial guess ${ \bf B } _ { 0 }$ (if, for example, an initial $L U$ decomposition is not feasible)?

We can define the norm of a matrix as the largest amplification of length that it is able to induce on a vector,

$$
\left\| \mathbf { R } \right\| \equiv \operatorname* { m a x } _ { \mathbf { v } \neq 0 } { \frac { | \mathbf { R } \cdot \mathbf { v } | } { | \mathbf { v } | } }
$$

If we let equation (2.5.7) act on some arbitrary right-hand side $\mathbf { b }$ , as one wants a matrix inverse to do, it is obvious that a sufficient condition for convergence is

$$
\| \mathbf { R } \| < 1
$$

Pan and Reif [2] point out that a suitable initial guess for ${ \bf B } _ { 0 }$ is any sufficiently small constant $\epsilon$ times the matrix transpose of $\mathbf { A }$ , that is,

$$
\mathbf { B } _ { 0 } = \epsilon \mathbf { A } ^ { T } \qquad \mathrm { o r } \qquad \mathbf { R } = \mathbf { 1 } - \epsilon \mathbf { A } ^ { T } \cdot \mathbf { A }
$$

To see why this is so involves concepts from Chapter 11; we give here only the briefest sketch: $\mathbf { A } ^ { T } \cdot \mathbf { A }$ is a symmetric, positive-definite matrix, so it has real, positive eigenvalues. In its diagonal representation, $\mathbf { R }$ takes the form

$$
\mathbf { R } = \mathrm { d i a g } ( 1 - \epsilon \lambda _ { 0 } , 1 - \epsilon \lambda _ { 1 } , \ldots , 1 - \epsilon \lambda _ { N - 1 } )
$$

where all the $\lambda _ { i }$ ’s are positive. Evidently any $\epsilon$ satisfying $0 < \epsilon < 2 / ( \operatorname* { m a x } _ { i } \lambda _ { i } )$ will give $\| \mathbf { R } \| ~ < ~ 1$ . It is not difficult to show that the optimal choice for $\epsilon$ , giving the most rapid convergence for equation (2.5.11), is

$$
\epsilon = 2 / ( \operatorname* { m a x } _ { i } \lambda _ { i } + \operatorname* { m i n } _ { i } \lambda _ { i } )
$$

Rarely does one know the eigenvalues of $\mathbf { A } ^ { T } \cdot \mathbf { A }$ in equation (2.5.16). Pan and Reif derive several interesting bounds, which are computable directly from A. The following choices guarantee the convergence of ${ \bf B } _ { n }$ as $n  \infty$ :

$$
\epsilon \leq 1 \bigg / \sum _ { j , k } a _ { j k } ^ { 2 } \qquad \mathrm { o r } \qquad \epsilon \leq 1 \bigg / \bigg ( \operatorname* { m a x } _ { i } \sum _ { j } | a _ { i j } | \times \operatorname* { m a x } _ { j } \sum _ { i } | a _ { i j } | \bigg )
$$

The latter expression is truly a remarkable formula, which Pan and Reif derive by noting that the vector norm in equation (2.5.12) need not be the usual $L _ { 2 }$ norm, but can instead be either the $L _ { \infty }$ (max) norm, or the $L _ { 1 }$ (absolute value) norm. See their work for details.

Another approach, with which we have had some success, is to estimate the largest eigenvalue statistically, by calculating $s _ { i } \equiv | \mathbf { A } \cdot \mathbf { v } _ { i } | ^ { 2 }$ for several unit vector $\mathbf { v } _ { i }$ ’s with randomly chosen directions in $N$ -space. The largest eigenvalue $\lambda$ can then be bounded by the maximum of $2 \operatorname* { m a x } s _ { i }$ and $2 N \mathrm { V a r } ( s _ { i } ) / \mu ( s _ { i } )$ , where Var and $\mu$ denote the sample variance and mean, respectively.

# CITED REFERENCES AND FURTHER READING:

Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), $\ S 2 . 3 . 4$ , p. 55.   
Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), $\ S 3 . 5 . 3$ .   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 5 . 5 . 6$ , p. 183.   
Forsythe, G.E., and Moler, C.B. 1967, Computer Solution of Linear Algebraic Systems (Englewood Cliffs, NJ: Prentice-Hall), Chapter 13.   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 9 . 5$ , p. 437.   
Higham, N.J. 1997, “Iterative Refinement for Linear Systems and LAPACK,” IMA Journal of Numerical Analysis,vol.17,pp. 495-509.[1]   
Pan, V., and Reif, J. 1985, “Efficient Parallel Solution of Linear Systems,” in Proceedings of the Seventeenth Annual ACM Symposium on Theory of Computing (New York: Association for Computing Machinery).[2]

# 2.6 Singular Value Decomposition

There exists a very powerful set of techniques for dealing with sets of equations or matrices that are either singular or else numerically very close to singular. In many cases where Gaussian elimination and $L U$ decomposition fail to give satisfactory results, this set of techniques, known as singular value decomposition, or $S V D$ , will diagnose for you precisely what the problem is. In some cases, SVD will not only diagnose the problem, it will also solve it, in the sense of giving you a useful numerical answer, although, as we shall see, not necessarily “the” answer that you thought you should get.

SVD is also the method of choice for solving most linear least-squares problems. We will outline the relevant theory in this section, but defer detailed discussion of the use of SVD in this application to Chapter 15, whose subject is the parametric modeling of data.

SVD methods are based on the following theorem of linear algebra, whose proof is beyond our scope: Any $M \times N$ matrix A can be written as the product of an $M \times N$ column-orthogonal matrix $\mathbf { U }$ , an $N \times N$ diagonal matrix W with positive or zero elements (the singular values), and the transpose of an $N \times N$ orthogonal matrix $\mathbf { V }$ . The various shapes of these matrices are clearer when shown as tableaus. If $M > N$ (which corresponds to the overdetermined situation of more equations than unknowns), the decomposition looks like this:

$$
\begin{array} { r } { \left( \begin{array} { l l l l l } & & \\ & & \\ & { \mathbf { A } } & & \\ & & & \\ & & & \end{array} \right) = \left( \begin{array} { l l l l l } & & \\ & & \\ & { \mathbf { U } } & \\ & & & \\ & & & { \cdots } & \\ & & & & { w _ { N - 1 } } \end{array} \right) \cdot \left( \begin{array} { l l l l l } & & \\ & { \mathbf { V } ^ { T } } & \\ & & { \mathbf { \Omega } } \end{array} \right) } \end{array}
$$

If $M < N$ (the undetermined situation of fewer equations than unknowns), it looks like this:

$$
\left( \begin{array} { l l l l } & { \textbf { A } } & { } \end{array} \right) = \left( \begin{array} { l l l l } & { \textbf { U } } & { } \end{array} \right) \cdot \left( \begin{array} { l l l l } { w _ { 0 } } & { } & { } & { } \\ { } & { w _ { 1 } } & { } & { } \\ { } & { } & { \cdots } & { } \\ { } & { } & { \cdots } & { } \\ { } & { } & { } & { w _ { N - 1 } } \end{array} \right) \cdot \left( \begin{array} { l l l l } { \ } & { \textbf { v } ^ { T } } & { } & { } \\ { } & { \textbf { v } ^ { T } } & { } \\ { } & { } & { } & { } \end{array} \right)
$$

The matrix $\mathbf { V }$ is orthogonal in the sense that its columns are orthonormal,

$$
\sum _ { j = 0 } ^ { N - 1 } V _ { j k } V _ { j n } = \delta _ { k n } \qquad 0 \leq k \leq N - 1
$$

that is, $\mathbf { V } ^ { T } \cdot \mathbf { V } = \mathbf { 1 }$ . Since $\mathbf { V }$ is square, it is also row-orthonormal, $\mathbf { V } \cdot \mathbf { V } ^ { T } = 1$ . When $M \geq N$ , the matrix $\mathbf { U }$ is also column-orthogonal,

$$
\sum _ { i = 0 } ^ { M - 1 } U _ { i k } U _ { i n } = \delta _ { k n } \qquad 0 \leq k \leq N - 1
$$

that is, $\mathbf { U } ^ { T } \cdot \mathbf { U } = \mathbf { 1 }$ . In the case $M \ < \ N$ , however, two things happen: (i) The singular values $w _ { j }$ for $j = M , \dotsc , N - 1$ are all zero, and (ii) the corresponding columns of $\mathbf { U }$ are also zero. Equation (2.6.4) then holds only for $k , n \le M - 1$ .

The decomposition (2.6.1) or (2.6.2) can always be done, no matter how singular the matrix is, and it is “almost” unique. That is to say, it is unique up to (i) making the same permutation of the columns of $\mathbf { U }$ , elements of $\mathbf { W }$ , and columns of $\mathbf { V }$ (or rows of $\bar { \mathbf { V } } ^ { T }$ ); or (ii) performing an orthogonal rotation on any set of columns of $\mathbf { U }$ and $\mathbf { V }$ whose corresponding elements of $\mathbf { W }$ happen to be exactly equal. (A special case is multiplying any column of $\mathbf { U }$ , and the corresponding column of $\mathbf { V }$ by $- 1 . )$ A consequence of the permutation freedom is that for the case $M < N$ , a numerical algorithm for the decomposition need not return zero $w _ { j }$ ’s in the canonical positions $j = M , \dotsc , N - 1$ ; the $N - M$ zero singular values can be scattered among all positions $j = 0 , 1 , \ldots , N - 1$ , and one needs to perform a sort to get the canonical order. In any case, it is conventional to sort all the singular values into descending order.

A Webnote [1] gives the details of the routine that actually performs SVD on an arbitrary matrix A, yielding U , W , and $\mathbf { V }$ . The routine is based on a routine by Forsythe et al. [2], which is in turn based on the original routine of Golub and Reinsch, found, in various forms, in [4-6] and elsewhere. These references include extensive discussion of the algorithm used. As much as we dislike the use of blackbox routines, we need to ask you to accept this one, since it would take us too far afield to cover its necessary background material here. The algorithm is very stable, and it is very unusual for it ever to misbehave. Most of the concepts that enter the algorithm (Householder reduction to bidiagonal form, diagonalization by $\boldsymbol { \mathcal { Q } R }$ procedure with shifts) will be discussed further in Chapter 11.

As we did for $L U$ decomposition, we encapsulate the singular value decomposition and also the methods that depend on it into an object, SVD. We give its declaration here. The rest of this section will give the details on how to use it.

struct SVD {   
Object for singular value decomposition of a matrix A, and related functions. Int m,n; MatDoub u,v; The matrices $\mathbf { U }$ and $\mathbf { V }$ . VecDoub w; The diagonal matrix $\mathbf { W }$ . Doub eps, tsh; SVD(MatDoub_I &a) : m(a.nrows()), n(a.ncols()), u(a), $\mathtt { v } ( \mathtt { n } , \mathtt { n } )$ , $\mathbb { w } ( \beth )$ { Constructor. The single argument is A. The SVD computation is done by decompose, and the results are sorted by reorder. eps $=$ numeric_limits<Doub>::epsilon(); decompose(); reorder(); tsh $=$ 0.5\*sqrt(m+n+1.)\*w[0]\*eps; Default threshold for nonzero singular } values.

void solve(VecDoub_I &b, VecDoub_O &x, Doub thresh); void solve(MatDoub_I &b, MatDoub_O &x, Doub thresh); Solve with (apply the pseudoinverse to) one or more right-hand side

Int rank(Doub thresh); Quantities associated with the range and Int nullity(Doub thresh); nullspace of A. MatDoub range(Doub thresh); MatDoub nullspace(Doub thresh); Doub inv_condition() { Return reciprocal of the condition numreturn (w[0] $\scriptstyle < = \ 0$ . || w[n-1] <= 0.) ? 0. : w[n-1]/w[0]; ber of A. } void decompose(); Functions used by the constructor. void reorder(); Doub pythag(const Doub a, const Doub b); };

# 2.6.1 Range, Nullspace, and All That

Consider the familiar set of simultaneous equations

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

where $\mathbf { A }$ is an $M \times N$ matrix, and $\mathbf { X }$ and $\mathbf { b }$ are vectors of dimension $N$ and $M$ respectively. Equation (2.6.5) defines $\mathbf { A }$ as a linear mapping from an $N$ -dimensional vector space to (generally) an $M$ -dimensional one. But the map might be able to reach only a lesser-dimensional subspace of the full $M$ -dimensional one. That subspace is called the range of A. The dimension of the range is called the rank of A. The rank of A is equal to its number of linearly independent columns, and also (perhaps less obviously) to its number of linearly independent rows. If A is not identically zero, its rank is at least 1, and at most $\operatorname* { m i n } ( M , N )$ .

Sometimes there are nonzero vectors $\mathbf { X }$ that are mapped to zero by A, that is, $\mathbf { A \cdot x } = 0$ . The space of such vectors (a subspace of the $N$ -dimensional space that $\mathbf { X }$ lives in) is called the nullspace of $\mathbf { A }$ , and its dimension is called A’s nullity. The nullity can have any value from zero to $N$ . The rank-nullity theorem states that, for any A, the rank plus the nullity is $N$ , the number of columns.

An important special case is $M \ = \ N$ , so the $\mathbf { A }$ is square, $N \times N$ . If the rank of $\mathbf { A }$ is $N$ , its maximum possible value, then A is nonsingular and invertible: $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ has a unique solution for any $\mathbf { b }$ , and only the zero vector is mapped to zero. This is a case where $L U$ decomposition (-2.3) is the preferred solution method for $\mathbf { X }$ . However, if A has rank less than $N$ (i.e., has nullity greater than zero), then two things happen: (i) most right-hand side vectors $\mathbf { b }$ yield no solution, but (ii) some have multiple solutions (in fact a whole subspace of them). We consider this situation further, below.

What has all this to do with singular value decomposition? SVD explicitly constructs orthonormal bases for the nullspace and range of a matrix! Specifically, the columns of $\mathbf { U }$ whose same-numbered elements $w _ { j }$ are nonzero are an orthonormal set of basis vectors that span the range; the columns of $\mathbf { V }$ whose same-numbered elements $w _ { j }$ are zero are an orthonormal basis for the nullspace. Our SVD object has methods that return the rank or nullity (integers), and also the range and nullspace, each of these packaged as a matrix whose columns form an orthonormal basis for the respective subspace.

# svd.h Int SVD::rank(Doub thresh $\begin{array} { r l } { \mathbf { \Phi } } & { { } = \mathbf { \Phi } - \mathbf { 1 } \mathbf { \Phi } . } \end{array}$ ) {

Return the rank of A, after zeroing any singular values smaller than thresh. If thresh is negative, a default value based on estimated roundoff is used.

Int j, $\mathtt { n c } = 0$ ; tsh $=$ (thresh $> = ~ 0$ . ? thresh : 0.5\*sqrt $\mathtt { m } + \mathtt { n } + 1$ .)\*w[0]\*eps); for ( $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j++) if (w[j] $>$ tsh) nr++; return nr; }

# Int SVD::nullity(Doub thresh $\begin{array} { r l } { \mathbf { \Phi } } & { { } = \mathbf { \Phi } - \mathbf { 1 } \mathbf { \Phi } . } \end{array}$ ) {

Return the nullity of A, after zeroing any singular values smaller than thresh. Default value as above.

Int j, $\mathtt { n n } { = } 0 $ ;   
tsh $=$ (thresh $> = ~ 0$ . ? thresh : 0.5\*sqrt( $\mathtt { m } + \mathtt { n } + 1$ .)\*w[0]\*eps);   
for ( $\scriptstyle { \dot { \ j } } = 0$ ;j<n; ${ \mathrm { j } } + +$ ) if (w[j] $< =$ tsh) $\mathtt { n n } + +$ ;   
return nn;

# }

MatDoub SVD::range(Doub thresh = -1.){

Give an orthonormal basis for the range of A as the columns of a returned matrix. thresh as above.

Int i,j, $\mathtt { n r } { = } 0$ ;   
MatDoub rnge(m,rank(thresh));   
for (j=0;j<n;j++) { if (w[j] $>$ tsh) { for (i=0;i<m;i++) rnge[i][nr] $=$ u[i][j]; nr++; }   
}   
return rnge;

MatDoub SVD::nullspace(Doub thresh $= - 1 . ) $

Give an orthonormal basis for the nullspace of A as the columns of a returned matrix. thresh as above.

Int j,jj, $\mathtt { n n } { = } 0$ ;   
MatDoub nullsp(n,nullity(thresh));   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { if (w[j] $< =$ tsh) { for (jj=0;jj<n;jj $^ { + + }$ ) nullsp[jj][nn] $=$ v[jj][j]; nn++; }   
}   
return nullsp;

The meaning of the optional parameter thresh is discussed below.

# 2.6.2 SVD of a Square Matrix

We return to the case of a square $N \times N$ matrix A. U , $\mathbf { V }$ , and $\mathbf { W }$ are also square matrices of the same size. Their inverses are also trivial to compute: $\mathbf { U }$ and $\mathbf { V }$ are orthogonal, so their inverses are equal to their transposes; $\mathbf { W }$ is diagonal, so its inverse is the diagonal matrix whose elements are the reciprocals of the elements $w _ { j }$ . From (2.6.1) it now follows immediately that the inverse of $\mathbf { A }$ is

$$
\mathbf { A } ^ { - 1 } = \mathbf { V } \cdot \left[ \operatorname { d i a g } \left( 1 / w _ { j } \right) \right] \cdot \mathbf { U } ^ { T }
$$

The only thing that can go wrong with this construction is for one of the $w _ { j }$ ’s to be zero, or (numerically) for it to be so small that its value is dominated by roundoff error and therefore unknowable. If more than one of the $w _ { j }$ ’s has this problem, then the matrix is even more singular. So, first of all, SVD gives you a clear diagnosis of the situation.

Formally, the condition number of a matrix is defined as the ratio of the largest (in magnitude) of the $w _ { j }$ ’s to the smallest of the $w _ { j }$ ’s. A matrix is singular if its condition number is infinite, and it is ill-conditioned if its condition number is too large, that is, if its reciprocal approaches the machine’s floating-point precision (for example, less than about $1 0 ^ { - 1 5 }$ for values of type double). A function returning the condition number (or, rather, its reciprocal, to avoid overflow) is implemented in SVD.

Now let’s have another look at solving the set of simultaneous linear equations (2.6.5) in the case that A is singular. We already saw that the set of homogeneous equations, where $\mathbf b = 0$ , is solved immediately by SVD. The solution is any linear combination of the columns returned by the nullspace method above.

When the vector $\mathbf { b }$ on the right-hand side is not zero, the important question is whether it lies in the range of A or not. If it does, then the singular set of equations does have a solution $\mathbf { X }$ ; in fact it has more than one solution, since any vector in the nullspace (any column of $\mathbf { V }$ with a corresponding zero $w _ { j }$ ) can be added to $\mathbf { X }$ in any linear combination.

If we want to single out one particular member of this solution set of vectors as a representative, we might want to pick the one with the smallest length $\left| \mathbf { x } \right| ^ { 2 }$ . Here is how to find that vector using SVD: Simply replace $1 / w _ { j }$ by zero if $w _ { j } = 0$ . (It is not very often that one gets to set $\infty = 0$ !) Then compute, working from right to

left,

$$
\mathbf { x } = \mathbf { V } \cdot \left[ \operatorname { d i a g } \left( 1 / w _ { j } \right) \right] \cdot \left( \mathbf { U } ^ { T } \cdot \mathbf { b } \right)
$$

This will be the solution vector of smallest length; the columns of $\mathbf { V }$ that are in the nullspace complete the specification of the solution set.

Proof: Consider $| { \bf x } + { \bf x } ^ { \prime } |$ , where $\mathbf { x } ^ { \prime }$ lies in the nullspace. Then, if $\mathbf { W } ^ { - 1 }$ denotes the modified inverse of $\mathbf { W }$ with some elements zeroed,

$$
\begin{array} { r l } & { \left| \mathbf { x } + \mathbf { x } ^ { \prime } \right| = \left| \mathbf { V } \cdot \mathbf { W } ^ { - 1 } \cdot \mathbf { U } ^ { T } \cdot \mathbf { b } + \mathbf { x } ^ { \prime } \right| } \\ & { \qquad = \left| \mathbf { V } \cdot ( \mathbf { W } ^ { - 1 } \cdot \mathbf { U } ^ { T } \cdot \mathbf { b } + \mathbf { V } ^ { T } \cdot \mathbf { x } ^ { \prime } ) \right| } \\ & { \qquad = \left| \mathbf { W } ^ { - 1 } \cdot \mathbf { U } ^ { T } \cdot \mathbf { b } + \mathbf { V } ^ { T } \cdot \mathbf { x } ^ { \prime } \right| } \end{array}
$$

Here the first equality follows from (2.6.7), and the second and third from the orthonormality of $\mathbf { V }$ . If you now examine the two terms that make up the sum on the right-hand side, you will see that the first one has nonzero $j$ components only where $w _ { j } \neq 0$ , while the second one, since $\mathbf { x } ^ { \prime }$ is in the nullspace, has nonzero $j$ components only where $w _ { j } = 0$ . Therefore the minimum length obtains for $\mathbf { x } ^ { \prime } = 0$ , q.e.d.

If $\mathbf { b }$ is not in the range of the singular matrix A, then the set of equations (2.6.5) has no solution. But here is some good news: If $\mathbf { b }$ is not in the range of $\mathbf { A }$ , then equation (2.6.7) can still be used to construct a “solution” vector $\mathbf { X }$ . This vector $\mathbf { X }$ will not exactly solve $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ . But, among all possible vectors $\mathbf { X }$ , it will do the closest possible job in the least-squares sense. In other words, (2.6.7) finds

$$
\mathbf { x } \quad \mathrm { w h i c h ~ m i n i m i z e s } \quad r \equiv \left| \mathbf { A } \cdot \mathbf { x } - \mathbf { b } \right|
$$

The number $r$ is called the residual of the solution.

The proof is similar to (2.6.8): Suppose we modify $\mathbf { X }$ by adding some arbitrary $\mathbf { x } ^ { \prime }$ . Then $\mathbf { A \cdot x } - \mathbf { b }$ is modified by adding some $\mathbf { b } ^ { \prime } \equiv \mathbf { A } \cdot \mathbf { x } ^ { \prime }$ . Obviously $ { \mathbf { b } } ^ { \prime }$ is in the range of A. We then have

$$
\begin{array} { r l } & { \left| \mathbf { A } \cdot \mathbf { x } - \mathbf { b } + \mathbf { b } ^ { \prime } \right| = \left| ( \mathbf { U } \cdot \mathbf { W } \cdot \mathbf { V } ^ { T } ) \cdot ( \mathbf { V } \cdot \mathbf { W } ^ { - 1 } \cdot \mathbf { U } ^ { T } \cdot \mathbf { b } ) - \mathbf { b } + \mathbf { b } ^ { \prime } \right| } \\ & { \qquad = \left| ( \mathbf { U } \cdot \mathbf { W } \cdot \mathbf { W } ^ { - 1 } \cdot \mathbf { U } ^ { T } - 1 ) \cdot \mathbf { b } + \mathbf { b } ^ { \prime } \right| } \\ & { \qquad = \left| \mathbf { U } \cdot \left[ ( \mathbf { W } \cdot \mathbf { W } ^ { - 1 } - 1 ) \cdot \mathbf { U } ^ { T } \cdot \mathbf { b } + \mathbf { U } ^ { T } \cdot \mathbf { b } ^ { \prime } \right] \right| } \\ & { \qquad = \left| ( \mathbf { W } \cdot \mathbf { W } ^ { - 1 } - 1 ) \cdot \mathbf { U } ^ { T } \cdot \mathbf { b } + \mathbf { U } ^ { T } \cdot \mathbf { b } ^ { \prime } \right| } \end{array}
$$

Now, $( \mathbf { W } \cdot \mathbf { W } ^ { - 1 } - 1 )$ is a diagonal matrix that has nonzero $j$ components only for $w _ { j } = 0$ , while $\mathbf { U } ^ { T } \mathbf { b } ^ { \prime }$ has nonzero $j$ components only for $w _ { j } \neq 0$ , since $ { \mathbf { b } } ^ { \prime }$ lies in the range of A. Therefore the minimum obtains for $\mathbf { b } ^ { \prime } = 0$ , q.e.d.

Equation (2.6.7), which is also equation (2.6.6) applied associatively to $\mathbf { b }$ , is thus very general. If no $w _ { j }$ ’s are zero, it solves a nonsingular system of linear equations. If some $w _ { j }$ ’s are zero, and their reciprocals are made zero, then it gives a “best” solution, either the one of shortest length among many, or the one of minimum residual when no exact solution exists. Equation (2.6.6), with the singular $1 / w _ { j }$ ’s zeroized, is called the Moore-Penrose inverse or pseudoinverse of A.

Equation (2.6.7) is implemented in the SVD object as the method solve. (As in LUdcmp, we also include an overloaded form that solves for multiple right-hand sides simultaneously.) The argument thresh inputs a value below which $w _ { j }$ ’s are to be considered as being zero; if you omit this argument, or set it to a negative value, then the program uses a default value based on expected roundoff error.

void SVD::solve(VecDoub_I &b, VecDoub_O &x, Doub thresh $\begin{array} { r l } { \mathbf { \Phi } } & { { } = \mathbf { \Phi } - \mathbf { 1 } \mathbf { \Phi } . } \end{array}$ ) {

Solve $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ for a vector x using the pseudoinverse of A as obtained by SVD. If positive, thresh is the threshold value below which singular values are considered as zero. If thresh is negative, a default based on expected roundoff error is used.

Int i,j,jj; Doub s; if (b.size() $! = { \mathfrak { m } }$ || x.size() ${ \ ! } = \textbf { n } ,$ ) throw("SVD::solve bad sizes"); VecDoub tmp(n); tsh $=$ (thresh $> = ~ 0$ . ? thresh : 0.5\*sqrt $\langle \mathtt { m } + \mathtt { n } + 1$ .)\*w[0]\*eps); for (j=0;j<n;j++) { Calculate $U ^ { T } B$ . $\mathtt { s } = 0 \mathtt { . 0 }$ ; if (w[j] $>$ tsh) { Nonzero result only if $w _ { j }$ is nonzero. for ( $\mathtt { i } = 0$ ;i<m;i++) s $+ = \mathrm { ~ \ u ~ }$ [i][j]\*b[i]; s /= w[j]; This is the divide by $w _ { j }$ . tmp[j] $= \tt s$ ; } for (j=0;j<n;j++) { Matrix multiply by $V$ to get answer. $\mathtt { s } = 0 . 0$ ; for (jj ${ = } 0$ ;jj<n;jj $^ { + + }$ ) s $\scriptstyle + = \quad \mathtt { V }$ [j][jj]\*tmp[jj]; $\mathrm { \ x [ j ] = s }$ ; } }

void SVD::solve(MatDoub_I &b, MatDoub_O &x, Doub thresh $= - 1 .$ ) Solves m sets of n equations A $\mathbf { \nabla } _ { \mathbf { \partial } _ { \mathbf { \hat { \mu } } } } \cdot \mathbf { X } = \mathbf { B }$ using the pseudoinverse of A. The right-hand sides are input as b[0..n-1][0..m-1], while $\mathbf { x }$ [0..n-1][0..m-1] returns the solutions. thresh as above. {

int i,j, $\mathrm { m } { = } \mathrm { b }$ .ncols(); if (b.nrows() $! = \mathrm { ~ n ~ }$ || x.nrows() $\ ! = { \textbf { n } }$ || b.ncols() $\mathbf { \Psi } _ { \mathbf { { i } } } ^ { \mathsf { I } } = \mathbf { \Psi } _ { \mathbf { { X } } }$ .ncols()) throw("SVD::solve bad sizes"); VecDoub xx(n); for $( \ j = 0$ ;j<m; $\mathrm { j } { + + } \mathrm { , }$ ) { Copy and solve each column in turn. for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) xx[i] $=$ b[i][j]; solve(xx,xx,thresh); for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) x[i][j] $=$ xx[i]; }

Figure 2.6.1 summarizes the situation for the SVD of square matrices.

There are cases in which you may want to set the value of thresh to larger than its default. (You can retrieve the default as the member value tsh.) In the discussion since equation (2.6.5), we have been pretending that a matrix either is singular or else isn’t. Numerically, however, the more common situation is that some of the $w _ { j }$ ’s are very small but nonzero, so that the matrix is ill-conditioned. In that case, the direct solution methods of $L U$ decomposition or Gaussian elimination may actually give a formal solution to the set of equations (that is, a zero pivot may not be encountered); but the solution vector may have wildly large components whose algebraic cancellation, when multiplying by the matrix A, may give a very poor approximation to the right-hand vector $\mathbf { b }$ . In such cases, the solution vector $\mathbf { X }$ obtained by zeroing the small $w _ { j }$ ’s and then using equation (2.6.7) is very often better (in the sense of the residual $\left| \mathbf { A \cdot x } - \mathbf { b } \right|$ being smaller) than both the direct-method solution and the SVD solution where the small $w _ { j }$ ’s are left nonzero.

![](images/51e15da28c6f23b02704771af5f43a3e0a0f67e9c27897b5cc37534eab439e9a.jpg)  
Figure 2.6.1. (a) A nonsingular matrix A maps a vector space into one of the same dimension. The vector $\mathbf { x }$ is mapped into $\mathbf { b }$ , so that $\mathbf { x }$ satisfies the equation $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ . (b) A singular matrix A maps a vector space into one of lower dimensionality, here a plane into a line, called the “range” of A. The “nullspace” of $\mathbf { A }$ is mapped to zero. The solutions of $\mathbf { A } \cdot \mathbf { x } = \mathbf { d }$ consist of any one particular solution plus any vector in the nullspace, here forming a line parallel to the nullspace. Singular value decomposition (SVD) selects the particular solution closest to zero, as shown. The point c lies outside of the range of $\mathbf { A }$ , so $\mathbf { A } \cdot \mathbf { x } = \mathbf { c }$ has no solution. SVD finds the least-squares best compromise solution, namely a solution of $\mathbf { A } \cdot \mathbf { x } = \mathbf { c } ^ { \prime }$ , as shown.

It may seem paradoxical that this can be so, since zeroing a singular value corresponds to throwing away one linear combination of the set of equations that we are trying to solve. The resolution of the paradox is that we are throwing away precisely a combination of equations that is so corrupted by roundoff error as to be at best useless; usually it is worse than useless since it “pulls” the solution vector way off toward infinity along some direction that is almost a nullspace vector. In doing this, it compounds the roundoff problem and makes the residual $\left| \mathbf { A \cdot x } - \mathbf { b } \right|$ larger.

You therefore have the opportunity of deciding at what threshold thresh to zero the small $w _ { j }$ ’s, based on some idea of what size of computed residual $\left| \mathbf { A \cdot x } - \mathbf { b } \right|$ is acceptable.

For discussion of how the singular value decomposition of a matrix is related to its eigenvalues and eigenvectors, see $\ S 1 1 . 0 . 6$ .

# 2.6.3 SVD for Fewer Equations than Unknowns

If you have fewer linear equations $M$ than unknowns $N$ , then you are not expecting a unique solution. Usually there will be an $N - M$ dimensional family of solutions (which is the nullity, absent any other degeneracies), but the number could be larger. If you want to find this whole solution space, then SVD can readily do the job: Use solve to get one (the shortest) solution, then use nullspace to get a set of basis vectors for the nullspace. Your solutions are the former plus any linear combination of the latter.

# 2.6.4 SVD for More Equations than Unknowns

This situation will occur in Chapter 15, when we wish to find the least-squares solution to an overdetermined set of linear equations. In tableau, the equations to be solved are

$$
\left( \begin{array} { c c }  \begin{array} { c c } { \begin{array} { r l } \end{array} } & { \begin{array} { r l } \end{array} } \\ { \begin{array} { r l } \end{array} } & { \begin{array} { r l } \end{array} } \\ { \begin{array} { r l } \end{array} } & { \left( \begin{array} { c c } { \mathbf { x } } \\ { \mathbf { x } } \end{array} \right) = \left( \begin{array} { c c } { \begin{array} { r l } \end{array} } \\ { \mathbf { b } } \\ { \begin{array} { r l } \end{array} } \end{array} \right) } \end{array} \right) \end{array}
$$

The proofs that we gave above for the square case apply without modification to the case of more equations than unknowns. The least-squares solution vector $\mathbf { X }$ is given by applying the pseudoinverse (2.6.7), which, with nonsquare matrices, looks like this,

$$
) \cdot \left( \begin{array} { c } { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \end{array} \right) \cdot \left( \begin{array} { c } { { } } \\ { { } } \\ { { \bf { b } } } \\ { { } } \\ { { } } \end{array} \right)
$$

In general, the matrix W will not be singular, and no $w _ { j }$ ’s will need to be set to zero. Occasionally, however, there might be column degeneracies in A. In this case you will need to zero some small $w _ { j }$ values after all. The corresponding column in $\mathbf { V }$ gives the linear combination of $\mathbf { X }$ ’s that is then ill-determined even by the supposedly overdetermined set.

Sometimes, although you do not need to zero any $w _ { j }$ ’s for computational reasons, you may nevertheless want to take note of any that are unusually small: Their corresponding columns in $\mathbf { V }$ are linear combinations of $\mathbf { X }$ ’s that are insensitive to your data. In fact, you may then wish to zero these $w _ { j }$ ’s, by increasing the value of thresh, to reduce the number of free parameters in the fit. These matters are discussed more fully in Chapter 15.

# 2.6.5 Constructing an Orthonormal Basis

Suppose that you have $N$ vectors in an $M$ -dimensional vector space, with $N \leq M$ . Then the $N$ vectors span some subspace of the full vector space. Often you want to construct an orthonormal set of $N$ vectors that span the same subspace. The elementary textbook way to do this is by Gram-Schmidt orthogonalization, starting with one vector and then expanding the subspace one dimension at a time. Numerically, however, because of the build-up of roundoff errors, naive Gram-Schmidt orthogonalization is terrible.

The right way to construct an orthonormal basis for a subspace is by SVD: Form an $M \times N$ matrix A whose $N$ columns are your vectors. Construct an SVD object from the matrix. The columns of the matrix $\mathbf { U }$ are your desired orthonormal basis vectors.

You might also want to check the $w _ { j }$ ’s for zero values. If any occur, then the spanned subspace was not, in fact, $N$ -dimensional; the columns of U corresponding to zero $w _ { j }$ ’s should be discarded from the orthonormal basis set. The method range does this.

$\boldsymbol { \mathcal { Q } R }$ factorization, discussed in $\ S 2 . 1 0$ , also constructs an orthonormal basis; see [3].

# 2.6.6 Approximation of Matrices

Note that equation (2.6.1) can be rewritten to express any matrix $A _ { i j }$ as a sum of outer products of columns of $\mathbf { U }$ and rows of $\mathbf { V } ^ { T }$ , with the “weighting factors” being the singular values $w _ { j }$ ,

$$
A _ { i j } = \sum _ { k = 0 } ^ { N - 1 } w _ { k } \ U _ { i k } V _ { j k }
$$

If you ever encounter a situation where most of the singular values $w _ { j }$ of a matrix $\mathbf { A }$ are very small, then A will be well-approximated by only a few terms in the sum (2.6.13). This means that you have to store only a few columns of $\mathbf { U }$ and $\mathbf { V }$ (the same $k$ ones) and you will be able to recover, with good accuracy, the whole matrix.

Note also that it is very efficient to multiply such an approximated matrix by a vector x: You just dot $\mathbf { X }$ with each of the stored columns of $\mathbf { V }$ , multiply the resulting scalar by the corresponding $w _ { k }$ , and accumulate that multiple of the corresponding column of $\mathbf { U }$ . If your matrix is approximated by a small number $K$ of singular values, then this computation of $\mathbf { A } \cdot \mathbf { x }$ takes only about $K ( M + N )$ multiplications, instead of $M N$ for the full matrix.

# 2.6.7 Newer Algorithms

Analogous to the newer methods for eigenvalues of symmetric tridiagonal matrices mentioned in $\ S 1 1 . 4 . 4$ , there are newer methods for SVD. There is a divide-andconquer algorithm, implemented in LAPACK as dgesdd, which is typically faster by a factor of about 5 for large matrices than the algorithm we give (which is similar to the LAPACK routine dgesvd). Another routine based on the MRRR algorithm (see $\ S 1 1 . 4 . 4 )$ promises to be even better, but it is not available in LAPACK as of 2006. It will appear as routine dbdscr.

# CITED REFERENCES AND FURTHER READING:

Numerical Recipes Software 2007, “SVD Implementation Code,” Numerical Recipes Webnote No.2,at http://www.nr.com/webnotes?2 [1]

Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs, NJ: Prentice-Hal),Chapter 9.[2]

Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), $\ S 8 . 6$ and Chapter 12 (SVD). $\boldsymbol { \mathcal { Q } R }$ decomposition is discussed in $\ S 5$ .2.6.[3]

Lawson, C.L., and Hanson, R. 1974, Solving Least Squares Problems (Englewood Cliffs, NJ: Prentice-Hall); reprinted 1995 (Philadelphia: S.I.A.M.), Chapter 18.

Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer), Chapter I.10 by G.H. Golub and C. Reinsch.[4]

Anderson, E., et al. 1999, LAPACK User’s Guide, 3rd ed. (Philadelphia: S.I.A.M.). Online with software at $^ { 2 0 0 7 + }$ , http://www.netlib.org/lapack.[5]

Smith, B.T., et al. 1976, Matrix Eigensystem Routines — EISPACK Guide, 2nd ed., vol. 6 of Lecture Notes in Computer Science (New York: Springer).

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 6 . 7 . [ 6 ]$

# 2.7 Sparse Linear Systems

A system of linear equations is called sparse if only a relatively small number of its matrix elements $a _ { i j }$ are nonzero. It is wasteful to use general methods of linear algebra on such problems, because most of the $O ( N ^ { 3 } )$ arithmetic operations devoted to solving the set of equations or inverting the matrix involve zero operands. Furthermore, you might wish to work problems so large as to tax your available memory space, and it is wasteful to reserve storage for unfruitful zero elements. Note that there are two distinct (and not always compatible) goals for any sparse matrix method: saving time and/or saving space.

We considered one archetypal sparse form in $\ S 2 . 4$ , the band-diagonal matrix. In the tridiagonal case, e.g., we saw that it was possible to save both time (order $N$ instead of $N ^ { 3 }$ ) and space (order $N$ instead of $N ^ { 2 }$ ). The method of solution was not different in principle from the general method of $L U$ decomposition; it was just applied cleverly, and with due attention to the bookkeeping of zero elements. Many practical schemes for dealing with sparse problems have this same character. They are fundamentally decomposition schemes, or else elimination schemes akin to Gauss-Jordan, but carefully optimized so as to minimize the number of so-called fill-ins, initially zero elements that must become nonzero during the solution process, and for which storage must be reserved.

Direct methods for solving sparse equations, then, depend crucially on the precise pattern of sparsity of the matrix. Patterns that occur frequently, or that are useful as way stations in the reduction of more general forms, already have special names and special methods of solution. We do not have space here for any detailed review of these. References listed at the end of this section will furnish you with an “in” to the specialized literature, and the following list of buzz words (and Figure 2.7.1) will at least let you hold your own at cocktail parties:

- tridiagonal   
- band-diagonal (or banded) with bandwidth $M$   
- band triangular   
- block diagonal   
block tridiagonal block triangular cyclic banded singly (or doubly) bordered block diagonal singly (or doubly) bordered block triangular singly (or doubly) bordered band-diagonal   
- singly (or doubly) bordered band triangular   
- other (!)

You should also be aware of some of the special sparse forms that occur in the solution of partial differential equations in two or more dimensions. See Chapter 20.

If your particular pattern of sparsity is not a simple one, then you may wish to try an analyze/factorize/operate package, which automates the procedure of figuring out how fill-ins are to be minimized. The analyze stage is done once only for each pattern of sparsity. The factorize stage is done once for each particular matrix that fits the pattern. The operate stage is performed once for each right-hand side to be used with the particular matrix. Consult [2,3] for references on this. The NAG library [4] has an analyze/factorize/operate capability. A substantial collection of routines for sparse matrix calculation is also available from IMSL [5] as the Yale Sparse Matrix Package [6].

You should be aware that the special order of interchanges and eliminations, prescribed by a sparse matrix method so as to minimize fill-ins and arithmetic operations, generally acts to decrease the method’s numerical stability as compared to, e.g., regular $L U$ decomposition with pivoting. Scaling your problem so as to make its nonzero matrix elements have comparable magnitudes (if you can do it) will sometimes ameliorate this problem.

In the remainder of this section, we present some concepts that are applicable to some general classes of sparse matrices, and which do not necessarily depend on details of the pattern of sparsity.

# 2.7.1 Sherman-Morrison Formula

Suppose that you have already obtained, by herculean effort, the inverse matrix $\mathbf { A } ^ { - 1 }$ of a square matrix A. Now you want to make a “small” change in A, for example change one element $a _ { i j }$ , or a few elements, or one row, or one column. Is there any

![](images/2f10d13b980bb53e981e6f3d54532efa547e6513d21e825a7ba55956707ae5c4.jpg)  
Figure 2.7.1. Some standard forms for sparse matrices. (a) Band-diagonal; (b) block triangular; (c) block tridiagonal; (d) singly bordered block diagonal; (e) doubly bordered block diagonal; (f) singly bordered block triangular; (g) bordered band-triangular; (h) and (i) singly and doubly bordered band-diagonal; (j) and (k) other! (after Tewarson) [1].

way of calculating the corresponding change in $\mathbf { A } ^ { - 1 }$ without repeating your difficult labors? Yes, if your change is of the form

$$
\mathbf { A } \  \ ( \mathbf { A } + \mathbf { u } \otimes \mathbf { v } )
$$

for some vectors $\mathbf { u }$ and $\mathbf { V }$ . If $\mathbf { u }$ is a unit vector $\mathbf { e } _ { i }$ , then (2.7.1) adds the components of $\mathbf { V }$ to the $i$ th row. (Recall that $\mathbf { u } \otimes \mathbf { v }$ is a matrix whose $i , j$ th element is the product of the $i$ th component of $\mathbf { u }$ and the $j$ th component of $\mathbf { V }$ .) If $\mathbf { V }$ is a unit vector $\mathbf { e } _ { j }$ , then (2.7.1) adds the components of $\mathbf { u }$ to the $j$ th column. If both $\mathbf { u }$ and $\mathbf { V }$ are proportional to unit vectors $\mathbf { e } _ { i }$ and $\mathbf { e } _ { j }$ , respectively, then a term is added only to the element $a _ { i j }$ .

The Sherman-Morrison formula gives the inverse $( \mathbf { A } + \mathbf { u } \otimes \mathbf { v } ) ^ { - 1 }$ and is derived briefly as follows:

$$
\begin{array} { r l r } {  { ( \mathbf { A } + \mathbf { u } \otimes \mathbf { v } ) ^ { - 1 } = ( \mathbf { 1 } + \mathbf { A } ^ { - 1 } \cdot \mathbf { u } \otimes \mathbf { v } ) ^ { - 1 } \cdot \mathbf { A } ^ { - 1 } } } \\ & { } & { \quad = ( \mathbf { 1 } - \mathbf { A } ^ { - 1 } \cdot \mathbf { u } \otimes \mathbf { v } + \mathbf { A } ^ { - 1 } \cdot \mathbf { u } \otimes \mathbf { v } \cdot \mathbf { A } ^ { - 1 } \cdot \mathbf { u } \otimes \mathbf { v } - \ldots ) \cdot \mathbf { A } ^ { - 1 } } \\ & { } & { \quad = \mathbf { A } ^ { - 1 } - \mathbf { A } ^ { - 1 } \cdot \mathbf { u } \otimes \mathbf { v } \cdot \mathbf { A } ^ { - 1 } ( 1 - \lambda + \lambda ^ { 2 } - \ldots ) } \\ & { } & { \quad = \mathbf { A } ^ { - 1 } - { \frac { { ( \mathbf { A } ^ { - 1 } \cdot \mathbf { u } ) \otimes ( \mathbf { v } \cdot \mathbf { A } ^ { - 1 } ) } } { 1 + \lambda } } \quad \quad ( 2 . 7 . } \end{array}
$$

where

$$
\lambda \equiv \mathbf { v } \cdot \mathbf { A } ^ { - 1 } \cdot \mathbf { u }
$$

The second line of (2.7.2) is a formal power series expansion. In the third line, the associativity of outer and inner products is used to factor out the scalars $\lambda$ .

The use of (2.7.2) is this: Given $\mathbf { A } ^ { - 1 }$ and the vectors $\mathbf { u }$ and $\mathbf { V }$ , we need only perform two matrix multiplications and a vector dot product,

$$
\mathbf { z } \equiv \mathbf { A } ^ { - 1 } \cdot \mathbf { u } \qquad \mathbf { w } \equiv ( \mathbf { A } ^ { - 1 } ) ^ { T } \cdot \mathbf { v } \qquad \lambda = \mathbf { v } \cdot \mathbf { z }
$$

to get the desired change in the inverse

$$
\mathbf { A } ^ { - 1 } \quad \to \quad \mathbf { A } ^ { - 1 } - \frac { \mathbf { z } \otimes \mathbf { w } } { 1 + \lambda }
$$

The whole procedure requires only $3 N ^ { 2 }$ multiplies and a like number of adds (an even smaller number if $\mathbf { u }$ or $\mathbf { V }$ is a unit vector).

The Sherman-Morrison formula can be directly applied to a class of sparse problems. If you already have a fast way of calculating the inverse of $\mathbf { A }$ (e.g., a tridiagonal matrix or some other standard sparse form), then $( 2 . 7 . 4 ) - ( 2 . 7 . 5 )$ allow you to build up to your related but more complicated form, adding for example a row or column at a time. Notice that you can apply the Sherman-Morrison formula more than once successively, using at each stage the most recent update of $\mathbf { A } ^ { - 1 }$ (equation 2.7.5). Of course, if you have to modify every row, then you are back to an $N ^ { 3 }$ method. The constant in front of the $N ^ { 3 }$ is only a few times worse than the better direct methods, but you have deprived yourself of the stabilizing advantages of pivoting — so be careful.

For some other sparse problems, the Sherman-Morrison formula cannot be directly applied for the simple reason that storage of the whole inverse matrix $\mathbf { A } ^ { - 1 }$ is not feasible. If you want to add only a single correction of the form $\mathbf { u } \otimes \mathbf { v }$ and solve the linear system

$$
( \mathbf { A } + \mathbf { u } \otimes \mathbf { v } ) \cdot \mathbf { x } = \mathbf { b }
$$

then you proceed as follows. Using the fast method that is presumed available for the matrix A, solve the two auxiliary problems

$$
\mathbf { A } \cdot \mathbf { y } = \mathbf { b } \qquad \mathbf { A } \cdot \mathbf { z } = \mathbf { u }
$$

for the vectors $\mathbf { y }$ and $\mathbf { z }$ . In terms of these,

$$
\bf { x } = \bf { y } - \left[ \frac { \nabla v \cdot \bf { y } } { 1 + ( v \cdot z ) } \right] z
$$

as we see by multiplying (2.7.2) on the right by $\mathbf { b }$ .

# 2.7.2 Cyclic Tridiagonal Systems

So-called cyclic tridiagonal systems occur quite frequently and are a good example of how to use the Sherman-Morrison formula in the manner just described. The equations have the form

$$
\left[ \begin{array} { l l l l l l } { b _ { 0 ~ } } & { c _ { 0 ~ } } & { 0 } & { \cdots } & & { \beta } \\ { a _ { 1 ~ } } & { b _ { 1 ~ } } & { c _ { 1 ~ } } & { \cdots } & & \\ & & & { \cdots } & & \\ & & & { \cdots } & { a _ { N - 2 } } & { b _ { N - 2 } } & { c _ { N - 2 } } \\ { \alpha } & & { \cdots } & { 0 } & { a _ { N - 1 } } & { b _ { N - 1 } } \end{array} \right] \cdot \left[ \begin{array} { l } { x _ { 0 ~ } } \\ { x _ { 1 ~ } } \\ { \cdots } \\ { x _ { N - 2 } } \\ { x _ { N - 1 } } \end{array} \right] = \left[ \begin{array} { l } { r _ { 0 ~ } } \\ { r _ { 1 ~ } } \\ { \cdots } \\ { r _ { N - 2 } } \\ { r _ { N - 1 } } \end{array} \right]
$$

This is a tridiagonal system, except for the matrix elements $\alpha$ and $\beta$ in the corners. Forms like this are typically generated by finite differencing differential equations with periodic boundary conditions (-20.4).

We use the Sherman-Morrison formula, treating the system as tridiagonal plus a correction. In the notation of equation (2.7.6), define vectors $\mathbf { u }$ and $\mathbf { V }$ to be

$$
\mathbf { u } = \left[ \begin{array} { c } { \gamma } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { \alpha } \end{array} \right] \quad \quad \mathbf { v } = \left[ \begin{array} { c } { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { \beta / \gamma } \end{array} \right]
$$

Here $\gamma$ is arbitrary for the moment. Then the matrix A is the tridiagonal part of the matrix in (2.7.9), with two terms modified:

$$
b _ { 0 } ^ { \prime } = b _ { 0 } - \gamma , \qquad b _ { N - 1 } ^ { \prime } = b _ { N - 1 } - \alpha \beta / \gamma
$$

We now solve equations (2.7.7) with the standard tridiagonal algorithm and then get the solution from equation (2.7.8).

The routine cyclic below implements this algorithm. We choose the arbitrary parameter $\gamma = - b _ { 0 }$ to avoid loss of precision by subtraction in the first of equations (2.7.11). In the unlikely event that this causes loss of precision in the second of these equations, you can make a different choice.

void cyclic(VecDoub_I &a, VecDoub_I &b, VecDoub_I &c, const Doub alpha, const Doub beta, VecDoub_I &r, VecDoub_O &x)

Solves for a vector $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ the “cyclic” set of linear equations given by equation (2.7.9). a, b, c, and $\mathbf { r }$ are input vectors, all dimensioned as [0..n-1], while alpha and beta are the corner entries in the matrix. The input is not modified.

Int i, $\mathtt { n } = \mathtt { a }$ .size();   
Doub fact,gamma;   
if $\mathbf { \lambda } _ { \mathrm { ~ n ~ } } < = \mathbf { \lambda } _ { 2 } )$ ) throw("n too small in cyclic"); VecDoub bb(n),u(n),z(n);   
gamma $=$ -b[0];   
bb[0] $\mathtt { \Gamma } = \mathtt { b }$ [0]-gamma;   
bb[n-1]=b[n-1]-alpha\*beta/gamma;   
for ( $\dot { \bar { 1 } } = 1$ ;i<n-1;i++) bb[i] $= \mathrm { b }$ [i];   
tridag(a,bb,c,r,x);   
u[0] $=$ gamma;   
u[n-1] $=$ alpha;   
for ( $\dot { \bar { 1 } } = 1$ ;i<n-1;i $^ { + + }$ ) u[i]=0.0;   
tridag(a,bb,c,u,z);   
fact $=$ (x[0]+beta\*x[n-1]/gamma)/ (1. $_ { 0 + z }$ [0]+beta\*z[n-1]/gamma);   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) x[i] $- =$ fact\*z[i];

Avoid subtraction error in forming bb[0]. Set up the diagonal of the modified tridiagonal system.

Solve $\mathbf { A } \cdot \mathbf { x } = \mathbf { r }$ .   
Set up the vector $\mathbf { u }$ . Solve $\mathbf { A } \cdot \mathbf { z } = \mathbf { u }$ .   
Form $\mathbf { v } \cdot \mathbf { x } / ( 1 + \mathbf { v } \cdot \mathbf { z } )$ .

Now get the solution vector $\mathbf { x }$ .

# 2.7.3 Woodbury Formula

If you want to add more than a single correction term, then you cannot use (2.7.8) repeatedly, since without storing a new $\mathbf { A } ^ { - 1 }$ you will not be able to solve the auxiliary problems (2.7.7) efficiently after the first step. Instead, you need the Woodbury formula, which is the block-matrix version of the Sherman-Morrison formula,

$$
\begin{array} { r l } & { ( \mathbf { A } + \mathbf { U } \cdot \mathbf { V } ^ { T } ) ^ { - 1 } } \\ & { \qquad = \mathbf { A } ^ { - 1 } - \left[ \mathbf { A } ^ { - 1 } \cdot \mathbf { U } \cdot ( \mathbf { 1 } + \mathbf { V } ^ { T } \cdot \mathbf { A } ^ { - 1 } \cdot \mathbf { U } ) ^ { - 1 } \cdot \mathbf { V } ^ { T } \cdot \mathbf { A } ^ { - 1 } \right] } \end{array}
$$

Here $A$ is, as usual, an $N \times N$ matrix, while $\mathbf { U }$ and $\mathbf { V }$ are $N \times P$ matrices with $P < N$ and usually $P \ll N$ . The inner piece of the correction term may become clearer if written as the tableau,

$$
\begin{array} { r l } { \mathbf { U } } & { { } \quad \left[ \mathbf { 1 } + \mathbf { V } ^ { T } \cdot \mathbf { A } ^ { - 1 } \cdot \mathbf { U } \right] ^ { - 1 } \cdot \left[ \begin{array} { l l l l l l } { \quad } & { } & { } & { } & { } & { } \\ { } & { } & { } & { } & { } & { } \\ { } & { } & { } & { } & { } & { } & { } \\ { } & { } & { } & { } & { } & { } & { } \end{array} \right] } \end{array}
$$

where you can see that the matrix whose inverse is needed is only $P \times P$ rather than $N \times N$ .

The relation between the Woodbury formula and successive applications of the Sherman-Morrison formula is now clarified by noting that, if $\mathbf { U }$ is the matrix formed by columns out of the $P$ vectors $\mathbf { u } _ { 0 } , \ldots , \mathbf { u } _ { P - 1 }$ , and $\mathbf { V }$ is the matrix formed by columns out of the $P$ vectors $\mathbf { v } _ { 0 } , \ldots , \mathbf { v } _ { P - 1 }$ ,

$$
\mathbf { U } \equiv \left[ \mathbf { u } _ { 0 } \right] \ldots \left[ \mathbf { u } _ { P - 1 } \right] \qquad \mathbf { V } \equiv \left[ \mathbf { v } _ { 0 } \right] \ldots \left[ \mathbf { v } _ { P - 1 } \right]
$$

then two ways of expressing the same correction to $\mathbf { A }$ are

$$
\left( \mathbf { A } + \sum _ { k = 0 } ^ { P - 1 } \mathbf { u } _ { k } \otimes \mathbf { v } _ { k } \right) = ( \mathbf { A } + \mathbf { U } \cdot \mathbf { V } ^ { T } )
$$

(Note that the subscripts on $\mathbf { u }$ and $\mathbf { v }$ do not denote components, but rather distinguish the different column vectors.)

Equation (2.7.15) reveals that, if you have ${ \bf A } ^ { - 1 }$ in storage, then you can either make the $P$ corrections in one fell swoop by using (2.7.12) and inverting a $P \times P$ matrix, or else make them by applying (2.7.5) $P$ successive times.

If you don’t have storage for ${ \bf A } ^ { - 1 }$ , then you must use (2.7.12) in the following way: To solve the linear equation

$$
\left( \mathbf { A } + \sum _ { k = 0 } ^ { P - 1 } \mathbf { u } _ { k } \otimes \mathbf { v } _ { k } \right) \cdot \mathbf { x } = \mathbf { b }
$$

first solve the $P$ auxiliary problems

$$
\begin{array} { c } { \mathbf { A } \cdot \mathbf { z } _ { 0 } = \mathbf { u } _ { 0 } } \\ { \mathbf { A } \cdot \mathbf { z } _ { 1 } = \mathbf { u } _ { 1 } } \\ { \cdots } \\ { \mathbf { A } \cdot \mathbf { z } _ { P - 1 } = \mathbf { u } _ { P - 1 } } \end{array}
$$

and construct the matrix $\mathbf { Z }$ by columns from the $\mathbf { z }$ ’s obtained,

$$
\mathbf { Z } \equiv \left[ \mathbf { z } _ { 0 } \right] \ldots \left[ \mathbf { z } _ { P - 1 } \right]
$$

Next, do the $P \times P$ matrix inversion

$$
\mathbf { H } \equiv ( \mathbf { 1 } + \mathbf { V } ^ { T } \cdot \mathbf { Z } ) ^ { - 1 }
$$

Finally, solve the one further auxiliary problem

$$
\mathbf { A \cdot y } = \mathbf { b } 
$$

In terms of these quantities, the solution is given by

$$
\mathbf { x } = \mathbf { y } - \mathbf { Z } \cdot \left[ \mathbf { H } \cdot ( \mathbf { V } ^ { T } \cdot \mathbf { y } ) \right]
$$

# 2.7.4 Inversion by Partitioning

Once in a while, you will encounter a matrix (not even necessarily sparse) that can be inverted efficiently by partitioning. Suppose that the $N \times N$ matrix A is partitioned into

$$
\mathbf { A } = { \left[ \begin{array} { l l } { \mathbf { P } } & { \mathbf { Q } } \\ { \mathbf { R } } & { \mathbf { S } } \end{array} \right] }
$$

where $\mathbf { P }$ and S are square matrices of size $p \times p$ and $s \times s$ , respectively $( p + s = N )$ ). The matrices $\mathbf { Q }$ and $\mathbf { R }$ are not necessarily square and have sizes $p \times s$ and $s \times p$ , respectively.

If the inverse of $\mathbf { A }$ is partitioned in the same manner,

$$
\mathbf { A } ^ { - 1 } = \left[ \begin{array} { l l } { \widetilde { \mathbf { P } } } & { \widetilde { \mathbf { Q } } } \\ { \widetilde { \mathbf { R } } } & { \widetilde { \mathbf { S } } } \end{array} \right]
$$

then $\widetilde { \mathbf { P } } , \widetilde { \mathbf { Q } } , \widetilde { \mathbf { R } } , \widetilde { \mathbf { S } }$ , which have the same sizes as $\mathbf { P }$ , Q, R, S, respectively, can be found by either the formulas

$$
\begin{array} { r l } & { \tilde { \mathbf { P } } = ( \mathbf { P } - \mathbf { Q } \cdot \mathbf { S } ^ { - 1 } \cdot \mathbf { R } ) ^ { - 1 } } \\ & { \tilde { \mathbf { Q } } = - ( \mathbf { P } - \mathbf { Q } \cdot \mathbf { S } ^ { - 1 } \cdot \mathbf { R } ) ^ { - 1 } \cdot ( \mathbf { Q } \cdot \mathbf { S } ^ { - 1 } ) } \\ & { \tilde { \mathbf { R } } = - ( \mathbf { S } ^ { - 1 } \cdot \mathbf { R } ) \cdot ( \mathbf { P } - \mathbf { Q } \cdot \mathbf { S } ^ { - 1 } \cdot \mathbf { R } ) ^ { - 1 } } \\ & { \tilde { \mathbf { S } } = \mathbf { S } ^ { - 1 } + ( \mathbf { S } ^ { - 1 } \cdot \mathbf { R } ) \cdot ( \mathbf { P } - \mathbf { Q } \cdot \mathbf { S } ^ { - 1 } \cdot \mathbf { R } ) ^ { - 1 } \cdot ( \mathbf { Q } \cdot \mathbf { S } ^ { - 1 } ) } \end{array}
$$

or else by the equivalent formulas

$$
\begin{array} { r l } & { \widetilde { \mathbf { P } } = \mathbf { P } ^ { - 1 } + ( \mathbf { P } ^ { - 1 } \cdot \mathbf { Q } ) \cdot ( \mathbf { S } - \mathbf { R } \cdot \mathbf { P } ^ { - 1 } \cdot \mathbf { Q } ) ^ { - 1 } \cdot ( \mathbf { R } \cdot \mathbf { P } ^ { - 1 } ) } \\ & { \widetilde { \mathbf { Q } } = - ( \mathbf { P } ^ { - 1 } \cdot \mathbf { Q } ) \cdot ( \mathbf { S } - \mathbf { R } \cdot \mathbf { P } ^ { - 1 } \cdot \mathbf { Q } ) ^ { - 1 } } \\ & { \widetilde { \mathbf { R } } = - ( \mathbf { S } - \mathbf { R } \cdot \mathbf { P } ^ { - 1 } \cdot \mathbf { Q } ) ^ { - 1 } \cdot ( \mathbf { R } \cdot \mathbf { P } ^ { - 1 } ) } \\ & { \widetilde { \mathbf { S } } = ( \mathbf { S } - \mathbf { R } \cdot \mathbf { P } ^ { - 1 } \cdot \mathbf { Q } ) ^ { - 1 } } \end{array}
$$

The parentheses in equations (2.7.24) and (2.7.25) highlight repeated factors that you may wish to compute only once. (Of course, by associativity, you can instead do the matrix multiplications in any order you like.) The choice between using equations (2.7.24) and (2.7.25) depends on whether you want $\widetilde { \mathbf P }$ or $\widetilde { \mathbf { S } }$ to have the simpler formula; or on whether the repeated expression $( \mathbf { S } - \mathbf { R } \cdot \mathbf { P } ^ { - 1 } \cdot \mathbf { Q } ) ^ { - 1 }$ is easier to calculate than the expression $( \mathbf { P } - \mathbf { \bar { Q } } \cdot \mathbf { S } ^ { - 1 } \cdot \mathbf { \bar { R } } ) ^ { - 1 }$ ; or on the relative sizes of $\mathbf { P }$ and S; or on whether $\mathbf { P } ^ { - 1 }$ or ${ \mathbf { S } } ^ { - 1 }$ is already known.

Another sometimes useful formula is for the determinant of the partitioned matrix,

$$
\operatorname* { d e t } \mathbf { A } = \operatorname* { d e t } \mathbf { P } \operatorname* { d e t } ( \mathbf { S } - \mathbf { R } \cdot \mathbf { P } ^ { - 1 } \cdot \mathbf { Q } ) = \operatorname* { d e t } \mathbf { S } \operatorname* { d e t } ( \mathbf { P } - \mathbf { Q } \cdot \mathbf { S } ^ { - 1 } \cdot \mathbf { R } )
$$

# 2.7.5 Indexed Storage of Sparse Matrices

We have already seen (-2.4) that tri- or band-diagonal matrices can be stored in a compact format that allocates storage only to elements that can be nonzero, plus perhaps a few wasted locations to make the bookkeeping easier. What about more general sparse matrices? When a sparse matrix of dimension $M \times N$ contains only a few times $M$ or $N$ nonzero elements (a typical case), it is surely inefficient — and often physically impossible — to allocate storage for all $M N$ elements. Even if one did allocate such storage, it would be inefficient or prohibitive in machine time to loop over all of it in search of nonzero elements.

Obviously some kind of indexed storage scheme is required, one that stores only nonzero matrix elements, along with sufficient auxiliary information to determine where an element logically belongs and how the various elements can be looped over in common matrix operations. Unfortunately, there is no one standard scheme in general use. Each scheme has its own pluses and minuses, depending on the application.

Before we look at sparse matrices, let’s consider the simpler problem of a sparse vector. The obvious data structure is a list of the nonzero values and another list of the corresponding locations:

# struct NRsparseCol

Sparse vector data structure. {

Int nrows;   
Int nvals; Number of rows.   
Maximum number of nonzeros.   
VecInt row_ind; Row indices of nonzeros.   
VecDoub val; Array of nonzero values.   
NRsparseCol(Int m,Int nnvals) : nrows(m), nvals(nnvals),   
row_ind(nnvals,0),val(nnvals,0.0) {} Constructor. Initializes vector to zero.   
NRsparseCol() : nrows(0),nvals(0),row_ind(),val() {} Default constructor.   
void resize(Int m, Int nnvals) { nrows $= ~ \mathrm { ~ m ~ }$ ; nvals $=$ nnvals; row_ind.assign(nnvals,0); val.assign(nnvals,0.0);   
}

# };

While we think of this as defining a column vector, you can use exactly the same data structure for a row vector — just mentally interchange the meaning of row and column for the variables. For matrices, however, we have to decide ahead of time whether to use row-oriented or column-oriented storage.

One simple scheme is to use a vector of sparse columns:

NRvector<NRsparseCol \*> a;   
for ( $\scriptstyle \dot { \mathtt { 1 } } = 0$ ;i<n; $\mathrm { i } + + \mathrm { j }$ ) { nvals=... a[i] $=$ new NRsparseCol(m,nvals);   
}

Each column is filled with statements like

count ${ = } 0$ ;   
for (j=...) { a[i]->row_ind[count] $=$ .. a[i]->val[count]=... count++;   
}

This data structure is good for an algorithm that primarily works with columns of the matrix, but it is not very efficient when one needs to loop over all elements of the matrix.

A good general storage scheme is the compressed column storage format. It is sometimes called the Harwell-Boeing format, after the two large organizations that first systematically provided a standard collection of sparse matrices for research purposes. In this scheme, three vectors are used: val for the nonzero values as they are traversed column by column, row_ind for the corresponding row indices of each value, and col_ptr for the locations in the other two arrays that start a column. In other words, if val[k] $= \mathtt { a }$ [i][j], then row_ind $[ \mathbf { k } ] = \dot { \mathbf { 1 } }$ . The first nonzero in column $\dot { \mathsf { J } }$ is at col_ptr[j]. The last is at col_ptr $[ j + 1 ] - 1$ . Note that col_ptr[0] is always 0, and by convention we define col_ptr[n] equal to the number of nonzeros. Note also that the dimension of the col_ptr array is $N + 1$ , not $N$ . The advantage of this scheme is that it requires storage of only about two times the number of nonzero matrix elements. (Other methods can require as much as three or five times.)

As an example, consider the matrix

$$
\left[ { \begin{array} { c c c c c c } { 3 . 0 } & { 0 . 0 } & { 1 . 0 } & { 2 . 0 } & { 0 . 0 } \\ { 0 . 0 } & { 4 . 0 } & { 0 . 0 } & { 0 . 0 } & { 0 . 0 } \\ { 0 . 0 } & { 7 . 0 } & { 5 . 0 } & { 9 . 0 } & { 0 . 0 } \\ { 0 . 0 } & { 0 . 0 } & { 0 . 0 } & { 0 . 0 } & { 0 . 0 } \\ { 0 . 0 } & { 0 . 0 } & { 0 . 0 } & { 6 . 0 } & { 5 . 0 } \end{array} } \right]
$$

In compressed column storage mode, matrix (2.7.27) is represented by two arrays of length 9 and an array of length 6, as follows

<table><tr><td rowspan=1 colspan=1>index k</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>&gt;</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>val[k]</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>7.0</td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>5.0</td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1>9.0</td><td rowspan=1 colspan=1>&gt;6.0</td><td rowspan=1 colspan=1>5.0</td></tr><tr><td rowspan=1 colspan=1>row_ind[k]</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td></tr></table>

<table><tr><td rowspan=1 colspan=1>index i</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>col_ptr[i]</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>9</td></tr></table>

Notice that, according to the storage rules, the value of $N$ (namely 5) is the maximum valid index in col_ptr. The value of col_ptr[5] is 9, the length of the other two arrays. The elements 1.0 and 5.0 in column number 2, for example, are located in positions col_ptr[2] $\leq$ $k < \mathsf { c o l \_ p t r } \left[ 3 \right]$ .

Here is a data structure to handle this storage scheme:

# sparse.h

# struct NRsparseMa

Sparse matrix data structure for compressed column storage. {

Int nrows; Number of rows.   
Int ncols; Number of columns.   
Int nvals; Maximum number of nonzeros.   
VecInt col_ptr; Pointers to start of columns. Length is ncols $+ 1$ .   
VecInt row_ind; Row indices of nonzeros.   
VecDoub val; Array of nonzero values. NRsparseMat(); Default constructor.   
NRsparseMat(Int m,Int n,Int nnvals); Constructor. Initializes vector to zero.   
VecDoub ax(const VecDoub &x) const; Multiply A by a vector x[0..ncols-1].   
VecDoub atx(const VecDoub &x) const; Multiply $\mathbf { A } ^ { T }$ by a vector x[0..nrows-1].   
NRsparseMat transpose() const; Form $\mathbf { \delta A } ^ { T }$ .

The code for the constructors is standard:

NRsparseMat::NRsparseMat() : nrows(0),ncols(0),nvals(0),col_ptr(), row_ind(),val() {}   
NRsparseMat::NRsparseMat(Int m,Int n,Int nnvals) : nrows(m),ncols(n), nvals(nnvals),col_ptr $( \mathtt { n } + 1$ ,0),row_ind(nnvals,0),val(nnvals,0.0) {}

The single most important use of a matrix in compressed column storage mode is to multiply a vector to its right. Don’t implement this by traversing the rows of A, which is extremely inefficient in this storage mode. Here’s the right way to do it:

# sparse.h

VecDoub NRsparseMat::ax(const VecDoub &x) const { VecDoub y(nrows,0.0); for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<ncols;j $^ { + + }$ ) { for (Int $\mathrm { i } =$ col_ptr[j];i<col_ptr[j+1];i++) y[row_ind[i]] $+ =$ val[i]\*x[j]; } return y;   
}

Some inefficiency occurs because of the indirect addressing. While there are other storage modes that minimize this, they have their own drawbacks.

It is also simple to multiply the transpose of a matrix by a vector to its right, since we just traverse the columns directly. (Indirect addressing is still required.) Note that the transpose matrix is not actually constructed.

VecDoub NRsparseMat::atx(const VecDoub &x) const { VecDoub y(ncols); for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<ncols; $\mathbf { i } + + \mathbf { i }$ ) { y[i] ${ = } 0$ .0; for (Int $\dot { \bf { \cal { J } } } ^ { = }$ col_ptr[i];j<col_ptr[i+1];j++) y[i] $+ =$ val[j]\*x[row_ind[j]]; return y;   
}

Because the choice of compressed column storage treats rows and columns quite differently, it is rather an involved operation to construct the transpose of a matrix, given the matrix itself in compressed column storage mode. When the operation cannot be avoided, it is

NRsparseMat NRsparseMat::transpose() const { Int i,j,k,index, $\mathbb { m } =$ nrows, $\mathbf { n } { = } 1$ ncols; NRsparseMat at(n,m,nvals); Initialized to zero. First find the column lengths for $\mathbf { A } ^ { T }$ , i.e. the row lengths of A. VecInt count(m,0); Temporary counters for each row of A. for ( $\scriptstyle \dot { 1 } = 0$ ;i<n; $\mathrm { i } + + \mathrm { j }$ ) for (j=col_ptr[i];j<col_ptr[i+1];j++) { ${ \bf k } = { \bf \ell }$ row_ind[j]; count[k] $^ { + + }$ ; } for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<m;j++) Now set at.col_ptr. 0th entry stays 0. at.col_ptr[j+1] $=$ at.col_ptr[j]+count[j]; for( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<m;j++) Reset counters to zero. count[j]=0; for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n;i++) Main loop. for (j=col_ptr[i];j<col_ptr[i+1];j++) { k=row_ind[j]; index at.col_ptr[k] $^ +$ count[k]; Element’s position in column of $\mathbf { A } ^ { T }$ . at.row_ind[index] ${ \bf \Phi } = \dot { \bf 1 }$ ; at.val[index] $=$ val[j]; count[k] $^ { + + }$ ; Increment counter for next element in tha } column. return at;

The only sparse matrix-matrix multiply routine we give is to form the product $\mathbf { A } \mathbf { D } \mathbf { A } ^ { T }$ , where $\mathbf { D }$ is a diagonal matrix. This particular product is used to form the so-called normal equations in the interior-point method for linear programming (-10.11). We encapsulate the algorithm in its own structure, ADAT:

struct ADAT { const NRsparseMat &a,&at; Store references to A and $\mathbf { A } ^ { T }$ . NRsparseMat \*adat; This will hold $\mathbf { A } \mathbf { D } \mathbf { A } ^ { T }$ .

# ADAT(const NRsparseMat &A,const NRsparseMat &AT);

Allocates compressed column storage for $\mathbf { A } \mathbf { A } ^ { T }$ , where $\mathbf { A }$ and $\mathbf { A } ^ { T }$ are input in compressed column format, and fills in values of col_ptr and row_ind. Each column must be in sorted order in input matrices. Matrix is output with each column sorted.   
void updateD(const VecDoub &D);   
Computes $\mathbf { A } \mathbf { D } \mathbf { A } ^ { T }$ , where $\mathbf { D }$ is a diagonal matrix. This function can be called repeatedly to update $\mathbf { A } \mathbf { D } \mathbf { A } ^ { T }$ for fixed A.   
NRsparseMat &ref();   
Returns reference to adat, which holds $\mathbf { A } \mathbf { D } \mathbf { A } ^ { T }$ .   
\~ADAT();

The algorithm proceeds in two steps. First, the nonzero pattern of $\mathbf { A } \mathbf { A } ^ { T }$ is found by a call to the constructor. Since $\mathbf { D }$ is diagonal, $\mathbf { A A } ^ { T }$ and $\mathbf { A } \mathbf { D } \mathbf { A } ^ { T }$ have the same nonzero structure. Algorithms using ADAT will typically have both A and ${ \bf A } ^ { T }$ available, so we pass them both to the constructor rather than recompute ${ \bf A } ^ { T }$ from A. The constructor allocates storage and assigns values to col_ptr and row_ind. The structure of ADAT is returned with columns in sorted order because routines like the AMD ordering algorithm used in $\ S 1 0 . 1 1$ require it.

AT::ADAT(const NRsparseMat &A,const NRsparseMat &AT) : a(A), at(AT) {   
Int h,i,j,k,l,nvals, ${ \tt m } { = } \tt { A T }$ .ncols;   
VecInt done(m);   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<m; $\dot { 1 } + +$ ) Initialize to not done. done[i] $= - 1$ ;   
nvals=0; First pass determines number of nonzeros.   
for ( $\scriptstyle \mathbf { j } = 0$ ;j<m;j $^ { + + }$ ) { Outer loop over columns of $\mathbf { A } ^ { T }$ in $\mathbf { A } \mathbf { A } ^ { T }$ . for ( $\mathrm { i } =$ AT.col_ptr[j];i<AT.col_ptr[j+1];i++) k=AT.row_ind[i]; $\mathbf { A } _ { k j } ^ { T } \neq \mathbf { 0 }$ . Find column $k$ in first matrix, A. for (l=A.col_ptr[k];l<A.col_ptr[k+1]; $; 1 + + )$ { $\mathtt { h } = \mathtt { A }$ .row_ind[l]; $\mathbf { A } _ { h l } \neq \mathbf { 0 }$ . if (done[h] $\ ! =$ j) { Test if contribution already included. done[h]=j; nvals++; } } }   
}   
adat $=$ new NRsparseMat(m,m,nvals); Allocate storage for ADAT.   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<m; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \beta } } } .$ ) Re-initialize. done[i] $= - 1$ ;   
nvals ${ = } 0$ ;   
Second pass: Determine columns of adat. Code is identical to first pass except adat->col_ptr   
and adat->row_ind get assigned at appropriate places.   
for (j=0;j<m;j++) { adat->col_ptr[j] $=$ nvals; for ( $\dot { \bf 1 } =$ AT.col_ptr[j];i<AT.col_ptr[j+1];i++) { k=AT.row_ind[i]; for (l=A.col_ptr[k];l<A.col_ptr[k+1];l++) { ${ \bf h } { = } { \bf A }$ .row_ind[l]; if (done[h] $\ ! =$ j) { done[h]=j; adat->row_ind[nvals]=h; nvals++; } } }   
1   
adat->col_ptr[m] $=$ nvals; Set last value.   
for $( \ j = 0$ ;j<m;j++) { Sort columns $\dot { \bf 1 } =$ adat->col_ptr[j]; Int size $=$ adat->col_ptr[j+1]-i; if (size > 1) { VecInt col(size,&adat->row_ind[i]); sort(col); for $\scriptstyle 1 = 0$ ;k<size;k++) adat->row_ind[i+k] $=$ col[k]; }   
}

The next routine, updateD, actually fills in the values in the val array. It can be called repeatedly to update $\mathbf { A } \mathbf { D } \mathbf { A } ^ { T }$ for fixed A.

void ADAT::updateD(const VecDoub &D) { Int h,i,j,k,l, $\mathtt { m } = \mathtt { a }$ .nrows, $\mathtt { n } = \mathtt { a }$ .ncols; VecDoub temp(n),temp2(m,0.0); for ( $\scriptstyle \dot { 1 } = 0$ ;i<m; $\dot { \bar { \lambda } } + +$ ) { Outer loop over columns of $\mathbf { A } ^ { T }$ . for (j=at.col_ptr[i];j< at.col_ptr[i+1];j++) ${ \bf k } = { \bf \ell }$ at.row_ind[j]; Scale elements of each column with $\mathbf { D }$ and temp[k] $=$ at.val[j]\*D[k]; store in temp. } for (j=at.col_ptr[i];j<at.col_ptr[i+1];j++) { Go down column again. $\mathrm { k } =$ at.row_ind[j]; for ( $\mathtt { \_ l = a }$ .col_ptr[k];l<a.col_ptr[k+1]; $1 + +$ ) { Go down column $k$ in h=a.row_ind[l]; A. temp2[h] $+ =$ temp[k]\*a.val[l]; All terms from temp[k] used here. } } for (j=adat->col_ptr[i];j<adat->col_ptr[i+1];j++) { Store temp2 in column of answer. k=adat->row_ind[j]; adat->val[j] $=$ temp2[k]; temp2[k] ${ = } 0$ .0; Restore temp2. } }   
}

The final two functions are simple. The ref routine returns a reference to the matrix $\mathbf { A } \mathbf { D } \mathbf { A } ^ { T }$ stored in the structure for other routines that may need to work with it. And the destructor releases the storage.

NRsparseMat & ADAT::ref() { return \*adat;   
}   
ADAT::\~ADAT() { delete adat;   
}

By the way, if you invoke ADAT with different matrices A and $\mathbf { B } ^ { T }$ , everything will work fine as long as A and B have the same nonzero pattern.

In Numerical Recipes second edition, we gave a related sparse matrix storage mode in which the diagonal of the matrix is stored first, followed by the off-diagonal elements. We now feel that the added complexity of that scheme is not worthwhile for any of the uses in this book. For a discussion of this and other storage schemes, see [7,8]. To see how to work with the diagonal in the compressed column mode, look at the code for asolve at the end of this section.

# 2.7.6 Conjugate Gradient Method for a Sparse System

So-called conjugate gradient methods provide a quite general means for solving the $N \times N$ linear system

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

The attractiveness of these methods for large sparse systems is that they reference A only through its multiplication of a vector, or the multiplication of its transpose and a vector. As we have seen, these operations can be very efficient for a properly stored sparse matrix. You, the “owner” of the matrix A, can be asked to provide functions that perform these sparse matrix multiplications as efficiently as possible. We, the “grand strategists,” supply an abstract base class, Linbcg below, that contains the method for solving the set of linear equations, (2.7.29), using your functions.

The simplest, “ordinary” conjugate gradient algorithm [9-11] solves (2.7.29) only in the case that A is symmetric and positive-definite. It is based on the idea of minimizing the function

$$
\begin{array} { r } { f ( \mathbf { x } ) = \frac { 1 } { 2 } \mathbf { x } \cdot \mathbf { A } \cdot \mathbf { x } - \mathbf { b } \cdot \mathbf { x } } \end{array}
$$

This function is minimized when its gradient

$$
\nabla f = \mathbf { A } \cdot \mathbf { x } - \mathbf { b }
$$

is zero, which is equivalent to (2.7.29). The minimization is carried out by generating a succession of search directions $\mathbf { p } _ { k }$ and improved minimizers $\mathbf { x } _ { k }$ . At each stage a quantity $\alpha _ { k }$ is found that minimizes $f ( \mathbf { x } _ { k } + \alpha _ { k } \mathbf { p } _ { k } )$ , and $\mathbf { X } _ { k + 1 }$ is set equal to the new point $\mathbf { x } _ { k } + \alpha _ { k } \mathbf { p } _ { k }$ . The $\mathbf { p } _ { k }$ and $\mathbf { x } _ { k }$ are built up in such a way that $\mathbf { X } _ { k + 1 }$ is also the minimizer of $f$ over the whole vector space of directions already taken, $\left\{ \mathbf { p } _ { 0 } , \mathbf { p } _ { 1 } , \ldots , \mathbf { p } _ { k - 1 } \right\}$ . After $N$ iterations you arrive at the minimizer over the entire vector space, i.e., the solution to (2.7.29).

Later, in $\ S 1 0 . 8$ , we will generalize this “ordinary” conjugate gradient algorithm to the minimization of arbitrary nonlinear functions. Here, where our interest is in solving linear, but not necessarily positive-definite or symmetric, equations, a different generalization is important, the biconjugate gradient method. This method does not, in general, have a simple connection with function minimization. It constructs four sequences of vectors, $\mathbf { r } _ { k }$ ${ \bf \Lambda } _ { k } , \overline { { \bf r } } _ { k } , { \bf p } _ { k }$ , $\overline { { \mathbf { p } } } _ { k }$ ${ \bf \Psi } _ { k } , k = 0 , 1 , \ldots .$ You supply the initial vectors $\mathbf { r } _ { 0 }$ and $\overline { { \mathbf { r } } } _ { 0 }$ , and set $\mathbf { p } _ { 0 } = \mathbf { r } _ { 0 } , \mathbf { \overline { { p } } } _ { 0 } = \mathbf { \overline { { r } } } _ { 0 }$ . Then you carry out the following recurrence:

$$
\begin{array} { r l } & { \alpha _ { k } = \frac { \overline { { \mathbf { r } } } _ { k } \cdot \mathbf { r } _ { k } } { \overline { { \mathbf { p } } } _ { k } \cdot \mathbf { A } \cdot \mathbf { p } _ { k } } } \\ & { \mathbf { r } _ { k + 1 } = \mathbf { r } _ { k } - \alpha _ { k } \mathbf { A } \cdot \mathbf { p } _ { k } } \\ & { \overline { { \mathbf { r } } } _ { k + 1 } = \overline { { \mathbf { r } } } _ { k } - \alpha _ { k } \mathbf { A } ^ { T } \cdot \overline { { \mathbf { p } } } _ { k } } \\ & { \qquad \beta _ { k } = \frac { \overline { { \mathbf { r } } } _ { k + 1 } \cdot \mathbf { r } _ { k + 1 } } { \overline { { \mathbf { r } } } _ { k } \cdot \mathbf { r } _ { k } } } \\ & { \qquad \mathbf { p } _ { k + 1 } = \mathbf { r } _ { k + 1 } + \beta _ { k } \mathbf { p } _ { k } } \\ & { \qquad \overline { { \mathbf { p } } } _ { k + 1 } = \overline { { \mathbf { r } } } _ { k + 1 } + \beta _ { k } \overline { { \mathbf { p } } } _ { k } } \end{array}
$$

This sequence of vectors satisfies the biorthogonality condition

$$
\overline { { \mathbf { r } } } _ { i } \cdot \mathbf { r } _ { j } = \mathbf { r } _ { i } \cdot \overline { { \mathbf { r } } } _ { j } = 0 , \qquad j < i
$$

and the biconjugacy condition

$$
\overline { { \mathbf { p } } } _ { i } \cdot \mathbf { A } \cdot \mathbf { p } _ { j } = \mathbf { p } _ { i } \cdot \mathbf { A } ^ { T } \cdot \overline { { \mathbf { p } } } _ { j } = 0 , \qquad j < i
$$

There is also a mutual orthogonality,

$$
\overline { { \mathbf { r } } } _ { i } \cdot \mathbf { p } _ { j } = \mathbf { r } _ { i } \cdot \overline { { \mathbf { p } } } _ { j } = 0 , \qquad j < i
$$

The proof of these properties proceeds by straightforward induction [12]. As long as the recurrence does not break down earlier because one of the denominators is zero, it must terminate after $m \leq N$ steps with $\mathbf { r } _ { m } = \overline { { \mathbf { r } } } _ { m } = 0$ . This is basically because after at most $N$ steps you run out of new orthogonal directions to the vectors you’ve already constructed.

To use the algorithm to solve the system (2.7.29), make an initial guess $\mathbf { x } _ { 0 }$ for the solution. Choose $\mathbf { r } _ { 0 }$ to be the residual

$$
\mathbf { r } _ { 0 } = \mathbf { b } - \mathbf { A } \cdot \mathbf { x } _ { 0 }
$$

and choose $\overline { { \mathbf { r } } } _ { 0 } = \mathbf { r } _ { 0 }$ . Then form the sequence of improved estimates

$$
\mathbf { x } _ { k + 1 } = \mathbf { x } _ { k } + \alpha _ { k } \mathbf { p } _ { k }
$$

while carrying out the recurrence (2.7.32). Equation (2.7.37) guarantees that $\mathbf { r } _ { k + 1 }$ from the recurrence is in fact the residual $\mathbf { b } - \mathbf { A } \cdot \mathbf { x } _ { k + 1 }$ corresponding to $\mathbf { X } _ { k + 1 }$ . Since $\mathbf { r } _ { m } = 0$ , $\mathbf { X } _ { m }$ is the solution to equation (2.7.29).

While there is no guarantee that this whole procedure will not break down or become unstable for general $\mathbf { A }$ , in practice this is rare. More importantly, the exact termination in at most $N$ iterations occurs only with exact arithmetic. Roundoff error means that you should regard the process as a genuinely iterative procedure, to be halted when some appropriate error criterion is met.

The ordinary conjugate gradient algorithm is the special case of the biconjugate gradient algorithm when A is symmetric, and we choose $\overline { { \mathbf { r } } } _ { 0 } = \mathbf { r } _ { 0 }$ . Then $\overline { { \mathbf { r } } } _ { k } = \mathbf { r } _ { k }$ and $\overline { { \mathbf { p } } } _ { k } = \mathbf { p } _ { k }$ for all $k$ ; you can omit computing them and halve the work of the algorithm. This conjugate gradient version has the interpretation of minimizing equation (2.7.30). If A is positive-definite as well as symmetric, the algorithm cannot break down (in theory!). The solve routine Linbcg below indeed reduces to the ordinary conjugate gradient method if you input a symmetric A, but it does all the redundant computations.

Another variant of the general algorithm corresponds to a symmetric but non-positivedefinite $\mathbf { A }$ , with the choice $\overline { { \mathbf { r } } } _ { 0 } = \mathbf { A } \cdot \mathbf { r } _ { 0 }$ instead of $\overline { { { \mathbf { r } } } } _ { 0 } = \mathbf { r } _ { 0 }$ . In this case $\overline { { \mathbf { r } } } _ { k } = \mathbf { A } \cdot \mathbf { r } _ { k }$ and $\overline { { \mathbf { p } } } _ { k } = \mathbf { A } \cdot \mathbf { p } _ { k }$ for all $k$ . This algorithm is thus equivalent to the ordinary conjugate gradient algorithm, but with all dot products a $\mathbf { \nabla } \cdot \mathbf { b }$ replaced by a $\mathbf { \nabla } \cdot \mathbf { A } \cdot \mathbf { b }$ . It is called the minimum residual algorithm, because it corresponds to successive minimizations of the function

$$
\begin{array} { r } { \Phi ( \mathbf { x } ) = \frac { 1 } { 2 } \mathbf { r } \cdot \mathbf { r } = \frac { 1 } { 2 } | \mathbf { A } \cdot \mathbf { x } - \mathbf { b } | ^ { 2 } } \end{array}
$$

where the successive iterates $\mathbf { x } _ { k }$ minimize $\Phi$ over the same set of search directions $\mathbf { p } _ { k }$ generated in the conjugate gradient method. This algorithm has been generalized in various ways for unsymmetric matrices. The generalized minimum residual method (GMRES; see [13,14]) is probably the most robust of these methods.

Note that equation (2.7.38) gives

$$
\nabla \Phi ( { \bf x } ) = { \bf A } ^ { T } \cdot ( { \bf A } \cdot { \bf x } - { \bf b } )
$$

For any nonsingular matrix A, $\mathbf { A } ^ { T } \cdot \mathbf { A }$ is symmetric and positive-definite. You might therefore be tempted to solve equation (2.7.29) by applying the ordinary conjugate gradient algorithm to the problem

$$
( \mathbf { A } ^ { T } \cdot \mathbf { A } ) \cdot \mathbf { x } = \mathbf { A } ^ { T } \cdot \mathbf { b }
$$

Don’t! The condition number of the matrix $\mathbf { A } ^ { T } \cdot \mathbf { A }$ is the square of the condition number of A (see $\ S 2 . 6$ for definition of condition number). A large condition number both increases the number of iterations required and limits the accuracy to which a solution can be obtained. It is almost always better to apply the biconjugate gradient method to the original matrix A.

So far we have said nothing about the rate of convergence of these methods. The ordinary conjugate gradient method works well for matrices that are well-conditioned, i.e., “close” to the identity matrix. This suggests applying these methods to the preconditioned form of equation (2.7.29),

$$
( \widetilde \mathbf { A } ^ { - 1 } \cdot \mathbf { A } ) \cdot \mathbf { x } = \widetilde { \mathbf { A } } ^ { - 1 } \cdot \mathbf { b }
$$

The idea is that you might already be able to solve your linear system easily for some $\widetilde { \mathbf { A } }$ close to A, in which case $\widetilde { \mathbf { A } } ^ { - 1 }$ $\mathbf A \approx \mathbf 1$ , allowing the algorithm to converge in fewer steps. The matrix $\widetilde { \bf A }$ is called a preconditioner [9], and the overall scheme given here is known as the preconditioned biconjugate gradient method or PBCG. In the code below, the user-supplied routine atimes does sparse matrix multiplication by $\mathbf { A }$ , while the user-supplied routine asolve effects matrix multiplication by the inverse of the preconditioner $\widetilde { \mathbf { A } } ^ { - 1 }$

For efficient implementation, the PBCG algorithm introduces an additional set of vectors $\mathbf { z } _ { k }$ and $\overline { { \mathbf { z } } } _ { k }$ defined by

$$
\begin{array} { r } { \widetilde { \mathbf { A } } \cdot \mathbf { z } _ { k } = \mathbf { r } _ { k } \qquad \mathrm { a n d } \qquad \widetilde { \mathbf { A } } ^ { T } \cdot \overline { { \mathbf { z } } } _ { k } = \overline { { \mathbf { r } } } _ { k } } \end{array}
$$

and modifies the definitions of $\alpha _ { k }$ $, \beta _ { k } , \mathbf { p } _ { k }$ , and $\overline { { \mathbf { p } } } _ { k }$ in equation (2.7.32):

$$
\begin{array} { c } { \alpha _ { k } = \frac { \overline { { \mathbf { r } } } _ { k } \cdot \mathbf { z } _ { k } } { \overline { { \mathbf { p } } } _ { k } \cdot \mathbf { A } \cdot \mathbf { p } _ { k } } } \\ { \beta _ { k } = \frac { \overline { { \mathbf { r } } } _ { k + 1 } \cdot \mathbf { z } _ { k + 1 } } { \overline { { \mathbf { r } } } _ { k } \cdot \mathbf { z } _ { k } } } \\ { \mathbf { p } _ { k + 1 } = \mathbf { z } _ { k + 1 } + \beta _ { k } \mathbf { p } _ { k } } \\ { \overline { { \mathbf { p } } } _ { k + 1 } = \overline { { \mathbf { z } } } _ { k + 1 } + \beta _ { k } \overline { { \mathbf { p } } } _ { k } } \end{array}
$$

To use Linbcg, below, you will need to supply routines that solve the auxiliary linear systems (2.7.42). If you have no idea what to use for the preconditioner $\widetilde { \mathbf { A } }$ , then use the diagonal part of A, or even the identity matrix, in which case the burden of convergence will be entirely on the biconjugate gradient method itself.

Linbcg’s routine solve, below, is based on a program originally written by Anne Greenbaum. (See [11] for a different, less sophisticated, implementation.) There are a few wrinkles you should know about.

What constitutes “good” convergence is rather application-dependent. The routine solve therefore provides for four possibilities, selected by setting the flag itol on input. If itol $\sp { = 1 }$ , iteration stops when the quantity $\left| \mathbf { A \cdot x - b } \right| / \left| \mathbf { b } \right|$ is less than the input quantity tol. If itol $^ { = 2 }$ , the required criterion is

$$
| \widetilde { \mathbf { A } } ^ { - 1 } \cdot ( \mathbf { A } \cdot \mathbf { x } - \mathbf { b } ) | / | \widetilde { \mathbf { A } } ^ { - 1 } \cdot \mathbf { b } | < \mathtt { t o l }
$$

If $\mathtt { i t o l } { = } 3$ , the routine uses its own estimate of the error in $\mathbf { X }$ and requires its magnitude, divided by the magnitude of $\mathbf { X }$ , to be less than tol. The setting $\dot { 1 } \ t { 0 } 1 = 4$ is the same as $\mathtt { i t o l } { = } 3$ , except that the largest (in absolute value) component of the error and largest component of $\mathbf { X }$ are used instead of the vector magnitude (that is, the $L _ { \infty }$ norm instead of the $L _ { 2 }$ norm). You may need to experiment to find which of these convergence criteria is best for your problem.

On output, err is the tolerance actually achieved. If the returned count iter does not indicate that the maximum number of allowed iterations itmax was exceeded, then err should be less than tol. If you want to do further iterations, leave all returned quantities as they are and call the routine again. The routine loses its memory of the spanned conjugate gradient subspace between calls, however, so you should not force it to return more often than about every $N$ iterations.

# struct Linbcg {

Abstract base class for solving sparse linear equations by the preconditioned biconjugate gradient method. To use, declare a derived class in which the methods atimes and asolve are defined for your problem, along with any data that they need. Then call the solve method.

virtual void asolve(VecDoub_I &b, VecDoub_O &x, const Int itrnsp) $\mathit { \Theta } = \mathit { \Theta } 0$ ; virtual void atimes(VecDoub_I &x, VecDoub_O &r, const Int itrnsp) $\mathit { \Theta } = \mathit { \Theta } 0$ ; void solve(VecDoub_I &b, VecDoub_IO &x, const Int itol, const Doub tol, const Int itmax, Int &iter, Doub &err); Doub snrm(VecDoub_I &sx, const Int itol); Utility used by solve. ;

#

void Linbcg::solve(VecDoub_I &b, VecDoub_IO &x, const Int itol, const Doub tol,const Int itmax, Int &iter, Doub &err)

Solves $\mathbf { A \cdot x } = \mathbf { b }$ for $\mathbf { x } \left[ 0 \ldots \ldots \right]$ , given $\mathtt { b } \left[ 0 \ldots \mathtt { n - 1 } \right]$ , by the iterative biconjugate gradient method. On input $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ should be set to an initial guess of the solution (or all zeros); itol is 1,2,3, or 4, specifying which convergence test is applied (see text); itmax is the maximum number of allowed iterations; and tol is the desired convergence tolerance. On output, $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ is reset to the improved solution, iter is the number of iterations actually taken, and err is the estimated error. The matrix $\mathbf { A }$ is referenced only through the user-supplied routines atimes, which computes the product of either A or its transpose on a vector, and asolve, which solves $\widetilde { \mathbf { A } } \cdot \mathbf { x } = \mathbf { b }$ or $\tilde { \mathbf { A } } ^ { T } \cdot \mathbf { x } = \mathbf { b }$ for some preconditioner matrix Az (possibly the trivial diagonal part of A). This routine can be called repeatedly, with itmax.n, to monitor how err decreases; or it can be called once with a sufficiently large value of itmax so that convergence to tol is achieved.

Doub ak,akden,bk,bkden $= 1$ .0,bknum,bnrm,dxnrm,xnrm,zm1nrm,znrm;   
const Doub EPS=1.0e-14;   
Int j, $\mathtt { n } { = } \mathtt { b }$ .size();   
VecDoub p(n),pp(n),r(n),rr(n),z(n),zz(n);   
iter ${ = } 0$ ; Calculate initial residual.   
atimes(x,r,0); Input to atimes is $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ , output is r[0..n-1];   
for (j=0;j<n;j++) { the final 0 indicates that the matrix (not its r[j]=b[j]-r[j]; transpose) is to be used. rr[j]=r[j];   
}   
times(r,rr,0); Uncomment this line to get the “minimum resid-  
(itol $\scriptstyle = = \ 1$ ) { ual” variant of the algorithm.   
bnrm=snrm(b,itol);   
asolve(r,z,0); Input to asolve is $\mathbf { r } \left[ 0 \ldots \ldots \right]$ , output is $z [ \binom { 0 } { \sim } \cdot \cdot \cdot \mathbf { n } ^ { - 1 ] }$ the final 0 indicates that the matrix $\bar { \bf A }$ (not   
e if (itol $= = ~ 2$ ) { its transpose) is to be used.   
asolve(b,z,0);   
bnrm=snrm(z,itol);   
asolve(r,z,0);   
e if (itol $\scriptstyle = = 3$ || itol == 4) {   
asolve(b,z,0);   
bnrm=snrm(z,itol);   
asolve(r,z,0);   
znrm=snrm(z,itol);   
lse throw("illegal itol in linbcg");   
le (iter $<$ itmax) { Main loop.   
$^ { + + }$ iter;   
asolve(rr,zz,1); Final 1 indicates use of transpose matrix $\widetilde { \mathbf { A } } ^ { T }$ .   
for (bknum $_ { 1 = 0 }$ .0, $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) bknum $+ = \ z$ [j]\*rr[j];   
Calculate coefficient bk and direction vectors p and pp.   
if (iter == 1) { for (j=0;j<n;j++) { p[j] $= _ { 2 }$ [j]; pp[j]=zz[j];   
} else { bk=bknum/bkden; for (j=0;j<n;j++) { p[j]=bk\*p[j]+z[j]; pp[j]=bk\*pp[j]+zz[j]; }   
bkden bknum; Calculate coefficient ak, new iterate $\mathbf { x }$ , and new   
atimes(p,z,0); residuals r and rr.   
for (akden=0.0,j=0;j<n;j++) akden $+ = \ z$ [j]\*pp[j];   
ak=bknum/akden;   
atimes(pp,zz,1);   
for (j=0;j<n;j++) { x[j] $+ =$ ak\*p[j]; r[j] $- =$ ak\*z[j]; rr[j] $- =$ ak\*zz[j];   
asolve(r,z,0); Solve $\widetilde { \mathbf { A } } \cdot \mathbf { z } = \mathbf { r }$ and check stopping criterion.   
if (itol $\scriptstyle \mathbf { \mu = } \mathbf { \mu 1 }$ ) err=snrm(r,itol)/bnrm;   
else if (itol $= = ~ 2$ ) err=snrm(z,itol)/bnrm;   
else if (itol $\scriptstyle = = 3$ || itol == 4) { zm1nrm=znrm; znrm=snrm(z,itol); if (abs(zm1nrm-znrm) > EPS\*znrm) { dxnrm=abs(ak)\*snrm(p,itol); err=znrm/abs(zm1nrm-znrm)\*dxnrm; } else { err=znrm/bnrm; Error may not be accurate, so loop again. continue; } xnrm=snrm(x,itol); if (err $< =$ 0.5\*xnrm) err /= xnrm; else { err=znrm/bnrm; Error may not be accurate, so loop again. continue; }

} if (err <= tol) break; } }

The solve routine uses this short utility for computing vector norms:

Doub Linbcg::snrm(VecDoub_I &sx, const Int itol)   
Compute one of two norms for a vector sx[0..n-1], as signaled by itol. Used by solve. {

Int i,isamax,n=sx.size(); Doub ans; if (itol $\scriptstyle < = \ 3$ ) { ans $= ~ 0 . 0$ ; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) ans $+ =$ SQR(sx[i]); Vector magnitude norm. return sqrt(ans); } else { isamax $_ { = 0 }$ ; for (i=0;i<n;i++) { Largest component norm. if (abs(sx[i]) > abs(sx[isamax])) isamax ${ \mathop = } \dot { \beth }$ ; } return abs(sx[isamax]); } }

Here is an example of a derived class that solves $\mathbf { A \cdot X } = \mathbf { b }$ for a matrix A in NRsparseMat’s compressed column sparse format. A naive diagonal preconditioner is used.

struct NRsparseLinbcg : Linbcg { NRsparseMat &mat; Int n; NRsparseLinbcg(NRsparseMat &matrix) : mat(matrix), n(mat.nrows) {} The constructor just binds a reference to your sparse matrix, making it available to asolve and atimes. To solve for a right-hand side, you call this object’s solve method, as defined in the base class. void atimes(VecDoub_I &x, VecDoub_O &r, const Int itrnsp) { if (itrnsp) $\mathbf { \boldsymbol { x } } =$ mat.atx(x); else $x =$ mat.ax(x); } void asolve(VecDoub_I &b, VecDoub_O &x, const Int itrnsp) { Int i,j; Doub diag; for ( $\scriptstyle \dot { \mathtt { 1 } } = 0$ ;i<n;i++) { diag ${ = } 0$ .0; for (j=mat.col_ptr[i];j<mat.col_ptr[i+1];j++) if (mat.row_ind[j] $\mathbf { \lambda } = \mathbf { \lambda } \dot { \mathbf { \lambda } } $ ) { diag=mat.val[j]; break; } x[i] $=$ (diag $\smash { \downarrow = \ 0 , 0 }$ ? b[i]/diag : b[i]); The matrix $\widetilde { \mathbf { A } }$ is the diagonal part of A. Since the transpose matrix has the same diagonal, the flag itrnsp is not used in this example. } }   
};

For another example of using a class derived from Linbcg to solve a sparse matrix problem, see $\ S 3 . 8$ .

# CITED REFERENCES AND FURTHER READING:

Tewarson, R.P. 1973, Sparse Matrices (New York: Academic Press).[1]

Jacobs, D.A.H. (ed.) 1977, The State of the Art in Numerical Analysis (London: Academic Press), Chapter I.3 (by J.K. Reid).[2]   
George, A., and Liu, J.W.H. 1981, Computer Solution of Large Sparse Positive Definite Systems (Englewood Cliffs, NJ: Prentice-Hall).[3]   
NAG Fortran Library(Oxford, UK: Numerical Algorithms Group), see $^ { 2 0 0 7 + }$ ,http://www.nag. co.uk.[4]   
IMSLMath/Library Users Manual (Houston: IMSL Inc.),see $^ { 2 0 0 7 + }$ ,http://www.vni.com/ products/imsl.[5]   
Eisenstat, S.C., Gursky, M.C., Schultz, M.H., and Sherman, A.H. 1977, Yale Sparse Matrix Package,Technical Reports 112 and 114 (Yale University Department of Computer Science).[6]   
Bai, Z., Demmel, J., Dongarra, J. Ruhe, A., and van der Vorst, H. (eds.) 2000, Templates for the Solution of Algebraic Eigenvalue Problems:A Practical Guide Ch.10 (Philadelphia: S.I.A.M.). Online at URL in http://www.cs.ucdavis.edu/\~bai/ET/contents.html.[7]   
SPARSKIT, $^ { 2 0 0 7 + }$ ,at http://www-users.cs.umn.edu/\~saad/software/SPARSKIT/ sparskit.html.[8]   
Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), Chapters 4 and 10, particularly $\ S 1 0 . 2 \mathrm { - } \ S 1 0 . 3 . [ \ S$ 9]   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 8.[10]   
Baker, L. 1991, More C Tools for Scientists and Engineers (New York: McGraw-Hill).[11]   
Fletcher, R. 1976, in Numerical Analysis Dundee 1975, Lecture Notes in Mathematics, vol. 506, A. Dold and B Eckmann, eds. (Berlin: Springer), pp. 73–89.[12]   
PCGPAK User's Guide (New Haven: Scientific Computing Associates, Inc.).[13]   
Saad, Y., and Schulz, M. 1986, SIAM Journal on Scientific and Statistical Computing, vol. 7, pp. 856–869.[14]   
Ueberhuber, C.W. 1997, Numerical Computation: Methods Software and Analysis, 2 vols. (Berlin: Springer), Chapter 13.   
Bunch, J.R., and Rose, D.J. (eds.) 1976, Sparse Matrix Computations (New York: Academic Press).   
Duff, I.S., and Stewart, G.W. (eds.) 1979, Sparse Matrix Proceedings 1978 (Philadelphia: S.I.A.M.).

# 2.8 Vandermonde Matrices and Toeplitz Matrices

In $\ S 2 . 4$ the case of a tridiagonal matrix was treated specially, because that particular type of linear system admits a solution in only of order $N$ operations, rather than of order $N ^ { 3 }$ for the general linear problem. When such particular types exist, it is important to know about them. Your computational savings, should you ever happen to be working on a problem that involves the right kind of particular type, can be enormous.

This section treats two special types of matrices that can be solved in of order $N ^ { 2 }$ operations, not as good as tridiagonal, but a lot better than the general case. (Other than the operations count, these two types having nothing in common.) Matrices of the first type, termed Vandermonde matrices, occur in some problems having to do with the fitting of polynomials, the reconstruction of distributions from their moments, and also other contexts. In this book, for example, a Vandermonde problem crops up in $\ S 3 . 5$ . Matrices of the second type, termed Toeplitz matrices, tend to occur in problems involving deconvolution and signal processing. In this book, a Toeplitz problem is encountered in $\ S 1 3 . 7$ .

These are not the only special types of matrices worth knowing about. The Hilbert matrices, whose components are of the form $a _ { i j } = 1 / ( i + j + 1 )$ ; $i , j =$ $0 , \ldots , N - 1$ , can be inverted by an exact integer algorithm and are very difficult to invert in any other way, since they are notoriously ill-conditioned (see [1] for details). The Sherman-Morrison and Woodbury formulas, discussed in $\ S 2 . 7$ , can sometimes be used to convert new special forms into old ones. Reference [2] gives some other special forms. We have not found these additional forms to arise as frequently as the two that we now discuss.

# 2.8.1 Vandermonde Matrices

A Vandermonde matrix of size $N \times N$ is completely determined by $N$ arbitrary numbers $x _ { 0 } , x _ { 1 } , \ldots , x _ { N - 1 }$ , in terms of which its $N ^ { 2 }$ components are the integer powers $x _ { i } ^ { j }$ ; $i , j =$ $0 , \ldots , N - 1$ . Evidently there are two possible such forms, depending on whether we view the $i$ ’s as rows and $j$ ’s as columns, or vice versa. In the former case, we get a linear system of equations that looks like this,

$$
\left[ \begin{array} { c c c c c } { 1 } & { x _ { 0 } } & { x _ { 0 } ^ { 2 } } & { \cdots } & { x _ { 0 } ^ { N - 1 } } \\ { 1 } & { x _ { 1 } } & { x _ { 1 } ^ { 2 } } & { \cdots } & { x _ { 1 } ^ { N - 1 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { 1 } & { x _ { N - 1 } } & { x _ { N - 1 } ^ { 2 } } & { \cdots } & { x _ { N - 1 } ^ { N - 1 } } \end{array} \right] \cdot \left[ \begin{array} { c } { c _ { 0 } } \\ { c _ { 1 } } \\ { \vdots } \\ { c _ { N - 1 } } \end{array} \right] = \left[ \begin{array} { c } { y _ { 0 } } \\ { y _ { 1 } } \\ { \vdots } \\ { y _ { N - 1 } } \end{array} \right]
$$

Performing the matrix multiplication, you will see that this equation solves for the unknown coefficients $c _ { i }$ that fit a polynomial to the $N$ pairs of abscissas and ordinates $( x _ { j } , y _ { j } )$ . Precisely this problem will arise in $\ S 3 . 5$ , and the routine given there will solve (2.8.1) by the method that we are about to describe.

The alternative identification of rows and columns leads to the set of equations

$$
\left[ \begin{array} { c c c c } { { 1 } } & { { 1 } } & { { \cdots } } & { { 1 } } \\ { { x _ { 0 } } } & { { x _ { 1 } } } & { { \cdots } } & { { x _ { N - 1 } } } \\ { { x _ { 0 } ^ { 2 } } } & { { x _ { 1 } ^ { 2 } } } & { { \cdots } } & { { x _ { N - 1 } ^ { 2 } } } \\ & & { { \cdots } } & \\ { { x _ { 0 } ^ { N - 1 } } } & { { x _ { 1 } ^ { N - 1 } } } & { { \cdots } } & { { x _ { N - 1 } ^ { N - 1 } } } \end{array} \right] \cdot \left[ \begin{array} { c } { { w _ { 0 } } } \\ { { w _ { 1 } } } \\ { { w _ { 2 } } } \\ { { \cdots } } \\ { { w _ { N - 1 } } } \end{array} \right] = \left[ \begin{array} { c } { { q _ { 0 } } } \\ { { q _ { 1 } } } \\ { { q _ { 2 } } } \\ { { \cdots } } \\ { { q _ { N - 1 } } } \end{array} \right]
$$

Write this out and you will see that it relates to the problem of moments: Given the values of $N$ points $x _ { i }$ , find the unknown weights $w _ { i }$ , assigned so as to match the given values $q _ { j }$ of the first $N$ moments. (For more on this problem, consult [3].) The routine given in this section solves (2.8.2).

The method of solution of both (2.8.1) and (2.8.2) is closely related to Lagrange’s polynomial interpolation formula, which we will not formally meet until $\ S 3 . 2$ . Notwithstanding, the following derivation should be comprehensible:

Let $P _ { j } ( x )$ be the polynomial of degree $N - 1$ defined by

$$
P _ { j } ( x ) = \prod _ { { n = 0 } \atop { n \neq j } } ^ { N - 1 } { \frac { x - x _ { n } } { x _ { j } - x _ { n } } } = \sum _ { k = 0 } ^ { N - 1 } A _ { j k } x ^ { k }
$$

Here the meaning of the last equality is to define the components of the matrix $A _ { i j }$ as the coefficients that arise when the product is multiplied out and like terms collected.

The polynomial $P _ { j } ( x )$ is a function of $x$ generally. But you will notice that it is specifically designed so that it takes on a value of zero at all $x _ { i }$ with $i \neq j$ and has a value of unity at $x = x _ { j }$ . In other words,

$$
P _ { j } ( x _ { i } ) = \delta _ { i j } = \sum _ { k = 0 } ^ { N - 1 } A _ { j k } x _ { i } ^ { k }
$$

But (2.8.4) says that $A _ { j k }$ is exactly the inverse of the matrix of components $x _ { i } ^ { k }$ , which appears in (2.8.2), with the subscript as the column index. Therefore the solution of (2.8.2) is just that matrix inverse times the right-hand side,

$$
w _ { j } = \sum _ { k = 0 } ^ { N - 1 } A _ { j k } q _ { k }
$$

As for the transpose problem (2.8.1), we can use the fact that the inverse of the transpose is the transpose of the inverse, so

$$
c _ { j } = \sum _ { k = 0 } ^ { N - 1 } A _ { k j } y _ { k }
$$

The routine in $\ S 3 . 5$ implements this.

It remains to find a good way of multiplying out the monomial terms in (2.8.3), in order to get the components of $A _ { j k }$ . This is essentially a bookkeeping problem, and we will let you read the routine itself to see how it can be solved. One trick is to define a master $P ( x )$ by

$$
P ( x ) \equiv \prod _ { n = 0 } ^ { N - 1 } ( x - x _ { n } )
$$

work out its coefficients, and then obtain the numerators and denominators of the specific $P _ { j }$ ’s via synthetic division by the one supernumerary term. (See $\ S 5 . 1$ for more on synthetic division.) Since each such division is only a process of order $N$ , the total procedure is of order $N ^ { 2 }$ .

You should be warned that Vandermonde systems are notoriously ill-conditioned, by their very nature. (As an aside anticipating $\ S 5 . 8$ , the reason is the same as that which makes Chebyshev fitting so impressively accurate: There exist high-order polynomials that are very good uniform fits to zero. Hence roundoff error can introduce rather substantial coefficients of the leading terms of these polynomials.) It is a good idea always to compute Vandermonde problems in double precision or higher.

The routine for (2.8.2) that follows is due to G.B. Rybicki.

void vander(VecDoub_I &x, VecDoub_O &w, VecDoub_I &q)

Solves the Vaof the vectors lineaand $\begin{array} { r } { \sum _ { i = 0 } ^ { N - 1 } x _ { i } ^ { k } w _ { i } = q _ { k } } \end{array}$ $( k = 0 , \ldots , N - 1 )$ . Input consists $\mathbf { x } \left[ 0 \ldots \ldots \right] $ ${ \mathfrak { q } } \left[ 0 \ldots \cdot { \mathfrak { n } } ^ { - 1 ] } \right.$ $\mathtt { w } \left[ 0 \ldots \ldots \ldots 1 \right]$

Int i,j,k, $\mathtt { n } { } ^ { = } { \mathtt { q } }$ .size();   
Doub b,s,t,xx;   
VecDoub c $\left( \mathtt { n } \right)$ ;   
if $\mathbf { \Phi } _ { \mathbf { { n } } } \ = = \ 1 \mathbf { \Phi } _ { \mathbf { { \rho } } }$ ) w[0] $= c$ q[0];   
else { for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) c[i]=0.0; Initialize array. ${ \mathsf { c } } \left[ { \mathsf { n } } { - } 1 \right] ~ = ~ -$ x[0]; Coefficients of the master polynomial are found for ( $\scriptstyle { \dot { \hat { 1 } } } = 1$ ;i<n;i++) { by recursion. $\mathbf { x } \mathbf { x } ~ = ~ - \mathbf { x } \left[ \mathbf { i } \right]$ ; for $( \ j = ( \mathtt { n - 1 - i } ) \ ; \mathtt { j } < ( \mathtt { n - 1 } ) \ ; \mathtt { j } ^ { + + } ) \ \subset [ \mathtt { j } ] \ \ \ + = \ \mathtt { x x } ^ { * } \mathtt { c } [ \mathtt { j } ^ { + } ] \ ;$ c[n-1] $+ =$ xx; } for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { Each subfactor in turn

xx=x[i]; t=b=1.0; s=q[n-1]; for (k=n-1;k>0;k--) { b=c[k]+xx\*b; s += q[k-1]\*b; t=xx\*t+b; } w[i]=s/t; } } }

# 2.8.2 Toeplitz Matrices

An $N \times N$ Toeplitz matrix is specified by giving $2 N - 1$ numbers $R _ { k }$ , where the index $k$ ranges over $k = - N + 1 , \ldots , - 1 , 0 , 1 , \ldots , N - 1$ . Those numbers are then emplaced as matrix elements constant along the (upper-left to lower-right) diagonals of the matrix:

$$
\left[ \begin{array} { c c c c c c } { R _ { 0 } } & { R _ { - 1 } } & { R _ { - 2 } } & { \cdots } & { R _ { - ( N - 2 ) } } & { R _ { - ( N - 1 ) } } \\ { R _ { 1 } } & { R _ { 0 } } & { R _ { - 1 } } & { \cdots } & { R _ { - ( N - 3 ) } } & { R _ { - ( N - 2 ) } } \\ { R _ { 2 } } & { R _ { 1 } } & { R _ { 0 } } & { \cdots } & { R _ { - ( N - 4 ) } } & { R _ { - ( N - 3 ) } } \\ { \cdots } & { \cdots } & { \cdots } & { } & { } & { } \\ { R _ { N - 2 } } & { R _ { N - 3 } } & { R _ { N - 4 } } & { \cdots } & { R _ { 0 } } & { R _ { - 1 } } \\ { R _ { N - 1 } } & { R _ { N - 2 } } & { R _ { N - 3 } } & { \cdots } & { R _ { 1 } } & { R _ { 0 } } \end{array} \right]
$$

The linear Toeplitz problem can thus be written as

$$
\sum _ { j = 0 } ^ { N - 1 } R _ { i - j } x _ { j } = y _ { i } \qquad ( i = 0 , \ldots , N - 1 )
$$

where the $x _ { j }$ ’s, $j = 0 , \ldots , N - 1$ , are the unknowns to be solved for.

The Toeplitz matrix is symmetric if $R _ { k } = R _ { - k }$ for all $k$ . Levinson [4] developed an algorithm for fast solution of the symmetric Toeplitz problem, by a bordering method, that is, a recursive procedure that solves the $( M + 1 )$ -dimensional Toeplitz problem

$$
\sum _ { j = 0 } ^ { M } R _ { i - j } x _ { j } ^ { ( M ) } = y _ { i } \qquad ( i = 0 , \ldots , M )
$$

in turn for $M = 0 , 1 , \ldots$ until $M = N - 1$ , the desired result, is finally reached. The vector x.M /j is the result at the M th stage and becomes the desired answer only when N  1 is reached.

Levinson’s method is well documented in standard texts (e.g., [5]). The useful fact that the method generalizes to the nonsymmetric case seems to be less well known. At some risk of excessive detail, we therefore give a derivation here, due to G.B. Rybicki.

In following a recursion from step $M$ to step $M + 1$ we find that our developing solution $x ^ { ( M ) }$ changes in this way:

$$
\sum _ { j = 0 } ^ { M } R _ { i - j } x _ { j } ^ { ( M ) } = y _ { i } \qquad i = 0 , \dots , M
$$

becomes

$$
\sum _ { j = 0 } ^ { M } R _ { i - j } x _ { j } ^ { ( M + 1 ) } + R _ { i - ( M + 1 ) } x _ { M + 1 } ^ { ( M + 1 ) } = y _ { i } \qquad i = 0 , \dots , M + 1
$$

By eliminating $y _ { i }$ we find

$$
\sum _ { j = 0 } ^ { M } R _ { i - j } \left( \frac { x _ { j } ^ { ( M ) } - x _ { j } ^ { ( M + 1 ) } } { x _ { M + 1 } ^ { ( M + 1 ) } } \right) = R _ { i - ( M + 1 ) } \qquad i = 0 , \dots , M
$$

or by letting $i  M - i$ and $j \to M - j$ ,

$$
\sum _ { j = 0 } ^ { M } R _ { j - i } G _ { j } ^ { ( M ) } = R _ { - ( i + 1 ) }
$$

where

$$
G _ { j } ^ { ( M ) } \equiv \frac { x _ { M - j } ^ { ( M ) } - x _ { M - j } ^ { ( M + 1 ) } } { x _ { M + 1 } ^ { ( M + 1 ) } }
$$

To put this another way,

$$
x _ { M - j } ^ { ( M + 1 ) } = x _ { M - j } ^ { ( M ) } - x _ { M + 1 } ^ { ( M + 1 ) } G _ { j } ^ { ( M ) } \qquad j = 0 , \ldots , M
$$

Thus, if we can use recursion to find the order $M$ quantities $x ^ { ( M ) }$ and $G ^ { ( M ) }$ and the single order M C 1 quantity x.MC1/MC1 , then all of the other x.M C1/j ’s will follow. Fortunately, the quantity x.M C1/M C1 follows from equation (2.8.12) with i D M C 1,

$$
\sum _ { j = 0 } ^ { M } R _ { M + 1 - j } x _ { j } ^ { ( M + 1 ) } + R _ { 0 } x _ { M + 1 } ^ { ( M + 1 ) } = y _ { M + 1 }
$$

For the unknown order M C 1 quantities x.Mj $x _ { j } ^ { ( M + 1 ) }$ we can substitute the previous order quantities in $G$ since

$$
G _ { M - j } ^ { ( M ) } = \frac { x _ { j } ^ { ( M ) } - x _ { j } ^ { ( M + 1 ) } } { x _ { M + 1 } ^ { ( M + 1 ) } }
$$

The result of this operation is

$$
x _ { M + 1 } ^ { ( M + 1 ) } = \frac { \sum _ { j = 0 } ^ { M } R _ { M + 1 - j } x _ { j } ^ { ( M ) } - y _ { M + 1 } } { \sum _ { j = 0 } ^ { M } R _ { M + 1 - j } G _ { M - j } ^ { ( M ) } - R _ { 0 } }
$$

The only remaining problem is to develop a recursion relation for $G$ . Before we do that, however, we should point out that there are actually two distinct sets of solutions to the original linear problem for a nonsymmetric matrix, namely right-hand solutions (which we have been discussing) and left-hand solutions $z _ { i }$ . The formalism for the left-hand solutions differs only in that we deal with the equations

$$
\sum _ { j = 0 } ^ { M } R _ { j - i } z _ { j } ^ { ( M ) } = y _ { i } \qquad i = 0 , \ldots , M
$$

Then, the same sequence of operations on this set leads to

$$
\sum _ { j = 0 } ^ { M } R _ { i - j } H _ { j } ^ { ( M ) } = R _ { i + 1 }
$$

where

$$
H _ { j } ^ { ( M ) } \equiv \frac { z _ { M - j } ^ { ( M ) } - z _ { M - j } ^ { ( M + 1 ) } } { z _ { M + 1 } ^ { ( M + 1 ) } }
$$

(compare with 2.8.14 – 2.8.15). The reason for mentioning the left-hand solutions now is that, by equation (2.8.21), the $H _ { j }$ ’s satisfy exactly the same equation as the $x _ { j }$ ’s except for the substitution $y _ { i }  R _ { i + 1 }$ on the right-hand side. Therefore we can quickly deduce from equation (2.8.19) that

$$
H _ { M + 1 } ^ { ( M + 1 ) } = \frac { \sum _ { j = 0 } ^ { M } R _ { M + 1 - j } H _ { j } ^ { ( M ) } - R _ { M + 2 } } { \sum _ { j = 0 } ^ { M } R _ { M + 1 - j } G _ { M - j } ^ { ( M ) } - R _ { 0 } }
$$

By the same token, $G$ satisfies the same equation as $z$ , except for the substitution $y _ { i } $ $R _ { - ( i + 1 ) } .$ . This gives

$$
G _ { M + 1 } ^ { ( M + 1 ) } = \frac { \sum _ { j = 0 } ^ { M } R _ { j - M - 1 } G _ { j } ^ { ( M ) } - R _ { - M - 2 } } { \sum _ { j = 0 } ^ { M } R _ { j - M - 1 } H _ { M - j } ^ { ( M ) } - R _ { 0 } }
$$

The same “morphism” also turns equation (2.8.16), and its partner for $Z$ , into the final equations

$$
\begin{array} { r l } { G _ { j } ^ { ( M + 1 ) } = G _ { j } ^ { ( M ) } - G _ { M + 1 } ^ { ( M + 1 ) } H _ { M - j } ^ { ( M ) } } & { { } } \\ { H _ { j } ^ { ( M + 1 ) } = H _ { j } ^ { ( M ) } - H _ { M + 1 } ^ { ( M + 1 ) } G _ { M - j } ^ { ( M ) } } & { { } } \end{array}
$$

Now, starting with the initial values

$$
x _ { 0 } ^ { ( 0 ) } = y _ { 0 } / R _ { 0 } \qquad G _ { 0 } ^ { ( 0 ) } = R _ { - 1 } / R _ { 0 } \qquad H _ { 0 } ^ { ( 0 ) } = R _ { 1 } / R _ { 0 }
$$

we can recurse away. At each stage M we use equations (2.8.23) and (2.8.24) to find H .MC1/MC1 , G.MC1/MC1 , and then equation (2.8.25) to find the other components of H .MC1/; G.MC1/. From there the vectors $x ^ { ( M + 1 ) } \mathrm { a n d } / \mathrm { o r } z ^ { ( M + 1 ) }$ are easily calculated.

The program below does this. It incorporates the second equation in (2.8.25) in the form

$$
{ \cal H } _ { M - j } ^ { ( M + 1 ) } = { \cal H } _ { M - j } ^ { ( M ) } - { \cal H } _ { M + 1 } ^ { ( M + 1 ) } G _ { j } ^ { ( M ) }
$$

so that the computation can be done “in place.”

Notice that the above algorithm fails if $R _ { 0 } = 0$ . In fact, because the bordering method does not allow pivoting, the algorithm will fail if any of the diagonal principal minors of the original Toeplitz matrix vanish. (Compare with discussion of the tridiagonal algorithm in $\ S 2 . 4 . )$ If the algorithm fails, your matrix is not necessarily singular — you might just have to solve your problem by a slower and more general algorithm such as $L U$ decomposition with pivoting.

The routine that implements equations $( 2 . 8 . 2 3 ) - ( 2 . 8 . 2 7 )$ is also due to Rybicki. Note that the routine’s $\bf { r } \left[ \bf { n } { - } 1 { + } j \right]$ is equal to $R _ { j }$ above, so that subscripts on the $\mathbf { r }$ array vary from 0 to $2 N - 2$ .

# void toeplz(VecDoub_I &r, VecDoub_O &x, VecDoub_I &y)

Solves the Toeplitz system $\begin{array} { r } { \sum _ { j = 0 } ^ { N - 1 } R _ { ( N - 1 + i - j ) } x _ { j } \ = \ y _ { i } } \end{array}$ $( i = 0 , \ldots , N - 1 )$ oeplitz $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ $\mathtt { r } [ 0 \dots 2 { * } \mathtt { n } { - } 2 ]$ $\mathbf { x } \left[ 0 \ldots \ldots \right]$ output array.

Int j,k,m,m1,m2,n1,n=y.size();   
Doub pp,pt1,pt2,qq,qt1,qt2,sd,sgd,sgn,shn,sxn;   
$\mathtt { n 1 } = \mathtt { n - 1 }$ ;   
if (r[n1] $\scriptstyle = = \ 0 . 0 ,$ ) throw("toeplz-1 singular principal minor");   
x[0]=y[0]/r[n1]; Initialize for the recursion.   
if ( $\mathrm { ~  ~ n ~ 1 ~ } = = \mathrm { ~  ~ 0 ~ }$ ) return;   
VecDoub g(n1),h(n1);   
g[0] $= \tt { r }$ [n1-1]/r[n1];   
h[0] $= \tt { r }$ [n1+1]/r[n1];   
for $( \mathrm { m } { = } 0 ; \mathrm { m } { < } \mathrm { n } ; \mathrm { m } { + } + )$ { Main loop over the recursion. m1=m+1; sxn $=$ -y[m1]; Compute numerator and denominator for $x$ from eq. sd $=$ -r[n1]; (2.8.19), for (j=0;j<m+1;j $+ + { \bf \Gamma } .$ ) { sxn $+ = \texttt { r }$ [n1+m1-j]\*x[j]; sd $+ = \texttt { r }$ [n1+m1-j]\*g[m-j]; } if (sd $\mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ 0 ~ } . 0$ ) throw("toeplz-2 singular principal minor"); x[m1] $=$ sxn/sd; whence $x$ . for (j=0;j<m+1;j++) Eq. (2.8.16). x[j] -= x[m1]\*g[m-j]; if ( $\mathrm { ~ m 1 ~ } = = \mathrm { ~ n 1 ~ }$ ) return; sgn $=$ -r[n1-m1-1]; Compute numerator and denominator for $G$ and $H$ , shn $=$ -r[n1+m1+1]; eqs. (2.8.24) and (2.8.23), sgd $=$ -r[n1]; for (j=0;j<m+1;j++) { sgn $+ =$ r[n1+j-m1]\*g[j]; shn $+ = \texttt { r }$ [n1+m1-j]\*h[j]; sgd $+ = \texttt { r }$ [n1+j-m1]\*h[m-j]; } if (sgd $\scriptstyle = = \ 0 . 0$ ) throw("toeplz-3 singular principal minor"); g[m1] $=$ sgn/sgd; whence $G$ and $H$ . h[m1] $=$ shn/sd; $\mathrm { k } { = } \mathrm { m }$ ; m2=(m+2) >> 1; pp=g[m1]; qq=h[m1]; for (j=0;j<m2;j++) { pt1=g[j]; pt2=g[k]; qt1=h[j]; qt2=h[k]; g[j]=pt1-pp\*qt2; g[k]=pt2-pp\*qt1; h[j]=qt1-qq\*pt2; h[k--]=qt2-qq\*pt1; } Back for another recurrence.   
throw("toeplz - should not arrive here!");

If you are in the business of solving very large Toeplitz systems, you should find out about so-called “new, fast” algorithms, which require only on the order of $N ( \log N ) ^ { 2 }$ operations, compared to $N ^ { 2 }$ for Levinson’s method. These methods are too complicated to include here. Papers by Bunch [6] and de Hoog [7] will give entry to the literature.

# CITED REFERENCES AND FURTHER READING:

Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), Chapter 5 [also treats some other special forms].   
Forsythe, G.E., and Moler, C.B. 1967, Computer Solution of Linear Algebraic Systems (Englewood Cliffs, NJ: Prentice-Hall), $\ S 1 9$ .[1]   
Westlake, J.R. 1968, A Handbook of Numerical Matrix Inversion and Solution of Linear Equations (New York: Wiley).[2]   
von Mises, R. 1964, Mathematical Theory of Probability and Statistics (New York: Academic Press), pp. 394ff.[3]   
Levinson, N., Appendix B of N. Wiener, 1949, Extrapolation, Interpolation and Smoothing of Stationary Time Series (New York: Wiley).[4]   
Robinson, E.A., and Treitel, S. 1980, Geophysical Signal Analysis (Englewood Cliffs, NJ: Prentice-Hall), pp. 163ff.[5]   
Bunch, J.R. 1985, “Stability of Methods for Solving Toeplitz Systems of Equations,” SIAM Journal on Scientific and Statistical Computing,vol. 6,pp.349-364.[6]   
de Hoog, F. 1987, “A New Algorithm for Solving Toeplitz Systems of Equations,” Linear Algebra and Its Applications,vol.88/89,pp.123-138.[7]

# 2.9 Cholesky Decomposition

If a square matrix A happens to be symmetric and positive-definite, then it has a special, more efficient, triangular decomposition. Symmetric means that $a _ { i j } = a _ { j i }$ for $i , j =$ $0 , \ldots , N - 1$ , while positive-definite means that

$$
\mathbf { v } \cdot \mathbf { A } \cdot \mathbf { v } > 0 \quad { \mathrm { f o r ~ a l l ~ v e c t o r s ~ } } \mathbf { v }
$$

(In Chapter 11 we will see that positive-definite has the equivalent interpretation that A has all positive eigenvalues.) While symmetric, positive-definite matrices are rather special, they occur quite frequently in some applications, so their special factorization, called Cholesky decomposition, is good to know about. When you can use it, Cholesky decomposition is about a factor of two faster than alternative methods for solving linear equations.

Instead of seeking arbitrary lower and upper triangular factors $\mathbf { L }$ and $\mathbf { U }$ , Cholesky decomposition constructs a lower triangular matrix $\mathbf { L }$ whose transpose $\mathbf { L } ^ { T }$ can itself serve as the upper triangular part. In other words we replace equation (2.3.1) by

$$
\mathbf { L } \cdot \mathbf { L } ^ { T } = \mathbf { A }
$$

This factorization is sometimes referred to as “taking the square root” of the matrix A, though, because of the transpose, it is not literally that. The components of $\mathbf { L } ^ { T }$ are of course related to those of $\mathbf { L }$ by

$$
L _ { i j } ^ { T } = L _ { j i }
$$

Writing out equation (2.9.2) in components, one readily obtains the analogs of equations (2.3.12) – (2.3.13),

$$
L _ { i i } = \left( a _ { i i } - \sum _ { k = 0 } ^ { i - 1 } L _ { i k } ^ { 2 } \right) ^ { 1 / 2 }
$$

and

$$
L _ { j i } = \frac { 1 } { L _ { i i } } \left( a _ { i j } - \sum _ { k = 0 } ^ { i - 1 } L _ { i k } L _ { j k } \right) \qquad j = i + 1 , i + 2 , \ldots , N - 1
$$

If you apply equations (2.9.4) and (2.9.5) in the order $i = 0 , 1 , \ldots , N - 1$ , you will see that the $L$ ’s that occur on the right-hand side are already determined by the time they are needed. Also, only components $a _ { i j }$ with $j \geq i$ are referenced. (Since $\mathbf { A }$ is symmetric, these have complete information.) If storage is at a premium, it is possible to have the factor $\mathbf { L }$ overwrite the subdiagonal (lower triangular but not including the diagonal) part of $\mathbf { A }$ , preserving the input upper triangular values of $\mathbf { A }$ ; one extra vector of length $N$ is then needed to store the diagonal part of $\mathbf { L }$ . The operations count is $N ^ { 3 } / 6$ executions of the inner loop (consisting of one multiply and one subtract), with also $N$ square roots. As already mentioned, this is about a factor 2 better than $L U$ decomposition of $\mathbf { A }$ (where its symmetry would be ignored).

You might wonder about pivoting. The pleasant answer is that Cholesky decomposition is extremely stable numerically, without any pivoting at all. Failure of the decomposition simply indicates that the matrix A (or, with roundoff error, another very nearby matrix) is not positive-definite. In fact, this is an efficient way to test whether a symmetric matrix is positive-definite. (In this application, you may want to replace the throw in the code below with some less drastic signaling method.)

By now you should be familiar with, if not bored by, our conventions for objects implementing decomposition methods, so we list the object Cholesky as a single big mouthful. The methods elmult and elsolve perform manipulations using the matrix L. The first multiplies $\mathbf { L } \cdot \mathbf { y } = \mathbf { c }$ for a given y, returning c. The second solves this same equation, given c and returning y. These manipulations are useful in contexts such as multivariate Gaussians $( \ S 7 . 4$ and $\ S 1 6 . 5 \AA$ ) and in the analysis of covariance matrices (-15.6).

# struct Cholesky{

Object for Cholesky decomposition of a matrix A, and related functions. Int n; MatDoub el; Stores the decomposition. Cholesky(MatDoub_I &a) : n(a.nrows()) el(a) Constructor. Given a positive-definite symmetric matrix a[0..n-1][0..n-1], construct and store its Cholesky decomposition, ${ \mathbf { A } } = { \mathbf { L } } \cdot { \mathbf { L } } ^ { T }$ . Int i,j,k; VecDoub tmp; Doub sum; if (el.ncols() $! = \mathrm { ~ n ~ } ,$ ) throw("need square matrix"); for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) { for ( $\scriptstyle \dot { \mathcal { I } } = \dot { \mathcal { I } }$ ;j<n;j++) { for (sum=el[i][j],k=i-1;k>=0;k--) sum $- =$ el[i][k]\*el[j][k]; if ( $\begin{array} { r l } { \dot { \textbf { 1 } } } & { { } = = } \end{array}$ j) { if (sum $< = \ 0 . 0$ ) A, with rounding errors, is not positive-definite. throw("Cholesky failed"); el[i][i] $=$ sqrt(sum); else el[j][i] $=$ sum/el[i][i]; } for (i=0;i<n;i++) for (j ${ = } 0$ ;j<i;j++) el[j][i] = 0.;

void solve(VecDoub_I &b, VecDoub_O &x) {

Solve the set of n linear equations $\mathbf { A \cdot x } = \mathbf { b }$ , where a is a positive-definite symmetric matrix whose Cholesky decomposition has been stored. b $\left[ 0 \ldots \mathbf { n } \mathbf { - } 1 \right]$ is input as the right-hand side vector. The solution vector is returned in $\mathbf { x } \left[ 0 \ldots \ldots \right] $ .

Int i,k; Doub sum; if (b.size() $! = \mathrm { ~ n ~ }$ || x.size() $! = \mathrm { ~ n ~ } ,$ ) throw("bad lengths in Cholesky"); for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\dot { 1 } + +$ ) { Solve $\mathbf { L } \cdot \mathbf { y } = \mathbf { b } $ , storing $\mathbf { y }$ in $\mathbf { x }$ . for (sum=b[i], $\operatorname { k } { = } \operatorname { i } { - } 1 ; \operatorname { k } { > } { = } 0 ; \operatorname { k } { - } { - } \operatorname { \lambda }$ sum $- =$ el[i][k] $^ { * \mathbf { x } }$ [k]; x[i] $=$ sum/el[i][i]; } for (i=n-1;i>=0;i--) { Solve $\mathbf { L } ^ { T } \cdot \mathbf { x } = \mathbf { y }$ . for (sum $_ { 1 } = \mathbf { x }$ [i],k=i+1;k<n;k++) sum $- =$ el[k][i]\*x[k]; x[i] $=$ sum/el[i][i]; } }

void elmult(VecDoub_I &y, VecDoub_O &b) {

Multiply $\mathbf { L } \cdot \mathbf { y } = \mathbf { b } $ , where $\mathbf { L }$ is the lower triangular matrix in the stored Cholesky decomposition. $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ is input. The result is returned in b[0..n-1].

Int i,j;   
if (b.size() $\mathbf { \omega } _ { ! } = \mathbf { \omega } _ { \mathrm { ~ n ~ } }$ || y.size() $! = \mathrm { ~ n ~ } ,$ ) throw("bad lengths");   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) { b[i] $\qquad = \ 0$ .; for ( $\scriptstyle \cdot j = 0$ ;j $\Longleftarrow \dot { 1 }$ ;j++) b[i] $+ =$ el[i][j]\*y[j];   
}

void elsolve(VecDoub_I &b, VecDoub_O &y) {

Solve $\mathbf { L } \cdot \mathbf { y } = \mathbf { b } $ , where $\mathbf { L }$ is the lower triangular matrix in the stored Cholesky decomposition. b $\left[ 0 \cdot \cdot \mathbf { n } \mathbf { - } 1 \right]$ is input as the right-hand side vector. The solution vector is returned in $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ .

Int i,j;

Doub sum; if (b.size() $\ ! = { \texttt { n } }$ || y.size() $! = \mathrm { ~ \tt ~ n ~ } )$ throw("bad lengths"); for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) { for (sum $\mathtt { = b }$ [i], $\scriptstyle { \dot { \ j } } = 0$ ; $\mathrm { j } < \mathrm { i }$ ; ${ \mathrm { j } } + + { \mathrm { . } }$ ) sum $- =$ el[i][j]\*y[j]; y[i] $=$ sum/el[i][i]; } }

# void inverse(MatDoub_O &ainv) {

Set ainv[0..n-1][0..n-1] to the matrix inverse of A, the matrix whose Cholesky decomposition has been stored.

Int i,j,k;   
Doub sum;   
ainv.resize(n,n);   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0 $ ;i<n; $\dot { 1 } + + \dot { 1 }$ ) for $( { \mathrm { j } } { = } 0 ; { \mathrm { j } } { < } { = } { \mathrm { i } } ; { \mathrm { j } } { + } { + } ) \left\{ \begin{array} { r l } \end{array} \right.$ sum $=$ ( $\scriptstyle \mathbf { i } = = \mathbf { j } ? \ 1$ . : 0.); for $\mathrm { k } = \dot { \mathrm { 1 } } - 1$ ;k>=j;k--) sum $- =$ el[i][k]\*ainv[j][k]; ainv[j][i] $=$ sum/el[i][i];   
}   
for (i=n-1;i>=0;i--) for ( $\scriptstyle \mathrm { j } = 0$ ;j $\Longleftarrow \dot { 1 }$ ;j++){ sum $=$ (i<j? 0. : ainv[j][i]); for $\mathtt { k } = \mathtt { i } + 1$ ;k<n;k++) sum $- =$ el[k][i]\*ainv[j][k]; ainv[i][j] $=$ ainv[j][i] $=$ sum/el[i][i];   
}

# Doub logdet() {

Return the logarithm of the determinant of A, the matrix whose Cholesky decomposition has been stored.

Doub sum $\mathit { \Theta } = \mathit { \Theta } 0$ .; for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<n; $\dot { \bar { \lambda } } + +$ ) sum $+ =$ log(el[i][i]); return 2.\*sum; } };

# CITED REFERENCES AND FURTHER READING:

Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York:Springer),Chapter $1 / 1$   
Gill, P.E., Murray, W., and Wright, M.H. 1991, Numerical Linear Algebra and Optimization, vol. 1 (Redwood City, CA: Addison-Wesley), $\ S 4 . 9 . 2$ .   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 5 . 3 . 5$ .   
Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), $\ S 4 . 2$ .

# 2.10 QR Decomposition

There is another matrix factorization that is sometimes very useful, the so-called $\mathcal Q R$ decomposition,

$$
\mathbf { A } = \mathbf { Q } \cdot \mathbf { R }
$$

Here $\mathbf { R }$ is upper triangular, while $\mathbf { Q }$ is orthogonal, that is,

$$
{ \bf Q } ^ { T } \cdot { \bf Q } = { \bf 1 }
$$

where $\mathbf { Q } ^ { T }$ is the transpose matrix of $\mathbf { Q }$ . Although the decomposition exists for a general rectangular matrix, we shall restrict our treatment to the case when all the matrices are square, with dimensions $N \times N$ .

Like the other matrix factorizations we have met ( $L U$ , SVD, Cholesky), $\mathcal Q R$ decomposition can be used to solve systems of linear equations. To solve

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

first form $\mathbf { Q } ^ { T } \cdot \mathbf { b }$ and then solve

$$
\mathbf { R } \cdot \mathbf { x } = \mathbf { Q } ^ { T } \cdot \mathbf { b }
$$

by backsubstitution. Since $\mathcal Q R$ decomposition involves about twice as many operations as $L U$ decomposition, it is not used for typical systems of linear equations. However, we will meet special cases where $\mathcal Q R$ is the method of choice.

The standard algorithm for the $\mathcal Q R$ decomposition involves successive Householder transformations (to be discussed later in $\ S 1 1 . 3 )$ . We write a Householder matrix in the form $\mathbf { 1 } - \mathbf { u } \otimes \mathbf { u } / c$ , where $\begin{array} { r } { c = \frac { 1 } { 2 } \mathbf { u } \cdot \mathbf { u } } \end{array}$ . An appropriate Householder matrix applied to a given matrix can zero all elements in a column of the matrix situated below a chosen element. Thus we arrange for the first Householder matrix $\mathbf { Q } _ { 0 }$ to zero all elements in column 0 of A below the zeroth element. Similarly, $\mathbf { Q } _ { 1 }$ zeroes all elements in column 1 below element 1, and so on up to $\mathbf { Q } _ { n - 2 }$ . Thus

$$
\mathbf { R } = \mathbf { Q } _ { n - 2 } \cdots \mathbf { Q } _ { 0 } \cdot \mathbf { A }
$$

Since the Householder matrices are orthogonal,

$$
\mathbf { Q } = ( \mathbf { Q } _ { n - 2 } \cdots \mathbf { Q } _ { 0 } ) ^ { - 1 } = \mathbf { Q } _ { 0 } \cdots \mathbf { Q } _ { n - 2 }
$$

In many applications $\mathbf { Q }$ is not needed explicitly, and it is sufficient to store only the factored form (2.10.6). (We do, however, store $\mathbf { Q }$ , or rather its transpose, in the code below.) Pivoting is not usually necessary unless the matrix A is very close to singular. A general $\mathcal Q R$ algorithm for rectangular matrices including pivoting is given in [1]. For square matrices and without pivoting, an implementation is as follows:

# struct QRdcmp {

# qrdcmp.h

Object for $Q R$ decomposition of a matrix A, and related functions.

Int n;   
MatDoub qt, r; Stored $\mathbf { Q } ^ { T }$ and $\mathbf { R }$ .   
Bool sing; Indicates whether $\mathbf { A }$ is singular.   
QRdcmp(MatDoub_I &a); Constructor from A.   
void solve(VecDoub_I &b, VecDoub_O &x); Solve $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ for $\mathbf { x }$ .   
void qtmult(VecDoub_I &b, VecDoub_O &x); Multiply ${ \mathbf { Q } } ^ { T } \cdot { \mathbf { b } } = { \mathbf { x } }$ .   
void rsolve(VecDoub_I &b, VecDoub_O &x); Solve $\mathbf { R } \cdot \mathbf { x } = \mathbf { b }$ for $\mathbf { x }$ .   
void update(VecDoub_I &u, VecDoub_I &v); See next subsection.   
void rotate(const Int i, const Doub a, const Doub b); Used by update.

As usual, the constructor performs the actual decomposition:

QRdcmp::QRdcmp(MatDoub_I &a)

# qrdcmp.h

: n(a.nrows()), qt ${ ( \mathrm { n , n } ) }$ , r(a), sing(false)

Construct the $Q R$ decomposition of a[0..n-1][0..n-1]. The upper triangular matrix R and the transpose of the orthogonal matrix Q are stored. sing is set to true if a singularity is encountered during the decomposition, but the decomposition is still completed in this case; otherwise it is set to false.

Int i,j,k;   
VecDoub c(n), d(n);   
Doub scale,sigma,sum,tau;   
for (k=0;k<n-1;k++) { scale ${ } = 0$ .0; for ( $\dot { \mathtt { 1 } } \mathtt { = } \mathtt { k }$ ;i<n; $\dot { 1 } + + \dot { 1 }$ ) scale $\risingdotseq$ MAX(scale,abs(r[i][k])); if (scale $\scriptstyle = = \ 0 . 0 { \mathrm { . } }$ ) { Singular case. sing=true; c[k]=d[k] ${ = } 0$ .0; else { Form $\mathbf { Q } _ { k }$ and $\mathbf { Q } _ { k } \cdot \mathbf { A }$ . for ( $\dot { \bf \Phi } _ { 1 } = \bf k$ ;i<n;i++) r[i][k] $/ =$ scale; for (sum $_ { = 0 }$ .0, $\dot { \bf \Phi } _ { 1 } = \bf k$ ;i<n; $\dot { 1 } + +$ ) sum $+ =$ SQR $. { }$ [i][k]); sigma=SIGN(sqrt(sum),r[k][k]); r[k][k] $+ =$ sigma; c[k] $= _ { i }$ sigma\*r[k][k]; d[k] $=$ -scale\*sigma; for ( $\mathsf { i } \mathrm { = } \mathtt { k } \mathrm { + } 1$ ;j<n;j++) { for (sum $_ { = 0 }$ .0,i=k;i<n;i++) sum $+ = \texttt { r }$ [i][k]\*r[i][j]; tau=sum/c[k]; for ( $\dot { \bf \Phi } _ { 1 } = \bf k$ ;i<n;i++) r[i][j] $- =$ tau\*r[i][k]; } }   
d[n-1] $= \tt { r }$ [n-1][n-1];   
if (d[n-1] $\scriptstyle = = \ 0 . 0$ ) sing=true;   
for $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { Form $\mathbf { Q } ^ { T }$ explicitly. for (j=0;j<n;j++) qt[i][j]=0.0; qt[i][i] $= 1$ .0;   
for (k=0;k<n-1;k++) { if (c[k] $\ ! =$ 0.0) { for (j=0;j<n;j++) { sum=0.0; for ( $\dot { \mathtt { 1 } } \mathtt { = } \mathtt { k }$ ;i<n;i++) sum $+ = \textbf { r }$ [i][k]\*qt[i][j]; sum $/ =$ c[k]; for (i=k;i<n; $\dot { \bf 1 } + +$ ) qt[i][j] $- =$ sum\*r[i][k]; } }   
1   
for (i=0;i<n;i++) { Form R explicitly. r[i][i]=d[i]; for (j ${ = } 0$ ;j<i;j++) r[i][j]=0.0;   
}

The next set of member functions is used to solve linear systems. In many applications only the part (2.10.4) of the algorithm is needed, so we put in separate routines the multiplication $\mathbf { Q } ^ { \bar { T } } \cdot \mathbf { b }$ and the backsubstitution on R.

void QRdcmp::solve(VecDoub_I &b, VecDoub_O &x) {

Solve the set of n linear equations $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ . b $\left[ 0 \cdot \cdot \mathbf { n } \mathbf { - } 1 \right]$ is input as the right-hand side vector, and $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ is returned as the solution vector.

qtmult(b,x); Form $\mathbf { Q } ^ { T } \cdot \mathbf { b }$ . rsolve(x,x); Solve $\mathbf { R } \cdot \mathbf { x } = \mathbf { Q } ^ { T } \cdot \mathbf { b }$

void QRdcmp::qtmult(VecDoub_I &b, VecDoub_O &x) {   
Multiply $\mathbf { Q } ^ { T } \cdot \mathbf { b }$ and put the result in $\mathbf { x }$ . Since $\mathbf { Q }$ is orthogonal, this is equivalent to solving   
$\mathbf { Q } \cdot \mathbf { x } = \mathbf { b }$ for $\mathbf { x }$ . Int i,j; Doub sum; for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) { sum $\mathit { \Theta } = \mathit { \Theta } 0 .$ ;

for ( $\scriptstyle \mathbf { j } = 0$ ;j<n;j $^ { + + }$ ) sum $+ =$ qt[i][j]\*b[j]; x[i] $=$ sum; } }

void QRdcmp::rsolve(VecDoub_I &b, VecDoub_O &x) {   
Solve the triangular set of n linear equations $\mathbf { R } \cdot \mathbf { x } = \mathbf { b }$ . b[0..n-1] is input as the right-hand side vector, and $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ is returned as the solution vector.

Int i,j; Doub sum; if (sing) throw("attempting solve in a singular QR"); for ( $\dot { \mathtt { 1 } } = \mathtt { n } - 1$ ; $\scriptstyle \dot { 1 } > = 0$ ;i--) { sum=b[i]; for ( $ \scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { 1 } } } + { \mathsf { 1 } }$ ;j<n;j++) sum $\begin{array} { r } { \mathrm { ~ -- ~ } } \\ { \mathrm { ~ -- ~ } } \end{array} x \quad \mathrm { ~ - ~ } \ x$ [i][j]\*x[j]; x[i] $=$ sum/r[i][i]; } }

See [2] for details on how to use $\mathcal Q R$ decomposition for constructing orthogonal bases, and for solving least-squares problems. (We prefer to use SVD, $\ S 2 . 6$ , for these purposes, because of its greater diagnostic capability in pathological cases.)

# 2.10.1 Updating a QR decomposition

Some numerical algorithms involve solving a succession of linear systems each of which differs only slightly from its predecessor. Instead of doing $O ( N ^ { 3 } )$ operations each time to solve the equations from scratch, one can often update a matrix factorization in $O ( N ^ { 2 } )$ operations and use the new factorization to solve the next set of linear equations. The $L U$ decomposition is complicated to update because of pivoting. However, $\mathcal Q R$ turns out to be quite simple for a very common kind of update,

$$
\mathbf { A }  \mathbf { A } + \mathbf { s } \otimes \mathbf { t }
$$

(compare equation 2.7.1). In practice it is more convenient to work with the equivalent form

$$
\mathbf { A } = \mathbf { Q } \cdot \mathbf { R } \quad \mathbf { \Psi } \to \quad \mathbf { A } ^ { \prime } = \mathbf { Q } ^ { \prime } \cdot \mathbf { R } ^ { \prime } = \mathbf { Q } \cdot ( \mathbf { R } + \mathbf { u } \otimes \mathbf { v } )
$$

One can go back and forth between equations (2.10.7) and (2.10.8) using the fact that $\mathbf { Q }$ is orthogonal, giving

$$
\mathbf { t } = \mathbf { v } \quad { \mathrm { a n d ~ e i t h e r } } \quad \mathbf { s } = \mathbf { Q } \cdot \mathbf { u } \quad { \mathrm { o r } } \quad \mathbf { u } = \mathbf { Q } ^ { T } \cdot \mathbf { s }
$$

The algorithm [2] has two phases. In the first we apply $N - 1$ Jacobi rotations (-11.1) to reduce $\mathbf { R } + \mathbf { u } \otimes \mathbf { v }$ to upper Hessenberg form. Another $N - 1$ Jacobi rotations transform this upper Hessenberg matrix to the new upper triangular matrix $\mathbf { R } ^ { \prime }$ . The matrix $\mathbf { Q } ^ { \prime }$ is simply the product of $\mathbf { Q }$ with the $2 ( N - 1 )$ Jacobi rotations. In applications we usually want $\mathbf { Q } ^ { T }$ , so the algorithm is arranged to work with this matrix (which is stored in the QRdcmp object) instead of with Q.

# void QRdcmp::update(VecDoub_I &u, VecDoub_I &v) {

Starting from the stored $Q R$ decomposition $\mathbf { A } = \mathbf { Q } \cdot \mathbf { R }$ , update it to be the $Q R$ decomposition of the matrix $\mathbf { Q } \cdot ( \mathbf { R } + \mathbf { u } \otimes \mathbf { v } )$ . Input quantities are $\mathtt { u } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ , and $\mathtt { v } [ 0 \dots \underbrace { \mathtt { n } ^ { - 1 } } ]$ .

Find largest k such that $\mathbf { u } \left[ \mathbf { k } \right] \neq \mathbf { 0 }$ .

Int i,k;   
VecDoub $\mathfrak { w } ( \mathfrak { u } )$ ;   
for ( $\scriptstyle \mathbf { k } = \mathbf { n } - 1$ ; $\mathtt { k } > = 0$ ;k--) if (w[k] $\ ! = \ 0 . 0 \dot { } .$ ) break;   
if $( \mathrm {  ~ k ~ } < \mathrm {  ~ 0 ~ }$ ) $\mathtt { k } = 0$ ;   
for ( $\dot { \bf \underline { { 1 } } } = \bf k - $ ; $\scriptstyle \dot { 1 } > = 0$ ;i--) { rotate(i,w[i],-w[i+1]); if (w[i] $\mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ 0 ~ } . 0 \dot { \mathrm { ~  ~ \omega ~ } }$ ) w[i] $=$ abs(w[i+1]);

Transform $\mathbf { R } + \mathbf { u } \otimes \mathbf { v }$ to upper Hessenberg.

else if (abs(w[i]) $>$ abs(w[i+1])) w[i] $=$ abs(w[i])\*sqrt(1.0+SQR(w[i+1]/w[i])); else w[i] $=$ abs(w[i+1])\*sqrt(1.0+SQR(w[i]/w[i+1]));   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\mathrm { i } + +$ ) $\mathbf { r }$ [0][i] $\scriptstyle + = \ w$ [0]\*v[i];   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<k; $\dot { \bf 1 } + +$ ) Transform upper Hessenberg matrix to upper trirotate(i,r[i][i],-r[i+1][i]); angular.   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \beta } } } .$ ) if ( $\mathbf { \sigma } _ { \mathbf { r } }$ [i][i] $\scriptstyle = = \ 0 , 0$ ) sing=true;

# }

# void QRdcmp::rotate(const Int i, const Doub a, const Doub b)

Utility used by update. Given matrices $\mathbf { r } \left[ 0 \cdot \cdot \mathbf { n } \mathbf { - } 1 \right] \left[ 0 \cdot \cdot \mathbf { n } \mathbf { - } 1 \right]$ and qt[0..n-1][0..n-1], carry out a Jacobi rotation on rows i and $\dot { \bar { \mathbf { 1 } } } + \mathbf { 1 }$ of each matrix. a and b are the parameters of the rotation: cos $\theta = a / \sqrt { a ^ { 2 } + b ^ { 2 } }$ , $\sin \theta = b / \sqrt { a ^ { 2 } + b ^ { 2 } }$ .

Int j;   
Doub c,fact,s,w,y;   
if ( $\mathsf { a } ~ = = ~ 0 . 0$ ) { Avoid unnecessary overflow or underflow. $\mathtt { c } = 0 . 0$ ; $\mathbf { s } { = } \left( \mathrm { b } \ \mathbf { \Sigma } > = \ \mathbf { 0 } \mathbf { . } 0 \ \ ? \ \mathbf { 1 } \mathbf { . } 0 \ \ : \ - \mathbf { 1 } \mathbf { . } 0 \right) \mathbf { ; }$ ;   
} else if (abs(a) $>$ abs(b)) { fact=b/a; $c =$ SIGN(1.0/sqrt(1. $0 +$ (fact\*fact)),a); s=fact\*c;   
} else { fact=a/b; s=SIGN(1.0/sqrt(1.0+(fact\*fact)),b); c=fact\*s;   
}   
for (j=i;j<n;j++) { Premultiply r by Jacobi rotation. y=r[i][j]; $\mathtt { w } = \mathtt { r }$ [i+1][j]; r[i][j]=c\*y-s\*w; r[i+1][j]=s\*y+c\*w;   
}   
for (j=0;j<n;j++) { Premultiply qt by Jacobi rotation. y=qt[i][j]; w=qt[i+1][j]; qt[i][j]=c\*y-s\*w; qt[i+1][j]=s\*y+c\*w;   
}

We will make use of $\mathcal Q R$ decomposition, and its updating, in $\ S 9 . 7$ .

# CITED REFERENCES AND FURTHER READING:

Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer), Chapter I/8.[1]   
Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), $\ S 5 . 2$ , $\ S 5 . 3$ , $\ S 1 2 . 5 .$ [2]

# 2.11 Is Matrix Inversion an N3 Process?

We close this chapter with a little entertainment, a bit of algorithmic prestidigitation that probes more deeply into the subject of matrix inversion. We start with a seemingly simple question:

How many individual multiplications does it take to perform the matrix multiplication of two $2 \times 2$ matrices,

$$
{ \binom { a _ { 0 0 } } { a _ { 1 0 } } } \ a _ { 0 1 } \atop { \boldsymbol { a } } ) \cdot { \boldsymbol { ( \begin{array} { l l } { b _ { 0 0 } } & { b _ { 0 1 } } \\ { b _ { 1 0 } } & { b _ { 1 1 } } \end{array} ) } } = { \binom { c _ { 0 0 } } { c _ { 1 0 } } } \ c _ { 0 1 } )
$$

Eight, right? Here they are written explicitly:

$$
\begin{array} { r l } & { c _ { 0 0 } = a _ { 0 0 } \times b _ { 0 0 } + a _ { 0 1 } \times b _ { 1 0 } } \\ & { c _ { 0 1 } = a _ { 0 0 } \times b _ { 0 1 } + a _ { 0 1 } \times b _ { 1 1 } } \\ & { c _ { 1 0 } = a _ { 1 0 } \times b _ { 0 0 } + a _ { 1 1 } \times b _ { 1 0 } } \\ & { c _ { 1 1 } = a _ { 1 0 } \times b _ { 0 1 } + a _ { 1 1 } \times b _ { 1 1 } } \end{array}
$$

Do you think that one can write formulas for the $c$ ’s that involve only seven multiplications? (Try it yourself, before reading on.)

Such a set of formulas was, in fact, discovered by Strassen [1]. The formulas are

$$
\begin{array} { r l } & { \mathcal { Q } _ { 0 } \equiv ( a _ { 0 0 } + a _ { 1 1 } ) \times ( b _ { 0 0 } + b _ { 1 1 } ) } \\ & { \mathcal { Q } _ { 1 } \equiv ( a _ { 1 0 } + a _ { 1 1 } ) \times b _ { 0 0 } } \\ & { \mathcal { Q } _ { 2 } \equiv a _ { 0 0 } \times ( b _ { 0 1 } - b _ { 1 1 } ) } \\ & { \mathcal { Q } _ { 3 } \equiv a _ { 1 1 } \times ( - b _ { 0 0 } + b _ { 1 0 } ) } \\ & { \mathcal { Q } _ { 4 } \equiv ( a _ { 0 0 } + a _ { 0 1 } ) \times b _ { 1 1 } } \\ & { \mathcal { Q } _ { 5 } \equiv ( - a _ { 0 0 } + a _ { 1 0 } ) \times ( b _ { 0 0 } + b _ { 0 1 } ) } \\ & { \mathcal { Q } _ { 6 } \equiv ( a _ { 0 1 } - a _ { 1 1 } ) \times ( b _ { 1 0 } + b _ { 1 1 } ) } \end{array}
$$

in terms of which

$$
\begin{array} { r l } & { c _ { 0 0 } = Q _ { 0 } + Q _ { 3 } - Q _ { 4 } + Q _ { 6 } } \\ & { c _ { 1 0 } = Q _ { 1 } + Q _ { 3 } } \\ & { c _ { 0 1 } = Q _ { 2 } + Q _ { 4 } } \\ & { c _ { 1 1 } = Q _ { 0 } + Q _ { 2 } - Q _ { 1 } + Q _ { 5 } } \end{array}
$$

What’s the use of this? There is one fewer multiplication than in equation (2.11.2), but many more additions and subtractions. It is not clear that anything has been gained. But notice that in (2.11.3) the $a$ ’s and $b$ ’s are never commuted. Therefore (2.11.3) and (2.11.4) are valid when the $a$ ’s and $b$ ’s are themselves matrices. The problem of multiplying two very large matrices (of order $N = 2 ^ { m }$ for some integer $m$ ) can now be broken down recursively by partitioning the matrices into quarters, sixteenths, etc. And note the key point: The savings is not just a factor $" 7 / 8 "$ ; it is that factor at each hierarchical level of the recursion. In total it reduces the process of matrix multiplication to order $N ^ { \log _ { 2 } 7 }$ instead of $N ^ { 3 }$ .

What about all the extra additions in (2.11.3) – (2.11.4)? Don’t they outweigh the advantage of the fewer multiplications? For large $N$ , it turns out that there are six times as many additions as multiplications implied by $( 2 . 1 1 . 3 ) - ( 2 . 1 1 . 4 )$ . But, if $N$ is very large, this constant factor is no match for the change in the exponent from $N ^ { 3 }$ to $N ^ { \log _ { 2 } 7 }$ .

With this “fast” matrix multiplication, Strassen also obtained a surprising result for matrix inversion [1]. Suppose that the matrices

$$
\left( \begin{array} { c c } { { a _ { 0 0 } } } & { { a _ { 0 1 } } } \\ { { a _ { 1 0 } } } & { { a _ { 1 1 } } } \end{array} \right) \quad \mathrm { { a n d } } \quad \left( \begin{array} { c c } { { c _ { 0 0 } } } & { { c _ { 0 1 } } } \\ { { c _ { 1 0 } } } & { { c _ { 1 1 } } } \end{array} \right)
$$

are inverses of each other. Then the $c$ ’s can be obtained from the $a$ ’s by the following operations (compare equations 2.7.11 and 2.7.25):

$$
\begin{array} { r l } & { R _ { 0 } = \mathrm { I w v e r s e } ( a _ { 0 0 } ) } \\ & { R _ { 1 } = a _ { 1 0 } \times R _ { 0 } } \\ & { R _ { 2 } = R _ { 0 } \times a _ { 0 1 } } \\ & { R _ { 3 } = a _ { 1 0 } \times R _ { 2 } } \\ & { R _ { 4 } = R _ { 3 } - a _ { 1 1 } } \\ & { R _ { 5 } = \mathrm { I w e r s e } ( R _ { 4 } ) } \\ & { c _ { 0 1 } = R _ { 2 } \times R _ { 5 } } \\ & { c _ { 1 0 } = R _ { 5 } \times R _ { 1 } } \\ & { R _ { 6 } = R _ { 2 } \times c _ { 1 0 } } \\ & { c _ { 0 0 } = R _ { 0 } - R _ { 6 } } \\ & { c _ { 1 1 } = - R _ { 5 } . } \end{array}
$$

In (2.11.6) the “inverse” operator occurs just twice. It is to be interpreted as the reciprocal if the $a$ ’s and $c$ ’s are scalars, but as matrix inversion if the $a$ ’s and $c$ ’s are themselves submatrices. Imagine doing the inversion of a very large matrix, of order $N = 2 ^ { m }$ , recursively by partitions in half. At each step, halving the order doubles the number of inverse operations. But this means that there are only $N$ divisions in all! So divisions don’t dominate in the recursive use of (2.11.6). Equation (2.11.6) is dominated, in fact, by its 6 multiplications. Since these can be done by an $N ^ { \log _ { 2 } 7 }$ algorithm, so can the matrix inversion!

This is fun, but let’s look at practicalities: If you estimate how large $N$ has to be before the difference between exponent 3 and exponent $\log _ { 2 } 7 = 2 . 8 0 7$ is substantial enough to outweigh the bookkeeping overhead, arising from the complicated nature of the recursive Strassen algorithm, you will find that $L U$ decomposition is in no immediate danger of becoming obsolete. However, the fast matrix multiplication routine itself is beginning to appear in libraries like BLAS, where it is typically used for $N \gtrsim 1 0 0$ .

Strassen’s original result for matrix multiplication has been steadily improved. The fastest currently known algorithm [2] has an asymptotic order of $N ^ { 2 . 3 7 6 }$ , but it is not likely to be practical to implement it.

If you like this kind of fun, then try these: (1) Can you multiply the complex numbers $( a + i b )$ and $( c + i d )$ in only three real multiplications? [Answer: See $\ S 5 . 5 . ]$ (2) Can you evaluate a general fourth-degree polynomial in $x$ for many different values of $x$ with only three multiplications per evaluation? [Answer: See $\ S 5 . 1 . ]$

# CITED REFERENCES AND FURTHER READING:

Strassen, V. 1969, “Gaussian Elimination Is Not Optimal,” Numerische Mathematik, vol. 13, pp. 354–356.[1]

Coppersmith, D., and Winograd, S. 1990, “Matrix Multiplications via Arithmetic Progressions,” Journal of Symbolic Computation,vol. 9,pp.251-280.[2]   
Kronsjö, L. 1987, Algorithms: Their Complexity and Efficiency, 2nd ed. (New York: Wiley).   
Winograd, S. 1971, “On the Multiplication of 2 by 2 Matrices,” Linear Algebra and Its Applications, vol. 4, pp. 381–388.   
Pan, V. Ya. 1980, “New Fast Algorithms for Matrix Operations,” SIAM Journal on Computing, vol. 9, pp. 321–342.   
Pan, V. 1984, How to Multiply Matrices Faster, Lecture Notes in Computer Science, vol. 179 (New York: Springer)   
Pan, V. 1984, “How Can We Speed Up Matrix Multiplication?”, SIAM Review, vol. 26, pp. 393– 415.

# Interpolation and Extrapolation

# 3.0 Introduction

We sometimes know the value of a function $f ( x )$ at a set of points $x _ { 0 } , x _ { 1 } , \dotsc$ ; $x _ { N - 1 }$ (say, with $x _ { 0 } < . . . < x _ { N - 1 } ,$ , but we don’t have an analytic expression for $f ( x )$ that lets us calculate its value at an arbitrary point. For example, the $f ( x _ { i } )$ ’s might result from some physical measurement or from long numerical calculation that cannot be cast into a simple functional form. Often the $x _ { i }$ ’s are equally spaced, but not necessarily.

The task now is to estimate $f ( x )$ for arbitrary $x$ by, in some sense, drawing a smooth curve through (and perhaps beyond) the $x _ { i }$ . If the desired $x$ is in between the largest and smallest of the $x _ { i }$ ’s, the problem is called interpolation; if $x$ is outside that range, it is called extrapolation, which is considerably more hazardous (as many former investment analysts can attest).

Interpolation and extrapolation schemes must model the function, between or beyond the known points, by some plausible functional form. The form should be sufficiently general so as to be able to approximate large classes of functions that might arise in practice. By far most common among the functional forms used are polynomials (-3.2). Rational functions (quotients of polynomials) also turn out to be extremely useful (-3.4). Trigonometric functions, sines and cosines, give rise to trigonometric interpolation and related Fourier methods, which we defer to Chapters 12 and 13.

There is an extensive mathematical literature devoted to theorems about what sort of functions can be well approximated by which interpolating functions. These theorems are, alas, almost completely useless in day-to-day work: If we know enough about our function to apply a theorem of any power, we are usually not in the pitiful state of having to interpolate on a table of its values!

Interpolation is related to, but distinct from, function approximation. That task consists of finding an approximate (but easily computable) function to use in place of a more complicated one. In the case of interpolation, you are given the function $f$ at points not of your own choosing. For the case of function approximation, you are allowed to compute the function $f$ at any desired points for the purpose of developing your approximation. We deal with function approximation in Chapter 5.

One can easily find pathological functions that make a mockery of any interpolation scheme. Consider, for example, the function

$$
f ( x ) = 3 x ^ { 2 } + { \frac { 1 } { \pi ^ { 4 } } } \ln { \bigl [ } ( \pi - x ) ^ { 2 } { \bigr ] } + 1
$$

which is well-behaved everywhere except at $x = \pi$ , very mildly singular at $x = \pi$ , and otherwise takes on all positive and negative values. Any interpolation based on the values $x = 3 . 1 3 , 3 . 1 4 , 3 . 1 5 , 3 . 1 6$ , will assuredly get a very wrong answer for the value $x = 3 . 1 4 1 6$ , even though a graph plotting those five points looks really quite smooth! (Try it.)

Because pathologies can lurk anywhere, it is highly desirable that an interpolation and extrapolation routine should provide an estimate of its own error. Such an error estimate can never be foolproof, of course. We could have a function that, for reasons known only to its maker, takes off wildly and unexpectedly between two tabulated points. Interpolation always presumes some degree of smoothness for the function interpolated, but within this framework of presumption, deviations from smoothness can be detected.

Conceptually, the interpolation process has two stages: (1) Fit (once) an interpolating function to the data points provided. (2) Evaluate (as many times as you wish) that interpolating function at a target point $x$ .

However, this two-stage method is usually not the best way to proceed in practice. Typically it is computationally less efficient, and more susceptible to roundoff error, than methods that construct a functional estimate $f ( x )$ directly from the $N$ tabulated values every time one is desired. Many practical schemes start at a nearby point $f ( x _ { i } )$ , and then add a sequence of (hopefully) decreasing corrections, as information from other nearby $f ( x _ { i } )$ ’s is incorporated. The procedure typically takes $O ( M ^ { 2 } )$ operations, where $M \ll N$ is the number of local points used. If everything is well behaved, the last correction will be the smallest, and it can be used as an informal (though not rigorous) bound on the error. In schemes like this, we might also say that there are two stages, but now they are: (1) Find the right starting position in the table $x _ { i }$ or $i$ ). (2) Perform the interpolation using $M$ nearby values (for example, centered on $x _ { i }$ ).

In the case of polynomial interpolation, it sometimes does happen that the coefficients of the interpolating polynomial are of interest, even though their use in evaluating the interpolating function should be frowned on. We deal with this possibility in $\ S 3 . 5$ .

Local interpolation, using $M$ nearest-neighbor points, gives interpolated values $f ( x )$ that do not, in general, have continuous first or higher derivatives. That happens because, as $x$ crosses the tabulated values $x _ { i }$ , the interpolation scheme switches which tabulated points are the “local” ones. (If such a switch is allowed to occur anywhere else, then there will be a discontinuity in the interpolated function itself at that point. Bad idea!)

In situations where continuity of derivatives is a concern, one must use the “stiffer” interpolation provided by a so-called spline function. A spline is a polynomial between each pair of table points, but one whose coefficients are determined “slightly” nonlocally. The nonlocality is designed to guarantee global smoothness in the interpolated function up to some order of derivative. Cubic splines (-3.3) are the most popular. They produce an interpolated function that is continuous through the second derivative. Splines tend to be stabler than polynomials, with less possibility of wild oscillation between the tabulated points.

![](images/95313c1159d825ac9f1b7b80f4a90cce66770b16976d14774cb5f27369500eb3.jpg)  
Figure 3.0.1. (a) A smooth function (solid line) is more accurately interpolated by a high-order polynomial (shown schematically as dotted line) than by a low-order polynomial (shown as a piecewise linear dashed line). (b) A function with sharp corners or rapidly changing higher derivatives is less accurately approximated by a high-order polynomial (dotted line), which is too “stiff,” than by a low-order polynomial (dashed lines). Even some smooth functions, such as exponentials or rational functions, can be badly approximated by high-order polynomials.

The number $M$ of points used in an interpolation scheme, minus 1, is called the order of the interpolation. Increasing the order does not necessarily increase the accuracy, especially in polynomial interpolation. If the added points are distant from the point of interest $x$ , the resulting higher-order polynomial, with its additional constrained points, tends to oscillate wildly between the tabulated values. This oscillation may have no relation at all to the behavior of the “true” function (see Figure 3.0.1). Of course, adding points close to the desired point usually does help, but a finer mesh implies a larger table of values, which is not always available.

For polynomial interpolation, it turns out that the worst possible arrangement of the $x _ { i }$ ’s is for them to be equally spaced. Unfortunately, this is by far the most common way that tabulated data are gathered or presented. High-order polynomial interpolation on equally spaced data is ill-conditioned: small changes in the data can give large differences in the oscillations between the points. The disease is particularly bad if you are interpolating on values of an analytic function that has poles in the complex plane lying inside a certain oval region whose major axis is the $M$ -point interval. But even if you have a function with no nearby poles, roundoff error can, in effect, create nearby poles and cause big interpolation errors. In $\ S 5 . 8$ we will see that these issues go away if you are allowed to choose an optimal set of $x _ { i }$ ’s. But when you are handed a table of function values, that option is not available.

As the order is increased, it is typical for interpolation error to decrease at first, but only up to a certain point. Larger orders result in the error exploding.

For the reasons mentioned, it is a good idea to be cautious about high-order interpolation. We can enthusiastically endorse polynomial interpolation with 3 or 4 points; we are perhaps tolerant of 5 or 6; but we rarely go higher than that unless there is quite rigorous monitoring of estimated errors. Most of the interpolation methods in this chapter are applied piecewise using only $M$ points at a time, so that the order is a fixed value $M - 1$ , no matter how large $N$ is. As mentioned, splines (-3.3) are a special case where the function and various derivatives are required to be continuous from one interval to the next, but the order is nevertheless held fixed a a small value (usually 3).

In $\ S 3 . 4$ we discuss rational function interpolation. In many, but not all, cases, rational function interpolation is more robust, allowing higher orders to give higher accuracy. The standard algorithm, however, allows poles on the real axis or nearby in the complex plane. (This is not necessarily bad: You may be trying to approximate a function with such poles.) A newer method, barycentric rational interpolation (-3.4.1) suppresses all nearby poles. This is the only method in this chapter for which we might actually encourage experimentation with high order (say, $> ~ 6$ ). Barycentric rational interpolation competes very favorably with splines: its error is often smaller, and the resulting approximation is infinitely smooth (unlike splines).

The interpolation methods below are also methods for extrapolation. An important application, in Chapter 17, is their use in the integration of ordinary differential equations. There, considerable care is taken with the monitoring of errors. Otherwise, the dangers of extrapolation cannot be overemphasized: An interpolating function, which is perforce an extrapolating function, will typically go berserk when the argument $x$ is outside the range of tabulated values by more (and often significantly less) than the typical spacing of tabulated points.

Interpolation can be done in more than one dimension, e.g., for a function $f ( x , y , z )$ . Multidimensional interpolation is often accomplished by a sequence of one-dimensional interpolations, but there are also other techniques applicable to scattered data. We discuss multidimensional methods in $\ S 3 . 6 - \ S 3 . 8$ .

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 2 5 . 2$ .   
Ueberhuber, C.W. 1997, Numerical Computation: Methods, Software, and Analysis, vol. 1 (Berlin: Springer), Chapter 9.   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 2.   
Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 3.   
Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), Chapter 5.   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), Chapter 3.   
Isaacson, E., and Keller, H.B. 1966, Analysis of Numerical Methods; reprinted 1994 (New York: Dover), Chapter 6.

# 3.1 Preliminaries: Searching an Ordered Table

We want to define an interpolation object that knows everything about interpolation except one thing — how to actually interpolate! Then we can plug mathematically different interpolation methods into the object to get different objects sharing a common user interface. A key task common to all objects in this framework is finding your place in the table of $x _ { i }$ ’s, given some particular value $x$ at which the function evaluation is desired. It is worth some effort to do this efficiently; otherwise you can easily spend more time searching the table than doing the actual interpolation.

Our highest-level object for one-dimensional interpolation is an abstract base class containing just one function intended to be called by the user: interp $\left( \mathbf { \boldsymbol { x } } \right)$ returns the interpolated function value at $x$ . The base class “promises,” by declaring a virtual function rawinterp $( { \mathrm { j } } 1 0 , \mathbf { x } )$ , that every derived interpolation class will provide a method for local interpolation when given an appropriate local starting point in the table, an offset $\mathtt { j l o }$ . Interfacing between interp and rawinterp must thus be a method for calculating $\mathtt { j l o }$ from $x$ , that is, for searching the table. In fact, we will use two such methods.

# struct Base_interp

Abstract base class used by all interpolation routines in this chapter. Only the routine interp is called directly by the user.

Int n, mm, jsav, cor, dj;   
const Doub \*xx, \*yy;   
Base_interp(VecDoub_I &x, const Doub \*y, Int m)   
Constructor: Set up for interpolating on a table of x’s and y’s of length m. Normally called   
by a derived class, not by the user. : n(x.size()), mm(m), jsav(0), cor(0), xx(&x[0]), yy(y) { dj $=$ MIN(1,(int)pow((Doub)n,0.25));   
}   
Doub interp(Doub x) {   
Given a value x, return an interpolated value, using data pointed to by xx and yy. Int jlo $=$ cor ? hunt(x) : locate(x); return rawinterp(jlo,x);   
} Int locate(const Doub x); See definitions below.   
Int hunt(const Doub x);

Doub virtual rawinterp(Int jlo, Doub ${ \bf { x } } ) \ = \ 0 ;$ Derived classes provide this as the actual interpolation method.

# };

Formally, the problem is this: Given an array of abscissas $x _ { j }$ , $j = 0 , \ldots , N - 1$ , with the abscissas either monotonically increasing or monotonically decreasing, and given an integer $M \leq N$ , and a number $x$ , find an integer $j _ { \mathrm { l o } }$ such that $x$ is centered

among the $M$ abscissas $x _ { j _ { \mathrm { l o } } } , \dots , x _ { j _ { \mathrm { l o } } + M - 1 }$ . By centered we mean that $x$ lies between $x _ { m }$ and $x _ { m + 1 }$ insofar as possible, where

$$
m = j _ { \mathrm { l o } } + \left\lfloor { \frac { M - 2 } { 2 } } \right\rfloor
$$

By “insofar as possible” we mean that $j _ { \mathrm { l o } }$ should never be less than zero, nor should $j _ { \mathrm { l o } } + M - 1$ be greater than $N - 1$ .

In most cases, when all is said and done, it is hard to do better than bisection, which will find the right place in the table in about $\log _ { 2 } N$ tries.

# Int Base_interp::locate(const Doub x)

Given a value $\mathbf { x }$ , return a value $\dot { \mathsf { J } }$ such that $\mathbf { x }$ is (insofar as possible) centered in the subrange $\mathbf { x } \mathbf { x } \left[ \mathbf { j } \cdot \mathbf { \nabla } \cdot \mathbf { j } \mathbf { + m m } \mathbf { - } 1 \right]$ , where $\tt x x$ is the stored pointer. The values in xx must be monotonic, either increasing or decreasing. The returned value is not less than 0, nor greater than $\mathtt { n - 1 }$ .

Int ju,jm,jl;   
if $\mathrm { ( n ~ < ~ 2 ~ | ~ | ~ \ m m ~ < ~ 2 ~ | ~ | ~ \ m m ~ > ~ n ) }$ throw("locate size error");   
Bool ascnd $\cdot ^ { = }$ (xx[n-1] $> =$ xx[0]); True if ascending order of table, false otherwise.   
$\scriptstyle { \mathrm { j } } 1 = 0$ ; Initialize lower   
$\scriptstyle { \mathrm { j u = n - 1 } }$ ; and upper limits.   
while (ju-jl > 1) { If we are not yet done, jm $=$ (ju+jl) >> 1; compute a midpoint, if (x >= xx[jm] $= =$ ascnd) jl=jm; and replace either the lower limit else ju=jm; or the upper limit, as appropriate.   
} Repeat until the test condition is satisfied.   
cor $=$ abs(jl-jsav) $>$ dj ? 0 : 1; Decide whether to use hunt or locate next time.   
jsav $=$ jl;   
return MAX(0,MIN(n-mm,jl-((mm-2)>>1)));

The above locate routine accesses the array of values $\tt x x \left[ \right]$ via a pointer stored by the base class. This rather primitive method of access, avoiding the use of a higher-level vector class like VecDoub, is here preferable for two reasons: (1) It’s usually faster; and (2) for twodimensional interpolation, we will later need to point directly into a row of a matrix. The peril of this design choice is that it assumes that consecutive values of a vector are stored consecutively, and similarly for consecutive values of a single row of a matrix. See discussion in $\ S 1 . 4 . 2$ .

# 3.1.1 Search with Correlated Values

Experience shows that in many, perhaps even most, applications, interpolation routines are called with nearly identical abscissas on consecutive searches. For example, you may be generating a function that is used on the right-hand side of a differential equation: Most differential equation integrators, as we shall see in Chapter 17, call for right-hand side evaluations at points that hop back and forth a bit, but whose trend moves slowly in the direction of the integration.

In such cases it is wasteful to do a full bisection, ab initio, on each call. Much more desirable is to give our base class a tiny bit of intelligence: If it sees two calls that are “close,” it anticipates that the next call will also be. Of course, there must not be too big a penalty if it anticipates wrongly.

The hunt method starts with a guessed position in the table. It first “hunts,” either up or down, in increments of 1, then 2, then 4, etc., until the desired value is bracketed. It then bisects in the bracketed interval. At worst, this routine is about a factor of 2 slower than locate above (if the hunt phase expands to include the whole table). At best, it can be a factor of $\log _ { 2 } \mathtt { n }$ faster than locate, if the desired point is usually quite close to the input guess. Figure 3.1.1 compares the two routines.

![](images/68f2e171cf90aa5c9217bf3987de9d42d7d3f1eddba0a5632bae035fb8af8720.jpg)  
Figure 3.1.1. Finding a table entry by bisection. Shown here is the sequence of steps that converge to element 50 in a table of length 64. (b) The routine hunt searches from a previous known position in the table by increasing steps and then converges by bisection. Shown here is a particularly unfavorable example, converging to element 31 from element 6. A favorable example would be convergence to an element near 6, such as 8, which would require just three “hops.”

# Int Base_interp::hunt(const Doub x)

Given a value x, return a value j such that $\mathbf { x }$ is (insofar as possible) centered in the subrange $\mathbf { x } \mathbf { x } \left[ \mathbf { j } \cdot \mathbf { \nabla } \cdot \mathbf { j } \mathbf { + m m } \mathbf { - } 1 \right]$ , where $_ { \tt X X }$ is the stored pointer. The values in xx must be monotonic, either increasing or decreasing. The returned value is not less than 0, nor greater than $\mathtt { n - 1 }$ . {

Int $\mathrm { j } \mathrm { 1 = }$ jsav, jm, ju, $\mathtt { i n c } = 1$ ;   
if $\mathrm { ( n ~ < ~ 2 ~ | ~ | ~ \ m m ~ < ~ 2 ~ | ~ | ~ \ m m ~ > ~ n ) }$ ) throw("hunt size error");   
Bool ascnd=(xx[n-1] $> = \ \mathbf { x } \mathbf { x } \left[ 0 \right]$ ); True if ascending order of table, false otherwise.   
if (jl $< ~ 0$ || ${ \mathfrak { j } } 1 > { \mathfrak { n } } { - } 1 ;$ ) { Input guess not useful. Go immediately to bisec-${ \mathrm { j 1 } } = 0 { \mathrm { : } }$ ; tion. $\scriptstyle { \dot { \mathtt { J } } } \mathtt { u } = \mathtt { n } - 1$ ;   
} else { if (x >= xx[jl] $= =$ ascnd) { Hunt up: for (;;) { ju $= \mathrm { ~ j ~ 1 ~ } +$ inc; if (ju $> = \ n - 1$ ) { ju $\ l = \ \mathtt { n - 1 }$ ; break;} Off end of table. else if $( \mathbb { x } < \mathbb { x } \mathbb { x } \mathbb { [ j u ] } = =$ ascnd) break; Found bracket. else { Not done, so double the increment and try again. ${ \ j } 1 \ = \ { \ j } { \ u } ;$ inc $+ =$ inc; } } } else { Hunt down: ${ \mathrm { j } } { \mathrm { u } } \ = \ { \mathrm { j } } 1 { \mathrm { : } }$ ; for (;;) { $\mathrm { j } 1 ~ = ~ \mathrm { j } 1$ - inc; if (jl $\scriptstyle < = 0$ ) { $\mathrm { ~ j ~ 1 ~ } = \mathrm { ~ 0 ~ }$ ; break;} Off end of table. else if $( \mathbf { x _ { \alpha } > = x } \mathbf { x } \mathbf { [ j 1 ] _ { \alpha } = } \mathbf { = }$ ascnd) break; Found bracket. else { Not done, so double the increment and try again. j $\mathrm { ~ \tt ~ { ~ 1 ~ } ~ } = \mathrm { ~ \tt ~ { ~ j ~ 1 ~ } ~ }$ ; inc $+ =$ inc;


<!-- chunk 0003: pages 141-210 -->
} } } } while (ju-jl > 1) { Hunt is done, so begin the final bisection phase: jm $=$ (ju+jl) >> 1; if (x >= xx[jm] $= =$ ascnd) jl=jm; else ju=jm; cor $=$ abs(jl-jsav) $>$ dj ? 0 : 1; Decide whether to use hunt or locate next jsav $= \ j 1$ ; time. return MAX(0,MIN(n-mm,jl-((mm-2)>>1)));

The methods locate and hunt each update the boolean variable cor in the base class, indicating whether consecutive calls seem correlated. That variable is then used by interp to decide whether to use locate or hunt on the next call. This is all invisible to the user, of course.

# 3.1.2 Example: Linear Interpolation

You may think that, at this point, we have wandered far from the subject of interpolation methods. To show that we are actually on track, here is a class that efficiently implements piecewise linear interpolation.

struct Linear_interp : Base_interp   
Piecewise linear interpolation object. Construct with x and y vectors, then call interp for interpolated values.

Linear_interp(VecDoub_I &xv, VecDoub_I &yv) : Base_interp(xv,&yv[0],2) {} Doub rawinterp(Int j, Doub x) if (xx[j] $= =$ xx[j+1]) return yy[j]; Table is defective, but we can recover. else return yy[j] $^ +$ ((x-xx[j])/(xx[j+1]-xx[j]))\*(yy[j+1]-yy[j]); } };

You construct a linear interpolation object by declaring an instance with your filled vectors of abscissas $x _ { i }$ and function values $y _ { i } = f ( x _ { i } )$ ,

Int n=...;  
VecDoub xx(n), yy(n);  
Linear_interp myfunc(xx,yy);

Behind the scenes, the base class constructor is called with $M = 2$ because linear interpolation uses just the two points bracketing a value. Also, pointers to the data are saved. (You must ensure that the vectors $\tt x x$ and yy don’t go out of scope while myfunc is in use.)

When you want an interpolated value, it’s as simple as

Doub x,y;   
$\mathrm { ~ y ~ } =$ myfunc.interp(x);

If you have several functions that you want to interpolate, you declare a separate instance of Linear_interp for each one.

We will now use the same interface for more advanced interpolation methods.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 6 . 2 . 1$ .

# 3.2 Polynomial Interpolation and Extrapolation

Through any two points there is a unique line. Through any three points there is a unique quadratic. Et cetera. The interpolating polynomial of degree $M - 1$ through the $M$ points $y _ { 0 } = f ( x _ { 0 } ) , y _ { 1 } = f ( x _ { 1 } ) , \ldots , y _ { M - 1 } = f ( x _ { M - 1 } )$ is given explicitly by Lagrange’s classical formula,

$$
\begin{array} { l } { { P ( x ) = \displaystyle \frac { ( x - x _ { 1 } ) ( x - x _ { 2 } ) . . . ( x - x _ { M - 1 } ) } { ( x _ { 0 } - x _ { 1 } ) ( x _ { 0 } - x _ { 2 } ) . . . ( x _ { 0 } - x _ { M - 1 } ) } y _ { 0 } } } \\ { { + \displaystyle \frac { ( x - x _ { 0 } ) ( x - x _ { 2 } ) . . . ( x - x _ { M - 1 } ) } { ( x _ { 1 } - x _ { 0 } ) ( x _ { 1 } - x _ { 2 } ) . . . ( x _ { 1 } - x _ { M - 1 } ) } y _ { 1 } + \cdots } } \\ { { + \displaystyle \frac { ( x - x _ { 0 } ) ( x - x _ { 1 } ) . . . ( x - x _ { M - 2 } ) } { ( x _ { M - 1 } - x _ { 0 } ) ( x _ { M - 1 } - x _ { 1 } ) . . . ( x _ { M - 1 } - x _ { M - 2 } ) } y _ { M - 1 } } } \end{array}
$$

There are $M$ terms, each a polynomial of degree $M - 1$ and each constructed to be zero at all of the $x _ { i }$ ’s except one, at which it is constructed to be $y _ { i }$ .

It is not terribly wrong to implement the Lagrange formula straightforwardly, but it is not terribly right either. The resulting algorithm gives no error estimate, and it is also somewhat awkward to program. A much better algorithm (for constructing the same, unique, interpolating polynomial) is Neville’s algorithm, closely related to and sometimes confused with Aitken’s algorithm, the latter now considered obsolete.

Let $P _ { 0 }$ be the value at $x$ of the unique polynomial of degree zero (i.e., a constant) passing through the point $( x _ { 0 } , y _ { 0 } )$ ; so $P _ { 0 } = y _ { 0 }$ . Likewise define $P _ { 1 } , P _ { 2 } , \ldots$ ; $P _ { M - 1 }$ . Now let $P _ { 0 1 }$ be the value at $x$ of the unique polynomial of degree one passing through both $( x _ { 0 } , y _ { 0 } )$ and $( x _ { 1 } , y _ { 1 } )$ . Likewise $P _ { 1 2 }$ $, P _ { 2 3 } , . . . , P _ { ( M - 2 ) ( M - 1 ) }$ . Similarly, for higher-order polynomials, up to $P _ { 0 1 2 . . . ( M - 1 ) }$ , which is the value of the unique interpolating polynomial through all $M$ points, i.e., the desired answer. The various $P$ ’s form a “tableau” with “ancestors” on the left leading to a single “descendant” at the extreme right. For example, with $M = 4$ ,

$$
\begin{array} { l l l l l l } { { x _ { 0 } : } } & { { \mathrm { } } } & { { y _ { 0 } = P _ { 0 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { P _ { 0 1 } } } & { { } } & { { } } \\ { { x _ { 1 } : } } & { { \mathrm { } } } & { { y _ { 1 } = P _ { 1 } } } & { { } } & { { P _ { 0 1 2 } } } & { { } } \\ { { } } & { { } } & { { } } & { { P _ { 1 2 } } } & { { } } & { { P _ { 0 1 2 3 } } } \\ { { x _ { 2 } : } } & { { \mathrm { } } } & { { y _ { 2 } = P _ { 2 } } } & { { } } & { { P _ { 1 2 3 } } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { P _ { 2 3 } } } & { { } } & { { } } \\ { { x _ { 3 } : } } & { { \mathrm { } } } & { { y _ { 3 } = P _ { 3 } } } & { { } } & { { } } & { { } } & { { } } \end{array}
$$

Neville’s algorithm is a recursive way of filling in the numbers in the tableau a column at a time, from left to right. It is based on the relationship between a

“daughter” $P$ and its two “parents,”

$$
P _ { i ( i + 1 ) \dots ( i + m ) } = { \frac { ( x - x _ { i + m } ) P _ { i ( i + 1 ) \dots ( i + m - 1 ) } + ( x _ { i } - x ) P _ { ( i + 1 ) ( i + 2 ) \dots ( i + m ) } } { x _ { i } - x _ { i + m } } }
$$

This recurrence works because the two parents already agree at points $x _ { i + 1 } \ldots$ $x _ { i + m - 1 }$ .

An improvement on the recurrence (3.2.3) is to keep track of the small differences between parents and daughters, namely to define (for $m = 1 , 2 , \ldots , M - 1 )$ ,

$$
\begin{array} { l } { { C _ { m , i } \equiv P _ { i \dots ( i + m ) } - P _ { i \dots ( i + m - 1 ) } } } \\ { { D _ { m , i } \equiv P _ { i \dots ( i + m ) } - P _ { ( i + 1 ) \dots ( i + m ) } . } } \end{array}
$$

Then one can easily derive from (3.2.3) the relations

$$
\begin{array} { l } { \displaystyle { D _ { m + 1 , i } = \frac { ( x _ { i + m + 1 } - x ) ( C _ { m , i + 1 } - D _ { m , i } ) } { x _ { i } - x _ { i + m + 1 } } } } \\ { \displaystyle { C _ { m + 1 , i } = \frac { ( x _ { i } - x ) ( C _ { m , i + 1 } - D _ { m , i } ) } { x _ { i } - x _ { i + m + 1 } } } } \end{array}
$$

At each level $m$ , the $C$ ’s and $D$ ’s are the corrections that make the interpolation one order higher. The final answer $P _ { 0 . . . ( M - 1 ) }$ is equal to the sum of any $y _ { i }$ plus a set of $C$ ’s and/or $D$ ’s that form a path through the family tree to the rightmost daughter.

Here is the class implementing polynomial interpolation or extrapolation. All of its “support infrastructure” is in the base class Base_interp. It needs only to provide a rawinterp method that contains Neville’s algorithm.

# struct Poly_interp : Base_interp

Polynomial interpolation object. Construct with $\mathbf { x }$ and $\mathbf { y }$ vectors, and the number $M$ of points to be used locally (polynomial order plus one), then call interp for interpolated values.

Doub dy; Poly_interp(VecDoub_I &xv, VecDoub_I &yv, Int m) : Base_interp(xv,&yv[0],m), dy(0.) {} Doub rawinterp(Int jl, Doub x);

# };

# Doub Poly_interp::rawinterp(Int jl, Doub x)

Given a value $\mathbf { x }$ , and using pointers to data xx and yy, this routine returns an interpolated value y, and stores an error estimate dy. The returned value is obtained by mm-point polynomial interpolation on the subrange $\mathbf { x } \mathbf { x } \left[ \mathbf { j } \mathbf { 1 } . . . \mathbf { j } \mathbf { 1 } + \mathbf { m m } ^ { - 1 } \right]$ .

Int i,m,ns ${ = } 0$ ;   
Doub y,den,dif,dift,ho,hp,w;   
const Doub \*xa $=$ &xx[jl], \*ya $=$ &yy[jl];   
VecDoub c(mm),d(mm);   
dif $=$ abs(x-xa[0]);   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<mm; $\dot { 1 } + +$ ) { Here we find the index ns of the closest table entry, if ((dift $=$ abs(x-xa[i])) $<$ dif) { ns=i; dif=dift; } c[i]=ya[i]; and initialize the tableau of c’s and d’s. d[i]=ya[i];   
}   
y=ya[ns--]; This is the initial approximation to y.   
for ( $\scriptstyle { \mathtt { m } } = 1$ ;m<mm;m++) { For each column of the tableau,

for (i=0;i<mm-m;i++) { we loop over the current c’s and d’s and update ho=xa[i]-x; them. hp=xa[i+m]-x; w=c[i+1]-d[i]; if ((den=ho-hp) == 0.0) throw("Poly_interp error"); This error can occur only if two input xa’s are (to within roundoff) identical. den=w/den; d[i] $\risingdotseq$ hp\*den; Here the c’s and d’s are updated. c[i] $=$ ho\*den; $\begin{array} { r } { \mathrm { ~  ~ y ~ } + = \mathrm { ~  ~ ( d y = ( 2 * ( n s + 1 ) ~  ~ < ~ ( m m - m ) ~  ~ \stackrel { { ~ \wedge ~ } } { ~ } c ~ \unboldmath [ n s + 1 ] ~ \unboldmath : ~ d [ n s - - 1 ) ~ ) ~ } ; } \end{array}$ After each column in the tableau is completed, we decide which correction, c or d, we want to add to our accumulating value of y, i.e., which path to take through the tableau — forking up or down. We do this in such a way as to take the most “straight line” route through the tableau to its apex, updating ns accordingly to keep track of where we are. This route keeps the partial approximations centered (insofar as possible) on the target $\mathbf { x }$ . The last dy added is thus the error indication. } return y;

The user interface to Poly_interp is virtually the same as for Linear_interp (end of -3.1), except that an additional argument in the constructor sets $M$ , the number of points used (the order plus one). A cubic interpolator looks like this:

Int n=...;   
VecDoub xx(n), yy(n);   
Poly_interp myfunc(xx,yy,4);

Poly_interp stores an error estimate dy for the most recent call to its interp function:

Doub x,y,err;   
$\mathtt { y } =$ myfunc.interp(x);   
err $=$ myfunc.dy;

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 2 5 . 2$ .   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 2 . 1$ .   
Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 6 . 1$ .

# 3.3 Cubic Spline Interpolation

Given a tabulated function $y _ { i } = y ( x _ { i } )$ ; $i = 0 . . . N - 1$ , focus attention on one particular interval, between $x _ { j }$ and $x _ { j + 1 }$ . Linear interpolation in that interval gives the interpolation formula

$$
y = A y _ { j } + B y _ { j + 1 }
$$

where

$$
A \equiv { \frac { x _ { j + 1 } - x } { x _ { j + 1 } - x _ { j } } } \qquad B \equiv 1 - A = { \frac { x - x _ { j } } { x _ { j + 1 } - x _ { j } } }
$$

Equations (3.3.1) and (3.3.2) are a special case of the general Lagrange interpolation formula (3.2.1).

Since it is (piecewise) linear, equation (3.3.1) has zero second derivative in the interior of each interval and an undefined, or infinite, second derivative at the abscissas $x _ { j }$ . The goal of cubic spline interpolation is to get an interpolation formula that is smooth in the first derivative and continuous in the second derivative, both within an interval and at its boundaries.

Suppose, contrary to fact, that in addition to the tabulated values of $y _ { i }$ , we also have tabulated values for the function’s second derivatives, $y ^ { \prime \prime }$ , that is, a set of numbers $y _ { i } ^ { \prime \prime }$ . Then, within each interval, we can add to the right-hand side of equation (3.3.1) a cubic polynomial whose second derivative varies linearly from a value $y _ { j } ^ { \prime \prime }$ on the left to a value $y _ { j + 1 } ^ { \prime \prime }$ on the right. Doing so, we will have the desired continuous second derivative. If we also construct the cubic polynomial to have zero values at $x _ { j }$ and $x _ { j + 1 }$ , then adding it in will not spoil the agreement with the tabulated functional values $y _ { j }$ and $y _ { j + 1 }$ at the endpoints $x _ { j }$ and $x _ { j + 1 }$ .

A little side calculation shows that there is only one way to arrange this construction, namely replacing (3.3.1) by

$$
y = A y _ { j } + B y _ { j + 1 } + C y _ { j } ^ { \prime \prime } + D y _ { j + 1 } ^ { \prime \prime }
$$

where $A$ and $B$ are defined in (3.3.2) and

$$
{ \begin{array} { r l r } { C \equiv { \frac { 1 } { 6 } } ( A ^ { 3 } - A ) ( x _ { j + 1 } - x _ { j } ) ^ { 2 } } & { { } } & { D \equiv { \frac { 1 } { 6 } } ( B ^ { 3 } - B ) ( x _ { j + 1 } - x _ { j } ) ^ { 2 } } \end{array} }
$$

Notice that the dependence on the independent variable $x$ in equations (3.3.3) and (3.3.4) is entirely through the linear $x$ -dependence of $A$ and $B$ , and (through $A$ and $B$ ) the cubic $x$ -dependence of $C$ and $D$ .

We can readily check that $y ^ { \prime \prime }$ is in fact the second derivative of the new interpolating polynomial. We take derivatives of equation (3.3.3) with respect to $x$ , using the definitions of $A , B , C$ ; and $D$ to compute $d A / d x , d B / d x , d C / d x$ , and $d D / d x$ . The result is

$$
\frac { d y } { d x } = \frac { y _ { j + 1 } - y _ { j } } { x _ { j + 1 } - x _ { j } } - \frac { 3 A ^ { 2 } - 1 } { 6 } ( x _ { j + 1 } - x _ { j } ) y _ { j } ^ { \prime \prime } + \frac { 3 B ^ { 2 } - 1 } { 6 } ( x _ { j + 1 } - x _ { j } ) y _ { j + 1 } ^ { \prime \prime }
$$

for the first derivative, and

$$
{ \frac { d ^ { 2 } y } { d x ^ { 2 } } } = A y _ { j } ^ { \prime \prime } + B y _ { j + 1 } ^ { \prime \prime }
$$

for the second derivative. Since $A = 1$ at $x _ { j }$ , $A = 0$ at $x _ { j + 1 }$ , while $B$ is just the other way around, (3.3.6) shows that $y ^ { \prime \prime }$ is just the tabulated second derivative, and also that the second derivative will be continuous across, e.g., the boundary between the two intervals $( x _ { j - 1 } , x _ { j } )$ and $( x _ { j } , x _ { j + 1 } )$ .

The only problem now is that we supposed the $y _ { i } ^ { \prime \prime }$ ’s to be known, when, actually, they are not. However, we have not yet required that the first derivative, computed from equation (3.3.5), be continuous across the boundary between two intervals. The key idea of a cubic spline is to require this continuity and to use it to get equations for the second derivatives $y _ { i } ^ { \prime \prime }$ .

The required equations are obtained by setting equation (3.3.5) evaluated for $x = x _ { j }$ in the interval $( x _ { j - 1 } , x _ { j } )$ equal to the same equation evaluated for $x = x _ { j }$ but in the interval $( x _ { j } , x _ { j + 1 } )$ . With some rearrangement, this gives (for $j = 1 , \ldots$ ; $N - 2 )$

$$
\frac { x _ { j } - x _ { j - 1 } } { 6 } y _ { j - 1 } ^ { \prime \prime } + \frac { x _ { j + 1 } - x _ { j - 1 } } { 3 } y _ { j } ^ { \prime \prime } + \frac { x _ { j + 1 } - x _ { j } } { 6 } y _ { j + 1 } ^ { \prime \prime } = \frac { y _ { j + 1 } - y _ { j } } { x _ { j + 1 } - x _ { j } } - \frac { y _ { j } - y _ { j - 1 } } { x _ { j } - x _ { j - 1 } }
$$

These are $N - 2$ linear equations in the $N$ unknowns $y _ { i } ^ { \prime \prime } , i = 0 , \ldots , N - 1$ . Therefore there is a two-parameter family of possible solutions.

For a unique solution, we need to specify two further conditions, typically taken as boundary conditions at $x _ { 0 }$ and $x N { - } 1$ . The most common ways of doing this are either

- set one or both of $y _ { 0 } ^ { \prime \prime }$ and $y _ { N - 1 } ^ { \prime \prime }$ equal to zero, giving the so-called natural cubic spline, which has zero second derivative on one or both of its boundaries, or - set either of $y _ { 0 } ^ { \prime \prime }$ and $y _ { N - 1 } ^ { \prime \prime }$ to values calculated from equation (3.3.5) so as to make the first derivative of the interpolating function have a specified value on either or both boundaries.

Although the boundary condition for natural splines is commonly used, another possibility is to estimate the first derivatives at the endpoints from the first and last few tabulated points. For details of how to do this, see the end of $\ S 3 . 7$ . Best, of course, is if you can compute the endpoint first derivatives analytically.

One reason that cubic splines are especially practical is that the set of equations (3.3.7), along with the two additional boundary conditions, are not only linear, but also tridiagonal. Each $y _ { j } ^ { \prime \prime }$ is coupled only to its nearest neighbors at $j \pm 1$ . Therefore, the equations can be solved in $O ( N )$ operations by the tridiagonal algorithm (-2.4). That algorithm is concise enough to build right into the function called by the constructor.

The object for cubic spline interpolation looks like this:

struct Spline_interp : Base_interp

Cubic spline interpolation object. Construct with $\mathbf { x }$ and $\mathbf { y }$ vectors, and (optionally) values of the first derivative at the endpoints, then call interp for interpolated values.

VecDoub y2;

Spline_interp(VecDoub_I &xv, VecDoub_I &yv, Doub yp1=1.e99, Doub ypn=1.e99)   
: Base_interp(xv,&yv[0],2), y2(xv.size())   
{sety2(&xv[0],&yv[0],yp1,ypn);}   
Spline_interp(VecDoub_I &xv, const Doub \*yv, Doub yp $\scriptstyle 1 = 1$ .e99, Doub ypn $^ { = 1 }$ .e99)   
: Base_interp(xv,yv,2), y2(xv.size())   
{sety2(&xv[0],yv,yp1,ypn);} void sety2(const Doub \*xv, const Doub \*yv, Doub yp1, Doub ypn);   
Doub rawinterp(Int jl, Doub xv);

For now, you can ignore the second constructor; it will be used later for two-dimensional spline interpolation.

The user interface differs from previous ones only in the addition of two constructor arguments, used to set the values of the first derivatives at the endpoints, $y _ { 0 } ^ { \prime }$ and $y _ { N - 1 } ^ { \prime }$ . These are coded with default values that signal that you want a natural spline, so they can be omitted in most situations. Both constructors invoke sety2 to do the actual work of computing, and storing, the second derivatives.

void Spline_interp::sety2(const Doub \*xv, const Doub \*yv, Doub yp1, Doub ypn) This routine stores an array $\mathtt { y 2 } [ 0 \ldots \mathtt { n } { - } 1 ]$ with second derivatives of the interpolating function at the tabulated points pointed to by xv, using function values pointed to by yv. If yp1 and/or ypn are equal to $1 \times 1 0 ^ { 9 9 }$ or larger, the routine is signaled to set the corresponding boundary condition for a natural spline, with zero second derivative on that boundary; otherwise, they are the values of the first derivatives at the endpoints.

Int i,k;   
Doub p,qn,sig,un;   
Int n=y2.size();   
VecDoub $\mathtt { u } ( \mathtt { n } ^ { - 1 } )$ ;   
if (yp1 $>$ 0.99e99) The lower boundary condition is set either to be “nat-${ \tt y } 2 \left[ 0 \right] = { \tt u } \left[ 0 \right] = 0 . 0 \ \mathrm { : }$ ; ural”   
else { or else to have a specified first derivative. y2[0] $= - 0 . 5$ ; u[0] $=$ (3.0/(xv[1]-xv[0]))\*((yv[1]-yv[0])/(xv[1]-xv[0])-yp1);   
}   
for ( $\dot { 1 } = 1$ ;i<n-1; $\dot { 1 } + + \dot { 1 }$ ) { This is the decomposition loop of the tridiagonal alsig=(xv[i]-xv[i-1])/(xv[i+1]-xv[i-1]); gorithm. y2 and u are used for temp=sig\*y2[i-1]+2.0; porary storage of the decomposed y2[i] $=$ (sig-1.0)/p; factors. u[i] $=$ (yv[i+1]-yv[i])/(xv[i+1]-xv[i]) - (yv[i]-yv[i-1])/(xv[i]-xv[i-1]); u[i] $=$ (6.0\*u[i]/(xv[i+1]-xv[i-1])-sig\*u[i-1])/p;   
}   
if (ypn $>$ 0.99e99) The upper boundary condition is set either to be qn=un=0.0; “natural”   
else { or else to have a specified first derivative. qn=0.5; un=(3.0/(xv[n-1]-xv[n-2]))\*(ypn-(yv[n-1]-yv[n-2])/(xv[n-1]-xv[n-2]));   
}   
y2[n-1] $=$ (un-qn\*u[n-2])/(qn\*y2[n-2]+1.0);   
for (k=n-2;k>=0;k--) This is the backsubstitution loop of the tridiagonal y2[k]=y2[k]\*y2[k+1]+u[k]; algorithm.

Note that, unlike the previous object Poly_interp, Spline_interp stores data that depend on the contents of your array of $y _ { i }$ ’s at its time of creation — a whole vector y2. Although we didn’t point it out, the previous interpolation object actually allowed the misuse of altering the contents of their $x$ and $y$ arrays on the fly (as long as the lengths didn’t change). If you do that with Spline_interp, you’ll get definitely wrong answers!

The required rawinterp method, never called directly by the users, uses the stored y2 and implements equation (3.3.3):

Doub Spline_interp::rawinterp(Int jl, Doub x)   
Given a value x, and using pointers to data xx and yy, and the stored vector of second derivatives y2, this routine returns the cubic spline interpolated value y.   
{ Int klo=jl,khi=jl+1;   
Doub y,h,b,a;   
h=xx[khi]-xx[klo];   
if $\mathit { \Omega } ^ { \prime } \mathbf { h } \ = = \ 0 . 0$ ) throw("Bad input to routine splint");   
$\mathtt { a } =$ (xx[khi]-x)/h;

The xa’s must be distinct.

$\mathtt { b } =$ (x-xx[klo])/h; Cubic spline polynomial is now evaluated.   
y=a\*yy[klo]+b\*yy[khi]+((a\*a\*a-a)\*y2[klo] +(b\*b\*b-b)\*y2[khi]) $^ *$ (h\*h)/6.0;   
return y;

Typical use looks like this:

Int n=...;   
VecDoub xx(n), yy(n);   
Spline_interp myfunc(xx,yy);

and then, as often as you like,

Doub x,y;   
y = myfunc.interp(x);

Note that no error estimate is available.

# CITED REFERENCES AND FURTHER READING:

De Boor, C. 1978, A Practical Guide to Splines (New York: Springer).   
Ueberhuber, C.W. 1997, Numerical Computation: Methods, Software, and Analysis, vol. 1 (Berlin: Springer), Chapter 9.   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 4 . 4 - \ S 4 . 5$ .   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 2 . 4$ .   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 3 . 8$ .

# 3.4 Rational Function Interpolation and Extrapolation

Some functions are not well approximated by polynomials but are well approximated by rational functions, that is quotients of polynomials. We denote by $R _ { i ( i + 1 ) \dots ( i + m ) }$ a rational function passing through the $m + 1$ points $( x _ { i } , y _ { i } ) , \ldots$ ; $( x _ { i + m } , y _ { i + m } )$ . More explicitly, suppose

$$
R _ { i ( i + 1 ) \ldots ( i + m ) } = { \frac { P _ { \mu } ( x ) } { Q _ { \nu } ( x ) } } = { \frac { p _ { 0 } + p _ { 1 } x + \dots + p _ { \mu } x ^ { \mu } } { q _ { 0 } + q _ { 1 } x + \dots + q _ { \nu } x ^ { \nu } } }
$$

Since there are $\mu + \nu + 1$ unknown $p$ ’s and $q$ ’s ( $\scriptstyle { \dot { q } } _ { 0 }$ being arbitrary), we must have

$$
m + 1 = \mu + \nu + 1
$$

In specifying a rational function interpolating function, you must give the desired order of both the numerator and the denominator.

Rational functions are sometimes superior to polynomials, roughly speaking, because of their ability to model functions with poles, that is, zeros of the denominator of equation (3.4.1). These poles might occur for real values of $x$ , if the function to be interpolated itself has poles. More often, the function $f ( x )$ is finite for all finite real $x$ but has an analytic continuation with poles in the complex $x$ -plane. Such poles can themselves ruin a polynomial approximation, even one restricted to real values of $x$ , just as they can ruin the convergence of an infinite power series in $x$ . If you draw a circle in the complex plane around your $m$ tabulated points, then you should not expect polynomial interpolation to be good unless the nearest pole is rather far outside the circle. A rational function approximation, by contrast, will stay “good” as long as it has enough powers of $x$ in its denominator to account for (cancel) any nearby poles.

For the interpolation problem, a rational function is constructed so as to go through a chosen set of tabulated functional values. However, we should also mention in passing that rational function approximations can be used in analytic work. One sometimes constructs a rational function approximation by the criterion that the rational function of equation (3.4.1) itself have a power series expansion that agrees with the first $m + 1$ terms of the power series expansion of the desired function $f ( x )$ . This is called Pade approximation´ and is discussed in $\ S 5 . 1 2$ .

Bulirsch and Stoer found an algorithm of the Neville type that performs rational function extrapolation on tabulated data. A tableau like that of equation (3.2.2) is constructed column by column, leading to a result and an error estimate. The Bulirsch-Stoer algorithm produces the so-called diagonal rational function, with the degrees of the numerator and denominator equal (if $m$ is even) or with the degree of the denominator larger by one (if $m$ is odd; cf. equation 3.4.2 above). For the derivation of the algorithm, refer to [1]. The algorithm is summarized by a recurrence relation exactly analogous to equation (3.2.3) for polynomial approximation:

$$
\begin{array} { r l } & { R _ { i ( i + 1 ) \dots ( i + m ) } = R _ { ( i + 1 ) \dots ( i + m ) } } \\ & { \qquad + \frac { R _ { ( i + 1 ) \dots ( i + m ) } - R _ { i \dots ( i + m - 1 ) } } { \left( \frac { x - x _ { i } } { x - x _ { i + m } } \right) \left( 1 - \frac { R _ { ( i + 1 ) \dots ( i + m ) } - R _ { i \dots ( i + m - 1 ) } } { R _ { ( i + 1 ) \dots ( i + m ) } - R _ { ( i + 1 ) \dots ( i + m - 1 ) } } \right) - 1 } } \end{array}
$$

This recurrence generates the rational functions through $m + 1$ points from the ones through $m$ and (the term $R _ { ( i + 1 ) \dots ( i + m - 1 ) }$ in equation $3 . 4 . 3 ) m - 1$ points. It is started with

$$
R _ { i } = y _ { i }
$$

and with

$$
{ \cal R } \equiv [ R _ { i ( i + 1 ) \ldots ( i + m ) } \quad \mathrm { w i t h } \quad m = - 1 ] = 0
$$

Now, exactly as in equations (3.2.4) and (3.2.5) above, we can convert the recurrence (3.4.3) to one involving only the small differences

$$
\begin{array} { l } { { C _ { m , i } \equiv R _ { i \dots ( i + m ) } - R _ { i \dots ( i + m - 1 ) } } } \\ { { D _ { m , i } \equiv R _ { i \dots ( i + m ) } - R _ { ( i + 1 ) \dots ( i + m ) } } } \end{array}
$$

Note that these satisfy the relation

$$
C _ { m + 1 , i } - D _ { m + 1 , i } = C _ { m , i + 1 } - D _ { m , i }
$$

which is useful in proving the recurrences

$$
\begin{array} { r l } & { D _ { m + 1 , i } = \frac { C _ { m , i + 1 } \left( C _ { m , i + 1 } - D _ { m , i } \right) } { \left( \frac { x - x _ { i } } { x - x _ { i + m + 1 } } \right) D _ { m , i } - C _ { m , i + 1 } } } \\ & { C _ { m + 1 , i } = \frac { \left( \frac { x - x _ { i } } { x - x _ { i + m + 1 } } \right) D _ { m , i } \left( C _ { m , i + 1 } - D _ { m , i } \right) } { \left( \frac { x - x _ { i } } { x - x _ { i + m + 1 } } \right) D _ { m , i } - C _ { m , i + 1 } } } \end{array}
$$

The class for rational function interpolation is identical to that for polynomial interpolation in every way, except, of course, for the different method implemented in rawinterp. See the end of $\ S 3 . 2$ for usage. Plausible values for $M$ are in the range 4 to 7.

# struct Rat_interp : Base_interp

Diagonal rational function interpolation object. Construct with $\mathbf { x }$ and $\mathbf { y }$ vectors, and the number m of points to be used locally, then call interp for interpolated values.

Doub dy; Rat_interp(VecDoub_I &xv, VecDoub_I &yv, Int m) : Base_interp(xv,&yv[0],m), dy(0.) {} Doub rawinterp(Int jl, Doub x);

# Doub Rat_interp::rawinterp(Int jl, Doub x)

Given a value $\mathbf { x }$ , and using pointers to data xx and yy, this routine returns an interpolated value y, and stores an error estimate dy. The returned value is obtained by mm-point diagonal rational function interpolation on the subrange $\mathbf { x } \mathbf { x } \left[ \mathbf { j } \mathbf { 1 } . . \mathbf { j } \mathbf { 1 } + \mathbf { m m } - 1 \right]$ .

const Doub TINY $^ { = 1 }$ .0e-99; A small number.   
Int m,i,ns=0;   
Doub y,w,t,hh,h,dd;   
const Doub \*xa $=$ &xx[jl], \*ya = &yy[jl];   
VecDoub c(mm),d(mm);   
hh=abs(x-xa[0]);   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<mm; $\dot { 1 } + + \dot { 2 }$ ) { $\mathrm { h } =$ abs(x-xa[i]); if $( \mathbf { h _ { \alpha } } = = \mathbf { \beta } 0 . 0 ) ^ { \prime }$ ) { dy=0.0; return ya[i]; } else if (h $<$ hh) $\mathbf { n } \mathbf { s } { = } \dot { \mathbf { 1 } }$ ; hh=h; } c[i]=ya[i]; d[i]=ya[i]+TINY; The TINY part is needed to prevent a rare zero-over-zero   
} condition.   
y=ya[ns--];   
for $\scriptstyle ( { \mathtt { m } } = 1$ ;m<mm;m++) { for (i=0;i<mm-m;i++) { w=c[i+1]-d[i]; h=xa[i+m]-x; h will never be zero, since this was tested in the initial-$\mathtt { t } =$ (xa[i]-x)\*d[i]/h; izing loop. dd=t-c[i+1]; if ( $\mathsf { d } \mathsf { d } \ = = \ 0 . 0 \rangle$ ) throw("Error in routine ratint"); This error condition indicates that the interpolating function has a pole at the requested value of x. dd=w/dd; d[i] $= \mathtt { c }$ [i+1]\*dd; c[i]=t\*dd;

} y += (dy=(2\*(ns+1) < (mm-m) ? c[ns+1] : d[ns--])); } return y;

# 3.4.1 Barycentric Rational Interpolation

Suppose one tries to use the above algorithm to construct a global approximation on the entire table of values using all the given nodes $x _ { 0 } , x _ { 1 } , \ldots , x _ { N - 1 }$ . One potential drawback is that the approximation can have poles inside the interpolation interval where the denominator in (3.4.1) vanishes, even if the original function has no poles there. An even greater (related) hazard is that we have allowed the order of the approximation to grow to $N - 1$ , probably much too large.

An alternative algorithm can be derived [2] that has no poles anywhere on the real axis, and that allows the actual order of the approximation to be specified to be any integer $d \digamma < N$ . The trick is to make the degree of both the numerator and the denominator in equation (3.4.1) be $N - 1$ . This requires that the $p$ ’s and the $q$ ’s not be independent, so that equation (3.4.2) no longer holds.

The algorithm utilizes the barycentric form of the rational interpolant

$$
R ( x ) = { \frac { \displaystyle \sum _ { i = 0 } ^ { N - 1 } { \frac { w _ { i } } { x - x _ { i } } } y _ { i } } { \displaystyle \sum _ { i = 0 } ^ { N - 1 } { \frac { w _ { i } } { x - x _ { i } } } } }
$$

One can show that by a suitable choice of the weights $w _ { i }$ , every rational interpolant can be written in this form, and that, as a special case, so can polynomial interpolants [3]. It turns out that this form has many nice numerical properties. Barycentric rational interpolation competes very favorably with splines: its error is often smaller, and the resulting approximation is infinitely smooth (unlike splines).

Suppose we want our rational interpolant to have approximation order $d$ , i.e., if the spacing of the points is $O ( h )$ , the error is $O ( h ^ { d + 1 } )$ as $h  0$ . Then the formula for the weights is

$$
w _ { k } = \sum _ { \stackrel { i = k - d } { 0 \leq i < N - d } } ^ { k } ( - 1 ) ^ { k } \prod _ { \stackrel { j = i } { j \neq k } } ^ { i + d } \frac { 1 } { x _ { k } - x _ { j } }
$$

For example,

$$
\begin{array} { l l } { { w _ { k } = ( - 1 ) ^ { k } , ~ } } & { { d = 0 } } \\ { { w _ { k } = ( - 1 ) ^ { k - 1 } \left[ \displaystyle \frac { 1 } { x _ { k } - x _ { k - 1 } } + \displaystyle \frac { 1 } { x _ { k + 1 } - x _ { k } } \right] , ~ } } & { { d = 1 } } \end{array}
$$

In the last equation, you omit the terms in $w _ { 0 }$ and $w _ { N - 1 }$ that refer to out-of-range values of $x _ { k }$ .

Here is a routine that implements barycentric rational interpolation. Given a set of $N$ nodes and a desired order $d$ , with $d \digamma < N$ , it first computes the weights $w _ { k }$ . Then subsequent calls to interp evaluate the interpolant using equation (3.4.9). Note that the parameter $\mathrm { j } \mathrm { 1 }$ of rawinterp is not used, since the algorithm is designed to construct an approximation on the entire interval at once.

The workload to construct the weights is of order $O ( N d )$ operations. For small $d$ , this is not too different from splines. Note, however, that the workload for each subsequent interpolated value is $O ( N )$ , not $O ( d )$ as for splines.

# struct BaryRat_interp : Base_interp

Barycentric rational interpolation object. After constructing the object, call interp for interpolated values. Note that no error estimate dy is calculated.

VecDoub w; Int d; BaryRat_interp(VecDoub_I &xv, VecDoub_I &yv, Int dd); Doub rawinterp(Int jl, Doub x); Doub interp(Doub x); ;

BaryRat_interp::BaryRat_interp(VecDoub_I &xv, VecDoub_I &yv, Int dd) : Base_interp(xv,&yv[0],xv.size()), w(n), d(dd)   
Constructor arguments are $\mathbf { x }$ and $\mathbf { y }$ vectors of length n, and order $d$ of desired approximation.   
{   
if ( $\scriptstyle \mathbf { n < = d } ,$ ) throw("d too large for number of points in BaryRat_interp");   
for (Int $\mathtt { k } = 0$ ;k<n;k++) { Compute weights from equation (3.4.10). Int imin=MAX(k-d,0); Int imax = k >= n-d ? n-d-1 : k; Doub temp $=$ imin & 1 ? -1.0 : 1.0; Doub sum $= 0 . ($ 0; for (Int $\dot { \bf 1 } =$ imin;i $\cdot { } ^ { < = }$ imax;i++) { Int jmax MIN(i+d,n-1); Doub term $^ { 1 = 1 }$ .0; for (Int $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { I } } }$ ;j $< =$ jmax;j++) { if (j $\scriptstyle = = \mathbf { k }$ ) continue; term $\ast =$ (xx[k]-xx[j]); } term $\cdot ^ { = }$ temp/term; temp $\mid =$ -temp; sum $+ =$ term; w[k] $=$ sum;   
}

Use equation (3.4.9) to compute the barycentric rational interpolant. Note that $\mathbf { j } \mathbf { 1 }$ is not used since the approximation is global; it is included only for compatibility with Base_interp.

Doub num $_ { = 0 }$ ,den ${ = } 0$ ;   
for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) { Doub $\mathbf { \hat { h } } \mathbf { = x } \mathbf { \cdot }$ -xx[i]; if $( \mathbf { h _ { \alpha } } = = \mathbf { \beta } 0 . 0 )$ ) { return yy[i]; } else { Doub temp=w[i]/h; num $+ =$ temp\*yy[i]; den $+ =$ temp; }   
  
return num/den;

Doub BaryRat_interp::interp(Doub x) {

No need to invoke hunt or locate since the interpolation is global, so override interp to simply call rawinterp directly with a dummy value of $\mathrm { j } \mathrm { 1 }$ .

return rawinterp(1,x);

# CITED REFERENCES AND FURTHER READING:

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 2 . 2 . [ 1 ]$   
Floater, M.S., and Hormann, K. ${ 2 0 0 6 + }$ , “Barycentric Rational Interpolation with No Poles and High Rates of Approximation,” at http://www.in.tu-clausthal.de/fileadmin/ homes/techreports/ifi0606hormann.pdf.[2]   
Berrut, J.-P., and Trefethen, L.N. 2004, “Barycentric Lagrange Interpolation,” SIAM Review, vol. 46, pp. 501–517.[3]   
Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 6 . 2$ .   
Cuyt, A., and Wuytack, L. 1987, Nonlinear Methods in Numerical Analysis (Amsterdam: North-Holland), Chapter 3.

# 3.5 Coefficients of the Interpolating Polynomial

Occasionally you may wish to know not the value of the interpolating polynomial that passes through a (small!) number of points, but the coefficients of that polynomial. A valid use of the coefficients might be, for example, to compute simultaneous interpolated values of the function and of several of its derivatives (see -5.1), or to convolve a segment of the tabulated function with some other function, where the moments of that other function (i.e., its convolution with powers of $x$ ) are known analytically.

Please be certain, however, that the coefficients are what you need. Generally the coefficients of the interpolating polynomial can be determined much less accurately than its value at a desired abscissa. Therefore, it is not a good idea to determine the coefficients only for use in calculating interpolating values. Values thus calculated will not pass exactly through the tabulated points, for example, while values computed by the routines in $\ S 3 . 1 - \ S 3 . 3$ will pass exactly through such points.

Also, you should not mistake the interpolating polynomial (and its coefficients) for its cousin, the best-fit polynomial through a data set. Fitting is a smoothing process, since the number of fitted coefficients is typically much less than the number of data points. Therefore, fitted coefficients can be accurately and stably determined even in the presence of statistical errors in the tabulated values. (See $\ S 1 4 . 9 .$ ) Interpolation, where the number of coefficients and number of tabulated points are equal, takes the tabulated values as perfect. If they in fact contain statistical errors, these can be magnified into oscillations of the interpolating polynomial in between the tabulated points.

As before, we take the tabulated points to be $y _ { i } \equiv y ( x _ { i } )$ . If the interpolating polynomial is written as

$$
y = c _ { 0 } + c _ { 1 } x + c _ { 2 } x ^ { 2 } + \cdots + c _ { N - 1 } x ^ { N - 1 }
$$

then the $c _ { i }$ ’s are required to satisfy the linear equation

$$
\left[ \begin{array} { c c c c c c } { 1 } & { x _ { 0 } } & { x _ { 0 } ^ { 2 } } & { \cdots } & { x _ { 0 } ^ { N - 1 } } \\ { 1 } & { x _ { 1 } } & { x _ { 1 } ^ { 2 } } & { \cdots } & { x _ { 1 } ^ { N - 1 } } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 1 } & { x _ { N - 1 } } & { x _ { N - 1 } ^ { 2 } } & { \cdots } & { x _ { N - 1 } ^ { N - 1 } } \end{array} \right] \cdot \left[ \begin{array} { c } { c _ { 0 } } \\ { c _ { 1 } } \\ { \vdots } \\ { c _ { N - 1 } } \end{array} \right] = \left[ \begin{array} { c } { y _ { 0 } } \\ { y _ { 1 } } \\ { \vdots } \\ { y _ { N - 1 } } \end{array} \right]
$$

This is a Vandermonde matrix, as described in $\ S 2 . 8$ . One could in principle solve equation (3.5.2) by standard techniques for linear equations generally (-2.3); however, the special method that was derived in $\ S 2 . 8$ is more efficient by a large factor, of order $N$ , so it is much better.

Remember that Vandermonde systems can be quite ill-conditioned. In such a case, no numerical method is going to give a very accurate answer. Such cases do not, please note, imply any difficulty in finding interpolated values by the methods of $\ S 3 . 2$ , but only difficulty in finding coefficients.

Like the routine in $\ S 2 . 8$ , the following is due to G.B. Rybicki.

# void polcoe(VecDoub_I &x, VecDoub_I &y, VecDoub_O &cof)

Given arrays $\mathbf { x } \left[ 0 \ldots \ldots \right]$ and $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ containing a tabulated function $\mathsf { y } _ { i } = f ( \mathbf { x } _ { i } )$ , this routine returns an array of coefficients cof[0..n-1], such that $\begin{array} { r } { \mathsf { y } _ { i } = \sum _ { j = 0 } ^ { n - 1 } \mathsf { c o f } _ { j } \mathsf { x } _ { i } ^ { j } } \end{array}$ .

Int k,j,i, $\mathrm { n } { = } \mathrm { x }$ .size(); Doub phi,ff,b; VecDoub s(n); for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) s[i] $=$ cof[i]=0.0; s[n-1] $=$ -x[0]; for ( $\dot { \mathbf { 1 } } = 1$ ;i<n; $\dot { 1 } + +$ ) { Coefficients $\mathsf { s } _ { i }$ of the master polynomial $P ( x )$ are for (j=n-1-i;j<n-1;j++) found by recurrence. $\begin{array} { r } { \mathbf { s } \left[ \mathrm { j } \right] \ \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { - } = \ \mathbf { x } \left[ \mathrm { i } \right] \ast \mathbf { s } \left[ \mathrm { j } + 1 \right] \mathrm { i } \left. \mathbf { \Sigma } \right. } \end{array}$ ; s[n-1] -= x[i]; } for (j=0;j<n;j++) { phi=n; for (k=n-1;k>0;k--) The quantity $\begin{array} { r } { \mathtt { p h i } = \prod _ { j \ne k } ( x _ { j } - x _ { k } ) } \end{array}$ is found as a phi=k\*s[k]+x[j]\*phi; derivative of $P ( x _ { j } )$ . ff=y[j]/phi; b=1.0; Coefficients of polynomials in each term of the Lafor (k=n-1;k> ${ = } 0$ ;k--) { grange formula are found by synthetic division of cof[k] $+ =$ b\*ff; $P ( x )$ by $( x - x _ { j } )$ . The solution $\mathtt { c } _ { k }$ is accumu-$\mathtt { b } = \mathtt { s }$ [k]+x[j]\*b; lated. } } }

# 3.5.1 Another Method

Another technique is to make use of the function value interpolation routine already given (polint; -3.2). If we interpolate (or extrapolate) to find the value of the interpolating polynomial at $x = 0$ , then this value will evidently be $c _ { 0 }$ . Now we can subtract $c _ { 0 }$ from the $y _ { i }$ ’s and divide each by its corresponding $x _ { i }$ . Throwing out one point (the one with smallest $x _ { i }$ is a good candidate), we can repeat the procedure to find $c _ { 1 }$ , and so on.

It is not instantly obvious that this procedure is stable, but we have generally found it to be somewhat more stable than the routine immediately preceding. This method is of order $N ^ { 3 }$ , while the preceding one was of order $N ^ { 2 }$ . You will find, however, that neither works very well for large $N$ , because of the intrinsic ill-condition of the Vandermonde problem. In single precision, $N$ up to 8 or 10 is satisfactory; about double this in double precision.

# void polcof(VecDoub_I &xa, VecDoub_I &ya, VecDoub_O &cof)

Given arrays $\mathtt { x a } [ 0 \ldots \mathtt { n - 1 } ]$ and ya[0..n-1] containing a tabulated function $\mathtt { y a } _ { i } = f ( \mathtt { x a } _ { i } )$ , this routine returns an array of coefficients cof $\left[ 0 \ldots \mathbf { n } \mathbf { - } 1 \right]$ , such that $\begin{array} { r } { \mathtt { y a } _ { i } = \sum _ { j = 0 } ^ { n - 1 } \mathtt { c o f } _ { j } \mathtt { x a } _ { i } ^ { j } } \end{array}$ .

Int k,j,i,n=xa.size();   
Doub xmin;   
VecDoub x(n),y(n);   
for ( $\scriptstyle \dot { \ j } = 0$ ;j<n;j++) { x[j]=xa[j]; y[j]=ya[j];   
}   
for (j=0;j<n;j++) { VecDoub x_t(n-j),y_t(n-j); for $( \mathtt { k } = 0$ ;k<n-j;k++) { x_t[k] $= \tt x$ [k]; y_t[k]=y[k]; } Poly_interp interp(x,y,n-j); cof[j] $=$ interp.rawinterp(0,0.); xmin $^ { = 1 }$ .0e99; $\texttt { k } = \texttt { - 1 }$ ; for (i=0;i<n-j;i++) { if (abs(x[i]) $<$ xmin) { xmin $\cdot ^ { = }$ abs(x[i]); k=i; } if (x[i] != 0.0) y[i] $=$ (y[i]-cof[j])/x[i]; } for (i=k+1;i<n-j;i++) { y[i-1]=y[i]; $\mathbf { x } \left[ \mathbf { i } - 1 \right] = \mathbf { x }$ [i]; }   
}

Find the remaining $\mathbf { x } _ { i }$ of smallest absolute value

(meanwhile reducing all the terms)

and eliminate it.

If the point $x \ = \ 0$ is not in (or at least close to) the range of the tabulated $x _ { i }$ ’s, then the coefficients of the interpolating polynomial will in general become very large. However, the real “information content” of the coefficients is in small differences from the “translation-induced” large values. This is one cause of illconditioning, resulting in loss of significance and poorly determined coefficients. In this case, you should consider redefining the origin of the problem, to put $x = 0$ in a sensible place.

Another pathology is that, if too high a degree of interpolation is attempted on a smooth function, the interpolating polynomial will attempt to use its high-degree coefficients, in combinations with large and almost precisely canceling combinations, to match the tabulated values down to the last possible epsilon of accuracy. This effect is the same as the intrinsic tendency of the interpolating polynomial values to oscillate (wildly) between its constrained points and would be present even if the machine’s floating precision were infinitely good. The above routines polcoe and polcof have slightly different sensitivities to the pathologies that can occur.

Are you still quite certain that using the coefficients is a good idea?

# CITED REFERENCES AND FURTHER READING:

Isaacson, E., and Keller, H.B. 1966, Analysis of Numerical Methods; reprinted 1994 (New York: Dover), $\ S 5 . 2$ .

# 3.6 Interpolation on a Grid in Multidimensions

In multidimensional interpolation, we seek an estimate of a function of more than one independent variable, $y ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ . The Great Divide is, Are we given a complete set of tabulated values on an $n$ -dimensional grid? Or, do we know function values only on some scattered set of points in the $n$ -dimensional space? In one dimension, the question never arose, because any set of $x _ { i }$ ’s, once sorted into ascending order, could be viewed as a valid one-dimensional grid (regular spacing not being a requirement).

As the number of dimensions $n$ gets large, maintaining a full grid becomes rapidly impractical, because of the explosion in the number of gridpoints. Methods that work with scattered data, to be considered in $\ S 3 . 7$ , then become the methods of choice. Don’t, however, make the mistake of thinking that such methods are intrinsically more accurate than grid methods. In general they are less accurate. Like the proverbial three-legged dog, they are remarkable because they work at all, not because they work, necessarily, well!

Both kinds of methods are practical in two dimensions, and some other kinds as well. For example, finite element methods, of which triangulation is the most common, find ways to impose some kind of geometrically regular structure on scattered points, and then use that structure for interpolation. We will treat two-dimensional interpolation by triangulation in detail in $\ S 2 1 . 6$ ; that section should be considered as a continuation of the discussion here.

In the remainder of this section, we consider only the case of interpolating on a grid, and we implement in code only the (most common) case of two dimensions. All of the methods given generalize to three dimensions in an obvious way. When we implement methods for scattered data, in $\ S 3 . 7$ , the treatment will be for general $n$ .

In two dimensions, we imagine that we are given a matrix of functional values $y _ { i j }$ , with $i = 0 , \ldots , M - 1$ and $j = 0 , \ldots , N - 1$ . We are also given an array of $x _ { 1 }$ values $x _ { 1 i }$ , and an array of $x _ { 2 }$ values $x _ { 2 j }$ , with $i$ and $j$ as just stated. The relation of these input quantities to an underlying function $y ( x _ { 1 } , x _ { 2 } )$ is just

$$
y _ { i j } = y ( x _ { 1 i } , x _ { 2 j } )
$$

We want to estimate, by interpolation, the function $y$ at some untabulated point $( x _ { 1 } , x _ { 2 } )$ .

An important concept is that of the grid square in which the point $( x _ { 1 } , x _ { 2 } )$ falls, that is, the four tabulated points that surround the desired interior point. For convenience, we will number these points from 0 to 3, counterclockwise starting from the lower left. More precisely, if

$$
\begin{array} { l } { { x _ { 1 i } \leq x _ { 1 } \leq x _ { 1 ( i + 1 ) } } } \\ { { x _ { 2 j } \leq x _ { 2 } \leq x _ { 2 ( j + 1 ) } } } \end{array}
$$

defines values of $i$ and $j$ , then

$$
\begin{array} { l } { y _ { 0 } \equiv y _ { i j } } \\ { y _ { 1 } \equiv y _ { ( i + 1 ) j } } \\ { y _ { 2 } \equiv y _ { ( i + 1 ) ( j + 1 ) } } \\ { y _ { 3 } \equiv y _ { i ( j + 1 ) } } \end{array}
$$

The simplest interpolation in two dimensions is bilinear interpolation on the grid square. Its formulas are

$$
\begin{array} { c } { t \equiv ( x _ { 1 } - x _ { 1 i } ) / ( x _ { 1 ( i + 1 ) } - x _ { 1 i } ) } \\ { u \equiv ( x _ { 2 } - x _ { 2 j } ) / ( x _ { 2 ( j + 1 ) } - x _ { 2 j } ) } \end{array}
$$

(so that $t$ and $u$ each lie between 0 and 1) and

$$
y ( x _ { 1 } , x _ { 2 } ) = ( 1 - t ) ( 1 - u ) y _ { 0 } + t ( 1 - u ) y _ { 1 } + t u y _ { 2 } + ( 1 - t ) u y _ { 3 }
$$

Bilinear interpolation is frequently “close enough for government work.” As the interpolating point wanders from grid square to grid square, the interpolated function value changes continuously. However, the gradient of the interpolated function changes discontinuously at the boundaries of each grid square.

We can easily implement an object for bilinear interpolation by grabbing pieces of “machinery” from our one-dimensional interpolation classes:

# struct Bilin_interp {

Object for bilinear interpolation on a matrix. Construct with a vector of $x _ { 1 }$ values, a vector of $x _ { 2 }$ values, and a matrix of tabulated function values $y _ { i j }$ . Then call interp for interpolated values.

Int m,n;  
const MatDoub &y;  
Linear_interp x1terp, x2terp;

Bilin_interp(VecDoub_I &x1v, VecDoub_I &x2v, MatDoub_I &ym) : m(x1v.size()), n(x2v.size()), y(ym), x1terp(x1v,x1v), x2terp(x2v,x2v) {} Construct dummy 1-dim interpolations for their locate and hunt Doub interp(Doub x1p, Doub x2p) { functions. Int i,j; Doub yy, t, u; $\begin{array} { r l } { \dot { \mathbf { 1 } } } & { { } = } \end{array}$ x1terp.cor ? x1terp.hunt(x1p) : x1terp.locate(x1p); ${ \dot { \textbf { j } } } =$ x2terp.cor ? x2terp.hunt(x2p) : x2terp.locate(x2p); Find the grid square. $\begin{array} { r l } { \mathbf { \epsilon } _ { \mathbf { { t } } } } & { { } = } \end{array}$ (x1p-x1terp.xx[i])/(x1terp.xx[i+1]-x1terp.xx[i]); Interpolate. $\mathrm { ~ \textbar ~ { ~ u ~ } ~ } =$ (x2p-x2terp.xx[j])/(x2terp.xx[j+1]-x2terp.xx[j]); yy = (1.-t)\*(1.-u)\*y[i][j] $^ +$ t\*(1.-u)\*y[i+1][j] + (1.-t)\*u\*y[i][j+1] $^ +$ t\*u\*y[i+1][j+1]; return yy; } };

Here we declare two instances of Linear_interp, one for each direction, and use them merely to do the bookkeeping on the arrays $x _ { 1 i }$ and $x _ { 2 _ { j } }$ — in particular, to provide the “intelligent” table-searching mechanisms that we have come to rely on. (The second occurrence of $\tt { x 1 v }$ and $\tt { x 2 v }$ in the constructors is just a placeholder; there are not really any one-dimensional “y” arrays.)

Usage of Bilin_interp is just what you’d expect:

Int $\mathrm { m } = .$ .. $\mathbf { n } =$ ..   
MatDoub yy(m,n);   
VecDoub x1(m), x2(n);   
Bilin_interp myfunc(x1,x2,yy);

followed (any number of times) by

Doub x1,x2,y;   
$\mathrm { ~ y ~ } =$ myfunc.interp(x1,x2);

Bilinear interpolation is a good place to start, in two dimensions, unless you positively know that you need something fancier.

There are two distinctly different directions that one can take in going beyond bilinear interpolation to higher-order methods: One can use higher order to obtain increased accuracy for the interpolated function (for sufficiently smooth functions!), without necessarily trying to fix up the continuity of the gradient and higher derivatives. Or, one can make use of higher order to enforce smoothness of some of these derivatives as the interpolating point crosses grid-square boundaries. We will now consider each of these two directions in turn.

# 3.6.1 Higher Order for Accuracy

The basic idea is to break up the problem into a succession of one-dimensional interpolations. If we want to do $\mathtt { m } - 1$ order interpolation in the $x _ { 1 }$ direction, and $\mathtt { n - 1 }$ order in the $x _ { 2 }$ direction, we first locate an $m \times n$ sub-block of the tabulated function matrix that contains our desired point $( x _ { 1 } , x _ { 2 } )$ . We then do m one-dimensional interpolations in the $x _ { 2 }$ direction, i.e., on the rows of the sub-block, to get function values at the points $( x _ { 1 i } , x _ { 2 } )$ , with $m$ values of $i$ . Finally, we do a last interpolation in the $x _ { 1 }$ direction to get the answer.

Again using the previous one-dimensional machinery, this can all be coded very concisely as

# struct Poly2D_interp {

Object for two-dimensional polynomial interpolation on a matrix. Construct with a vector of $x _ { 1 }$ values, a vector of $x _ { 2 }$ values, a matrix of tabulated function values $y _ { i j }$ , and integers to specify the number of points to use locally in each direction. Then call interp for interpolated values.

Int m,n,mm,nn; const MatDoub &y; VecDoub yv; Poly_interp x1terp, x2terp; Poly2D_interp(VecDoub_I &x1v, VecDoub_I &x2v, MatDoub_I &ym, Int mp, Int np) : m(x1v.size()), n(x2v.size()), mm(mp), nn(np), y(ym), yv(m), x1terp(x1v,yv,mm), x2terp(x2v,x2v,nn) {} Dummy 1-dim interpolations for their locate and hunt functions. Doub interp(Doub x1p, Doub x2p) { Int i,j,k; $\begin{array} { r l } { \dot { \bf \lambda } _ { 1 } } & { { } = } \end{array}$ x1terp.cor ? x1terp.hunt(x1p) : x1terp.locate(x1p); ${ \dot { \mathrm { ~  ~ j ~ } } } =$ x2terp.cor ? x2terp.hunt(x2p) : x2terp.locate(x2p); Find grid block. for $( \Bbbk { = } \dot$ ;k<i+mm;k++) { mm interpolations in the $x _ { 2 }$ direction. x2terp.yy $=$ &y[k][0]; yv[k] $=$ x2terp.rawinterp(j,x2p); } return x1terp.rawinterp(i,x1p); A final interpolation in the $x _ { 1 }$ direc-} tion. };

The user interface is the same as for Bilin_interp, except that the constructor has two additional arguments that specify the number of points (order plus one) to be used locally in, respectively, the $x _ { 1 }$ and $x _ { 2 }$ interpolations. Typical values will be in the range 3 to 7.

Code stylists won’t like some of the details in Poly2D_interp (see discussion in $\ S 3 . 1$ immediately following Base_interp). As we loop over the rows of the sub-block, we reach into the guts of x2terp and repoint its yy array to a row of our $y$ matrix. Further, we alter the contents of the array yv, for which x1terp has stored a pointer, on the fly. None of this is particularly dangerous as long as we control the implementations in both Base_interp and Poly2D_interp; and it makes for a very efficient implementation. You should view these two classes as not just (implicitly) friend classes, but as really intimate friends.

# 3.6.2 Higher Order for Smoothness: Bicubic Spline

A favorite technique for obtaining smoothness in two-dimensional interpolation is the bicubic spline. To set up a bicubic spline, you (one time) construct $M$ one-dimensional splines across the rows of the two-dimensional matrix of function values. Then, for each desired interpolated value you proceed as follows: (1) Perform $M$ spline interpolations to get a vector of values $y ( x _ { 1 i } , x _ { 2 } )$ , $i = 0 , \ldots , M - 1$ . (2) Construct a one-dimensional spline through those values. (3) Finally, splineinterpolate to the desired value $y ( x _ { 1 } , x _ { 2 } )$ .

If this sounds like a lot of work, well, yes, it is. The one-time setup work scales as the table size $M \times N$ , while the work per interpolated value scales roughly as $M \log M + N$ , both with pretty hefty constants in front. This is the price that you pay for the desirable characteristics of splines that derive from their nonlocality. For tables with modest $M$ and $N$ , less than a few hundred, say, the cost is usually tolerable. If it’s not, then fall back to the previous local methods.

Again a very concise implementation is possible:

# struct Spline2D_interp {

Object for two-dimensional cubic spline interpolation on a matrix. Construct with a vector of $x _ { 1 }$ values, a vector of $x _ { 2 }$ values, and a matrix of tabulated function values $y _ { i j }$ . Then call interp for interpolated values.

Int m,n; const MatDoub &y; const VecDoub &x1; VecDoub yv; NRvector<Spline_interp\*> srp; Spline2D_interp(VecDoub_I &x1v, VecDoub_I &x2v, MatDoub_I &ym) : m(x1v.size()), n(x2v.size()), y(ym), yv(m), x1(x1v), srp(m) { for (Int $\scriptstyle \dot { 1 } = 0$ ;i<m;i++) srp[i] $=$ new Spline_interp(x2v,&y[i][0]); Save an array of pointers to 1-dim row splines. } \~Spline2D_interp(){ for (Int $\scriptstyle \dot { 1 } = 0$ ;i<m;i++) delete srp[i]; We need a destructor to clean up. } Doub interp(Doub x1p, Doub x2p) { for (Int $\scriptstyle \dot { 1 } = 0$ ;i<m; $\lfloor + +$ ) yv[i] $=$ (\*srp[i]).interp(x2p); Interpolate on each row. Spline_interp scol(x1,yv); Construct the column spline, return scol.interp(x1p); and evaluate it. } };

The reason for that ugly vector of pointers to Spline_interp objects is that we need to initialize each row spline separately, with data from the appropriate row. The user interface is the same as Bilin_interp, above.

![](images/21ffb3f36620e71067758979f88a8786f6dce3aec5d443f16813bd421c0241c3.jpg)  
Figure 3.6.1. (a) Labeling of points used in the two-dimensional interpolation routines bcuint and bcucof. (b) For each of the four points in (a), the user supplies one function value, two first derivatives, and one cross-derivative, a total of 16 numbers.

# 3.6.3 Higher Order for Smoothness: Bicubic Interpolation

Bicubic interpolation gives the same degree of smoothness as bicubic spline interpolation, but it has the advantage of being a local method. Thus, after you set it up, a function interpolation costs only a constant, plus $\log M + \log N$ , to find your place in the table. Unfortunately, this advantage comes with a lot of complexity in coding. Here, we will give only some building blocks for the method, not a complete user interface.

Bicubic splines are in fact a special case of bicubic interpolation. In the general case, however, we leave the values of all derivatives at the grid points as freely specifiable. You, the user, can specify them any way you want. In other words, you specify at each grid point not just the function $y ( x _ { 1 } , x _ { 2 } )$ , but also the gradients $\partial y / \partial x _ { 1 } \ \equiv \ y _ { , 1 }$ , $\partial y / \partial x _ { 2 } \equiv y _ { , 2 }$ and the cross derivative $\partial ^ { 2 } y / \partial x _ { 1 } \partial x _ { 2 } \ \equiv \ y , _ { 1 2 }$ (see Figure 3.6.1). Then an interpolating function that is cubic in the scaled coordinates $t$ and $u$ (equation 3.6.4) can be found, with the following properties: (i) The values of the function and the specified derivatives are reproduced exactly on the grid points, and (ii) the values of the function and the specified derivatives change continuously as the interpolating point crosses from one grid square to another.

It is important to understand that nothing in the equations of bicubic interpolation requires you to specify the extra derivatives correctly! The smoothness properties are tautologically “forced,” and have nothing to do with the “accuracy” of the specified derivatives. It is a separate problem for you to decide how to obtain the values that are specified. The better you do, the more accurate the interpolation will be. But it will be smooth no matter what you do.

Best of all is to know the derivatives analytically, or to be able to compute them accurately by numerical means, at the grid points. Next best is to determine them by numerical differencing from the functional values already tabulated on the grid. The relevant code would be something like this (using centered differencing):

y1a[j][k] $=$ (ya[j $+ 1 ]$ [k]-ya[j-1][k])/(x1a[j+1]-x1a[j-1]); y2a[j][k] $=$ (ya[j][k+1]-ya[j][k-1])/(x2a[k+1]-x2a[k-1]); y12a[j][k] $=$ (ya[j $+ 1 ]$ [k+1]-ya[j+1][k-1]-ya[j-1][k+1]+ya[j-1][k-1]) /((x1a[j+1]-x1a[j-1])\*(x2a[k+1]-x2a[k-1]));

To do a bicubic interpolation within a grid square, given the function y and the derivatives y1, y2, y12 at each of the four corners of the square, there are two steps: First obtain the 16 quantities $c _ { i j }$ ; $i , j = 0 , \ldots , 3$ using the routine bcucof below. (The formulas that obtain the $c$ ’s from the function and derivative values are just a complicated linear transformation, with coefficients that, having been determined once in the mists of numerical history, can be tabulated and forgotten.) Next, substitute the $c$ ’s into any or all of the following bicubic formulas for function and derivatives, as desired:

$$
\begin{array} { l } { \displaystyle y ( x _ { 1 } , x _ { 2 } ) = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } c _ { i j } t ^ { i } u ^ { j } } \\ { \displaystyle y _ { , 1 } ( x _ { 1 } , x _ { 2 } ) = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } i c _ { i j } t ^ { i - 1 } u ^ { j } \left( d t / d x _ { 1 } \right) } \\ { \displaystyle y _ { , 2 } ( x _ { 1 } , x _ { 2 } ) = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } j c _ { i j } t ^ { i } u ^ { j - 1 } \left( d u / d x _ { 2 } \right) } \\ { \displaystyle y _ { , 1 2 } ( x _ { 1 } , x _ { 2 } ) = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } i j c _ { i j } t ^ { i - 1 } u ^ { j - 1 } \left( d u / d x _ { 1 } \right) \left( d u / d x _ { 2 } \right) } \end{array}
$$

where $t$ and $u$ are again given by equation (3.6.4).

void bcucof(VecDoub_I &y, VecDoub_I &y1, VecDoub_I &y2, VecDoub_I &y12,const Doub d1, const Doub d2, MatDoub_O &c) {

Given arrays y[0..3], y1[0..3], y2[0..3], and y12[0..3], containing the function, gradients, and cross-derivative at the four grid points of a rectangular grid cell (numbered counterclockwise from the lower left), and given d1 and d2, the length of the grid cell in the 1 and 2 directions, this routine returns the table c[0..3][0..3] that is used by routine bcuint for bicubic interpolation.

static Int wt_d[16\*16] $=$ {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 3, 0, 0, 0, 0,-2, 0, 0,-1, 0, 0, 0, 0, 2, 0, 0,-2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,-3, 0, 0, 3, 0, 0, 0, 0,-2, 0, 0,-1, 0, 0, 0, 0, 2, 0, 0,-2, 0, 0, 0, 0, 1, 0, 0, 1, -3, 3, 0, 0,-2,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-3, 3, 0, 0,-2,-1, 0, 0, 9,-9, 9,-9, 6, 3,-3,-6, 6,-6,-3, 3, 4, 2, 1, 2, -6, 6,-6, 6,-4,-2, 2, 4,-3, 3, 3,-3,-2,-1,-1,-2, 2,-2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,-2, 0, 0, 1, 1, 0, 0, -6, 6,-6, 6,-3,-3, 3, 3,-4, 4, 2,-2,-2,-2,-1,-1, 4,-4, 4,-4, 2, 2,-2,-2, 2,-2,-2, 2, 1, 1, 1, 1};   
Int l,k,j,i;   
Doub xx,d1d2=d1\*d2;   
VecDoub cl(16),x(16);   
static MatInt wt(16,16,wt_d);   
for (i=0;i<4;i++) { Pack a temporary vector x. x[i]=y[i]; x[i+4]=y1[i]\*d1; x[i+8]=y2[i]\*d2; x[i+12]=y12[i]\*d1d2;   
  
for (i=0;i<16;i++) { Matrix-multiply by the stored table. $\mathtt { x x } { = } 0 . 0$ ; for (k=0;k<16;k++) xx += wt[i][k]\*x[k]; cl[i] $= \tt x x$ ;   
}   
$\mathtt { 1 } = 0$ ;   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<4;i++) Unpack the result into the output table for (j ${ = } 0$ ;j<4;j++) c[i][j]=cl[l++];

The implementation of equation (3.6.6), which performs a bicubic interpolation, gives back the interpolated function value and the two gradient values, and uses the above routine bcucof, is simply:

void bcuint(VecDoub_I &y, VecDoub_I &y1, VecDoub_I &y2, VecDoub_I &y12, const Doub x1l, const Doub x1u, const Doub x2l, const Doub x2u, const Doub x1, const Doub x2, Doub &ansy, Doub &ansy1, Doub &ansy2) {   
Bicubic interpolation within a grid square. Input quantities are y,y1,y2,y12 (as described in   
bcucof); $\tt x 1 1$ and x1u, the lower and upper coordinates of the grid square in the 1 direction;   
$\tt x 2 1$ and x2u likewise for the 2 direction; and $\mathbf { x } \mathbf { 1 } , \mathbf { x } 2$ , the coordinates of the desired point for   
the interpolation. The interpolated function value is returned as ansy, and the interpolated   
gradient values as ansy1 and ansy2. This routine calls bcucof.   
Int i;   
Doub t,u,d1=x1u-x1l,d2=x2u-x2l;   
MatDoub c(4,4);   
bcucof(y,y1,y2,y12,d1,d2,c); Get the c’s.   
if $( \mathrm { x 1 u ~ } = = \mathrm { ~ \ x 1 1 ~ }$ || x $\ Q \ \mathbf { u } \ = \ \mathbf { x } 2 1 .$ ) throw("Bad input in routine bcuint");   
$\mathtt { t = }$ (x1-x1l)/d1; Equation (3.6.4).   
$\mathrm { u } =$ (x2-x2l)/d2;   
ansy=ansy2=ansy $\scriptstyle 1 = 0$ .0;   
for ( $\dot { 1 } = 3$ ; $\therefore 2 = 0$ ;i--) { Equation (3.6.6). ansy=t\*ansy+((c[i][3]\*u+c[i][2])\*u+c[i][1])\*u+c[i][0]; ansy2 $\Bumpeq$ t\*ansy2+(3.0\*c[i][3] $\ast \mathtt { u } + 2$ .0\*c[i][2])\*u+c[i][1]; ansy1=u\*ansy1+(3.0\*c[3][i]\*t+2.0\*c[2][i])\*t+c[1][i];   
ansy1 $/ =$ d1;   
ansy2 $/ =$ d2;

You can combine the best features of bicubic interpolation and bicubic splines by using splines to compute values for the necessary derivatives at the grid points, storing these values, and then using bicubic interpolation, with an efficient tablesearching method, for the actual function interpolations. Unfortunately this is beyond our scope here.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 2 5 . 2$ .

Kinahan, B.F., and Harm, R. 1975, “Chemical Composition and the Hertzsprung Gap,” Astrophysical Journal, vol. 200,pp. 330-335.

Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), $\ S 5 . 2 . 7$ .   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 7 . 7$ .

# 3.7 Interpolation on Scattered Data in Multidimensions

We now leave behind, if with some trepidation, the orderly world of regular grids. Courage is required. We are given an arbitrarily scattered set of $N$ data points $( { \bf x } _ { i } , y _ { i } ) , i = 0 , \dots , N - 1$ in $n$ -dimensional space. Here $\mathbf { X } _ { i }$ denotes an $n$ -dimensional vector of independent variables, $( x _ { 1 i } , x _ { 2 i } , \dots , x _ { n i } )$ , and $y _ { i }$ is the value of the function at that point.

In this section we discuss two of the most widely used general methods for this problem, radial basis function $( R B F )$ interpolation, and kriging. Both of these methods are expensive. By that we mean that they require $O ( N ^ { 3 } )$ operations to initially digest a set of data points, followed by $O ( N )$ operations for each interpolated value. Kriging is also able to supply an error estimate — but at the rather high cost of $O ( N ^ { 2 } )$ per value. Shepard interpolation, discussed below, is a variant of RBF that at least avoids the $O ( N ^ { 3 } )$ initial work; otherwise these workloads effectively limit the usefulness of these general methods to values of $N \lesssim 1 0 ^ { 4 }$ . It is therefore worthwhile for you to consider whether you have any other options. Two of these are

- If $n$ is not too large (meaning, usually, $n = 2$ ), and if the data points are fairly dense, then consider triangulation, discussed in $\ S 2 1 . 6$ . Triangulation is an example of a finite element method. Such methods construct some semblance of geometric regularity and then exploit that construction to advantage. Mesh generation is a closely related subject.   
- If your accuracy goals will tolerate it, consider moving each data point to the nearest point on a regular Cartesian grid and then using Laplace interpolation (-3.8) to fill in the rest of the grid points. After that, you can interpolate on the grid by the methods of $\ S 3 . 6$ . You will need to compromise between making the grid very fine (to minimize the error introduced when you move the points) and the compute time workload of the Laplace method.

If neither of these options seem attractive, and you can’t think of another one that is, then try one or both of the two methods that we now discuss. RBF interpolation is probably the more widely used of the two, but kriging is our personal favorite. Which works better will depend on the details of your problem.

The related, but easier, problem of curve interpolation in multidimensions is discussed at the end of this section.

# 3.7.1 Radial Basis Function Interpolation

The idea behind RBF interpolation is very simple: Imagine that every known point $j$ “influences” its surroundings the same way in all directions, according to some assumed functional form $\phi ( r )$ — the radial basis function — that is a function only of radial distance $r = | { \bf x } - { \bf x } _ { j } |$ from the point. Let us try to approximate the interpolating function everywhere by a linear combination of the $\phi$ ’s, centered on all the known points,

$$
y ( \mathbf { x } ) = \sum _ { i = 0 } ^ { N - 1 } w _ { i } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | )
$$

where the $w _ { i }$ ’s are some unknown set of weights. How do we find these weights? Well, we haven’t used the function values $y _ { i }$ yet. The weights are determined by requiring that the interpolation be exact at all the known data points. That is equivalent to solving a set of $N$ linear equations in $N$ unknowns for the $w _ { i }$ ’s:

$$
y _ { j } = \sum _ { i = 0 } ^ { N - 1 } w _ { i } \phi ( | \mathbf { x } _ { j } - \mathbf { x } _ { i } | )
$$

For many functional forms $\phi$ , it can be proved, under various general assumptions, that this set of equations is nondegenerate and can be readily solved by, e.g., $L U$ decomposition $( \ S 2 . 3 )$ . References [1,2] provide entry to the literature.

A variant on RBF interpolation is normalized radial basis function (NRBF) interpolation, in which we require the sum of the basis functions to be unity or, equivalently, replace equations (3.7.1) and (3.7.2) by

$$
y ( \mathbf { x } ) = \frac { \sum _ { i = 0 } ^ { N - 1 } w _ { i } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | ) } { \sum _ { i = 0 } ^ { N - 1 } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | ) }
$$

and

$$
y _ { j } \sum _ { i = 0 } ^ { N - 1 } \phi ( | \mathbf { x } _ { j } - \mathbf { x } _ { i } | ) = \sum _ { i = 0 } ^ { N - 1 } w _ { i } \phi ( | \mathbf { x } _ { j } - \mathbf { x } _ { i } | )
$$

Equations (3.7.3) and (3.7.4) arise more naturally from a Bayesian statistical perspective [3]. However, there is no evidence that either the NRBF method is consistently superior to the RBF method, or vice versa. It is easy to implement both methods in the same code, leaving the choice to the user.

As we already mentioned, for $N$ data points the one-time work to solve for the weights by $L U$ decomposition is $O ( N ^ { 3 } )$ . After that, the cost is $O ( N )$ for each interpolation. Thus $N \sim 1 0 ^ { 3 }$ is a rough dividing line (at 2007 desktop speeds) between “easy” and “difficult.” If your $N$ is larger, however, don’t despair: There are fast multipole methods, beyond our scope here, with much more favorable scaling [1,4,5]. Another, much lower-tech, option is to use Shepard interpolation discussed later in this section.

Here are a couple of objects that implement everything discussed thus far. RBF_fn is a virtual base class whose derived classes will embody different functional forms for $\mathtt { r b f } ( r ) \equiv \phi ( r )$ . RBF_interp, via its constructor, digests your data and solves the equations for the weights. The data points $\mathbf { X } _ { i }$ are input as an $N \times n$ matrix, and the code works for any dimension $n$ . A boolean argument nrbf inputs whether NRBF is to be used instead of RBF. You call interp to get an interpolated function value at a new point $\mathbf { X }$ .

# struct RBF_fn {

Abstract base class template for any particular radial basis function. See specific examples below.

virtual Doub rbf(Doub $\mathbf { \boldsymbol { r } } ) \ = \ \mathbf { \boldsymbol { 0 } } ;$ };

struct RBF_interp {   
Object for radial basis function interpolation using n points in dim dimensions. Call constructor once, then interp as many times as desired. Int dim, n;   
const MatDoub &pts;   
const VecDoub &vals;   
VecDoub w;   
RBF_fn &fn;   
Bool norm;

RBF_interp(MatDoub_I &ptss, VecDoub_I &valss, RBF_fn &func, Bool nrbf $=$ false) : dim(ptss.ncols()), n(ptss.nrows()) , pts(ptss), vals(valss), $\ l { w } ( { \mathrm { n } } )$ , fn(func), norm(nrbf) {

Constructor. The $\textbf { n } \times$ dim matrix ptss inputs the data points, the vector valss the function values. func contains the chosen radial basis function, derived from the class RBF_fn. The default value of nrbf gives RBF interpolation; set it to 1 for NRBF.

Int i,j;   
Doub sum;   
MatDoub rbf ${ ( \mathtt { n } , \mathtt { n } ) }$ ;   
VecDoub rhs(n);   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n; $\mathbf { i } + +$ ) { Fill the matrix $\phi ( | { \bf r } _ { i } - { \bf r } _ { j } | )$ and the r.h.s. vector. sum $\qquad = \ 0 .$ .; for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n;j++) { sum $+ =$ (rbf[i][j] $=$ fn.rbf(rad(&pts[i][0],&pts[j][0]))); } if (norm) rhs[i] $=$ sum\*vals[i]; else rhs[i] $=$ vals[i];   
}   
LUdcmp lu(rbf); Solve the set of linear equations.   
lu.solve(rhs,w);

# }

# Doub interp(VecDoub_I &pt) {

Return the interpolated function value at a dim-dimensional point pt.

Doub fval, sum $_ { = 0 }$ ., sumw ${ \tt = } 0$ .; if (pt.size() $! =$ dim) throw("RBF_interp bad pt size"); for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n; $\mathbf { i } + +$ ) { Sum over all tabulated points. fval $=$ fn.rbf(rad(&pt[0],&pts[i][0])); sumw $+ =$ w[i]\*fval; sum $+ =$ fval; } return norm ? sumw/sum : sumw; }

#

Doub rad(const Doub \*p1, const Doub \*p2) { Euclidean distance. Doub sum $\qquad = \ 0$ .; for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<dim; $\dot { 1 } + + \dot { 1 }$ ) sum $+ =$ SQR(p1[i]-p2[i]); return sqrt(sum); } };

# 3.7.2 Radial Basis Functions in General Use

The most often used radial basis function is the multiquadric first used by Hardy, circa 1970. The functional form is

$$
\phi ( r ) = ( r ^ { 2 } + r _ { 0 } ^ { 2 } ) ^ { 1 / 2 }
$$

where $r _ { 0 }$ is a scale factor that you get to choose. Multiquadrics are said to be less sensitive to the choice of $r _ { 0 }$ than some other functional forms.

In general, both for multiquadrics and for other functions, below, $r _ { 0 }$ should be larger than the typical separation of points but smaller than the “outer scale” or feature size of the function that you are interpolating. There can be several orders of magnitude difference between the interpolation accuracy with a good choice for $r _ { 0 }$ , versus a poor choice, so it is definitely worth some experimentation. One way to experiment is to construct an RBF interpolator omitting one data point at a time and measuring the interpolation error at the omitted point.

The inverse multiquadric

$$
\phi ( r ) = ( r ^ { 2 } + r _ { 0 } ^ { 2 } ) ^ { - 1 / 2 }
$$

gives results that are comparable to the multiquadric, sometimes better.

It might seem odd that a function and its inverse (actually, reciprocal) work about equally well. The explanation is that what really matters is smoothness, and certain properties of the function’s Fourier transform that are not very different between the multiquadric and its reciprocal. The fact that one increases monotonically and the other decreases turns out to be almost irrelevant. However, if you want the extrapolated function to go to zero far from all the data (where an accurate value is impossible anyway), then the inverse multiquadric is a good choice.

The thin-plate spline radial basis function is

$$
\phi ( r ) = r ^ { 2 } \log ( r / r _ { 0 } )
$$

with the limiting value $\phi ( 0 ) = 0$ assumed. This function has some physical justification in the energy minimization problem associated with warping a thin elastic plate. There is no indication that it is generally better than either of the above forms, however.

The Gaussian radial basis function is just what you’d expect,

$$
\begin{array} { r } { \phi ( r ) = \exp \left( - \frac { 1 } { 2 } r ^ { 2 } / r _ { 0 } ^ { 2 } \right) } \end{array}
$$

The interpolation accuracy using Gaussian basis functions can be very sensitive to $r _ { 0 }$ , and they are often avoided for this reason. However, for smooth functions and with an optimal $r _ { 0 }$ , very high accuracy can be achieved. The Gaussian also will extrapolate any function to zero far from the data, and it gets to zero quickly.

Other functions are also in use, for example those of Wendland [6]. There is a large literature in which the above choices for basis functions are tested against specific functional forms or experimental data sets [1,2,7]. Few, if any, general recommendations emerge. We suggest that you try the alternatives in the order listed above, starting with multiquadrics, and that you not omit experimenting with different choices of the scale parameters $r _ { 0 }$ .

The functions discussed are implemented in code as:

struct RBF_multiquadric : RBF_fn {   
Instantiate this and send to RBF_interp to get multiquadric interpolation. Doub r02; RBF_multiquadric(Doub scale $^ { = 1 }$ .) : r02(SQR(scale)) {} Constructor argument is the scale factor. See text. Doub rbf(Doub r) { return sqrt(SQR(r) $+ \tt r 0 2$ ); }   
};

struct RBF_thinplate : RBF_fn { Same as above, but for thin-plate spline.

Doub r0; RBF_thinplate(Doub scal $\mathtt { e } = 1$ .) : r0(scale) {} Doub rbf(Doub r) { return $x \ < = \ 0$ . ? 0. : SQR(r)\*log(r/r0); } ;

struct RBF_gauss : RBF_fn {   
Same as above, but for Gaussian. Doub r0; RBF_gauss(Doub scale $\ B = 1$ .) : r0(scale) {} Doub rbf(Doub r) { return exp(-0.5\*SQR(r/r0)); }   
};   
struct RBF_inversemultiquadric : RBF_fn {   
Same as above, but for inverse multiquadric. Doub r02; RBF_inversemultiquadric(Doub scale $^ { \prime = 1 }$ .) : r02(SQR(scale)) {} Doub rbf(Doub r) { return 1./sqrt(SQR(r)+r02); }   
};

Typical use of the objects in this section should look something like this:

Int npts $=$ ...,ndim=...;   
Doub r0=...;   
MatDoub pts(npts,ndim);   
VecDoub y(npts);   
RBF_multiquadric multiquadric(r0);   
RBF_interp myfunc(pts,y,multiquadric,0);

followed by any number of interpolation calls,

VecDoub pt(ndim);   
Doub val;   
val $=$ myfunc.interp(pt);

# 3.7.3 Shepard Interpolation

An interesting special case of normalized radial basis function interpolation (equations 3.7.3 and 3.7.4) occurs if the function $\phi ( r )$ goes to infinity as $r  0$ , and is finite (e.g., decreasing) for $r > 0$ . In that case it is easy to see that the weights $w _ { i }$ are just equal to the respective function values $y _ { i }$ , and the interpolation formula is simply

$$
y ( \mathbf { x } ) = \frac { \sum _ { i = 0 } ^ { N - 1 } y _ { i } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | ) } { \sum _ { i = 0 } ^ { N - 1 } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | ) }
$$

(with appropriate provision for the limiting case where $\mathbf { X }$ is equal to one of the $\mathbf { X } _ { i }$ ’s). Note that no solution of linear equations is required. The one-time work is negligible, while the work for each interpolation is $O ( N )$ , tolerable even for very large $N$ .

Shepard proposed the simple power-law function

$$
\phi ( r ) = r ^ { - p }
$$

with (typically) $1 < p \lesssim 3$ , as well as some more complicated functions with different exponents in an inner and outer region (see [8]). You can see that what is going on is basically interpolation by a nearness-weighted average, with nearby points contributing more strongly than distant ones.

Shepard interpolation is rarely as accurate as the well-tuned application of one of the other radial basis functions, above. On the other hand, it is simple, fast, and often just the thing for quick and dirty applications. It, and variants, are thus widely used.

An implementing object is

# struct Shep_interp {

Object for Shepard interpolation using n points in dim dimensions. Call constructor once, then interp as many times as desired.

Int dim, n;   
const MatDoub &pts;   
const VecDoub &vals;   
Doub pneg;

Shep_interp(MatDoub_I &ptss, VecDoub_I &valss, Doub $\scriptstyle \mathrm { p } = 2 .$ ) : dim(ptss.ncols()), n(ptss.nrows()) , pts(ptss), vals(valss), pneg $( - \tt p )$ {}

Constructor. The $\textbf { n } \times$ dim matrix ptss inputs the data points, the vector valss the function values. Set p to the desired exponent. The default value is typical.

Doub interp(VecDoub_I &pt) {

Return the interpolated function value at a dim-dimensional point pt. Doub r, w, sum $_ { 1 = 0 }$ ., sumw $\mathtt { \mathtt { \mathtt { = 0 } } }$ .; if (pt.size() $\ ! =$ dim) throw("RBF_interp bad pt size"); for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) { if ( $\scriptstyle x =$ rad(&pt[0],&pts[i][0])) $\mathrm { = } \mathrm { = } \ 0 .$ ) return vals[i]; sum $+ =$ ( ${ \textbf { \boldsymbol { w } } } =$ pow(r,pneg)); sumw $+ =$ w\*vals[i]; } return sumw/sum;   
}

Doub rad(const Doub \*p1, const Doub \*p2) { Euclidean distance. Doub sum $\qquad = \ 0 .$ .; for (Int i=0;i<dim; $\dot { 1 } + +$ ) sum $+ =$ SQR(p1[i]-p2[i]); return sqrt(sum); } };

# 3.7.4 Interpolation by Kriging

Kriging is a technique named for South African mining engineer D.G. Krige. It is basically a form of linear prediction (-13.6), also known in different communities as Gauss-Markov estimation or Gaussian process regression.

Kriging can be either an interpolation method or a fitting method. The distinction between the two is whether the fitted/interpolated function goes exactly through all the input data points (interpolation), or whether it allows measurement errors to be specified and then “smooths” to get a statistically better predictor that does not generally go through the data points (does not “honor the data”). In this section we consider only the former case, that is, interpolation. We will return to the latter case in $\ S 1 5 . 9$ .

At this point in the book, it is beyond our scope to derive the equations for kriging. You can turn to $\ S 1 3 . 6$ to get a flavor, and look to references [9,10,11] for details. To use kriging, you must be able to estimate the mean square variation of your function $y ( \mathbf { x } )$ as a function of offset distance r, a so-called variogram,

$$
\begin{array} { r } { v ( \mathbf { r } ) \sim \frac { 1 } { 2 } \left. \left[ y ( \mathbf { x } + \mathbf { r } ) - y ( \mathbf { x } ) \right] ^ { 2 } \right. } \end{array}
$$

where the average is over all $\mathbf { X }$ with fixed $\mathbf { r }$ . If this seems daunting, don’t worry. For interpolation, even very crude variogram estimates work fine, and we will give below a routine to estimate $v ( \mathbf { r } )$ from your input data points $\mathbf { X } _ { i }$ and $y _ { i } = y ( \mathbf { x } _ { i } )$ , $i = 0 , \ldots , N - 1$ , automatically. One usually takes $v ( \mathbf { r } )$ to be a function only of the magnitude $r = \left| \mathbf { r } \right|$ and writes it as $v ( r )$ .

Let $v _ { i j }$ denote $v ( | \mathbf { x } _ { i } - \mathbf { x } _ { j } | )$ , where $i$ and $j$ are input points, and let $v _ { * j }$ denote $v ( | \mathbf { x } _ { * } - \mathbf { x } _ { j } | )$ , $\mathbf { X } *$ being a point at which we want an interpolated value $y ( \mathbf { x } _ { * } )$ . Now define two vectors of length $N + 1$ ,

$$
\begin{array} { c } { { { \bf Y } = ( y _ { 0 } , y _ { 1 } , \dots , y _ { N - 1 } , 0 ) } } \\ { { { \bf V } _ { * } = ( v _ { * 1 } , v _ { * 2 } , \dots , v _ { * , N - 1 } , 1 ) } } \end{array}
$$

and an $( N + 1 ) \times ( N + 1 )$ symmetric matrix,

$$
\mathbf { V } = \left( \begin{array} { c c c c c } { v _ { 0 0 } } & { v _ { 0 1 } } & { \hdots } & { v _ { 0 , N - 1 } } & { 1 } \\ { v _ { 1 0 } } & { v _ { 1 1 } } & { \hdots } & { v _ { 1 , N - 1 } } & { 1 } \\ & & { \hdots } & & { \hdots } \\ { v _ { N - 1 , 0 } } & { v _ { N - 1 , 1 } } & { \hdots } & { v _ { N - 1 , N - 1 } } & { 1 } \\ { 1 } & { 1 } & { \hdots } & { 1 } & { 0 } \end{array} \right)
$$

Then the kriging interpolation estimate $\widehat { y } _ { * } \approx y ( \mathbf { x } _ { * } )$ is given by

$$
\widehat { y } _ { * } = \mathbf { V } _ { * } \cdot \mathbf { V } ^ { - 1 } \cdot \mathbf { Y }
$$

and its variance is given by

$$
\operatorname { V a r } ( \widehat { y } _ { * } ) = \mathbf { V } _ { * } \cdot \mathbf { V } ^ { - 1 } \cdot \mathbf { V } _ { * }
$$

Notice that if we compute, once, the $L U$ decomposition of $\mathbf { V }$ , and then backsubstitute, once, to get the vector $\mathbf { V } ^ { - 1 } \cdot \mathbf { Y }$ , then the individual interpolations cost only $O ( N )$ : Compute the vector $\mathbf { V } _ { * }$ and take a vector dot product. On the other hand, every computation of a variance, equation (3.7.15), requires an $O ( N ^ { 2 } )$ backsubstitution.

As an aside (if you have looked ahead to $\ S 1 3 . 6 )$ the purpose of the extra row and column in $\mathbf { V }$ , and extra last components in $\mathbf { V } _ { * }$ and $\mathbf { Y }$ , is to automatically calculate, and correct for, an appropriately weighted average of the data, and thus to make equation (3.7.14) an unbiased estimator.

Here is an implementation of equations (3.7.12) – (3.7.15). The constructor does the one-time work, while the two overloaded interp methods calculate either an interpolated value or else a value and a standard deviation (square root of the variance). You should leave the optional argument err set to the default value of NULL until you read $\ S 1 5 . 9$ .

# template<class T>

struct Krig {   
Object for interpolation by kriging, using npt points in ndim dimensions. Call constructor once, then interp as many times as desired. const MatDoub &x;   
const T &vgram;   
Int ndim, npt;   
Doub lastval, lasterr;   
VecDoub y,dstar,vstar,yvi;   
MatDoub v;   
LUdcmp \*vi;

Most recently computed value and (if computed) error.

Krig(MatDoub_I &xx, VecDoub_I &yy, T &vargram, const Doub \*err=NULL) : x(xx),vgram(vargram),npt(xx.nrows()),ndim(xx.ncols()),dstar(npt $+ 1 )$ , vstar(npt $^ { + 1 }$ ),v(npt+1,npt $+ 1$ ),y(npt+1),yvi(npt+1) {

Constructor. The npt $\times$ ndim matrix xx inputs the data points, the vector yy the function values. vargram is the variogram function or functor. The argument err is not used for interpolation; see $\ S 1 5 . 9$ .

Int i,j; for ( $\scriptstyle \dot { 1 } = 0$ ;i<npt; $\dot { \bf 1 } + +$ ) { Fill Y and V . y[i] $=$ yy[i]; for $( \ j = \mathtt { i }$ ;j<npt;j++) { v[i][j] $=$ v[j][i] $=$ vgram(rdist(&x[i][0],&x[j][0])); } v[i][npt] = v[npt][i] = 1.; } v[npt][npt] $=$ y[npt] = 0.; if (err) for ( $\dot { \bar { \boldsymbol { 1 } } } = 0$ ;i<npt; $\dot { 1 } + + \dot { 1 }$ ) v[i][i] -= SQR(err[i]); $\ S 1 5 . 9$ vi $=$ new LUdcmp(v); vi->solve(y,yvi); \~Krig() { delete vi; }

# Doub interp(VecDoub_I &xstar) {

Return an interpolated value at the point xstar. Int i; for ( $\scriptstyle \dot { \mathbf { 1 } } = 0$ ;i<npt; $\dot { 1 } + +$ ) vstar[i] $=$ vgram(rdist(&xstar[0],&x[i][0])); vstar[npt] $\ l = \ 1$ .; lastval $\qquad = \ 0 .$ .; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; $\ { \dot { \mathbf { 1 } } } < =$ npt; $\mathbf { i } + +$ ) lastval $+ =$ yvi[i]\*vstar[i]; return lastval;   
}

Doub interp(VecDoub_I &xstar, Doub &esterr) {

Return an interpolated value at the point xstar, and return its estimated error as esterr.

lastval $=$ interp(xstar);   
vi->solve(vstar,dstar);   
lasterr $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0 $ ;i $< =$ npt; $\Dot { \ b { 1 } } + +$ ) lasterr $+ =$ dstar[i]\*vstar[i];   
esterr $=$ lasterr $=$ sqrt(MAX(0.,lasterr));   
return lastval;

# }

Doub rdist(const Doub \*x1, const Doub \*x2) { Utility used internally. Cartesian distance between two points.

Doub $\mathtt { d } \mathtt { = } 0$ .;   
for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<ndim; $\dot { \bf 1 } + +$ ) d $+ =$ SQR(x1[i]-x2[i]);   
return sqrt(d);

The constructor argument vgram, the variogram function, can be either a func-

tion or functor (-1.3.3). For interpolation, you can use a Powvargram object that fits a simple model

$$
v ( r ) = \alpha r ^ { \beta }
$$

where $\beta$ is considered fixed and $\alpha$ is fitted by unweighted least squares over all pairs of data points $i$ and $j$ . We’ll get more sophisticated about variograms in $\ S 1 5 . 9$ ; but for interpolation, excellent results can be obtained with this simple choice. The value of $\beta$ should be in the range $1 \leq \beta < 2$ . A good general choice is 1:5, but for functions with a strong linear trend, you may want to experiment with values as large as 1:99. (The value 2 gives a degenerate matrix and meaningless results.) The optional argument nug will be explained in $\ S 1 5 . 9$ .

# struct Powvargram {

Functor for variogram $v ( r ) = \alpha r ^ { \beta }$ , where $\beta$ is specified, $\pmb { \alpha }$ is fitted from the data.

Doub alph, bet, nugsq;

Powvargram(MatDoub_I &x, VecDoub_I &y, const Doub beta $^ { = 1 }$ .5, const Doub nug=0.) : bet(beta), nugsq(nug\*nug) {

Constructor. The npt $\times$ ndim matrix $\mathbf { x }$ inputs the data points, the vector y the function values, beta the value of $\beta$ . For interpolation, the default value of beta is usually adequate. For the (rare) use of nug see $\ S 1 5 . 9$ .

Int i,j,k,npt=x.nrows(),ndim=x.ncols(); Doub rb,num $_ { = 0 }$ .,denom $_ { = 0 }$ .; for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<npt; $\dot { \bf 1 } + +$ ) for ( $\scriptstyle \cdot j = \mathbf { i } + 1$ ;j<npt;j++) { $x \mathrm { b } \ = \ 0 .$ ; for $\scriptstyle \mathtt { k } = 0$ ;k<ndim;k++) rb $+ =$ SQR(x[i][k]-x[j][k]); rb $=$ pow(rb,0.5\*beta); num $+ =$ rb\*(0.5\*SQR(y[i]-y[j]) - nugsq); denom $+ =$ SQR(rb); } alph $=$ num/denom; }

Doub operator() (const Doub r) const {return nugsq+alph\*pow(r,bet);} ;

Sample code for interpolating on a set of data points is

MatDoub x(npts,ndim);   
VecDoub y(npts), xstar(ndim);   
Powvargram vgram(x,y);   
Krig<Powvargram> krig(x,y,vgram);

followed by any number of interpolations of the form ystar $=$ krig.interp(xstar);

Be aware that while the interpolated values are quite insensitive to the variogram model, the estimated errors are rather sensitive to it. You should thus consider the error estimates as being order of magnitude only. Since they are also relatively expensive to compute, their value in this application is not great. They will be much more useful in $\ S 1 5 . 9$ , when our model includes measurement errors.

# 3.7.5 Curve Interpolation in Multidimensions

A different kind of interpolation, worth a brief mention here, is when you have an ordered set of $N$ tabulated points in $n$ dimensions that lie on a one-dimensional curve, $\mathbf { X } _ { 0 } , \ldots . . . \mathbf { X } _ { N - 1 }$ , and you want to interpolate other values along the curve. Two cases worth distinguishing are: (i) The curve is an open curve, so that $\mathbf { X } _ { 0 }$ and $\mathbf { X } _ { N - 1 }$ represent endpoints. (ii) The curve is a closed curve, so that there is an implied curve segment connecting $\mathbf { X } _ { N - 1 }$ back to $\mathbf { X } _ { 0 }$ .

A straightforward solution, using methods already at hand, is first to approximate distance along the curve by the sum of chord lengths between the tabulated points, and then to construct spline interpolations for each of the coordinates, $0 , \ldots$ ; $n - 1$ , as a function of that parameter. Since the derivative of any single coordinate with respect to arc length can be no greater than 1, it is guaranteed that the spline interpolations will be well-behaved.

Probably $90 \%$ of applications require nothing more complicated than the above. If you are in the unhappy $10 \%$ , then you will need to learn about Bezier curves ´ , $B$ - splines, and interpolating splines more generally [12,13,14]. For the happy majority, an implementation is

# struct Curve_interp {

Object for interpolating a curve specified by n points in dim dimensions.

Set if a closed curve.

Int dim, n, in;   
Bool cls;   
MatDoub pts;   
VecDoub s;   
VecDoub ans;   
NRvector<Spline_interp\*> srp;

Curve_interp(MatDoub &ptsin, Bool close $\mathtt { \mathtt { = 0 } }$ ) : n(ptsin.nrows()), dim(ptsin.ncols()), in(close ? 2\*n : n), cls(close), pts(dim,in), s(in), ans(dim), srp(dim) {

Constructor. The $\mathrm { ~ \tt ~ { ~ n ~ } ~ } \times$ dim matrix ptsin inputs the data points. Input close as 0 for an open curve, 1 for a closed curve. (For a closed curve, the last data point should not duplicate the first — the algorithm will connect them.)

Int i,ii,im,j,ofs; Doub ss,soff,db,de; ofs $=$ close ? n/2 : 0; The trick for closed curves is to duplicate half a $\mathbf { s } \left[ 0 \right] \ = \ 0 .$ ; period at the beginning and end, and then for ( $\scriptstyle \dot { 1 } = 0$ ;i<in; $\dot { \bf 1 } + +$ ) { use the middle half of the resulting spline. $\mathrm { i \mathrm { i } \mathrm { \Omega } = \Omega ( \mathrm { i } - \mathrm { o f } s + \mathrm { n } ) \Omega \mathrm { \Omega } \mathrm { \Omega } _ { \mathrm { 0 } } ^ { \mathrm { { q } } } \mathrm { n } ; }$ $\mathrm { i m \ = \ \Gamma ( i i \mathrm { \bf i - 1 + n } ) }$ % n; for $( \ j = 0$ ;j<dim; ${ \mathrm { j } } + + { \mathrm { j } }$ ) pts[j][i] $=$ ptsin[ii][j]; Store transpose. if (i>0) { Accumulate arc length. s[i] $=$ s[i-1] $^ +$ rad(&ptsin[ii][0],&ptsin[im][0]); if $\mathrm { \Delta \ J ~ } = = \mathrm { \Delta s [ i - 1 ] }$ ) throw("error in Curve_interp") Consecutive points may not be identical. For a closed curve, the last data point should not duplicate the first. } } ss $=$ close ? s[ofs+n]-s[ofs] : s[n-1]-s[0]; Rescale parameter so that the soff $=$ s[ofs]; interval [0,1] is the whole curve (or one period). for ( $\scriptstyle \dot { 1 } = 0$ ;i<in; $\dot { \bf 1 } + +$ ) s[i] $=$ (s[i]-soff)/ss; for (j ${ = } 0$ ;j<dim;j++) { Construct the splines using endpoint derivatives. db $=$ in $< ~ 4 ~ 7$ 1.e99 : fprime(&s[0],&pts[j][0],1); de $=$ in $<$ 4 ? 1.e99 : fprime(&s[in-1],&pts[j][in-1],-1); srp[j] $=$ new Spline_interp(s,&pts[j][0],db,de); } }

\~Curve_interp() {for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<dim;j++) delete srp[j];}

# VecDoub &interp(Doub t) {

Interpolate a point on the stored curve. The point is parameterized by t, in the range [0,1]. For open curves, values of t outside this range will return extrapolations (dangerous!). For closed curves, t is periodic with period 1.

if (cls) $\texttt { t } = \texttt { t }$ - floor(t); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<dim; $\mathrm { j } + + \mathrm { . }$ ) ans[j] $=$ (\*srp[j]).interp(t); return ans; }

Doub fprime(Doub \*x, Doub \*y, Int pm) Utility for estimating the derivatives at the endpoints. x and y point to the abscissa and ordinate of the endpoint. If pm is $+ 1$ , points to the right will be used (left endpoint); if it is $^ { - 1 }$ , points to the left will be used (right endpoint). See text, below.

Doub $\mathbf { s } 1 ~ = ~ \mathbf { x } \left[ 0 \right] - \mathbf { x } \left[ \mathbf { p } \mathbf { m } * 1 \right]$ , ${ \bf s } 2 ~ = ~ { \bf x } \left[ 0 \right] - { \bf x } \left[ \mathrm { p m } { * 2 } \right]$ , ${ \bf s } 3 ~ = ~ { \bf x } \left[ 0 \right] - { \bf x } \left[ { \bf p } { \mathrm { m } } * 3 \right]$ , s12 $=$ s1-s2, $\mathtt { s } 1 3 \ = \ \mathtt { s } 1 - \mathtt { s } 3$ , ${ \tt s } 2 3 = { \tt s } 2 - { \tt s } 3 $ ;   
return -(s1\*s2/(s13\*s23\*s3))\*y[pm $^ *$ 3] $^ +$ (s1\*s3/(s12\*s2\*s23))\*y[pm\*2] -(s2\*s3/(s1\*s12\*s13))\*y[pm\*1]+(1./s1+1./s2+1./s3)\*y[0];

# }

Doub rad(const Doub \*p1, const Doub \*p2) {  
Euclidean distance.Doub sum $\qquad = \ 0$ .;for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<dim;i++) sum $+ =$ SQR(p1[i]-p2[i]);return sqrt(sum);  
}

};

The utility routine fprime estimates the derivative of a function at a tabulated abscissa $x _ { 0 }$ using four consecutive tabulated abscissa-ordinate pairs, $( x _ { 0 } , y _ { 0 } ) , \ldots$ ; $( x _ { 3 } , y _ { 3 } )$ . The formula for this, readily derived by power-series expansion, is

$$
y _ { 0 } ^ { \prime } = - C _ { 0 } y _ { 0 } + C _ { 1 } y _ { 1 } - C _ { 2 } y _ { 2 } + C _ { 3 } y _ { 3 }
$$

where

$$
\begin{array} { l } { \displaystyle C _ { 0 } = \frac { 1 } { s _ { 1 } } + \frac { 1 } { s _ { 2 } } + \frac { 1 } { s _ { 3 } } } \\ { \displaystyle C _ { 1 } = \frac { s _ { 2 } s _ { 3 } } { s _ { 1 } ( s _ { 2 } - s _ { 1 } ) ( s _ { 3 } - s _ { 1 } ) } } \\ { \displaystyle C _ { 2 } = \frac { s _ { 1 } s _ { 3 } } { ( s _ { 2 } - s _ { 1 } ) s _ { 2 } ( s _ { 3 } - s _ { 2 } ) } } \\ { \displaystyle C _ { 3 } = \frac { s _ { 1 } s _ { 2 } } { ( s _ { 3 } - s _ { 1 } ) ( s _ { 3 } - s _ { 2 } ) s _ { 3 } } } \end{array}
$$

with

$$
\begin{array} { c } { { s _ { 1 } \equiv x _ { 1 } - x _ { 0 } } } \\ { { \nonumber } } \\ { { s _ { 2 } \equiv x _ { 2 } - x _ { 0 } } } \\ { { \nonumber } } \\ { { s _ { 3 } \equiv x _ { 3 } - x _ { 0 } } } \end{array}
$$

# CITED REFERENCES AND FURTHER READING:

Buhmann, M.D. 2003, Radial Basis Functions: Theory and Implementations (Cambridge, UK: Cambridge University Press).[1]

Powell, M.J.D. 1992, “The Theory of Radial Basis Function Approximation” in Advances in Numerical Analysis I: Wavelets, Subdivision Algorithms and Radial Functions,ed.W.A.Light (Oxford: Oxford University Press), pp. 105–210.[2]

Wikipedia. $^ { 2 0 0 7 + }$ , “Radial Basis Functions,” at http://en.wikipedia.org/.[3]

Beatson, R.K. and Greengard, L. 1997, “A Short Course on Fast Multipole Methods”, in Wavelets, Multilevel Methodsand Eliptic PDEs,eds.M.Ainsworth,J.Levesley，W.Light,andM.Marletta (Oxford: Oxford University Press), pp. 1–37.[4]

Beatson, R.K. and Newsam, G.N. 1998, “Fast Evaluation of Radial Basis Functions: Moment-Based Methods” in SIAM Journal on Scientific Computing, vol. 19, pp. 1428-1449.[5]   
Wendland, H. 2005, Scattered Data Approximation (Cambridge, UK: Cambridge University Press).[6]   
Franke, R. 1982, “Scattered Data Interpolation: Tests of Some Methods," Mathematics of Computation, vol.38,pp.181-200.[7]   
Shepard, D. 1968, “A Two-dimensional Interpolation Function for Irregularly-spaced Data,” in Proceedings of the 1968 23rd ACM National Conference (New York: ACM Press),pp.517- 524.[8]   
Cressie, N. 1991, Statistics for Spatial Data (New York: Wiley).[9]   
Wackernagel, H. 1998, Multivariate Geostatistics, 2nd ed. (Berlin: Springer).[10]   
Rybicki, G.B., and Press, W.H. 1992, “Interpolation, Realization, and Reconstruction of Noisy, Irregularly Sampled Data,” Astrophysical Journal, vol. 398, pp. 169–176.[11]   
Isaaks, E.H., and Srivastava, R.M. 1989, Applied Geostatistics (New York: Oxford University Press).   
Deutsch, C.V., and Journel, A.G. 1992, GSLIB: Geostatistical Software Library and User’s Guide (New York: Oxford University Press).   
Knott, G.D. 1999, Interpolating Cubic Splines (Boston: Birkhäuser).[12]   
De Boor, C. 2001, A Practical Guide to Splines (Berlin: Springer).[13]   
Prautzsch, H., Boehm, W., and Paluszny, M. 2002, Bézier and B-Spline Techniques (Berlin: Springer).[14]

# 3.8 Laplace Interpolation

In this section we look at a missing data or gridding problem, namely, how to restore missing or unmeasured values on a regular grid. Evidently some kind of interpolation from the not-missing values is required, but how shall we do this in a principled way?

One good method, already in use at the dawn of the computer age [1,2], is Laplace interpolation, sometimes called Laplace/Poisson interpolation. The general idea is to find an interpolating function $y$ that satisfies Laplace’s equation in $n$ dimensions,

$$
\nabla ^ { 2 } y = 0
$$

wherever there is no data, and which satisfies

$$
y ( \mathbf { x } _ { i } ) = y _ { i }
$$

at all measured data points. Generically, such a function does exist. The reason for choosing Laplace’s equation (among all possible partial differential equations, say) is that the solution to Laplace’s equation selects, in some sense, the smoothest possible interpolant. In particular, its solution minimizes the integrated square of the gradient,

$$
\int _ { \Omega } | \nabla y | ^ { 2 } d \Omega
$$

where $\Omega$ denotes the $n$ -dimensional domain of interest. This is a very general idea, and it can be applied to irregular meshes as well as to regular grids. Here, however, we consider only the latter.

For purposes of illustration (and because it is the most useful example) we further specialize to the case of two dimensions, and to the case of a Cartesian grid whose $x _ { 1 }$ and $x _ { 2 }$ values are evenly spaced — like a checkerboard.

In this geometry, the finite difference approximation to Laplace’s equation has a particularly simple form, one that echos the mean value theorem for continuous solutions of the Laplace equation: The value of the solution at any free gridpoint (i.e., not a point with a measured value) equals the average of its four Cartesian neighbors. (See $\ S 2 0 . 0 . \ r .$ ) Indeed, this already sounds a lot like interpolation.

If $y _ { 0 }$ denotes the value at a free point, while $y _ { u } , y _ { d } , y _ { l }$ , and $y _ { r }$ denote the values at its up, down, left, and right neighbors, respectively, then the equation satisfied is

$$
\begin{array} { r } { y _ { 0 } - \frac { 1 } { 4 } y _ { u } - \frac { 1 } { 4 } y _ { d } - \frac { 1 } { 4 } y _ { l } - \frac { 1 } { 4 } y _ { r } = 0 } \end{array}
$$

For gridpoints with measured values, on the other hand, a different (simple) equation is satisfied,

$$
y _ { 0 } = y _ { 0 } ( \mathrm { m e a s u r e d } )
$$

Note that these nonzero right-hand sides are what make an inhomogeneous, and therefore generally solvable, set of linear equations.

We are not quite done, since we must provide special forms for the top, bottom, left, and right boundaries, and for the four corners. Homogeneous choices that embody “natural” boundary conditions (with no preferred function values) are

$$
\begin{array} { r l } { y _ { 0 } - \frac 1 2 y _ { u } - \frac 1 2 y _ { d } = 0 \quad } & { ( \mathrm { l e f t a n d ~ r i g h t ~ b o u n d a r i e s } ) } \\ { y _ { 0 } - \frac 1 2 y _ { l } - \frac 1 2 y _ { r } = 0 \quad } & { ( \mathrm { t o p ~ a n d ~ b o t t o m ~ b o u n d a r i e s } ) } \\ { y _ { 0 } - \frac 1 2 y _ { r } - \frac 1 2 y _ { d } = 0 \quad } & { ( \mathrm { t o p \mathrm { - } l e f t ~ c o r n e r } ) } \\ { y _ { 0 } - \frac 1 2 y _ { l } - \frac 1 2 y _ { d } = 0 \quad } & { ( \mathrm { t o p \mathrm { - } r i g h t ~ c o r n e r } ) } \\ { y _ { 0 } - \frac 1 2 y _ { r } - \frac 1 2 y _ { u } = 0 \quad } & { ( \mathrm { b o t t o m \mathrm { - } l e f t ~ c o r n e r } ) } \\ { y _ { 0 } - \frac 1 2 y _ { l } - \frac 1 2 y _ { u } = 0 \quad } & { ( \mathrm { b o t t o m \mathrm { - } r i g h t ~ c o r n e r } ) } \end{array}
$$

Since every gridpoint corresponds to exactly one of the equations in (3.8.4), (3.8.5), or (3.8.4), we have exactly as many equations as there are unknowns. If the grid is $M$ by $N$ , then there are $M N$ of each. This can be quite a large number; but the equations are evidently very sparse. We solve them by defining a derived class from $\ S 2 . 7$ ’s Linbcg base class. You can readily identify all the cases of equations (3.8.4) – (3.8.6) in the code for atimes, below.

# struct Laplace_interp : Linbcg {

Object for interpolating missing data in a matrix by solving Laplace’s equation. Call constructor once, then solve one or more times (see text).

MatDoub &mat;   
Int ii,jj;   
Int nn,iter;   
VecDoub b,y,mask;   
Laplace_interp(MatDoub_IO &matrix) : mat(matrix), ii(mat.nrows()),   
jj(mat.ncols()), nn(ii\*jj), iter(0), b(nn), y(nn), mask(nn) {   
Constructor. Values greater than 1.e99 in the input matrix mat are deemed to be missing   
data. The matrix is not altered until solve is called. Int i,j,k; Doub $\mathtt { v 1 } = 0 .$ .;

for $\scriptstyle ( \mathtt { k } = 0$ ;k<nn;k++) { Fill the r.h.s. vector, the initial guess, $\mathrm { ~ i ~ } = \mathrm { ~ k ~ } / \mathrm { j } \mathrm { j }$ ; and a mask of the missing data. $\mathrm { ~ j ~ } = \mathrm { ~ k ~ }$ - i\*jj; if (mat[i][j] < 1.e99) { b[k] $=$ y[k] $\ l = \ l { \nabla \bot } =$ mat[i][j]; mask[k] $\ c = ~ 1$ ; } else { b[k] $\qquad = \ 0 .$ ; y[k] $\mathbf { \Sigma } = \mathbf { \Sigma } \_ { 1 } \mathbf { \Sigma } _ { 1 }$ ; mask[k] $\mathit { \Theta } = \mathit { \Theta } 0$ ; } } }

void asolve(VecDoub_I &b, VecDoub_O &x, const Int itrnsp);   
void atimes(VecDoub_I &x, VecDoub_O &r, const Int itrnsp);   
See definitions below. These are the real algorithmic content.

Doub solve(Doub tol $= 1$ .e-6, Int itmax=-1) {

Invoke Linbcg::solve with appropriate arguments. The default argument values will usually work, in which case this routine need be called only once. The original matrix mat is refilled with the interpolated solution.

Int i,j,k; Doub err; if (itmax $\mathit { \Theta } < = \mathit { \Theta } 0 .$ ) itmax $\quad = \ 2 *$ MAX(ii,jj); Linbcg::solve(b,y,1,tol,itmax,iter,err); for $\scriptstyle 1 = 0$ , $\scriptstyle \dot { 1 } = 0$ ;i<ii; $\dot { \bf 1 } + +$ ) for ( $\scriptstyle \mathbf { j } = 0$ ;j<jj;j $^ { + + }$ ) mat[i][j] $=$ y[k $+ + ]$ ; return err; } };

void Laplace_interp::asolve(VecDoub_I &b, VecDoub_O &x, const Int itrnsp) {   
Diagonal preconditioner. (Diagonal elements all unity.) Int i, $\mathtt { n } = \mathtt { b }$ .size(); for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n; $\dot { 1 } + +$ ) x[i] $=$ b[i];   
}

void Laplace_interp::atimes(VecDoub_I &x, VecDoub_O &r, const Int itrnsp) { Sparse matrix, and matrix transpose, multiply. This routine embodies eqs. (3.8.4), (3.8.5), and (3.8.6).

Int i,j,k, $\mathbf { n } { = } \mathbf { r }$ .size(),jjt,it;   
Doub del;   
for $( \mathtt { k } = 0$ ;k<n;k++) r[k] = 0.;   
for $\scriptstyle ( \mathtt { k } = 0$ ;k<n;k $^ { + + }$ ) { $\begin{array} { r l } { \dot { \mathbf { 1 } } } & { { } = } \end{array}$ k/jj; j = k - i\*jj; if (mask[k]) { Measured point, eq. (3.8.5). r[k] $+ =$ x[k]; } else if ( $\mathtt { i } > 0$ && i<ii-1 && j>0 && j<jj-1) { Interior point, eq. (3.8.4). if (itrnsp) { r[k] $+ =$ x[k]; del $=$ -0.25\*x[k]; r[k-1] $+ =$ del; r[k+1] $+ =$ del; r[k-jj] $+ =$ del; r[k+jj] $+ =$ del; } else { r[k] $=$ x[k] - 0.25\*(x[k-1]+x[k+1]+x[k+jj]+x[k-jj]); } } else if (i>0 && i<ii-1) { Left or right edge, eq. (3.8.6). if (itrnsp) { r[k] $+ = \texttt { x }$ [k]; del $=$ -0.5\*x[k]; r[k-jj] $+ =$ del;

r[k+jj] $+ =$ del; } else { r[k] $=$ x[k] - 0.5\*(x[k+jj]+x[k-jj]); } } else if (j>0 && j<jj-1) { Top or bottom edge, eq. (3.8.6). if (itrnsp) { r[k] $+ =$ x[k]; del $=$ -0.5\*x[k]; r[k-1] $+ =$ del; r[k+1] $+ =$ del; } else { r[k] $=$ x[k] - 0.5\*(x[k+1]+x[k-1]); } } else { Corners, eq. (3.8.6). jjt $= \mathrm { \ i = = } 0$ ? jj : -jj; it $= \mathrm { \ j = = } 0$ ? 1 : -1; if (itrnsp) { r[k] $+ =$ x[k]; del $=$ -0.5\*x[k]; r[k+jjt] $+ =$ del; r[k+it] $+ =$ del; } else { r[k] $=$ x[k] - 0.5\*(x[k+jjt]+x[k+it]); } }

Usage is quite simple. Just fill a matrix with function values where they are known, and with 1.e99 where they are not; send the matrix to the constructor; and call the solve routine. The missing values will be interpolated. The default arguments should serve for most cases.

Int m=...,n=...;   
MatDoub mat(m,n);   
Laplace_interp mylaplace(mat);   
mylaplace.solve();

Quite decent results are obtained for smooth functions on $3 0 0 ~ \times ~ 3 0 0$ matrices in which a random $10 \%$ of gridpoints have known function values, with $90 \%$ interpolated. However, since compute time scales as $M N$ max $( M , N )$ (that is, as the cube), this is not a method to use for much larger matrices, unless you break them up into overlapping tiles. If you experience convergence difficulties, then you should call solve, with appropriate nondefault arguments, several times in succession, and look at the returned error estimate after each call returns.

# 3.8.1 Minimum Curvature Methods

Laplace interpolation has a tendency to yield cone-like cusps around any small islands of known data points that are surrounded by a sea of unknowns. The reason is that, in two dimensions, the solution of Laplace’s equation near a point source is logarithmically singular. When the known data is spread fairly evenly (if randomly) across the grid, this is not generally a problem. Minimum curvature methods deal with the problem at a more fundamental level by being based on the biharmonic equation

$$
\nabla ( \nabla y ) = 0
$$

instead of Laplace’s equation. Solutions of the biharmonic equation minimize the integrated square of the curvature,

$$
\int _ { \Omega } | \nabla ^ { 2 } y | ^ { 2 } d \Omega
$$

Minimum curvature methods are widely used in the earth-science community [3,4].

The references give a variety of other methods that can be used for missing data interpolation and gridding.

# CITED REFERENCES AND FURTHER READING:

Noma, A.A. and Misulia, M.G. 1959, “Programming Topographic Maps for Automatic Terrain Model Construction,” Surveying and Mapping, vol. 19, pp. 355–366.[1]   
Crain, I.K. 1970, “Computer Interpolation and Contouring of Two-dimensional Data: a Review,” Geoexploration,vol.8,pp.71-86.[2]   
Burrough, P.A. 1998, Principles of Geographical Information Systems, 2nd ed. (Oxford, UK: Clarendon Press)   
Watson, D.F. 1982, Contouring: A Guide to the Analysis and Display of Spatial Data (Oxford, UK: Pergamon).   
Briggs, I.C. 1974, “Machine Contouring Using Minimum Curvature,” Geophysics, vol. 39, pp. 39– 48.[3]   
Smith, W.H.F. and Wessel, P. 1990, “Gridding With Continuous Curvature Splines in Tension,” Geophysics,vol.55,pp.293-305.[4]

# 4.0 Introduction

Numerical integration, which is also called quadrature, has a history extending back to the invention of calculus and before. The fact that integrals of elementary functions could not, in general, be computed analytically, while derivatives could be, served to give the field a certain panache, and to set it a cut above the arithmetic drudgery of numerical analysis during the whole of the 18th and 19th centuries.

With the invention of automatic computing, quadrature became just one numerical task among many, and not a very interesting one at that. Automatic computing, even the most primitive sort involving desk calculators and rooms full of “computers” (that were, until the 1950s, people rather than machines), opened to feasibility the much richer field of numerical integration of differential equations. Quadrature is merely the simplest special case: The evaluation of the integral

$$
I = \int _ { a } ^ { b } f ( x ) d x
$$

is precisely equivalent to solving for the value $I \equiv y ( b )$ the differential equation

$$
{ \frac { d y } { d x } } = f ( x )
$$

with the boundary condition

$$
y ( a ) = 0
$$
