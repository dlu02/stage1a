<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Loi exponentielle polynomiale</title>
<link rel="stylesheet" type="text/css" href="../css/style_page.css">

<!-- Pour LaTeX -->
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      jax: ["input/TeX", "output/HTML-CSS"],
      extensions: ["tex2jax.js"],
      "HTML-CSS": { preferredFont: "TeX", availableFonts: ["STIX","TeX"] },
      tex2jax: { inlineMath: [ ["$", "$"], ["\\(","\\)"] ], displayMath: [ ["$$","$$"], ["\\[", "\\]"] ], processEscapes: true, ignoreClass: "tex2jax_ignore|dno" },
      TeX: { noUndefined: { attributes: { mathcolor: "red", mathbackground: "#FFEEEE", mathsize: "90%" } } },
      messageStyle: "none"
    });
</script>
<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML"></script>

<!-- <script type="text/javascript"
  async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js/MathJax.js?config=TeX-MML-AM_CHTML">
</script> -->
<!-- Fin LaTeX -->
</head>

<body>
	<header>
		<?php include "../top.php"; ?>
	</header>

	<div class="page">
		<h2 class="titre">Modèles de durée de vie</h2>
		<h3>Loi exponentielle polynomiale <a href=lois.php class=button_link>Choisir une autre loi</a></h3>
		<p> Pour déterminer $C(a,b)$, nous utilisons le fait que :
			$$\int_{-\infty}^{+\infty} f(x,a,b) \mathrm{d} x = 1$$
			Nous obtenons ainsi :
			$$\boxed{C(a,b)=\dfrac{1}{\displaystyle \sum_{k=1}^m a_k \dfrac{k!}{b^{k+1}}}}$$
		</p>
		<table class="alternate">

		<tr> <th colspan="2">Propriétés de la loi exponentielle polynomiale</th> </tr>

		<tr><td>Densité</td><td>$\displaystyle f(x,a,b)= C(a,b) \left(\sum_{k=1}^m a_kx^k \right) \mathrm{e}^{-bx} \mathbb{1}_{]0,+\infty[}(x)$</td></tr>
		<tr><td>Domaines des paramètres</td><td>$\begin{cases} m\in \mathbb{N}^* \\ a=(a_1,...,a_m) \\ \forall 1 \leqslant k \leqslant m, a_k \geqslant 0 \\ b>0 \end{cases}$ </td></tr>
		<tr><td>Fonction de répartition</td>
		<td>Pour $x>0$, $\displaystyle F(x,a,b)= C(a,b) \sum_{k=1}^m a_k \dfrac{k!}{b^{k+1}} \left( 1-\mathrm{e}^{-bx} \right)$</td></tr>
		<tr><td>Moments d'ordre $k$</td><td>$\displaystyle E(X^k)=\sum_{i=1}^m C(a,b) a_i \dfrac{(i+k)!}{b^{k+i+1}}$</td></tr>
		<tr><td>$\displaystyle E(X)$</td><td>$\displaystyle \sum_{i=1}^m C(a,b)a_i \dfrac{(i+1)!}{b^{i+2}}$</td></tr>
		<tr><td>$\displaystyle V(X)$</td><td>$\displaystyle \sum_{i=1}^m C(a,b)a_i \dfrac{(i+2)!}{b^{i+3}} - \left(\sum_{i=1}^m C(a,b)a_i \dfrac{(i+1)!}{b^{i+2}} \right)^2$</td></tr>
		<tr><td>Skewness</td><td>$\gamma_{1}=\dfrac{M_3-3E(X)V(X)-E(X)^3}{V(X)^{3/2}}$</td></tr>
		<tr><td>Kurtosis</td><td>$\gamma_{2}=\dfrac{M_4-4E(X)V(X)^{3/2}\gamma_1-6E(X)^2V(X)-E(X)^4}{V(X)^2}$</td></tr>
		</table>

		<form method="POST" id="densite" action="submit.php" autocomplete="off">
			<input id="nom" name="nom" type="hidden" value="Loi exponentielle polynomiale ">
			<input id="loi" name="loi" type="hidden" value="4">
			<table class="alternate">
			<tr> <th colspan="2">Tracé de la densité</th> </tr>
			<tr><td>Valeur de $a$ (syntaxe CSV, espace comme séparateur)</td><td><textarea name="parametre1" rows="1" cols="50"></textarea></tr>
			<tr><td>Valeur de $b$</td><td><input type="number" id="parametre2" name="parametre2" step="any"></td></tr>
			<tr> <th colspan="2"><input type="submit" name="submit5" id="submit5" value="Tracé de la densité"></th> </tr>
			</table>
		</form>
	</div>
</body>
</html>
