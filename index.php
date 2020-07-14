<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/style_page.css">
	<title>Modélisation statistique de la durée de vie</title>
</head>

<body>
    <header>
        <?php include 'top.php'; ?>
    </header>

	<div class="page">
		<h2 class="titre">Introduction</h2>
			<p class="update_time">
				<?php echo "Dernière mise à jour : ". date("d/m/Y H:i:s.",filemtime(__FILE__)); ?>
			</p>
			<p>
				Il a toujours été important, notamment pour des appareils de production à très haute disponibilité, ou pour des questions de coût, de connaître la durée de vie d'un appareil. En fait, la problématique principale est de savoir s'il est possible de prévoir une prochaine panne de cet appareil.
			</p>
		<h3>Pré-requis</h3>
			<p>
				Considérons un appareil que l'on note P. Nous possédons un jeu de données sur P contenant la durée de fonctionnement de N appareils P.
			</p>
		<h3>Objectif</h3>
			<p>
				L'objectif est, à partir de ce jeu de données, d'en faire une description statistique, puis ensuite, au moyen de tests statistiques, de trouver la ou les lois qui correspondent le plus à ces données, et ensuite de prévoir la durée de vie moyenne d'un appareil.
			</p>
		<h3>Moyens techniques</h3>
			<p>
				La page est propulsée par un serveur Arch Linux sous Apache 2.4.43, PHP 7.4.8 et Python 3.8.3. Tous les calculs et les modélisations sont effectués à l'aide de Python via le langage PHP.
			</p>
	</div>
</body>
<footer>
	<?php include 'bottom.php'; ?>
</footer>
</html>
