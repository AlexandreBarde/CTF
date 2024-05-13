<h1>Coup de circuit [1/3]</h1>
<h3>Facile - <b>200pts.</b></h3> 
<p><i>Ce challenge est le premier d'une série de trois challenges faciles. Le challenge suivant sera disponible dans la catégorie Renseignement en sources ouvertes une fois que vous aurez validé celui-ci.</i>
 
C'est la catastrophe ! Je me prépare pour mon prochain match de baseball, mais on m'a volé mon mojo ! Sans lui, je vais perdre, c'est certain... Je crois qu'on m'a eu en me faisant télécharger un virus ou je ne sais quoi, et le fichier a été supprimé de mon ordinateur. J'ai demandé de l'aide à un ami expert et il a extrait des choses du PC, mais il n'a pas le temps d'aller plus loin. Vous pourriez m'aider ?

Auteurs : @<b>Smyler</b></p>

<hr>

Identifiez le malware et donnez son condensat sha1. Le flag est au format suivant : `404CTF{sha1}`.

Fichier :
<a href="Collection.zip">Collection.zip</a> _(MD5 : `b018d1f191cb506275ea3ff6820a2065`)_

<hr>

<h3>Solution</h3>

Après avoir ouvert tous les fichiers du zip, je me suis concentré sur `20240505010820_Amcache_UnassociatedFileEntries.csv` car il contient tous les éxécutables ainsi que leur SHA1, et en regardant bien on trouve un fichier étrange nommé `sflgdqsfhbl.exe`, on récupère le SHA1 associé et voilà.

Le flag est donc : <b>404CTF{5cf530e19c9df091f89cede690e5295c285ece3c}</b>