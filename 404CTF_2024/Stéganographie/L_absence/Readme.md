<h1>L'absence</h1>
<h3>Introduction - <b>100pts.</b></h3> 
<p>Hier, Francis n'était pas là à son épreuve de barres asymétriques, il nous a envoyé une lettre d'excuse. Malheureusement, la fin de sa lettre est illisible.
Déchiffrez la fin de ses excuses.

Auteurs : @<b>Crevette</b> & @<b>Ceriseuh</b></p>

Fichiers :

<a href="./lettre.txt">lettre.txt</a>

<hr>

<h3>Solution</h3>

En voyant le message à déchiffrer :

```
bonsoir, désolé pour le déranGement. je n'ai pas pu Y aller hier pour l'épreuve de barres asyMétriques. désolé si je N'ai pas été à lA hauteur de voS attenTes, je feraIs mieux aux épreuves publiQUes de dEmain. 


bises.
franciS vigenere.

ps :
Kl qsfwm, r'qc hm s'ynfefmmh wej rc peahxik xi eg lmgigg i uni voqevmmem fuv vkq srnk jcy psmryurnl yiyli hkppee ehv fuck ! Syuf ahkmi orw rmztuw kmsbijifq, w'aa xvvcr ha jq eelkwkpij. Rc hbiub : 404KJZ{RwBmxrzHtaBywVxybramqAlj}
```

On peut voir que dans le premier paragraphe, certaines lettres sont en majuscules, ainsi on trouve `GYMNASTIQUES` ainsi une référence intéressante `franciS vigenere` qui fait référence au `chiffre de Vigenère`.

En lisant l'article Wikipédia associé, <a href="https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re">Chiffre de Vigenère</a>: 

```
Le chiffre de Vigenère est un système de chiffrement par substitution polyalphabétique dans lequel une même lettre du message clair peut, suivant sa position dans celui-ci, être remplacée par des lettres différentes, contrairement à un système de chiffrement mono alphabétique comme le chiffre de César (qu'il utilise cependant comme composant). Cette méthode résiste ainsi à l'analyse de fréquences, ce qui est un avantage décisif sur les chiffrements mono alphabétiques. Cependant le chiffre de Vigenère a été percé par le major prussien Friedrich Kasiski qui a publié sa méthode en 1863. Depuis cette époque, il n‘offre plus aucune sécurité.

[...]

Ce chiffrement introduit la notion de clé. Une clé se présente généralement sous la forme d'un mot ou d'une phrase. Pour pouvoir chiffrer le texte, chaque caractère utilise une lettre de la clé pour effectuer la substitution. Plus la clé est longue et variée, mieux le texte est chiffré.
```

En utilisant la clef que nous avons trouvé auparavant ainsi que l'algorithme, celui nous permet de décoder le texte :

```
en effet, j'ai du m'absenter car le drapeau de ma nation a ete dissimule par des gens qui voulaient faire perdre mon pays ! mais apres une longue recherche, j'ai enfin pu le retrouver. le voici : 404ctf{nevolezpaslesdrapeauxsvp}
```

Le flag est donc : <b>404CTF{nevolezpaslesdrapeauxsvp}</b>