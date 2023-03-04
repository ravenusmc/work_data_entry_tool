<template>
  <div>
    <!--
			Types of graphs:
			Graph that shows recurit actions vs non recruit actionsby individual
        -Allow user to select individual ie number 
    
		-->
    <section>
      <h1>Static Graphs</h1>
      <div class='static-graphs'>
        <ActionsByCount />
        <ActionsByRecruitType />
        <LegalAuthority />
      </div>
      <br/>
      <div>
        <AnalyzeForm/>
      </div>
      <h1>Dynamic Graphs</h1>
      <div>
        <ActionsByIeNumber/>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ActionsByCount from "@/components/Graphs/ActionsByCount.vue";
import ActionsByRecruitType from "@/components/Graphs/ActionsByRecruitType.vue";
import ActionsByIeNumber from "@/components/Graphs/ActionsByIeNumber.vue";
import LegalAuthority from "@/components/Graphs/LegalAuthority.vue";
import AnalyzeForm from "@/components/graphForms/AnalyzeForm.vue";

export default {
  name: "Analyze",
  components: {
    ActionsByCount,
    ActionsByRecruitType,
    AnalyzeForm,
    ActionsByIeNumber,
    LegalAuthority,
  },
  mounted() {
    console.log("MOUNTED");
  },
};
</script>

<style scoped>
section {
  /* display: flex;
  justify-content: center;
  align-items: center; */
}

.static-graphs {
  margin: 5% 5% 0 5%;
  display: grid; 
  grid-template-columns: 1fr 1fr;
  border-bottom: 2px solid black;
}
</style>