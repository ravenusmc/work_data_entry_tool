<template>
  <div>
    <form class="location-action-form" @submit="findAction">
      <div class="field">
        <label for="exampleInputPassword2">Action Number:</label>
        <input
          class="input is-primary is-rounded"
          type="name"
          v-model="actionNumber"
          placeholder="Action Number"
        />
      </div>
      <div v-if="!actionFound" class="button-div">
        <button class="btn btn-primary form-submit-btn">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "LocateAction",
  computed: {
    ...mapGetters("data", ["actionFound"]),
  },
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

<style scoped>
.location-action-form {
  margin-top: 50px;
}
</style>