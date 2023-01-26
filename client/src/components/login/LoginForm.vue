<template>
  <div>
    <section>
      <div class="form-area">
        <div class="form-input-area">
          <h2 class="center signup-title title-size font">Login</h2>
          <h1 v-if="userNotFound" class="center login-problem">
            User is not found, Please
            <a
              ><router-link class="alert" to="/sign_up"
                >sign up.</router-link
              ></a
            >
          </h1>
          <h1 v-if="passwordNoMatch" class="center login-problem alert">
            Password is Invalid
          </h1>
          <form @submit="login">
            <div class="field">
              <input
                class="input is-primary is-rounded"
                type="name"
                v-model="userName"
                placeholder="UserName"
              />
            </div>
            <div class="field">
              <input
                class="input is-primary is-rounded"
                type="password"
                v-model="password"
                placeholder="Password"
              />
            </div>
            <div class="button-div">
              <button class="btn btn-success">Explore</button>
            </div>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Form",
  computed: {
    ...mapGetters("common", ["userNotFound", "passwordNoMatch"]),
  },
  data() {
    return {
      userName: "",
      password: "",
    };
  },
  methods: {
    ...mapActions("common", ["loginUser"]),
    login(evt) {
      evt.preventDefault();
      const payload = {
        userName: this.userName,
        password: this.password,
      };
      this.loginUser({ payload });
    },
  },
};
</script>

<style scoped>
section {
  /* height: 95vh;
  margin: 3%;
  background-image: url("../../assets/images/login.jpg");
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: center; */
}
.signup-title {
  text-transform: uppercase;
  font-weight: bold;
  color: white;
}
.login-problem {
  font-size: 10px;
  color: white;
}
.form-area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.form-input-area {
  background-color: rgb(0, 0, 0, 0.8);
  padding: 15px;
  border-radius: 12%;
}
.button-div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
button {
  margin-top: 10px;
}
@media only all and (max-width: 900px) {
  section {
    margin-top: -100px;
  }
}
</style>