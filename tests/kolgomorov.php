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
		<h2 class="titre">Tests statistiques</h2>
		<h3>Test de Kolgomorov-Smirnov</h3>
		Soit $\alpha=0.05$ la règle de décision. Soit $(X_1,...,X_n)$ un échantillon donné d'une variable aléatoire continue. Le but du test de Kolgomorov-Smirnov est de comparer la fonction de répartition empirique des données à la fonction de répartition théorique concernant la loi à vérifier : pour cela, on calcule également une sorte de distance entre ces fonctions de répartition, que l'on définit ci-dessous :
		$$D=\max (F_n(x)-F(x))$$
		où $F_n$ est la fonction de répartition empirique des données et $F$ est la fonction de répartition de la loi théorique. Le théorème de Kolgomorov permet d'assurer que sous l'hypothèse $(H_0)$, pour tout $\lambda > 0$ :
		$$P\left(\sqrt{n} D \leqslant \lambda \right) \underset{n\to +\infty}{\longrightarrow} 1+2\sum_{k=1}^{+\infty} (-1)^k \exp(-2k^2\lambda^2)$$
		et cette convergence est très rapide (au bout de 3 ou 4 itérations). L'absence de conditions d'application montre que le test de Kolgomorov-Smirnov est un test <b>non paramétrique</b>.
		<h4>Implémentation</h4>
		Le fichier TXT ou CSV ou DAT doit contenir une seule sorte de données écrites soit en lignes, soit en colonnes.
			<form method="POST" action="submit_ks.php" enctype="multipart/form-data">
				<table class="alternate">
					<tr>
					  <td>Choisir un fichier</td>
					  <td><input type="file" name="fichier"></td>
					</tr>
					<tr>
						<td>Sélectionner la loi théorique</td>
						<td><select name="loi" id="loi">
				                <option value="">Choisir une loi</option>
				                <option value="hyperexpo">Loi hyperexponentielle</option>
				                <option value="lomax">Loi Lomax</option>
				                <option value="weibull">Loi de Weibull</option>
				                <option value="expo_poly">Loi exponentielle polynomiale</option>
								<option value="burr">Loi de Burr</option>
								<option value="expo_convo">Loi exponentielle convolution</option>
			                </select>
						</td>
					</tr>
					<tr>
						<td>Sélectionner la méthode d'estimation des paramètres</td>
						<td><select name="param" id="param">
								<option value="">Choisir une méthode</option>
								<option value=1>Méthode 1 (contrainte sur moment)</option>
								<option value=2>Méthode 2 (contrainte sur skewness)</option>
							</select>
						</td>
					</tr>
					<tr>
						<td>(Uniquement loi exponentiellle polynomiale) Taille N de la liste de paramètres $(a_1,...,a_N)$</td>
						<td><input type="number" id="parametre_a" name="parametre_a" step="any" value="0"></td>
					</tr>
					<tr> <th colspan="2"><input type="submit" name="submit4" id="submit4" value="Envoyer"></th> </tr>
				</table>
			</form>
	</div>
</body>
</html>
