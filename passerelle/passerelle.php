<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="../css/style_page.css">
  <title>Passerelle Python/PHP</title>
</head>
<body>
    <header>
        <?php include "../top.php"; ?>
    </header>
  <div class="page">
	  	<h2 class="titre">Passerelle Python/PHP</h2>
        <p class="update_time">
            <?php echo "Dernière mise à jour : ". date("d/m/Y H:i:s.",filemtime(__FILE__)); ?>
        </p>
		<h3>Générateur de nombres aléatoires</h3>
		<div>
		  <form method="POST" action="gen_aleat.php" autocomplete="off" >
			<table class="alternate">
				<tr>
				  <td>minimum</td>
				  <td><input type="number" id="nombre_min" name="nombre_min"></td>
				</tr>

				<tr>
				  <td>maximum</td>
				  <td><input type="number" id="nombre_max" name="nombre_max"></td>
				</tr>

				<tr>
				  <td>nombre d'éléments à générer</td>
				  <td><input type="number" id="taille" name="taille"></td>
				</tr>

				<tr>
				  <td>fichier de sortie</td>
				  <td><input type="text" id="fichier" name="fichier"></td>
				</tr>
				<tr> <th colspan="2"><input type="submit" name="submit" id="submit" value="Générer"></th> </tr>
			</table>

		</form>
		</div>
		<h3>Conversion zone de texte vers txt</h3>
		<div>
			<form method="POST" action="textarea.php" autocomplete="off">
				<table class="alternate">
					<tr>
					  <td>Saisir le nom du fichier</td>
					  <td><input type="text" id="nom_fichier" name="nom_fichier"></td>
					</tr>

					<tr>
					  <td>Saisir le contenu du fichier</td>
					  <td><textarea name="contenu" rows="4" cols="30"></textarea></td>
					</tr>
					<tr> <th colspan="2"><input type="submit" name="submit2" id="submit2" value="Convertir"></th> </tr>
				</table>

			</form>
		</div>
		<!-- <h3>Recherche d'un fichier dans l'arborescence</h3>
		<div>
			<form method="POST" action="search.php" autocomplete="off">
				<table class="alternate">
					<tr>
					  <td>Saisir le nom du fichier</td>
					  <td><input type="text" id="nom_fichier_3" name="nom_fichier_3"></td>
					</tr>
					<tr> <th colspan="2"><input type="submit" name="submit3" id="submit3" value="Rechercher"></th> </tr>
				</table>
			</form>
		</div> -->
	</div>
    <footer>
    	<?php include '../bottom.php'; ?>
    </footer>
</body>
</html>
