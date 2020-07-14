<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/style_page.css">
  <title>Résultats de l'analyse</title>
</head>
<body>
    <header>
        <?php include "top.php"; ?>
    </header>

	<div class="page">
		<h2 class="titre">Statistiques descriptives</h2>
		<h3>Résultats de l'analyse <a href=stats_descriptives.php class=button_link>Nouvelle analyse</a></h3>
		<?php
			if (!(empty ($_POST["nom_fichier4"])) AND !(empty ($_POST["contenu2"])) AND !(empty ($_POST["size2"]))) {
				$nom_fichier = $_POST["nom_fichier4"];
				$contenu = $_POST["contenu2"];
				$nom_fichier=$nom_fichier.".txt";
				$size2 = $_POST["size2"];
				file_put_contents($nom_fichier,$contenu);
				echo "Succès : vos données saisies ont été écrites dans le fichier $nom_fichier".", que vous pouvez ouvrir : ";
				echo "<a href=$nom_fichier class=button_link>Ouvrir le fichier créé</a>";
			}
			else{
				echo "<h3> ERREUR : un ou plusieurs champ(s) est/sont vide(s). </h3></div></body></html>";
				exit();
			}

			$result = json_decode(exec("python stats.py ".$nom_fichier." ".$size2), true);
		?>
			<table class="alternate">
				<tr>
				  <td>minimum</td>
				  <td><?php echo $result['min']; ?></td>
				</tr>

				<tr>
				  <td>maximum</td>
				  <td><?php echo $result['max']; ?></td>
				</tr>

				<tr>
				  <td>moyenne</td>
				  <td><?php echo $result['moy']; ?></td>
				</tr>
				<tr>
				  <td>variance</td>
				  <td><?php echo $result['var']; ?></td>
				</tr>
				<tr>
				  <td>écart-type</td>
				  <td><?php echo $result['ec']; ?></td>
				</tr>
				<tr>
				  <td>skewness</td>
				  <td><?php echo $result['skew']; ?></td>
				</tr>
				<tr>
				  <td>kurtosis</td>
				  <td><?php echo $result['kurt']; ?></td>
				</tr>
			</table>
			<h3>Histogramme généré : <a href=hist.png class=button_link>Zoom de l'image</a></h3>
			<img src="hist.png" width=700px alt="Histogramme" class="img_center">
	</div>
	</body>
    <footer>
    	<?php include 'bottom.php'; ?>
    </footer>
</html>
