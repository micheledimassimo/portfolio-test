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
          I build modern, scalable, and stunning web experiences. From crafting pixel-perfect interfaces to architecting robust backends, I bring ideas to life through code.
        </p>
        <div class="hero-actions">
          <router-link to="/projects" class="btn btn-primary btn-glow">View My Work</router-link>
          <a href="#contact" class="btn btn-outline">Let's Talk</a>
        </div>
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
  
  // Decorative background blob
  &::before {
    content: '';
    position: absolute;
    top: -100px;
    right: -100px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(79, 70, 229, 0.4) 0%, rgba(6, 182, 212, 0) 70%);
    border-radius: 50%;
    filter: blur(60px);
    z-index: -1;
    animation: blob-float 10s infinite alternate;
  }
}

.hero-content {
  width: 100%;
  display: flex;
  justify-content: flex-start;
}

.hero-text {
  max-width: 650px;
  padding: 50px;
  text-align: left;
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
  background: linear-gradient(135deg, $accent-primary, $accent-secondary);
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
  color: $text-light;
  border: 1px solid rgba(255, 255, 255, 0.2);
  
  &:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.4);
    transform: translateY(-2px);
  }
}

@keyframes blob-float {
  0% { transform: translate(0, 0) scale(1); }
  100% { transform: translate(-30px, 50px) scale(1.1); }
}

@media (max-width: 768px) {
  .hero-text {
    padding: 30px;
  }
  .title {
    font-size: 3rem;
  }
}
</style>
