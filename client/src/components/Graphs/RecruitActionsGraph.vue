<template>
  <div>
    <h1>Recruit</h1>
    <GChart :type="typeOne" :data="recruitActionCount" :options="chartOptionsOne" />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import GraphCard from "@/components/Graphs/GraphCard.vue";

export default {
  name: "RecruitActionsGraph",
  components: {
    GraphCard,
  },
  computed: {
    ...mapGetters("analyze", ["recruitActionCount"]),
  },
  data() {
    return {
      typeOne: "PieChart",
      chartOptionsOne: {
        title: "All Actions by Legal Authority",
        legend: { position: "top" },
        colors: ["#50A8F1", "#F19950"],
        height: 500,
        width: 650,
        vAxes: {
          0: { title: "Count" },
        },
        hAxes: {
          0: { title: "Recruit Action" },
        },
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    };
  },
};
</script>

<style scoped>
</style>
