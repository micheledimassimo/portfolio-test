<script>
// 1) Importazione dei componenti della pagina
import HeroSection from './components/HeroSection.vue';
import SkillsSection from './components/SkillsSection.vue';
import AppFooter from './components/AppFooter.vue';

export default {
  // 2) Dichiarazione dei componenti
  components: {
    HeroSection,
    SkillsSection,
    AppFooter
  }
}
</script>

<template>
  <div class="portfolio-app">
    <!-- NavBar can be added later, for now just the main sections -->
    
    <main>
      <!-- Hero Section Component -->
      <HeroSection />

      <!-- Skills Section Component -->
      <SkillsSection />
    </main>

    <!-- Footer Component -->
    <AppFooter />
  </div>
</template>

<style lang="scss">
@use 'assets/scss/main' as *;
// Import all of Bootstrap's CSS
@import "bootstrap/scss/bootstrap";
</style>
