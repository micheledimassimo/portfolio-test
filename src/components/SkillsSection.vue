<script>
export default {
  name: "SkillsSection",
  data() {
    return {
      skills: [
        { name: 'HTML5', icon: 'devicon-html5-plain colored' },
        { name: 'CSS3', icon: 'devicon-css3-plain colored' },
        { name: 'JavaScript', icon: 'devicon-javascript-plain colored' },
        { name: 'Bootstrap', icon: 'devicon-bootstrap-plain colored' },
        { name: 'Vue.js', icon: 'devicon-vuejs-plain colored' },
        { name: 'PHP', icon: 'devicon-php-plain colored' },
        { name: 'Laravel', icon: 'devicon-laravel-original colored' },
        { name: 'MySQL', icon: 'devicon-mysql-plain colored' },
        { name: 'Vite', icon: 'devicon-vitejs-plain colored' },
        { name: 'Git', icon: 'devicon-git-plain colored' },
        { name: 'GitHub', icon: 'devicon-github-original' }
      ]
    }
  }
}
</script>

<template>
  <section class="skills-section" id="skills">
    <div class="container-custom text-center">
      <h2 class="section-title">My <span class="text-gradient">Tech Stack</span></h2>
      <p class="section-subtitle text-muted">Technologies I work with daily</p>
      
      <div class="skills-grid">
        <div 
          v-for="(skill, index) in skills" 
          :key="index" 
          class="skill-card glass-panel"
        >
          <div class="icon-wrapper">
            <i :class="skill.icon"></i>
          </div>
          <h4 class="skill-name">{{ skill.name }}</h4>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@use '../assets/scss/partials/variables' as *;

.skills-section {
  position: relative;
  
  &::before {
    content: '';
    position: absolute;
    bottom: -50px;
    left: -100px;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(236, 72, 153, 0.2) 0%, rgba(236, 72, 153, 0) 70%);
    border-radius: 50%;
    filter: blur(60px);
    z-index: -1;
  }
}

.section-title {
  font-size: 3rem;
}

.section-subtitle {
  font-size: 1.1rem;
  margin-bottom: 4rem;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 30px;
  max-width: 1000px;
  margin: 0 auto;
}

.skill-card {
  padding: 30px 15px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  
  &:hover {
    transform: translateY(-10px) scale(1.05);
    border-color: rgba(255,255,255, 0.2);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4), inset 0 0 20px rgba(255,255,255,0.05);
    
    .icon-wrapper {
      transform: scale(1.15) rotate(5deg);
    }
  }
}

.icon-wrapper {
  font-size: 4.5rem;
  margin-bottom: 15px;
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  
  /* Ensure Github icon is visible in dark mode */
  i[class*="github"] {
    color: #ffffff;
  }
}

.skill-name {
  font-size: 1.1rem;
  margin-bottom: 0;
  color: $text-light;
  font-weight: 500;
}
</style>
