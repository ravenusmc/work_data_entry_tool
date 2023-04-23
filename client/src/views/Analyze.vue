<template>
  <div>
    <section>
      <div class='static-graphs'>
        <ActionsByCount />
        <ActionsByRecruitType />
        <LegalAuthority />
        <StackedGraph />
      </div>
      <br/>
      <div>
        <AnalyzeForm/>
      </div>
      <div class='dynamic-graphs'>
        <ActionsByIeNumber/>
        <RecruitActionsGraph/>
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
import RecruitActionsGraph from "@/components/Graphs/RecruitActionsGraph.vue";
import StackedGraph from "@/components/Graphs/StackedGraph.vue";
import AnalyzeForm from "@/components/graphForms/AnalyzeForm.vue";

export default {
  name: "Analyze",
  components: {
    ActionsByCount,
    ActionsByRecruitType,
    StackedGraph,
    AnalyzeForm,
    ActionsByIeNumber,
    LegalAuthority,
    RecruitActionsGraph,
  },
};
</script>

<style scoped>
.static-graphs {
  margin: 5% 5% 0 5%;
  display: grid; 
  grid-template-columns: 1fr 1fr;
  border-bottom: 2px solid black;
}

.dynamic-graphs {
  margin: 5% 5% 0 5%;
  display: grid; 
  grid-template-columns: 1fr 1fr;
}
</style>