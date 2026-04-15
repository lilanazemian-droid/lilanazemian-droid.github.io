/* nav.js — SPA navigation: keeps audio, snow and menu alive across pages */
(function () {
  'use strict';

  var _busy = false;

  function navigate(url, push) {
    if (_busy) return;
    _busy = true;

    fetch(url)
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })
      .then(function (html) {
        var doc = new DOMParser().parseFromString(html, 'text/html');

        // 1. Tear down current page's resources (e.g. cancel Damavand rAF)
        if (typeof window._pageCleanup === 'function') {
          window._pageCleanup();
          window._pageCleanup = null;
        }

        // 2. Swap page-specific <style id="page-style">
        var pStyle = document.getElementById('page-style');
        var nStyle = doc.getElementById('page-style');
        if (pStyle && nStyle) pStyle.textContent = nStyle.textContent;

        // 3. Swap <main>
        var pMain = document.querySelector('main');
        var nMain = doc.querySelector('main');
        if (pMain && nMain) {
          pMain.innerHTML = nMain.innerHTML;
          var ns = nMain.getAttribute('style');
          if (ns) pMain.setAttribute('style', ns);
          else pMain.removeAttribute('style');
          // Re-execute any inline scripts inside the new <main>
          pMain.querySelectorAll('script').forEach(function (s) {
            var r = document.createElement('script');
            r.textContent = s.textContent;
            s.parentNode.replaceChild(r, s);
          });
        }

        // 4. Re-run page-level scripts tagged data-page (e.g. Damavand canvas)
        doc.querySelectorAll('script[data-page]').forEach(function (s) {
          var r = document.createElement('script');
          r.textContent = s.textContent;
          document.body.appendChild(r);
        });

        // 5. Update title + URL
        document.title = doc.title;
        if (push !== false) history.pushState({ url: url }, doc.title, url);

        // 6. Update active nav link
        var name = url.split('/').pop().split('?')[0] || 'index.html';
        document.querySelectorAll('.drawer nav a').forEach(function (a) {
          a.classList.toggle('active', a.getAttribute('href') === name);
        });

        // 7. Close drawer
        if (typeof closeDrawer === 'function') closeDrawer();

        _busy = false;
      })
      .catch(function () { _busy = false; location.href = url; });
  }

  // Intercept internal .html link clicks
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    if (/^(https?:|mailto:|tel:|\/\/|#)/.test(h)) return;
    if (!h.endsWith('.html')) return;
    e.preventDefault();
    navigate(h);
  }, true);

  // Browser back / forward
  window.addEventListener('popstate', function (e) {
    navigate(e.state ? e.state.url : location.href, false);
  });

  history.replaceState({ url: location.href }, document.title, location.href);
}());
