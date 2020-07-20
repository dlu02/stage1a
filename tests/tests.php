<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../css/style_page.css">
	<title>Tests statistiques</title>
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
			<p>
				Dans cette partie, nous allons vérifier l'adéquation des données qui sont saisies ou chargées via un fichier CSV à une des lois usuelles décrivant la durée de vie. Pour cela, nous allons utiliser deux tests statistiques : le test du Khi-2 et le test de Kolgomorov-Smirnov.
			</p>

			<h3>Contexte</h3>
				<p>
				Soit l'échantillon $(X_1,...,X_n)$ associé aux données. Nous écrivons les hypothèses du test :
				$$\begin{cases} (H_0) : X_1,...,X_n \text{ suivent la loi } L \\ (H_1) : X_1,...,X_n \text{ ne suivent pas la loi } L \end{cases}$$
				et nous fixons $\alpha=0.05$ la règle de décision.
				<div class="definition">
					<h4>Définition (p-value ou valeur p)</h4>
					<p> On appelle <b>p-value</b> (ou valeur p) la probabilité d'obtenir des réalisations aussi extrêmes ou plus que celles observées, considérant l'hypothèse nulle $(H_0)$ vérifiée.
					</p>
				</div>
				Si la p-value retournée par le test dépasse $\alpha$, alors nous ne pouvons pas rejeter l'hypothèse $(H_0)$ et dans le cas contraire, nous pouvons rejeter l'hypothèse $(H_0)$.
				</p>
			<h3><a href="khi2.php">Test du Khi-2</a></h3>
			<h3><a href="kolgomorov.php">Test de Kolgomorov-Smirnov</a></h3>
	</div>
	<footer>
		<?php include '../bottom.php'; ?>
	</footer>
</body>
</html>
