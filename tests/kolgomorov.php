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
		Le fichier TXT ou CSV doit contenir une seule sorte de données, écrites sur une seule ligne et séparées par un espace, ou sur une seule colonne.
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
			                </select></td>
					</tr>
					<tr>
						<td>Sélectionner la méthode d'estimation des paramètres</td>
						<td><select name="param" id="param">
							<option value="">Choisir une méthode</option>
							<option value=1>Méthode 1 (contrainte sur moment)</option>
							<option value=2>Méthode 2 (contrainte sur skewness)</option>
						</select> </td>
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
