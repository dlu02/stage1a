<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../css/style_page.css">
	<title>Test de Kolgomorov-Smirnov</title>
</head>

<body>
    <header>
        <?php include '../top.php'; ?>
    </header>

	<div class="page">
		<h2 class="titre">Tests statistiques</h2>
		<p class="update_time">
		    <?php echo "Dernière mise à jour : ". date("d/m/Y H:i:s.",filemtime(__FILE__)); ?>
		</p>
		<h3>Test de Kolgomorov-Smirnov</h3>
		Soit $\alpha=0.05$ la règle de décision. Soit $(X_1,...,X_n)$ un échantillon donné d'une variable aléatoire continue. Le but du test de Kolgomorov-Smirnov est de comparer la fonction de répartition empirique des données à la fonction de répartition théorique concernant la loi à vérifier : pour cela, on calcule également une sorte de distance entre ces fonctions de répartition, que l'on définit ci-dessous :
		$$D=\max (F_n(x)-F(x))$$
		où $F_n$ est la fonction de répartition empirique des données et $F$ est la fonction de répartition de la loi théorique. Le théorème de Kolgomorov permet d'assurer que sous l'hypothèse $(H_0)$, pour tout $\lambda > 0$ :
		$$P\left(\sqrt{n} D \leqslant \lambda \right) \underset{n\to +\infty}{\longrightarrow} 1+2\sum_{k=1}^{+\infty} (-1)^k \exp(-2k^2\lambda^2)$$
		et cette convergence est très rapide (au bout de 3 ou 4 itérations). Ceci nous permet alors de déterminer la p-value du test. L'absence de conditions d'application montre que le test de Kolgomorov-Smirnov est un test <b>non paramétrique</b>.
		<div class="formul">
			<h4>Implémentation</h4>
			<p>
			Le fichier TXT ou CSV ou DAT doit contenir une seule sorte de données écrites soit en lignes, soit en colonnes. Si plusieurs sortes de données sont présentes, elles sont concaténées et regroupées en une seule sorte de données. </p>
			<form method="POST" action="submit.php" enctype="multipart/form-data">
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
						<td><input type="number" id="parametre_a" name="parametre_a" step="any" value="0" min="0"></td>
					</tr>
					<tr> <th colspan="2"><input type="submit" name="submit4" id="submit4" value="Envoyer"></th> </tr>
				</table>
				<input id="test" name="test" type="hidden" value=" de Kolgomorov-Smirnov">
				<input id="test2" name="test2" type="hidden" value="2">
			</form>
		</div>
	</div>
	<footer>
		<?php include '../bottom.php'; ?>
	</footer>
</body>
</html>
