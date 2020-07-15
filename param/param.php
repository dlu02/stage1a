<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../css/style_page.css">
	<title>Estimation de paramètres</title>
</head>

<body>
    <header>
        <?php include '../top.php'; ?>
    </header>

	<div class="page">
		<h2 class="titre">Estimation de paramètres</h2>
		<p class="update_time">
			<?php echo "Dernière mise à jour : ". date("d/m/Y H:i:s.",filemtime(__FILE__)); ?>
		</p>
			<p>
				Soit $(X_1,...,X_n)$ l'échantillon associé au fichier de données de l'utilisateur.
			</p>
			<div class="definition">
				<h4>Définition (Vraisemblance et log-vraisemblance)</h4>
				<p>Considérons un échantillon $(X_1,...,X_n)$ associé au fichier ou à la saisie par l'utilisateur, suivant une même loi $L$ de densité $f(x,a,b)$. On appelle <b>vraisemblance</b> associée à l'échantillon $(X_1,...,X_n)$ la quantité :
				$$\ell (x_1,...,x_n ; a,b) = \prod_{i=1}^n f(x_i,a,b)$$
				De même, on appelle <b>log-vraisemblance</b> associée à l'échantillon $(X_1,...,X_n)$ la quantité :
				$$\mathcal{L} (x_1,...,x_n;a,b) = \sum_{i=1}^n \ln (f(x_i,a,b))$$ </p>
			</div>
			<p>Nous allons estimer les paramètres de cet échantillon en maximisant sa vraisemblance (ou, ce qui revient au même, la log-vraisemblance). Dans notre cas, nous ajoutons des contraintes sur l'échantillon, décrites ci-dessous. Les réels $a^*$ et $b^*$ vérifiant cette propriété sont alors une estimation des paramètres de l'échantillon. </p>
			<h3><a href="param1.php">Maximum de vraisemblance sous contraintes sur l'espérance et le moment d'ordre 2 empiriques</a></h3>
			$$\max\limits_{a,b} \mathcal{L} (x_1,...,x_n;a,b) \quad \text{s.c.} \quad \begin{cases} \displaystyle E(X)=\dfrac{1}{n}\sum_{i=1}^n x_i \\ \displaystyle E(X^2) = \dfrac{1}{n}\sum_{i=1}^n x_i^2 \end{cases}$$

			<h3><a href="param2.php">Maximum de vraisemblance sous contrainte de signe du skewness $(\gamma_1)$</a></h3>
			$$\max\limits_{a,b} \mathcal{L} (x_1,...,x_n;a,b) \qquad \text{s.c.} \quad E\left( \left( X-E(X) \right)^3 \right) \gamma_1 \geqslant 0$$
	</div>
</body>
<footer>
	<?php include '../bottom.php'; ?>
</footer>
</html>
