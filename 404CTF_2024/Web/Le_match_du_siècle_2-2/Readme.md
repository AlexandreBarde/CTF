<h1>Le match du siècle [2/2]</h1>
<h3>Moyen - <b>200pts.</b></h3> 
<p>Vous avez déjà en votre possession un billet, néanmoins, pour impressionner votre famille, vous souhaiteriez des places VIP.

Auteurs : @<b>callister</b></p>

<hr>

Connexion :

`https://le-match-du-siecle.challenges.404ctf.fr`

<hr>

<h3>Solution</h3>

<i>J'ai utilisé cette méthode pour trouver le flag, mais ce n'était pas la solution de base, il aurait fallut utiliser les JWT.</i>

Dans la partie 1, lors du téléchargement du billet, on remarque que le site web fait une requête à une API :

<img src="1.png" style="width: 100%">

Avec une payload :

<img src="2.png" style="width: 40%">

En achetant d'autres billets et en récupérant l'image on voit que les requêtes sont similaires et juste la payload change, donc en changeant le token par `VIP` et en la renvoyant :

<img src="3.png" style="width: 70%">

Et hop, voilà le flag !

<img src="4.png" style="width: 70%">

Le flag est donc : <b>404CTF{b7554ee60d0020216749d428830a55f1}</b>