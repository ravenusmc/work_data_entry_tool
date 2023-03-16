<template>
  <div>
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
import { GChart } from "vue-google-charts";
export default {
  name: "GraphCard",
  props: ["typeOne", "data", "options"],
  components: {
    GChart,
  },
  data() {
    return {
      chartEvents: {
        select: () => {
          // this.modalTitle = "Drill Down Data for ";
          console.log(this.data) // This will show you the data
          // const chart = this.$refs.gChart.chartObject;
          // const selection = chart.getSelection()[0];
          // I need to add one to the row because the first row contains the
          // column headers.
          // let row = selection.row + 1;
          // This pulls out the specific date from the element that the user
          // clicked on
          // let date = this.data[row][0];
          // const payload = {
          //   date,
          // };
          // this.fetchDrillDownData({ payload });
          // this.showModal = true;
          // this.modalTitle = `${this.modalTitle} ${date}`;
        },
      }, // End Chart Events
    }
  }
};
</script>

<style>
</style>