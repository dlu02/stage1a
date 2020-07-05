<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Loi hyperexponentielle</title>
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
		<h3>Loi exponentielle convolution <a href=lois.php class=button_link>Choisir une autre loi</a></h3>
		Par l'écriture de la densité de la loi exponentielle convolution, pour $x>0$ et $a,b > 0$ :
		$$f(x,a,b)=\dfrac{ab}{b-a}(\mathrm{e}^{-ax}-\mathrm{e}^{-bx})$$
		nous constatons que
		<p>- dans le cas où $a\neq b$, il s'agit d'un mélange de deux variables iid exponentielles de paramètres différents a et b qui sont donc indépendantes (nous avons en fait fait l'opération de convolution de deux variables)</p>
		<p>- dans le cas où $a=b$, nous retombons sur la somme de deux variables iid exponentielles de même paramètre $a=b$, et on montre que cette somme suit une loi de Gamma de paramètres 2 et $a=b$.</p>
		<table class="alternate">

		<tr> <th colspan="2">Propriétés de la loi exponentielle convolution (cas où $a\neq b$)</th> </tr>

		<tr><td>Densité</td><td>$ \displaystyle  f(x,a,b)= \dfrac{ab}{b-a}(\mathrm{e}^{-ax}-\mathrm{e}^{-bx}) \mathbb{1}_{]0,+\infty[}(x)$</td></tr>
		<tr><td>Domaines des paramètres</td><td>$a>0,b>0,a\neq b$</td></tr>
		<tr><td>Fonction de répartition</td>
		<td>Pour $x>0$, $\displaystyle F(x,a,b)=1+\dfrac{a}{b-a}\mathrm{e}^{-b x} - \dfrac{b}{b-a} \mathrm{e}^{-a x}$</td></tr>
		<tr><td>Moments d'ordre $k$</td><td>$\displaystyle \mathbb{E}[X^k]=k! \sum_{i=0}^k \dfrac{1}{a^i} \dfrac{1}{b^{k-i}}$</td></tr>
		<tr><td>$\displaystyle E(X)$</td><td>$\dfrac{1}{a}+\dfrac{1}{b}$</td></tr>
		<tr><td>$\displaystyle V(X)$</td><td>$2\left(\dfrac{1}{a^2}+\dfrac{1}{ab}+\dfrac{1}{b^2}\right) - \dfrac{1}{a} - \dfrac{1}{b}$</td></tr>
		<tr><td>Skewness</td><td>$\displaystyle \gamma_{1}=\dfrac{2\left(\dfrac{1}{a^3}+\dfrac{1}{b^3}\right)}{\left(\dfrac{1}{a^2}+\dfrac{1}{b^2}\right)^{3/2}}$</td></tr>
		<tr><td>Kurtosis</td><td>$\displaystyle \gamma_{2}=\dfrac{6\left( \dfrac{1}{a^4}+\dfrac{1}{b^4} \right)}{\left(\dfrac{1}{a^2}+\dfrac{1}{b^2} \right)^2}$</td></tr>

		</table>

		<table class="alternate">

		<tr> <th colspan="2">Propriétés de la loi exponentielle convolution (cas où $a=b$) <br> ou loi Gamma $\Gamma(2,a)$</th> </tr>

		<tr><td>Densité</td><td>$ \displaystyle  f(x,a)= \dfrac{a^2x}{\Gamma(2)} \mathrm{e}^{-ax} \mathbb{1}_{]0,+\infty[}(x)=a^2x \mathrm{e}^{-ax}\mathbb{1}_{]0,+\infty[}(x)$ (car $\Gamma(2)=(2-1)!=1$)</td></tr>
		<tr><td>Domaines des paramètres</td><td>$a=b>0$</td></tr>
		<tr><td>Fonction de répartition</td>
		<td>Pour $x>0$, $\displaystyle F(x,a)=1-\mathrm{e}^{-ax}(ax+1)$</td></tr>
		<tr><td>Moments d'ordre $k$</td><td>$\displaystyle \mathbb{E}[X^k]=\dfrac{(2+k-1)!}{a^k}$</td></tr>
		<tr><td>$\displaystyle E(X)$</td><td>$\dfrac{2}{a}$</td></tr>
		<tr><td>$\displaystyle V(X)$</td><td>$\dfrac{2}{a^2}$</td></tr>
		<tr><td>Skewness</td><td>$\displaystyle \gamma_{1}=\dfrac{2}{\sqrt{2}}$</td></tr>
		<tr><td>Kurtosis</td><td>$\gamma_2=6$</td></tr>

		</table>
		<form method="POST" id="densite" action="submit.php" autocomplete="off">
			<input id="nom" name="nom" type="hidden" value="Loi exponentielle convolution ">
			<input id="loi" name="loi" type="hidden" value="4">
			<table class="alternate">
				<tr><th colspan="2">Tracé de la densité</th></tr>
				<tr><td>Valeur de $a$</td><td><input type="number" id="parametre1" name="parametre1" step="any" min=0></td></tr>
				<tr><td>Valeur de $b$</td><td><input type="number" id="parametre2" name="parametre2" step="any" min=0></td></tr>
				<tr> <th colspan="2"><input type="submit" name="submit5" id="submit5" value="Tracé de la densité"></th> </tr>
			</table>
		</form>
	</div>
</body>
</html>
