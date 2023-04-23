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
import { mapGetters, mapActions } from "vuex";
import AnalyzeModal from "@/components/drilldown/AnalyzeModal.vue";
import { GChart } from "vue-google-charts";

export default {
  name: "AnalyzeGraphs",
  props: ["typeOne", "data", "options"],
  components: {
    AnalyzeModal,
    GChart,
  },
  computed: {
    ...mapGetters("analyze", ["selectedIENumber"]),
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
          let selectedDataTwo = ''
          let columnType = ''
          let columnTypeOne = ''
          let columnTypeTwo = ''
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
          if (selectedGraph === 650) {
            columnType = 'Authority'
          }
          if (selectedGraph === 651) {
            let column = selection.column
            selectedDataTwo = this.data[0][column]
            columnTypeOne = 'NOA'
            columnTypeTwo = 'Processor_ieNumber'
            const payload = {
              selectedData,
              selectedDataTwo,
              columnTypeOne,
              columnTypeTwo
            };
             this.fetchDrillDownData({ payload });
          }
          if (selectedGraph === 652) {
            const payload = {
              columnType:'NOA',
              selectedData,
              needsIENUMBER: true, 
            };
             this.fetchDrillDownData({ payload });
          }
          if ((selectedGraph != 651) && (selectedGraph != 652)) {
            console.log("HEREND")
            const payload = {
              columnType,
              selectedData,
            };
            this.fetchDrillDownData({ payload });
          }
          // this.showModal = true;
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