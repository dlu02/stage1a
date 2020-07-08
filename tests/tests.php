<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../css/style_page.css">
	<title>Tests statistiques</title>

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
		<h2 class="titre">Tests statistiques</h2>
			<p>
				Dans cette partie, nous allons vérifier l'adéquation des données qui sont saisies ou chargées via un fichier CSV à une des lois usuelles décrivant la durée de vie. Pour cela, nous allons utiliser deux tests statistiques : le test du Khi-2 et le test de Kolgomorov-Smirnov.
			</p>
			<h3>Contexte</h3>
				<p>
				Soit l'échantillon $(X_1,...,X_n)$ associé aux données. Nous écrivons les hypothèses du test :
				$$\begin{cases} (H_0) : X_1,...,X_n \text{ suivent la loi } L \\ (H_1) : X_1,...,X_n \text{ ne suivent pas la loi } L \end{cases}$$
				et nous fixons $\alpha=0.05$ la règle de décision : si la $p$-value retournée par le test dépasse $\alpha$, alors nous ne pouvons pas rejeter l'hypothèse $(H_0)$ et dans le cas contraire, nous pouvons rejeter l'hypothèse $(H_0)$.
				</p>
			<h3><a href="khi2.php">Test du Khi-2</a></h3>
			<h3><a href="kolgomorov.php">Test de Kolgomorov-Smirnov</a></h3>
	</div>
</body>
</html>
