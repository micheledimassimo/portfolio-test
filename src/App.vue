<script>
// 1) Importazione dei componenti della pagina (Header, Footer, Menu - visibili ovunque)
import AppFooter from './components/AppFooter.vue';

export default {
  // 2) Dichiarazione dei componenti fissi globali
  components: {
    AppFooter
  }
}
</script>

<template>
  <div class="portfolio-app">

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
// Import all of Bootstrap's CSS
@import "bootstrap/scss/bootstrap";

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
</style>
