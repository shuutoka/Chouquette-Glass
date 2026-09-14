# Audit de l'ancien Chouquette Glass

Audit réalisé lors de la migration vers Chouquette Glass 2.0 (14 septembre 2026).

## État du dépôt historique

Le dépôt contient environ **1 858 lignes de CSS** actives/archivées, réparties entre le thème principal, la police et plusieurs fichiers d'animations.

### 1. Principal problème : classes Discord générées

L'ancien code référence **343 sélecteurs ressemblant à des classes générées par Discord** (`.chat__52833`, `.panels__58331`, `.message__80c10`, etc.). Ces suffixes ne constituent pas une API stable : Discord les remplace lors de mises à jour internes.

Une mise à jour « chercher/remplacer tous les hashes » fonctionnerait seulement jusqu'au prochain remaniement. La v2 préfère donc :

1. les variables/design tokens de Discord ;
2. les sélecteurs structurels stables (`li[id^="chat-messages-"]`) ;
3. les préfixes sémantiques (`[class*="channelTextArea_"]`) lorsqu'un composant précis doit être ciblé ;
4. les classes `.bd-*` uniquement pour l'interface BetterDiscord, car elles appartiennent à BetterDiscord et non au bundle Discord.

### 2. Variables absentes ou héritées implicitement

Plusieurs variables sont utilisées sans être définies par Chouquette Glass lui-même :

- `--messages-radius`
- `--messages-padding`
- `--color-secondary-light`
- `--card-color`

D'autres variables non définies dans le dépôt étaient probablement des variables natives de Discord à l'époque et ont depuis changé de nom.

La v2 définit ses propres variables `--cg-*` et fournit quelques alias pour les anciens noms utiles.

### 3. Erreur de syntaxe réelle

Dans l'ancienne section **Server Boost**, le commentaire de la déclaration `border` se terminait par `*//` :

```css
border: 1px solid var(--color-secondary); /*panels color*//
```

Le parseur CSS signale cette zone comme déclaration incorrecte. Cette section historique reste archivée, mais elle n'est plus chargée par la v2.

### 4. Imports et animations devenus fragiles

Les anciens fichiers d'animations ciblent eux aussi des hashes Discord précis. Ils sont donc archivés et leurs comportements utiles ont été réécrits dans le cœur v2 :

- survol des boutons du compositeur ;
- halo des mentions ;
- cartes « activité des amis » ;
- rôles/profil ;
- éléments sélectionnés.

Le clignotement permanent des mentions est conservé comme option mais désactivé par défaut afin de réduire la distraction visuelle.

### 5. Fonds d'écran distants

Le preset `dust` utilisait une URL Discord CDN comportant une signature et une date d'expiration de 2023. Il ne pouvait donc pas constituer une ressource permanente. Il a été retiré des presets actifs.

Le fond historique « Minsk » est conservé comme valeur par défaut, mais il reste recommandé d'utiliser une URL HTTPS que tu contrôles (par exemple un fichier placé dans le dépôt GitHub et servi par GitHub Pages).

### 6. Lisibilité

La police historique **Baloo Bhaijaan 2** est conservée. La v2 ajoute des réglages très modérés uniquement au corps des messages :

- interligne `1.42` ;
- espacement des lettres `0.012em` ;
- espacement des mots `0.025em`.

Ces valeurs sont exposées comme variables et peuvent être adaptées sans réécrire les sélecteurs.

### 7. Mouvement et accessibilité

La v2 respecte `prefers-reduced-motion`. Les animations sont automatiquement neutralisées lorsque le système de l'utilisateur demande une réduction des mouvements.

## Architecture v2

- `ChouquetteGlass.theme.css` : fichier final à placer dans BetterDiscord.
- `cg2/chouquette-core.css` : source réellement éditable.
- `tools/build-theme.py` : reconstruit le fichier final.
- `tools/audit_css.py` : refuse les nouveaux sélecteurs Discord avec hash exact.
- `.github/workflows/css-check.yml` : vérification automatique à chaque push/PR.
- `legacy-original/` : copie intacte de l'ancien dépôt CSS pour comparaison.
- `cg2/theme.css` et `cg2/cgtheme.css` : shims de compatibilité pour les anciennes URL GitHub Pages.

## Dépendance moderne

Chouquette Glass 2.0 importe la couche **Translucence 2.x** de CapnKitten pour la compatibilité générale du verre/transparence avec les surfaces Discord actuelles. Chouquette Glass conserve ensuite sa propre palette, sa typographie, ses réglages de lisibilité et ses effets.

Cela évite de recopier et de maintenir plusieurs centaines de sélecteurs internes Discord dans ce dépôt.
