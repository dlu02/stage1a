<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/style_page.css">
  <title>Recherche d'un histogramme</title>
</head>
<body>
    <header>
        <?php include "top.php"; ?>
    </header>
    <div class="page">
	  	<h2 class="titre">Recherche d'un histogramme ou d'une densité</h2>
        <p class="update_time">
            <?php echo "Dernière mise à jour : ". date("d/m/Y H:i:s.",filemtime(__FILE__)); ?>
        </p>
		<h3>Recherche d'un histogramme ou d'une densité</h3>
		<div>
			<form method="POST" action="recherche_image.php" autocomplete="off">
				<table class="alternate">
					<tr>
					  <td>Saisir le numéro du fichier</td>
					  <td><input type="text" id="nom_fichier_3" name="nom_fichier_3"></td>
					</tr>
					<tr> <th colspan="2"><input type="submit" name="submit3" id="submit3" value="Rechercher"></th> </tr>
				</table>
			</form>
		</div>
	</div>
    <footer>
    	<?php include 'bottom.php'; ?>
    </footer>
</body>
</html>
