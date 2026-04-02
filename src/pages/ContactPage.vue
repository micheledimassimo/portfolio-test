<script>
export default {
  name: "ContactPage"
}
</script>

<template>
  <section class="contact-page">
    <div class="container-custom">
      <div class="page-header text-center">
        <h2 class="title">Let's <span class="text-gradient">Connect</span></h2>
        <p class="description text-muted">Hai un progetto in mente o semplicemente vuoi fare due chiacchiere? Scrivimi o scarica il mio curriculum.</p>
      </div>

      <div class="contact-grid">
        <!-- Contact Info Card -->
        <div class="contact-card glass-panel">
          <h3>Mettiamoci in contatto</h3>
          <p class="text-muted">Sentiti libero di contattarmi per collaborazioni, progetti freelance o per bere un caffè virtuale!</p>
          
          <ul class="contact-list">
            <li>
              <i class="fa-solid fa-envelope"></i>
              <a href="mailto:devbymichele@gmail.com">devbymichele@gmail.com</a>
            </li>
            
            <li>
              <i class="fa-solid fa-location-dot"></i>
              <span>Milano, Italia (Remote)</span>
            </li>
          </ul>

          <div class="social-links-contact">
            <a href="https://github.com/micheledimassimo" target="_blank" class="social-badge" title="GitHub"><i class="fa-brands fa-github"></i> GitHub</a>
            <a href="https://www.linkedin.com/in/micheledimassimo" target="_blank" class="social-badge" title="LinkedIn"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>
            <a href="https://www.instagram.com/devbymichele" target="_blank" class="social-badge" title="Instagram"><i class="fa-brands fa-instagram"></i> Instagram</a>
          </div>
        </div>

        <!-- Resume Card -->
        <div class="resume-card glass-panel text-center">
          <div class="resume-icon">
            <i class="fa-regular fa-file-pdf"></i>
          </div>
          <h3>Curriculum Vitae</h3>
          <p class="text-muted">Esplora la mia esperienza lavorativa, accademica e le mie competenze tecniche complete.</p>
          <!-- Il tag # funge da placeholder, potrai inserire il link al PDF definitivo quando sarà pronto -->
          <a href="cv/Michele-Di-Massimo.pdf" target="_blank" class="btn btn-primary btn-glow mt-3">
            <i class="fa-solid fa-download"></i> Scarica CV
          </a>
        </div>
      </div>
      <div class="back-action">
          <router-link to="/" class="btn btn-outline">
             Back to Home
          </router-link>
        </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@use '../assets/scss/partials/variables' as *;

.contact-page {
  padding-top: 150px;
  padding-bottom: 100px;
  min-height: 80vh;
  position: relative;
}

.page-header {
  margin-bottom: 60px;
  
  .title {
    font-size: 3.5rem;
  }
}

.contact-grid {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 40px;
  max-width: 1000px;
  margin: 0 auto;
}

.contact-card, .resume-card {
  padding: 40px;
  
  h3 {
    font-size: 2rem;
    margin-bottom: 15px;
  }
}

.contact-list {
  list-style: none;
  padding: 0;
  margin: 30px 0;
  
  li {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 20px;
    font-size: 1.1rem;
    color: var(--text-light);
    
    i {
      color: var(--accent-primary);
      font-size: 1.5rem;
      width: 30px;
      text-align: center;
    }
    
    a {
      color: var(--text-light);
      text-decoration: none;
      transition: color 0.3s ease;
      
      &:hover {
        color: var(--accent-primary);
      }
    }
  }
}

.social-links-contact {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-top: 20px;
}

.social-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 30px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--glass-border);
  color: var(--text-light);
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  
  &:hover {
    background: var(--accent-primary);
    color: #fff;
    transform: translateY(-3px);
  }
}

.resume-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  
  .resume-icon {
    font-size: 5rem;
    color: var(--accent-primary);
    margin-bottom: 20px;
  }
  
  .btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 12px 25px;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
    border: none;
    font-family: 'Inter', sans-serif;
    cursor: pointer;
  }

  .btn-primary {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
    color: #fff;
    
    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 20px rgba(35, 146, 235, 0.4);
      color: #fff;
    }
  }
  
  .mt-3 {
    margin-top: 1.5rem;
  }
}
.back-action {
  margin-top: 30px;
  text-align: center;
}

@media (max-width: 768px) {
  .contact-grid {
    grid-template-columns: 1fr;
  }
  
  .page-header .title {
    font-size: 2.5rem;
  }
}
</style>
