<template>
  <div class="container">
    <header
      role="banner"
      class="jumbotron-style jumbotron jumbotron-fluid text-center jumbotron-image"
    >
      <div class='jumbotron_div_area'>
        <h1 class="display-3 title-font">Work Data Tool</h1>
        <p class="lead title-font">An Easier Way to Enter Data</p>
      </div>
    </header>

    <section>
      <p>
        This site is a basic security system site. I got the idea for it one day
        when I briefly worked as a security guard waiting for my federal job to
        start. There was this monitor up on the wall that showed all of the
        buildings on site. If there was an issue, like a fire alarm, the
        building that would have the issue would start to light up. I want to
        recreate a similar thing with this.
      </p>
      <p>
        The true purpose of this is to build something in PHP again and to use
        some vanilla JavaScript. Both of these tools I've not used in quite some
        time. I've just been doing so many python and vue.js projects one after
        another that it may be almost a year since I've done a PHP project -
        time really fly's by!
      </p>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "HomeView",
};
</script>

<style lang="css" scoped>
.jumbotron-image {
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url("../assets/images/work_entry.jpg");
  height: 500px;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}

.jumbotron_div_area {
  border: 2px solid black;
  color: white;
  background-color: rgba(0, 0, 0, 0.6);
  text-transform: uppercase;
  padding: 15px;
}

section {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

</style>
