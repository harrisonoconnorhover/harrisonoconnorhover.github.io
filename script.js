const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const revealEntries = document.querySelectorAll('[data-reveal]');

if (!prefersReducedMotion && 'IntersectionObserver' in window) {
  document.documentElement.classList.add('reveal-enabled');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;

      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, {
    threshold: 0.14,
    rootMargin: '0px 0px -8% 0px',
  });

  revealEntries.forEach((entry) => observer.observe(entry));
}
