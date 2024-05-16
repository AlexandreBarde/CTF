<h1>Bugdroid Fight [1/2]</h1>
<h3>Facile - <b>200pts.</b></h3> 
<p>Un Bugdroid sauvage apparait !

Il est temps de mettre vos compétences de boxe en pratique, mais attention, cette fois il n'y a ni ring ni arbitre. Assurez-vous de bien observer autour de vous car, comme sur le ring, il est important de connaître les habitudes de son adversaire. Bon courage,

<hr >

Retrouvez le message du Bugdroid.

Format de flag : `404CTF{message}`.

<hr>

Fichier : 

<a href="./Bugdroid_Fight_-_Part_1.apk">Bugdroid_Fight_-_Part_1.apk</a>

Auteur : @<b>Whiplash</b></p>

<hr>

<h3>Solution</h3>

Tout d'abord il va falloir décompiler cet APK, j'ai utilisé `jadx`, ce qui nous permet d'avoir accès au code source.

Et maintenant il va falloir chercher dans les classes si on voit des choses étranges, et on tombe vite sur cette variable

```java
// MainActivityKt
public static final String element = "Br4v0_tU_as_";
```

Ainsi que

```xml
res/values/strings.xml

<string name="attr_special">tr0uv3_m0N</string>
```

Et

```java
// Utils
String lastPart = "_m3S5ag3!";
```

Le flag est donc : <b>404CTF{Br4v0_tU_as_tr0uv3_m0N_m3S5ag3}</b>