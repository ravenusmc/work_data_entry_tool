<template>
  <div>
    <Modal
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
import Modal from "@/components/drilldown/Modal.vue";
import { GChart } from "vue-google-charts";

export default {
  name: "Graphs",
  props: ["typeOne", "data", "options"],
  components: {
    Modal,
    GChart,
  },
  data() {
    return {
      modalTitle: "",
      showModal: false,
      chartEvents: {
        select: () => {
          this.modalTitle = "Drill Down Data for ";
          // console.log(this.data) // This will show you the data
          const chart = this.$refs.gChart.chartObject;
          let selectedGraph = chart.ga;
          const selection = chart.getSelection()[0];
          // I need to add one to the row because the first row contains the
          // column headers.
          let row = selection.row + 1;
          // This pulls out the specific date from the element that the user
          // clicked on
          let selectedData = this.data[row][0];
          const payload = {
            selectedData,
          };
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