<script>
import HeroSection from '../components/HeroSection.vue';
import SkillsSection from '../components/SkillsSection.vue';

export default {
  name: 'HomePage',
  components: {
    HeroSection,
    SkillsSection
  }
}
</script>

<template>
  <div class="home-page">
    <HeroSection />
    <SkillsSection />
  </div>
</template>
