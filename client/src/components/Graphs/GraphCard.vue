<template>
  <div>
    <GChart :type="typeOne" :data="data" :options="options" />
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
};
</script>

<style>
</style>