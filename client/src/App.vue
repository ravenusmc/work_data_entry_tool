<template>
  <div id="app">
    <Navbar />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/generic/Navbar.vue";
import Footer from "@/components/generic/Footer.vue";

export default {
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}

html,
body {
  min-height: 100vh;
}

#app {
  display: grid;
  grid-template-rows: auto 1fr auto;
  text-align: center;
  /* min-height: 100vh; */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
