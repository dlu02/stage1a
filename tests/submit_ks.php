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
		<h2 class="titre">Test d'adéquation de Kolgomorov-Smirnov</h2>
		<h3>Résultats de l'analyse <a href=khi2.php class=button_link>Nouvelle analyse</a></h3>

		<?php
			if(isset($_FILES['fichier'])){
			    $nom_fichier = $_FILES['fichier']['name'];
			    $taille = $_FILES['fichier']['size'];
			    $file_tmp = $_FILES['fichier']['tmp_name'];
			    $file_type = $_FILES['fichier']['type'];
				$loi = $_POST['loi'];
				$modele = $_POST['param'];
			    $extension_fichier=strtolower(end(explode('.',$_FILES['fichier']['name'])));
		    	$extensions= array("txt","dat","csv");
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
			$result = json_decode(exec("python donnees/stats_ks.py donnees/$nom_fichier $loi $modele"), true);
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
					<td><?php echo $result['param_a'];?></td>
				</tr>
				<tr>
					<td>Paramètre $b$</td>
					<td><?php echo $result['param_b'];?></td>
				</tr>
			</table>
			<h3>Résultat du test de Kolgomorov-Smirnov</h3>
			<table class="alternate">
				<tr>
					<td>p-value</td>
					<td><?php echo $result['ks_pvalue'];?></td>
				</tr>
			</table>
	</div>
	</body>
</html>
