<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../css/style_page.css">
	<title>Estimation de paramètres</title>
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

		Le fichier TXT ou CSV ou DAT doit contenir une seule sorte de données écrites soit en lignes, soit en colonnes. Si plusieurs sortes de données sont présentes, elles sont concaténées et regroupées en une seule sorte de données.
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
					<tr>
						<td>(Uniquement loi exponentiellle polynomiale) Taille N de la liste de paramètres $(a_1,...,a_N)$</td>
						<td><input type="number" id="parametre_a" name="parametre_a" step="any" value="0" min="0"></td>
					</tr>
					<tr> <th colspan="2"><input type="submit" name="submit4" id="submit4" value="Envoyer"></th> </tr>
				</table>
			</form>
		<p>À des fins de test, voici un <a href="donnees/test_weibull_2_5.txt">exemple</a> de fichier txt contenant un échantillon de 500 réalisations de la loi de Weibull de paramètres 2 et 5 généré avec scipy.stats.</p>
	</div>
</body>
</html>
