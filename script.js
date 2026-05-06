// Typed text effect
const roles = [
  'Web Developer',
  'Laravel Engineer',
  'Python Data Scientist',
  'Astro Enthusiast',
  'ERP Developer',
];

let roleIdx = 0, charIdx = 0, isDeleting = false;
const typedEl = document.getElementById('typed');

function type() {
  const current = roles[roleIdx];

  if (isDeleting) {
    charIdx--;
    typedEl.textContent = current.slice(0, charIdx);
    if (charIdx === 0) {
      isDeleting = false;
      roleIdx = (roleIdx + 1) % roles.length;
      setTimeout(type, 350);
      return;
    }
    setTimeout(type, 50);
  } else {
    typedEl.textContent = current.slice(0, charIdx);
    charIdx++;
    if (charIdx > current.length) {
      isDeleting = true;
      setTimeout(type, 2000);
      return;
    }
    setTimeout(type, 95);
  }
}
type();

// Navbar scroll
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
});

// Hamburger menu
const hamburger = document.getElementById('hamburger');
const navMobile = document.getElementById('navMobile');
hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('open');
  navMobile.classList.toggle('open');
});
navMobile.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    hamburger.classList.remove('open');
    navMobile.classList.remove('open');
  });
});

// Intersection Observer — reveal + skill bars
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('visible');

    // animate skill bars inside this element
    entry.target.querySelectorAll('.skill-fill').forEach(bar => {
      bar.classList.add('animated');
    });

    observer.unobserve(entry.target);
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal, .skill-card, .project-card, .contact-card, .about-grid').forEach(el => {
  el.classList.add('reveal');
  observer.observe(el);
});

// Active nav link on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 100) current = sec.id;
  });
  navLinks.forEach(a => {
    a.style.color = a.getAttribute('href') === `#${current}` ? 'var(--white)' : '';
  });
});
