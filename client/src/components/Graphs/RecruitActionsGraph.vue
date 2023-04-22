<template>
  <div>
    <h1>Recruit</h1>
    <AnalyzeGraphs
      :typeOne="typeOne"
      :data="recruitActionCount"
      :options="chartOptionsOne"
    />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import AnalyzeGraphs from "@/components/Graphs/AnalyzeGraphs.vue";

export default {
  name: "RecruitActionsGraph",
  components: {
    AnalyzeGraphs,
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
        width: 653,
        vAxes: {
          0: { title: "Count" },
        },
        hAxes: {
          0: { title: "Recruit Action" },
        },
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
};
</script>

<style scoped>
</style>
