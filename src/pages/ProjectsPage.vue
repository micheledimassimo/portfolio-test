<script>
export default {
  name: 'ProjectsPage',
  data() {
    return {
      projects: [
        {
          id: 1,
          title: 'E-Commerce Platform',
          description: 'A full-stack e-commerce solution with cart and checkout functionalities built with Vue and PHP.',
          techStack: ['Vue.js', 'PHP', 'MySQL', 'CSS3'],
          link: '#'
        },
        {
          id: 2,
          title: 'Admin Dashboard',
          description: 'A responsive, dark-mode analytics dashboard showing real-time metrics.',
          techStack: ['HTML5', 'CSS3', 'JavaScript', 'Vite'],
          link: '#'
        },
        {
          id: 3,
          title: 'Social Web App',
          description: 'A real-time scalable social network prototype handling thousands of queries.',
          techStack: ['Vue.js', 'JavaScript', 'MySQL', 'Git'],
          link: '#'
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
        
        <div class="back-action">
          <router-link to="/" class="btn btn-outline">
             Back to Home
          </router-link>
        </div>
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
            <a :href="project.link" class="btn btn-primary btn-sm">View Project</a>
          </div>
        </div>
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
  
  // Decorative blur
  &::after {
    content: '';
    position: absolute;
    top: 20%;
    left: 20%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(6, 182, 212, 0.15) 0%, rgba(79, 70, 229, 0) 70%);
    border-radius: 50%;
    filter: blur(60px);
    z-index: -1;
  }
}

.page-header {
  margin-bottom: 60px;
}

.page-title {
  font-size: 3.5rem;
}

.back-action {
  margin-top: 30px;
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
  
  &:hover {
    transform: translateY(-10px);
    border-color: rgba(255, 255, 255, 0.15);
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
  background: rgba(0, 0, 0, 0.2);
  border-top: 1px solid rgba(255, 255, 255, 0.05);
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
