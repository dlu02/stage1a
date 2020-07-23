<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="../css/style_page.css">
  <title>Recherche d'un résultat</title>
</head>
<body>
    <header>
        <?php include "../top.php"; ?>
    </header>

	<div class="page">
		<h2 class="titre">Recherche d'un résultat</h2>
        <?php
          if (!(empty ($_POST["nom_fichier"])))  {
            $loc_fichier = "../save/".$_POST["nom_fichier"].".html";
            $nom_fichier = $_POST["nom_fichier"].".html";
            $nom = $_POST["nom_fichier"];
            if (file_exists($loc_fichier)){
                header('Location: ../save/'.$nom.'.html');
                exit();
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
    <footer>
    	<?php include '../bottom.php'; ?>
    </footer>
</body>
</html>
