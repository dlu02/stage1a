<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/style_page.css">
  <title>Recherche d'un fichier dans l'arborescence</title>
</head>
<body>
    <header>
        <?php include "top.php"; ?>
    </header>

	<div class="page">
		<h2 class="titre">Recherche d'un fichier dans l'arborescence</h2>
		<?php
		  if (!(empty ($_POST["nom_fichier_3"])))  {
		    $nom_fichier = $_POST["nom_fichier_3"];
			if (file_exists($nom_fichier)){
				echo "Le fichier $nom_fichier existe : ";
				echo "<br> <a href=".$nom_fichier." class=button_link>Ouvrir le fichier</a>";
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
		<a href=passerelle.php class=button_link>Nouvelle recherche</a>
	</div>
    <footer>
    	<?php include 'bottom.php'; ?>
    </footer>
</body>
</html>
