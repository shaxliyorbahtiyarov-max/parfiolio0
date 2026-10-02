// Accordion (Projects va Interests): sichqoncha olib borilsa yoki bosilsa kengayadi
document.querySelectorAll('.acc').forEach(acc => {
  acc.querySelectorAll('.pn').forEach(p => {
    const open = () => { acc.querySelectorAll('.pn').forEach(x => x.classList.remove('on')); p.classList.add('on'); };
    p.addEventListener('mouseenter', () => matchMedia('(hover:hover)').matches && open());
    p.addEventListener('click', open);
  });
});

// Aloqa formasi: pochta dasturini ochadi
const form = document.getElementById('form');
form.addEventListener('submit', e => {
  e.preventDefault();
  const to = form.dataset.email;
  location.href = `mailto:${to}?subject=${encodeURIComponent('Message from ' + form.n.value)}&body=${encodeURIComponent(form.m.value + '\n\n' + form.e.value)}`;
});

// Silliq scroll (Lenis) + parallax (GSAP)
gsap.registerPlugin(ScrollTrigger);
const lenis = new Lenis();
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add(t => lenis.raf(t * 1000));
gsap.ticker.lagSmoothing(0);
// Menyu va havolalar: bosilganda silliq scroll bilan o'tadi
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const id = a.getAttribute('href');
    if (id === '#') return;                    // Resume kabi bo'sh havolalar
    const el = document.querySelector(id);
    if (!el) return;
    e.preventDefault();
    lenis.scrollTo(el, {
      duration: 1.6,                           // sekinroq/tezroq qilish uchun o'zgartiring
      easing: t => 1 - Math.pow(1 - t, 4)      // oxirida sekinlashadi
    });
  });
});

// 1) Kirish animatsiyasi: faqat ichki elementlarga
gsap.fromTo('.portrait > *',
  { opacity: 0, y: 60 },
  { opacity: 1, y: 0, duration: 1.4, ease: 'power3.out' });
gsap.fromTo('.left > *, .right > *',
  { opacity: 0, y: 40 },
  { opacity: 1, y: 0, duration: 1.2, delay: .3, stagger: .08, ease: 'power3.out' });

// 2) Scroll animatsiyasi: boshlang'ich qiymatlar aniq yozilgan
const st = { trigger: '#hero', start: 'top top', end: 'bottom top', scrub: true };
gsap.fromTo('.left, .right', { yPercent: 0, opacity: 1 }, { yPercent: -25, opacity: .2, ease: 'none', scrollTrigger: st });
gsap.fromTo('.bg-word',      { yPercent: 0 },             { yPercent: -40, ease: 'none', scrollTrigger: st });
gsap.fromTo('.portrait',     { yPercent: 0, scale: 1 },   { yPercent: 8, scale: 1.05, ease: 'none', scrollTrigger: st });
gsap.fromTo('.scroll',       { opacity: 1 },              { opacity: 0, ease: 'none', scrollTrigger: { ...st, end: '20% top' } });
// Menyuda joriy bo'lim belgilanadi
const links = [...document.querySelectorAll('#menu a')];
['hero', 'about', 'projects', 'interests', 'contact'].forEach(id => {
  const el = document.getElementById(id);
  new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) links.forEach(a => a.classList.toggle('on', a.hash === '#' + id));
  }), { rootMargin: '-45% 0px -50% 0px' }).observe(el);
});

// About rasmi: scroll qilib kelganda chapdan o'ngga siljib chiqadi (hero animatsiyasiga aloqasi yo'q)
gsap.fromTo('.about .pic img',
  { x: -180, opacity: 0 },
  { x: 0, opacity: 1, duration: 1.4, ease: 'power3.out',
    scrollTrigger: { trigger: '#about', start: 'top 65%', toggleActions: 'play none none reverse' } });
