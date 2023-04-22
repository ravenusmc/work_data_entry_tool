<template>
  <div>
    <AnalyzeGraphs
      :typeOne="typeOne"
      :data="actionsByIenumber"
      :options="chartOptionsOne"
    />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import AnalyzeGraphs from "@/components/Graphs/AnalyzeGraphs.vue";

export default {
  name: "ActionsByCount",
  components: {
    AnalyzeGraphs,
  },
  computed: {
    ...mapGetters("analyze", ["actionsByIenumber"]),
  },
  data() {
    return {
      typeOne: "ColumnChart",
      chartOptionsOne: {
        title: "Actions by IeNumber",
        legend: { position: "top" },
        colors: ["#50A8F1"],
        height: 500,
        width: 652,
        vAxes: {
          0: { title: "Count" },
        },
        hAxes: {
          0: { title: "Nature of Action" },
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

<style>
</style>