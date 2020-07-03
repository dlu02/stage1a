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
		<h2 class="titre">Estimation de paramètres par maximum de vraisemblance</h2>
		<h3>Contraintes sur l'espérance et le moment d'ordre 2 empiriques</h3>
		<p>
			$$\max\limits_{\theta} \ell (x_1,...,x_n;\theta) \quad \text{s.c.} \quad \begin{cases} \displaystyle E(X)=\dfrac{1}{n}\sum_{i=1}^n x_i \\ \displaystyle E(X^2) = \dfrac{1}{n}\sum_{i=1}^n x_i^2 \end{cases}$$
			Cette partie permet à partir d'un fichier CSV d'étudier les données statistiques et, à partir d'une loi choisie préalablement, d'estimer ses paramètres par maximum de vraisemblance et sous les contraintes ci-dessus.
		</p>
		<p>
			Le fichier TXT ou CSV doit contenir une seule sorte de données, écrites sur une seule ligne et séparées par un espace.
			<form method="POST" action="stats_csv.php" enctype="multipart/form-data">
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
			                </select></td>
					</tr>
					<tr> <th colspan="2"><input type="submit" name="submit4" id="submit4" value="Envoyer"></th> </tr>
				</table>
			</form>
		</p>
		<p>NB 1 : pour l'instant, seule la loi hyperexponentielle est implémentée à des fins de tests.</p>
		<p>NB 2 : l'optimisation est effectuée en résolvant le système d'équations $\nabla \mathcal{L} = \mathbf{0}$ suivi des contraintes, via la fonction scipy.optimize.fsolve. Pour l'instant, les résultats semblent aberrants. Voici le script python : <a href="donnees/stats_csv.py">stats_csv.py</a></p>
	</div>
</body>
</html>
