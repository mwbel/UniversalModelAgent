![](images/c8d39bd479d7069bb175a27deb475da158dc3822b2d52f2be6734029d4a7a46a.jpg)

(a)

![](images/c20adf96de98c1b083f2c59ab10d8889cd96036c78fb4814fd42a55b66bcf44c.jpg)  
Figure 22.3.1. Single-bit operations for calculating the Gray code $G ( i )$ from $i$ (a), or the inverse (b). LSB and MSB indicate the least and most significant bits, respectively. XOR denotes exclusive-or.

# struct Gray {

Methods for the Gray code and its inverse.

Uint gray(const Uint n) {return n ^ (n >> 1);} Return the Gray code of an integer n. This is the easy direction!

Uint invgray(const Uint n) { Return the inverse of the Gray code. Int ish $^ { = 1 }$ ; Uint ans $= _ { \mathrm { n } }$ ,idiv; for (;;) { In hierarchical stages, starting with a one-bit right-shift, ans $\hat { \mathbf { \alpha } } =$ (idiv=ans >> ish); cause each bit to be XORed with all more sigif (idiv $\scriptstyle < = ~ 1$ || ish $\scriptstyle = = \ 1 6 $ ) return ans; nificant bits. ish $< < = ~ 1$ ; Double the amount of shift on the next cycle. } } };

In numerical work, Gray codes can be useful when you need to do some task that depends intimately on the bits of $i$ , looping over many values of $i$ . Then, if there are economies in repeating the task for values differing by only one bit, it makes sense to do things in Gray code order rather than consecutive order. We saw an example of this in $\ S 7 . 8$ , for the generation of quasi-random sequences.

# CITED REFERENCES AND FURTHER READING:

Horowitz, P., and Hill, W. 1989, The Art of Electronics, 2nd ed. (New York: Cambridge University Press), $\ S 8 . 0 2$ .   
Knuth, D.E. 2005, Generating All Tuples and Permutations, fascicle 2 of vol. 4 of The Art of Computer Programming (Upper Saddle River, NJ: Addison-Wesley), $\ S 7 . 2 . 1 . 1$ .

# 22.4 Cyclic Redundancy and Other Checksums

There are networks all around you: not just “the” Internet with its IP and TCP protocols, but also embedded networks that move bits around within a device or among closely coupled devices. Examples include the SMBus network that communicates power management information between smart batteries and the devices that they power, or the Bluetooth network that connects cell phones to nearby accessories. We wouldn’t be overly surprised to find a network inside of our wristwatch or electric toothbrush!

Different networks have different protocols, but standard engineering practice is to package the raw information into packets with fixed or variable numbers of bits. Packet lengths are typically in the range from a few tens to a few thousand bits. Smaller would imply proportionally too much overhead per packet, while longer would make excessive demands on buffer sizes, collision avoidance, etc.

When a packet is sent from point A to point B, one wants to know that it has arrived without error. The simplest form of insurance is to add a “parity bit,” chosen so as to make the total number of one-bits (versus zero-bits) either always even (“even parity”) or always odd (“odd parity”). Any single-bit error in a packet will thereby be detected. When errors are sufficiently rare, or their consequence sufficiently minor, use of parity provides enough error detection. For example, the ASCII character set was originally designed for 7-bit characters, with an 8th parity bit.

Since the parity bit has two possible values (0 and 1), it has, on average, only a $50 \%$ chance of detecting an erroneous packet with multiple wrong bits. That is not nearly good enough for most applications. Most communications protocols [1] use a multibit generalization of the parity bit called a “cyclic redundancy check” or CRC. Often, the CRC is 16 bits (two bytes) long. Then the chance of a random set of errors going undetected is 1 in $2 ^ { 1 6 } = 6 5 5 3 6$ .

Now enters mathematics. It is easy to find $M$ -bit CRCs that have the property of detecting all errors that occur in $M$ or fewer consecutive bits, for any length of message. (We prove this below.) Since noise in communication channels tends to be “bursty,” with short sequences of adjacent bits getting corrupted, this consecutive-bit property is highly desirable. Furthermore, for packets with a fixed (or bounded) payload size of $N$ bits, one can find CRCs that find all occurrences of $D$ or fewer errors anywhere in the payload. Obviously, the game is to find the CRC that maximizes $D$ . The value $D + 1$ is the Hamming distance of the CRC for that value of $N$ using that checksum (cf. $\ S 1 6 . 2 )$ .

<table><tr><td rowspan=1 colspan=4>Useful 16-bit CRC Polynomials (after [3])</td></tr><tr><td rowspan=1 colspan=1>j</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Polynomial</td><td rowspan=1 colspan=1>Best N (bits)</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0x755B=(x³+x²+1)*(x6+x5+x²+x+1)*(x7+x³+1)*</td><td rowspan=1 colspan=1>242-2048+</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>OxA7D3=(x³+x²+1)*(x+x5+x²+x+1)*(x7+x6+x5+x4+1)*</td><td rowspan=1 colspan=1>256-2048+</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>ANSI-16</td><td rowspan=1 colspan=1>0x8005=(x+1)(x15+x+1)*</td><td rowspan=1 colspan=1>242-2048+</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>CCITT-16</td><td rowspan=1 colspan=1>0x1021=(x+1)(x15+x14+x13+x12+x4+x³+x2+x+1)*</td><td rowspan=1 colspan=1>242-2048+</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0x5935=(x16+x14+𝑥1²+x11+x8+x5+x4+x²+1)</td><td rowspan=1 colspan=1>136-241</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0x90D9=(x+1)(x15+x11+x10+x9+x8+x7+x5+x4+x²+x+1)</td><td rowspan=1 colspan=1>20-135</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>IEC-16</td><td rowspan=1 colspan=1>0x5B93=(x+1)(x+1)(x7+x+x³+x+1)*(x7+x+x5+x4+x³+x²+1)*</td><td rowspan=1 colspan=1>20-112</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0x2D17=(x²+x+1)*(x14+x1³+x9+x7+x5+x4+1)</td><td rowspan=1 colspan=1>16-19</td></tr><tr><td rowspan=1 colspan=4>* denotes primitive factor</td></tr></table>

The design of CRCs lies in the province of communications software experts and chip-level hardware designers — people with bits under their fingernails. A passing familiarity with some of the concepts involved can be useful, however, both because the mathematics involved has connections to other applications (for example, random number generation, cf. $\ S 7 . 1$ and $\ S 7 . 5$ , and because you might actually want to add a couple of bytes of checksum to your own data records in some applications where you are handling, or moving, large amounts of data.

Sometimes CRCs can be used to compress data as they are recorded. If identical data records occur frequently, one can keep sorted in memory the CRCs of previously encountered records. A new record is archived in full if its CRC is different, otherwise only a pointer to a previous record need be archived. In this application one might use 8 bytes of CRC, to make the odds of mistakenly discarding a different data record tolerably small; or, if previous records can be randomly accessed, a full comparison can be made to decide whether records with identical CRCs are in fact identical.

Now let us briefly discuss the theory of CRCs. After that, we will give an implementation that generates 16-bit CRCs that are known to be particularly good, or else are enshrined as standard (and, it turns out, this is not the same thing!).

The mathematics underlying CRCs is “polynomials over the integers modulo 2.” Any binary message can be thought of as a polynomial with coefficients 0 and 1. For example, the message “1100001101” is the polynomial $x ^ { 9 } + x ^ { 8 } + x ^ { 3 } + x ^ { 2 } + 1$ Since 0 and 1 are the only integers modulo 2, a power of $x$ in the polynomial is either present (1) or absent (0).

An $M$ -bit-long CRC is based on a polynomial of degree $M$ , called the generator polynomial. Given the generator polynomial $G$ (which can be written either in polynomial form or as a bit-string, e.g., 10001000000100001 for $x ^ { 1 6 } + x ^ { 1 2 } + x ^ { 5 } + 1 )$ , here is how you compute the CRC for a sequence of bits $S$ : First, multiply $S$ by $x ^ { M }$ , that is, append $M$ zero bits to it. Second, divide, by long division, $G$ into $S x ^ { M }$ . Keep in mind that the subtractions in the long division are done modulo 2, so that there are never any “borrows”: Modulo 2 subtraction is the same as logical exclusive-or (XOR). Third, ignore the quotient you get. Fourth, when you eventually get to a remainder, it is the CRC; call it $C$ . $C$ will be a polynomial of degree $M - 1$ or less, otherwise you would not have finished the long division. Therefore, in bit-string form, it has $M$ bits, which may include leading zeros. ( $C$ might even be all zeros; see below.)

If you work through the above steps in an example, you will see that most of what you write down in the long-division tableau is superfluous. You are actually just left-shifting sequential bits of $S$ , from the right, into an $M$ -bit register. Every time a 1 bit gets shifted off the left end of this register, you zap the register by an XOR with the $M$ low-order bits of $G$ (that is, all the bits of $G$ except its leading 1). When a 0 bit is shifted off the left end you don’t zap the register. When the last bit that was originally part of $S$ gets shifted off the left end of the register, what remains is the CRC.

You can immediately recognize how efficiently this procedure can be implemented in hardware. It requires only a shift register with a few hard-wired XOR taps into it. That is how CRCs are computed in communications devices, taking a tiny part of a single chip. In software, the implementation is not so elegant, since bit-shifting is not generally very efficient. One therefore typically finds (as in our implementation below) table-driven routines that pre-calculate the result of a bunch of shifts and XORs, say for each of 256 possible 8-bit inputs [2].

Every generator polynomial of degree $M$ with a nonzero $x ^ { 0 }$ term yields a CRC that detects all possible combinations of errors in any frame of $M$ consecutive bits. (A special case of this is that it detects any single-bit error in a message of arbitrary length $N$ .) To see how this works, suppose two messages, $S$ and $T$ , differ only within a frame of $M$ bits. Then their CRCs differ by an amount that is the remainder when $G$ is divided into $( S - T ) x ^ { M } \equiv R$ . Now $R$ has the form of leading zeros (which can be ignored), followed by some 1’s in an $M$ -bit frame, followed by trailing zeros (which are just multiplicative factors of $x$ ): $R = x ^ { n } F$ , where $F$ is a polynomial of degree at most $M - 1$ and $n > 0$ . But since $G$ has a nonzero $x ^ { 0 }$ term, it is not divisible by $x$ . So $G$ cannot divide $R$ . Therefore $S$ and $T$ must have different CRCs.

What about two-bit errors, not necessarily in a frame of size $M ?$ That leads us to primitive polynomials: A polynomial over the integers modulo 2 may be irreducible, meaning that it can’t be factored. A subset of the irreducible polynomials is the primitive polynomials. These generate maximum length sequences when used in shift registers, as described in $\ S 7 . 5$ . The polynomial $x ^ { 2 } + 1$ is not irreducible: $x ^ { 2 } +$ $1 = ( x + 1 ) ( x + 1 )$ , so it is also not primitive. The polynomial $x ^ { 4 } + x ^ { 3 } + x ^ { 2 } + x + 1$ is irreducible, but it turns out not to be primitive. The polynomial $x ^ { 4 } + x + 1$ is both irreducible and primitive.

Primitive polynomials are here interesting because they have a very high order. Don’t confuse order with degree: The order $e$ of a polynomial is the smallest integer $e$ such that the polynomial divides (in the present mod 2 case) $x ^ { e } + 1$ . Primitive polynomials, it turns out, have the largest possible order $e$ for their degree $n$ , given by

$$
e = 2 ^ { n } - 1
$$

(In fact, this is why their shift registers have maximum length.) If two messages differ on exactly two bits, spaced $k$ bits apart, then their difference is $x ^ { k } + 1$ times some trailing powers of $x$ . If the generator $G$ contains a primitive factor of order $e$ , then $G$ can’t possibly divide this difference, as long as $k < e$ .

Thus, a primitive factor of degree $n$ guarantees two-bit error detection for spacings up to $2 ^ { n } - 1$ . For this reason, generators are often chosen to be primitive polynomials of degree $M$ . Alternatively, the generator may be chosen be a primitive polynomial times $( 1 + x )$ , which turns out to detect parity errors for all message sizes $N$ , while the range of two-bit detections is reduced only by a factor of 2.

A number of “standard” CRC polynomials were chosen by no other criteria, sometimes adding only the criterion that they should have only a small number of terms. (This was at one time important for hardware design.) For example, the CCITT (Comite Consultatif International T ´ el´ egraphique et T ´ el´ ephonique) has ´ anointed $x ^ { 1 6 } + x ^ { 1 2 } + x ^ { 5 } + 1$ as “CCITT- $1 6 ^ { \circ }$ ; it is the product of $x + 1$ and a primitive polynomial. The polynomial ANSI-16 (see table on p. 1169) also has this character.

Similarly for some choices other than 16 bits: “CRC-12” is $( x + 1 ) ( x ^ { 1 1 } + x ^ { 2 } +$ 1/, the latter factor being primitive. The most common 32-bit CRC, “CRC-32,” used in the ethernet standard (IEEE 802.3) and elsewhere, is $x ^ { 3 2 } + x ^ { 2 6 } + x ^ { 2 3 } + x ^ { 2 2 } +$ $x ^ { 1 6 } + x ^ { 1 2 } + x ^ { 1 1 } + x ^ { 1 0 } + x ^ { 8 } + x ^ { 7 } + x ^ { 5 } + x ^ { 4 } + x ^ { 2 } + x + 1$ , which is primitive.

Now here is something relatively new in this ancient field [3]: For carefully chosen generators $G$ , all two-bit errors in a packet with payload size $N$ can be detected even if $e < N$ . This is because the previous argument was sufficient, but not necessary: A cleverly chosen $G$ can fail to divide $x ^ { k } - 1$ for other reasons than having a primitive factor of large order. This idea opens up the design space to search, essentially by brute force, for generators that have $D > 2$ , that is, are capable of finding not just all two-bit errors, but all three-bit errors, all four-bit errors, etc., up to some bound that depends on $N$ and $M$ . Several of these “new” generators are shown in the table on p. 1169, which is based on [3] (which see for details), along with their recommended values of $N$ . A generator that is good for large $N$ is not necessarily good for small $N$ , and vice versa, so you should stick to the recommended values. The hexadecimal values in the table give binary representations of the polynomials, with the convention that each must be prefaced by a leading 1 (the $x ^ { 1 6 }$ term).

In most protocols, a transmitted block of data consists of some $N$ data bits, directly followed by the $M$ bits of their CRC (or the CRC XORed with a constant; see below). There are two equivalent ways of validating a block at the receiving end. Most obviously, the receiver can compute the CRC of the data bits, and compare it to the transmitted CRC bits. Less obviously, but more elegantly, the receiver can simply compute the CRC of the total block, with $N + M$ bits, and verify that a result of zero is obtained. Proof: The total block is the polynomial $S x ^ { M } + C$ (data left-shifted to make room for the CRC bits). The definition of $C$ is that $S x ^ { m } = Q G + C$ , where $Q$ is the discarded quotient. But then $S x ^ { M } + C = Q G + C + C = Q G$ (remember modulo 2), which is a perfect multiple of $G$ . It remains a multiple of $G$ when it gets multiplied by an additional $x ^ { M }$ on the receiving end, so it has a zero CRC, q.e.d.

A couple of small variations on the basic procedure need to be mentioned [1]: First, when the CRC is computed, the $M$ -bit register need not be initialized to zero.

Initializing it to some other $M$ -bit value (e.g., all 1’s) in effect prefaces all blocks by a phantom message that would have given the initialization value as its remainder. It is advantageous to do this, since the CRC described thus far otherwise cannot detect the addition or removal of any number of initial zero bits. (Loss of an initial bit, or insertion of zero bits, are common “clocking errors.”) Second, one can add (XOR) any $M$ -bit constant $K$ to the CRC before it is transmitted. This constant can either be XORed away at the receiving end, or else it just changes the expected CRC of the whole block by a known amount, namely the remainder of dividing $G$ into $K x ^ { M }$ . The constant $K$ is frequently “all bits,” changing the CRC into its ones complement. This has the advantage of detecting another kind of error that the CRC would otherwise not find: deletion of an initial 1 bit in the message with spurious insertion of a 1 bit at the end of the block.

The following object Icrc implements the calculation of 16-bit CRCs for the generators listed in the table. The constructor sets which generator is to be used, and also whether the initial register should be all bits (the default) or zero. Icrc is loosely based on the function in [2]. Here is how to understand its operation: First look at the function icrc1. This is used only by the constructor, to initialize a table of length 256, incorporating one character into a 16-bit CRC register. The only trick used is that a character’s bits are XORed into the most significant bits of the register, all eight together, instead of being fed into the least significant bit, one bit at a time, at the time of the register shift. This works because XOR is associative and commutative — we can feed in character bits any time before they will determine whether to zap with the generator polynomial.

Now look at the methods crc and concat. Go back to thinking about a character’s bits being shifted into the CRC register from the least significant end. The key observation is that while 8 bits are being shifted into the register’s low end, all the generator zapping is being determined by the bits already in the high end. Since XOR is commutative and associative, all we need is a table of the results of all this zapping, for each of 256 possible high-bit configurations. Then we can play catch-up and XOR an input character into the result of a lookup into this table. But this is exactly the table that was constructed by icrc1. References [2,4,5] give further details on table-driven CRC computations.

# struct Icrc {

Object for computing 16-bit cyclic redundancy checksums.

Uint jcrc,jfill,poly;   
static Uint icrctb[256];   
Icrc(const Int jpoly, const Bool fill $=$ true) : jfill(fill ? 255 : 0) {   
Constructor. Choose one of 8 generators (see table) by the value of jpoly. Initialize the   
CRC register to all bits if fill is true, otherwise to zero. Int j; Uint okpolys[8] $=$ {0x755B,0xA7D3,0x8005,0x1021,0x5935,0x90D9,0x5B93,0x2D17}; Generator polynomials, see table. poly $=$ okpolys[jpoly & 7]; for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<256; ${ \mathrm { j } } ^ { + + }$ ) { icrctb[j] $=$ icrc1(j << 8,0); Table of CRCs of all characters. jcrc $=$ (jfill | (jfill << 8));   
Uint crc(const string &bufptr) {   
Initialize the CRC register, compute and return the 16-bit CRC for the string bufptr. jcrc $=$ (jfill | (jfill $\ < < ~ 8 )$ ); return concat(bufptr);   
}

Uint concat(const string &bufptr) {

Without reinitializing the CRC register, compute and return the 16-bit CRC for the string bufptr. In effect, this appends bufptr to previous strings since the last call of crc and returns the overall CRC.

Uint j,cword=jcrc,len=bufptr.size();   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<len;j++) { Loop over the characters in the string. cword=icrctb[Uchar(bufptr[j]) ^ hibyte(cword)] ^ (lobyte(cword) << 8);   
return jcrc $=$ cword;

Uint icrc1(const Uint jcrc, const Uchar onech) {

Given a remainder up to now, return the new CRC after one character is added. Used by Icrc to initialize its table.

Int i;   
Uint ans ${ } = { }$ (jcrc ^ onech $\ < < ~ 8 )$ ;   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<8; $\dot { \bf 1 } + +$ ) { Here is where 8 one-bit shifts, and some XORs if (ans & 0x8000) ans $=$ (ans $\angle < = \ 1$ ) $\hat { }$ poly; with the generator polyelse ans $< < = ~ 1$ ; nomial, are done. ans $\& =$ 0xffff;   
}   
return ans;

inline Uchar lobyte(const unsigned short x) { return (Uchar) $( \mathbb { x }$ & 0xff); } inline Uchar hibyte(const unsigned short x) { return (Uchar)( $( \mathrm {  ~ x ~ } > > \mathrm {  ~ 8 ~ }$ ) & 0xff); } }; Uint Icrc::icrctb[256];

What if you need more than 16 bits of checksum? For a true 32-bit CRC, you will need to rewrite the routines given to work with a longer generating polynomial. For example, $x ^ { 3 2 } + x ^ { 7 } + x ^ { 5 } + x ^ { 3 } + x ^ { 2 } + x + 1$ is primitive modulo 2 and has nonleading, nonzero bits only in its least significant byte (which makes for some simplification). The idea of table lookup on only the most significant byte of the CRC register goes through unchanged.

Easier, if you don’t care about the $M$ -consecutive bit property of the checksum, is to just instantiate more than one copy of Icrc, each with a different generator (first argument in constructor). These provide statistically independent checks.

# 22.4.1 Other Kinds of Checksums

Quite different from CRCs are the various techniques used to append a decimal “check digit” to numbers that are handled by human beings (e.g., typed into a computer). Check digits need to be proof against the kinds of highly structured errors that humans tend to make, such as transposing consecutive digits. Wagner and Putter [6] give an interesting introduction to this subject, including specific algorithms.

Checksums now in widespread use vary from fair to poor. The 10-digit ISBN (International Standard Book Number) that you find on most books, including this

one, uses the check equation

$$
1 0 d _ { 1 } + 9 d _ { 2 } + 8 d _ { 3 } + \cdots + 2 d _ { 9 } + d _ { 1 0 } = 0 { \pmod { 1 1 } }
$$

where $d _ { 1 0 }$ is the right-hand check digit. The character “X” is used to represent a check digit value of 10. Another popular scheme is the so-called “IBM check,” often used for account numbers (including, e.g., MasterCard). Here, the check equation is

$$
2 \# d _ { 1 } + d _ { 2 } + 2 \# d _ { 3 } + d _ { 4 } + \cdots = 0 \pmod { 1 0 }
$$

where $2 \# d$ means, “multiply $d$ by two and add the resulting decimal digits.” United States banks code checks with a nine-digit processing number whose check equation is

$$
3 a _ { 1 } + 7 a _ { 2 } + a _ { 3 } + 3 a _ { 4 } + 7 a _ { 5 } + a _ { 6 } + 3 a _ { 7 } + 7 a _ { 8 } + a _ { 9 } = 0 { \pmod { 1 0 } }
$$

The familiar 12-digit Universal Product Code (UPC) is printed with both a decimal representation and a synonymous bar code. The digits are divided into a one-digit “category,” a five-digit manufacturer, a five-digit product identification, and one-digit checksum. The check equation is

$$
3 a _ { 1 } + a _ { 2 } + 3 a _ { 3 } + a _ { 4 } + 3 a _ { 5 } + \cdot \cdot \cdot + 3 a _ { 1 1 } + a _ { 1 2 } = 0 { \pmod { 1 0 } }
$$

The bar code put on many envelopes by the U.S. Postal Service is decoded by removing the single tall marker bars at each end and breaking the remaining bars into six or ten groups of five. In each group the five bars signify (from left to right) the values $7 , 4 , 2 , 1 , 0$ . Exactly two of them will be tall. Their sum is the represented digit, except that zero is represented as $7 + 4$ . The five- or nine-digit zip code is followed by a check digit, with the check equation

$$
\sum d _ { i } = 0 { \pmod { 1 0 } }
$$

None of these schemes is close to optimal. An elegant scheme due to Verhoeff is described in [6]. The underlying idea is to use the ten-element dihedral group $D _ { 5 }$ , which corresponds to the symmetries of a pentagon, instead of the cyclic group of the integers modulo 10. The check equation is

$$
a _ { 1 } * f ( a _ { 2 } ) * f ^ { 2 } ( a _ { 3 } ) * \cdots * f ^ { n - 1 } ( a _ { n } ) = 0
$$

where $^ *$ is (noncommutative) multiplication in $D _ { 5 }$ , and $f ^ { i }$ denotes the $i$ th iteration of a certain fixed permutation. Verhoeff’s method finds all single errors in a string, and all adjacent transpositions. It also finds about $9 5 \%$ of twin errors $( a a  b b$ ), jump transpositions $( a c b  b c a$ ), and jump twin errors $( a c a  b c b$ ). Here is an implementation:

# decchk.h

# Bool decchk(string str, char &ch) {

Decimal check digit computation or verification. Returns as ch a check digit for appending to string[0..n-1], that is, for storing into string[n]. In this mode, ignore the returned boolean value. If string[0..n-1] already ends with a check digit (string[n-1]), returns the function value true if the check digit is valid, otherwise false. In this mode, ignore the returned value of ch. Note that string and ch contain ASCII characters corresponding to the digits 0-9, not byte values in that range. Other ASCII characters are allowed in string, and are ignored in calculating the check digit.

char c;

Int j, $\mathtt { k } = 0$ , $\mathtt { m } = 0$ , $\mathbf { n } =$ str.length();   
static Int ip[10][8] $=$ {{0,1,5,8,9,4,2,7},{1,5,8,9,4,2,7,0}, {2,7,0,1,5,8,9,4},{3,6,3,6,3,6,3,6},{4,2,7,0,1,5,8,9}, {5,8,9,4,2,7,0,1},{6,3,6,3,6,3,6,3},{7,0,1,5,8,9,4,2}, {8,9,4,2,7,0,1,5},{9,4,2,7,0,1,5,8}};   
static Int ij[10][10] $=$ {{0,1,2,3,4,5,6,7,8,9},{1,2,3,4,0,6,7,8,9,5}, {2,3,4,0,1,7,8,9,5,6},{3,4,0,1,2,8,9,5,6,7},{4,0,1,2,3,9,5,6,7,8}, {5,9,8,7,6,0,4,3,2,1},{6,5,9,8,7,1,0,4,3,2},{7,6,5,9,8,2,1,0,4,3}, {8,7,6,5,9,3,2,1,0,4},{9,8,7,6,5,4,3,2,1,0}}; Group multiplication and permutation tables.   
for (j=0;j<n;j++) { Look at successive characters. c=str[j]; if (c >= 48 && $\mathrm { ~ c ~ } < = \ 5 7 .$ ) Ignore everything except digits. k=ij[k][ip[(c+2) % 10][7 & m++]];   
}   
for (j=0;j<10;j++) Find which appended digit will check proper if (ij[k][ip[j][m & 7]] $\scriptstyle = = 0$ ) break;   
ch=char $( \mathrm { j + 4 8 } )$ ; Convert to ASCII.   
return $\mathtt { k } = = 0$ ;

# CITED REFERENCES AND FURTHER READING:

Saadawi, T.N., and Ammar, M.H. 1994, Fundamentals of Telecommunication Networks (New York: Wiley).[1]   
LeVan, J. 1987, “A Fast CRC,” Byte, vol. 12, pp. 339–341 (November).[2]   
Koopman, P., and Chakravarty, T. 2004, “Cyclic Redundancy Code (CRC) Polynomial Selection for Embedded Networks,” in International Conference on Dependable Systems and Networks (DSN-2004) (IEEE Computer Society).[3]   
Sarwate, D.V. 1988, “Computation of Cyclic Redundancy Checks via Table Look-Up,” Communications of the ACM,vol.31,pp.1008-1013.[4]   
Griffiths, G., and Stones, G.C. 1987, “The Tea-Leaf Reader Algorithm: An Efficient Implementation of CRC-16 and CRC-32,” Communications of the ACM, vol. 30, pp. 617–620.[5]   
Wagner, N.R., and Putter, P.S. 1989, “Error Detecting Decimal Digits,” Communications of the ACM, vol. 32,pp. 106-110.[6]

# 22.5 Huffman Coding and Compression of Data

A lossless data compression algorithm takes a string of symbols (typically ASCII characters or bytes) and translates it reversibly into another string, one that is on the average of shorter length. The words “on the average” are crucial; it is obvious that no reversible algorithm can make all strings shorter — there just aren’t enough short strings to be in one-to-one correspondence with longer strings. Compression algorithms are possible only when, on the input side, some strings, or some input symbols, are more common than others. These can then be encoded in fewer bits than rarer input strings or symbols, giving a net average gain. We already quantified this idea, with the concept of entropy, in $\ S 1 4 . 7$ .

There exist many, quite different, compression techniques, corresponding to different ways of detecting and using departures from equiprobability in input strings.

In this section and the next we shall consider only variable length codes with defined word inputs. In these, the input is sliced into fixed units, for example ASCII characters, while the corresponding output comes in chunks of variable size. The simplest such method is Huffman coding [1], discussed in this section. Another example, arithmetic compression, is discussed in $\ S 2 2 . 6$ .

At the opposite extreme from defined-word, variable length codes are schemes that divide up the input into units of variable length (words or phrases of English text, for example) and then transmit these, often with a fixed length output code. The most widely used code of this general type is the Ziv-Lempel code [2]. References [3-5] give the flavor of some other compression techniques, with references to the large literature.

The idea behind Huffman coding is simply to use shorter bit patterns for more common characters. Suppose the input alphabet has $N _ { \mathrm { c h } }$ characters, and that these occur in the input string with respective probabilities $p _ { i } , i \ = \ 1 , . . . , N _ { \mathrm { c h } }$ , so that $\sum p _ { i } \ = \ 1$ . As we saw in $\ S 1 4 . 7$ , strings consisting of independently random sequences of these characters (a conservative, but not always realistic assumption) require, on the average, at least

$$
H = - \sum p _ { i } \log _ { 2 } p _ { i }
$$

bits per character, where $H$ is the entropy of the probability distribution. Moreover, coding schemes exist that approach the bound arbitrarily closely. For the case of equiprobable characters, with all $p _ { i } = 1 / N _ { \mathrm { c h } }$ , one easily sees that $H = \log _ { 2 } N _ { \mathrm { c h } }$ , which is the case of no compression at all. Any other set of $p _ { i }$ ’s gives a smaller entropy, allowing some useful compression.

Notice that the bound of (22.5.1) would be achieved if we could encode character $i$ with a code of length $L _ { i } = - \log _ { 2 } p _ { i }$ bits: Equation (22.5.1) would then be the average $\sum p _ { i } L _ { i }$ . The trouble with such a scheme is that $- \log _ { 2 } { p _ { i } }$ is not generally an integer. How can we encode the letter “Q” in 5.32 bits? Huffman coding makes a stab at this by, in effect, approximating all the probabilities $p _ { i }$ by integer powers of $1 / 2$ , so that all the $L _ { i }$ ’s are integral. If all the $p _ { i }$ ’s are in fact of this form, then a Huffman code does achieve the entropy bound $H$ .

The construction of a Huffman code is best illustrated by example. Imagine a language, Vowellish, with the $N _ { \mathrm { c h } } ~ = ~ 5$ character alphabet A, E, I, O, and U, occurring with the respective probabilities 0.12, 0.42, 0.09, 0.30, and 0.07. Then the construction of a Huffman code for Vowellish is accomplished in the table on the next page.

Here is how it works, proceeding in sequence through $N _ { \mathrm { c h } }$ stages, represented by the columns of the table. The first stage starts with $N _ { \mathrm { c h } }$ nodes, one for each letter of the alphabet, containing their respective relative frequencies. At each stage, the two smallest probabilities are found, summed to make a new node, and then dropped from the list of active nodes. (A “block” denotes the stage where a node is dropped.) All active nodes (including the new composite) are then carried over to the next stage (column). In the table, the names assigned to new nodes (e.g., AUI) are inconsequential. In the example shown, it happens that (after stage 1) the two smallest nodes are always an original node and a composite one; this need not be true in general: The two smallest probabilities might be both original nodes, or both composites, or one of each. At the last stage, all nodes will have been collected into one grand composite of total probability 1.

<table><tr><td>Node</td><td>Stage:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>A:</td><td>0.12</td><td>0.12</td><td></td><td></td><td></td></tr><tr><td>2</td><td>E:</td><td>0.42</td><td>0.42</td><td>0.42</td><td>0.42</td><td></td></tr><tr><td>3</td><td>I:</td><td>0.09</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>0:</td><td>0.30</td><td>0.30</td><td>0.30</td><td></td><td></td></tr><tr><td>5</td><td>U:</td><td>0.07</td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td>UI:</td><td>0.16</td><td></td><td></td><td></td></tr><tr><td>7</td><td></td><td></td><td>AUI:</td><td>0.28</td><td></td><td></td></tr><tr><td>8</td><td></td><td></td><td></td><td>AUIO:</td><td>0.58</td><td></td></tr><tr><td>9</td><td></td><td></td><td></td><td></td><td>EAUIO:</td><td>1.00</td></tr></table>

![](images/c0078414d512bc5f40346193df5316b60d06ed347e4db346cd96dd18b2e7850f.jpg)  
Figure 22.5.1. Huffman code for the fictitious language Vowellish, in tree form. A letter (A, E, I, O, or U) is encoded or decoded by traversing the tree from the top down; the code is the sequence of 0’s and 1’s on the branches. The value to the right of each node is its probability; to the left, its node number in the table.

Now, to see the code, you redraw the data in the table as a tree (Figure 22.5.1). As shown, each node of the tree corresponds to a node (row) in the table, indicated by the integer to its left and probability value to its right. Terminal nodes, so called, are shown as circles; these are single alphabetic characters. The branches of the tree are labeled 0 and 1. The code for a character is the sequence of zeros and ones that lead to it, from the top down. For example, E is simply 0, while U is 1010.

Any string of zeros and ones can now be decoded into an alphabetic sequence. Consider, for example, the string 1011111010. Starting at the top of the tree we descend through 1011 to I, the first character. Since we have reached a terminal node, we reset to the top of the tree, next descending through 11 to O. Finally 1010 gives U. The string thus decodes to IOU.

These ideas are embodied in the following Huffcode object. The constructor lets you specify $N _ { \mathrm { c h } }$ , and an integer frequency-of-occurrence table of length $N _ { \mathrm { c h } }$ telling how often each character occurs in some large corpus of text. These integers are, of course, proportional to the $p _ { i }$ ’s. The reason for using integers is so that any two computers will produce exactly the same code from the same input data. This might not be true if we used floating-point values. The constructor utilizes a heap structure (see $\ S 8 . 3 )$ for efficiency; for a detailed description, see Sedgewick [6].

Once you have created an instance of Huffcode, you code a message by calling codeone for each message character in turn. This writes bits into a byte array code that you supply as an argument. There is no message-dependent saved state, so you could interleave different messages if there were some reason to do so.

Decoding a Huffman-encoded message is slightly more complicated. The coding tree must be traversed from the top down, using up a variable number of bits. This is done by the method decodeone.

There is no such thing as an “end of message” (EOM) marker in Huffman codes not unless you provide one. Successive calls to decodeone will happily decode bits into characters until your hardware traps an illegal memory read! That is because every path on the tree (cf. Figure 22.5.1) terminates in a valid character. In practice, one increases $N _ { \mathrm { c h } }$ by 1, and gives the extra character a frequency of occurrence of 1 (versus large values for the other characters). The new character becomes the EOM marker. Similarly, one can add other extra characters for other “out-of-band” signaling. If these occur rarely, the overhead on the message is negligible.

# struct Huffcode {

Object for Huffman encoding and decoding.

Int nch,nodemax,mq;   
Int ilong,nlong;   
VecInt ncod,left,right;   
VecUint icod;   
Uint setbit[32];

Huffcode(const Int nnch, VecInt_I &nfreq) : nch(nnch), mq(2\*nch-1), icod(mq), ncod(mq), left(mq), right(mq) { Constructor. Given the frequency of occurrence table nfreq[0..nnch-1] for nnch characters, constructs the Huffman code. Also sets ilong and nlong as the character number that produced the longest code symbol, and the length of that symbol.

Int ibit,j,node,k,n,nused;   
VecInt index(mq), nprob(mq), up(mq);   
for ( $\scriptstyle \mathrm { i = 0 }$ ;j<32;j++) setbit[j] $= \ 1 \ < <$ j;   
for (nused ${ = } 0$ , $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<nch;j $^ { + + }$ ) { nprob[j] $=$ nfreq[j]; icod[j]=ncod[j] ${ = } 0$ ; if (nfreq[j] $! = ~ 0 ^ { \prime }$ ) index[nused++]=j;   
}   
for (j=nused-1;j> ${ = } 0$ ;j--) Sort nprob into a heap structure in index. heep(index,nprob,nused,j);   
$\mathtt { k } =$ nch;   
while (nused $> ~ 1$ ) { Combine heap nodes, remaking the heap at node $=$ index[0]; each stage. index[0] $=$ index[(nused--)-1]; heep(index,nprob,nused,0); nprob[k] $=$ nprob[index[0]]+nprob[node]; left[k] $=$ node; Store left and right children of a node. right[k++] $=$ index[0]; up[index[0]] $=$ -Int(k); Indicate whether a node is a left or right index[0]=k-1; of its parent. up[node] ${ \tt = } \tt k$ ; heep(index,nprob,nused,0);   
up[(nodemax $\scriptstyle = \mathbf { k }$ )-1] ${ = } 0$ ;   
for ( $\scriptstyle \mathbf { j } = 0$ ;j<nch; $\mid + +$ ) { Make the Huffman code from the tree. if (nprob[j] $! = ~ 0 ^ { \cdot }$ ) { for ( $\scriptstyle \mathtt { n } = 0$ ,ibit ${ = } 0$ ,node $=$ up[j];node;node=up[node-1],ibit++) { if (node $\mathit { \Theta } < \mathit { \Theta } 0 \mathit { \Theta }$ ) { n $| =$ setbit[ibit]; node $=$ -node; } } icod[j] $= \mathbf { n }$ ; ncod[j] $=$ ibit; }   
}   
nlong $_ { = 0 }$ ;   
for (j=0;j<nch;j++) { if (ncod[j] $>$ nlong) nlong=ncod[j]; ilong=j; }   
}   
if (nlong $>$ numeric_limits<Uint>::digits) throw("Code too long in Huffcode. See text.");

void codeone(const Int ich, char \*code, Int &nb) {

Huffman encode the single character ich (in the range 0..nch-1), write the result to the byte array code starting at bit nb (whose smallest valid value is zero), and increment nb to the first unused bit. This routine is called repeatedly to encode consecutive characters in a message. The user is responsible for monitoring that the value of nb does not overrun the length of code.

Int m,n,nc; if (ich $> =$ nch) throw("bad ich (out of range) in Huffcode"); if (ncod[ich] $\scriptstyle = = 0$ ) throw("bad ich (zero prob) in Huffcode"); for ( $\mathtt { n } =$ ncod[ich]-1;n >= 0;n--,++nb) { Loop over the bits in the stored nc=nb $\ b > 3$ ; Huffman code for ich. m=nb & 7; if $\mathbf { \Omega } _ { \mathrm { ~ m ~ } } = = \mathbf { \Omega } 0$ ) code[nc] ${ = } 0$ ; Set appropriate bits in code. if ((icod[ich] & setbit[n]) $! = ~ 0 ^ { \prime }$ ) code[nc] $| =$ setbit[m]; } }

# Int decodeone(char \*code, Int &nb) {

Starting at bit number nb in the byte array code, decode a single character (returned as ich in the range 0..nch-1) and increment nb appropriately. Repeated calls, starting with $\mathtt { n b } = 0$ , will return successive characters in a compressed message. The user is responsible for detecting EOM from the message content.

Int nc;   
Int node=nodemax-1;   
for (;;) { Set node to the top of the decoding tree, and nc=nb >> 3; loop until a valid character is obtained. node $=$ ((code[nc] & setbit[7 & nb++]) $\smash { ! = \begin{array} { l l } { 0 } & { ? } \end{array} }$ right[node] : left[node]); Branch left or right in tree, depending on its value. if (node $<$ nch) return node; If we reach a terminal node, we have a com-  
} plete character and can return.

void heep(VecInt_IO &index, VecInt_IO &nprob, const Int n, const Int m) { Used by the constructor to maintain a heap structure in the array index[0..m-1].

Int $\dot { \mathtt { 1 } } = \mathtt { m }$ ,j,k;$\mathtt { k } =$ index[i];while (i < $\mathrm { ~ ( ~ n ~ } > > \ 1 )$ ) {if $( ( \ j \ = \ 2 * \ i + 1 ) \ < \ \mathtt { n } - 1$ && nprob[index[j]] $>$ nprob[index[j+1]]) j++;if (nprob[k] $< =$ nprob[index[j]]) break;index[i] $=$ index[j];i=j;}index[i] ${ \tt = } \tt k$ ;}};

Huffcode requires that the longest code for a single character fits into your machine’s integer wordlength (typically 32 bits), and will tell you if this is violated. If this happens, you’ll need to increase the frequency-of-occurrence value for the rarest characters. This will affect your compression hardly at all.

It is a feature, not a bug, that Huffcode allows you to specify some characters as having zero frequency of occurrence, and then completely omits these from the code. This can be very useful when, for example, you want to compress a file consisting only of ASCII characters $0 { - } 9 , + , - ,$ , and “.”, as might occur in a file of numerical values. But don’t then try to encode one of the omitted characters!

# 22.5.1 Run-Length Encoding

For the compression of highly correlated bit streams (for example the black or white values along a facsimile scan line), Huffman compression is often combined with run-length encoding: Instead of sending each bit, the input stream is converted to a series of integers indicating how many consecutive bits have the same value. These integers are then Huffman-compressed. The Group 3 CCITT facsimile standard functions in this manner, with a fixed, immutable, Huffman code, optimized for a set of eight standard documents [7].

# CITED REFERENCES AND FURTHER READING:

Hamming, R.W. 1980, Coding and Information Theory (Englewood Cliffs, NJ: Prentice-Hall).   
Huffman, D.A. 1952, “A Method for the Construction of Minimum-Redundancy Codes,” Proceedings of the Institute of Radio Engineers,vol.40,pp.1098-1101.[1]   
Ziv, J., and Lempel, A. 1978, “Compression of Individual Sequences via Variable-Rate Coding,” IEEE Transactions on Information Theory,vol. IT-24,pp.530-536.[2]   
Sayood, K. 2005, Introduction to Data Compression, 3rd ed. (San Francisco: Morgan Kaufmann).[3]   
Salomon, D. 2004, Data Compression: The Complete Reference, 3rd ed. (New York: Springer).[4]   
Wayner, P. 1999, Compression Algorithms for Real Programmers (San Francisco: Morgan Kaufmann).[5]   
Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapter 22.[6]   
Hunter, R., and Robinson, A.H. 1980, “International Digital Facsimile Coding Standard,” Proceedings of the IEEE,vol. 68, pp.854-867.[7]

# 22.6 Arithmetic Coding

We saw in the previous section, as well as $\ S 1 4 . 7$ , that a perfect coding scheme would use $L _ { i } = - \log _ { 2 } p _ { i }$ bits to encode character $i$ (in the range $1 \leq i \leq N _ { \mathrm { c h } } )$ , if $p _ { i }$ is its probability of occurrence and characters occur independently randomly. Huffman coding gives a way of rounding the $L _ { i }$ ’s to close integer values and constructing a code with those lengths. Arithmetic coding [1], which we now discuss, actually does manage to encode characters using noninteger numbers of bits! It also provides a convenient way to output the result not as a stream of bits, but as a stream of symbols in any desired radix. This latter property is particularly useful if you want, e.g., to convert data from bytes (radix 256) to printable ASCII characters (radix 94), or to case-independent alphanumeric sequences containing only A-Z and 0-9 (radix 36).

In arithmetic coding, an input message of any length is represented as a real number $R$ in the range $0 \leq R < 1$ . The longer the message, the more precision required of $R$ . This is best illustrated by an example, so let us return to the fictitious language, Vowellish, of the previous section. Recall that Vowellish has a five-character alphabet (A, E, I, O, U), with occurrence probabilities 0.12, 0.42, 0.09, 0.30, and 0.07, respectively. Figure 22.6.1 shows how a message beginning “IOU” is encoded: The interval $[ 0 , 1 )$ is divided into segments corresponding to the five alphabetical characters; the length of a segment is the corresponding $p _ { i }$ . We see that the first message character, “I”, narrows the range of $R$ to $0 . 3 7 \leq R < 0 . 4 6$ . This interval is now subdivided into five subintervals, again with lengths proportional to the $p _ { i }$ ’s. The second message character, “O”, narrows the range of $R$ to $0 . 3 7 6 3 \le R < 0 . 4 0 3 3$ . The “U” character further narrows the range to $0 . 3 7 6 3 0 \leq R < 0 . 3 7 8 1 9$ Any value of $R$ in this range can be sent as encoding “IOU”. In particular, the binary fraction :011000001 is in this range, so “IOU” can be sent in 9 bits. (Huffman coding took 10 bits for this example; see $\ S 2 2 . 5 . \ O$ )

Of course there is the problem of knowing when to stop decoding. The fraction :011000001 represents not simply “IOU,” but “IOU. . . ,” where the ellipses represent an infinite string of successor characters. We had a similar problem in Huffman coding, but there we would at least stop when we ran off the edge of the input buffer. Here, the real number :011000001 actually does represent an infinite message! Arithmetic coding therefore always must assume the existence of a special $N _ { \mathrm { c h } } + 1 \mathrm { s t }$ character, EOM (end of message), which occurs only once at the end of the input. Since EOM has a low probability of occurrence, it gets allocated only a very tiny piece of the number line.

In the above example, we gave $R$ as a binary fraction. We could just as well have output it in any other radix, e.g., base 94 or base 36, whatever is convenient for the anticipated storage or communication channel.

You might wonder how one deals with the seemingly incredible precision required of $R$ for a long message. The answer is that $R$ is never actually represented all at once. At any give stage we have upper and lower bounds for $R$ represented as a finite number of digits in the output radix. As digits of the upper and lower bounds become identical, we can left-shift them away and bring in new digits at the lowsignificance end. The object below has a parameter NWK for the number of working digits to keep around. This must be large enough to make the chance of an accidental degeneracy vanishingly small. (The object signals if a degeneracy ever occurs.)

![](images/21c608b485877440122b9bf1303442a638514f9a9b493f9cc914f619a66d5d64.jpg)  
Figure 22.6.1. Arithmetic coding of the message “IOU...” in the fictitious language Vowellish. Successive characters give successively finer subdivisions of the initial interval between 0 and 1. The final value can be output as the digits of a fraction in any desired radix. Note how the subinterval allocated to a character is proportional to its probability of occurrence.

Since the process of discarding old digits and bringing in new ones is performed identically on encoding and decoding, everything stays synchronized.

In the Arithcode object below, the constructor has arguments to specify the number of characters and an integer frequency-of-occurrence table (as in Huffcode), plus an argument that allows you to specify an output radix for the code. Because there is some saved state between coding successive characters (the upper and lower bounds for $R$ , for example), you must call messageinit prior to encoding or decoding the first character of a new message, and not interleave the encoding of different messages in a single instance of Arithcode. If you want to interleave messages, create more than one instance.

Successive calls to codeone for each input character encode the message. A final call with character nch (that is, one larger than your specified character set) adds the EOM marker and is mandatory. After this final call, lcd will be set to the number of bytes in the coded message (i.e., will point to the first unused location in code). The decodeone routine similarly returns successive characters of the decoded message in turn, with nch returned to indicate EOM.

Unlike the Huffcode object, Arithcode has no provision for omitting specified message characters from the code. Therefore, it also refuses to believe zero values in the table nfreq; a 0 is treated as if it were a 1. If you want to live dangerously, with a very slightly more efficient coding, you can change this in the constructor.

# struct Arithcode {

Object for arithmetic coding.

Int nch,nrad,ncum;   
Uint jdif,nc,minint;   
VecUint ilob,iupb;   
VecInt ncumfq;   
static const Int NWK $:$ 20;

Arithcode(VecInt_I &nfreq, const Int nnch, const Int nnrad) : nch(nnch), nrad(nnrad), ilob(NWK), iupb(NWK), ncumfq(nch+2) { Constructor. Given the frequency of occurrence table nfreq[0..nnch-1] for nnch characters, constructs the Huffman code whose output has radix nnrad (which must be $\leq 2 5 6$ ).

# Int j;

if (nrad $>$ 256) throw("output radix must be $< =$ 256 in Arithcode");   
minint $=$ numeric_limits<Uint>::max()/nrad;   
ncumfq $[ 0 ] = 0$ ;   
for ( $\scriptstyle { \dot { \mathbf { J } } } = 1$ ;j<=nch;j++) ncumfq[j] $=$ ncumfq[j-1]+MAX(nfreq[j-1],1);   
ncum ncumfq[nch $^ +$ 1] $=$ ncumfq[nch] $+ 1$ ;

# void messageinit() {

Clear saved state for a new message (either encode or decode). This is mandatory before encoding or decoding the first character.

Int j;   
jdif=nrad-1;   
for (j=NWK-1;j> ${ \tt > } = 0$ ;j--) { Initialize enough digits of the upper and lower iupb[j] $=$ nrad-1; bounds. ilob[j]=0; nc=j; if (jdif $>$ minint) return; Initialization complete. jdif ${ } = { }$ (jdif+1)\*nrad-1;   
}   
throw("NWK too small in arcode.");

oid codeone(const Int ich, char \*code, Int &lcd) {

Encode the single character ich in the range 0 : : : nch-1 into the byte array code, starting at location code[lcd] and (if necessary) incrementing lcd so that, on return, it points to the first unused byte in code. A final call with ich $\cdot ^ { = }$ nch encodes “end of message.” Byte values written into code will be in the range 0 : : : nrad  1.

if (ich $>$ nch) throw("bad ich in Arithcode");   
advance(ich,code,lcd,1);

Check for valid input character.

# }

# Int decodeone(char \*code, Int &lcd) {

Decode and return a single message character, using code starting at location code[lcd], and (if necessary) increment lcd appropriately. Successive calls return successive message characters. The returned value nch indicates end of message (subsequent calls will return nonsense).

Int ich;   
Uint j,ihi,ja,m;   
$\mathtt { j a } =$ (Uchar) code[lcd]-ilob[nc];   
for (j=nc+1;j<NWK;j++) { ja $\ast =$ nrad; ja $+ =$ Uchar(code[lcd+j-nc])-ilob[j];   
}   
ihi=nch+1;   
ich $_ { = 0 }$ ;   
while (ihi-ich $>$ 1) { If decoding, locate the character ich by bisection.

$\mathbb { m } =$ (ich+ihi)>>1; if (ja $> =$ multdiv(jdif,ncumfq[m],ncum)) ich=m; else ihi $= \mathtt { m }$ ; } if (ich $\ ! =$ nch) advance(ich,code,lcd,-1); return ich; }

void advance(const Int ich, char \*code, Int &lcd, const Int isign) { Used internally. Operations common to encoding and decoding. Convert character ich to a new subrange [ilob,iupb).

Uint j,k,jh,jl;   
jh=multdiv(jdif,ncumfq[ich+1],ncum);   
jl=multdiv(jdif,ncumfq[ich],ncum);   
jdif=jh-jl;   
arrsum(ilob,iupb,jh,NWK,nrad,nc);   
arrsum(ilob,ilob,jl,NWK,nrad,nc);   
for (j=nc;j<NWK;j++) { How many leading digits to output (if enif (ich $\ ! =$ nch && iupb[j] $\ ! =$ ilob[j]) break; coding) or skip over? if (isign $> 0 \dot { . }$ ) code[lcd] $=$ ilob[j]; lcd++;   
}   
if (j+1 $>$ NWK) return; Ran out of message. Did someone forget to   
nc=j; encode a terminating ncd?   
for(j=0;jdif<minint;j++) How many digits to shift? jdif $\ast =$ nrad;   
if (j $>$ nc) throw("NWK too small in arcode.");   
if (j $! = ~ 0 ^ { \prime }$ ) Shift them. for (k=nc;k<NWK;k++) { iupb[k-j] $=$ iupb[k]; ilob[k-j] $=$ ilob[k]; }   
nc $\mathrm { ~ -- ~ } \mathrm { ~ j ~ }$ ;   
for ( $\mathbf { k } =$ NWK-j;k<NWK;k++) iupb[k] $=$ ilob[k]=0;   
return; Normal return.

inline Uint multdiv(const Uint j, const Uint k, const Uint m) { Calculate $( \mathtt { k } { * } \mathtt { j } ) / \mathtt { m }$ without overflow by use of double-length integers. return Uint((Ullong(j)\*Ullong(k)/Ullong(m))); }

void arrsum(VecUint_I &iin, VecUint_O &iout, Uint ja,   
const Int nwk, const Uint nrad, const Uint nc) {   
Add the integer ja to the radix nrad multiple-precision integer iin[nc..nwk-1]. Return the result in iout[nc..nwk-1].

Uint karry ${ = } 0$ ,j,jtmp; for (j=nwk-1;j>nc;j--) { jtmp=ja; ja /= nrad; iout[j]=iin[j]+(jtmp-ja\*nrad)+karry; if (iout[j] $> =$ nrad) { iout[j] $- =$ nrad; karry=1; } else karry ${ \tt = } 0$ ; iout[nc]=iin[nc]+ja+karry; };

A few further notes: When an interval of size jdif is to be partitioned in the proportions of some n to some ntot, say, then we must compute (n\*jdif)/ntot.

With ordinary integer arithmetic, the numerator is likely to overflow; and, unfortunately, an expression like jdif/(ntot/n) is not equivalent. We therefore need to use double-length integers, type Ullong, usually 64 bits, just for this operation.

The internally set variable minint, which is the minimum allowed number of discrete steps between the upper and lower bounds, determines when new lowsignificance digits are added. minint must be large enough to provide resolution of all the input characters. That is, we must have $p _ { i } \ \times \mathrm { m i n i n t } \ > \ 1$ for all $i$ . A value of $1 0 0 N _ { \mathrm { c h } }$ , or $1 . 1 / \operatorname* { m i n } p _ { i }$ , whichever is larger, is generally adequate. However, for safety, the routine takes minint to be as large as possible, with the product minint\*nradd just smaller than overflow. This results in some time inefficiency, and in a few unnecessary characters being output at the end of a message. You can decrease minint if you want to live closer to the edge.

If radix-changing, rather than compression, is your primary aim (for example to convert an arbitrary file into printable characters), then you are of course free to set all the components of nfreq equal, say, to 1.

While the output radix is limited to 256 (so that values fit into a byte), the input alphabet size $N _ { \mathrm { c h } } =$ nch can be less than, equal to, or greater than 256.

# CITED REFERENCES AND FURTHER READING:

Sayood, K. 2005, Introduction to Data Compression, 3rd ed. (San Francisco: Morgan Kaufmann).   
Salomon, D. 2004, Data Compression: The Complete Reference, 3rd ed. (New York: Springer).   
Wayner, P. 1999, Compression Algorithms for Real Programmers (San Francisco: Morgan Kaufmann).   
Witten, I.H., Neal, R.M., and Cleary, J.G. 1987, “Arithmetic Coding for Data Compression,” Communications of the ACM,vol.30,pp. 520-540.[1]

# 22.7 Arithmetic at Arbitrary Precision

Let’s compute the number $\pi$ to a couple of thousand decimal places. In doing so, we’ll learn some things about multiple precision arithmetic on computers and meet quite an unusual application of the fast Fourier transform (FFT). We’ll also develop a set of routines that you can use for other calculations at any desired level of arithmetic precision.

To start with, we need an analytic algorithm for $\pi$ . Useful algorithms are quadratically convergent, i.e., they double the number of significant digits at each iteration. Quadratically convergent algorithms for $\pi$ are based on the AGM (arithmetic geometric mean) method, which also finds application to the calculation of elliptic integrals (cf. $\ S 6 . 1 2 )$ and in advanced implementations of the ADI method for elliptic partial differential equations (-20.5). Borwein and Borwein [1] treat this subject, which is beyond our scope here. One of their algorithms for $\pi$ starts with the initializations

$$
\begin{array} { l } { { X _ { 0 } = \sqrt { 2 } } } \\ { { \pi _ { 0 } = 2 + \sqrt { 2 } } } \\ { { { Y _ { 0 } = \sqrt [ 4 ] { 2 } } } } \end{array}
$$

and then, for $i = 0 , 1 , \ldots$ , repeats the iteration

$$
\begin{array} { l c r } { \displaystyle { X _ { i + 1 } = \frac { 1 } { 2 } \left( \sqrt { X _ { i } } + \frac { 1 } { \sqrt { X _ { i } } } \right) } } \\ { \displaystyle { \pi _ { i + 1 } = \pi _ { i } \left( \frac { X _ { i + 1 } + 1 } { Y _ { i } + 1 } \right) } } \\ { \displaystyle { Y _ { i + 1 } = \frac { Y _ { i } \sqrt { X _ { i + 1 } } + \frac { 1 } { \sqrt { X _ { i + 1 } } } } { Y _ { i } + 1 } } } \end{array}
$$

The value $\pi$ emerges as the limit $\pi _ { \infty }$

Now to the question of how to do arithmetic to arbitrary precision: In a highlevel language like $\mathrm { C } { + + }$ , a natural choice is to work in radix (base) 256, so that character arrays can be directly interpreted as strings of digits. At the very end of our calculation, we will want to convert our answer to radix 10, but that is essentially a frill for the benefit of human ears, accustomed to the familiar chant, “three point one four one five nine. . . .” For any less frivolous calculation, we would likely never leave base 256 (or the thence trivially reachable hexadecimal, octal, or binary bases).

We will adopt the convention of storing digit strings in the “human” ordering, that is, with the first stored digit in an array being most significant, the last stored digit being least significant. The opposite convention would, of course, also be possible. “Carries,” where we need to partition a number larger than 255 into a low-order byte and a high-order carry, present a minor programming annoyance, solved, in the routines below, by the use of the functions lobyte and hibyte. It will be our usual convention to assume that the digit strings represent floating-point numbers with the radix point falling after the the first digit. When an operation results in a number that requires more digits in front of the decimal point, it is the responsibility of the user to shift the digits to the right and keep track of any excess factors of 256 that this implies.

It is easy at this point, following Knuth [2], to write a routines for the “fast” arithmetic operations: short addition (adding a single byte to a string), addition, subtraction, short multiplication (multiplying a string by a single byte), short division, ones-complement negation, and a couple of utility operations, copying and left-shifting strings. These are implemented in the following MParith object. The additional routines that are declared, but not defined, are discussed below.

# struct MParith {

Multiple precision arithmetic operations done on character strings, interpreted as radix 256 numbers with the radix point after the first digit. Implementations for the simpler operations are listed here.

void mpadd(VecUchar_O &w, VecUchar_I &u, VecUchar_I &v) {

Adds the unsigned radix 256 numbers u and v, yielding the unsigned result w. To achieve the full available accuracy, the array w must be longer, by one element, than the shorter of the two arrays u and v.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { m } = \mathtt { v }$ .size(), $\mathtt { p - w }$ .size();   
Int n_min $\ c =$ MIN(n,m),p_min $\boldsymbol { \cdot }$ MIN(n_min,p-1);   
Uint ireg ${ \left. \sum 0 \right. }$ ;   
for (j=p_min-1;j>=0;j--) { ireg=u[j]+v[j]+hibyte(ireg); w[j+1]=lobyte(ireg);   
}   
w[0]=hibyte(ireg);   
if (p > p_min $+ 1$ )

for (j=p_min+1;j<p;j++) w[j] ${ = } 0$ ;

# }

void mpsub(Int &is, VecUchar_O &w, VecUchar_I &u, VecUchar_I &v) {

Subtracts the unsigned radix 256 number v from u yielding the unsigned result w. If the result is negative (wraps around), is is returned as $^ { - 1 }$ ; otherwise it is returned as 0. To achieve the full available accuracy, the array $\mathtt { w }$ must be as long as the shorter of the two arrays u and v.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathrm { m } { = } \mathrm { v }$ .size(), $\mathtt { p - w }$ .size();   
Int n_min $\ c =$ MIN(n,m),p_min $\downharpoonleft$ MIN(n_min,p-1);   
Uint ireg=256;   
for (j=p_min-1;j>=0;j--) { ireg=255+u[j]-v[j]+hibyte(ireg); w[j] $=$ lobyte(ireg);   
}   
is=hibyte(ireg)-1;   
if (p > p_min) for (j=p_min;j<p;j++) w[j] ${ = } 0$ ;

oid mpsad(VecUchar_O &w, VecUchar_I &u, const Int iv) {

Short addition: The integer iv (in the range $\begin{array} { r } { 0 \leq \mathrm { i v } \leq 2 5 5 } \end{array}$ ) is added to the least significant radix position of unsigned radix 256 number u, yielding result $\mathtt { w }$ . To ensure that the result does not require two digits before the radix point, one may first right-shift the operand u so that the first digit is 0, and keep track of multiples of 256 separately.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { p - w }$ .size();   
Uint ireg=256\*iv;   
for (j=n-1; $\scriptstyle { \dot { \mathsf { J } } } > = 0$ ;j--) { ireg=u[j]+hibyte(ireg); if (j+1 < p) w[j+1] $=$ lobyte(ireg);   
}   
w[0]=hibyte(ireg);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = { \mathsf { n } } + 1$ ;j<p;j $^ { + + }$ ) w[j] ${ = } 0$ ;

void mpsmu(VecUchar_O &w, VecUchar_I &u, const Int iv) {

Short multiplication: The unsigned radix 256 number u is multiplied by the integer iv (in the range $\begin{array} { r } { 0 \leq \mathtt { i v } \leq 2 5 5 , } \end{array}$ ), yielding result w. To ensure that the result does not require two digits before the radix point, one may first right-shift the operand u so that the first digit is 0, and keep track of multiples of 256 separately.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { p - w }$ .size();   
Uint ireg=0;   
for $\scriptstyle \ j = \mathtt { n } - 1$ ; $\scriptstyle { \dot { \mathcal { I } } } > = 0$ ;j--) { ireg=u[j]\*iv+hibyte(ireg); if (j < p-1) w[j+1] $=$ lobyte(ireg);   
  
w[0] $=$ hibyte(ireg);   
for ( $\scriptstyle { \dot { \mathbf { J } } } = { \mathbf { n } } + 1$ ;j<p;j++) w[j] ${ = } 0$ ;

void mpsdv(VecUchar_O &w, VecUchar_I &u, const Int iv, Int &ir) {

Short division: The unsigned radix 256 number u is divided by the integer iv (in the range $\mathbf { 0 } \leq \mathrm { i v } \leq 2 5 5$ ), yielding a quotient w and a remainder ir (with ${ \mathbf { 0 } } \leq \mathrm { i } { \mathbf { r } } \leq 2 5 5$ ). To achieve the full available accuracy, the array w must be as long as the array u.

Int i,j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { p - w }$ .size(),p_min=MIN(n,p);   
$\scriptstyle { \dot { \mathtt { 1 } } } \mathbf { r } = 0$ ;   
for (j=0;j<p_min;j $^ { + + }$ ) { i=256\*ir+u[j]; w[j]=Uchar(i/iv); ir=i % iv;   
}   
if (p > p_min) for (j=p_min;j<p;j++) w[j] ${ = } 0$ ;   
void mpneg(VecUchar_IO &u) {   
Ones-complement negate the unsigned radix 256 number u. Int j, $\mathbf { n } { = } \mathbf { u }$ .size(); Uint ireg=256; for ( $\dot { \mathsf { J } } = \mathtt { n } - \dot { \mathsf { 1 } }$ 1; $\scriptstyle { \dot { \mathsf { J } } } > = 0$ ;j--) { ireg=255-u[j]+hibyte(ireg); u[j] $= 1$ lobyte(ireg); }   
} void mpmov(VecUchar_O &u, VecUchar_I &v) {   
Move the unsigned radix 256 number v into u. To achieve full accuracy, the array $\mathtt { v }$ must be as long as the array u.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { m } = \mathtt { v }$ .size(),n_min=MIN(n,m); for (j $_ { | = 0 }$ ;j<n_min;j++) u[j] $= \tt v$ [j]; if (n $>$ n_min) for(j=n_min;j<n-1;j++) u[j] ${ = } 0$ ;

# }

void mplsh(VecUchar_IO &u) { Left-shift digits of unsigned radix 256 number u. The final element of the array is set to 0.

Int j, $\mathrm { n } { = } \mathrm { u }$ .size();   
for ( $\scriptstyle \mathbf { j } = 0$ ;j<n-1;j++) u[j] $= \mathrm { u }$ [j+1];   
u[n-1] ${ = } 0$ ;

# }

Uchar lobyte(Uint x) {return (x & 0xff);} Uchar hibyte(Uint x) {return ( $( \mathrm {  ~ x ~ } > > \mathrm {  ~ 8 ~ }$ ) & 0xff);}

The following, more complicated, methods have discussion and implementation below.

void mpmul(VecUchar_O &w, VecUchar_I &u, VecUchar_I &v);   
void mpinv(VecUchar_O &u, VecUchar_I &v);   
void mpdiv(VecUchar_O &q, VecUchar_O &r, VecUchar_I &u, VecUchar_I &v);   
void mpsqrt(VecUchar_O &w, VecUchar_O &u, VecUchar_I &v);   
void mp2dfr(VecUchar_IO &a, string &s);   
string mppi(const Int np);

};

Full multiplication of two strings of digits, if done by the traditional hand method, is not a fast operation: In multiplying two strings of length $N$ , the multiplicand would be short-multiplied in turn by each byte of the multiplier, requiring $O ( N ^ { 2 } )$ operations in all. We will see, however, that all the arithmetic operations on numbers of length $N$ can in fact be done in $O ( N \times \log N \times \log \log N )$ operations.

The trick is to recognize that multiplication is essentially a convolution (-13.1) of the digits of the multiplicand and multiplier, followed by some kind of carry operation. Consider, for example, two ways of writing the calculation $4 5 6 \times 7 8 9$ :

<table><tr><td colspan="2">456 ×789</td><td>×</td><td>4 7</td><td>5 8</td><td>9</td></tr><tr><td colspan="2">4104</td><td></td><td></td><td>36 45 54</td><td></td></tr><tr><td colspan="2">3648</td><td>32</td><td></td><td>4048</td><td></td></tr><tr><td colspan="2">3192 359784</td><td>2835</td><td>42</td><td></td><td></td></tr><tr><td colspan="2"></td><td>28 67 359</td><td>118</td><td>93 54</td><td>784</td></tr></table>

The tableau on the left shows the conventional method of multiplication, in which three separate short multiplications of the full multiplicand (by 9, 8, and 7) are added to obtain the final result. The tableau on the right shows a different method (sometimes taught for mental arithmetic), where the single-digit cross products are all computed (e.g. $8 \times 6 = 4 8$ ), then added in columns to obtain an incompletely carried result (here, the list 28; 67; 118; 93; 54). The final step is a single pass from right to left, recording the single least-significant digit and carrying the higher digit or digits into the total to the left (e.g. $9 3 + 5 = 9 8$ , record the 8, carry 9).

You can see immediately that the column sums in the right-hand method are components of the convolution of the digit strings, for example $1 1 8 = 4 \times 9 + 5 \times$ $8 + 6 \times 7$ . In $\ S 1 3 . 1$ , we learned how to compute the convolution of two vectors by the fast Fourier transform (FFT): Each vector is FFT’d, the two complex transforms are multiplied, and the result is inverse-FFT’d. Since the transforms are done with floating arithmetic, we need sufficient precision so that the exact integer value of each component of the result is discernible in the presence of roundoff error. We should therefore allow a (conservative) few times $\log _ { 2 } ( \log _ { 2 } N )$ bits for roundoff in the FFT. A number of length $N$ bytes in radix 256 can generate convolution components as large as the order of $( 2 5 6 ) ^ { 2 } N$ , thus requiring $1 6 + \log _ { 2 } N$ bits of precision for exact storage. If it is the number of bits in the floating mantissa (cf. -22.2), we obtain the condition

$$
1 6 + \log _ { 2 } { N } + \mathrm { f e w } \times \log _ { 2 } { \log _ { 2 } { N } } < \mathrm { i t }
$$

We see that single precision, say with $\mathrm { i t } = 2 4$ , is inadequate for any interesting value of $N$ , while double precision, say with $\mathrm { i t } \ = \ 5 3$ , allows $N$ to be greater than $1 0 ^ { 6 }$ , corresponding to some millions of decimal digits. The use of Doub in the routines realft (-12.3) and four1 (-12.2) is therefore a necessity, not merely a convenience, for this application.

void MParith::mpmul(VecUchar_O &w, VecUchar_I &u, VecUchar_I &v) { Uses fast Fourier transform to multiply the unsigned radix 256 integers u[0..n-1] and $\mathtt { v } \left[ 0 \dots \dots \dots 1 \right]$ , yielding a product $\mathtt { w } [ 0 \rVert \cdot \mathtt { \sigma } \mathtt { \cdot n } \mathtt { + m } \mathtt { - } 1 ]$ .

const Doub RX $\equiv$ 256.0;   
Int j, $\mathrm { n n } { = } 1$ , $\mathbf { n } { = } \mathbf { u }$ .size(), ${ \mathfrak { m } } { = } \mathfrak { v }$ .size(), $\mathtt { p - w }$ .size(),n_max=MAX(m,n);   
Doub cy,t;   
while ( $\ln \mathrm { ~ < ~ } \mathrm { n } _ { - } \mathrm { m a x } ) \mathrm { n n ~ } < < = \mathrm { ~ 1 } ;$ Find the smallest usable power of 2 for the transform. nn $< < = ~ 1$ ;   
VecDoub a(nn,0.0),b(nn,0.0);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j $^ { + + }$ ) a[j] ${ \bf \varepsilon } = { \bf u }$ [j]; Move $U$ and $V$ to double precision floating arrays. for ( $\scriptstyle \mathrm { j = 0 }$ ;j<m;j++) b[j] $= \tt v$ [j];   
realft(a,1); Perform the convolution: First, the two Fourier transrealft(b,1); forms.   
b[0] $\ast = \mathrm { ~ a ~ } [ 0 ]$ ; Then multiply the complex results (real and imagib[1] $\ast =$ a[1]; nary parts).   
for ( $\scriptstyle \mathbf { j } = 2$ ;j<nn;j $+ { = } 2$ ) {   
b[j] $=$ (t=b[j])\*a[j]-b[j+1]\*a[j+1];   
b[j+1]=t\*a[j+1]+b[j+1]\*a[j];   
}   
realft(b,-1); Then do the inverse Fourier transform.   
$\mathtt { c y = 0 . 0 }$ ; Make a final pass to do all the carries.   
for (j=nn-1;j>=0;j--) {   
t=b[j]/(nn >> 1)+cy+0.5; The 0.5 allows for roundoff error.   
cy=Uint(t/RX);   
b[j]=t-cy\*RX;   
}   
if (cy $> =$ RX) throw("cannot happen in mpmul");   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<p;j++) w[j] ${ = } 0$ ;   
w[0]=Uchar(cy); Copy answer to output.   
for ( $\mathrm { j } = 1$ ;j<MIN(n+m,p);j++) w[j] $\mathbf { \delta } =$ Uchar(b[j-1]);

With multiplication thus a “fast” operation, division is best performed by multiplying the dividend by the reciprocal of the divisor. The reciprocal of a value $V$ is calculated by iteration of Newton’s rule,

$$
U _ { i + 1 } = U _ { i } ( 2 - V U _ { i } )
$$

which results in the quadratic convergence of $U _ { \infty }$ to $1 / V$ , as you can easily prove. (Many historical supercomputers, and some more recent RISC processors, actually use this iteration to perform divisions.) We can now see where the operations count $N \log N \log \log N$ , mentioned above, originates: $N \log N$ is in the Fourier transform, with the iteration to converge Newton’s rule giving an additional factor of $\log \log N$ .

# void MParith::mpinv(VecUchar_O &u, VecUchar_I &v) {

Character string $\mathtt { v } \left[ 0 \dots \dots \dots 1 \right]$ is interpreted as a radix 256 number with the radix point after (nonzero) v[0]; u[0..n-1] is set to the most significant digits of its reciprocal, with the radix point after u[0].

const Int $\tt N F { = } 4$ ;   
const Doub $\mathbb { B } \mathbb { I } = 1$ .0/256.0;   
Int i,j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { m } = \mathtt { v }$ .size(),mm=MIN(MF,m);   
Doub fu,fv=Doub(v[mm-1]);   
VecUchar s $\left( \mathtt { n } + \mathtt { m } \right)$ ,r(2\*n+m);   
for $( { \mathrm { j } } { = } { \mathrm { m m } } { - } 2 ; { \mathrm { j } } { > } { = } 0 ; { \mathrm { j } } { - } { - } )$ { Use ordinary floating arithmetic to get an initial fv $\ast = \mathrm { ~ B I ~ }$ ; approximation. fv += v[j];   
}   
fu=1.0/fv;   
for (j=0;j<n;j++) { i=Int(fu); u[j]=Uchar(i); fu=256.0\*(fu-i);   
}   
for (;;) { Iterate Newton’s rule to convergence. mpmul(s,u,v); Construct $2 - U V$ in $s$ . mplsh(s); mpneg(s); s[0] $+ =$ Uchar(2); Multiply $s U$ into $U$ . mpmul(r,s,u); mplsh(r); mpmov(u,r); for ( $\mathrm { j } = 1$ ;j<n-1;j++) If fractional part of $s$ is not zero, it has not if (s[j] $! = ~ 0 )$ break; converged to 1. if $\scriptstyle \ j = = \mathtt { n - 1 }$ ) return;   
}

Division now follows as a simple corollary, with only the necessity of calculating the reciprocal to sufficient accuracy to get an exact quotient and remainder.

void MParith::mpdiv(VecUchar_O &q, VecUchar_O &r, VecUchar_I &u, VecUchar_I &v) { Divides unsigned radix 256 integers $\mathbf { u } \left[ 0 \ldots \mathbf { n - 1 } \right]$ by $\mathtt { v } [ 0 \dots \dots \dots 1 ]$ (with $\mathtt { m } \le \mathtt { n }$ required), yielding a quotient q[0..n-m] and a remainder $\mathbf { r } \left[ 0 \ldots \ldots \right] $ .

const Int MACC $\mathrel { \mathop = } 1$ ;   
Int i,is,mm, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { m } = \mathtt { v }$ .size(), $\mathtt { p - r }$ .size(),n_min $\cdot ^ { = }$ MIN(m,p);   
if $\mathbf { \chi } _ { \mathrm { ~ m ~ } } > \mathbf { \chi } _ { \mathrm { ~ n ~ } }$ ) throw("Divisor longer than dividend in mpdiv");   
mm=m+MACC;   
VecUchar s(mm),rr(mm),ss(mm+1),qq(n-m+1),t(n);   
mpinv(s,v); Set $S = 1 / V$ .   
mpmul(rr,s,u); Set $Q = S U$ .   
mpsad(ss,rr,1); mplsh(ss);   
mplsh(ss);   
mpmov(qq,ss);   
mpmov(q,qq);   
mpmul(t,qq,v); Multiply and subtract to get the remainder.   
mplsh(t);   
mpsub(is,t,u,t);   
if (is $! = ~ 0$ ) throw("MACC too small in mpdiv");   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n_min; $\dot { 1 } + +$ ) r[i] $\mathtt { \Omega } = \mathtt { t }$ [i+n-m];   
if (p>m) for (i=m;i<p; $\Dot { \ b { 1 } } + +$ ) $\mathbf { r } \left[ \dot { \mathbf { 1 } } \right] { = } 0$ ;

}

Square roots are calculated by a Newton’s rule much like division. If

$$
\begin{array} { r } { U _ { i + 1 } = \frac { 1 } { 2 } U _ { i } ( 3 - V U _ { i } ^ { 2 } ) } \end{array}
$$

then $U _ { \infty }$ converges quadratically to $1 / \sqrt { V }$ . A final multiplication by $V$ gives $\sqrt { V }$ .

void MParith::mpsqrt(VecUchar_O &w, VecUchar_O &u, VecUchar_I &v) { Character string $\mathtt { v } [ 0 \dots \dots 1 ]$ is interpreted as a radix 256 number with the radix point after $\tt v [ 0 ]$ ; $\mathtt { w } \left[ 0 \ldots \ldots \ldots 1 \right]$ is set to its square root (radix point after $\mathtt { w } [ 0 ]$ ), and $\mathtt { u } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ is set to the reciprocal thereof (radix point before u[0]). w and u need not be distinct, in which case they are set to the square root.

const Int $\mathtt { M F } { = } 3$ ;   
const Doub $\mathbb { B } \mathbb { I } = 1$ .0/256.0;   
Int i,ir,j, $\mathbf { n } { = } \mathbf { u }$ .size(), ${ \mathfrak { m } } { = } \mathfrak { v }$ .size(),mm=MIN(m,MF);   
VecUchar $\mathtt { r } ( 2 \ast \mathtt { n } )$ ,x $\left( \mathtt { n } + \mathtt { m } \right)$ ,s(2\*n+m),t(3\*n+m);   
Doub fu,fv $=$ Doub(v[mm-1]);   
for (j=mm-2;j>=0;j--) { Use ordinary floating arithmetic to get an initial apfv $\ast =$ BI; proximation. fv += v[j];   
}   
fu=1.0/sqrt(fv);   
for (j=0;j<n;j++) $\dot { \bf 1 } =$ Int(fu); u[j]=Uchar(i); fu=256.0\*(fu-i);   
}   
for (;;) { Iterate Newton’s rule to convergence. mpmul(r,u,u); Construct $S = ( 3 - V U ^ { 2 } ) / 2$ . mplsh(r); mpmul(s,r,v); mplsh(s); mpneg(s); s[0] $+ =$ Uchar(3); mpsdv(s,s,2,ir); for (j=1;j<n-1; $\mathrm { i } + +$ ) { If fractional part of $s$ is not zero, it has not conif (s[j] != 0) { verged to 1. mpmul(t,s,u); Replace $U$ by $s U$ . mplsh(t); mpmov(u,t); break; } if (j<n-1) continue; mpmul(x,u,v); Get square root from reciprocal and return. mplsh(x); mpmov(w,x); return;   
}

We already mentioned that radix conversion to decimal is a merely cosmetic operation that should normally be omitted. The simplest way to convert a fraction to decimal is to multiply it repeatedly by 10, picking off (and subtracting) the resulting integer part. This has an operations count of $O ( N ^ { 2 } )$ , however, since each liberated decimal digit takes an $O ( N )$ operation. It is possible to do the radix conversion as a fast operation by a “divide-and-conquer” strategy, in which the fraction is (fast) multiplied by a large power of 10, enough to move about half the desired digits to the left of the radix point. The integer and fractional pieces are now processed independently, each further subdivided. If our goal were a few billion digits of $\pi$ , instead of a few thousand, we would need to implement this scheme. For present purposes, the following lazy routine is adequate:

# void MParith::mp2dfr(VecUchar_IO &a, string &s)

Converts a radix 256 fraction a[0..n-1] (radix point before a[0]) to a decimal fraction represented as an ASCII string $\mathbf { s } \left[ 0 \ldots \ldots \right]$ , where m is a returned value. The input array $\mathbf { a } \left[ 0 \ldots \mathbf { n - 1 } \right]$ is destroyed. NOTE: For simplicity, this routine implements a slow $( \propto \dot { N } ^ { 2 } )$ algorithm. Fast $( \propto N \ln N )$ ), more complicated, radix conversion algorithms do exist.   
{   
const Uint IAZ=48;   
char buffer[4];   
Int j,m;   
Int $\mathrm { n } = \mathrm { a }$ .size();   
m=Int(2.408\*n);   
sprintf(buffer,"%d",a[0]);   
s=buffer;   
s +=   
mplsh(a);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<m;j++) { mpsmu(a,a,10); s $+ =$ a[0]+IAZ; mplsh(a);   
}

Finally, then, we arrive at a routine implementing equations (22.7.1) and (22.7.2):

string MParith::mppi(const Int np) J   
Demonstrate multiple precision routines by calculating and printing the first np bytes of $\pi$ . const Uint IAOFF $\ddots$ 48,MACC $^ { * 2 }$ ; Int ir,j,n=np+MACC; Uchar mm; string s; VecUchar x(n),y(n),sx(n),sxi(n),z(n),t(n),pi(n),ss( $^ { 2 * \mathrm { n } }$ ),tt $( 2 \ast \mathtt { n } )$ ; t[0] $^ { = 2 }$ ; Set $T = 2$ . for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<n;j++) t[j] ${ = } 0$ ; mpsqrt(x,x,t); Set $X _ { 0 } = \sqrt { 2 }$ . mpadd(pi,t,x); Set $\pi _ { 0 } = 2 + { \sqrt { 2 } }$ . mplsh(pi); mpsqrt(sx,sxi,x); Set $Y _ { 0 } = 2 ^ { 1 / 4 }$ . mpmov(y,sx); for (;;) { mpadd(z,sx,sxi); Set $X _ { i + 1 } = ( X _ { i } ^ { 1 / 2 } + X _ { i } ^ { - 1 / 2 } ) / 2$ . mplsh(z); mpsdv(x,z,2,ir);mpsqrt(sx,sxi,x); Form the temporary $T = Y _ { i } X _ { i + 1 } ^ { 1 / 2 } + X _ { i + 1 } ^ { - 1 / 2 }$ . mpmul(tt,y,sx); mplsh(tt);

mpadd(tt,tt,sxi); mplsh(tt); x[0]++; Increment $X _ { i + 1 }$ and $Y _ { i }$ by 1. y[0]++; mpinv(ss,y); Set $Y _ { i + 1 } = T / ( Y _ { i } + 1 )$ . mpmul(y,tt,ss); mplsh(y); mpmul(tt,x,ss); Form temporary $T = ( X _ { i + 1 } + 1 ) / ( Y _ { i } + 1 )$ . mplsh(tt); mpmul(ss,pi,tt); Set $\pi _ { i + 1 } = T \pi _ { i }$ . mplsh(ss); mpmov(pi,ss); mm=tt[0]-1; If $T = 1$ , then we have converged. for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j < n-1;j++) if (tt[j] $! = ~ \mathtt { m m } ,$ ) break; if ${ \mathrm { ( j ~ } } = = { \mathrm { ~ n } } - 1 { \mathrm { ) } }$ ) { mp2dfr(pi,s); Convert to decimal for printing. NOTE: The conversion routine, for this demon stration only, is a slow $( \propto N ^ { 2 } )$ algorithm. Fast $( \propto N \ln N )$ , more complicated radix conversion algorithms do exist. s.erase(Int(2.408\*np),s.length()); return s; } } }

$$
{ \frac { 1 } { \pi } } = { \frac { \sqrt { 8 } } { 9 8 0 1 } } \sum _ { n = 0 } ^ { \infty } { \frac { ( 4 n ) ! ( 1 1 0 3 + 2 6 3 9 0 n ) } { ( n ! 3 9 6 ^ { n } ) ^ { 4 } } }
$$

using the above routines. You might also use the routines to verify that the number $2 ^ { 5 1 2 } ~ + ~ 1$ is not a prime, but has factors 2,424,833 and 7,455,602,825,647,884,208,337,395,736,200,454,918,783,366,342,657 (which are in fact prime; the remaining prime factor being about $7 . 4 1 6 \times 1 0 ^ { 9 8 }$ ) [4].

# CITED REFERENCES AND FURTHER READING:

Borwein, J.M., and Borwein, P.B. 1987, Pi and the AGM: A Study in Analytic Number Theory and Computational Complexity (New York: Wiley).[1]   
Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 4 . 3 . [ 2 ]$   
Ramanujan, S. 1927, Collected Papers of Srinivasa Ramanujan, G.H. Hardy, P.V. Seshu Aiyar, and B.M. Wilson, eds. (Cambridge, UK: Cambridge University Press), pp. 23–39.[3]   
Kolata, G. 1990, June 20, “Biggest Division a Giant Leap in Math,” The New York Times.[4]   
Kronsjö, L. 1987, Algorithms: Their Complexity and Efficiency, 2nd ed. (New York: Wiley).   
Abstract Base Class (ABC) 24, 33, 34, 87, 114, 703, 874   
Accelerated convergence of series 177, 211–218   
Accuracy 8–12 achievable in minimization 493, 497, 503 achievable in root finding 448 contrasted with fidelity 1037, 1046 CPU different from memory 230 vs. stability 907, 931, 932, 1035, 1050   
Adams-Bashford-Moulton method 943   
Adams’ stopping criterion 467   
Adaptive integration 901, 910–921, 928, 930, 935, 946, 995 Monte Carlo 410–418 PI stepsize control 915 predictive stepsize control 939 see also Adaptive quadrature   
Adaptive quadrature 155, 167, 194–196 and singularities 195 termination criterion 194   
Addition multiple precision 1186 theorem, elliptic integrals 310   
ADI (alternating direction implicit) method 1052, 1053, 1065, 1066, 1185   
Adjoint operator 1071   
Advanced topics (explanation) 6   
Advective equation 1032   
Affine scaling 543   
Agglomerative clustering 873–882   
AGM (arithmetic geometric mean) 1185   
Airy function 254, 283, 289, 291 routine for 290   
Aitken’s delta squared process 212, 214 interpolation algorithm 118   
Algorithms, less-numerical 1160–1193   
Aliasing 606, 685 see also Fourier transform   
Alignment of strings by DP 559–562   
All-poles or all-zeros models 681, 682 see also Maximum entropy method (MEM); Periodogram   
Alternating-direction implicit method (ADI) 1052, 1053, 1065, 1066, 1185   
Alternating series 211, 216   
Alternative extended Simpson’s rule 160   
AMD (approximate minimum degree) 544, 548   
Amoeba 503 see also Simplex, method of Nelder and Mea   
Amplification factor 1033, 1035, 1038, 1045, 1046   
Amplitude error 1036   
Analog-to-digital converter 1018, 1166   
Analyticity 246   
Analyze/factorize/operate package 76, 1030   
Anderson-Darling statistic 739   
Andrew’s sine 821   
Angle between vectors 1120, 1121 coordinates on $n$ -sphere 1128 exterior, of polygons 1122   
Annealing, method of simulated 487, 488, 549–555 assessment 554, 555 for continuous variables 550, 552–554 schedule 551, 552 thermodynamic analogy 550 traveling salesman problem 551, 552   
ANSI-16 1171   
ANSI/ISO $\mathrm { C } { + } { + }$ standard 5   
Antonov-Saleev variant of Sobol’ sequence 404–406, 408, 409   
Apple Mac OS X 5   
Approximate inverse of matrix 63   
Approximation of functions 110 by Chebyshev polynomials 234, 625 by rational functions 247–251 by wavelets 711, 712, 989 Pade approximant 212, 245–247 ´ see also Fitting   
Area polygon 1126 sphere in $n$ -dimensions 1128 triangle 1111   
Arithmetic arbitrary precision 1160, 1185–1193 floating point 1163 IEEE standard 1164, 1165 rounding 1164, 1165 64 bit 341   
Arithmetic coding 755, 1160, 1181–1185   
Arithmetic-geometric mean (AGM) method 1185   
Array assign function 27 centered subarray of 115 classes for 24–29 resize function 27 size function 27 three-dimensional 36 unit-offset 36 zero-offset 36   
Artificial viscosity 1037, 1042   
Ascending transformation, elliptic integrals 310   
ASCII character set 1168, 1175, 1181   
assign 27   
Associated Legendre polynomials 971 recurrence relation for 294 relation to Legendre polynomials 293   
Association, measures of 721, 741, 758–761   
Asymptotic series 210, 216 exponential integral 216, 269   
Attenuation factors 698   
Autocorrelation in linear prediction 673–675 use of FFT 648, 649 Wiener-Khinchin theorem 602, 682   
Autoregressive model (AR) see Maximum entropy method (MEM)   
Average deviation of distribution 723   
Averaging kernel, in Backus-Gilbert method 1014   
B-spline 148   
Backsubstitution 47, 49, 53, 56, 103 complex equations 55 direct for computing ${ \bf A } ^ { - 1 }$ - B 53 in band-diagonal matrix 60 relaxation solution of boundary value problems 966   
Backtracking 522 in quasi-Newton methods 478–483   
Backus-Gilbert method 1014–1016   
Backward deflation 464, 465   
Bader-Deuflhard method 940   
Bahl-Cocke-Jelinek-Raviv algorithm forward-backward algorithm 867   
Bairstow’s method 466, 471   
Balancing 592, 594   
Band-diagonal matrix 56, 58–61 backsubstitution 60 $_ { L U }$ decomposition 59 multiply by vector 58 storage 58   
Band-pass filter 667, 670 wavelets 701   
Bandwidth limited function 605   
Bank accounts, checksum for 1174   
Bar codes, checksum for 1174   
Barrier method 541   
Bartels-Golub update 535   
Bartlett window 657   
Barycentric coordinates 1114, 1116   
Barycentric rational interpolation 113, 127, 128   
Base class 23   
Base of representation 8, 1164   
Basin of convergence 461, 463   
Basis functions in general linear least squares 788   
Baum-Welch re-estimation hidden Markov model 865–867 relation to expectation-maximization 866   
Bayes’ theorem 774, 777, 825   
Bayesian approach to inverse problems 1005, 1022 contrasted with frequentist 774 estimation of parameters by MCMC 774, 824–835 lack of goodness-of-fit methods 779, 1010 normalizing constant 779 odds ratio 757, 779 parameter estimation 777, 778 prior 757, 775, 777, 1005 views on straight line fitting 787 vs. historic maximum entropy method 1022   
Bayesian algorithms hidden Markov model 868 Viterbi decoding 868   
Bayesian networks 840, 841 node parents 841 nodes 840 posterior probabilities 841 prior probabilities 841   
Bayesian re-estimation hidden Markov model 864–866   
Belief networks 840 forward-backward algorithm 867   
Bellman-Dijkstra-Viterbi algorithm 556, 850, 853   
Berlekamp-Massey decoding algorithm 852   
Bernoulli number 164   
Bessel functions 274–292 asymptotic form 274, 279, 284 complex 254 continued fraction 283, 284, 287, 288 fractional order 274, 283–292 Miller’s algorithm 221, 278 modified 279–283 modified, fractional order 287–289 modified, normalization formula 282, 288 modified, routines for 280 normalization formula 221 recurrence relation 219, 274, 275, 278, 281, 283–285 reflection formulas 286 reflection formulas, modified functions 289 routines for 276, 286 routines for modified functions 289 series for 210, 274 series for $K _ { \nu }$ 288 series for $Y _ { \nu }$ 284, 285 spherical 283, 291, 292 turning point 283

![](images/a03563108e75539239b188b39a7e5fe588fbd594e92a35a8d363f8bf6036c888.jpg)  
Figure 22.7.1. The first 2398 decimal digits of $\pi$ , computed by the routines in this section.

Wronskian 283, 284, 287 Best-fit parameters 773, 781, 785, 822–824 see also Fitting Beta function 256, 258, 259 incomplete see Incomplete beta function Beta probability distribution 333, 334 deviates 371 gamma as limiting case 333 Betting 755–758, 760, 761 fair bet 755, 756, 758, 760, 761 proportional 758, 760 Bezier curve 148 BFGS algorithm see Broyden-Fletcher-Goldfarb-Shanno algorithm Bias of exponent 8 removal in linear prediction 145, 678, 679 Biconjugacy 88 Biconjugate gradient method elliptic partial differential equations 1030 for sparse system 88, 716 preconditioning 89, 1030 Bicubic interpolation 136–138 Bicubic spline 135 Big-endian 9 Biharmonic equation 153 Bilinear interpolation 133, 134 Binary block code 851 Binomial coefficients 256, 258 recurrences for 258 Binomial probability function 258, 338, 339 deviates from 374–377 moments of 735 Poisson as limiting case 338 Binormal distribution 746, 813 Biorthogonality 88 Bisection 115, 460 compared to minimum bracketing 492 root finding 445, 447–449, 454, 492, 584 Bispectrum 604 Bit 8, 754–756, 760, 761 phantom 9 pop count 16 reversal in fast Fourier transform (FFT) 610, 638 Bit-parallel random comparison 374 Bit-twiddling hacks 16 Bitwise logical functions 1170 test if integer a power of 2 16, 611 trick for next power of 2 16, 361 Black-Scholes formula 329 BLAST (software) 562 BLAT (software) 562 Block-by-block method 994 Bluetooth 1168 Bode’s rule 158 Boltzmann probability distribution 550 Boltzmann’s constant 550 Bolyai-Gerwien theorem 1127 Bookie, information theory view of 758

Bool 25   
Bootstrap method 809, 810   
Bordering method for Toeplitz matrix 96   
Borwein and Borwein method for $\pi$ 1185   
Boundary 196, 528, 955   
Boundary conditions for differential equations 900 for spheroidal harmonics 972, 973 in multigrid method 1072 initial value problems 900 partial differential equations 620, 1025, 1053–1058 two-point boundary value problems 900, 955–984   
Boundary value problems 1026 see also Differential equations; Elliptic partial differential equations; Two-point boundary value problems   
Bounds checking 35 in vector by at 35   
Box 1099–1101 test if point inside 1100 tree of, as data structure 1101   
Box-Muller algorithm for normal deviate 364   
Bracketing of function minimum 445, 490–496, 503 of roots 443, 445–447, 454, 455, 464, 465, 470, 492   
Branch cut, for hypergeometric function 252–254   
Break iteration 15   
Brenner’s FFT implementation 611, 628   
Brent’s method minimization 489, 496–499, 785 minimization, using derivative 489, 499, 500 root finding 443, 449, 453–456, 459, 786   
Broyden-Fletcher-Goldfarb-Shanno algorithm 490, 521–525   
Broyden’s method 474, 483–486 singular Jacobian 486   
Bubble sort 420   
Bugs, how to report 5   
Bulirsch-Stoer algorithm for rational function interpolation 125 for second order equations 929 method 252, 318, 900, 901, 909, 921–929, 942 method, dense output 927 method, implementation 927 method, stepsize control 924–926, 929   
Burg’s LP algorithm 677   
Burn-in 826, 833–835   
Butterfly 360, 361, 610   
Byte 8   
C (programming language) 1 _FILE__ and __LINE__ macros 30 idioms 16 syntax 12–17   
$\mathrm { C } { + } { + }$ ANSI/ISO standard 5 C family syntax 12–17 const statement 31, 32 contiguous storage for vector 27 control structures 14, 15 error class 30 inline directive 29 NR not a textbook on 2 operator associativity 12 operator precedence 12 overloading 28 scope, temporary 20, 21 standard library 10, 24 templates 17, 22, 26, 33, 34, 419, 421 throw 30 try and catch 30 types 25 types used in NR 4 user-defined conversions 31 valarray class 25 vector class 24 virtual function 33 why used in NR 1   
C# (programming language) 1, 12   
Calendar algorithms 2, 3, 6, 7   
Calibration 778   
Cardinal functions 1089–1091   
Cards, sorting a hand of 420, 422   
Carlson’s elliptic integrals 310–316   
Carpe diem 830   
catch 30   
Cauchy principal value integrals 178   
Cauchy probability distribution 322, 323 deviates from 367 see also Lorentzian probability distribution   
Cauchy problem for partial differential equations 1024   
Cavender-Felsenstein model 873   
Cayley’s representation of $\exp ( - i H t )$ 1049   
CCITT (Comite Consultatif International ´ Tel´ egraphique et T ´ el´ ephonique) 1171, 1180 ´   
CCITT-16 1171   
CDF see Cumulative Distribution Function   
Center of mass 399, 400, 1113, 1127   
Central limit theorem 777   
Central tendency, measures of 721   
Centroid see Center of mass   
Change of variable in integration 170–172, 995 in Monte Carlo integration 401 in probability distribution 362   
Char 25   
Character-based clustering methods 869   
Characteristic polynomial digital filter 670 eigensystems 563, 583, 665 linear prediction 676 matrix with a specified 469 of recurrence relation 221 of tridiagonal system 665   
Characteristics of partial differential equations 1024–1026   
Chebyshev acceleration in successive over-relaxation (SOR) 1064   
Chebyshev approximation 95, 156, 232–239 Clenshaw-Curtis quadrature 241 Clenshaw’s recurrence formula 236 coefficients for 234 contrasted with Pade approximation 245 ´ derivative of approximated function 232, 240, 241 economization of series 243–245 even function 237 fast cosine transform and 625 for error function 264 gamma functions 285 integral of approximated function 240, 241 odd function 237 polynomial fits derived from 241, 243, 248 rational function 247–251 Remes exchange algorithm for filter 669   
Chebyshev polynomials 183, 187, 233–239 basis functions for spectral methods 1085 continuous orthonormality 233 discrete orthonormality 233 explicit formulas for 233 formula for $x ^ { k }$ in terms of 233   
Check digit (decimal) 1173   
Checksum 1160, 1168–1175 cyclic redundancy (CRC) 1168–1173   
Chemical reaction networks 946–954   
Chi-by-eye 774   
Chi-square fitting see Fitting; Least-squares fitting   
Chi-square probability function 330, 331, 732, 778, 779, 1003 as boundary of confidence region 812 deviates from 371   
Chi-square test 731–734 and confidence limit estimation 812 chi-by-eye 774 chi-square-gamma test 735 degrees of freedom 732, 733 for binned data 731–734 for contingency table 742–745 for inverse problems 1003 for straight line fitting 781 for straight line fitting, errors in both coordinates 785 for two binned data sets 732 goodness-of-fit 780 how much $\Delta \chi ^ { 2 }$ is significant 816 least-squares fitting 778–780 and likelihood ratio test 735 modified Neyman 735 nonlinear models 799 small numbers of counts 734, 735 for two binned data sets 735 unequal size samples 733   
Chirp signal 672   
Cholesky decomposition 100–102, 525, 568 and covariance structure 378, 379 decorrelating random variables 379 multivariate Gaussian distribution 847, 848 operation count 100 pivoting 101 solution of normal equations 543, 790, 791 sparse decomposition 544, 548   
Circle inscribed or circumscribed 1112 largest empty 1147 random point on 1131   
Circulant 700   
Circumscribed circle (circumcircle) 1112   
CLAPACK 567   
Class 17–24 abstract base (ABC) 24, 33, 34, 87, 114, 703, 874 base class 23 derived 23 error class 30 inheritance 23, 24 is-a relationship 23 matrix 24–29 partial abstraction via 24 prerequisite relationship 23 public vs. private 17 pure virtual 34 suffix _I, _O, _IO 26, 32 templated 22, 33, 34 vector 24–29 see also Object   
Class library 2   
Classification 840–898 kernel methods 889, 892 support vector machine 883–898   
Clenshaw-Curtis quadrature 156, 241, 624, 625   
Clenshaw’s recurrence formula 219, 222, 223 for Chebyshev polynomials 236 stability 223   
Clock, program timing routine 355   
Clocking errors 1172   
CLP (linear programming package) 536   
Clustering agglomerative 873–882 hierarchical 868–882 k-means 848–850 neighbor-joining (NJ) 873, 878–882   
cn function 316   
Coarse-grid correction 1068   
Coarse-to-fine operator 1068   
Codes binary block codes 851 codeword 851 correcting bit errors 855 error-correcting 851–855 Golay code 852 Hamming code 852 Hamming distance 851, 1168 hard-decision decoding 853 linear codes 851

minimal trellis 853 perfect code 852 Reed-Solomon 852, 855 soft-decision decoding 853 syndrome decoding 852 trellis 853, 856 turbo codes 855 Viterbi decoding 854 Coding arithmetic 755, 1181–1185 checksums 1168–1175 compression 754, 756 decoding a Huffman-encoded message 1178 Huffman 713, 1175–1180 run-length 1180 variable length code 1176 Ziv-Lempel 1176 see also Arithmetic coding; Huffman coding Coefficients binomial 258 for Gaussian quadrature 179, 180 for Gaussian quadrature, nonclassical weight function 189–191, 995 for quadrature formulas 157–162, 995 Column operations on matrix 43, 45 Column totals 743, 759 Combinatorial minimization see Annealing Comite Consultatif International T ´ el´ egraphique et ´ Tel´ ephonique (CCITT) 1171, 1180´ Communications protocol 1168 Comparison function for rejection method 366 Compiler check on via constructors 36 tested 5 Complementary error function see Error function Complete elliptic integral see Elliptic integrals Complex arithmetic 225, 226 access vector as if complex 613, 620 avoidance of in path integration 253 Complex type 25 cubic equations 228, 229 linear equations 55 quadratic equations 227 Complex error function 302 Complex plane fractal structure for Newton’s rule 462 path integration for function evaluation 251–254, 318 poles in 124, 210, 252, 256, 670, 682, 922 Complex systems of linear equations 55 Compression of data 713, 715, 1160, 1175–1185 Computational geometry floating point arithmetic in 1098 Computer graphics 1097 Computer vision 1097 Concordant pair for Kendall’s tau 751 Condition number 69, 89, 791, 793 Conditional entropy 758–761 Confidence level 810, 811, 814–816 Confidence limits

and chi-square 811 bootstrap method 809, 810 by Monte Carlo simulation 807–810 confidence region, confidence interval 810, 811 from singular value decomposition (SVD) 816, 817 on estimated model parameters 807–817   
Confluent hypergeometric function 254, 287   
Conjugate directions 509, 511, 512, 516   
Conjugate gradient method and wavelets 716 biconjugate 88 compared to variable metric method 521 elliptic partial differential equations 1030 for minimization 489, 515–520, 1011, 1020 for sparse system 87–92, 716 minimum residual method 89 preconditioner 89, 90   
Conservative differential equations 928, 930   
const correctness 26, 31, 32 protects container, not contents 31, 32 to protect data 32   
Constellation in Viterbi decoding 855   
Constrained linear inversion method 1006   
Constrained linear optimization see Linear programming   
Constrained optimization 487   
Constraints deterministic 1011–1013 linear 526, 530   
Constructor 18, 27   
Container, STL 421   
Contingency coefficient C 743, 744   
Contingency table 741–745, 753, 758, 759 statistics based on chi-square 742–745 statistics based on entropy 758–761   
Continue statement 15   
Continued fraction 206–209 and recurrence relation 222 Bessel functions 283, 284, 288 convergence criterion 208 equivalence transformation 208 evaluation 206–209 evaluation along with normalization condition 288 even and odd parts 208, 260, 267, 298, 301 exponential integral 267 Fresnel integral 298 incomplete beta function 270 incomplete gamma function 260 Lentz’s method 207, 260 modified Lentz’s method 208 Pincherle’s theorem 222 ratio of Bessel functions 287 rational function approximation 207, 260 recurrence for evaluating 207, 208 sine and cosine integrals 301 Steed’s method 207 tangent function 206 typography for 206   
Continuous variable (statistics) 741   
Control structures and scope 21   
Convergence accelerated, for series 177, 211–218 basin of 461, 463 criteria for 448, 493, 503, 598, 599, 802, 969 eigenvalues accelerated by shifting 585 exponential 174–178, 180, 238, 239, 1083–1096 golden ratio 449, 500 hyperlinear (series) 211 linear 448, 495 linear (series) 211 logarithmic (series) 211 Markov model 858 of algorithm for $\pi$ 1185 of golden section search 494, 495 of Levenberg-Marquardt method 802 of $Q L$ method 584, 585 of Ridders’ method 452 quadratic 64, 452, 459, 511, 512, 522, 1185 rate 448, 454, 457, 459 recurrence relation 222 series vs. continued fraction 206 spectral radius and 1061, 1066   
Conversions, user-defined 31   
Convex hull 1097, 1132, 1146   
Convex sets, use in inverse problems 1011–1013   
Convolution and polynomial interpolation 129 denoted by asterisk 602 finite impulse response (FIR) 642, 643 multiple precision arithmetic 1188 multiplication as 1188 necessity for optimal filtering 645 of functions 602, 616, 617, 631 of large data sets 646, 647 overlap-add method 647 overlap-save method 646 relation to wavelet transform 700, 701 theorem 602, 641, 656 theorem, discrete 642, 643 treatment of end effects 643 use of FFT 641–647 wraparound problem 643   
Cooley-Tukey FFT algorithm 616   
Cornwell-Evans algorithm 1021   
Corporate promotion ladder 427   
Corrected distance transformation 873   
Corrected two-pass algorithm 724   
Correction, in multigrid method 1067   
Correlation coefficient (linear) 745–748   
Correlation function 602, 617 and Fourier transforms 602, 617 autocorrelation 602, 649, 673–675 theorem 602, 648 three-point 604 treatment of end effects 648

using FFT 648, 649 Wiener-Khinchin theorem 602, 682 Correlation, statistical 721, 741 among parameters in a fit 782, 793 Kendall’s tau 749, 751–754 linear correlation coefficient 745–748, 783 linear related to least-squares fitting 745, 783 nonparametric or rank statistical 748–754 Spearman rank-order coefficient 749–751 sum squared difference of ranks 749 uncertainty coefficient 761 Coset leader 852 Cosine function, recurrence 219 Cosine integral 297, 300–302 continued fraction 301 routine for 301 series 301 Cosine transform see Fast Fourier transform (FFT); Fourier transform Coulomb wave function 254, 283 Counts, small numbers of 734, 735 Courant condition 1034, 1036, 1038–1040, 1042 multidimensional 1051 Courant-Friedrichs-Lewy stability criterion see Courant condition Covariance a priori 824 from singular value decomposition (SVD) 817 in general linear least squares 790, 791, 794 in nonlinear models 802 in straight line fitting 782 matrix, and normal equations 790 matrix, Cholesky decomposition 101 matrix, is inverse of Hessian matrix 802 matrix, of errors 1003, 1015 matrix, when it is meaningful 812, 813 relation to chi-square 812–816 CR method see Cyclic reduction (CR) Cramer’s V 743, 744 Crank-Nicolson method 1045, 1049, 1051, 1052 Cray, Seymour 1163 CRC (cyclic redundancy check) 1168–1173 CRC-12 1171 Critical (Nyquist) sampling 605, 607, 653 Cross $\otimes$ (denotes matrix outer product) 78 Crosstabulation analysis 742 see also Contingency table Crout’s algorithm 49, 59 Cubic equations 227–229, 461 Cubic spline interpolation 120–124 see also Spline Cumulative Distribution Function (cdf) 435 Curse of dimensionality 556, 891 Curvature matrix see Hessian matrix Curve interpolation 147 Cycle, in multigrid method 1069 Cyclic Jacobi method 573 Cyclic reduction (CR) 224, 1054, 1057, 1058 Cyclic redundancy check (CRC) 1168–1173

Cyclic tridiagonal systems 79, 80   
D.C. (direct current) 602   
Danielson-Lanczos lemma 609, 610, 638   
Data continuous vs. binned 731 entropy 754–761, 1176 essay on 720 fitting 773–838 fraudulent 780 glitches in 777 iid (independent and identically distributed) 809 linearly separable 884 missing data points 150–154 modeling 773–838 smoothing 721, 766–772 statistical tests 720–772 unevenly or irregularly sampled 139–154, 685, 690, 771 use of CRCs in manipulating 1169 windowing 655–667 see also Statistical tests   
Data compression 713, 715, 1160 arithmetic coding 1181–1185 cosine transform 625 Huffman coding 713, 1175–1181 linear predictive coding (LPC) 679–681 lossless 1175   
Data Encryption Standard (DES) 358–361   
Data type 8   
DAUB4 700, 702, 706, 707, 711, 715   
DAUB6 702   
DAUB20 706   
Daubechies wavelet coefficients 700–702, 704, 706–708, 715   
Davidon-Fletcher-Powell algorithm 490, 521, 522   
Dawson’s integral 302, 304, 717 approximation for 303 routine for 303   
DE rule 174 implementation 175 infinite range 176   
Decoding Berlekamp-Massey algorithm for Reed-Solomon code 852 directed graph 556, 850 hard-decision 853 hard-decision vs. soft-decision 855 maximum likelihood 854 Reed-Solomon codes 855 soft-decision decoding 853 syndrome decoding 852 Turbo codes 855 Viterbi algorithm 854 Viterbi, compared to hidden Markov model 867, 868   
Decomposition see Cholesky decomposition; $_ { L U }$ decomposition; $\boldsymbol { Q R }$ decomposition; Singular value decomposition (SVD)   
Deconvolution 645–647, 650 see also Convolution; Fast Fourier transform (FFT); Fourier transform   
Decorrelating random variables 379   
Defect, in multigrid method 1067   
Deferred approach to the limit see Richardson’s deferred approach to the limit   
Deflation of matrix 585 of polynomials 464–466, 471   
Degeneracy kernel 992 linear algebraic equations 73, 793 minimization principle 1002   
Degrees of freedom 732, 733, 778, 779, 813–815   
Delaunay triangulation 1097, 1131–1149 applications of 1141–1149 incremental constructions 1134 interpolation using 1141 largest minimum angle property 1134 minimum spanning tree 1147 not minimum weight 1134   
Delone, B.N. see Delaunay Triangulation   
Dense output, for differential equations 904, 915, 927   
Dependencies, program 4   
Dependency graph or matrix 949   
Derivatives approximation by sinc expansion 178 computation via Chebyshev approximation 232, 240, 241 computation via Savitzky-Golay filters 232, 769 matrix of first partial see Jacobian determinant matrix of second partial see Hessian matrix numerical computation 229–232, 480, 769, 936, 960, 978 of polynomial 202 use in optimization 499–502   
Derived class 23   
DES see Data Encryption Standard   
Descending transformation, elliptic integrals 310   
Descent direction 478, 484, 522   
Descriptive statistics 720–772 see also Statistical tests   
Design matrix 768, 788, 1002   
Design of experiments 410   
Detailed balance equation 825–827   
Determinant 39, 54, 55   
Devex 535   
Deviates, random see Random deviates   
DFP algorithm see Davidon-Fletcher-Powell algorithm   
Diagonal dominance 57, 802, 987, 1060   
Diagonal rational function 125   
Diehard test, for random numbers 345   
Difference equations, finite see Finite difference equations (FDEs)   
Difference operator 212   
Differential equations 899–954

accuracy vs. stability 907, 931   
Adams-Bashforth-Moulton schemes 943   
adaptive stepsize control 901, 910–921,   
924–926, 929, 939, 941, 943, 944, 946   
algebraically difficult sets 970   
backward Euler’s method 932   
Bader-Deuflhard method for stiff 940   
boundary conditions 900, 955, 962, 977   
Bulirsch-Stoer method 252, 318, 900, 901,   
909, 921–928, 942   
Bulirsch-Stoer method for conservative   
equations 928, 930   
comparison of methods 900, 901, 942, 946,   
957   
conservative 928, 930   
dense output 904, 915, 927   
discreteness effects 946–954   
eigenvalue problem 958, 973, 977–981   
embedded Runge-Kutta method 911, 936   
equivalence of multistep and multivalue   
methods 945   
Euler’s method 900, 907, 931   
forward Euler’s method 931   
free boundary problem 958, 983   
global vs. local error 914   
high-order implicit methods 934   
implicit differencing 932, 933, 944   
initial value problems 900   
integrating to an unknown point 916   
internal boundary conditions 983, 984   
internal singular points 983, 984   
interpolation on right-hand sides 115   
Kaps-Rentrop method for stiff 934   
local extrapolation 911   
modified midpoint method 922, 923   
multistep methods 900, 942–946   
multivalue methods 942–946   
Nordsieck method 944   
order of method 907, 922   
path integration for function evaluation   
251–254, 318   
predictor-corrector methods 900, 909, 934,   
942–946   
r.h.s. independent of $x$ 932, 934   
reduction to first-order sets 899, 956   
relaxation method 957, 964–970   
relaxation method, example of 971, 973–977   
Rosenbrock methods for stiff 934–940   
Runge-Kutta method 900, 907–921, 934, 942,   
1096   
Runge-Kutta method, high-order 907–910,   
912   
scaling stepsize to required accuracy 913, 914   
second order 928, 930   
semi-implicit differencing 934   
semi-implicit Euler method 934, 940   
semi-implicit extrapolation method 934, 935,   
940, 941   
semi-implicit midpoint rule 940   
shooting method 956, 959–961

shooting method, example 971, 977–981 similarity to Volterra integral equations 993 singular points 921, 962, 983, 984 solving with sinc expansions 178 step doubling 910 stepsize control 901, 910–920, 924, 929, 938, 941, 944, 946 stepsize, danger of too small 920 stiff 901, 931–941 stiff methods compared 941 stochastic simulation 946–954 Stoermer’s rule 928 see also Partial differential equations; Two-point boundary value problems Differentiation matrix 1091 routine for 1092 Diffusion equation 1024, 1043–1049, 1059 Crank-Nicolson method 1045, 1049, 1051, 1052 forward time centered space (FTCS) 1044, 1046, 1059 implicit differencing 1045 multidimensional 1051, 1052 Digamma function 267 Digital filtering see Filter Dihedral angle 1116 Dihedral group $D _ { 5 }$ 1174 Dimensionality, curse of 556, 891 Dimensions (units) 801 Diminishing increment sort 422 Dingbats, Zapf 1162 Dirac delta function 700, 987 Direct method see Periodogram Direct methods for linear algebraic equations 40 Direct product see Outer product of matrices Directed graph Markov model 856 stages and states 556, 850 transition matrix 856 transition probability 856 trellis 856 Viterbi decoding 850 Direction numbers, Sobol’s sequence 404 Direction of largest decrease 512 Direction set methods for minimization 489, 509–514 Dirichlet boundary conditions 1026, 1045, 1055, 1061, 1063 Discordant pair for Kendall’s tau 751 Discrete convolution theorem 642, 643 Discrete Fourier transform (DFT) 605–608 approximation to continuous transform 607, 608 see also Fast Fourier transform (FFT) Discrete optimization 536, 549 Discrete prolate spheroidal sequence (dpss) 662–667 Discretization error 173 Discriminant 227, 572 Dispersion 1036

DISPO see Savitzky-Golay filters   
Dissipation, numerical 1035   
Distance matrix 869   
Distributions, statistical see Statistical distributions   
Divergent series 210, 211, 216   
Divide-and-conquer method 589   
Division complex 226 integer vs. floating 8 multiple precision 1190 of polynomials 204, 464, 471   
dn function 316   
DNA sequence 559–562, 869, 884   
Do-while iteration 15   
Dogleg step methods 486   
Domain of integration 196   
Dominant solution of recurrence relation 220   
Dormand-Prince parameters 912, 920   
Dot - denotes matrix multiplication 37 denotes row or column sums 759   
Doub 25   
Double exponential error distribution 820   
Double root 443   
Doubling rate 756   
Downhill simplex method see Simplex, method of Nelder and Mead   
DP see Dynamic programming   
dpss (discrete prolate spheroidal sequence) 662–667   
Dual problem 538, 886   
Dual viewpoint, in multigrid method 1077   
Duality gap 538   
Duplication theorem, elliptic integrals 311   
DWT (discrete wavelet transform) see Wavelet transform   
Dynamic programming 555–562 Bellman-Dijkstra-Viterbi algorithm 556, 850 directed graph 556, 850   
e-folding rate 756   
Eardley’s equivalence class method 440   
Economization of power series 243–245   
Eigensystems 563–599 and integral equations 987, 992 balancing matrix 592, 594 bounds on eigenvalues 64 calculation of few eigenvectors or eigenvalues 568, 598 canned routines 567 characteristic polynomial 563, 583 completeness 564, 565 defective 564, 591, 598, 599 deflation 585 degenerate eigenvalues 563, 565 divide-and-conquer method 589 eigenvalues 563 elimination method 567, 594 factorization method 567 fast Givens reduction 578

generalized eigenproblem 568, 569   
Givens reduction 578–583   
Givens transformation 587   
Hermitian matrix 590   
Hessenberg matrix 567, 585, 590–595, 598   
Householder transformation 567, 578–584,   
587, 590, 594   
ill-conditioned eigenvalues 591, 592   
implicit shifts 586–589   
invariance under similarity transform 566   
inverse iteration 568, 584, 589, 597–599   
Jacobi transformation 567, 570–576, 578,   
590, 599   
left eigenvalues 565   
list of tasks 568   
Markov model transition matrix 858, 859   
MRRR algorithm 589, 599   
multiple eigenvalues 599   
nonlinear 568, 569   
nonsymmetric matrix 590–595   
operation count of balancing 592   
operation count of Givens reduction 578   
operation count of Householder reduction   
582   
operation count of inverse iteration 598, 599   
operation count of Jacobi method 573, 574   
operation count of $Q L$ method 585, 588   
operation count of $\boldsymbol { Q R }$ method for Hessenberg   
matrices 596   
operation count of reduction to Hessenberg   
form 594   
orthogonality 564   
polynomial roots and 469   
$Q L$ method 584–586, 590   
$\boldsymbol { Q R }$ method 67, 567, 571, 584–586   
$\boldsymbol { Q R }$ method for Hessenberg matrices 596   
real symmetric matrix 188, 576, 577, 582,   
992   
reduction to Hessenberg form 594, 595   
relation to singular value decomposition   
(SVD) 569, 570   
right eigenvalues 565   
shifting eigenvalues 563, 585, 596   
special matrices 568   
termination criterion 598, 599   
tridiagonal matrix 567, 576, 577, 583–589,   
598   
genvalue and eigenvector, defined 563   
igenvalue problem for differential equations   
958, 973, 977–981   
genvalues and polynomial root finding 469   
ISPACK 567   
lectromagnetic potential 631   
imination see Gaussian elimination   
lipse in confidence limit estimation 811, 814,   
815   
lliptic integrals 309–316, 1185   
addition theorem 310   
Carlson’s forms and algorithms 310–316   
Cauchy principal value 311

duplication theorem 311 Legendre 309, 314, 315 routines for 311–315 symmetric form 309, 310 Weierstrass 310   
Elliptic partial differential equations 1024 alternating-direction implicit method (ADI) 1065, 1066, 1185 analyze/factorize/operate package 1030 biconjugate gradient method 1030 boundary conditions 1026 comparison of rapid methods 1058 conjugate gradient method 1030 cyclic reduction 1054, 1057, 1058 Fourier analysis and cyclic reduction (FACR) 1053–1058 Gauss-Seidel method 1060, 1061, 1068, 1078 Jacobi’s method 1060, 1061, 1068 matrix methods 1028, 1030 multigrid method 1030, 1066–1083 rapid (Fourier) method 1029, 1054–1057 relaxation method 1028, 1059–1066 spectral methods 1096 successive over-relaxation (SOR) 1061–1066, 1070   
EM algorithm see Expectation-maximization algorithm   
Embedded networks 1168   
Embedded Runge-Kutta method 911, 936   
Encryption 358   
Entropy 754–761, 1006, 1176 chain rule 759 conditional 758–761 of data 1017 relative 756   
EOM (end of message) 1178, 1181   
epsilon () algorithm 212   
Equality constraints 526, 528   
Equations cubic 227–229, 461 differential see Differential equations normal (fitting) 768, 789–793, 1007 quadratic 10, 227–229 see also Differential equations; Partial differential equations; Root finding   
Equilibrium, physical 825   
Equivalence classes 419, 439–441   
Equivalence transformation 208   
Ergodic Markov model 858   
Ergodic property 825   
Error 8–12 checksums for preventing 1172 clocking 1172 discretization 173 double exponential distribution 820 in multigrid method 1067 interpolation 113 local truncation 1077, 1078 Lorentzian distribution 820 nonnormal 779, 812, 818–824 relative truncation 1077 roundoff 10, 11, 229, 1163, 1164 series, advantage of an even 165, 923 systematic vs. statistical 778 trimming 173 truncation 11, 173, 229, 500, 910, 911, 116 varieties of, in PDEs 1036–1038 see also Roundoff error   
Error-correcting codes 851–855 Berlekamp-Massey decoding algorithm 852 binary block code 851 codeword 851 correcting bit errors 855 coset leader 852 Golay code 852 Hamming code 852 Hamming distance 851, 1168 hard-decision decoding 853 linear codes 851 minimal trellis 853 parity-check matrix 851 perfect code 852 Reed-Solomon 852, 855 soft-decision decoding 853 syndrome 852 syndrome decoding 852 trellis 853, 856 turbo codes 855 Viterbi decoding 854, 855   
Error ellipse, how to draw 817, 847   
Error function 259, 264–266, 718 approximation via sampling theorem 718, 719 Chebyshev approximation 264 complex 302 Fisher’s z-transformation 747 inverse 264 relation to Dawson’s integral 302 relation to Fresnel integrals 298 relation to incomplete gamma function 264 routine for 264 significance of correlation 746 sum squared difference of ranks 750   
Error handling in programs 2, 30, 31, 35   
Estimation of parameters see Fitting; Maximum likelihood estimate   
Estimation of power spectrum 681–684   
Euclid 1098   
Euler equation (fluid flow) 1037   
Euler-Maclaurin summation formula 164, 167   
Euler’s constant 267, 269, 300   
Euler’s method for differential equations 900, 907, 931   
Euler’s transformation 211, 212   
Evaluation of functions see Function   
Even and odd parts, of continued fraction 208, 260, 267   
Even parity 1168   
Exception handling in programs 2, 30, 31, 35   
Expectation-maximization algorithm 842–844 expectation step (E-step) 843 for hidden Markov model 866 maximization step (M-step) 843 relation to Baum-Welch re-estimation 866   
Explicit differencing 1032   
Exponent in floating point format 8, 1164   
Exponential convergence 174–178, 180, 238, 239, 1083–1096   
Exponential integral 266–269 asymptotic expansion 269 continued fraction 267 recurrence relation 219 related to incomplete gamma function 267 relation to cosine integral 301 routine for $\operatorname { E i } ( x )$ 269 routine for $E _ { n } ( x )$ 268 series 267   
Exponential probability distribution 326, 327, 686 deviate from 362 relation to Poisson process 369, 829   
Extended midpoint rule 157, 161, 167   
Extended precision, use in iterative improvement 62   
Extended Simpson’s rule 160, 994, 997 three-eighths rule 995   
Extended trapezoidal rule 157, 159, 162, 167, 993 roundoff error 165   
Extirpolation (so-called) 690, 691   
Extrapolation 110–154 Bulirsch-Stoer method 922, 924 by linear prediction 673–681 differential equations 900 local 911 maximum entropy method as type of 683 polynomial 922, 924, 943 rational function 922 relation to interpolation 110 Romberg integration 166 see also Interpolation   
Extremization see Minimization   
$F$ -distribution probability function 332, 333 deviates 371   
F-test for differences of variances 728, 730   
FACR see Fourier analysis and cyclic reduction (FACR)   
Facsimile standard 1180   
Factorial evaluation of 210 relation to gamma function 256 representability 257 routine for 257 routine for log 258   
False position 449, 452, 454   
Family tree 440   
FAS (full approximation storage algorithm) 1076–1083

st Fourier transform (FFT) 608–616, 640, 11   
alternative algorithms 615, 616   
applications 640–719   
approximation to continuous transform 608   
bare routine for 611   
bit reversal 610, 638   
butterfly 360, 361, 610   
Clenshaw-Curtis quadrature 241   
convolution 616, 631, 641–647, 1189   
convolution of large data sets 646, 647   
Cooley-Tukey algorithm 616   
correlation 648, 649   
cosine transform 241, 624–627, 1056   
cosine transform, second form 625, 1057   
Danielson-Lanczos lemma 609, 610, 638   
data sets not a power of 2 616   
data smoothing 766, 767   
data windowing 655–667   
decimation-in-frequency algorithm 616   
decimation-in-time algorithm 615   
decomposition into blocks 614   
differentiation matrix using 1092   
discrete autocorrelation 649   
discrete convolution theorem 642, 643   
discrete correlation theorem 648   
double frequency 690   
endpoint corrections 694   
external storage 637, 638   
figures of merit for data windows 658   
filtering 667–672   
FIR filter 668, 669   
for quadrature 156   
for spherical harmonic transforms 296   
four-step framework 615   
Fourier integrals 692–699   
Fourier integrals,infinite range 699   
history 609   
IIR filter 668–672   
image processing 1010, 1012   
integrals using 156   
inverse of sine transform 623   
large data sets 637, 638   
leakage 655, 656   
Lomb periodogram and 689   
memory-local algorithm 638   
multidimensional 627–630   
multiple precision arithmetic 1185   
multiple precision multiplication 1189   
number-theoretic transforms 616   
of real data in 2D and 3D 631–637   
of real functions 617–627, 631–637   
of single real function 618–620   
of two real functions simultaneously 617, 6   
operation count 609, 610   
optimal (Wiener) filtering 649–652, 673, 67   
order of storage in 611   
parallel 614   
partial differential equations 1029,   
1054–1057   
periodicity of 608

periodogram 653–656, 681, 683 power spectrum estimation 652–667 related algorithms 615, 616 Sande-Tukey algorithm 616 sine transform 620–623, 1055 Singleton’s algorithm 637, 638 six-step framework 615 spectral methods 1086 treatment of end effects in convolution 643 treatment of end effects in correlation 648 Tukey’s trick for frequency doubling 690 two real functions simultaneously 617 use in smoothing data 766, 767 virtual memory machine 638 Winograd algorithms 616 zoom transforms 615 see also Discrete Fourier transform (DFT); Fourier transform; Spectral density Fast Legendre transform 295, 297 Fast multipole methods 140, 1150 FASTA (software) 562 Faure sequence 404 Fax (facsimile) Group 3 standard 1180 Feasible vector 526, 538 basis vector 528 Fermi-Dirac integral 178 FFT see Fast Fourier transform (FFT) Field, in data record 428 Figure-of-merit function 773 __FILE__ (ANSI C macro) 30 Fill-in, sparse linear equations 59, 76, 535, 544 Filon’s method 698 Filter 667–672 acausal 668 bilinear transformation method 670, 672 by fast Fourier transform (FFT) 637, 649, 667–672 causal 668, 767, 770 characteristic polynomial 670 data smoothing 766 digital 667–672 DISPO 767 finite impulse response (FIR) 642, 643, 668, 669 homogeneous modes of 670 infinite impulse response (IIR) 668–672, 681 Kalman 824 linear 668–672 low-pass for smoothing 766 nonrecursive 668 optimal (Wiener) 645, 649–652, 673, 674, 767 quadrature mirror 701, 708 realizable 668, 670, 671 recursive 668–672, 681 Remes exchange algorithm 669 Savitzky-Golay 232, 766–772 stability of 670, 671 time domain 667–672 Fine-to-coarse operator 1068

Finite difference equations (FDEs) 964, 970, 98 accuracy of 1085 alternating-direction implicit method (ADI) 1052, 1053, 1065, 1066 art, not science 1035 Cayley’s form for unitary operator 1049 Courant condition 1034, 1036, 1038, 1042 Courant condition (multidimensional) 1051 Crank-Nicolson method 1045, 1049, 1051, 1052 eigenmodes of 1033, 1034 explicit vs. implicit schemes 1033 forward Euler 1032 forward time centered space (FTCS) 1032, 1044, 1049, 1059 implicit scheme 1045 in relaxation methods 964 Lax method 1034–1036, 1042 Lax method (multidimensional) 1050, 1051 mesh drifting instability 1040 numerical derivatives 229 partial differential equations 1027 relation to spectral methods 1093 staggered leapfrog method 1038, 1039 two-step Lax-Wendroff method 1040 upwind differencing 1037, 1042 see also Partial differential equations   
Finite element methods 132, 1030   
Finite impulse response (FIR) 642, 643   
FIR (finite impulse response) filter 668, 669   
First-class objects 397   
Fisher discriminant algorithm 892   
Fisher’s z-transformation 746   
Fitting 773–838 basis functions 788 by Chebyshev approximation 234 by rational Chebyshev approximation 247–251 chi-square 778–780 confidence levels from singular value decomposition (SVD) 816, 817 confidence levels related to chi-square values 812–816 confidence limits on fitted parameters 807–817 covariance matrix not always meaningful 774, 812 degeneracy of parameters 797 exponential, an 797 freezing parameters in 791, 824 Gaussians, a sum of 805 general linear least squares 788–798 how much $\Delta \chi ^ { 2 }$ is significant 816 K–S test, caution regarding 740 Kalman filter 824 kriging 836–838 least squares 776–780 Legendre polynomials 797 Levenberg-Marquardt method 801–806, 1022 linear regression 780–785 Markov chain Monte Carlo 824–835 maximum likelihood estimation 777, 818 Monte Carlo simulation 740, 779, 807–810 multidimensional 798, 836–838 nonlinear models 799–806 nonlinear models, advanced methods 806 nonlinear problems that are linear 797 nonnormal errors 781, 812, 818–824 of sharp spectral features 682 polynomial 94, 129, 241, 243, 768, 788, 797 robust methods 818–824 standard (probable) errors on fitted parameters 781, 782, 786, 787, 790, 794, 795, 807–817 straight line 780–785, 822–824 straight line, errors in both coordinates 785–787 see also Error; Least-squares fitting; Maximum likelihood estimate; Robust estimation   
Five-point difference star 1071   
Fixed point format 8   
Fletcher-Powell algorithm see Davidon-Fletcher-Powell algorithm   
Fletcher-Reeves algorithm 489, 515–519   
Floating point format 8–11, 1163–1165 care in numerical derivatives 229, 230 in computational geometry 1098 enabling exceptions 35, 575 history 1163 IEEE 9, 10, 34, 1164 little- vs. big-endian 9 NaN 34, 35   
Flux-conservative initial value problems 1031–1043   
FMG (full multigrid method) 1067, 1072–1076   
for iteration 14   
Formats of numbers 8–11, 1163–1165   
Fortran 1 INTENT attribute 26   
Forward-backward algorithm as a sum-product algorithm 867 Bahl-Cocke-Jelinek-Raviv algorithm 867 belief propagation 867 compared to Viterbi decoding 867 hidden Markov model 861, 862, 864–867 renormalization 862   
Forward deflation 464, 465   
Forward difference operator 212   
Forward Euler differencing 1032   
Forward Time Centered Space see FTCS   
Four-step framework, for FFT 615   
Fourier analysis and cyclic reduction (FACR) 1054, 1058   
Fourier and spectral applications 600, 640–719   
Fourier integrals attenuation factors 698 endpoint corrections 694 tail integration by parts 699 use of fast Fourier transform (FFT) 692–699

urier series as basis functions for spectral   
methods 1085   
ourier transform 110, 600–640   
aliasing 606, 685   
approximation of Dawson’s integral 303   
autocorrelation 602   
basis functions compared 621   
contrasted with wavelet transform 699, 700,   
711   
convolution 602, 616, 617, 631, 641–647,   
1189   
correlation 602, 617, 648, 649   
cosine transform 241, 624–627, 1056   
cosine transform, second form 625, 1057   
critical sampling 605, 653, 655   
decomposition into blocks 614   
definition 600   
discrete Fourier transform (DFT) 233, 236,   
605–608   
Gaussian function 717, 718   
image processing 1010, 1012   
infinite range 699   
inverse of discrete Fourier transform 608   
method for partial differential equations   
1054–1057   
missing data 685   
missing data, fast algorithm 689–692   
Nyquist frequency 605, 607, 632, 653, 655,   
685   
optimal (Wiener) filtering 649–652, 673, 674   
Parseval’s theorem 602, 603, 608, 654   
power spectral density (PSD) 602, 603   
power spectrum estimation by FFT 652–667   
power spectrum estimation by maximum   
entropy method 681–684   
properties of 601   
sampling rate 605   
sampling theorem 605, 653, 655, 717–719   
scalings of 601   
significance of a peak in 686   
sine transform 620–623, 1055   
symmetries of 601   
uneven sampling, fast algorithm 689–692   
unevenly sampled data 685–692   
wavelets and 707, 708   
Wiener-Khinchin theorem 602, 674, 682   
see also Fast Fourier transform (FFT); Spectral   
density   
ractal region 462   
actional step methods 1052   
edholm alternative 987   
redholm equations 986   
eigenvalue problems 987, 992   
error estimate in solution 991   
first kind 986   
Fredholm alternative 987   
homogeneous vs. inhomogeneous 987   
homogeneous, second kind 991   
ill-conditioned 987   
infinite range 995

inverse problems 987, 1001–1006 kernel 986 nonlinear 988 Nystrom method 989–992, 995 product Nystrom method 995 second kind 987–992 subtraction of singularity 996 symmetric kernel 992 with singularities 995–1000 with singularities, worked example 999, 1000 see also Inverse problems   
Frequency domain 600   
Frequency spectrum see Fast Fourier transform (FFT)   
Frequentist, contrasted with Bayesian 774   
Fresnel integrals 297–300 asymptotic form 298 continued fraction 298 routine for 299 series 298   
Friday the 13th 7   
FSAL (first-same-as-last) 913   
FTCS (forward time centered space) 1032, 1044, 1049 stability of 1033, 1044, 1060   
Full approximation storage (FAS) algorithm 1076–1083   
Full conditional distribution 827   
Full moon 7   
Full multigrid method (FMG) 1067, 1072–1076   
Full Newton methods, nonlinear least squares 806   
Full pivoting 43   
Full weighting 1071   
Function Airy 254, 283, 289, 291 approximation 110, 233–239 associated Legendre polynomial 293, 971 autocorrelation of 602 bandwidth limited 605 Bessel 219, 254, 274–292 beta 258, 259 branch cuts of 252–254 chi-square probability 1003 complex 251 confluent hypergeometric 254, 287 convolution of 602, 617 correlation of 602, 617 Coulomb wave 254, 283 cumulative distribution (cdf) 320–339 Dawson’s integral 302, 304, 717 digamma 267 elliptic integrals 309–316, 1185 error 264–266, 298, 302, 718, 746, 750 error function 259 evaluation 201–254 evaluation by path integration 251–254, 318 exponential integral 219, 266–269, 301 factorial 256, 257 Fermi-Dirac integral 178

Fresnel integral 297–300 functor 21–23, 444, 459, 905 gamma 256, 257 hypergeometric 252, 318–320 incomplete beta 270–273 incomplete gamma 259–263, 732, 779 inverse cumulative distribution 320–339 inverse hyperbolic 227, 310 inverse incomplete gamma 263 inverse of $x \log ( x )$ 307–309, 335 inverse trigonometric 310 Jacobian elliptic 309, 316, 317 Kolmogorov-Smirnov probability 737, 763 Legendre polynomial 219, 293, 797 log factorial 258 logarithm 310 minimization 487–562 modified Bessel 279–283 modified Bessel, fractional order 287–289 object 21 path integration to evaluate 251–254 pathological 111, 445 probability 320–339 representations of 600 routine for plotting a 444 sine and cosine integrals 297, 300–302 sn, dn, cn 316, 317 spherical Bessel 283 spherical harmonics 292–297 spheroidal harmonic 971–981 statistical 320–339 templated 17, 22, 26 utility 17 virtual 33 Weber 254 unction object see Functor unctional iteration, for implicit equations 943 unctor 21–23, 202, 204, 237, 240, 444, 459, 660, 905, 936, 940 WHM (full width at half maximum) 659

solution of normal equations 790 storage requirements 44 Gauss-Kronrod quadrature 192, 195 Gauss-Laguerre integration 183, 995 Gauss-Legendre integration 183, 193 see also Gaussian integration Gauss-Lobatto quadrature 191, 192, 195, 241, 624, 1089 Gauss-Markov estimation 144 Gauss-Radau quadrature 191 Gauss-Seidel method (relaxation) 1060–1062, 1068 nonlinear 1078 Gauss transformation 310 Gaussian Hardy’s theorem on Fourier transforms 717 multivariate 378, 379, 842, 843, 847, 848, 1006, 1129, 1130 see also Gaussian (normal) distribution Gaussian (normal) distribution 341, 776, 778, 1004 central limit theorem 777 Cholesky decomposition of 847, 848 deviates from 364, 365, 368, 686 kurtosis of 723, 724 multivariate 813, 842 semi-invariants of 725 sum of 12 uniform 377 tails compared to Poisson 778 two-dimensional (binormal) 746 variance of skewness of 723 see also Normal (Gaussian) distribution Gaussian elimination 46–48, 65, 71 fill-in 59, 76, 535 in reduction to Hessenberg form 594 integral equations 993 operation count 47 relaxation solution of boundary value problems 966, 984 Gaussian integration 159, 179–193, 238, 296, 995, 997, 1086–1089 and orthogonal polynomials 181, 1087 calculation of abscissas and weights 182–188 discrete orthogonality relation 1087 error estimate in solution 991 exponential convergence of 180, 1089 extensions of 191–193, 1089 for integral equations 988, 990 from known recurrence relation 188, 189 Golub-Welsch algorithm for weights and abscissas 188 for incomplete beta function 271 for incomplete gamma function 260, 262 nonclassical weight function 189–191, 995 preassigned nodes 191 weight function $\log x$ 190, 191 weight functions 179–181, 995 Gaussian mixture model 842–848 Gaussian process regression 144, 836–838 Gear’s method (stiff ODEs) 934, 941

$^ { \mathrm { g + + } }$ 5   
Gambling 755–758, 760, 761   
Gamma function 256, 257 and area of sphere 1129 complex 257 incomplete see Incomplete gamma function   
Gamma probability distribution 331, 332 as limiting case of beta 333 deviates from 369 relation to Poisson process 829 sum rule for deviates 370   
Gauss-Chebyshev integration 180, 183, 187, 625   
Gauss-Hermite integration 183, 995 abscissas and weights 185 normalization 185   
Gauss-Jacobi integration 183 abscissas and weights 186   
Gauss-Jordan elimination 41–46, 75 operation count 47, 54   
Geiger counter 340   
Gene sequencing alignment algorithms 559–562 hidden Markov model 866   
Generalized eigenvalue problems 568, 569   
Generalized minimum residual method (GMRES) 89   
Genetic algorithms 840   
Geometric series 211, 214   
Geophysics, use of Backus-Gilbert method 1016   
Gerchberg-Saxton algorithm 1012   
Ghostscript 1161   
Gibbs sampler 827, 828 recommended for discrete distributions 828   
Gilbert and Sullivan 920   
Gillespie method 947   
Givens reduction 578–583, 587 fast 578 operation count 578   
Glassman, A.J. 229   
Global optimization 487, 488, 549–555, 774 continuous variables 552–554 difficulty of 803   
Globally convergent minimization 521–525 root finding 474, 477–486, 959, 960, 963   
GLPK (linear programming package) 536   
GMRES (generalized minimum residual method) 89   
GNU $\mathrm { C } { + } { + }$ compiler 5   
GNU Scientific Library 3   
Gnuplot 1162   
Godunov’s method 1043   
Golden mean (golden ratio) 11, 449, 494, 500   
Golden section search 443, 489, 496   
Goldman-Tucker theorem 539   
Golub-Welsch algorithm, for Gaussian quadrature 188   
Goodness-of-fit 773, 779, 782, 783, 787, 813 no good Bayesian methods 779, 1010   
Gram-Schmidt orthogonalization 105, 564, 565, 589, 598 SVD as alternative to 74   
Graphics, function plotting 444, 1160–1163   
Gravitational potential 631   
Gray code 405, 1160, 1166–1168   
Greenbaum, A. 90   
Gregorian calendar 6   
Grid square 132   
Gridding 150–154   
Group, dihedral 1174   
Guard digits 1164   
Half weighting 1071   
Halley’s method 263, 264, 271, 335, 463

Halton’s quasi-random sequence 404   
Hamming code 852   
Hamming distance 873   
error-correcting codes 851, 1168   
Hamming window 658

Hamming’s motto 443   
Hann window 657   
Hard-decision decoding 853 error correction 855   
Harmonic analysis see Fourier transform   
Harwell-Boeing format 83   
Hash collision strategy 387, 390 examples 396 function 352, 387–389 key 387 memory 392–397 multimap memory 394–397 table 386–392 of whole array 358–361   
Heap (data structure) 426, 434, 952, 1178   
Heapsort 420, 426–428, 434   
Helmholtz equation 1057   
Hermite interpolation 916   
Hermite polynomials 183, 185   
Hermitian matrix 564, 590   
Hertz (unit of frequency) 600   
Hessenberg matrix 105, 567, 585, 590–595, 598 QR algorithm 596 see also Matrix   
Hessian matrix 483, 510, 517, 521, 522, 799–801, 1011, 1020, 1021 is inverse of covariance matrix 802 second derivatives in 800, 801   
Hidden Markov model 856–868 backward estimate 861 Baum-Welch re-estimation 865–867 Bayesian nature of 868 Bayesian posterior probability 860, 861, 864 Bayesian re-estimation 864–866 compared to Viterbi algorithm 867, 868 convergence of Baum-Welch re-estimation 866 expectation-maximization algorithm 866 forward-backward algorithm 861, 862, 864–867 forward estimate 860 gene sequencing 866 hidden state 859 know intermediate states 864 missing data 864 observations 859 re-estimation of symbol probability matrix 865 re-estimation of transition probabilities 865 renormalization 862 speech recognition 866 symbols 859 trellis decoding 864 variations 864   
Hierarchical clustering 868–882   
Hierarchically band-diagonal matrix 716   
High-order not same as high-accuracy 112, 156, 238, 489, 500, 908, 911, 943   
High-pass filter 667   
Higher-order statistics 604   
Hilbert matrix 94   
Hilbert’s Third Problem 1127   
Histogram, variable-size bins 438   
Historic maximum entropy method 1022   
Hobson’s choice 704   
Homogeneous linear equations 69   
Hook step methods 486   
HOPDM (software) 548   
Hotelling’s method for matrix inverse 64, 716   
Householder transformation 67, 567, 578–584, 586, 587, 590, 594 in $\boldsymbol { Q R }$ decomposition 103 operation count 582   
Huffman coding 680, 713, 1160, 1175–1181   
Hull, convex 1097, 1132, 1146   
Hyperbolic functions, explicit formulas for inverse 227   
Hyperbolic partial differential equations 1024 advective equation 1032 flux-conservative initial value problems 1031–1043   
Hypergeometric function 252, 318–320 routine for 318, 319   
Hypothesis, null 720   
_I 26, 32, 36   
IBM bad random number generator 344 checksum 1174 radix base for floating point arithmetic 592   
ICF (intrinsic correlation function) model 1022   
Identity (unit) matrix 39   
Idioms 16   
IEEE floating point format 9, 10, 34, 257   
if structure 14 warning about nesting 14   
IIR (infinite impulse response) filter 668–672, 681   
Ill-conditioned integral equations 987   
Image processing 631, 1010 as an inverse problem 1010 cosine transform 625 fast Fourier transform (FFT) 631, 637, 1010 from modulus of Fourier transform 1012 maximum entropy method (MEM) 1016–1022 QO tree and 1150 wavelet transform 713, 715   
Implicit function theorem 442 pivoting 44 shifts in $Q L$ method 586–589   
Implicit differencing 1033 for diffusion equation 1045 for stiff equations 932, 933, 944   
Importance sampling, in Monte Carlo 411, 412, 414, 835, 836   
Improper integrals 167–172   
Impulse response function 641–643, 649, 668   
IMSL 3, 40, 76, 466, 470, 568   
IMT (Iri, Moriguti, Takasawa) rule 173   
In-place selection 439   
Include files 3, 4   
Incomplete beta function 270–273 for F-test 730 for Student’s t 729 routine for 273   
Incomplete gamma function 259–263 deviates from 369 for chi-square 732, 779 inverse 263   
Increment of linear congruential generator 343   
Incremental quantile estimation 435 changes with time 438   
Indentation of blocks 14   
Index table 419, 426, 428–431   
Inequality constraints 526, 528, 538   
Inference 840–898   
Information mutual 758–761 side 760, 761 theory 754–761   
Inheritance 23, 24 examples of in NR 23   
Initial value problems 900, 1024, 1026 see also Differential equations;   
Injection operator 1068   
inline directive 29   
Inscribed circle (incircle) 1112   
Instability see Stability   
Instantiation 18, 19   
Int, __int32, __int64 25   
Integer programming 536   
Integral equations 986–1023 adaptive stepsize control 995 block-by-block method 994 correspondence with linear algebraic equations 986 degenerate kernel 992 eigenvalue problems 987, 992 error estimate in solution 991 Fredholm 986, 989–992 Fredholm alternative 987 homogeneous, second kind 991 ill-conditioned 987 infinite range 995 inverse problems 987, 1001–1006 kernel 986 nonlinear 988, 994 Nystrom method 989–992, 995 product Nystrom method 995 solving with sinc expansions 178 subtraction of singularity 996 symmetric kernel 992 unstable quadrature 994 Volterra 988, 992–995 wavelets 989 with singularities 995–1000 with singularities, worked example 999, 10 see also Inverse problems   
Integral operator, wavelet approximation of 71 989   
Integration of functions 155–200 Chebyshev approximation 240, 241 cosine integrals 300 Fourier integrals 692–699 Fourier integrals, infinite range 699 Fresnel integrals 297 Gauss-Hermite 185 Gauss-Jacobi 186 Gauss-Laguerre 184 Gauss-Legendre 183 infinite ranges 176–178 integrals that are elliptic integrals 309 path integration 251–254 sine integrals 300 see also Quadrature   
Integro-differential equations 989   
INTENT attribute (Fortran) 26   
Interior-point method 85, 536–549 see also Linear Programming   
Intermediate value theorem 445   
Interpolation 110–154 Aitken’s algorithm 118 avoid in Fourier analysis 685 barycentric rational 113, 127, 128 bicubic 136–138 biharmonic 153 bilinear 133, 134 caution on high-order 112, 113 coefficients of polynomial 111, 129–131, 241, 243, 690 curve 139, 147 error estimates for 111 for computing Fourier integrals 694 for differential equation output 916 functions with poles 124 grid, on a 132–135 Hermite 916 inverse multiquadric 142 inverse quadratic 454, 496 irregular grid 139–149, 1097, 1141, 1142 kriging 144–147 Laplace/Poisson 150–154 minimum curvature 153 multidimensional 113, 132–135, 139–154 multigrid method, in 1070–1072 multiquadric 141 Neville’s algorithm 118, 231, 924 normalized radial basis functions 140 Nystrom 990 open vs. closed curve 148 operation count for 111 operator 1068 order of 112 ordinary differential equations and 113 oscillations of polynomial 112, 129, 489, 5 parabolic, for minimum finding 496–499

polynomial 110, 118–120, 231, 924 pseudospectral method and 1087 radial basis functions 139–144 rational Chebyshev approximation 247–251 rational function 110, 113, 124–128, 245, 275, 922 reverse (extirpolation) 690, 691 scattered data 139–154 Shepard’s method 140 spline 111, 120–124, 135 trigonometric 110 see also Fitting Intersection line and sphere 1121 line and triangle 1121 line segments 1118 lines 1117 QO tree used to find 1150 Intersections 1097 Interval variable (statistics) 741 Intrinsic correlation function (ICF) model 1022 Inverse function of $x$ $\log ( x )$ 307–309, 335 Inverse hyperbolic function 227, 310 Inverse iteration see Eigensystems stable equilibrium of Markov model 859 Inverse multiquadric 142 Inverse problems 987, 1001–1006 and integral equations 987 Backus-Gilbert method 1014–1016 Bayesian approach 1005, 1022 central idea 1005 constrained linear inversion method 1006 data inversion 1014 deterministic constraints 1011–1013 Gerchberg-Saxton algorithm 1012 in geophysics 1016 incomplete Fourier coefficients 1018, 1020 linear regularization 1006–1013 maximum entropy method (MEM) 1016–1022 MEM demystified 1019, 1020 optimally localized average 1014–1016 Phillips-Twomey method 1006 principal solution 1004 regularization 1002–1006 regularizing operator 1004 stabilizing functional 1004 Tikhonov-Miller regularization 1007 trade-off curve 1002, 1016 two-dimensional regularization 1010, 1011 use of conjugate gradient minimization 1011, 1020 use of convex sets 1011–1013 use of Fourier transform 1010, 1012 Van Cittert’s method 1011 Inverse quadratic interpolation 454, 496 Inverse response kernel, in Backus-Gilbert method 1014 Inverse trigonometric function 310 _IO 26, 32, 36

IQ (incremental quantile) agent 435   
Irreducibility of Markov model 858   
Irreducible polynomials modulo 2 382   
Irregular grid, interpolation on 139–149, 1141, 1142   
Is-a relationship 23   
ISBN (International Standard Book Number) checksum 1173   
Iterated integrals 196, 197   
Iteration 14 for linear algebraic equations 40 functional 943 in root finding 443 required for two-point boundary value problems 955–957 to improve solution of linear algebraic equations 61–65, 245   
Iteration matrix 1060   
Jacobi matrix, for Gaussian quadrature 188   
Jacobi transformation (or rotation) 105, 567, 570–576, 578, 590, 599 decorrelating random variables 380   
Jacobi’s method (relaxation) 1060, 1061, 1068   
Jacobian determinant 364, 981   
Jacobian elliptic functions 309, 316, 317   
Jacobian matrix 475, 477, 480, 483, 540, 935, 936 singular in Newton’s rule 486   
Java 1, 12   
Jenkins-Traub method 470   
Jordan curve theorem 1124   
JPEG-2000 standard 712   
Julian Day 3, 6   
Jump transposition errors 1174

two-dimensional 762–766 variants 738, 762 Kriging 139 fitting by 836–838 fitting not same as interpolation 838 interpolation by 144–147 is Gaussian process regression 837 linear prediction and 674, 679 nugget effect 838 Kuiper’s statistic 739 Kullback-Leibler distance 756–758 symmetrized 757 Kurtosis 723, 725

K-means clustering 848–850   
K-S test see Kolmogorov-Smirnov test   
Kalman filter 824   
Kaps-Rentrop method 934   
KD tree 1101–1110 construction of 1102–1106 number of boxes in 1102   
Kelly’s formula 758   
Kendall’s tau 749, 751–754   
Kernel 986 averaging, in Backus-Gilbert method 1014 degenerate 992 finite rank 992 inverse response 1014 separable 992 singular 995 symmetric 992   
Kernel methods of classification 840, 889, 892   
Keys used in sorting 428   
KKT (Karush-Kuhn-Tucker) conditions 539, 542, 886, 889   
Kolmogorov-Smirnov probability distribution 334–336   
Kolmogorov-Smirnov test 731, 736–738, 819   
L-estimate 818   
Lag 602, 648, 669   
Lagged Fibonacci generator 354   
Lagrange multiplier 758, 760, 1001   
Lagrange’s formula for polynomial interpolation 94, 118, 690, 691, 694, 1089, 1092   
Laguerre polynomials 183   
Laguerre’s method 444, 466–469 convergence 466   
Lanczos lemma 609, 610   
Lanczos method for gamma function 256   
Landen transformation 310   
LAPACK 40, 567   
Laplace’s equation 292, 1024 see also Poisson equation   
Laplace/Poisson interpolation 150–154   
Las Vegas 744   
Latin square or hypercube 409, 410   
Latitude/longitude in $n$ -dimensions 1128   
Laurent series 681, 682   
Lax method 1034–1036, 1042, 1050, 1051 multidimensional 1050, 1051   
Lax-Wendroff method 1040   
LCG see Linear congruential random number generator   
ldexp 207, 279, 283   
LDL 544, 548   
Ldoub 25   
Leakage in power spectrum estimation 655, 656, 658, 662–665   
Leakage width 658, 659   
Leapfrog method 1038, 1039   
Least-squares filters see Savitzky-Golay filters   
Least-squares fitting 776–798 degeneracies in 794, 795, 797 Fourier components 686 freezing parameters in 791, 824 general linear case 788–798 how much $\Delta \chi ^ { 2 }$ is significant 816 Levenberg-Marquardt method 801–806, 1022 Lomb periodogram 686 maximum likelihood estimator 777 method for smoothing data 768 multidimensional 798 nonlinear 486, 799–806, 1022 nonlinear, advanced methods 806 normal equations 768, 789–793, 1007 normal equations often singular 793, 797 optimal (Wiener) filtering 650 $\boldsymbol { Q R }$ method in 105, 791 rational Chebyshev approximation 249 relation to linear correlation 745, 783 Savitzky-Golay filter as 768 singular value decomposition (SVD) 39, 65–75, 249, 793 skewed by outliers 778 spectral analysis 686 standard (probable) errors on fitted parameters 794 weighted 777 see also Fitting   
Left eigenvalues or eigenvectors 564, 565   
Legendre elliptic integral see Elliptic integrals   
Legendre polynomials 183, 293 basis functions for spectral methods 1086 fitting data to 797 recurrence relation 219 see also Associated Legendre polynomials; Spherical harmonics   
Lehmer-Schur algorithm 470   
Lemarie’s wavelet 708   
Lentz’s method for continued fraction 207, 260   
Lepage, P. 414   
Leptokurtic distribution 723   
Levenberg-Marquardt algorithm 486, 801–806, 1022 advanced implementation 806   
Levin transformation 214   
Levinson’s method 96   
Liapunov stability 933   
Likelihood ratio 735, 757   
Limbo 457   
Limit cycle Laguerre’s method 466 Markov model 858   
Line 1097, 1117–1121 closest approach of two 1121 closest approach to point 1121 distance of point to 1118 equation satisfied by 1117 in 3 dimensions 1121 intersection of two 1117 intersection with sphere 1121 intersection with triangle 1121 left-of relations 1118 segments 1118–1120 skew 1121 _LINE__ (ANSI C macro) 30   
Line minimization see Minimization, along a ray   
Line search see Minimization, along a ray   
Linear algebraic equations 37–109 and integral equations 986, 990 band-diagonal 58–61 biconjugate gradient method 88 Cholesky decomposition 100–102, 378, 379, 525, 543, 568, 791 complex 55 computing A-1 - B 53 conjugate gradient method 87–92, 716 cyclic tridiagonal 79, 80 direct methods 40, 76 Gauss-Jordan elimination 41–46 Gaussian elimination 46, 48 Hilbert matrix 94 Hotelling’s method 64, 716 iterative improvement 61–65, 245, 548 iterative methods 40, 87–92 large sets of 38, 39 least-squares solution 65, 70, 73, 249, 793 $_ { L U }$ decomposition 48–55, 245, 483, 484, 486, 534, 936, 990, 1008 nonsingular 38, 39 overdetermined 39, 249, 793, 1004 parallel solution 57 partitioned 81 QR decomposition 102–106, 483, 484, 486, 791 row vs. column elimination 45, 46 Schultz’s method 64, 716 Sherman-Morrison formula 76–79, 94, 534 singular 38, 69, 73, 249, 793 singular value decomposition (SVD) 65–75, 249, 793, 1003 sparse 39, 58, 75–92, 534, 544, 548, 937, 1011 summary of tasks 39, 40 Toeplitz 93, 96–99, 245 Vandermonde 93–96, 130 wavelet solution 715, 716, 989 Woodbury formula 80, 81, 94 see also Eigensystems   
Linear codes 851   
Linear congruential random number generator 341, 343, 348   
Linear constraints 526, 530   
Linear convergence 448, 495   
Linear correlation (statistics) 745–748   
Linear dependency constructing orthonormal basis 74, 105 in linear algebraic equations 38 of directions in $N$ -dimensional space 511   
Linear equations see Differential equations; Integral equations; Linear algebraic equations   
Linear feedback shift register (LFSR) 346, 380–386 state vector 380 update rule 380   
Linear inversion method, constrained 1006   
Linear optimization 526   
Linear prediction 673–681 characteristic polynomial 676 coefficients 673–681 compared with regularization 1008 contrasted to polynomial extrapolation 675, 677 is Gaussian process regression 837

kriging and 144   
multidimensional 836–838   
related to optimal filtering 673, 674   
removal of bias in 145, 678, 679   
stability 676   
near predictive coding (LPC) 679–681   
near programming 488, 526–549   
affine scaling 543   
artificial variables 530, 531   
augmented equations 543, 548   
auxiliary objective function 530   
barrier method 541   
basic variables 529, 531   
boundary 528   
bounded variables 535, 546   
centering parameter 541   
central path 540   
complementarity condition 539   
complementary slackness theorem 539   
constraints 526, 530   
cycling 534   
degenerate basis 533   
Devex 535   
dual algorithm 535   
dual feasible basis vector 538   
dual interior-point method 542   
dual problem 538, 539   
duality gap 538   
duality measure 541   
efficiency 537, 541   
ellipsoid method 537   
equality constraints 526, 528   
feasible basis vector 528, 529, 532   
feasible vector 526, 538   
free variables 538   
fundamental theorem 528   
Goldman-Tucker theorem 539   
inequality constraints 526, 528, 538   
infeasible method 537   
interior-point method 85, 488, 536–549   
KKT conditions 539, 542   
logical variables 530, 538   
long-step method 541   
minimum ratio test 532   
multiple pricing 535   
nonbasic variables 529, 531   
normal equations 85, 543, 548   
objective function 526, 528, 530   
optimal feasible vector 526, 528, 532   
path-following method 541   
phases one and two 530   
predictor-corrector method 547   
primal algorithm 535   
primal-dual interior-point method 542   
primal-dual solution 539   
primal interior-point method 542   
primal problem 538   
reduced cost 531   
scaling of variables 535, 546   
short-step method 541

simplex method 488, 502, 526–536, 548 simplex vs. interior-point 548 slack variables 529, 531, 535, 538, 547 sparse linear algebra 534, 544, 548 stalling 534 standard form 529, 530, 538 steepest edge pricing 535 strict complementarity 539 strong duality theorem 539 structural variables 530 surplus variables 529 unbounded objective function 532, 538 vertex of simplex 528, 531 weak duality theorem 538 worked example 530–533 zero variables 530   
Linear regression 780–787 see also Fitting   
Linear regularization 1006–1013   
Linearly separable data 884   
LINPACK 40, 567   
Little-endian 9, 34   
Llong 25   
Local extrapolation 911, 914   
Local extremum 487, 551   
Localization of roots see Bracketing   
Log-sum-exp formula 844   
Logarithmic function 310 barrier function 541 inverse of $x$ log.x/ 307–309, 335   
Logistic probability distribution 324–326 deviates from 363   
Lognormal probability distribution 328, 329, 827   
Lomb periodogram method of spectral analysis 685–687 fast algorithm 689–692   
long long int 25   
Loops 14   
Lorentzian distribution 322   
Lorentzian probability distribution 820   
Low-pass filter 667, 766   
LP coefficients see Linear prediction   
LPC (linear predictive coding) 679–681   
lp solve 535, 536   
$_ { L U }$ decomposition 48–55, 62, 65, 71, 75, 108, 475, 534, 790, 936 band-diagonal matrix 59 Bartels-Golub update 535 complex equations 55 Crout’s algorithm 49, 59 fill-in, minimizing 535 for ${ \bf A } ^ { - 1 }$ - B 53 for integral equations 990 for inverse iteration of eigenvectors 598 for inverse problems 1008 for matrix inverse 54 for nonlinear sets of equations 475, 486 for Pade approximant 245 ´ for Toeplitz matrix 98 operation count 49, 54

pivoting 50, 535 repeated backsubstitution 54, 60 solution of linear algebraic equations 54 solution of normal equations 790 stable equilibrium of Markov model 859 threshold partial pivoting 535 Lucifer (encryption algorithm) 358 Lucy’s $Y ^ { 2 }$ and $Z ^ { 2 }$ statistic 735 LUSOL 535

M-estimates 818 how to compute 821, 822 local 819–821 see also Maximum likelihood estimate   
Machine accuracy 10, 1163   
Machine learning 840 supervised 883 support vector machine 883–898 unsupervised 842, 868   
Macintosh, see Apple Macintosh   
Maehly’s procedure 465, 472   
Magic in MEM image restoration 1019, 1020 in Pade approximation 246, 247 ´   
Mantissa in floating point format 8–10, 1164   
Mantissa in floating-point format 1189   
Maple (software) 3   
Marginals 743, 759, 825   
Markov chain 825   
Markov chain Monte Carlo 551, 774, 824–836 acceptance probability 827, 832 best stepsize 832 burn-in 826, 833–835 candidate point 827 compared to Monte Carlo integration 825 convergence diagnostics 835 converges to sample, not population, values 834 correlated directions 831 correlation time 834 detailed balance equation 825, 827 ergodic average 834 ergodic behavior 825 fitting model parameters 825 full conditional distributions 827 Gibbs sampler 827, 828 and inverse problems 1006 lognormal steps 827 Metropolis-Hastings algorithm 826, 827 normalizing constant 825, 828, 835, 836 parallel computing 835 parameter uncertainties 833 proposal distribution 826–828, 835 proposal generator 830 rapid mixing 826, 831 variable dimension models 835   
Markov model 856–868 aperiodic 858 as ensemble 857 convergence 858 corrected phylogenetic distance for 873 diagnosing 858, 859 directed graph 856 equilibrium distribution 857 ergodic 858 evolution in time 857 hidden 856–868 inverse iteration 859 irreducible 858 limit cycle 858 $_ { L U }$ decomposition 859 multiple equilibria 859 population vector 857 transition matrix 856 transition probability 856 unstable equilibria 858, 859   
Markowitz criterion 535   
Marquardt method (least-squares fitting) 801–806, 1022   
Mass, center of 399, 400   
MasterCard checksum 1174   
MatDoub , MatInt, etc. 26   
Mathematica (software) 1, 3   
Mathematical Center (Amsterdam) 454   
Matlab 1, 3   
Matrix 37, 38 approximation of 74, 75, 715 band-diagonal 56, 58–61, 76 band triangular 76 banded 40, 568 bidiagonal 67 block diagonal 76, 964, 966 block triangular 76 block tridiagonal 76 bordered 76 characteristic polynomial 563, 583 Cholesky decomposition 100–102, 378, 379, 525, 543, 568, 791 class for 24–29 column augmented 42, 43 complex 55 condition number 69, 89 curvature 800 cyclic banded 76 cyclic tridiagonal 79, 80 defective 564, 591, 598, 599 of derivatives see Hessian matrix; Jacobian determinant design (fitting) 768, 788 determinant of 39, 54, 55 diagonalization 566 distance 869 elementary row and column operations 42, 43 finite differencing of partial differential equations 1027 Hermitian 564, 568, 590 Hermitian conjugate 564 Hessenberg 105, 567, 585, 590–596, 598 Hessian see Hessian matrix hierarchically band-diagonal 716

Hilbert 94   
identity 39   
ill-conditioned 69, 71, 130, 131   
indexed storage of 82–87   
integral equations and 986, 990   
inverse 39, 41, 47, 54, 76, 78, 81, 82,   
106–108, 565   
inverse by Hotelling’s method 64, 716   
inverse by Schultz’s method 64, 716   
inverse multiplied by a matrix 53   
inverse, approximate 63   
iteration for inverse 63–65, 716   
Jacobi rotation 573   
Jacobi transformation 567, 570–576, 578   
Jacobian 935, 936   
logical multiplication 949   
lower triangular 48, 100, 988   
Moore-Penrose inverse 70   
multiplication denoted by dot 37   
multiplication, optimizing order of 558, 559   
norm 64   
normal 564, 565   
nullity 67, 68   
nullspace 39, 67–70, 72, 563, 1002   
orthogonal 103, 564, 579, 703, 1130   
orthogonal transformation 566, 578, 584   
orthonormal basis 74, 105   
outer product denoted by $\otimes$ 78, 523   
partitioning for determinant 82   
partitioning for inverse 81, 82   
positive-definite 40, 100, 543, 791   
pseudoinverse 70, 73   
$\boldsymbol { Q R }$ decomposition 102–106, 483, 484, 486,   
791   
range 67, 68   
rank 67   
rank-nullity theorem 68   
residual 63   
responsibility 842   
rotation 1097, 1130, 1131   
row and column indices 38   
row vs. column operations 45, 46   
self-adjoint 564, 565   
similarity transform 566, 567, 570, 592, 594   
singular 69, 71, 73, 563   
singular value decomposition 39, 65–75,   
1003   
sparse 39, 75–92, 534, 544, 548, 715, 937,   
964, 966, 1011   
special forms 40   
splitting in relaxation method 1060   
spread 1015   
storage schemes in $\mathrm { C } { + } { + }$ 38   
suffix _I, _O, _IO 26, 32, 36   
symmetric 40, 100, 563, 565, 568, 571,   
576–583, 992   
Toeplitz 93, 96–99, 245   
transpose of sparse 85   
triangular 567

tridiagonal 40, 56–61, 75, 76, 78, 122, 188, 576–589, 598, 1045, 1057, 1058, 1066 tridiagonal with fringes 1028 unitary 564 updating 105, 106, 484 upper Hessenberg 594 upper triangular 48, 103 Vandermonde 93–96, 130 see also Eigensystems; NRmatrix   
Matrix equations see Linear algebraic equations   
Matterhorn 723   
MAX utility function 17   
Maximization see Minimization   
Maximum entropy method (MEM) 681–684, 1006 algorithms for image restoration 1020 Bayesian 1022 Cornwell-Evans algorithm 1021 demystified 1019, 1020 for inverse problems 1016–1022 historic vs. Bayesian 1022 image restoration 1016–1022 intrinsic correlation function (ICF) model 1022 operation count 683 see also Linear prediction   
Maximum likelihood compared with probability 854 trellis decoding 854   
Maximum likelihood estimate (M-estimates) 812, 818 chi-square test 812 defined 777 how to compute 821, 822 mean absolute deviation 820, 822 relation to least squares 777   
Maxwell’s equations 1032   
MCMC see Markov chain Monte Carlo   
Mean absolute deviation of distribution 723, 820 related to median 822   
Mean value theorem 151   
Mean(s) of distribution 722, 723, 725 statistical differences between two 726–730   
Measurement errors 773   
Median 419 by selection 822 calculating 432 changes with time 438 incremental estimation 435 as L-estimate 818 of distribution 722, 725, 726 role in robust straight line fitting 822   
Median-of-three, in Quicksort 423   
MEM see Maximum entropy method (MEM)   
Memory, using scope to manage 20   
Merit function 773 for inverse problems 1004 for straight line fitting 781, 822 for straight line fitting, errors in both coordinates 785 in general linear least squares 788 nonlinear models 799   
Mesh-drift instability 1040   
Mesh generation 1150   
Mesokurtic distribution 723   
Message 754   
Method of lines 1095   
Method of regularization 1006   
Metropolis algorithm 550, 552, 825   
Metropolis-Hastings algorithm 551, 826, 827 Gibbs sampler as special case 827   
Microsoft integer types 26 NaN handling poor 35 Visual $\mathrm { C } { + } { + }$ 5 Windows 5   
Midpoint method see Modified midpoint method; Semi-implicit midpoint rule   
Mikado, or the Town of Titipu 920   
Miller’s algorithm 221, 278   
Min-sum algorithm dynamic programming 556 Viterbi decoding 867   
MIN utility function 17   
Minimal solution of recurrence relation 220, 221   
Minimal trellis 853   
Minimax polynomial 235, 248 rational function 248, 249   
Minimization 487–562 along a ray 88, 478, 489, 507–509, 511, 512, 519–521, 524, 540 annealing, method of simulated 487, 488, 549–555 bracketing of minimum 490–496, 503 Brent’s method 489, 496–500, 785 Broyden-Fletcher-Goldfarb-Shanno algorithm 490, 521–525 by searching smaller subspaces 1021 chi-square 778–780, 799 choice of methods 488–490 combinatorial 549 conjugate gradient method 489, 515–520, 1011, 1020 convergence rate 495, 511 Davidon-Fletcher-Powell algorithm 490, 521, 522 degenerate 1002 direction set methods 489, 509–514 downhill simplex method 489, 502–507, 552, 821 finding best-fit parameters 773 Fletcher-Reeves algorithm 489, 515–519 functional 1001, 1002 global 487, 552–554, 774 globally convergent multidimensional 521–525 golden section search 492–496 in nonlinear model fitting 799 KKT conditions 539, 542 line methods 507–509 linear 526 multidimensional 502–525 of path length 555–562 Polak-Ribiere algorithm 489, 517 Powell’s method 489, 502, 509–514 quasi-Newton methods 477, 489, 521–525 root finding and 476, 477 scaling of variables 523 steepest descent method 516, 1011 termination criterion 493, 503 use for sparse linear systems 87, 89 use in finding double roots 443 using derivatives 489, 499–502 variable metric methods 489, 521–525 see also Linear programming   
Minimum curvature method 153   
Minimum residual method, for sparse system 89   
Minimum spanning tree 1147   
MINPACK 806   
Missing data 150–154, 685 in hidden Markov model 864   
Mississippi River 552, 555   
Mixture model, Gaussian 842–848   
Mixture weight 843   
Mode of distribution 722, 725, 726   
Model-trust region 486, 806   
Modeling of data see Fitting   
Modes, homogeneous, of recursive filters 670   
Modified Bessel functions see Bessel functions   
Modified Lentz’s method, for continued fractions 208   
Modified midpoint method 922, 923   
Modified moments 190   
Modulation, trellis coded 855   
Modulus of linear congruential generator 343   
Moments and quadrature formulas 996 filter that preserves 768 modified problem of 190 of distribution 721–726 problem of 94 semi-invariants 725   
Monic polynomial 181   
Monotonicity constraint, in upwind differencing 1042   
Monte Carlo 197, 341, 397–418 adaptive 410–418 and Kolmogorov-Smirnov statistic 740, 762, 764 bootstrap method 809, 810 comparison of sampling methods 412–414 importance sampling 411, 412, 414, 835, 836 integration 156, 197, 397–403, 410–418 integration compared to MCMC 825 integration, recursive 416 integration, using Sobol’ sequence 408, 409 integration, VEGAS algorithm 414–416 Markov chain 774, 824–836 partial differential equations 1030 quasi-random sequences in 403–410 quick and dirty 809, 810 recursive 410–418 significance of Lomb periodogram 686, 687 simulation of data 779, 807–810, 812 stratified sampling 412–414, 416   
Moore-Penrose inverse 70   
Mother functions 700   
Mother Nature 807, 809   
Moving average (MA) model 681   
Moving window averaging 767   
MRRR algorithm (Multiple Relatively Robust Representations) 589, 599   
Muller’s method 466, 473   
Multidimensional confidence levels of fitting 810, 812, 814, 816 data, use of binning 741 fitting 798, 836–838 Fourier transform 627–630 Fourier transform, real data 631–637 initial value problems 1049–1053 integrals 156, 196–199, 398, 410 interpolation 132–135, 139–154 Kolmogorov-Smirnov test 762–766 minimization 502–525 Monte Carlo integration 397–403, 410 normal (Gaussian) distribution 813 partial differential equations 1049–1053, 1083, 1095 root finding 442–486, 956, 959, 960, 963, 964 search using quasi-random sequence 404 secant method 474, 483 wavelet transform 712, 713   
Multigrid method 1030, 1066–1083 avoid SOR 1070 boundary conditions 1072 choice of operators 1071 coarse-grid correction 1068 coarse-to-fine operator 1068 cycle 1069 dual viewpoint 1077 fine-to-coarse operator 1068 full approximation storage (FAS) algorithm 1076–1083 full multigrid method (FMG) 1067, 1072–1076 full weighting 1071 Gauss-Seidel relaxation 1069 half weighting 1071 importance of adjoint operator 1071 injection operator 1068 interpolation operator 1068 line relaxation 1070 local truncation error 1077, 1078 Newton’s rule 1077, 1079 nonlinear equations 1077 nonlinear Gauss-Seidel relaxation 1078 odd-even ordering 1070, 1073

operation count 1067 prolongation operator 1068 recursive nature 1069 relative truncation error 1077 relaxation as smoothing operator 1069 restriction operator 1068 speeding up FMG algorithm 1076 stopping criterion 1078 straight injection 1071 symbol of operator 1070, 1071 use of Richardson extrapolation 1072 V-cycle 1069 W-cycle 1069 zebra relaxation 1070 Multiple precision arithmetic 1185–1193 Multiple roots 443, 464 Multiplication complex 225 multiple precision 1188 Multiplicative linear congruential generator (MLCG) 341, 344, 348, 349 Multiplier of linear congruential generator 343 Multiply-with-carry (MWC) 347 Multipole methods, fast 140, 1150 Multiquadric 141 Multistep and multivalue methods (ODEs) 900, 942–946 see also Differential Equations; Predictor-corrector methods Multitaper methods 662–665 Multivariate normal deviates 378, 379 distribution 813, 847, 848 Murphy’s Law 509 Mutual information 758–761

NAG 3, 40, 76, 568   
Namespace, why no NR 36   
NaN (not-a-number) 34, 35 how to set and test 34 isnan 35 quiet vs. signalling 35   
Nat 755, 756, 760, 761   
Natural cubic spline 122   
Navier-Stokes equation 1035   
Nearest neighbor 1097, 1101–1110, 1146 all points within specified radius 1109 Delaunay edges connect 1146   
Needle, eye of (minimization) 503   
Needleman-Wunsch algorithm 559   
Negation, multiple precision 1186   
Negentropy 1017–1019   
Neighbor-joining (NJ) method 873, 878–882   
Nelder-Mead minimization method 489, 502–507   
Nested iteration 1072   
Netlib 3   
Networks 1168   
Neumann boundary conditions 1026, 1045, 1056, 1057, 1063   
Neural networks 840, 883   
Neutrino 762   
Neville’s algorithm 118, 125, 166, 231   
Newton-Cotes formulas 158, 179 open 158, 159   
Newton-Raphson method see Newton’s rule   
Newton’s rule 182, 229, 443, 444, 456–462, 46 466, 470, 584 caution on use of numerical derivatives 459 extended by Halley 463 first published by Raphson 456 for interior-point method 539 for matrix inverse 64, 716 for reciprocal of number 1190 for square root of number 1191 fractal domain of convergence 462 globally convergent multidimensional 474, 477–486, 959, 960, 963 in multidimensions 472–476, 959, 960, 96 964 in nonlinear multigrid 1077, 1079 nonlinear Volterra equations 994 safe 460 scaling of variables 484 singular Jacobian 486 solving stiff ODEs 943, 944 with backtracking 478–483   
Next reaction method 952   
Niederreiter sequence 404   
NIST-STS, for random number tests 345   
NL2SOL 806   
Noise bursty 1168 effect on maximum entropy method 683 equivalent bandwidth 658 fitting data that contains 770, 773 model, for optimal filtering 651   
Nominal variable (statistics) 741   
Non-interfering directions see Conjugate directions   
Nonexpansive projection operator 1012   
Nonlinear eigenvalue problems 568, 569   
Nonlinear equations finding roots of 442–486 in MEM inverse problems 1018 integral equations 988, 994 multigrid method for elliptic PDEs 1077   
Nonlinear instability 1037   
Nonlinear programming 536   
Nonnegativity constraints 526, 527 barrier function 541   
Nonparametric statistics 748–754   
Nonpolynomial complete (NP-complete) 551   
Nordsieck method 944   
Norm, of matrix 64   
Normal (Gaussian) distribution 320, 321, 341, 776, 778, 805, 1004 central limit theorem 777 deviates from 364, 365, 368, 377, 686 kurtosis of 723, 724

multivariate 378, 379, 813, 842, 843, 847, 848, 1006, 1129, 1130 semi-invariants of 725 sum of 12 uniform 377 tails compared to Poisson 778 two-dimensional (binormal) 746 variance of skewness of 723 see also Gaussian (normal) distribution Normal equations (fitting) 40, 768, 789–793, 1002, 1007 often are singular 793 Normal equations (interior-point method) 85, Normalization normalizing constant 825, 828, 835, 836 of Bessel functions 221 of floating-point representation 9 of functions 181, 973 of modified Bessel functions 282 Normalized Radial Basis Functions 140 Not a Number see NaN Notch filter 667, 671 NP-complete problem 551 NR::, why missing in 3rd ed. 36 nr3.h file 3, 4, 17, 28–30, 34–36 NRmatrix 26, 28, 29 bounds checking 35 instrumenting 36 methods in 27 NRvector 26, 28, 29 bounds checking 35 instrumenting 36 methods in 27 Nugget effect 838 different from measurement error 838 Null hypothesis 720 Nullity 67, 68 Nullspace 39, 67–70, 72, 563, 1002 Number-theoretic transforms 616 numeric_limits 10, 34 Numerical derivatives 178, 229–232, 769 Numerical integration see Quadrature Numerical Recipes bugs in 5 compilers tested 5 cookbook, not menu 3 dependencies 4 electronic versions 5 how to use routines in 3 is not a program library 2, 18 is not a programming text 2 machines tested 5 obtaining source code 3 types 25 webnotes 4 Nyquist frequency 605, 607, 632, 653, 655, 685–687, 693 Nystrom method 989–992, 995 product version 995 _O 26, 32, 36

Object 17–24 avoid copying large 36 constructor 18, 27 definition 18 destruction 20, 21 functor 21–23 grouping related functions 18 hides internal structure 17 inheritance 23, 24 instantiation 18, 19 multiple instances of 20 returning multiple values via 19 saving internal state 20 simple uses of 18–20 standardizing an interface 19 struct vs. class 17 see also Class   
Object-oriented programming (OOP) 17–21, 23   
Objective function 526, 528, 530   
Oblateness parameter 971   
Octave (software) 3   
Octree see QO tree   
Odd-even ordering in Gauss-Seidel relaxation 1070, 1073 in successive over-relaxation (SOR) 1064   
Odd parity 1168   
Odds ratio 757   
ODE see Differential equations   
One-sided power spectral density 602   
OOP see Object-oriented programming   
Operation count balancing 592 Baum-Welch re-estimation of hidden Markov model 865 Bessel function evaluation 278 bisection method 448 Cholesky decomposition 100 coefficients of interpolating polynomial 130 complex multiplication 108 cubic spline interpolation 122 evaluating polynomial 203 fast Fourier transform (FFT) 609, 610 Gauss-Jordan elimination 47, 54 Gaussian elimination 47 Givens reduction 578 Householder reduction 582 interpolation 111 inverse iteration 598, 599 iterative improvement 63 Jacobi transformation 573, 574 Kendall’s tau 752 $_ { L U }$ decomposition 49, 54 Markov model diagnosis 858 matrix inversion 108 matrix multiplication 107 maximum entropy method 683 multidimensional minimization 515 multigrid method 1067 multiplication 1188, 1190 polynomial evaluation 108, 203 QR decomposition 103, 105 $\boldsymbol { Q R }$ method for Hessenberg matrices 596 reduction to Hessenberg form 594 selection by partitioning 433 sorting 420, 422, 423 Toeplitz matrix 93 Vandermonde matrix 93   
Operator precedence, in $\mathrm { C } { + } { + }$ 12 splitting 1028, 1052, 1053, 1065   
Optimal (Wiener) filtering 645, 649–652, 673, 674, 767 compared with regularization 1008   
Optimal feasible vector 526, 528   
Optimally Localized Average (OLA) 1014–1016   
Optimization see Minimization   
Options, financial 329   
Ordinal variable (statistics) 741   
Ordinary differential equations see Differential equations   
Orthogonal see Orthonormal functions; Orthonormal polynomials   
Orthogonal transformation 566, 578, 584, 699   
Orthonormal basis, constructing 74, 105   
Orthonormal functions 181, 292   
Orthonormal polynomials and Gaussian quadrature 181, 1087 Chebyshev 183, 187, 233 construct for arbitrary weight 189–191 Gaussian weights from recurrence 188, 189 Hermite 183 in Gauss-Hermite integration 185 Jacobi 183 Laguerre 183 Legendre 183 weight function log x 190, 191   
Orthonormality 66, 68, 70, 181, 579   
Out-of-band signaling 1178   
Outer product of matrices (denoted by $\otimes$ ) 78, 523   
Outgoing wave boundary conditions 1026   
Outlier 723, 778, 779, 781, 818, 821 see also Robust estimation   
Overcorrection 1061, 1062   
Overflow 1164 in complex arithmetic 225, 226   
Overlap-add and overlap-save methods 646, 647   
Overrelaxation parameter 1062 choice of 1062–1064   
$p$ -value test 720   
Packet-switched networks 1168   
Pade approximant 125, 212, 245–247 ´   
Parabolic interpolation 496, 497   
Parabolic partial differential equations 1024, 1043   
Parallel axis theorem 413   
Parallel programming cyclic reduction 224

FFT 614   
polynomial evaluation 205   
recurrence relations 223, 224   
recursive doubling 223   
tridiagonal systems 57   
rameters in fitting function 776–780, 807–817   
rentheses, annoying 12   
rity bit 1168   
rity-check matrix 851   
rseval’s theorem 602, 603, 654   
discrete form 608   
rsimony, maximum 882   
rtial abstraction 24   
rtial differential equations 1024–1096   
advective equation 1032   
alternating-direction implicit method (ADI)   
1052, 1053, 1065, 1066   
amplification factor 1033, 1038   
analyze/factorize/operate package 1030   
artificial viscosity 1037, 1042   
biconjugate gradient method 1030   
boundary conditions 1025   
boundary value problems 1025–1030,   
1053–1058   
Cauchy problem 1024   
Cayley’s form 1049   
characteristics 1024–1026   
Chebyshev acceleration 1064   
classification of 1024–1030   
comparison of rapid methods 1058   
conjugate gradient method 1030   
Courant condition 1034, 1036, 1038–1040,   
1042   
Courant condition (multidimensional) 1051   
Crank-Nicolson method 1045, 1047, 1049,   
1051, 1052   
cyclic reduction (CR) method 1054, 1057,   
1058   
diffusion equation 1024, 1043–1049, 1051,   
1052, 1059   
Dirichlet boundary conditions 1026, 1045,   
1055, 1061, 1063   
elliptic, defined 1024   
error, varieties of 1036–1038   
explicit vs. implicit differencing 1033   
FACR method 1058   
finite difference method 1027   
finite element methods 1030   
flux-conservative initial value problems   
1031–1043   
forward Euler differencing 1032   
forward time centered space (FTCS) 1032,   
1044, 1049, 1059   
Fourier analysis and cyclic reduction (FACR)   
1053–1058   
Gauss-Seidel method (relaxation) 1060,   
1061, 1068, 1078   
Godunov’s method 1043   
Helmholtz equation 1057   
high-order methods, caution on 1050   
hyperbolic 1024, 1031   
implicit differencing 1045   
inhomogeneous boundary conditions 1055   
initial value problems 1024, 1026   
initial value problems, recommendations on   
1042   
Jacobi’s method (relaxation) 1060, 1061,   
1068   
Laplace’s equation 1024   
Lax method 1034–1036, 1042, 1050, 1051   
Lax method (multidimensional) 1050, 1051   
matrix methods 1028, 1030   
mesh drift instability 1040   
Monte Carlo methods 1030   
multidimensional initial value problems   
1049–1053   
multigrid method 1029, 1066–1083   
Neumann boundary conditions 1026, 1045,   
1056, 1057, 1063   
nonlinear diffusion equation 1047   
nonlinear instability 1037   
numerical dissipation or viscosity 1035   
operator splitting 1028, 1052, 1053, 1065   
outgoing wave boundary conditions 1026   
parabolic 1024, 1043   
periodic boundary conditions 1055, 1063   
piecewise parabolic method (PPM) 1043   
Poisson equation 1024, 1057   
rapid (Fourier) methods 620, 1029, 1054   
relaxation methods 1028, 1059–1066   
Schrodinger equation 1048, 1049¨   
second-order accuracy 1038–1042, 1045   
shock 1037, 1042, 1043   
sparse matrices from 76   
spectral methods 239, 1030, 1083–1096   
spectral radius 1061, 1066   
stability vs. accuracy 1035   
stability vs. efficiency 1027   
staggered grids 625, 1057   
staggered leapfrog method 1038, 1039   
successive over-relaxation (SOR) 1061–1066,   
1070   
time splitting 1052, 1053, 1065   
two-step Lax-Wendroff method 1040   
upwind differencing 1037, 1042   
variational methods 1030   
varieties of error 1036–1038   
von Neumann stability analysis 1033, 1034,   
1036, 1039, 1045, 1046   
wave equation 1024, 1031   
see also Elliptic partial differential equations;   
Finite difference equations (FDEs)   
rtial pivoting 43, 45, 535   
rtition-exchange 423, 433   
rtitioned matrix, inverse of 81, 82   
rty tricks 106, 203   
rzen window 657   
scal (language) 1   
th integration, for function evaluation   
251–254, 318

Path length, minimization of 555–562   
PAUP (software) 874   
PBCG (preconditioned biconjugate gradient method) 89, 1030   
PC methods see Predictor-corrector methods   
PCx (software) 548   
PDEs see Partial differential equations   
PDF (probability density function) see Statistical distributions   
Pearson’s r 745   
PECE method 944   
Penalty function 541   
Pentagon, symmetries of 1174   
Percentile 320, 419, 435   
Perfect code 852   
Period of linear congruential generator 343   
Periodic boundary conditions 1055, 1063   
Periodogram 653–657, 681, 683 Lomb’s normalized 685–687, 689 variance of 655, 656   
Perron’s theorems 221   
Perturbation methods for matrix inversion 76–79   
Peter Principle 427   
Phantom bit 9   
Phase error 1036   
Phase-locked loop 824   
Phi statistic 744   
Phillips-Twomey method 1006   
PHYLIP (software) 874   
Phylogenetic tree see Tree, phylogenetic   
$\pi$ , computation of 1185   
PI stepsize control 915   
Piecewise parabolic method (PPM) 1043   
Pigeonhole principle 387   
Pincherle’s theorem 222   
Pivot element 43, 46, 47, 967   
Pivoting 41, 43–45, 60, 76, 78, 101 and $\boldsymbol { Q R }$ decomposition 103, 105 for tridiagonal systems 57 full 43 implicit 44, 51 in $_ { L U }$ decomposition 50 in reduction to Hessenberg form 594 in relaxation method 967 Markowitz criterion 535 partial 43, 45, 46, 50, 535 threshold partial 535   
Pixel 631, 714, 715, 1010, 1017   
Planck’s constant 1048   
Plane rotation see Givens reduction; Jacobi transformation (or rotation)   
Plane, defined by triangle 1115   
Platykurtic distribution 723   
Plotting of functions 444, 1160–1163   
POCS (projection onto convex sets) 1012   
Point 1099–1101 closest approach of line to 1121 distance between two 1099 distance to line 1118 projection into plane 1115 random in triangle 1114 random on sphere 1129, 1130 test if inside box 1100 test if inside polygon 1124   
Poisson equation 631, 1024, 1057   
Poisson probability function 336–338, 390 as limiting case of binomial 338 deviates from 372–374, 686 moments of 725, 734 semi-invariants of 725 tails compared to Gaussian 778   
Poisson process 362, 369, 829, 830   
Polak-Ribiere algorithm 489, 517   
Poles see Complex plane, poles in   
Polishing of roots 459, 465, 471   
Polygon 1097, 1122–1127 area 1126 Bolyai-Gerwien theorem 1127 CCW vs. CW 1122 centroid of 1127 constructable by compass/straightedge 1127 convex vs. concave 1122 Jordan curve theorem 1124 pentagon, symmetries of 1174 removal of hidden 1150 routine for classifying 1125 simple vs. complex 1122, 1125 sum of exterior angles 1122 test if point inside 1124 winding number 1122–1124   
Polynomial interpolation 110, 118–120 Aitken’s algorithm 118 coefficients for 129–131 in Bulirsch-Stoer method 924 in predictor-corrector method 943 Lagrange’s formula 94, 118, 1089, 1092 multidimensional 132–135 Neville’s algorithm 118, 125, 166, 231, 924 pathology in determining coefficients for 130 Runge phenomenon 1090 smoothing filters 768 see also Interpolation   
Polynomials 201–205 algebraic manipulations 203 approximation from Chebyshev coefficients 241, 243 characteristic 469 characteristic, for digital filters 670, 676 characteristic, for eigenvalues of matrix 563, 583 Chebyshev 187 deflation 464–466, 471 derivatives of 202 division 95, 204, 464, 471 evaluation of 201, 202 evaluation of derivatives 202 extrapolation in Bulirsch-Stoer method 922, 924 extrapolation in Romberg integration 166 fitting 94, 129, 241, 243, 768, 788, 797

generator for CRC 1170 ill-conditioned 463 irreducible modulo 2 382 matrix method for roots 469 minimax 235, 248 modulo 2 381, 1169 monic 181 multiplication 203, 204 operation count for 203 order, distinct from degree 1170 orthonormal 181, 1087 parallel evaluation 205 primitive modulo 2 382–386, 406 roots of 227–229, 463–473 shifting of 243 stopping criterion in root finding 467 Population count of bits 16 Population vector 857 Portable random number generator see Random number generator Positive-definite matrix, testing for 101 Positivity constraints 526, 527 Postal Service (U.S.), barcode 1174 PostScript 1161 Powell’s method 489, 502, 509–514 Power (in a signal) 602 Power of 2 next higher 16, 361 test if integer is a 16, 611 Power series 201–205, 209–218, 246 economization of 243, 244 Pade approximant of 245–247 ´ Power spectral density see Fourier transform; Spectral density Power spectrum 655 Bartlett window 657 data windowing 655–660 estimation by FFT 652–667 figures of merit for data windows 658 Hamming window 658 Hann window 657 leakage 655, 656, 658, 662–665 mean squared amplitude 653 multitaper methods 662–667 normalization conventions 652, 653 overlapping data segments 660–662 Parzen window 657 periodogram 653–657 power spectral density 652 PSD 652 Slepian tapers 662–667 square window 656 sum squared amplitude 653 time-integral squared amplitude 653 variance reduction in spectral estimation 656 662 Welch window 658 Power spectrum estimation see Fourier transform; Spectral density PPM (piecewise parabolic method) 1043

Precedence of operators, in $\mathrm { C } { + } { + }$ 12   
Precision floating point 1164 multiple 1185–1193   
Preconditioned biconjugate gradient method (PBCG) 89   
Preconditioning, in conjugate gradient methods 1030   
Predictive stepsize control 939   
Predictor-corrector methods 900, 909, 934, 942–946 Adams-Bashforth-Moulton schemes 943 adaptive order methods 946 compared to other methods 942, 946 fallacy of multiple correction 943 functional iteration vs. Newton’s rule 944 multivalue compared with multistep 945, 946 Nordsieck method 944 starting and stopping 944 stepsize control 943, 944, 946 with fixed number of iterations 944   
Prerequisite relationship 23   
Primitive polynomials modulo 2 382–386, 406, 1170   
Principal component analysis (PCA) 892   
Principal directions 509, 512   
Principal solution, of inverse problem 1004   
Principal value integrals 178   
Prior probability 757, 775, 841, 1005 smoothness 1006   
Prize, $\$ 1000$ offer revoked 342   
Probability see Random number generator; Statistical tests; Statistical distributions   
Process loss 658   
Product Nystrom method 995   
Products, reaction 947   
Program(s) as black boxes 67, 255, 443, 507 dependencies 4 NR not a program library 2 typography of 14 validation 5   
Programming, NR not a textbook on 2   
Projection onto convex sets (POCS) 1011–1013 generalizations 1013   
Projection operator, nonexpansive 1012   
Prolongation operator 1068   
Proportional betting 758, 760   
Proposal distribution 826–828, 835   
Protocol, for communications 1168   
PSD (power spectral density) see Fourier transform; Spectral density; Power spectrum   
Pseudo-random numbers 340–386   
Pseudoinverse 70   
Pseudospectral method see Spectral methods   
Puns, particularly bad 35, 202, 946, 958, 1098   
Pure virtual class 34   
Pyramidal algorithm 702, 703   
Pythagorean theorem 1111   
Pythagoreans 494   
QO tree 1149–1158 applications of 1156–1158 intersecting objects 1150 use of hash in implementing 1151   
$\boldsymbol { Q R }$ decomposition 102–106, 483, 484, 486 and least squares 791 backsubstitution 103 operation count 103 pivoting 103 updating 105, 106, 483 use for orthonormal basis 74, 105 use for random rotation 1130 see also Eigensystems   
Quadratic convergence 64, 310, 452, 459, 511, 512, 522, 1185 equations 10, 227–229, 494, 572 interpolation 454, 466 programming 536, 884–886   
Quadrature 155–200 adaptive 155, 167, 194–196, 241, 995 alternative extended Simpson’s rule 160 and computer science 1160 arbitrary weight function 189–191, 995 Bode’s rule 158 Cauchy principal values 178 change of variable in 170–172, 995 Chebyshev fitting 156, 240, 241 classical formulas for 156–162 Clenshaw-Curtis 156, 241, 624, 625 closed formulas 157–160 cubic splines 156 DE rule 174 error estimate in solution 991 extended formula of order $1 / N ^ { 3 }$ 160 extended midpoint rule 161, 167 extended rules 159–162, 166, 993, 995, 997 extended Simpson’s rule 160 extended trapezoidal rule 159, 162 for improper integrals 167–172, 995–1000 for integral equations 988, 993 Fourier integrals 692–699 Fourier integrals, infinite range 699 functors and 22 Gauss-Chebyshev 183, 187, 625 Gauss-Hermite 183, 995 Gauss-Jacobi 183 Gauss-Kronrod 192, 195 Gauss-Laguerre 183, 995 Gauss-Legendre 183, 193, 990, 996 Gauss-Lobatto 191, 192, 195, 241, 624 Gauss-Radau 191 Gaussian integration 159, 179–193, 238, 296, 988, 990, 995, 1086–1089 Gaussian integration, nonclassical weight function 189–191, 995 IMT rule 173 infinite ranges 176–178 Monte Carlo 156, 197, 397–403, 410 multidimensional 156, 196–199

Newton-Cotes formulas 158, 179 Newton-Cotes open formulas 158, 159 open formulas 157–162, 167 oscillatory function 217 related to differential equations 155 related to predictor-corrector methods 943 Romberg integration 156, 166, 169, 231, 923, 994 semi-open formulas 160–162 Simpson’s rule 158, 165, 169, 698, 990, 994, 997 Simpson’s three-eighths rule 158, 995, 997 singularity removal 170, 171, 173, 995 singularity removal, worked example 999, 1000 TANH rule 173 trapezoidal rule 158, 160, 162, 166, 173, 175, 178, 695, 698, 989, 993 using FFTs 156 variable transformation 172–178 weight function log x 190, 191 see also Integration of functions Quadrature mirror filter 701, 708 Quadtree see QO tree Quantile changes with time 438 estimation 435 values 320, 419 Quantum mechanics, Uncertainty Principle 717 Quartet puzzling 882 Quartile value 419 Quasi-Newton methods for minimization 489, 521–525 Quasi-random sequence 403–410, 418, 1160, 1168 for Monte Carlo integration 408, 413, 418 Halton’s 404 Sobol’s 404–406 see also Random number generator Quicksort 420, 422–426, 429, 433 Quotient-difference algorithm 206

R (programming language) 3   
R-estimates 818   
Racetrack betting 757, 760   
Radial Basis Functions 139–144 Gaussian 142 inverse multiquadric 142 multiquadric 141 thin-plate spline 142 Wendland 142   
Radioactive decay 362   
Radix base for floating point arithmetic 592, 1164   
Radix base for floating-point arithmetic 1186, 1192   
Radix conversion 1181, 1185, 1192   
Ramanujan’s identity for $\pi$ 1193   
Random angle variables 364 bits 380–386 byte 352 point in triangle 1114 point on circle 1131 point on sphere 1129, 1130 rotation matrix 1130, 1131 variables, decorrelating 379 walk 10 walk, multiplicative 329   
Random deviates 340–386 angles 364 beta distribution 371 binomial 374–377 Cauchy distribution 367 chi-square distribution 371 exponential 362 $F$ -distribution 371 faster 377 gamma distribution 369 Gaussian 341, 364, 365, 368, 377, 686, 1004 integer range 343 logistic 363 multivariate Gaussian 378, 379 normal 341, 364, 365, 368, 377, 686 Poisson 372–374, 686 quasi-random sequences 403–410, 1160, 1168 Rayleigh 365 squeeze 368 Student’s-t distribution 371 sum of 12 uniform 377 trig functions 364 uniform 341–357   
Random number generator 32-bit limited 355–357 Box-Muller algorithm 364 combined generators 342, 345–352 Data Encryption Standard 358–361 Diehard test 345 floating point 354 for everyday use 351 for hash function 387 for integer-valued probability distribution 372 hash function 352 highest quality 342, 351 inheritance 23 lagged Fibonnaci 354 linear congruential generator 341, 343, 348 linear feedback shift register (LSFR) 346, 380–386 MLCG 341, 344, 348, 349 multiply with carry method (MWC) 347 NIST-STS test 345 nonrandomness of low-order bits 344 planes, numbers lie on 344 primitive polynomials modulo 2 382 pseudo-DES 358 quasi-random sequences 403–410, 1160, 1168 Quicksort use of 423 random bits 380–386 random byte 352 ratio-of-uniforms method 367–371 recommended methods 345–352 rejection method 365–368 simulated annealing method 551, 552 spectral test 344 subtractive method 354 successor relation 350, 352 system-supplied 342 timings 355 transformation method 362–365 trick for trigonometric functions 364, 367 uniform 341–357 xorshift method 345   
Random numbers see Monte Carlo; Random deviates   
RANDU, infamous routine 344   
Range 67, 68, 70   
Rank (matrix) 67 kernel of finite 992   
Rank (sorting) 419, 428–431   
Rank (statistics) 748–754, 818 Kendall’s tau 751–754 Spearman correlation coefficient 749–751 sum squared differences of 749   
Rank-nullity theorem 68   
Raphson, Joseph 456   
Rate equations 947, 948   
Ratio-of-uniforms method for random number generator 367–371   
Ratio variable (statistics) 741   
Rational Chebyshev approximation 247–251   
Rational function 110, 201–205, 245, 248, 670 approximation for Bessel functions 275 approximation for continued fraction 207, 260 as power spectrum estimate 681 Chebyshev approximation 247–251 diagonal 125 evaluation of 204, 205 extrapolation in Bulirsch-Stoer method 922 interpolation and extrapolation using 110, 124–128, 245, 247–251, 922 minimax 248, 249 response of recursive filter 670   
Rayleigh deviates 365   
RBF see Radial Basis Functions   
Reactions, chemical or nuclear 946–954 reaction products 947   
Realizable (causal) 668, 670, 671   
Rearranging see Sorting   
Reciprocal, multiple precision 1190   
Record, in data file 428   
Recurrence relation 219–223 and continued fraction 222 associated Legendre polynomials 294 Bessel function 219, 274, 275, 278, 283–285 binomial coefficients 258 Bulirsch-Stoer 125

characteristic polynomial of tridiagonal matrix 583, 665 Clenshaw’s recurrence formula 222, 223 continued fraction evaluation 207, 208 convergence 222 cosine function 219, 610 dominant solution 220 exponential integrals 219 gamma function 256 Golden Mean 11 hidden Markov model 861 Legendre polynomials 219 minimal vs. dominant solution 220 modified Bessel function 281 Neville’s 118, 231 orthonormal polynomials 181 parallel evaluation 223, 224 Perron’s theorems 221 Pincherle’s theorem 222 polynomial interpolation 118, 119, 231 random number generator 343 rational function interpolation 125 sequence of trig functions 219 sine function 219, 610 spherical harmonics 294 stability of 12, 220, 222, 223, 275, 278, 282, 294 trig functions 687 weight of Gaussian quadrature 183 Recursive doubling (parallel method) 223 Monte Carlo integration 410–418 multigrid method 1069 stratified sampling 416–418 Red-black see Odd-even ordering Reduction of variance in Monte Carlo integration 402, 410 Reed-Solomon code 852, 855 Berlekamp-Massey algorithm 852 syndrome decoding 852 References (explanation) 6 Reflection formula for gamma function 256 Regula falsi (false position) 449 Regularity condition 983 Regularization compared with optimal filtering 1008 constrained linear inversion method 1006 linear 1006–1013 nonlinear 1018 objective criterion 1009 of inverse problems 1002–1006 Phillips-Twomey method 1006 support vector machines 893 Tikhonov-Miller 1007 trade-off curve 1005 two-dimensional 1010, 1011 zeroth order 1002–1006 see also Inverse problems Regularizing operator 1004

Rejection method for random number generator 365–368   
Relative entropy 756   
Relaxation method automated allocation of mesh points 981–983 computation of spheroidal harmonics 971, 973–977 elliptic partial differential equations 1028, 1059–1066 example 971, 973–977 for algebraically difficult sets 970 for differential equations 957, 964–970 Gauss-Seidel method 1060, 1061, 1068, 1078 internal boundary conditions 983, 984 internal singular points 983, 984 Jacobi’s method 1060, 1061, 1068 successive over-relaxation (SOR) 1061–1066, 1070 see also Multigrid method   
Remes algorithms exchange algorithm 669 for minimax rational function 249   
Residual 63, 70, 88 in multigrid method 1067   
resize 27   
Resolution function, in Backus-Gilbert method 1014   
Response function 641–643, 649   
Responsibility matrix 842   
Restriction operator 1068   
Reward, $\$ 1000$ offer revoked 342   
Richardson’s deferred approach to the limit 166, 169, 231, 900, 911, 921, 922, 994, 1072 see also Bulirsch-Stoer method   
Richtmyer artificial viscosity 1042   
Ridders’ method for numerical derivatives 231 root finding 443, 449, 452–454   
Riemann shock problem 1043   
Riemann zeta function 211   
Right eigenvalues or eigenvectors 564, 565   
Rights management 5   
Rise/fall time 659   
Robust estimation 723, 778, 818–824 Andrew’s sine 821 average deviation 723 double exponential errors 820 Kalman filtering 824 Lorentzian errors 820 mean absolute deviation 723 nonparametric correlation 748–754 Tukey’s biweight 821 use of a priori covariances 824 see also Statistical tests   
Romberg integration 156, 166, 169, 231, 923, 994   
Root finding 181, 182, 442–486 advanced implementations of Newton’s rule 486 Bairstow’s method 466, 471

bisection 445, 447–449, 454, 460, 492, 584, 822 bracketing of roots 443, 445–447, 454, 455, 464, 465, 470 Brent’s method 443, 449, 453–456, 459, 786 Broyden’s method 474, 483–486 compared with multidimensional minimization 476, 477 complex analytic functions 466 convergence criteria 448, 475 deflation of polynomials 464, 471 double root 443 eigenvalue methods 469, 470 false position 449, 452, 454 Halley’s method 263, 264, 271, 335, 463 in complex plane 254 in one dimension 442 in relaxation method 964 in shooting method 956, 959 Jenkins-Traub method 470 Laguerre’s method 444, 466–469 Lehmer-Schur algorithm 470 Maehly’s procedure 465, 472 matrix method 469, 470 Muller’s method 466, 473 multidimensional 442, 459 multiple roots 443 Newton’s rule 182, 229, 443, 444, 456–462, 464, 466, 470–477, 539, 584, 944, 959, 964, 994, 1077, 1079, 1190, 1191 pathological cases 445, 457, 464, 474 polynomials 444, 463–473, 563 Ridders’ method 443, 449, 452–454 root polishing 459, 465, 470–473 safe Newton’s rule 460 secant method 449, 454, 466, 500 singular Jacobian in Newton’s rule 486 stopping criterion for polynomials 467 use of minimum finding 443 using derivatives 456 without derivatives 456 zero suppression 473 see also Roots Root polishing 459, 465, 470–473 Roots Chebyshev polynomials 233 cubic equations 228 multiple 443, 466 nonlinear equations 442–486 polynomials 444, 464, 563 quadratic equations 227 reflection in unit circle 676 square, multiple precision 1191 see also Root finding Rosenbrock method 934–940 compared with semi-implicit extrapolation 941 stepsize control 938 Rotation matrix 1097, 1130, 1131 Roundoff error 10, 11, 1163, 1164

bracketing a minimum 500 conjugate gradient method 1030 eigensystems 572, 573, 582, 584, 586, 591, 594 extended trapezoidal rule 165 general linear least squares 791, 795 graceful 1165 hardware aspects 1164 Householder reduction 581, 582 IEEE standard 1165 least-squares fitting 783, 791 Levenberg-Marquardt method 802 linear algebraic equations 38, 41, 43, 61, 72, 95 linear predictive coding (LPC) 680 magnification of 10, 11, 61 maximum entropy method (MEM) 683 multidimensional minimization 521, 525 multiple roots 464 numerical derivatives 229 recurrence relations 220 reduction to Hessenberg form 594 series 207, 210 straight line fitting 783 variance 724   
Row degeneracy 38 operations on matrix 42, 45 totals 743, 759   
RSS algorithm 416, 417   
RST properties (reflexive, symmetric, transitive) 440   
Run-length encoding 1180   
Runge-Kutta method 900, 901, 907–910, 935, 942, 1096 dense output 915 Dormand-Prince parameters 912, 920 embedded 911, 936 FSAL (first-same-as-last) 913 high-order 907–910, 912, 920 implementation 916–920 number of function evaluations 912 stepsize control 910–920   
Runge phenomenon 1090   
Rybicki, G.B. 96, 130, 183, 303, 634, 689, 717   
Sampling a distribution 825 importance 411, 412, 414 Latin square or hypercube 409, 410 Markov chain Monte Carlo 825 recursive stratified 416–418 stratified 412–414 uneven or irregular 685, 771   
Sampling theorem 178, 239, 605, 653 for numerical approximation 717–719   
Sande-Tukey FFT algorithm 616   
Savitzky-Golay filters for data smoothing 766–772 for numerical derivatives 232, 769   
ScaLAPACK 40   
Scallop loss 658   
Schrodinger equation 1048, 1049¨   
Schrage’s algorithm 344   
Schultz’s method for matrix inverse 64, 716   
Scilab (software) 3   
Scope, temporary 20, 21   
Searching an ordered table 114–118 selection 431–439 with correlated values 115   
Secant method 443, 449, 454, 466, 500 Broyden’s method 483–486 multidimensional (Broyden’s) 474, 483–48   
Second Euler-Maclaurin summation formula 16   
Second order differential equations 928, 930   
Seed of random number generator 343   
Selection 419, 431–439 by partition-exchange 433 find $m$ largest elements 434 for median 822 heap algorithm 434 in place 432, 439 incremental quantile estimation 435 largest or smallest 434 operation count 433, 439 single-pass 432 use to find median 726   
Semi-implicit Euler method 934, 940   
Semi-implicit extrapolation method 934, 935, 940, 941 compared with Rosenbrock method 941 stepsize control 941   
Semi-implicit midpoint rule 940   
Semi-invariants of a distribution 725   
Sentinel, in Quicksort 424, 433   
Separable kernel 992   
Separation of variables 292   
Sequence, alignment of by DP 559–562   
Sequential quantile estimation 435 changes with time 438   
Series 209–218 accelerating convergence of 177, 211–218 alternating 211, 216 asymptotic 210, 216 Bessel function $K _ { \nu }$ 288 Bessel function $Y _ { \nu }$ 284, 285 Bessel functions 210, 274 divergent 210, 211, 216 economization 243–245 $\epsilon$ algorithm 212 Euler’s transformation 211, 212 exponential integral 267, 269 Fresnel integral 298 geometric 211, 214 hypergeometric 252, 318 hyperlinear convergence 211 incomplete beta function 270 incomplete gamma function 259 Laurent 681, 682 Levin transformation 214 linear convergence 211 logarithmic convergence 211 relation to continued fractions 206 Riemann zeta function 211 roundoff error in 207 sine and cosine integrals 301 sine function 210 Taylor 456, 510, 900, 911, 965, 969 transformation of 211, 212 van Wijngaarden’s algorithm 217   
Set bits, counting 16   
Shaft encoder 1166   
Shell algorithm (Shell’s sort) 420–423   
Shepard interpolation 140   
Sherman-Morrison formula 76–79, 94, 483, 534   
Shifting of eigenvalues 563, 585, 596   
Shock wave 1037, 1042, 1043   
Shooting method computation of spheroidal harmonics 979 example 971, 977–981 for differential equations 956, 959–961, 971, 977–981 for difficult cases 962 interior fitting point 962   
Side information 760, 761   
Sidelobe level 658   
Sign bit in floating point format 8   
SIGN utility function 17   
Signal, bandwidth limited 605   
Significance (statistical) 727 of 2-d K-S test 763, 764 one- vs. two-sided 747 peak in Lomb periodogram 686, 687 two-tailed 730   
Similarity transform 566, 567, 570, 592, 594   
Simplex defined 502 method in linear programming 489, 502, 526–536, 548 method of Nelder and Mead 489, 502–507, 552, 821 use in simulated annealing 552   
Simplex method see Linear Programming   
Simpson’s rule 156, 158, 160, 165, 169, 698, 990, 994   
Simpson’s three-eighths rule 158, 995, 997   
Simulated annealing see Annealing, method of simulated   
Simulation see Monte Carlo   
Sinc expansion 178   
Sine function evaluated from tan. $\theta / 2 )$ / 219 recurrence 219 series 210   
Sine integral 297, 300–302 continued fraction 301 routine for 301 series 301 see also Cosine integral   
Sine transform see Fast Fourier transform (FFT); Fourier transform   
Singleton’s algorithm for FFT 637, 638   
Singular value decomposition (SVD) 39, 65–75 and least squares 65, 70, 73, 249, 791, 793 and rational Chebyshev approximation 249 approximation of matrices 74, 75 basis for nullspace and range 68 confidence levels from 816, 817 covariance matrix 817 fewer equations than unknowns 73 for inverse problems 1003 in minimization 512 more equations than unknowns 73, 74 of square matrix 69–73 relation to eigendecomposition 569, 570 use for ill-conditioned matrices 71, 73, 563 use for orthonormal basis 74, 105   
Singularities in integral equations 995–1000 in integral equations, worked example 999, 1000 in integrands 167, 173, 195, 995 of hypergeometric function 252, 253, 318 removal in numerical integration 170, 171, 173, 995   
Singularity, subtraction of the 996   
Six-step framework, for FFT 615   
size 27   
Skewness of distribution 723, 725   
Slack variables 529, 538, 888   
Slepian functions 662–667   
SMBus 1168   
Smith-Waterman algorithm 562   
Smoothing data 129, 766–772 in multigrid methods 1069 operator in integral equations 987   
Smoothness prior 1006   
sn function 316   
Sobol’s quasi-random sequence 404–406   
Soft-decision decoding 851–855 error correction 855 minimal trellis 853 trellis 853, 856 Viterbi algorithm 854   
Software engineering 2   
Sorting 419–441 bubble sort cautioned against 420 compared to selection 431 eigenvectors 575 Heapsort 420, 426–428, 434 index table 419, 426, 428–431 operation count 420, 422, 423 Quicksort 420, 422–426, 429, 433 rank table 419, 431 ranking 428–431 Shell’s method 420–423 straight insertion 420, 423, 575   
Source code, obtaining NR 3   
Sparse linear equations 39, 75–92, 534, 544, 548, 937 band-diagonal 58 Bartels-Golub update 535 biconjugate gradient method 88, 716 fill-in, minimizing 59, 76, 535, 544 in inverse problems 1011 indexed storage 82–87 minimum residual method 89 named patterns 76, 1028 partial differential equations 1028 relaxation method for boundary value problems 964 wavelet transform 700, 716 see also Matrix   
Spearman rank-order coefficient 749–751, 819   
Special functions see Function   
Spectral analysis see Fourier transform; Periodogram   
Spectral density one-sided PSD 602 periodogram 681, 683 power spectral density (PSD) 602, 603, 652 power spectral density per unit time 603 power spectrum estimation by MEM 681–684 two-sided PSD 603 see also Power spectrum   
Spectral lines, how to smooth 767   
Spectral methods 239, 1030, 1083–1096 analytic example 1084 and discontinuities 1083 and Gaussian quadrature 1087–1089 as finite difference methods 1093 cardinal functions 1089–1091 choice of basis functions 1085 collocation method 1086 contrasted with finite differencing 1083, 1085 differentiation matrix 1091 efficiency of 1083 exponential convergence of 1085 Galerkin method 1086 grid point representation 1090 interpolation of solution 1093 method of lines 1095 multidimensional equations 1095 nonlinear equations 1094 pseudospectral 1088 tau method 1086 variable coefficient equations 1094 worked example 1094, 1095   
Spectral radius 1061, 1066   
Spectral test for random number generator 344   
Spectrum see Fourier transform   
Speech recognition by hidden Markov model 866   
Sphere 1097, 1128–1130 2- vs. 3-sphere 1128 angular coordinates 1128 find all points within a 1109 intersection with line 1121 random point on 1129, 1130 surface area in $n$ -dimensions 1128 volume in $n$ -dimensions 1129   
Spherical Bessel functions 283 routine for 291   
Spherical coordinates 1128   
Spherical harmonics 292–297 basis functions for spectral methods 1085 fast transform 295, 297 orthogonality 292 routine for 294 stable recurrence for 294 table of 293 see also Associated Legendre polynomials   
Spheroidal harmonics 971–981 boundary conditions 972, 973 normalization 973 routines for 975–977   
Spline 111 cubic 120–124 gives tridiagonal system 122 interpolating 148 natural 122 operation count 122 two-dimensional (bicubic) 135   
Spread matrix 1015   
Square root complex 226 multiple precision 1191   
Square window 656   
Squeeze, for computing random deviates 368   
Stability 8–12 and stiff differential equations 932 Courant condition 1034, 1036, 1038, 1042, 1051 diffusion equation 1045, 1046 in quadrature solution of Volterra equation 994 mesh drift in PDEs 1040 nonlinear 1037 of Clenshaw’s recurrence 223 of Gauss-Jordan elimination 41, 43 of implicit differencing 932, 1046 of Markov model 858, 859 of polynomial deflation 464, 465 of recurrence relations 220, 222, 223, 275, 278, 282, 294 partial differential equations 1026, 1033 von Neumann analysis for PDEs 1033, 1034, 1036, 1039, 1045, 1046 see also Accuracy   
Stabilized Kolmogorov-Smirnov test 739   
Stabilizing functional 1004   
Stage, trellis 857   
Staggered leapfrog method 1038, 1039   
Standard (probable) errors 727, 781, 783, 786, 787, 790, 794, 807–817   
Standard deviation of a distribution 722, 723 of Fisher’s z 747 of linear correlation coefficient 746 of sum squared difference of ranks 750   
Standard Template Library (STL) containers 42   
State change vector 947   
Statistical distributions 320–339 beta 333, 334 binomial 338, 339 Cauchy 322, 323 chi-square 330, 331 density, change of variables in 362 exponential 326, 327 $F$ -distribution 332, 333 full conditional 827 gamma 331, 332 Kolmogorov-Smirnov 334–336 logistic 324–326 lognormal 328, 329 Lorentzian 322 normal 320, 321 Poisson 336–338 Student’s 323, 324 Weibull 327, 328   
Statistical error 778   
Statistical tests 720–772 Anderson-Darling 739 average deviation 723 bootstrap method 809, 810 chi-square 731–734, 742–745 contingency coefficient C 743, 744 contingency tables 741–745, 753, 758 correlation 721 Cramer’s V 743, 744 difference of distributions 730–740 difference of means 727 difference of variances 728, 730 entropy measures of association 758–761 F-test 728, 730 Fisher’s z-transformation 746 general paradigm 720 Kendall’s tau 749, 751–754 Kolmogorov-Smirnov 731, 736–738, 762, 819 Kuiper’s statistic 739 kurtosis 723, 725 L-estimates 818 linear correlation coefficient 745–748 Lucy’s $Y ^ { 2 }$ and $Z ^ { 2 }$ 735 M-estimates 818 mean 721–723, 725, 726 mean absolute deviation 723 measures of association 721, 741, 759 measures of central tendency 721–726 median 722, 725, 726, 818 mode 722, 725, 726 moments 721–726 nonparametric correlation 748–754 $p$ -value test 720 Pearson’s r 745 periodic signals 686, 687 phi statistic 744 R-estimates 818

rank correlation 748–754 robust 723, 749, 818–824 semi-invariants 725 shift vs. spread 739 significance 727 significance, one- vs. two-sided 730, 747 skewness 723, 725 small numbers of counts 734, 735 Spearman rank-order coefficient 749–751, 819 standard deviation 722, 723 strength vs. significance 727, 741 Student’s t 727–730, 746 Student’s t, for correlation 746 Student’s t, paired samples 729 Student’s t, Spearman rank-order coefficient 749 Student’s t, unequal variances 728 sum squared difference of ranks 749 tail test 720 Tukey’s trimean 818 two-dimensional 762–766 variance 721, 722, 724, 725, 729 Wilcoxon 818 see also Error; Robust estimation Statistics, higher-order 604 Steed’s method Bessel functions 283, 287 continued fractions 207 Steepest descent method 516 in inverse problems 1011 Step doubling 162, 174, 177, 910 tripling 168, 169 Stieltjes, procedure of 189 Stiff equations 901, 931–941 Kaps-Rentrop method 934 methods compared 941 predictor-corrector method 934 Rosenbrock method 934–940 scaling of variables 935 semi-implicit Euler method 940 semi-implicit extrapolation method 934, 935 semi-implicit midpoint rule 940 Stiff functions 111, 500 Stirling’s approximation 256, 1017 STL see Standard Template Library Stochastic simulation 946–954 when not to use 953 Stock market prices 329 Stoermer’s rule 928 Stopping criterion multigrid method 1078 polynomial root finding 467 Storage band-diagonal matrix 58 sparse matrices 82–87 Straight injection 1071 Straight insertion 420, 423, 575 Straight-line fitting 780–785

errors in both coordinates 785–787 robust estimation 822–824 Strassen’s fast matrix algorithms 107 Stratified sampling, Monte Carlo 412–414, 416 Strings, aligning by DP 559–562 struct see Class; Object Student-t deviates 371 Student’s probability distribution 323, 324 Cauchy as special case 323 normal as limiting case 323 Student’s t-test for correlation 746 for difference of means 727–730 for difference of means (paired samples) 729 for difference of means (unequal variances) 728 for difference of ranks 750 Spearman rank-order coefficient 749 Sturmian sequence 583 Sub-random sequences see Quasi-random sequence Subtraction, multiple precision 1186 Subtractive method for random number generator 354 Successive over-relaxation (SOR) 1061–1066 bad in multigrid method 1070 Chebyshev acceleration 1064 choice of overrelaxation parameter 1062–1064 Successor relation, random generators 350 Sum-product algorithm 867 Sum squared difference of ranks 749 Sums see Series Supernova 1987A 762 Support vector machine 883–898 dual formulation 886–889 kernel examples 891 kernel trick 889–892 linearly separable data 884 Mangasarian-Musicant variant 893–898 margin 884 regularization parameter 888, 893 SVMlight package 893 SVD see Singular value decomposition (SVD) SVM see Support vector machine SWAP utility function 17 Symbol, of operator 1070, 1071 Syndrome decoding coset leader 852 error-correcting codes 852 Golay code 852 Hamming code 852 perfect code 852 Reed-Solomon code 852 Synthetic division 95, 202, 243, 464, 471 Systematic errors 778 Tableau (interpolation) 118, 125 Tail test 720

Tangent function, continued fraction 206

TANH rule 173 infinite range 176   
Taylor series 229, 456, 510, 900, 911, 944, 965, 969   
Templates $( \mathbf { C } + + )$ ) 17, 22, 26, 419, 421   
Thermodynamics, and simulated annealing 550   
Thin-plate spline 142   
Three-dimensional array 36   
Threshold partial pivoting 535   
throw statement 30   
Tides 677   
Tikhonov-Miller regularization 1007   
Time domain 600   
Time reuse 952   
Time splitting 1052, 1053, 1065   
Timing, C routine for 355   
TNT parsimony software 882   
Toeplitz matrix 93, 96–99, 245 $_ { L U }$ decomposition 98 new, fast algorithms 99 nonsymmetric 96–98   
Tongue twisters 431   
Torus 400, 401, 408   
Trade-off curve 1002, 1016   
Transformation Gauss 310 Landen 310 method for random number generator 362–365   
Transforms, number theoretic 616   
Transition matrix directed graph 856 eigenvalues and eigenvectors 858, 859 Markov model 856   
Transition probability directed graph 856 Markov model 856   
Transport error 1037   
Transpose of sparse matrix 85   
Trapezoidal rule 158, 160, 162, 166, 173, 175, 178, 695, 698, 989, 993   
Traveling salesman problem 549, 551, 552   
Tree data structure 1097 KD see KD tree minimum spanning 1097, 1147 of boxes as data structure 1101 quadtree/octree see QO tree   
Tree, phylogenetic 868–882 additive 871 agglomerative clustering 874–882 branch length 870 corrected distance transformation 873 maximum likelihood 882 maximum parsimony 882 rooted vs. unrooted 871 search over topologies 882 software packages 874 ultrametric 871 UPGMA 877 WPGMA 877   
Trellis 853, 856 directed graph 856 maximum likelihood 854 stage 857   
Trellis coded modulation 855   
Triangle 1097, 1111–1116 angle between two 1116 area of 1111 centroid or barycenter 1113 circumscribed circle (circumcircle) 1112 in 3 dimensions 1114 inscribed circle (incircle) 1112 intersection with line 1121 plane defined by 1115 random point in 1114   
Triangulation and interpolation 132 applications of 1141–1149 definition 1131 Delaunay 1097, 1131–1149 hashing and 1136 incremental construction 1134 interpolation using 1141 largest minimum angle property 1134 minimum weight 1134 number of lines and triangles in 1132   
Tridiagonal matrix 56–61, 188, 567, 598 cyclic 79, 80 eigenvalues 576, 577, 583–589, 665 from cubic spline 122 from operator splitting 1066 in alternating-direction implicit method (ADI) 1066 in cyclic reduction 1057, 1058 parallel solution 57 reduction of symmetric matrix to 576–583 with fringes 1028 see also Matrix   
Trigonometric functions, $\tan ( \theta / 2 )$ as minimal 219 functions, recurrence relation 219, 687 interpolation 110 solution of cubic equation 228   
Trimming error 173   
Truncation error 11, 173, 500, 910, 911, 1163 exponentially decreasing 238 in multigrid method 1077 in numerical derivatives 229   
try 30   
Tukey’s biweight 821   
Tukey’s trimean 818   
Turbo codes 855   
Twenty questions 755, 758, 761   
Twin errors 1174   
Two-dimensional see Multidimensional   
Two-dimensional K–S test 762–766   
Two-pass algorithm for variance 724   
Two-point boundary value problems 900, 955–984

automated allocation of mesh points 981–983   
boundary conditions 955, 962, 977   
difficult cases 962   
eigenvalue problem for differential equations   
958, 973, 977–981   
free boundary problem 958, 983   
grid (mesh) points 957, 964, 981–983   
internal boundary conditions 983, 984   
internal singular points 983, 984   
linear requires no iteration 961   
multiple shooting 964   
problems reducible to standard form 958   
regularity condition 983   
relaxation method 957, 964–970   
relaxation method, example of 973–977   
shooting method 956, 959–961, 971, 977–981   
shooting method, example of 977–981   
shooting to a fitting point 962   
singular endpoints 962, 972, 978   
see also Elliptic partial differential equations   
o-sided exponential error distribution 820   
wo-sided power spectral density 603   
wo-step Lax-Wendroff method 1040   
pes used in NR 4, 25, 26   
Uchar 25   
Uint 25   
Ullong 25   
Ultrametric tree 871   
Uncertainty coefficient 761   
Uncertainty principle 717   
Underflow, in IEEE arithmetic 9, 1165   
Underrelaxation 1062   
Uniform deviates see Random deviates, uniform   
Unit-offset array 36   
Unitary (function) 1048, 1049   
Unitary (matrix) see Matrix   
Universal Product Code (UPC) 1174   
Unnormalized value 9   
Unsupervised learning 842, 868   
UPC checksum 1174   
UPGMA 877   
Upper Hessenberg matrix see Hessenberg matrix   
Upwind differencing 1037, 1042   
U.S. Postal Service barcode 1174   
Utility functions 17

V-cycle 1069   
valarray class 25   
Validation of Numerical Recipes procedures 5   
Valley, long or narrow 503, 509, 512, 516, 550, 552   
Van Cittert’s method 1011   
Van Wijngaarden-Dekker-Brent method see Brent’s method   
Vandermonde matrix 93–96, 130   
Variable length code 1176   
Variable metric method 489, 521–525 compared to conjugate gradient method 521   
Variable step-size integration 155, 167, 901, 924, 928–930, 938, 941, 943, 944, 946   
Variance(s) of distribution 721, 722, 725, 728–730 pooled 727 reduction of (in Monte Carlo) 402, 410 statistical differences between two 726–730 two-pass algorithm for computing 724 see also Covariance   
Variational methods, partial differential equations 1030   
Variogram 145, 837 various models for 837   
VecDoub , VecInt, etc. 26   
Vector angle between two 1120, 1121 $\mathrm { C } { + } { + }$ vector class 24 class for 24–29 contiguous storage for 27 of matrices 36 suffix _I , _O , _IO 26, 32, 36 see also Array; NRvector   
VEGAS algorithm for Monte Carlo 414–416   
Verhoeff’s algorithm for checksums 1174   
Viete’s formulas for cubic roots 228\`   
Viscosity artificial 1037, 1042 numerical 1035, 1042   
Viterbi decoding 850–855 as a min-sum algorithm 867 Bayesian nature of 868 compared to forward-backward algorithm 867 compared to hidden Markov model 867, 868 constellation 855 directed graph 850 state defined 850 training 867 transition 850 with arbitrary transition probability 867 with parameter re-estimation 867   
Volterra equations 988 adaptive stepsize control 995 analogy with ODEs 993 block-by-block method 994 first kind 988, 993 nonlinear 988, 994 second kind 988, 992–995 unstable quadrature 994   
von Neumann-Richtmyer artificial viscosity 1042   
von Neumann stability analysis for PDEs 1033, 1034, 1036, 1039, 1045, 1046   
Voronoi diagram 1097, 1142–1146 and Delaunay triangulation 1143 avoiding obstacles 1147   
Vowellish (coding example) 1176, 1181   
W-cycle 1069   
Wave equation 292, 1024, 1031   
Wavelet transform 699–716 and Fourier domain 707, 708 appearance of wavelets 706, 707

approximation condition of order $p$ 701 coefficient values 703, 704 contrasted with Fourier transform 699, 700, 711 Daubechies wavelet filter coefficients 700, 702, 704, 706–708, 715 detail information 701, 702 discrete wavelet transform (DWT) 702–706 DWT (discrete wavelet transform) 702–706 eliminating wraparound 703, 709 fast solution of linear equations 715, 716 filters 707, 708 for integral equations 989 image processing 713, 715 inheritance 23 inverse 703 JPEG-2000 712 Lemarie’s wavelet 708 mother-function coefficient 703 mother functions 700 multidimensional 712, 713 nonsmoothness of wavelets 707 of linear operator 715 on the interval 709 pyramidal algorithm 702, 703 quadrature mirror filter 701 smooth information 701, 702 truncation 711, 712 wavelet filter coefficient 700, 703 wavelets 700, 706, 707 Wavelets see Wavelet transform Weber function 254 Webnotes, Numerical Recipes 4 Weibull probability distribution 327, 328 Weighted Kolmogorov-Smirnov test 739 Weighted least-squares fitting see Least-squares fitting Weighting, full vs. half in multigrid 1071 Weights for Gaussian quadrature 179, 180, 995 nonclassical weight function 189–191, 995 Welch window 658 while iteration 14 Wiener filtering 645, 649–652, 673, 674, 767 compared to regularization 1008 Wiener-Khinchin theorem 602, 674, 682 Wilcoxon test 818 Winding number 1122–1124 Window function 660 Bartlett 657 flat-topped 658, 659 Hamming 658 Hann 657 Parzen 657 Slepian 662 square 656 Welch 658 Winograd Fourier transform algorithms 616 Woodbury formula 80, 81, 94 Wordlength 8, 12 WPGMA 877

Wraparound object for accessing vector 613 order for storing spectrum 611, 628, 632 problem in convolution 643   
Wronskian, of Bessel functions 283, 284, 287

X-ray diffraction pattern, processing of 1012   
Xorshift random number generator 345

Yale Sparse Matrix Package 76

Z-transform 670, 681   
Z-transformation, Fisher’s 746   
Zapf Dingbats 1162   
Zealots 1020   
Zebra relaxation 1070   
Zero contours 474   
Zero-offset array 36   
Zeroth-order regularization 1002–1006   
Zip code, barcode for 1174   
Ziv-Lempel compression 1176   
ZooAnimal (OOP example) 23   
Zoom transforms 615

# CAMBRIDGE UNIVERSITY PRESS and NUMERICAL RECIPES SOFTWARE

Coupon for Special Offer Number One

At a future time, this coupon will be exchangeable for a valuable benefit to owners of this Numerical Recipes, Third Edition book, ISBN 9780521866088. You must clip and mail this actual coupon, not a photocopy or fax. This coupon is valid only for Offer Number One, not for any other offer.

To find out about special offers, visit http://www.nr.com/specialoffers.html

# »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» CAMBRIDGE UNIVERSITY PRESS and NUMERICAL RECIPES SOFTWARE

Coupon for Special Offer Number Two

At a future time, this coupon will be exchangeable for a valuable benefit to owners of this Numerical Recipes, Third Edition book, ISBN 9780521866088. You must clip and mail this actual coupon, not a photocopy or fax. This coupon is valid only for Offer Number Two, not for any other offer.

To find out about special offers, visit http://www.nr.com/specialoffers.html