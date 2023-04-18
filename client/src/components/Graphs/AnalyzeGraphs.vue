<template>
  <div>
    <AnalyzeModal
      :showModal="showModal"
      :modalTitle="modalTitle"
      @close-modal="update"
    />
    <GChart
      :type="typeOne"
      :data="data"
      :options="options"
      :events="chartEvents"
      ref="gChart"
    />
  </div>
</template>

<script>
import { mapActions } from "vuex";
import AnalyzeModal from "@/components/drilldown/AnalyzeModal.vue";
import { GChart } from "vue-google-charts";

export default {
  name: "AnalyzeGraphs",
  props: ["typeOne", "data", "options"],
  components: {
    AnalyzeModal,
    GChart,
  },
  data() {
    return {
      modalTitle: "",
      showModal: false,
      chartEvents: {
        select: () => {
          this.modalTitle = "Drill Down Data";
          // console.log(this.data) // This will show you the data
          const chart = this.$refs.gChart.chartObject;
          // This gets the specific graph that has been clicked on
          // There maybe a better way to do this. 
          let selectedGraph = chart.ga;
          const selection = chart.getSelection()[0];
          // I need to add one to the row because the first row contains the
          // column headers.
          let row = selection.row + 1;
          let columnType = ''
          // This pulls out the specific date from the element that the user
          // clicked on
          let selectedData = this.data[row][0];
          if (selectedGraph === 648) {
            columnType = 'NOA'
          }
          if (selectedGraph === 649) {
            if (selectedData === 'True') {
              selectedData = true 
            }else {
              selectedData = false
            }
            columnType = 'recruit_action'
          }
          const payload = {
            columnType,
            selectedData,
          };
          console.log(typeof payload['selectedData'])
          this.fetchDrillDownData({ payload });
          this.showModal = true;
        },
      }, // End Chart Events
    };
  },
  methods: {
    ...mapActions("analyze", ["fetchDrillDownData"]),
    update(close) {
      this.showModal = close;
    },
  }, // End of Methods
};
</script>

<style>
</style>