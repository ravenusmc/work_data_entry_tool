<template>
  <div class="container">
    <header
      role="banner"
      class="jumbotron-style jumbotron jumbotron-fluid text-center jumbotron-image"
    >
      <div class="jumbotron_div_area">
        <h1 class="display-3 title-font">Work Data Tool</h1>
        <p class="lead title-font">An Easier Way to Enter Data</p>
      </div>
    </header>

    <section class="paragraph-section">
      <p>
        At my job we have this spreadsheet where we have to enter in data. Now,
        that would seem easy. The issue is that multiple people are in the
        spreadsheet at any given time making edits and that drastically slows
        everything down in it. Imagine entering data, hitting tab, waiting 3-5
        seconds, moving over to the next column, enter data and the same process
        repeating over and over again. I got sick of this. I started to imagine
        what a new work flow would be like so I decided to create this site.
      </p>
      <p>
        The purpose of this site would be to speed up my workflow with entering
        data. It would also give a manager the ability to see statitics on the
        data that people have entered in the form of graphs. Now, saying all of
        that, I don't believe that I'll ever actually use this website at my
        job. I work for the government and there are probably way to many
        security and other requirements for me to get this site used. I may
        mention it though and see where things go from there.
      </p>
    </section>

    <section class="sign-in-area">
      <div class="sign-in-div">
        <p>
          <a>
            <router-link v-if="!loginFlag" to="/login">Login | </router-link>
          </a>
          <a>
            <router-link v-if="!loginFlag" to="/sign_up">Sign up</router-link>
          </a>
            <router-link @click.native="onClick" v-if="loginFlag" to="">Log Out</router-link>
          </a>
        </p>
      </div>
    </section>

    <section class="picture-section">
      <div class="image-1 image"></div>
      <div class="image-2 image"></div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "HomeView",
  computed: {
    ...mapGetters("common", ["loginFlag"]),
  },
  methods: {
    ...mapActions(["common/logout"]),
    onClick() {
      this.$store.dispatch("common/logout");
    },
  },
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
  border-radius: 10px;
}

.paragraph-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.sign-in-area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 30px;
}

.sign-in-div {
  width: 200px;
  height: 200px;
  line-height: 200px;
  border-radius: 50%;
  font-size: 20px;
  color: #fff;
  text-align: center;
  background: #343a40;
}

a {
  color: white;
}

.picture-section {
  display: grid;
  grid-gap: 30px;
  grid-template-columns: 1fr 1fr;
  height: 500px;
  margin: 30px;
}

.image {
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}

.image-1 {
  background-image: url("../assets/images/image-1.jpg");
}

.image-2 {
  background-image: url("../assets/images/image-2.jpg");
}
</style>
