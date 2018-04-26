# Django + VueJs
This is a test project, it's goal is to find how far Djang and VueJs can be combined.

## Statuse
Succeeded by Linking **Vue.js** file in **django** HTML template.

## Possibilities

+ Using **VueJs** in a single HTML page.
+ Using **VueJs** in all extended pages.
+ Using delimiters without overriding **Django's**. `delimiters: ['[[', ']]']`
+ Importing **Vue's** components using [http-vue-loader](https://www.npmjs.com/package/http-vue-loader). `components: { 'vue-component': httpVueLoader({% static 'components/component.vue' %})}`
+ Using components and delimiters in other **Django's** Templates.

## Under Testing

* Passing variables from **Django** to **VueJs**.
* Passing variables from **VueJs** to **Django**.

## Information

- python >= 3.5
- Django 2.0.4
- VueJs 2.5.17
- http-vue-loader 1.2.4