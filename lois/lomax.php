<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="../css/style_page.css">
    <title>Loi Lomax</title>
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
		<h3>Loi Lomax <a href=lois.php class=button_link>Choisir une autre loi</a></h3>
        <div class="definition">
            <h4>Densité</h4>
            <p>$$f(x,a,b)= \dfrac{ab^a}{(b+x)^{a+1}} \mathbb{1}_{]0,+\infty[}(x)$$
            où $\Gamma$ est la fonction Gamma d'Euler définie sur $\mathbb{R}_+^*$ par :
            $$\Gamma(x)= \displaystyle \int_0^{+\infty} t^{x-1}\mathrm{e}^{-t} \mathrm{d} t$$</p>
        </div>
        <div class="densite">
            <h4>Aperçu de la densité</h4>
            <img class="img_center" src="images/lomax.png" alt="Densité de Lomax" style="float: left;">
            <form method="POST" id="densite" action="submit.php" autocomplete="off">
                <input id="nom" name="nom" type="hidden" value="Loi Lomax">
                <input id="loi" name="loi" type="hidden" value="1">

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
		<tr> <th colspan="4">Propriétés de la loi Lomax</th> </tr>
		<tr><td>Densité</td><td>$f(x,a,b)= \dfrac{ab^a}{(b+x)^{a+1}} \mathbb{1}_{]0,+\infty[}(x)$</td><td>$\displaystyle E(X)$</td><td>$\dfrac{b}{a-1}$ pour $a>1$</td></tr>
		<tr><td>Domaines des paramètres</td><td>$ a >0 \,$  ,  $ b >0 $</td><td>$\displaystyle V(X)$</td><td>$\dfrac{ab^2}{(a-1)^2(a-2)}$ pour $a>2$</td></tr>
		<tr><td>Fonction de répartition</td>
		<td>Pour $x>0$, $F(x,a,b)=1-\left( 1+\dfrac{x}{b} \right)^{-a}$</td><td>Skewness</td><td>$\dfrac{2(1+a)}{a-3}\sqrt{\dfrac{a-2}{a}}$ pour $a>3$</td></tr>
		<tr><td>Moments d'ordre $k$</td><td>$\dfrac{b^k \Gamma(a-k) \Gamma(k+1)}{\Gamma(a)}$ pour $a>k$ </td><td>Kurtosis</td><td>$\dfrac{6(a^3+a^2-6a-2)}{a(a-3)(a-4)}$ pour $a>4$</td></tr>
		</table>
	</div>
    <footer>
    	<?php include '../bottom.php'; ?>
    </footer>
</body>
</html>
