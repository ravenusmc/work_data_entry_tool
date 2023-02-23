<template>
  <div>
    <!--
			Types of graphs: 
			Graph of all action types - shows number done
			-Graph by IE Number that shows actions that the individual did 
			Graph that shows legal authority types 
			Graph that shows recurit actions vs non recruit actions - overall and then by individual 
		-->
    <ActionsByCount/>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ActionsByCount from "@/components/Graphs/ActionsByCount.vue";


export default {
  name: "Analyze",
  components: {
    ActionsByCount,
  },
  mounted() {
    console.log("MOUNTED");
  },
};
</script>

<style scoped>
</style>