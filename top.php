<div class="top">
	<h1 class="titre_top"><a href="/stage1a/index.php">Modélisation statistique de durée de vie</a></h1>
	<h3>Stage ENSIIE 1ère année 2020</h3>

	<p>Organisme d'accueil : CNAM département EPN06 Mathématiques et Statistiques <br>
	Tuteur de stage : Dariush GHORBANZADEH
	</p>
	<div style="clear: both;"></div>
	<ul class="menubar" id="menubar">
		<li><a href="/stage1a/index.php">Accueil</a></li>
		<li class="menu_deroulant"><a href="/stage1a/passerelle/passerelle.php" class="bouton_deroulant">Passerelle basique Python/PHP</a>
			<ul class="contenu_menu">
				<li><a href="/stage1a/passerelle/passerelle.php">Fonctions basiques Python/PHP</a></li>
				<li><a href="/stage1a/passerelle/stats_descriptives.php">Statistiques descriptives</a></li>
			</ul>
		</li>
		<li class="menu_deroulant"><a href="/stage1a/lois/lois.php" class="bouton_deroulant">Modèles de durée de vie</a>
			<ul class="contenu_menu">
				<li><a href="/stage1a/lois/hyperexpo.php">Loi hyperexponentielle</a> </li>
				<li><a href="/stage1a/lois/lomax.php">Loi Lomax</a> </li>
				<li><a href="/stage1a/lois/weibull.php">Loi de Weibull</a> </li>
				<li><a href="/stage1a/lois/expo_poly.php">Loi exponentielle polynomiale</a> </li>
				<li><a href="/stage1a/lois/burr.php">Loi de Burr</a> </li>
				<li><a href="/stage1a/lois/expo_convo.php">Loi exponentielle convolution</a> </li>
			</ul>
		</li>
		<li class="menu_deroulant"><a href="/stage1a/param/param.php" class="bouton_deroulant">Estimation de paramètres</a>
			<ul class="contenu_menu">
				<li><a href="/stage1a/param/param1.php">Contrainte sur les moments</a> </li>
				<li><a href="/stage1a/param/param2.php">Contrainte sur le skewness</a> </li>
			</ul>
		</li>
		<li class="menu_deroulant"><a href="/stage1a/tests/tests.php" class="bouton_deroulant">Tests statistiques</a>
			<ul class="contenu_menu">
				<li><a href="/stage1a/tests/khi2.php">Test du Khi-2</a> </li>
				<li><a href="/stage1a/tests/kolgomorov.php">Test de Kolgomorov-Smirnov</a> </li>
			</ul>
		</li>
		<li> <a href="/stage1a/passerelle/recherche_image_ask.php">Recherche résultats et images générées</a></li>
		<!-- <li><a href="/stage1a/etude_fichier.php">Étude d'un fichier</a></li> -->
	</ul>
	<br> <br>
</div>

<!-- Script JS menu après scroll -->
<script>
	window.onscroll = function() {myFunction()};

	var navbar = document.getElementById("menubar");
	var sticky = navbar.offsetTop;

	function myFunction() {
	  if (window.pageYOffset >= sticky) {
	    navbar.classList.add("sticky")
	  } else {
	    navbar.classList.remove("sticky");
	  }
	}
</script>

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

<!-- import police Fira Sans depuis Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
