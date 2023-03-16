<template>
  <div>
    <h1>Welcome {{ userObject.first_name }}, here are your Actions:</h1>
    <!-- 
		Goal: Need to display actions. If the user submits an action to actions then display 
		those. If it goes to a missing action form, pull those. 

		-Allow user to see both actions and missing actions on their demand 
		-Allow

	-->
    <div class="table-area">
      <GraphCard
        :typeOne="typeOne"
        :data="actionsByUser"
        :options="chartOptionsOne"
      />
    </div>
  </div>
</template>
	
<script>
import GraphCard from "@/components/Graphs/GraphCard.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Actions",
  components: {
    GraphCard,
  },
  computed: {
    ...mapGetters("session", ["userObject", "actionsByUser"]),
    ...mapGetters("data", ["actionsByUser"]),
  },
  methods: {
    ...mapActions("data", ["getSpecificActionsByUser"]),
    submitAction() {
      const payload = {
        action_number: this.actionNumber,
      };
      this.submitMissingActionToDatabase({ payload });
    },
  },
  data() {
    return {
      division_name: "Bottoms",
      typeOne: "Table",
      chartOptionsOne: {
        title: "All Actions by User",
        legend: { position: "top" },
        colors: ["#f24867"],
        height: 500,
        allowHTML: true,
        animation: {
          duration: 1000,
          easing: "linear",
        },
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    };
  },
  mounted() {
    const payload = {
      action_number: 7,
    };
    this.getSpecificActionsByUser({ payload });
  },
};
</script>

<style scoped>
.table-area {
  border: 2px solid black;
}
</style>