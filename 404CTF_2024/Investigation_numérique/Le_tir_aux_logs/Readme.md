<h1>Le tir aux logs</h1>
<h3>Introduction - <b>100pts.</b></h3> 
<p>Il semblerait qu'une personne malveillante ait réussi à se connecter sur le site d'inscription d'une compétition de tir à l'arc.
Aidez-nous à investiguer sur cette attaque via le fichier de logs de notre serveur. Quel est l'URL complète (formée du nom de domaine, puis de la ressource), qui a permis de se connecter de manière frauduleuse ?</p>
 
<hr>

<p>Le flag attendu est l'URL utilisée par l'attaquant pour exploiter une vulnérabilité du site avec succès, entouré du format habituel.
Par exemple, si l'attaquant se rend sur la page https://example.com/page.php?authenticated=1 pour se connecter de manière frauduleuse, le flag sera 404CTF{https://example.com/page.php?authenticated=1}.

Le décodage url n'est pas nécessaire.
Par ailleurs, toutes les IP utilisées sont fictives et non pertinentes.

Auteurs : @<b>ElPouleto</b></p>

<hr>


<h3>Solution</h3>

<b>TODO</b>

Le flag est donc : <b>404CTF{http://www.inscription_tir_arc.com/index.php?username=admin%27%23&password=test}</b>