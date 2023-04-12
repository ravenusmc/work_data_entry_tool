<template>
  <div>
    <Graphs
      :typeOne="typeOne"
      :data="allActionsByCount"
      :options="chartOptionsOne"
    />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import Graphs from "@/components/Graphs/Graphs.vue";

export default {
  name: "ActionsByCount",
  components: {
    Graphs,
  },
  computed: {
    ...mapGetters("analyze", ["allActionsByCount"]),
  },
  data() {
    return {
      typeOne: "ColumnChart",
      chartOptionsOne: {
        title: "All Actions by NOA",
        legend: { position: "top" },
        colors: ["#50A8F1"],
        height: 500,
        width: 650,
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