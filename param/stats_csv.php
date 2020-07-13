<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="/stage/css/style_page.css">
  <title>Résultats de l'analyse</title>
</head>
<body>
    <header>
        <?php include "../top.php"; ?>
    </header>

	<div class="page">
		<h2 class="titre">Statistiques descriptives</h2>
		<h3>Résultats de l'analyse <a href=param1.php class=button_link>Nouvelle analyse</a></h3>

		<?php
			if(isset($_FILES['fichier'])){
			    $nom_fichier = $_FILES['fichier']['name'];
			    $taille = $_FILES['fichier']['size'];
			    $file_tmp = $_FILES['fichier']['tmp_name'];
			    $file_type = $_FILES['fichier']['type'];
				$loi = $_POST['loi'];
				$taillea = $_POST['parametre_a'];
			    $extension_fichier=strtolower(end(explode('.',$_FILES['fichier']['name'])));
		    	$extensions= array("txt","dat","csv");
				if ($loi=="expo_poly" && $taillea <=0){
					echo "<h4> ERREUR : Le nombre de paramètres de a doit valoir au moins 1. </h4></div></body></html>";
					exit();
				}
			    if(in_array($extension_fichier,$extensions)=== false){
					echo $extension_fichier;
					echo "Extension non autorisée. Veuillez importer un fichier TXT ou DAT ou CSV </div></body></html>";
					exit();
			    }
				else{
					move_uploaded_file($file_tmp,"donnees/".$nom_fichier);
					echo "Succès, fichier ".$nom_fichier." bien importé";
			    }
			}
			else {
				echo "Pas de fichier sélectionné. </div></body></html>";
				exit();
			}
            $replace = exec("sed -i 's/ /\\n/g; s/,/\\n/g; s/\\t/\\n/g; s/;/\\n/g' donnees/$nom_fichier && sed -i '/^$/d' donnees/$nom_fichier"); // remplace les espaces de séparation, les tabulations, les virgules et les points virgules par une nouvelle ligne dans le fichier nom_fichier, puis supprime les lignes vides
			$result = json_decode(exec("python donnees/stats_csv.py donnees/$nom_fichier $loi 1 $taillea"), true);
            if ($result['error'] == "error"){
                echo "<h4> ERREUR : Données discrètes. Veuillez vérifier vos données. </h4></div></body></html>";
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
			<h3>Histogramme généré : <a href=hist.png class=button_link>Zoom de l'image</a></h3>
			<img src="hist.png" width=700px alt="Histogramme" class="img_center">
			<h3>Estimation des paramètres</h3>
			<?php
				if ($loi==""){
					echo "Veuillez sélectionner une loi de modélisation. </div></body></html>";
					exit();
				}
			?>
			<table class="alternate">
				<tr>
					<td>Paramètre $a$</td>
					<td><?php print_r($result['param_a']);?></td>
				</tr>
				<tr>
					<td>Paramètre $b$</td>
					<td><?php print_r($result['param_b']);?></td>
				</tr>
			</table>
	</div>
	</body>
</html>
