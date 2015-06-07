ffSlides
========

A collection of all my slides.

http://slides.ferrai.tk

### Requirements
* git

### How to use

* Clone the repo somewhere
* Then:
```bash
cd my-slides
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
git clone https://github.com/isagalaev/highlight.js.git
```