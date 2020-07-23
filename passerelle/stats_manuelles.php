<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="../css/style_page.css">
  <title>Résultats de l'analyse</title>
</head>
<body>
    <header>
        <?php include "../top.php"; ?>
    </header>

	<div class="page">
		<h2 class="titre">Statistiques descriptives</h2>
		<h3>Résultats de l'analyse <a href=stats_descriptives.php class=button_link>Nouvelle analyse</a></h3>
		<?php
			if (!(empty ($_POST["nom_fichier4"])) AND !(empty ($_POST["contenu2"])) AND !(empty ($_POST["size2"]))) {
				$nom_fichier = $_POST["nom_fichier4"];
				$contenu = $_POST["contenu2"];
				$rep_nouv_fichier = "donnees/$nom_fichier.txt";
				$size2 = $_POST["size2"];
				file_put_contents($rep_nouv_fichier,$contenu);
				echo "Succès : vos données saisies ont été écrites dans le fichier $nom_fichier".", que vous pouvez ouvrir : ";
				echo "<a href=$rep_nouv_fichier class=button_link>Ouvrir le fichier créé</a>";
			}
			else{
				echo "<h3> ERREUR : un ou plusieurs champ(s) est/sont vide(s). </h3></div></body></html>";
				exit();
			}
            $replace = exec("sed -i 's/ /\\n/g; s/,/\\n/g; s/\\t/\\n/g; s/;/\\n/g' $rep_nouv_fichier && sed -i '/^$/d' $rep_nouv_fichier"); // remplace les espaces de séparation, les tabulations, les virgules et les points virgules par une nouvelle ligne dans le fichier nom_fichier, puis supprime les lignes vides
			$result = json_decode(exec("python ../scripts/stats_manuelles.py $rep_nouv_fichier $size2"), true);
            if ($result['error'] == "error"){
                echo "<h3> ERREUR : taille de l'échantillon incorrecte.</h3></div></body></html>";
				exit();
            }
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
            <?php $hist_loc = "../images/m".$result['hist'].".png";?>
			<h3>Histogramme généré n°m<?php echo $result['hist']; ?> : <a href=<?php echo $hist_loc; ?> class=button_link>Zoom de l'image</a></h3>
			<img src=<?php echo $hist_loc; ?> width=700 alt="Histogramme" class="img_center">
	</div>
    <footer>
    	<?php include '../bottom.php'; ?>
    </footer>
	</body>
</html>
