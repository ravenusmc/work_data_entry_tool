<template>
<div>
    <GChart
      :type="typeOne"
      :data="stackedGraph"
      :options="chartOptionsOne"
    />
</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import GraphCard from "@/components/Graphs/GraphCard.vue";

export default {
  name: "StackedGraph",
  components: {
    GraphCard,
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
				width: 650,
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