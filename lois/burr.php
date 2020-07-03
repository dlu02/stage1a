<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Loi de Burr</title>
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
		<h2 class="titre">Étude de lois</h2>
		<h3>Loi de Burr <a href=lois.php class=button_link>Choisir une autre loi</a></h3>
		On note $\Gamma$ la fonction Gamma d'Euler définie sur $\mathbb{R}_+^*$ par :
		$$\Gamma(x)= \displaystyle \int_0^{+\infty} t^{x-1}\mathrm{e}^{-t} \mathrm{d} t$$
		<table class="alternate">

		<tr> <th colspan="2">Propriétés de la loi de Burr</th> </tr>

		<tr><td>Densité</td><td>$f(x,a,b)= \dfrac{abx^{a-1}}{(1+x^a)^{b+1}} \mathbb{1}_{]0,+\infty[}(x)$</td></tr>
		<tr><td>Domaines des paramètres</td><td>$ a >0 \,$  ,  $ b >0 $</td></tr>
		<tr><td>Fonction de répartition</td>
		<td>Pour $x>0$, $F(x,a,b)=1-(1+x^a)^{-b}$</td></tr>
		<tr><td>Moments d'ordre $k$</td><td>$E(X^k)=\dfrac{1}{\Gamma(b)} \Gamma\left(1+\dfrac{k}{a}\right) \Gamma\left(b-\dfrac{k}{a}\right)$ </td></tr>
		<tr><td>$\displaystyle E(X)$</td><td>$\dfrac{1}{\Gamma(b)} \Gamma\left(1+\dfrac{1}{a}\right) \Gamma\left(b-\dfrac{1}{a}\right)$</td></tr>
		<tr><td>$\displaystyle V(X)$</td><td>$\dfrac{1}{\Gamma(b)} \left( \Gamma\left(b-\dfrac{2}{a}\right) \Gamma\left(1+\dfrac{2}{a}\right) - \dfrac{\left( \Gamma\left(b-\dfrac{1}{a}\right) \Gamma\left(1+\dfrac{1}{a}\right) \right)^2}{\Gamma(b)} \right)$</td></tr>
		<tr><td>Skewness</td><td>$\gamma_{1}=\dfrac{M_3-3E(X)V(X)-E(X)^3}{V(X)^{3/2}}$</td></tr>
		<tr><td>Kurtosis</td><td>$\gamma_{2}=\dfrac{M_4-4E(X)V(X)^{3/2}\gamma_1-6E(X)^2V(X)-E(X)^4}{V(X)^2}$</td></tr>
		</table>

		<form method="POST" id="densite" action="submit.php" autocomplete="off">
			<input id="nom" name="nom" type="hidden" value="Loi de Burr ">
			<input id="loi" name="loi" type="hidden" value="3">
			<table class="alternate">
			<tr> <th colspan="2">Tracé de la densité</th> </tr>
			<tr><td>Valeur de $a$</td><td><input type="number" id="parametre1" name="parametre1" step="any" min=0></td></tr>
			<tr><td>Valeur de $b$</td><td><input type="number" id="parametre2" name="parametre2" step="any" min=0></td></tr>
			<tr> <th colspan="2"><input type="submit" name="submit5" id="submit5" value="Tracé de la densité"></th> </tr>
			</table>
		</form>
	</div>
</body>
</html>
