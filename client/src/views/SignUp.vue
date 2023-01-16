<template>
  <div>
    <div class="signup-heading">
      <h1>Sign Up</h1>
    </div>

    <section class="container">
      <div class="form-div">
        <form @submit="signup">
          <div class="form-group form-inline">
            <label for="firstname">First Name:</label>
            <input
              type="text"
              name="firstname"
              v-model="firstName"
              class="form-control"
              id="firstname"
              placeholder="Enter First Name"
            />
          </div>
          <div class="form-group form-inline">
            <label for="lastName">Last Name:</label>
            <input
              type="text"
              name="lastName"
              class="form-control"
              id="lastName"
              v-model="lastName"
              placeholder="Enter Last Name"
            />
          </div>
          <div class="form-group form-inline">
            <label for="email">Email:</label>
            <input
              type="text"
              name="email"
              class="form-control"
              id="email"
               v-model="email"
              placeholder="Enter Email"
            />
          </div>
          <div class="form-group form-inline">
            <label for="ienumber">IE Number:</label>
            <input
              type="text"
              name="ienumber"
              class="form-control"
              id="ieNumber"
              v-model="ieNumber"
              placeholder="Enter IE Number"
            />
          </div>
          <div class="form-group form-inline">
            <label for="exampleInputPassword1">Password: </label>
            <input
              type="password"
              name="password"
              class="form-control"
              id="exampleInputPassword1"
              v-model="password"
              placeholder="Password"
            />
          </div>
          <div class="form-group form-inline">
            <label for="exampleInputPassword2">Confirm Password:</label>
            <input
              type="password"
              name="password2"
              class="form-control"
              id="exampleInputPassword2"
              v-model="confirmPassword"
              placeholder="Confirm Password"
            />
          </div>

          <button
            type="submit"
            name="login"
            class="btn btn-primary form-submit-btn"
          >
            Submit
          </button>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Form",
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      ieNumber: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    ...mapActions("common", ["setUpUser"]),
    signup(evt) {
      evt.preventDefault();
      if (this.firstName === "") {
        alert("First name must be entered");
      } else if (this.lastName === "") {
        alert("Last name must be entered");
      } else if (this.email === "") {
        alert("Email must be entered");
      } else if (this.ieNumber === "") {
        alert("User name must be entered");
      } else if (this.password === "") {
        alert("Password must be entered");
      } else if (this.password !== this.confirmPassword) {
        alert("Passwords must be the same");
      } else if (this.password.length < 6) {
        alert("Password must be at least 6 characters long");
      } else {
        const payload = {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          ieNumber: this.ieNumber,
          password: this.password,
          confirmPassword: this.confirmPassword,
        };
        this.setUpUser({ payload });
      }
    },
  },
};
</script>

<style scoped>
.signup-heading {
  margin-top: 30px;
}

.form-div {
  display: flex;
  justify-content: center;
  align-items: center;
}

form {
  border: 2px solid black;
  border-radius: 15px;
  margin: 50px;
  padding: 20px;
  background-color: #2da5e5;
}
</style>