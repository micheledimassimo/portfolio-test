<script>
export default {
  name: "HeroSection"
}
</script>

<template>
  <section class="hero-section">
    <div class="container-custom hero-content">
      <div class="hero-text glass-panel">
        <h2 class="greeting">Hi, I'm <span class="text-gradient">Michele</span></h2>
        <h1 class="title">Full Stack Developer</h1>
        <p class="description text-muted">
          Realizzo siti web moderni, responsivi e ottimizzati per i motori di ricerca. Dalla progettazione all'implementazione, mi occupo di ogni aspetto dello sviluppo web.
          <br>
          Hai bisogno di un sito web? Contattami e realizzeremo insieme il tuo progetto.
        </p>
        
        <div class="hero-actions">
          <router-link to="/projects" class="btn btn-primary btn-glow">I Miei Lavori</router-link>
          <router-link to="/contact" class="btn btn-outline">Contattami</router-link>
        </div>
      </div>
      
      <!-- Sezione Immagine Profilo/Logo -->
      <div class="hero-image-wrapper">
        <div class="hero-logo"></div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@use '../assets/scss/partials/variables' as *;

.hero-section {
  min-height: 80vh;
  display: flex;
  align-items: center;
  position: relative;
  overflow: hidden;
  padding-top: 150px;
  padding-bottom: 50px;
}

.hero-content {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
}

.hero-text {
  flex: 1;
  max-width: 650px;
  padding: 50px;
  text-align: left;
  box-shadow: 0 10px 40px rgba(35, 146, 235, 0.35); /* Azzurro palette ombra */
}

.hero-image-wrapper {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-logo {
  width: 100%;
  max-width: 450px;
  height: 450px;
  background-image: var(--hero-logo-img);
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  transition: background-image 0.4s ease, transform 0.4s ease;
  animation: float 6s ease-in-out infinite;
}

.greeting {
  font-size: 1.5rem;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 1rem;
}

.title {
  font-size: 4.5rem;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  background: linear-gradient(135deg, var(--text-light), var(--accent-primary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.description {
  font-size: 1.15rem;
  line-height: 1.6;
  margin-bottom: 2.5rem;
}

.hero-actions {
  display: flex;
  gap: 15px;
}

.btn {
  padding: 14px 30px;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
}

.btn-primary {
  background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
  color: #fff;
  border: none;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(79, 70, 229, 0.4);
    color: #fff;
  }
}

.btn-outline {
  background: transparent;
  color: var(--text-light);
  border: 1px solid var(--text-light);
  opacity: 0.8;
  
  &:hover {
    opacity: 1;
    background: rgba(255, 255, 255, 0.05);
    transform: translateY(-2px);
  }
}

@keyframes blob-float {
  0% { transform: translate(0, 0) scale(1); }
  100% { transform: translate(-30px, 50px) scale(1.1); }
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-15px); }
  100% { transform: translateY(0px); }
}

@media (max-width: 992px) {
  .hero-content {
    flex-direction: column;
    text-align: center;
    
  }
  
  .hero-image-wrapper {
    order: -1;
    width: 100%;
    margin-bottom: 20px;
  }
  
  .hero-text {
    text-align: center;
    padding: 30px;
  }
  
  .hero-actions {
    justify-content: center;
  }
  
  .title {
    font-size: 3rem;
  }
  
  .hero-logo {
    height: 300px;
  }
}
</style>
