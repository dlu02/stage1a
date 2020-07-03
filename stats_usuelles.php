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
		  $param1 = $_POST["parametre1"];
		  $param2 = $_POST["parametre2"];
		  $taille = $_POST["size5"];
		  $lois = $_POST["lois"];
		  if (empty ($_POST["lois"])){
			  echo "<h3> ERREUR : veuillez choisir une loi. </h3></div></body></html>";
			  exit();
		  }
		  if (!(empty ($_POST["size5"]))){
		    if ($lois == "exp"){
		      $choix=2;
		      if ($param1 <= 0){
		        echo "<h3> ERREUR : le paramètre d'une loi exponentielle doit être strictement positif. </h3></div></body></html>";
				exit();
		      }
		    }
		    else if ($lois == "norm"){
				if ((empty ($_POST["parametre1"])) && (empty ($_POST["parametre2"]))){
					echo "<h3> ERREUR : paramètres manquants. </h3>";
					exit();
				}
				$choix=1;
		    	if ($param2 < 0){
					echo "<h3> ERREUR : le paramètre 2 (sigma) d'une loi normale doit être positif. </h3></div></body></html>";
					exit();
		    	}
		    }
		    else if ($lois == "pois"){
		      $choix=3;
		      if ($param1 <= 0){
				  echo "<h3> ERREUR : le paramètre 1 d'une loi de Poisson doit être positif. </h3></div></body></html>";
				  exit();
		      }
		    }
		    else{
		      $choix=4;
		      if ($param2 > 1 || $param2 < 0){
				  echo "<h3> ERREUR : le paramètre 2 d'une loi binomiale (p) doit être compris entre 0 inclus et 1 inclus. </h3></div></body></html>";
				  exit();
		      }
			  if ($param1 <= 0){
				  echo "<h3> ERREUR : le paramètre 1 d'une loi binomiale (n) doit être strictement positif. </h3></div></body></html>";
				  exit();
			  }
		    }
		  }
		  else {
			  echo "<h3> ERREUR : taille manquante. </h3></div></body></html>";
			  exit();
		  }

		  $result = json_decode(exec("python lois.py ".$choix." ".$param1." ".$param2." ".$taille), true);

		  function print_loi($choix){
		    switch ($choix){
		      case 1:
		        return "loi normale";
		        break;
		      case 2:
		        return "loi exponentielle";
		        break;
		      case 3:
		        return "loi de Poisson";
		        break;
		      case 4:
		        return "loi binomiale";
		        break;
		    }
		  }
		  $loi=print_loi($choix);
		  echo "Rappel : vous avez choisi de générer un échantillon de taille ".$taille." suivant une ".$loi." de paramètres ".$param1." et ".$param2;
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
		<h3>Histogramme généré : <a href=hist.png class=button_link>Zoom de l'image</a></h2>
		<img src="hist.png" width=700px alt="Histogramme" class="img_center">
	</div>
</body>
</html>
