# Methodjoincreate
Recréer la méthode join 
Le but de cet exercice était de recréer la méthode join, encore une fois en la transformant en fonction.

La méthode join s'utilise sur une chaîne de caractère et permet de joindre plusieurs éléments d'une liste par la chaîne de caractère en question. Par exemple : "-".join(["Bonjour", "tout", "le", "monde"]) pour joindre les 4 mots dans la liste par des tirets.

Nous allons donc recréer cette méthode en la transformant en fonction : en premier argument nous passerons le caractère de séparation, puis tous les autres arguments correspondront aux mots que l'on veut joindre ensemble.

Notre fonction join pouvant accepter un nombre indéfini de paramètre, il nous faudra donc utiliser les "args" :

    def join(*args):

Notez que ce qui est vraiment important ici c'est l'astérisque. Vous pourriez remplacer "args" par "robert" et votre code fonctionnerait également. args est une convention et nous allons donc l'utiliser.

Cette syntaxe nous permet de passer un nombre indéfini d'arguments à notre fonction : ces arguments seront récupérables dans la liste "args" à l'intérieur de notre fonction.

À l'intérieur de notre fonction, nous récupérons donc le premier élément de la liste args, qui correspondra au séparateur utilisé pour joindre les arguments suivants :

    separateur = args[0]

Nous récupérons ensuite tous les arguments restants grâce à la syntaxe des slices :

    elements = args[1:]

Cette syntaxe indique que nous voulons récupérer tous les éléments à partir du 1er indice, jusqu'à la fin de la liste.
Cela nous permet donc de récupérer dans ce cas-ci les mots "Bonjour", "tout", "le" et "monde".

Il ne nous reste plus qu'à joindre ensemble tous les éléments récupérés dans la liste "elements" par le séparateur contenu dans la variable "separateur". Nous avons défini au début de la fonction une variable "resultat" qui contient une chaîne de caractère vide.

Nous allons passer à travers chaque élément grâce à une boucle for et ajouter un à un les éléments et le séparateur à la variable "resultat" :

    for element in elements:
        resultat += element + separateur

À ce stade-ci, la variable "resultat" contient donc :

    "Bonjour:tout:le:monde:"

Tout fonctionne à merveille, le seul problème est que nous avons un séparateur en trop à la fin de notre chaîne de caractère. Nous allons donc retourner notre chaîne de caractère en enlevant le dernier caractère, là encore grâce aux slices, qui peuvent également être utilisés directement sur une chaîne de caractère (car une chaîne de caractère est comme une liste de caractères individuels) :

    return resultat[:-1]

Cette syntaxe indique que nous souhaitons récupérer tous les caractères de la chaîne de caractère sauf le dernier (-1).
