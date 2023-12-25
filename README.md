# Cryptosystème de Merckle-Hellman ou de Kifli


## Présentation

Ce repository est une implémentation du cryptosystème de Merckle-Hellman ainsi que l'attaque permettant de le casser. J'ai effectué ce projet pour mes cours de cryptographie. Dans le sujet de base, le cryptosystème s'appelait cryptosystème de Kifli, comme une énigme nous avons du retrouver le véritable cryptosystème qui se cachait.
Voici le l'énoncé: 
```
Le NIST (National Institute of Standards and Technology, organisme de standardisation américain) organise depuis 2016 un concours international en vue de la standardisation d'algorithmes cryptographiques post-quantiques. Dans le cadre de ce concours, le NIST a publié le 5 juillet dernier une liste de quatre premiers algorithmes sélectionnés.

Pourtant, un crypto-système qui semblait très prometteur n'a pas été retenu dans cette liste. Il s'agit d'un système de chiffrement original, qui utilise des poches et des pochons. Il a été proposé, il y a quelques années, par une jeune informaticienne bordelaise, Augustine Kifli, et nous allons voir comment fonctionne ce système dans le cadre de ce projet.
```
Et pour de plus amples explications sur le cryptosystème de Kifli, [le site du sujet](https://ramet.gitlab.io/r3.09-crypto/SAE.html).
J'explique plus loin notre démarche pour arriver à la solution.

## Fonctionnalités

Voici une liste complète des différents prototypes implémentés
```py
gen_pochon(n)
gen_cle_privee(n)
gen_cle_publique(cle_privee) 
solve_pochon(pochon, c)
chiffre(message, cle_publique)
dechiffre(message_chiffre, cle_privee)
test_chiffrement_dechiffrement(message, n)
```

## Résolution

Tout au long du sujet nous avons pu remarquer de nombreux indices sur ce cryptosystème créé par la mystérieuse Augustine Kifli. Pourtant, aucune trace de publications et encore moins de la soit disante conceptrise du cryptosystème.
Nous avons essayer de résoudre ce mystère tout en répondant à la question posée en fin de sujet:
```D'après vous, le NIST a-t-il eu raison de ne pas retenir le crypto-système de Kifli dans sa liste d'algorithmes post-quantique ?```



### Un problème de poche mais pas que...

Après de nombreuses recherches, nous avons finis par découvrir ce qui se cache réellement derrière le problème de poche. Il ne s'agit pas uniquement d'un problème de poche mais aussi de sac à dos !

Le cryptosystème de Kifli est en réalité le [cryptosystème de Merkle-Hellman](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem), un sous-problème du problème de sac à dos.
Ce cryptosystème, présenté par Martin Hellman, Ralph Merkle et Whitfield Diffie, est à la base du premier chiffrement asymétrique. Il est utilisé dans des primitives et des protocoles de cryptographie, tels que le cryptosystème de Merkle-Hellman. <br/>

En lisant les pages wikipédia nous apprenons que le problème du sac à dos est en effet NP-complet mais que des attaques de cryptanalyses existent sur le cryptosystème Merkle-Hellman. En 1984, Adi Shamir a publié une attaque qui permet de déchiffrer des messages chiffrés en temps polynomial sans utiliser la clé privée. Voici la publication originale: [pdf](https://static.aminer.org/pdf/PDF/000/120/454/a_polynomial_time_algorithm_for_breaking_the_basic_merkle_hellman.pdf). 
Une différence que nous avons pu constater, c'est que le système de Merkle-Hellman n'utilise pas de permutation.<br/>


### Casser le cryptosystème de Kifli

Nous avons alors essayer de casser le cryptosystème. La publication de Adi Shamir étant vieille et peu lisible, nous avons trouvé un autre paper plus clair et concis: APPLICATIONS DE L’ALGORITHME LLL EN CRYPTOGRAPHIE par Abderrahmane Nitaj.

Grâce à ces précisions nous avons pu concevoir un script sage math disponible dans [cryptanalyse.sage](cryptanalyse.sage) . En mettant comme entrée un message chiffré et une clé publique, nous avons bien réussi à retrouver le message en clair.
Mission accomplie ! 

### L'ancêtre du croissant

Une de nos pistes pour le nom "Kifli" serait la suivante: https://fr.wikipedia.org/wiki/Kifli
Celle ci nous indique que le Kifli serait l'ancêtre du croissant ce qui peut être lié au fait que dans l'énoncé du problème on parle chocolatines, croissant et supercroissant.
Cependant pour le prénom Augustine, nous n'avons pas trouvé d'explications.


# Sources

- [Problème du sac à dos](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos)
- [Merkle–Hellman knapsack cryptosystem](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem)
- APPLICATIONS DE L’ALGORITHME LLL EN CRYPTOGRAPHIE par Abderrahmane Nitaj