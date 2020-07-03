<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/style_page.css">
  <title>Statistiques descriptives</title>
</head>
<body>
    <header>
        <?php include "top.php"; ?>
    </header>
  <div class="page">
	  <h2 class="titre">Statistiques descriptives</h2>
    <h3>Étude descriptive de données saisies manuellement</h3>
	  <div>
		  <form method="POST" action="stats.php" autocomplete="off">
			  <table class="alternate">
				  <tr>
					<td>Nom du fichier où enregistrer les données</td>
					<td><input type="text" id="nom_fichier4" name="nom_fichier4"></td>
				  </tr>

				  <tr>
					<td>Taille de l'échantillon</td>
					<td><input type="number" id="size2" name="size2" min="1"></td>
				  </tr>
				  <tr>
					<td>Données à étudier <br> (syntaxe CSV : espace comme séparateur)</td>
					<td><textarea name="contenu2" rows="1" cols="50"></textarea></td>
				  </tr>
				  <tr> <th colspan="2"><input type="submit" name="submit4" id="submit4" value="Envoyer"></th> </tr>
			  </table>
		  </form>
	  </div>
	  <h3>Étude descriptive de données suivant une loi usuelle</h3>
    <div>
      <form method="POST" action="stats_usuelles.php" autocomplete="off">
        <table class="alternate">
          <tr class="row2">
          <td>Sélectionner la loi</td>
          <td><select name="lois" id="lois">
                <option value="">Choisir une loi</option>
                <option value="norm">Loi normale</option>
                <option value="exp">Loi exponentielle</option>
                <option value="pois">Loi de Poisson</option>
                <option value="binom">Loi binomiale</option>
              </select>
          </td>
          </tr>

          <tr>
          <td>Paramètre 1</td>
          <td><input type="number" id="parametre1" name="parametre1" step="any"></td>
          </tr>

          <tr>
          <td>Paramètre 2 <br> (dans le cas d'une loi à un seul paramètre, mettre -1)</td>
          <td><input type="number" id="parametre2" name="parametre2" step="any" value="-1"></td>
          </tr>

          <tr>
          <td>Taille de l'échantillon</td>
          <td><input type="number" id="size5" name="size5" min="1"></td>
          </tr>

		  <tr> <th colspan="2"><input type="submit" name="submit5" id="submit5" value="Envoyer"></th> </tr>
        </table>
      </form>
    </div>
  </div>
</body>
</html>
