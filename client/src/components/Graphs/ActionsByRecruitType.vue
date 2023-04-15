<template>
  <div>
    <Graphs
      :typeOne="typeOne"
      :data="recruitTypes"
      :options="chartOptionsOne"
    />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Graphs from "@/components/Graphs/Graphs.vue";

export default {
  name: "ActionsByRecruitType",
  components: {
    Graphs,
  },
  computed: {
    ...mapGetters("analyze", ["recruitTypes"]),
  },
  data() {
    return {
      typeOne: "PieChart",
      chartOptionsOne: {
        title: "Actions by Recruit Type",
        legend: { position: "top" },
        colors: ["#50A8F1", "#F19950"],
        height: 500,
        width: 649,
        vAxes: {
          0: { title: "Count" },
        },
        hAxes: {
          0: { title: "Recruit Type" },
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