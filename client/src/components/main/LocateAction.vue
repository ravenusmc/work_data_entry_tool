<template>
  <div>
    <form class="location-action-form" @submit="findAction">
      <!-- <div class='button-div'> -->
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
      <div class="btn-div" v-if="actionFound || actionNotFound">
        <button
          @click.prevent="hideForm"
          type="submit"
          name="login"
          class="btn btn-warning"
        >
          Hide Form
        </button>
      </div>
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
  computed: {
    ...mapGetters("data", ["actionFound", "actionNotFound"]),
  },
  methods: {
    ...mapActions("data", ["locateAction", "hideAddActionsForm"]),
    findAction(evt) {
      evt.preventDefault();
      const payload = {
        actionNumber: this.actionNumber,
      };
      this.locateAction({ payload });
    },
    hideForm(evt) {
      evt.preventDefault();
      this.hideAddActionsForm();
    },
  },
};
</script>

<style scoped>
.location-action-form {
  margin-top: 50px;
}

.btn-div {
  margin-top: 10px;
}
</style>