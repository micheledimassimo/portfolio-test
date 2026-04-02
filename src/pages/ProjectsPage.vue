<script>
export default {
  name: 'ProjectsPage',
  data() {
    return {
      projects: [
        {
          id: 1,
          title: 'Sams SRL - W.I.P',
          description: 'Realizzazione del sito web per Sams SRL. Sito multipagina e multilinuga, gestito dinamicamente con Vue Router',
          techStack: ['Vue.js', 'Vue Router', 'Scss'],
          link: '#'
        },
        /* {
          id: 2,
          title: 'Admin Dashboard',
          description: 'A responsive, dark-mode analytics dashboard showing real-time metrics.',
          techStack: ['HTML5', 'CSS3', 'JavaScript', 'Vite'],
          link: '#'
        }, */
        {
          id: 3,
          title: 'DeliveBoo',
          description: 'Progetto di gruppo per la creazione di una piattaforma di delivery di cibo a domicilio. ',
          techStack: ['Vue.js', 'Laravel', 'MySQL', 'PHP', 'Axios'],
          link: 'https://github.com/micheledimassimo/deliveboo-frontend-team3/blob/main/README.md'
        }
      ]
    }
  }
}
</script>

<template>
  <div class="projects-page">
    <div class="container-custom">
      <div class="page-header text-center">
        <h1 class="page-title">My <span class="text-gradient">Projects</span></h1>
        <p class="text-muted">A collection of my recent work and explorations.</p>
      </div>

      <div class="projects-grid">
        <div 
          v-for="project in projects" 
          :key="project.id" 
          class="project-card glass-panel"
        >
          <div class="project-content">
            <h3 class="project-title">{{ project.title }}</h3>
            <p class="project-desc text-muted">{{ project.description }}</p>
            
            <div class="tech-tags">
              <span v-for="tag in project.techStack" :key="tag" class="tag">
                {{ tag }}
              </span>
            </div>
          </div>
          <div class="project-footer">
            <a :href="project.link" target="blank" class="btn btn-primary btn-sm">View Project</a>
          </div>
        </div>
      </div>
      <div class="back-action">
          <router-link to="/" class="btn btn-outline">
             Back to Home
          </router-link>
        </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use '../assets/scss/partials/variables' as *;

.projects-page {
  padding-top: 150px;
  padding-bottom: 100px;
  min-height: 80vh;
  position: relative;
}

.page-header {
  margin-bottom: 60px;
}

.page-title {
  font-size: 3.5rem;
}

.back-action {
  margin-top: 30px;
  text-align: center;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 30px;
}

.project-card {
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-10px);
    border-color: rgba(35, 146, 235, 0.5);
    box-shadow: 0 10px 30px rgba(35, 146, 235, 0.2);
  }
}

.project-content {
  padding: 30px;
  flex-grow: 1;
}

.project-title {
  font-size: 1.5rem;
  margin-bottom: 15px;
  color: $text-light;
}

.project-desc {
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 20px;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tag {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: $accent-secondary;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.project-footer {
  padding: 20px 30px;
  background: transparent;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.btn-outline {
  background: transparent;
  color: $text-light;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 10px 24px;
  border-radius: 8px;
  text-decoration: none;
  display: inline-block;
  transition: all 0.3s ease;
  
  &:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.4);
  }
}

.btn-primary.btn-sm {
  padding: 8px 16px;
  font-size: 0.9rem;
  width: 100%;
  text-align: center;
  display: block;
}
</style>
