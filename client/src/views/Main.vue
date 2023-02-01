<template>
  <div>
    I need to make two forms - one for if the action is found and one if it's
    not. Use two seperate components for this. -The first form will ask the user
    to enter an action number -if it's found then one form will be used -If the
    action number is not found then another form will be returned..
    <form @submit="findAction">
      <div class="field">
        <label for="exampleInputPassword2">Action Number:</label>
        <input
          class="input is-primary is-rounded"
          type="name"
          v-model="actionNumber"
          placeholder="Action Number"
        />
      </div>
      <div class="button-div">
        <button class="btn btn-primary form-submit-btn">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Main",
  // computed: {
  //   ...mapGetters("common", ["userNotFound", "passwordNoMatch"]),
  // },
  data() {
    return {
      actionNumber: "",
    };
  },
  methods: {
    ...mapActions("data", ["locateAction"]),
    findAction(evt) {
      evt.preventDefault();
      const payload = {
        actionNumber: this.actionNumber,
      };
      this.locateAction({ payload });
    },
  },
};
</script>