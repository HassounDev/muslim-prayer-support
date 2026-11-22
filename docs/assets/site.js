// Small enhancements only; every page works without JavaScript.
(function () {
  // FAQ: a link to one question (faq.html#adhan-30s) opens it.
  function openTarget() {
    var id = location.hash.slice(1);
    var el = id && document.getElementById(id);
    if (el && el.tagName === "DETAILS") {
      el.open = true;
      el.scrollIntoView();
    }
  }
  // Language selector: stay on the same question or section.
  function keepHash() {
    document.querySelectorAll("a[data-lang-link]").forEach(function (a) {
      a.hash = location.hash;
    });
  }
  function update() {
    openTarget();
    if (location.hash) keepHash();
  }
  window.addEventListener("hashchange", update);
  update();
})();
