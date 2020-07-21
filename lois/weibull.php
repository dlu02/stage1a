<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="../css/style_page.css">
    <title>Loi de Weibull</title>
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
		<h3>Loi de Weibull <a href=lois.php class=button_link>Choisir une autre loi</a></h3>
        <div class="definition">
            <h4>Densité</h4>
            <p>$$f(x,a,b)= \dfrac{bx^{b-1}}{a^b} \mathrm{e}^{-(x/a)^b} \mathbb{1}_{[0,+\infty[}(x)$$
            où $\Gamma$ est la fonction Gamma d'Euler définie sur $\mathbb{R}_+^*$ par :
            $$\Gamma(x)= \displaystyle \int_0^{+\infty} t^{x-1}\mathrm{e}^{-t} \mathrm{d} t$$</p>
        </div>
        <div class="densite">
            <h4>Aperçu de la densité</h4>
            <img class="img_center" src="images/weibull.png" alt="Densité de Weibull" style="float: left;">
            <form method="POST" id="densite" action="submit.php" autocomplete="off">
                <input id="nom" name="nom" type="hidden" value="Loi de Weibull ">
                <input id="loi" name="loi" type="hidden" value="2">

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
		<tr> <th colspan="4">Propriétés de la loi de Weibull</th> </tr>
		<tr><td>Densité</td><td>$f(x,a,b)= \dfrac{bx^{b-1}}{a^b} \mathrm{e}^{-(x/a)^b} \mathbb{1}_{[0,+\infty[}(x)$</td><td>$\displaystyle E(X)$</td><td>$a\Gamma\left(1+\dfrac{1}{b}\right)$</td></tr>
		<tr><td>Domaines des paramètres</td><td>$ a >0 \,$  ,  $ b >0 $</td><td>$\displaystyle V(X)$</td><td>$a^2\left(\Gamma\left(1+\dfrac{2}{b}\right) - \Gamma\left(1+\dfrac{1}{b}\right)^2 \right)$ </td></tr>
		<tr><td>Fonction de répartition</td>
		<td>Pour $x\geqslant 0$, $F(x,a,b)=1-\exp\left( - \dfrac{x^b}{a^b} \right)$</td><td>Skewness</td><td>$\dfrac{a^3\Gamma(1+3/b)-3E(X)V(X)-E(X)^3}{V(X)^{3/2}}$</td></tr>
		<tr><td>Moments d'ordre $k$</td><td>$a^k \Gamma\left( 1+\dfrac{k}{b}\right)$ pour $b\geqslant 1$ </td><td>Kurtosis</td><td>$\gamma_{2}=\dfrac{M_4-4E(X)V(X)^{3/2}\gamma_1-6E(X)^2V(X)-E(X)^4}{V(X)^2}$</td></tr>
		</table>
	</div>
    <footer>
    	<?php include '../bottom.php'; ?>
    </footer>
</body>
</html>
