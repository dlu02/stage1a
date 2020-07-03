<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title><?php echo $_POST['nom']; ?></title>
<link rel="stylesheet" type="text/css" href="../css/style_page.css">

<!-- Pour LaTeX -->
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      jax: ["input/TeX", "output/HTML-CSS"],
      extensions: ["tex2jax.js"],
      "HTML-CSS": { preferredFont: "TeX", availableFonts: ["STIX","TeX"] },
      tex2jax: { inlineMath: [ ["$", "$"], ["\\(","\\)"] ], displayMath: [ ["$$","$$"], ["\\[", "\\]"] ], processEscapes: true, ignoreClass: "tex2jax_ignore|dno" },
      TeX: { noUndefined: { attributes: { mathcolor: "red", mathbackground: "#FFEEEE", mathsize: "90%" } } },
      messageStyle: "none"
    });
</script>
<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML"></script>

<!-- <script type="text/javascript"
  async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js/MathJax.js?config=TeX-MML-AM_CHTML">
</script> -->
<!-- Fin LaTeX -->
</head>

<body>
	<header>
		<?php include "../top.php"; ?>
	</header>

	<div class="page">
		<h2 class="titre">Étude de lois</h2>
		<h3><?php echo $_POST['nom']; ?><a href=lois.php class=button_link>Choisir une autre loi</a></h3>
		<!-- <p>Densité : <br>
		<?php
			if ($_POST['loi']==0){
				echo "$$ \displaystyle  f(x,a,b)= \dfrac{ab}{a+b}\left(\mathrm{e}^{-ax}+\mathrm{e}^{-bx}\right) \mathbb{1}_{]0,+\infty[}(x)$$";
			}
			elseif ($_POST['loi']==1){
				echo "$$ f(x,a,b)= \dfrac{ab^a}{(b+x)^{a+1}} \mathbb{1}_{]0,+\infty[}(x) $$";
			}
			elseif ($_POST['loi']==2){
				echo "$$ f(x,a,b)= \dfrac{bx^{b-1}}{a^b} \mathrm{e}^{-(x/a)^b} \mathbb{1}_{[0,+\infty[}(x)$$";
			}
			elseif ($_POST['loi']==3){
				echo "$$ f(x,a,b)= \dfrac{abx^{a-1}}{(1+x^a)^{b+1}} \mathbb{1}_{]0,+\infty[}(x)$$";
			}
			elseif ($_POST['loi']==4){
				echo "$$\displaystyle f(x,a,b)= C(a,b) \left(\sum_{k=1}^m a_kx^k \right) \mathrm{e}^{-bx} \mathbb{1}_{]0,+\infty[}(x)$$";
			}
		?> -->
		<table class="alternate">
			<tr> <th colspan="2">Tracé de la densité</th> </tr>
			<tr><td>Valeur de $a$</td><td><?php echo $_POST['parametre1']; ?></td></tr>
			<tr><td>Valeur de $b$</td><td><?php echo $_POST['parametre2']; ?></td></tr>
		</table>
		<?php
			if (!(empty ($_POST["parametre1"])) AND !(empty ($_POST["parametre2"])) AND ($_POST["loi"]=="4")){
				$a= $_POST['parametre1'];
				$b= $_POST['parametre2'];
				file_put_contents("temp.txt",$a);
				$cmd = "python expopoly.py temp.txt ".$b;
				exec($cmd);
				echo "<h3>Graphique généré : <a href=densite.png class=button_link>Zoom de l'image</a></h3>
				<img src=densite.png width=700px alt=Densite class=img_center>";
			}
			else if (!(empty ($_POST["parametre1"])) AND !(empty ($_POST["parametre2"]))){
				$a= $_POST['parametre1'];
				$b= $_POST['parametre2'];
				$loi= $_POST['loi'];
				$cmd = "python densite_v2.py ".$a." ".$b." ".$loi;
				exec($cmd);
				echo "<h3>Graphique généré : <a href=densite.png class=button_link>Zoom de l'image</a></h3>
				<img src=densite.png width=700px alt=Densite class=img_center>";
			}
			else {
				echo "<h3> ERREUR : un ou plusieurs champ(s) est/sont vide(s). </h3></div></body></html>";
				exit();
			}
		?>
	</div>
</body>
</html>
