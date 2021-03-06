<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="../css/style_page.css">
  <title>Modèles de durée de vie</title>
</head>
<body>
    <header>
        <?php include "../top.php"; ?>
    </header>
	<div class="page">
		<h2 class="titre">Modèles de durée de vie</h2>
        <p class="update_time">
            <?php echo "Dernière mise à jour : ". date("d/m/Y H:i:s.",filemtime(__FILE__)); ?>
        </p>
		<p>Pour modéliser des phénomènes de durée de vie, nous allons utiliser une modélisation par une loi usuelle. Nous décrivons ici les aspects théoriques de ces lois : leur caractéristique statistique (moyenne, variance, skewness, kurtosis, etc.) ainsi qu'une représentation de leur densité en fonction du ou des paramètres en jeu : </p>

		<ul>
			<li><a href="hyperexpo.php">Loi hyperexponentielle</a> </li>
			<li><a href="lomax.php">Loi Lomax</a> </li>
			<li><a href="weibull.php">Loi de Weibull</a> </li>
			<li><a href="expo_poly.php">Loi exponentielle polynomiale</a> </li>
			<li><a href="burr.php">Loi de Burr</a> </li>
			<li><a href="expo_convo.php">Loi exponentielle convolution</a> </li>
		</ul>

	</div>
    <footer>
    	<?php include '../bottom.php'; ?>
    </footer>
</body>
</html>
