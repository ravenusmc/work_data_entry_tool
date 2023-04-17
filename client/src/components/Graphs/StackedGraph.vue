<template>
<div>
    <AnalyzeGraphs
      :typeOne="typeOne"
      :data="stackedGraph"
      :options="chartOptionsOne"
    />
</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import AnalyzeGraphs from "@/components/Graphs/AnalyzeGraphs.vue";

export default {
  name: "StackedGraph",
  components: {
    AnalyzeGraphs,
  },
  computed: {
    ...mapGetters("analyze", ["stackedGraph"]),
  },
  data() {
    return {
      typeOne: "ColumnChart",
      chartOptionsOne: {
        title: "All Actions by NOA and Processor",
        legend: { position: "top" },
        height: 500,
				width: 651,
				isStacked: true,
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