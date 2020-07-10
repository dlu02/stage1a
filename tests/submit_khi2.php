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
		<h2 class="titre">Test d'adéquation du Khi-2</h2>
		<h3>Résultats de l'analyse descriptive <a href=khi2.php class=button_link>Nouvelle analyse</a></h3>

		<?php
			if(isset($_FILES['fichier'])){
			    $nom_fichier = $_FILES['fichier']['name'];
			    $taille = $_FILES['fichier']['size'];
			    $file_tmp = $_FILES['fichier']['tmp_name'];
			    $file_type = $_FILES['fichier']['type'];
				$loi = $_POST['loi'];
				$modele = $_POST['param'];
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
            $replace = exec("sed -i 's/\ /,/g' donnees/$nom_fichier"); // remplace les espaces de séparation par des virgules dans le fichier nom_fichier
			$result = json_decode(shell_exec("python donnees/stats_khi2.py donnees/$nom_fichier $loi $modele $taillea"), true);
            if ($result['error'] == "error"){
                echo "<h4> ERREUR : Données discrètes. Veuillez vérifier vos données. </h4></div></body></html>";
                exit();
            }
            if ($result['error_dim'] == "error"){
                echo "<h4> ERREUR : Plusieurs variables présentes dans le fichier. Veuillez vérifier vos données. </h4></div></body></html>";
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
					<td><?php echo print_r($result['param_a']);?></td>
				</tr>
				<tr>
					<td>Paramètre $b$</td>
					<td><?php echo $result['param_b'];?></td>
				</tr>
			</table>
			<h3>Résultat du test du Khi-2</h3>
			<table class="alternate">
				<tr>
					<td>p-value</td>
					<td><?php echo $result['chi2_pvalue'];?></td>
				</tr>
			</table>
            <h4 style="text-align:center; color: red;">
                <?php if ($result['chi2_pvalue'] < 0.05){
                    echo "Hypothèse rejetée. L'échantillon étudié ne suit pas la loi $loi.";
                }
                else {
                    echo "Hypothèse non rejetée. L'échantillon étudié est susceptible de suivre la loi $loi.";
                }
                ?>
            </h4>
	</div>
	</body>
</html>
