<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import landingPage from './components/landing.vue'
import auth from './components/auth-components/auth.vue'
import panel from './components/panel.vue'

export default {
  name: 'App',
  components: {
    'landing-component': landingPage,
    'auth-component': auth,
    'panel-component': panel
  }
}
</script>

<style lang="scss">

@import '@/css/custom.scss';

@mixin input{
    background-color: transparent;
    border: none;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

</style>