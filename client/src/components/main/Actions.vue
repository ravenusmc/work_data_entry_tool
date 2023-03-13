<template>
<div>
	<h1>Welcome {{ userObject.first_name }}, here are your Actions:</h1>
	<!-- 
		Goal: Need to display actions. If the user submits an action to actions then display 
		those. If it goes to a missing action form, pull those. 

		-Allow user to see both actions and missing actions on their demand 
		-Allow

	-->
	
</div>
</template>
	
<script>
import { mapGetters, mapActions } from "vuex";

export default {
	name: "Actions",
	  computed: {
    ...mapGetters("session", ["userObject",]),
	},
	  methods: {
    ...mapActions("data", ["getSpecificActionsByUser",]),
    submitAction() {
      const payload = {
        action_number: this.actionNumber,
      };
      this.submitMissingActionToDatabase({ payload });
    },
  },
	mounted() {
		  const payload = {
        action_number: 7,
      };
		this.getSpecificActionsByUser({ payload });
  },
}
</script>

<style scoped>

</style>