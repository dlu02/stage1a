<?php ob_start(); ?>
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

    <?php
    $test2 = $_POST['test2'];
    $test = $_POST['test']; ?>

	<div class="page">
		<h2 class="titre">Test d'adéquation <?php echo $test;?> </h2>
		<h3>Résultats de l'analyse descriptive <a href=tests.php class=button_link>Nouvelle analyse</a></h3>

		<?php
			if (isset($_FILES['fichier'])){
			    $nom_fichier = $_FILES['fichier']['name'];
			    $taille = $_FILES['fichier']['size'];
			    $file_tmp = $_FILES['fichier']['tmp_name'];
			    $file_type = $_FILES['fichier']['type'];
				$loi = $_POST['loi'];
				$modele = $_POST['param'];
				$taillea = $_POST['parametre_a'];
			    $extension_fichier=strtolower(end(explode('.',$_FILES['fichier']['name'])));
		    	$extensions= array("txt","dat","csv");
			    if (in_array($extension_fichier,$extensions) === false){
					echo "<h4> ERREUR : Extension non autorisée ou fichier inexistant. Veuillez importer un fichier TXT ou DAT ou CSV. </h4> </div></body></html>";
					exit();
			    }
                if (empty ($_POST["loi"])) {
                    echo "<h4> ERREUR : Veuillez sélectionner une loi. </h4> </div> </body> </html>";
                    exit();
                }
                if (empty ($_POST["param"])){
                    echo "<h4> ERREUR : Veuillez sélectionner un modèle d'estimation des paramètres.</h4> </div></body></html>";
                    exit();
                }
                if ($loi=="expo_poly" && $taillea < 1){
                    echo "<h4> ERREUR : Le nombre de paramètres de a doit valoir au moins 1. </h4></div></body></html>";
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
			$result = json_decode(shell_exec("python ../scripts/tests.py donnees/$nom_fichier $loi $modele $taillea $test2"), true);
            if ($result['error'] == "error"){
                echo "<h4> ERREUR : Données discrètes. Veuillez vérifier vos données. </h4></div></body></html>";
                exit();
            }
            $histogr = "../images/".strval($result['hist']).".png";
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
			<h3>Histogramme généré n°<?php echo $result['hist']; ?> : <a href=<?php echo $histogr; ?> class=button_link>Zoom de l'image</a></h3>
            <img src=<?php echo $histogr; ?> width=700 alt='Histogramme' class=img_center>
            <p>Vous pouvez retrouver l'histogramme ci-dessus dans la partie Recherche avec le code ci-dessus.</p>
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
					<td><?php echo $result['test_pvalue'];?></td>
				</tr>
			</table>
            <h4 style="text-align:center; color: red;">
                <?php if ($result['test_pvalue'] < 0.05){
                    echo "Hypothèse rejetée. L'échantillon étudié ne suit pas la loi $loi.";
                }
                else {
                    echo "Hypothèse non rejetée. L'échantillon étudié est susceptible de suivre la loi $loi.";
                }
                ?>
            </h4>
			<div class="densite">
				<p> Cette page a été sauvegardée. Vous pouvez la retrouver à posteriori dans la partie recherche, muni du numéro d'histogramme ci-dessus, qui est : <?php echo $result['hist'];?>, ou avec le lien ci-contre : <a href= <?php echo "../save/".$result['hist'].".html"; ?> class="button_link">Lien vers cette page</a> </p>
			</div>
	</div>
    <footer>
    	<?php include '../bottom.php'; ?>
    </footer>
</body>
</html>

<?php
$dir = '../save/'.$result['hist'].'.html';
file_put_contents($dir, ob_get_contents()); ?>
