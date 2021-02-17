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
				L'objectif est, à partir de ce jeu de données, d'en faire une description statistique, puis ensuite, au moyen de tests statistiques, de trouver la ou les lois qui correspondent le plus à ces données, et ensuite d'en déduire des prédictions sur la durée de vie de futurs appareils P à partir de ces lois.
			</p>
		<h3>Organisation du site</h3>
			<p>Le site, qui est en quelque sorte l'illustration d'une bibliothèque Python, est divisé en 5 parties : <br>
			- une passerelle Python/PHP basique montrant sur des fonctions basiques le dialogue entre Python et PHP, <br>
			- une présentation théorique des modèles de durée de vie, avec un tracé de leurs densités, <br>
			- une partie estimation des paramètres d'un échantillon suivant une loi donnée parmi les modèles de durée de vie, <br>
			- une partie tests qui permet d'effectuer un test statistique sur un échantillon qui suivrait une loi parmi les modèles de durée de vie. </p>
			<p> Une partie recherche d'histogrammes ou de densités à partir de leurs numéros est également disponible pour retrouver à posteriori les fichiers générés. </p>
			<p> Pour chaque partie, un script Python est exécuté suivant plusieurs arguments qui sont obtenus via un formulaire HTML. </p>

			<p>Chaque page de résultat de test est enregistrée sur le serveur et se voit attribuer un numéro, qui permet à postériori de pouvoir la retrouver soit via le lien renvoyé, soit dans la partie Recherche, muni du numéro.</p>
		<h3>Moyens techniques</h3>
			<p>
				La page est propulsée par un serveur Debian 10 sous Nginx 1.14.2, PHP 7.3 et Python 3.7. Tous les calculs et les modélisations sont effectués à l'aide de Python via le langage PHP.
			</p>
	</div>
	<footer>
		<?php include 'bottom.php'; ?>
	</footer>
</body>
</html>
