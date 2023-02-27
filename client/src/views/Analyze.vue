<template>
  <div>
    <!--
			Types of graphs:
      Static:
        -Pie Chart of recruit actions versus non recruit 

      Dynamic:   
			-Graph by IE Number that shows actions that the individual did 
        -This will have to have the ability to select an IE Number 
			Graph that shows legal authority types
        -The will have to allow the user to select the type of action  
			Graph that shows recurit actions vs non recruit actionsby individual
        -Allow user to select individual ie number 
      
      FORM:
        Select IE Number
        SELECT TYPE OF ACTION
		-->
    <section>
      <ActionsByCount/>
      <ActionsByRecruitType/>
    </section>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ActionsByCount from "@/components/Graphs/ActionsByCount.vue";
import ActionsByRecruitType from "@/components/Graphs/ActionsByRecruitType.vue";


export default {
  name: "Analyze",
  components: {
    ActionsByCount,
    ActionsByRecruitType,
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