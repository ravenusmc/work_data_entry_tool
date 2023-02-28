<template>
  <div>
    <h1>FORM</h1>
    <form @submit="submitOptions">
      <select v-model="ieNumber">
        <option v-for="ieNumber in ieNumbers" :key="ieNumber">
          {{ ieNumber }}
        </option>
      </select>
      <select v-model="selectedAction">
        <option v-for="action in typeOfAction" :key="action">
          {{ action }}
        </option>
      </select>
      <div class="button-div">
        <button class="btn btn-primary form-submit-btn">Submit</button>
      </div>
    </form>
  </div>
</template>
	
<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "AnalyzeForm",
  data() {
    return {
			ieNumber: "ie7046",
			selectedAction: "101",
    };
  },
  computed: {
    ...mapGetters("analyze", ["ieNumbers", "typeOfAction"]),
  },
  methods: {
    ...mapActions("analyze", [""]),
    submitOptions(evt) {
      evt.preventDefault();
      const payload = {
        ieNumber: this.ieNumber,
        selectedAction: this.selectedAction,
      };
      console.log(payload);
      // this.loginUser({ payload });
    },
  },
};
</script>

<style scoped>
</style>