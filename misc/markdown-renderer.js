var MarkdownIt = require('markdown-it'),
    mk = require('markdown-it-math-katex'),
    hljs = require('highlight.js'),
    footnote = require('markdown-it-footnote'),
    mila = require('markdown-it-link-attributes');

var md = new MarkdownIt({
    html: false, // No html = no xss
    linkify: true,
    highlight: function (string, language) {
        var langExec = "";
        if (language) {
            langExec = ' exec-target" data-lang="' + language;
        }
        if (language && hljs.getLanguage(language)) {
            try {
                return '<pre class="hljs' + langExec + '"><code>' +
                    hljs.highlight(language, string, true).value +
                    '</code></pre>';
            } catch (__) {
                return '<div style="font-size: 3rem; color: red; font-weight: 300">Error Rendering</div>';
            }
        }

        return '<pre class="hljs' + langExec + '"><code>' + md.utils.escapeHtml(string) + '</code></pre>';
    }
}).use(mk, {
    throwOnError: false,
    errorColor: "#F00"
}).use(mila, {
    attrs: {
        target: '_blank',
        rel: 'nofollow'
    }
}).use(footnote);

module.exports = md;
