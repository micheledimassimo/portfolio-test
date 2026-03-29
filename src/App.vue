<script>
import AppFooter from './components/AppFooter.vue';

export default {
  components: {
    AppFooter
  },
  data() {
    return {
      theme: 'light' // Default to light theme
    }
  },
  mounted() {
    // Attempt to load from localStorage or keep default light
    const savedTheme = localStorage.getItem('portfolio-theme');
    if (savedTheme) {
      this.theme = savedTheme;
    }
    this.applyTheme();
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === 'light' ? 'dark' : 'light';
      localStorage.setItem('portfolio-theme', this.theme);
      this.applyTheme();
    },
    applyTheme() {
      document.documentElement.setAttribute('data-theme', this.theme);
    }
  }
}
</script>

<template>
  <div class="portfolio-app">

    <!-- Theme Toggle Button -->
    <button @click="toggleTheme" class="theme-toggle" :aria-label="'Switch to ' + (theme === 'light' ? 'dark' : 'light') + ' theme'">
      <i v-if="theme === 'light'" class="devicon-devicon-plain" style="font-size: 1.2rem; transform: rotate(180deg);">🌙</i>
      <i v-else class="devicon-devicon-plain" style="font-size: 1.2rem;">☀️</i>
    </button>

    <!-- Area in cui iniettare dinamicamente le pagine caricate dal Vue Router -->
    <main>
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- Footer Component visibile su tutte le pagine -->
    <AppFooter />
  </div>
</template>

<style lang="scss">
@use 'assets/scss/main' as *;

/* Semplici transizioni di routing per un feeling più moderno */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.theme-toggle {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 1000;
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: blur(10px);
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--text-light);
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), background 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.theme-toggle:hover {
  transform: scale(1.15) rotate(10deg);
  background: var(--accent-primary);
  color: #fff;
}
</style>
