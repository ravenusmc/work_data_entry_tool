<template>
  <div>
    <form @submit="submitAction">
      <div class="form-group form-inline">
        <label for="firstname">Recruit Action:</label>
        <select v-model="selectedValueRecruitAction">
          <option disabled value="">Please select one</option>
          <option v-for="item in recruit_action" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <!-- <div class="form-group form-inline">
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
      </div> -->

      <button
        type="submit"
        name="login"
        class="btn btn-primary form-submit-btn"
      >
        Submit
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: "ActionsForm",
  data() {
    return {
			recruit_action: ["True", "False"],
			selectedValueRecruitAction: null,
      action_number: "", // Get in payload?
      NOA: "",
      Authority: "",
      Processor_ieNumber: "", // Get from user
      Date_Receieved: "",
      Returned: "",
      Keyed: "",
      Applied: "",
    };
  },
  methods: {
    // ...mapActions("data", ["setUpUser"]),
    submitAction(evt) {
      evt.preventDefault();
      console.log(this.selectedValueRecruitAction);
      // if (this.firstName === "") {
      //   alert("First name must be entered");
      // } else if (this.lastName === "") {
      //   alert("Last name must be entered");
      // } else if (this.email === "") {
      //   alert("Email must be entered");
      // } else if (this.ieNumber === "") {
      //   alert("User name must be entered");
      // } else if (this.password === "") {
      //   alert("Password must be entered");
      // } else if (this.password !== this.confirmPassword) {
      //   alert("Passwords must be the same");
      // } else if (this.password.length < 6) {
      //   alert("Password must be at least 6 characters long");
      // } else {
      //   const payload = {
      //     firstName: this.firstName,
      //     lastName: this.lastName,
      //     email: this.email,
      //     ieNumber: this.ieNumber,
      //     password: this.password,
      //     confirmPassword: this.confirmPassword,
      //   };
      //   this.setUpUser({ payload });
      // }
    },
  },
};
</script>