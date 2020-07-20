<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/style_page.css">
  <title> Conversion zone de texte vers fichier txt</title>
</head>
<body>
    <header>
        <?php include "top.php"; ?>
    </header>

	<div class="page">
		<h2 class="titre">Conversion zone de texte vers fichier txt</h2>
		<?php
		  if (!(empty ($_POST["nom_fichier"])) AND !(empty ($_POST["contenu"])))  {
		    $nom_fichier = $_POST["nom_fichier"];
		    $contenu = $_POST["contenu"];
			$nom_fichier=$nom_fichier.".txt";
			file_put_contents($nom_fichier,$contenu);
			echo "Écriture du fichier $nom_fichier effectuée.";
			echo "<br> <a href=".$nom_fichier." class=button_link>Ouvrir le fichier créé</a>";
		  }
		  else{
			  echo "<h3> ERREUR : un ou plusieurs champ(s) est/sont vide(s). </h3>";
		  }
		?>
		<br>
		<a href=passerelle.php class=button_link>Nouveau fichier</a>
	</div>
    <footer>
    	<?php include 'bottom.php'; ?>
    </footer>
</body>
</html>
