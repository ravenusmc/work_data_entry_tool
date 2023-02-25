<template>
  <div>
    <!--
			Types of graphs: 
			-Graph by IE Number that shows actions that the individual did 
			Graph that shows legal authority types 
			Graph that shows recurit actions vs non recruit actions - overall and then by individual 
		-->
    <section>
      <ActionsByCount/>
    </section>
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
section {
  border: 2px solid red;
  display: flex; 
  justify-content: center;
  align-items: center;;
}
</style>