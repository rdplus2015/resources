
# CSS
- **Introduction**
- **Useful links**

---

## Inheritance of Properties

- Property values can be inherited from parent elements.
- Example: If the `body` is set to red, all children elements will inherit the red color.

## Selector Priority and Specificity

- Default styles are applied in CSS unless overridden.
- When there are conflicting styles, the more specific rule takes precedence:
  - **Specificity**: ID > Class > Element
  - Example: An ID selector overrides a class selector, which in turn overrides an element selector.
  - In CSS, inline styles take precedence over internal styles, which themselves take precedence over external styles.

### Tips and note :

- **A parent is simply an element that contains another element, regardless of whether it is a block or inline element. and the contained element is the child**
- Override general rules with more specific ones.
- Use a simple depth level for readability and performance.
- A simple depth level makes it easy to overwrite a ruler because the latter is less specific



## **Useful Links**

- [Mozilla Developer Network (MDN) CSS Documentation](https://developer.mozilla.org/fr/docs/Web/CSS)
  - [CSS Documentation on DevDocs](https://devdocs.io/css)

- [Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
  - [Flexbox Froggy](https://flexboxfroggy.com/#fr)

- [Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
  - [CSS Grid Garden](https://cssgridgarden.com/#fr)
  - [Mozilla Developers CSS Grid Playground](https://mozilladevelopers.github.io/playground/css-grid/)

- [Media queries](https://web.dev/learn/design/media-queries)

- [FontSquirrel](https://www.fontsquirrel.com/)
  - [Transfonter](https://transfonter.org/) - Convert font formats.

- [Can I Use](https://caniuse.com/)
  - [Autoprefixer](https://autoprefixer.github.io/)
  - [Preset Env](https://preset-env.cssdb.org/) - Generate code for older browsers using CSS variables.

- [Meyerweb Reset CSS](https://meyerweb.com/eric/tools/css/reset/) - A popular CSS reset stylesheet.
- [Mini Reset CSS](https://jgthms.com/minireset.css/) - A minimal CSS reset.
- [Normalize CSS](https://necolas.github.io/normalize.css/) - A modern CSS reset.
- [Animista](https://animista.net/play/basic/slide-fwd) - Animasta
