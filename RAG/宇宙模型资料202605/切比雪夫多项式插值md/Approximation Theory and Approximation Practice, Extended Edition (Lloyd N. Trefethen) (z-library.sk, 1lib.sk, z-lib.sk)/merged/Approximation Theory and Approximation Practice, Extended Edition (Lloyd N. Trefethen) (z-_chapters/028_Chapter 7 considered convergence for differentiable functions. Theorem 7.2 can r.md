Chapter 7 considered convergence for differentiable functions. Theorem 7.2 can readily be restated for the transformed context—see Exercise 22.1. For a numerical illustration, here is a repetition of the experiment from Chapter 7 involving $f ( x ) =$ $| x |$ . On the loglog scale, the transformed approximants run parallel to the same line as the Chebyshev interpolants, but lower.

$\begin{array} { r l } & { \mathrm { \bf ~ f ~ = ~ \ a b s ( x ) : ~ \ f g ~ = ~ \bf ~ f \left( g \right) : ~ \omega ~ } } \\ & { \mathrm { \bf ~ n n ~ = ~ \omega ~ 2 * r o u n d \left( 2 . \hat { \omega } ( 0 : \cdot 3 : 7 ) \right) - 1 ; ~ { \vec { \varphi } } ~ e ~ = ~ \omega ~ 0 * n n ; ~ { \vec { \varphi } } ~ e \in ~ \omega _ 0 \ * n n ; } } \\ & { \mathrm { \bf ~ f o r ~ \bf ~ j ~ = ~ \bf ~ 1 : 1 \cdot } \mathrm { \bf ~ e n g t h } \mathrm { \bf ~ ( n n ) } } \\ & { \mathrm { \bf ~ n ~ = ~ \omega ~ n n ( j ) : ~ \omega _ \mathrm { { f } ~ n ~ = ~ \ c h e b f u n ( f , n + 1 ) ; ~ \vec { \varphi } e e ( j ) ~ = ~ \ n o r m ( f - f n , i n f ) ~ ; } } } \\ & { \mathrm { \bf ~ f n 2 ~ = ~ \ c h e b f u n ( f g , n + 1 ) ; ~ \vec { \varphi } e e 2 ( j ) ~ = ~ \ n o r m ( f g - f n 2 , i n f ) ~ ; } } \end{array}$   
end   
$\log 1 0 \mathbf { g } \left( \mathtt { n n } , 1 . / \mathtt { n n } , ^ { \prime } \mathtt { r } ^ { \prime } \right)$   
hold on, loglog(nn,ee,'.'), loglog(nn,ee2,'sm')   
ratio $=$ ee(end-4:end)./ee2(end-4:end)

ratio $=$

1.3167 1.3167 1.3167 1.3167 1.3167

![](../chunks/Approximation Theory and Approximation Practice, Extended Edition (Lloyd N. Trefethen) (z-_part_0003_pages_0141-0210/auto/images/f7077a8ad74b49d1e12289efd32e01b45e17d95f749d1ed792a1e2fc23225126.jpg)
