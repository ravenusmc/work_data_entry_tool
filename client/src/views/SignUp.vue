<template>
  <div>

    <div class='signup-heading'>
      <h1>Sign Up</h1>
    </div>

    <section class="container">
      <div class="form-div">
        <form>
          <div class="form-group form-inline">
            <label for="firstname">First Name:</label>
            <input
              type="text"
              name="firstname"
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
              placeholder="Enter Email"
            />
          </div>
          <div class="form-group form-inline">
            <label for="ienumber">IE Number:</label>
            <input
              type="text"
              name="ienumber"
              class="form-control"
              id="username"
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
	background-color: #2DA5E5;
}
</style>