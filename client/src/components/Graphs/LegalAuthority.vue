<template>
<div>
    <AnalyzeGraphs
      :typeOne="typeOne"
      :data="legalAuthority"
      :options="chartOptionsOne"
    />
</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import AnalyzeGraphs from "@/components/Graphs/AnalyzeGraphs.vue";

export default {
	name: "LegalAuthority",
  components: {
    AnalyzeGraphs,
  },
  computed: {
    ...mapGetters("analyze", ["legalAuthority"]),
  },
  data() {
    return {
      typeOne: "ColumnChart",
      chartOptionsOne: {
        title: "All Actions by Legal Authority",
        legend: { position: "top" },
        colors: ["#50A8F1"],
        height: 500,
        width: 650,
        vAxes: {
          0: { title: "Count" },
        },
        hAxes: {
          0: { title: "Legal Authority" },
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
	