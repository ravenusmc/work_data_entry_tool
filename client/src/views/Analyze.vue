<template>
  <div>
    <!--
			Types of graphs:

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
      <div>
        <ActionsByCount />
        <ActionsByRecruitType />
      </div>
      <div>
        <AnalyzeForm/>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ActionsByCount from "@/components/Graphs/ActionsByCount.vue";
import ActionsByRecruitType from "@/components/Graphs/ActionsByRecruitType.vue";
import AnalyzeForm from "@/components/graphForms/AnalyzeForm.vue";

export default {
  name: "Analyze",
  components: {
    ActionsByCount,
    ActionsByRecruitType,
    AnalyzeForm,
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
  align-items: center;
}
</style>