// Tier 1 reveals. Progressive enhancement: with no JavaScript the panels are
// hidden and the buttons are inert, so nothing sensitive is exposed by accident.
(function () {
  'use strict';
  document.querySelectorAll('.reveal__button').forEach(function (button) {
    var panel = document.getElementById(button.getAttribute('aria-controls'));
    if (!panel) return;
    button.addEventListener('click', function () {
      var open = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!open));
      panel.hidden = open;
    });
  });
})();
