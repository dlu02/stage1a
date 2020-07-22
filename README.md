# Code source stage 1A 2020

## Introduction :
Pour plus de facilité, et pour voir le résultat, vous pouvez accéder à la page web hébergée par moi-même directement à l'adresse : http://dlu02.freeboxos.fr/stage.

**NB : les liens de l'en-tête sont configurés dans le cas où le contenu de ce git est situé dans ``~/stage` où `~` est le répertoire racine du serveur web. Si vous clonez le git, n'oubliez pas d'adapter les chemins absolus présents dans le fichier `top.php` à votre configuration !**

## Présentation globale :
- La page d'accueil est le fichier `index.php`.
- Le répertoire `scripts` contient tous les scripts Python nécessaires à la page web :
  - `annexes.py` contient quelques fonctions annexes nécessaires aux autres scripts Python,
  - `bib_densite.py` contient la bibliothèque de tracé des densités,
  - `bib_estimation.py` contient la bibliothèque d'estimation des paramètres par maximum de vraisemblance selon les deux modèles présentés sur le site,
  - `densite.py` et `densite_expopoly.py` contiennent le script de tracé des densités à partir des paramètres passés sur le site,
  - `estimation.py` contient le script d'estimation des paramètres à partir des paramètres passés sur le site,
  - `gen_aleat.py` contient le script de génération de nombres aléatoires,
  - `histogramme.py` contient la bibliothèque de tracé des histogrammes,
  - `lois_theo.py` contient les fonctions de répartition, densités, moments, espérances, variances et log-vraisemblances théoriques des lois
  - `stats_manuelles.py` contient le script d'étude descriptive des données saisies dans la passerelle
  - `stats_usuelles.py` contient le script d'étude descriptive de données générées à partir de lois usuelles
  - `tests.py` contient le script implémentant les tests du Khi-2 et de Kolgomorov-Smirnov
  - Le CSS du site est dans le répertoire `css`,
  - Toutes les images générées par le site sont localisées dans le dossier `images`
  - Tous les répertoires contiennent le code source des pages web pour chaque partie, et chaque fichier envoyé au site est téléchargé sur le serveur dans le dossier donnees contenu dans le répertoire lié à chaque partie.

- L'en-tête du site est contenu dans `top.php` et est inclus via PHP dans chaque page du site, et de même pour le pied de page du site, contenu dans `bottom.php`

Bonne lecture !

Damien Lu
