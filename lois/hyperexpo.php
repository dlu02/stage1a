<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="../css/style_page.css">
    <title>Loi hyperexponentielle</title>
</head>

<body>
	<header>
		<?php include "../top.php"; ?>
	</header>

	<div class="page">
		<h2 class="titre">Modèles de durée de vie</h2>
        <p class="update_time">
            <?php echo "Dernière mise à jour : ". date("d/m/Y H:i:s.",filemtime(__FILE__)); ?>
        </p>
		<h3>Loi hyperexponentielle <a href=lois.php class=button_link>Choisir une autre loi</a></h3>
        <div class="definition">
            <h4>Densité</h4>
            <p>$$f(x,a,b)= \dfrac{ab}{a+b}\left(\mathrm{e}^{-ax}+\mathrm{e}^{-bx}\right) \mathbb{1}_{]0,+\infty[}(x)$$</p>
        </div>
        <div class="densite">
            <h4>Aperçu de la densité</h4>
            <img class="img_center" src="images/hyperexpo.png" alt="Densité hyperexponentielle" style="float: left;">
            <form method="POST" id="densite" action="submit.php" autocomplete="off">
                <input id="nom" name="nom" type="hidden" value="Loi hyperexponentielle ">
                <input id="loi" name="loi" type="hidden" value="0">

                <table class="alternate">
                <tr> <th colspan="2">Tracé de la densité</th> </tr>
                <tr><td>Valeur de $a$</td><td><input type="number" id="parametre1" name="parametre1" step="any" min=0></td></tr>
                <tr><td>Valeur de $b$</td><td><input type="number" id="parametre2" name="parametre2" step="any" min=0></td></tr>
                <tr> <th colspan="2"><input type="submit" name="submit5" id="submit5" value="Tracé de la densité"></th> </tr>
                </table>
            </form>
            <div style="clear: both;"></div>
        </div>
		<table class="alternate">
		<tr> <th colspan="4">Propriétés de la loi hyperexponentielle</th> </tr>
		<tr><td>Densité</td><td>$ \displaystyle  f(x,a,b)= \dfrac{ab}{a+b}\left(\mathrm{e}^{-ax}+\mathrm{e}^{-bx}\right) \mathbb{1}_{]0,+\infty[}(x)$</td><td>$\displaystyle E(X)$</td><td>$\dfrac{b}{a(a+b)}+\dfrac{a}{b(a+b)}$</td></tr>
		<tr><td>Domaines des paramètres</td><td>$ a >0 \,$  ,  $ b >0 $</td><td>$\displaystyle V(X)$</td><td>$\dfrac{b^2+2ab}{a^2(a+b)^2} + \dfrac{a^2 + 2ab}{b^2(a+b)^2}$</td></tr>
		<tr><td>Fonction de répartition</td>
		<td>Pour $x>0$, $\displaystyle F(x,a,b)=\dfrac{a b}{a+b}\left(\dfrac{1-\mathrm{e}^{-a x}}{a} + \dfrac{1-\mathrm{e}^{-b x}}{b} \right)$</td><td>Skewness</td><td>$\displaystyle \gamma_{1}=\dfrac{M_3-3E(X)V(X)-E(X)^3}{V(X)^{3/2}}  $</td></tr>
		<tr><td>Moments d'ordre $k$</td><td>$\displaystyle \mathbb{E}[X^k]=\dfrac{b}{a+b}\dfrac{k!}{a^k}+\dfrac{a}{a+b}\dfrac{k!}{b^k}$</td><td>Kurtosis</td><td>$\displaystyle \gamma_{2}=\dfrac{M_4-4E(X)V(X)^{3/2}\gamma_1-6E(X)^2V(X)-E(X)^4}{V(X)^2} $</td></tr>
		</table>
	</div>
    <footer>
    	<?php include '../bottom.php'; ?>
    </footer>
</body>
</html>
