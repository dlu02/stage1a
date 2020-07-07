<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../css/style_page.css">
	<title>Estimation de paramètres</title>

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
        <?php include '../top.php'; ?>
    </header>

	<div class="page">
		<h2 class="titre">Estimation de paramètres</h2>
			<p>
				Dans cette partie, il s'agira, à partir d'un fichier de données ou de la saisie des données par l'utilisateur, et du choix d'une loi, d'estimer sous deux modèles différents décrits ci-dessous les paramètres de cette loi. <br> Considérons un échantillon $(X_1,...,X_n)$ associé au fichier ou à la saisie par l'utilisateur.
			</p>
			<h3><a href="param1.php">Maximum de vraisemblance sous contraintes sur l'espérance et le moment d'ordre 2 empiriques</a></h3>
			$$\max\limits_{\theta} \ell (x_1,...,x_n;\theta) \quad \text{s.c.} \quad \begin{cases} \displaystyle E(X)=\dfrac{1}{n}\sum_{i=1}^n x_i \\ \displaystyle E(X^2) = \dfrac{1}{n}\sum_{i=1}^n x_i^2 \end{cases}$$

			<h3><a href="param2.php">Maximum de vraisemblance sous contrainte de signe du skewness $(\gamma_1)$</a></h3>
			$$\max\limits_{\theta} \ell (x_1,...,x_n;\theta) \qquad \text{s.c.} \quad E\left( \left( X-E(X) \right)^3 \right) \gamma_1 \geqslant 0$$
	</div>
</body>
</html>
