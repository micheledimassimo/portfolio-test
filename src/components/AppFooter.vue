<script>
export default {
  name: "AppFooter",
  computed: {
    currentYear() {
      return new Date().getFullYear()
    }
  }
}
</script>

<template>
  <footer class="app-footer">
    <div class="container-custom content-wrapper">
      <div class="footer-brand">
        <h3>Michele Di Massimo</h3>
        <p class="text-muted">Full Stack Developer building digital experiences.</p>
      </div>
      
      <div class="footer-socials">
        <a href="#" class="social-link" title="GitHub"><i class="fa-brands fa-github"></i></a>
        <a href="#" class="social-link" title="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
        <a href="#" class="social-link" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
      </div>
    </div>
    
    <div class="footer-bottom text-muted">
      <p>&copy; {{ currentYear }} Michele Di Massimo. All Rights Reserved.</p>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
@use '../assets/scss/partials/variables' as *;

.app-footer {
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  padding: 60px 0 20px 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.4), transparent);
}

.content-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 30px;
  margin-bottom: 40px;
}

.footer-brand {
  h3 {
    margin-bottom: 5px;
  }
  p {
    margin-bottom: 0;
    font-size: 0.95rem;
  }
}

.footer-socials {
  display: flex;
  gap: 15px;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-light);
  text-decoration: none;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  
  &:hover {
    background: $accent-primary;
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(79, 70, 229, 0.4);
  }
}

.footer-bottom {
  text-align: center;
  font-size: 0.85rem;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

@media (max-width: 768px) {
  .content-wrapper {
    flex-direction: column;
    text-align: center;
    justify-content: center;
  }
}
</style>
