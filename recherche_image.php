<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/style_page.css">
  <title>Recherche d'un histogramme ou d'une densité</title>
</head>
<body>
    <header>
        <?php include "top.php"; ?>
    </header>

	<div class="page">
		<h2 class="titre">Recherche d'un histogramme ou d'une densité</h2>
		<?php
		  if (!(empty ($_POST["nom_fichier_3"])))  {
		    $loc_fichier = "images/".$_POST["nom_fichier_3"].".png";
            $nom_fichier = $_POST["nom_fichier_3"].".png";
            $nom = $_POST["nom_fichier_3"];
			if (file_exists($loc_fichier)){
                echo "<h3>Histogramme généré n°$nom : <a href=$loc_fichier class=button_link>Zoom de l'image</a></h3>
                <img src=$loc_fichier width=700px alt='Histogramme' class=img_center>";
			}
			else {
				echo "<h3> ERREUR : le fichier $nom_fichier n'existe pas. </h3>";
			}
		  }
		  else{
			  echo "<h3> ERREUR : un ou plusieurs champ(s) est/sont vide(s). </h3>";
		  }
		?>
		<br>
		<a href=recherche_image_ask.php class=button_link>Nouvelle recherche</a>
	</div>
</body>
<footer>
	<?php include 'bottom.php'; ?>
</footer>
</html>
