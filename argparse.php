<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/style_page.css">
  <title>Générateur de nombres aléatoires</title>
</head>
<body>
    <header>
        <?php include "top.php"; ?>
    </header>

	<div class="page">
		<h2 class="titre">Générateur de nombres aléatoires</h2>
		<?php
		  if (!(empty ($_POST["nombre_min"])) AND !(empty ($_POST["nombre_max"])) AND !(empty ($_POST["taille"])) AND !(empty ($_POST["fichier"])))  {
			$min = $_POST["nombre_min"];
			$max = $_POST["nombre_max"];
			$taille = $_POST["taille"];
			$fichier = $_POST ["fichier"];
			$fichier = $fichier.".txt";
			$cmd = "python script.py ".$min." ".$max." ".$taille." ".$fichier;
			$sortie = shell_exec($cmd);
			echo "L'échantillon a bien été créé.";
			echo "<br> <a href=$fichier class=button_link>Ouvrir le fichier créé</a>";
		  }
		  else{
			  echo "<h3> ERREUR : un ou plusieurs champ(s) est/sont vide(s). </h3>";
		  }
		?>
		<br>
		<a href=passerelle.php class=button_link>Nouvel échantillon</a>


	</div>
</body>
</html>
